#!/usr/bin/env bash
# PostToolUse(Edit|Write|MultiEdit): the fast checks for the one file just edited, so an error
# reaches Claude on the edit that caused it rather than at the end of the task.
#
# Exit 2 + stderr = the output is fed back to Claude (docs: code.claude.com/docs/en/hooks).
# Only the edited file is judged. For a page that includes its outbound links and #anchors, so a
# link to a page or id that does not exist is caught here; a page that breaks links INTO it is
# caught by the Stop hook, which checks the whole site.
set -uo pipefail

file=$(jq -r '.tool_input.file_path // empty')
[ -z "$file" ] || [ ! -f "$file" ] && exit 0

root="${CLAUDE_PROJECT_DIR:-$(git -C "$(dirname "$file")" rev-parse --show-toplevel 2>/dev/null)}"
rel="${file#"$root"/}"
out=""
fail=0

case "$rel" in
  *.html|*.css|*.svg|*.json|*.yml|*.yaml)
    if [ -f "$root/scripts/site_check.py" ]; then
      o=$(SITE_ROOT="$root" python3 "$root/scripts/site_check.py" "$file" 2>&1); rc=$?
      if [ $rc -eq 1 ]; then out+=$'site_check:\n'"$o"$'\n'; fail=1; fi
      if [ $rc -eq 2 ]; then echo "post-edit-check: site_check could not run on $rel: $o" >&2; exit 1; fi
    fi
    ;;
  *.py)
    if ! o=$(python3 -m py_compile "$file" 2>&1); then out+=$'python syntax:\n'"$o"$'\n'; fail=1; fi
    ;;
  *.sh)
    if ! o=$(bash -n "$file" 2>&1); then out+=$'bash syntax:\n'"$o"$'\n'; fail=1; fi
    ;;
esac

if [ "$fail" -ne 0 ]; then
  printf '%s\nFix these in %s before moving on.\n' "$out" "$rel" | head -c 8000 >&2
  exit 2
fi
exit 0
