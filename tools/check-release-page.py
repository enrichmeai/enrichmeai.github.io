#!/usr/bin/env python3
"""Keep each project's page in step with what that project has actually released.

Every release reaches this site: the version, every library, and the new features (CLAUDE.md
§ "Project releases"). This checks a project page against the truth:

  * the registries (Maven Central, and PyPI where the project publishes there) — what is released;
  * a checkout of the project's repository — which libraries and capabilities exist, and the
    version on its main branch;
  * pip extras come from the PyPI release itself, not from main: an extra merged after the release
    is not on the page until a release ships it (CLAUDE.md § Voice: never run ahead of a release).

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

Projects that release on GitHub rather than Maven Central (kind "github": Penstock, Cistern) are
checked against their latest GitHub release instead, with two markers:

  <span P="release-version">v0.5.2</span>  the latest GitHub release (a leading "v" is ignored)
  <section P-release="0.5.2">              what's new in that release
  <… P-history>                            an earlier release named on purpose (a scan record, "since");
                                           it may not name a release newer than the latest
  <a data-link-<project>="release|history" href="…/<repo>/…/v0.5.2…">
                                           a link into the project's repository that names a version:
                                           "release" links must name the latest release, "history" an older one

Pages that repeat a project's facts (the home page, /persona/) are listed under "also": their markers
are checked against the same truth, and a version on them outside every project's markers is an error,
so the home page cannot keep an old version after the project page moves on. Markers are required
only on the project's own page.

Rules: every marker equals the truth; every released library has a row (an unreleased one may have one,
but releases are batched, so it need not), and no row names a library that is gone; extras and capabilities match exactly; the newest release has a "what's new" block; and no other
version appears on the page outside a marker or a "what's new" block, so nothing can go stale unseen.

Usage:
  tools/check-release-page.py culvert --repo ../culvert
  tools/check-release-page.py enrich-test-api --repo ../enrich-test-api
  tools/check-release-page.py penstock            (kind "github": no --repo needed)
  … --dump-facts          print the gathered facts as JSON
  … --facts facts.json    offline (tests)
Exit 1 when the page is behind; 2 when the facts could not be gathered (never reported as passing).
"""
from __future__ import annotations

import argparse
import json
import os
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
        "also": ["index.html"],
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
        "also": ["index.html"],
    },
    "penstock": {
        "repo": "enrichmeai/penstock",
        "page": "penstock/index.html",
        "attr": "data-penstock",
        "kind": "github",
        "also": ["index.html", "persona/index.html", "headworks/index.html"],
    },
    "cistern": {
        "repo": "enrichmeai/cistern",
        "page": "cistern/index.html",
        "attr": "data-cistern",
        "kind": "github",
        "also": ["index.html", "persona/index.html", "penstock/index.html", "headworks/index.html"],
    },
}
# Every project's markers, plus data-other-version for a version that is not any project's own
# (a build tool's, say), so a page states it on purpose rather than by accident.
PREFIXES = tuple(cfg["attr"] for cfg in PROJECTS.values()) + ("data-other-version",)

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
    return [norm_extra(x) for x in re.findall(r"^([A-Za-z0-9_.-]+)\s*=\s*\[", block.group(1), re.M)] if block else []


def released_extras(pypi_info: dict) -> list[str] | None:
    """The extras the latest PyPI release declares (its Provides-Extra), or None when it is not published."""
    if not pypi_info.get("version"):
        return None
    return sorted(norm_extra(x) for x in pypi_info.get("provides_extra") or [])


def norm_extra(name: str) -> str:
    """An extra's name as PEP 685 compares it: lower case, runs of -_. as one hyphen."""
    return re.sub(r"[-_.]+", "-", name).lower()


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
            headers = {"User-Agent": "enrichmeai-site-release-check"}
            if url.startswith("https://api.github.com/") and os.environ.get("GITHUB_TOKEN"):
                headers["Authorization"] = f"Bearer {os.environ['GITHUB_TOKEN']}"
            req = urllib.request.Request(url, headers=headers)
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


