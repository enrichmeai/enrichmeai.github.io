#!/usr/bin/env python3
"""Keep each project's page in step with what that project has actually released.

Every release reaches this site: the version, every library, and the new features (CLAUDE.md
§ "Project releases"). This checks a project page against the truth:

  * the registries (Maven Central, and PyPI where the project publishes there) — what is released;
  * a checkout of the project's repository — which libraries, pip extras and capabilities exist,
    and the version on its main branch.

The page marks every fact it states, so nothing is scraped from prose. With the project's prefix
P (for example `data-culvert`):

  <span P="maven-version">0.2.0</span>     newest release on Maven Central, or "unpublished"
  <span P="pypi-version">0.1.1</span>      newest release on PyPI (projects that publish there)
  <span P="main-version">…-SNAPSHOT</span> the version on main       (projects with main_version)
  <span P="next-version">0.3.0-alpha1</span> main's version without -SNAPSHOT, the next tag
  <tr P-artifact="<artifactId>" data-state="released|unreleased"> … <span P="artifact-version">
  <code P-extra="gcp">                      one per pip extra              (projects with extras)
  <dt P-capability="BlobStorage">           one per capability interface   (projects with capabilities)
  <section P-release="0.2.0">               what's new in that release

Rules: every marker equals the truth; every library has a row and no row names a library that is
gone; extras and capabilities match exactly; the newest release has a "what's new" block; and no other
version appears on the page outside a marker or a "what's new" block, so nothing can go stale unseen.

Usage:
  tools/check-release-page.py culvert --repo ../culvert
  tools/check-release-page.py enrich-test-api --repo ../enrich-test-api
  … --dump-facts          print the gathered facts as JSON
  … --facts facts.json    offline (tests)
Exit 1 when the page is behind; 2 when the facts could not be gathered (never reported as passing).
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

PROJECTS = {
    "culvert": {
        "repo": "enrichmeai/culvert",
        "page": "culvert/index.html",
        "attr": "data-culvert",
        "group": "com.enrichmeai.culvert",
        "reactor": "data-pipeline-libraries-java/pom.xml",
        "pypi": "culvert",
        "extras": "python-culvert/pyproject.toml",
    },
    "enrich-test-api": {
        "repo": "enrichmeai/enrich-test-api",
        "page": "enrich-test-api/index.html",
        "attr": "data-eta",
        "group": "com.enrichmeai",
        "reactor": "pom.xml",
        # release.yml deploys with -pl '!test-feature': it has no main sources to publish.
        "unpublished": ["test-feature"],
        "main_version": "pom.xml",
        "capabilities": "test-core/src/main/java/com/enrichmeai/test/core/cloud/capability",
    },
}

# A release-shaped version: 0.2.0, v0.3.0-alpha1, 0.3.0-alpha1-SNAPSHOT. Two-part numbers (Python
# 3.10, Airflow 2.9.x, a 0.81 coverage figure) are not versions of the project.
VERSION = re.compile(r"(?<![\w.])v?\d+\.\d+\.\d+(?:-[A-Za-z0-9]+(?:\.[A-Za-z0-9]+)*)*(?![\w.]*\d)")


# ---------------------------------------------------------------- facts
def vkey(v: str) -> tuple:
    return tuple(int(x) if x.isdigit() else -1 for x in re.split(r"[.\-]", v))


def own_pom(pom_text: str) -> str:
    return re.sub(r"<parent>.*?</parent>", "", pom_text, flags=re.S)


def reactor_libraries(repo: Path, cfg: dict) -> list[str]:
    """Artifact ids of every published library in the reactor."""
    agg_path = repo / cfg["reactor"]
    out = []
    for module in re.findall(r"<module>([^<]+)</module>", agg_path.read_text(encoding="utf-8")):
        pom = own_pom((agg_path.parent / module / "pom.xml").read_text(encoding="utf-8"))
        artifact = re.search(r"<artifactId>([^<]+)</artifactId>", pom).group(1)
        if artifact in cfg.get("unpublished", []):
            continue
        if re.search(r"<maven\.deploy\.skip>\s*true", pom) or re.search(r"never published", pom, re.I):
            continue  # a build gate, not a library (e.g. culvert's data-pipeline-registration-audit)
        out.append(artifact)
    return out


def pip_extras(repo: Path, cfg: dict) -> list[str]:
    text = (repo / cfg["extras"]).read_text(encoding="utf-8")
    block = re.search(r"^\[project\.optional-dependencies\]\s*$(.*?)^\[", text, re.S | re.M)
    return re.findall(r"^([A-Za-z0-9_-]+)\s*=\s*\[", block.group(1), re.M) if block else []


def main_version(repo: Path, cfg: dict) -> str:
    pom = own_pom((repo / cfg["main_version"]).read_text(encoding="utf-8"))
    return re.search(r"<version>([^<]+)</version>", pom).group(1)


def capabilities(repo: Path, cfg: dict) -> list[str]:
    caps = []
    for f in sorted((repo / cfg["capabilities"]).glob("*.java")):
        if re.search(r"public\s+interface\s+\w+\s+extends\s+Capability\b", f.read_text(encoding="utf-8")):
            caps.append(f.stem)
    return caps


def fetch(url: str, attempts: int = 5) -> str | None:
    """GET a registry URL. 404 means "not published"; 429/5xx are retried with backoff."""
    for i in range(attempts):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "enrichmeai-site-release-check"})
            with urllib.request.urlopen(req, timeout=30) as r:  # noqa: S310 — fixed https URLs
                return r.read().decode("utf-8")
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            if (e.code == 429 or e.code >= 500) and i < attempts - 1:
                time.sleep(int(e.headers.get("Retry-After") or 0) or 2 ** (i + 1))
                continue
            raise
    return None


def gather(project: str, repo: Path) -> dict:
    cfg = PROJECTS[project]
    facts: dict = {"maven": {}}
    for a in reactor_libraries(repo, cfg):
        meta = fetch(f"https://repo1.maven.org/maven2/{cfg['group'].replace('.', '/')}/{a}/maven-metadata.xml")
        m = re.search(r"<release>([^<]+)</release>", meta or "")
        facts["maven"][a] = m.group(1) if m else None
    if "pypi" in cfg:
        facts["pypi_version"] = json.loads(fetch(f"https://pypi.org/pypi/{cfg['pypi']}/json") or "{}").get(
            "info", {}
        ).get("version")
    if "extras" in cfg:
        facts["extras"] = pip_extras(repo, cfg)
    if "main_version" in cfg:
        facts["main_version"] = main_version(repo, cfg)
    if "capabilities" in cfg:
        facts["capabilities"] = capabilities(repo, cfg)
    return facts


# ---------------------------------------------------------------- page
class Node:
    def __init__(self, tag: str, attrs: dict, parent: "Node | None"):
        self.tag, self.attrs, self.parent = tag, attrs, parent
        self.children: list = []

    def text(self) -> str:
        return "".join(c if isinstance(c, str) else c.text() for c in self.children)

    def walk(self):
        yield self
        for c in self.children:
            if isinstance(c, Node):
                yield from c.walk()


class Tree(HTMLParser):
    VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node("#root", {}, None)
        self.cur = self.root

    def handle_starttag(self, tag, attrs):
        node = Node(tag, {k: (v or "") for k, v in attrs}, self.cur)
        self.cur.children.append(node)
        if tag not in self.VOID:
            self.cur = node

    def handle_startendtag(self, tag, attrs):
        self.cur.children.append(Node(tag, {k: (v or "") for k, v in attrs}, self.cur))

    def handle_endtag(self, tag):
        n = self.cur
        while n is not self.root and n.tag != tag:
            n = n.parent
        if n is not self.root:
            self.cur = n.parent

    def handle_data(self, data):
        self.cur.children.append(data)


def parse(html: str) -> Node:
    t = Tree()
    t.feed(html)
    return t.root


def stray_versions(node: Node, prefix: str, out: list[str]) -> None:
    """Versions in text outside markers, "what's new" blocks, scripts and styles."""
    if node.tag in ("script", "style") or any(k.startswith(prefix) for k in node.attrs):
        return
    for c in node.children:
        if isinstance(c, str):
            out += VERSION.findall(c)
        else:
            stray_versions(c, prefix, out)


def check(html: str, facts: dict, project: str) -> list[str]:
    P = PROJECTS[project]["attr"]
    errors: list[str] = []
    root = parse(html)
    nodes = list(root.walk())

    def marks(key):
        return [n for n in nodes if n.attrs.get(P) == key]

    released = {a: v for a, v in facts["maven"].items() if v}
    maven_version = max(released.values(), key=vkey) if released else None

    # 1. version markers
    expected = {"maven-version": maven_version or "unpublished"}
    if "pypi_version" in facts:
        expected["pypi-version"] = facts["pypi_version"] or "unpublished"
    if "main_version" in facts:
        expected["main-version"] = facts["main_version"]
        expected["next-version"] = re.sub(r"-SNAPSHOT$", "", facts["main_version"])
    required = {"maven-version", "pypi-version", "main-version"}
    for key, want in expected.items():
        found = marks(key)
        if not found and key in required:
            errors.append(f'no {P}="{key}" marker on the page (the truth is {want})')
        for n in found:
            got = n.text().strip().lstrip("v") if key == "next-version" else n.text().strip()
            if got != want:
                errors.append(f'{P}="{key}" says {n.text().strip()!r}, the truth is {want}')

    # 2. libraries
    rows = {n.attrs[f"{P}-artifact"]: n for n in nodes if f"{P}-artifact" in n.attrs}
    for a, v in facts["maven"].items():
        row = rows.get(a)
        if row is None:
            errors.append(f"library {a} ({'released ' + v if v else 'unreleased'}) has no {P}-artifact row")
            continue
        state = row.attrs.get("data-state")
        shown = [n.text().strip() for n in row.walk() if n.attrs.get(P) == "artifact-version"]
        if v:
            if state != "released":
                errors.append(f'{a} is released ({v}) but its row says data-state="{state}"')
            if shown != [v]:
                errors.append(f"{a} row shows version {shown or 'none'}, Maven Central has {v}")
        else:
            if state != "unreleased":
                errors.append(f'{a} is not on Maven Central but its row says data-state="{state}"')
            if shown:
                errors.append(f"{a} is not on Maven Central but its row shows version {shown}")
    for a in sorted(set(rows) - set(facts["maven"])):
        errors.append(f"the page lists {a}, which is not a published library in the project any more")

    # 3. pip extras / 4. capabilities: exactly the set in the source
    for key, what in (("extras", "pip extra"), ("capabilities", "capability")):
        if key not in facts:
            continue
        attr = f"{P}-{key[:-1] if key == 'extras' else 'capability'}"
        on_page = {n.attrs[attr] for n in nodes if attr in n.attrs}
        for x in sorted(set(facts[key]) - on_page):
            errors.append(f"{what} {x} is missing from the page ({attr})")
        for x in sorted(on_page - set(facts[key])):
            errors.append(f"the page lists {what} {x}, which the source no longer defines")

    # 5. what's new
    newest = max(
        [v for v in (facts.get("pypi_version"), maven_version) if v], key=vkey, default=None
    )
    blocks = {n.attrs[f"{P}-release"] for n in nodes if f"{P}-release" in n.attrs}
    if newest and newest not in blocks:
        errors.append(f"no \"what's new\" block ({P}-release=\"{newest}\") for the newest release, {newest}")

    # 6. hard-coded versions
    stray: list[str] = []
    stray_versions(root, P, stray)
    for v in sorted(set(stray), key=lambda s: vkey(s.lstrip("v"))):
        errors.append(f"version {v} is hard-coded outside a {P} marker — mark it, or drop it")
    return errors


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("project", choices=sorted(PROJECTS))
    ap.add_argument("--repo", required=True, help="a checkout of the project's repository (main)")
    ap.add_argument("--facts", help="read the facts from this JSON file instead of gathering them")
    ap.add_argument("--dump-facts", action="store_true", help="print the gathered facts as JSON and exit")
    ap.add_argument("--page", help="override the page path")
    args = ap.parse_args()

    cfg = PROJECTS[args.project]
    try:
        facts = json.loads(Path(args.facts).read_text()) if args.facts else gather(args.project, Path(args.repo))
    except (OSError, urllib.error.URLError, ValueError, AttributeError) as e:
        print(f"check-release-page: could not gather the facts ({e}) — the check did NOT run", file=sys.stderr)
        return 2
    if args.dump_facts:
        print(json.dumps(facts, indent=2))
        return 0

    page = Path(args.page) if args.page else ROOT / cfg["page"]
    errors = check(page.read_text(encoding="utf-8"), facts, args.project)
    for e in errors:
        print(f"ERROR {e}")
    released = {a: v for a, v in facts["maven"].items() if v}
    summary = [
        f"Maven {max(released.values(), key=vkey) if released else 'unpublished'} "
        f"({len(released)}/{len(facts['maven'])} libraries released)"
    ]
    if "pypi_version" in facts:
        summary.insert(0, f"PyPI {facts['pypi_version']}")
    if "main_version" in facts:
        summary.append(f"main {facts['main_version']}")
    for k in ("extras", "capabilities"):
        if k in facts:
            summary.append(f"{len(facts[k])} {k}")
    print(f"check-release-page {args.project}: {' · '.join(summary)} — {len(errors)} error(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
