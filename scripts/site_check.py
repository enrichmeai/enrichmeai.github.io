#!/usr/bin/env python3
"""The fast gate for this site: everything a static page can get wrong without a browser.

Run from the repo root:  python3 scripts/site_check.py            (whole site)
                         python3 scripts/site_check.py a.html b.svg (only those files)

Checks, per file type:
  *.html  - tags balance (void and optional-close elements allowed), no duplicate id,
            <html lang>, <title>, meta description and viewport present, every internal
            href/src resolves to a file in the repo, every #fragment resolves to an id on
            the target page, every <img> has alt.
  *.css   - braces balance (comments and strings ignored).
  *.svg   - well-formed XML.
  *.json  - parses.   *.yml/*.yaml - parses (when PyYAML is installed).

Exit 0 clean, 1 findings, 2 the check could not run. Standard library only, so it runs
in CI, in a hook and on a laptop with nothing installed.
"""
from __future__ import annotations

import json
import os
import re
import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit

ROOT = os.path.abspath(os.environ.get("SITE_ROOT") or os.path.join(os.path.dirname(__file__), ".."))
SKIP_DIRS = {".git", "node_modules", ".venv", "fonts", ".claude"}

VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta",
        "source", "track", "wbr"}
# Elements whose end tag HTML lets you omit; closing them implicitly is not an error.
OPTIONAL_CLOSE = {"p", "li", "dt", "dd", "tr", "td", "th", "thead", "tbody", "tfoot",
                  "option", "optgroup", "rt", "rp", "colgroup", "caption"}
# SVG children written as <path ... /> are self-closing; the parser reports those separately.