def gather(project: str, repo: Path | None) -> dict:
    cfg = PROJECTS[project]
    if cfg.get("kind") == "github":
        latest = json.loads(fetch(f"https://api.github.com/repos/{cfg['repo']}/releases/latest") or "{}")
        tag = latest.get("tag_name")
        if not tag:
            raise ValueError(f"{cfg['repo']} has no latest release")
        return {"release": tag.lstrip("v")}
    facts: dict = {"maven": {}}
    for a in reactor_libraries(repo, cfg):
        meta = fetch(f"https://repo1.maven.org/maven2/{cfg['group'].replace('.', '/')}/{a}/maven-metadata.xml")
        m = re.search(r"<release>([^<]+)</release>", meta or "")
        facts["maven"][a] = m.group(1) if m else None
    pypi_info: dict = {}
    if "pypi" in cfg:
        pypi_info = json.loads(fetch(f"https://pypi.org/pypi/{cfg['pypi']}/json") or "{}").get("info", {})
        facts["pypi_version"] = pypi_info.get("version")
    if "extras" in cfg:
        # The released set; main's pyproject only while nothing is on PyPI yet.
        released = released_extras(pypi_info)
        facts["extras"] = released if released is not None else pip_extras(repo, cfg)
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


def stray_versions(node: Node, prefixes: tuple, out: list[str]) -> None:
    """Versions in text outside every project's markers, "what's new" and history blocks, scripts and styles."""
    if node.tag in ("script", "style") or any(k.startswith(prefixes) for k in node.attrs):
        return
    for c in node.children:
        if isinstance(c, str):
            out += VERSION.findall(c)
        else:
            stray_versions(c, prefixes, out)


def collapse(errors: list[str]) -> list[str]:
    """One line per distinct error, with a count when it repeats (a release bump repeats one error per marker)."""
    counts: dict[str, int] = {}
    for e in errors:
        counts[e] = counts.get(e, 0) + 1
    return [e if c == 1 else f"{e} (×{c})" for e, c in counts.items()]


