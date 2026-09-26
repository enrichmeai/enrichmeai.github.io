#!/usr/bin/env python3
"""Keep /culvert/ in step with what Culvert has actually released.

Every Culvert release has to reach this site: the version, every library, and the new features
(CLAUDE.md § "Culvert releases"). This checks culvert/index.html against the truth:

  * PyPI (`culvert`) and Maven Central (`com.enrichmeai.culvert:*`) — what is released;
  * a Culvert checkout — which libraries exist (the Java reactor) and which pip extras exist.

The page marks every fact it states, so nothing is scraped from prose:

  <span data-culvert="pypi-version">0.1.1</span>          the latest culvert on PyPI
  <span data-culvert="maven-version">0.2.0</span>         the latest com.enrichmeai.culvert release
  <tr data-culvert-artifact="data-pipeline-aws-s3" data-state="released|unreleased">
      … <span data-culvert="artifact-version">0.2.0</span> (released rows only)
  <code data-culvert-extra="gcp">                         one per pip extra
  <section data-culvert-release="0.2.0">                  what's new in that release

Rules:
  1. every version marker equals the registry;
  2. every library in the reactor has a row; released ones say "released" with their Maven
     version, unreleased ones say "unreleased"; no row names a library that no longer exists;
  3. the extras on the page are exactly the extras in python-culvert/pyproject.toml;
  4. there is a "what's new" block for the newest release in either ecosystem;
  5. no other x.y.z version appears on the page outside a marker or a "what's new" block, so a
     hard-coded "0.1.0" can never go stale again.

Usage:
  tools/check-culvert-page.py --culvert ../culvert            # fetch registries, check the page
  tools/check-culvert-page.py --culvert ../culvert --dump-facts
  tools/check-culvert-page.py --culvert ../culvert --facts facts.json   # offline (tests)
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
PAGE = ROOT / "culvert" / "index.html"
GROUP = "com.enrichmeai.culvert"
VERSION = re.compile(r"(?<![\w.])\d+\.\d+\.\d+(?![\w.]*\d)")


# ---------------------------------------------------------------- facts
def vkey(v: str) -> tuple:
    return tuple(int(x) if x.isdigit() else -1 for x in re.split(r"[.\-]", v))


def reactor_libraries(culvert: Path) -> list[str]:
    """Artifact ids of every library in the Java reactor, minus modules that are never published."""
    agg = (culvert / "data-pipeline-libraries-java" / "pom.xml").read_text(encoding="utf-8")
    out = []
    for module in re.findall(r"<module>([^<]+)</module>", agg):
        pom = (culvert / "data-pipeline-libraries-java" / module / "pom.xml").read_text(encoding="utf-8")
        own = re.sub(r"<parent>.*?</parent>", "", pom, flags=re.S)
        artifact = re.search(r"<artifactId>([^<]+)</artifactId>", own).group(1)
        if re.search(r"<maven\.deploy\.skip>\s*true", own) or re.search(r"never published", own, re.I):
            continue  # a build gate, not a library (e.g. data-pipeline-registration-audit)
        out.append(artifact)
    return out


def pip_extras(culvert: Path) -> list[str]:
    text = (culvert / "python-culvert" / "pyproject.toml").read_text(encoding="utf-8")
    block = re.search(r"^\[project\.optional-dependencies\]\s*$(.*?)^\[", text, re.S | re.M)
    return re.findall(r"^([A-Za-z0-9_-]+)\s*=\s*\[", block.group(1), re.M) if block else []


def fetch(url: str, attempts: int = 5) -> str | None:
    """GET a registry URL. 404 means "not published"; 429/5xx are retried with backoff."""
    for i in range(attempts):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "enrichmeai-site-culvert-check"})
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


def gather(culvert: Path) -> dict:
    libs = reactor_libraries(culvert)
    pypi = json.loads(fetch("https://pypi.org/pypi/culvert/json") or "{}")
    maven = {}
    for a in libs:
        meta = fetch(f"https://repo1.maven.org/maven2/{GROUP.replace('.', '/')}/{a}/maven-metadata.xml")
        m = re.search(r"<release>([^<]+)</release>", meta or "")
        maven[a] = m.group(1) if m else None
    return {
        "pypi_version": pypi.get("info", {}).get("version"),
        "maven": maven,
        "extras": pip_extras(culvert),
    }


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


def stray_versions(node: Node, out: list[str]) -> None:
    """x.y.z text outside markers, "what's new" blocks, scripts and styles."""
    if node.tag in ("script", "style") or any(k.startswith("data-culvert") for k in node.attrs):
        return
    for c in node.children:
        if isinstance(c, str):
            out += VERSION.findall(c)
        else:
            stray_versions(c, out)


def check(html: str, facts: dict) -> list[str]:
    errors: list[str] = []
    root = parse(html)
    nodes = list(root.walk())

    released = {a: v for a, v in facts["maven"].items() if v}
    maven_version = max(released.values(), key=vkey) if released else None
    pypi_version = facts.get("pypi_version")

    # 1. version markers
    for key, want in (("pypi-version", pypi_version), ("maven-version", maven_version)):
        marks = [n for n in nodes if n.attrs.get("data-culvert") == key]
        if want and not marks:
            errors.append(f'no data-culvert="{key}" marker on the page (the registry has {want})')
        for n in marks:
            if n.text().strip() != want:
                errors.append(f'data-culvert="{key}" says {n.text().strip()!r}, the registry has {want}')

    # 2. libraries
    rows = {n.attrs["data-culvert-artifact"]: n for n in nodes if "data-culvert-artifact" in n.attrs}
    for a, v in facts["maven"].items():
        row = rows.get(a)
        if row is None:
            errors.append(f"library {a} ({'released ' + v if v else 'unreleased'}) has no row in the Libraries table")
            continue
        state = row.attrs.get("data-state")
        if v:
            if state != "released":
                errors.append(f'{a} is released ({v}) but its row says data-state="{state}"')
            shown = [n.text().strip() for n in row.walk() if n.attrs.get("data-culvert") == "artifact-version"]
            if shown != [v]:
                errors.append(f"{a} row shows version {shown or 'none'}, Maven Central has {v}")
        elif state != "unreleased":
            errors.append(f'{a} is not on Maven Central but its row says data-state="{state}"')
    for a in sorted(set(rows) - set(facts["maven"])):
        errors.append(f"the Libraries table lists {a}, which is not a library in Culvert's reactor any more")

    # 3. extras
    page_extras = {n.attrs["data-culvert-extra"] for n in nodes if "data-culvert-extra" in n.attrs}
    for e in sorted(set(facts["extras"]) - page_extras):
        errors.append(f"pip extra culvert[{e}] is missing from the page")
    for e in sorted(page_extras - set(facts["extras"])):
        errors.append(f"the page lists culvert[{e}], which python-culvert/pyproject.toml no longer defines")

    # 4. what's new
    newest = max([v for v in (pypi_version, maven_version) if v], key=vkey, default=None)
    blocks = {n.attrs["data-culvert-release"] for n in nodes if "data-culvert-release" in n.attrs}
    if newest and newest not in blocks:
        errors.append(f"no \"what's new\" block (data-culvert-release=\"{newest}\") for the newest release, {newest}")

    # 5. hard-coded versions
    stray: list[str] = []
    stray_versions(root, stray)
    for v in sorted(set(stray), key=vkey):
        errors.append(f"version {v} is hard-coded outside a data-culvert marker — mark it, or drop it")
    return errors


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--culvert", required=True, help="a checkout of enrichmeai/culvert (main)")
    ap.add_argument("--facts", help="read registry facts from this JSON file instead of the network")
    ap.add_argument("--dump-facts", action="store_true", help="print the gathered facts as JSON and exit")
    ap.add_argument("--page", default=str(PAGE))
    args = ap.parse_args()

    culvert = Path(args.culvert)
    try:
        facts = json.loads(Path(args.facts).read_text()) if args.facts else gather(culvert)
    except (OSError, urllib.error.URLError, ValueError, AttributeError) as e:
        print(f"check-culvert-page: could not gather the facts ({e}) — the check did NOT run", file=sys.stderr)
        return 2
    if args.dump_facts:
        print(json.dumps(facts, indent=2))
        return 0

    errors = check(Path(args.page).read_text(encoding="utf-8"), facts)
    for e in errors:
        print(f"ERROR {e}")
    released = {a: v for a, v in facts["maven"].items() if v}
    print(
        f"check-culvert-page: PyPI {facts.get('pypi_version')} · Maven "
        f"{max(released.values(), key=vkey) if released else 'none'} "
        f"({len(released)}/{len(facts['maven'])} libraries released) · {len(facts['extras'])} extras "
        f"— {len(errors)} error(s)"
    )
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