class Page(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.stack: list[tuple[str, int]] = []
        self.errors: list[str] = []
        self.ids: dict[str, int] = {}
        self.links: list[tuple[str, int]] = []
        self.lang = False
        self.title = False
        self.meta: set[str] = set()
        self._in_title = False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        line = self.getpos()[0]
        if tag == "html" and a.get("lang"):
            self.lang = True
        if tag == "title":
            self._in_title = True
        if tag == "meta" and a.get("name") in {"description", "viewport"} and a.get("content"):
            self.meta.add(a["name"])
        if tag == "img" and "alt" not in a:
            self.errors.append(f"{line}: <img> without alt")
        self._attrs(a, line)
        if tag not in VOID:
            self.stack.append((tag, line))

    def handle_startendtag(self, tag, attrs):  # <x ... /> — never pushed
        self._attrs(dict(attrs), self.getpos()[0])

    def _attrs(self, a, line):
        if a.get("id"):
            if a["id"] in self.ids:
                self.errors.append(f"{line}: duplicate id \"{a['id']}\" (first on line {self.ids[a['id']]})")
            else:
                self.ids[a["id"]] = line
        for k in ("href", "src"):
            if a.get(k):
                self.links.append((a[k], line))

    def handle_data(self, data):
        if self._in_title and data.strip():
            self.title = True

    def handle_endtag(self, tag):
        line = self.getpos()[0]
        if tag == "title":
            self._in_title = False
        if tag in VOID:
            return
        names = [t for t, _ in self.stack]
        if tag not in names:
            self.errors.append(f"{line}: </{tag}> closes nothing that is open")
            return
        while self.stack:
            t, l = self.stack.pop()
            if t == tag:
                break
            if t not in OPTIONAL_CLOSE:
                self.errors.append(f"{line}: </{tag}> closes <{t}> from line {l}, which was never closed")

    def finish(self):
        for t, l in self.stack:
            if t not in OPTIONAL_CLOSE and t not in {"html", "body", "head"}:
                self.errors.append(f"{l}: <{t}> is never closed")


_parsed: dict[str, Page] = {}


def parse(path: str) -> Page:
    if path not in _parsed:
        p = Page()
        with open(path, encoding="utf-8") as fh:
            p.feed(fh.read())
        p.close()
        p.finish()
        _parsed[path] = p
    return _parsed[path]


def resolve(page: str, ref: str) -> tuple[str | None, str]:
    """Map an internal href/src to (repo file or None if external, fragment)."""
    u = urlsplit(ref)
    if u.scheme or u.netloc or ref.startswith(("mailto:", "tel:", "data:", "javascript:")):
        return None, ""
    frag = unquote(u.fragment)
    if not u.path:
        return page, frag
    base = ROOT if u.path.startswith("/") else os.path.dirname(page)
    target = os.path.normpath(os.path.join(base, unquote(u.path).lstrip("/")))
    if os.path.isdir(target) or u.path.endswith("/"):
        target = os.path.join(target, "index.html")
    return target, frag


def check_html(path: str) -> list[str]:
    p = parse(path)
    out = list(p.errors)
    if not p.lang:
        out.append("<html> has no lang attribute")
    if not p.title:
        out.append("no non-empty <title>")
    for m in ("description", "viewport"):
        if m not in p.meta:
            out.append(f"no <meta name=\"{m}\">")
    for ref, line in p.links:
        target, frag = resolve(path, ref)
        if target is None:
            continue
        if not target.startswith(ROOT) or not os.path.isfile(target):
            out.append(f"{line}: {ref} -> no such file in the repo")
            continue
        if frag and target.endswith(".html") and frag not in parse(target).ids:
            out.append(f"{line}: {ref} -> no id=\"{frag}\" on {os.path.relpath(target, ROOT)}")
    return out


def check_css(path: str) -> list[str]:
    with open(path, encoding="utf-8") as fh:
        text = re.sub(r"/\*.*?\*/", "", fh.read(), flags=re.S)
    text = re.sub(r"\"(\\.|[^\"\\])*\"|'(\\.|[^'\\])*'", "\"\"", text)
    depth = 0
    for n, line in enumerate(text.splitlines(), 1):
        for ch in line:
            depth += (ch == "{") - (ch == "}")
            if depth < 0:
                return [f"{n}: '}}' with no open block"]
    return [] if depth == 0 else [f"{depth} unclosed '{{' at end of file"]


def check_svg(path: str) -> list[str]:
    try:
        ET.parse(path)
        return []
    except ET.ParseError as e:
        return [f"invalid XML: {e}"]


def check_json(path: str) -> list[str]:
    try:
        with open(path, encoding="utf-8") as fh:
            json.load(fh)
        return []
    except ValueError as e:
        return [f"invalid JSON: {e}"]


def check_yaml(path: str) -> list[str]:
    try:
        import yaml  # type: ignore
    except ImportError:
        return []
    try:
        with open(path, encoding="utf-8") as fh:
            list(yaml.safe_load_all(fh))
        return []
    except yaml.YAMLError as e:
        return [f"invalid YAML: {e}"]


CHECKS = {".html": check_html, ".css": check_css, ".svg": check_svg, ".json": check_json,
          ".yml": check_yaml, ".yaml": check_yaml}


def all_files() -> list[str]:
    found = []
    for d, dirs, files in os.walk(ROOT):
        dirs[:] = sorted(x for x in dirs if x not in SKIP_DIRS)
        found += [os.path.join(d, f) for f in sorted(files) if os.path.splitext(f)[1] in CHECKS]
    return found


def main(argv: list[str]) -> int:
    files = [os.path.abspath(f) for f in argv] if argv else all_files()
    files = [f for f in files if os.path.splitext(f)[1] in CHECKS and os.path.isfile(f)]
    if not files:
        print("site-check: no checkable files", file=sys.stderr)
        return 2 if not argv else 0
    findings = 0
    for f in files:
        try:
            errs = CHECKS[os.path.splitext(f)[1]](f)
        except (OSError, UnicodeDecodeError) as e:
            print(f"site-check could not read {f}: {e}", file=sys.stderr)
            return 2
        for e in errs:
            print(f"{os.path.relpath(f, ROOT)}:{e}")
        findings += len(errs)
    print(f"site-check: {len(files)} files, {findings} findings", file=sys.stderr)
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