def check(html: str, facts: dict, project: str, primary: bool = True) -> list[str]:
    """Errors for one page. On the project's own page (primary) markers and "what's new" are required;
    on a page that only repeats its facts, the markers present must be true and no version may stray."""
    P = PROJECTS[project]["attr"]
    errors: list[str] = []
    root = parse(html)
    nodes = list(root.walk())

    def marks(key):
        return [n for n in nodes if n.attrs.get(P) == key]

    if PROJECTS[project].get("kind") == "github":
        want = facts["release"]
        repo, name = PROJECTS[project]["repo"], P[len("data-"):]
        # Links into the repository that name a version (a release page, docs at a tag) go stale like
        # text does, and the link text alone would not show it.
        for n in nodes:
            for a in ("href", "src"):
                url = n.attrs.get(a, "")
                if f"github.com/{repo}/" not in url:
                    continue
                vs = [v.lstrip("v") for v in VERSION.findall(url)]
                if not vs:
                    continue
                kind = n.attrs.get(f"data-link-{name}")
                if kind == "release":
                    for v in vs:
                        if v != want:
                            errors.append(f'link {url} (data-link-{name}="release") names {v}, the truth is {want}')
                elif kind == "history":
                    for v in vs:
                        if vkey(v) > vkey(want):
                            errors.append(f'link {url} is marked history but names {v}, newer than the latest release {want}')
                else:
                    errors.append(f'link {url} names version {vs[0]} without data-link-{name}="release|history"')
        # History names an earlier release; one that is not older than the latest is a stale marker.
        for n in nodes:
            if f"{P}-history" in n.attrs:
                pieces = [c for d in n.walk() for c in d.children if isinstance(c, str)]
                for v in (v for t in pieces for v in VERSION.findall(t)):
                    if vkey(v.lstrip("v")) > vkey(want):
                        errors.append(f"{P}-history says {v}, newer than the latest release {want}")
        found = marks("release-version")
        if not found and primary:
            errors.append(f'no {P}="release-version" marker on the page (the truth is {want})')
        for n in found:
            if n.text().strip().lstrip("v") != want:
                errors.append(f'{P}="release-version" says {n.text().strip()!r}, the truth is {want}')
        blocks = {n.attrs[f"{P}-release"].lstrip("v") for n in nodes if f"{P}-release" in n.attrs}
        if primary and want not in blocks:
            errors.append(f"no \"what's new\" block ({P}-release=\"{want}\") for the newest release, {want}")
        stray: list[str] = []
        stray_versions(root, PREFIXES, stray)
        for v in sorted(set(stray), key=lambda s: vkey(s.lstrip("v"))):
            errors.append(f"version {v} is hard-coded outside a project marker — mark it ({P}=…, {P}-history), or drop it")
        return collapse(errors)

    released = {a: v for a, v in facts["maven"].items() if v}
    maven_version = max(released.values(), key=vkey) if released else None

    # 1. version markers
    expected = {"maven-version": maven_version or "unpublished"}
    if "pypi_version" in facts:
        expected["pypi-version"] = facts["pypi_version"] or "unpublished"
    if "main_version" in facts:
        expected["main-version"] = facts["main_version"]
        expected["next-version"] = re.sub(r"-SNAPSHOT$", "", facts["main_version"])
    required = {"maven-version", "pypi-version", "main-version"} if primary else set()
    for key, want in expected.items():
        found = marks(key)
        if not found and key in required:
            errors.append(f'no {P}="{key}" marker on the page (the truth is {want})')
        for n in found:
            got = n.text().strip().lstrip("v") if key == "next-version" else n.text().strip()
            if got != want:
                errors.append(f'{P}="{key}" says {n.text().strip()!r}, the truth is {want}')

    if not primary:  # libraries, extras, capabilities and "what's new" live on the project's own page
        stray = []
        stray_versions(root, PREFIXES, stray)
        for v in sorted(set(stray), key=lambda s: vkey(s.lstrip("v"))):
            errors.append(f"version {v} is hard-coded outside a project marker — mark it, or drop it")
        return errors

    # 2. libraries
    rows = {n.attrs[f"{P}-artifact"]: n for n in nodes if f"{P}-artifact" in n.attrs}
    for a, v in facts["maven"].items():
        row = rows.get(a)
        if row is None:
            # Releases are batched: a library merged on main reaches the page with the release that
            # publishes it, not before. An unreleased library may have a row, but does not need one.
            if v:
                errors.append(f"library {a} (released {v}) has no {P}-artifact row")
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

    # 3. pip extras (as released) / 4. capabilities: exactly the set in the source
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
    stray_versions(root, PREFIXES, stray)
    for v in sorted(set(stray), key=lambda s: vkey(s.lstrip("v"))):
        errors.append(f"version {v} is hard-coded outside a {P} marker — mark it, or drop it")
    return errors


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("project", choices=sorted(PROJECTS))
    ap.add_argument("--repo", help="a checkout of the project's repository (main); not needed for kind github")
    ap.add_argument("--facts", help="read the facts from this JSON file instead of gathering them")
    ap.add_argument("--dump-facts", action="store_true", help="print the gathered facts as JSON and exit")
    ap.add_argument("--page", help="override the page path")
    args = ap.parse_args()

    cfg = PROJECTS[args.project]
    if cfg.get("kind") != "github" and not args.repo and not args.facts:
        ap.error(f"{args.project} needs --repo")
    try:
        facts = json.loads(Path(args.facts).read_text()) if args.facts else gather(
            args.project, Path(args.repo) if args.repo else None)
    except (OSError, urllib.error.URLError, ValueError, AttributeError) as e:
        print(f"check-release-page: could not gather the facts ({e}) — the check did NOT run", file=sys.stderr)
        return 2
    if args.dump_facts:
        print(json.dumps(facts, indent=2))
        return 0

    pages = [(Path(args.page), True)] if args.page else \
        [(ROOT / cfg["page"], True)] + [(ROOT / p, False) for p in cfg.get("also", [])]
    errors = []
    for page, primary in pages:
        for e in check(page.read_text(encoding="utf-8"), facts, args.project, primary=primary):
            errors.append(f"{page.relative_to(ROOT) if page.is_relative_to(ROOT) else page}: {e}")
    for e in errors:
        print(f"ERROR {e}")
    if cfg.get("kind") == "github":
        print(f"check-release-page {args.project}: GitHub release {facts['release']} · "
              f"{len(pages)} page(s) — {len(errors)} error(s)")
        return 1 if errors else 0
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
