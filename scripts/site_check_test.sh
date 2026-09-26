#!/usr/bin/env bash
# Fixture tests for scripts/site_check.py: each broken page must be caught, the clean one must pass.
# Run after ANY change to site_check.py:  scripts/site_check_test.sh
set -uo pipefail
here=$(cd "$(dirname "$0")" && pwd)
tmp=$(mktemp -d); trap 'rm -rf "$tmp"' EXIT
fail=0; n=0

head='<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>T</title><meta name="description" content="d"></head><body>'
mkdir -p "$tmp/sub"
printf '%s<h2 id="a">x</h2><p>para<ul><li>one<li>two</ul><img src="/sub/i.svg" alt=""></body></html>' "$head" > "$tmp/sub/index.html"
echo '<svg xmlns="http://www.w3.org/2000/svg"></svg>' > "$tmp/sub/i.svg"

case_() { # $1 = want (pass|find), $2 = label, $3 = file name, $4 = content
  n=$((n+1)); printf '%s' "$4" > "$tmp/$3"
  SITE_ROOT="$tmp" python3 "$here/site_check.py" "$tmp/$3" >/dev/null 2>&1; code=$?
  got=pass; [ $code -eq 1 ] && got=find; [ $code -eq 2 ] && got=error
  [ "$got" = "$1" ] || { echo "FAIL: $2 — expected $1, got $got"; fail=1; }
  rm -f "$tmp/$3"
}

case_ pass "clean page, links to a dir and an id"    ok.html   "$head<a href=\"/sub/#a\">s</a><a href=\"https://x.y/\">e</a></body></html>"
case_ find "unclosed div"                             a.html    "$head<div><span>x</span></body></html>"
case_ find "stray close tag"                          b.html    "$head</section></body></html>"
case_ find "duplicate id"                             c.html    "$head<h2 id=\"x\">1</h2><h2 id=\"x\">2</h2></body></html>"
case_ find "missing lang"                             d.html    "${head/ lang=\"en\"/}</body></html>"
case_ find "missing meta description"                 e.html    "${head/<meta name=\"description\" content=\"d\">/}</body></html>"
case_ find "link to a missing page"                   f.html    "$head<a href=\"/nope/\">x</a></body></html>"
case_ find "link to a missing anchor on another page" g.html    "$head<a href=\"/sub/#zz\">x</a></body></html>"
case_ find "link to a missing anchor on this page"    h.html    "$head<a href=\"#nowhere\">x</a></body></html>"
case_ find "img without alt"                          i.html    "$head<img src=\"/sub/i.svg\"></body></html>"
case_ find "unbalanced css"                           j.css     "a { color: red; "
case_ pass "css brace inside a string"                k.css     "a::after { content: \"}\"; }"
case_ find "broken svg"                               l.svg     "<svg><g></svg>"
case_ find "broken json"                              m.json    "{\"a\": }"

if [ $fail -eq 0 ]; then echo "site_check_test: $n cases passed"; else exit 1; fi
