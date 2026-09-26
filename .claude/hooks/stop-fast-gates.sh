#!/usr/bin/env bash
# Stop: before Claude ends a turn, run the fast gates for what this branch touches, and feed any
# failure back.
#   - any site file changed (html, css, svg, json, yaml): scripts/site_check.py on the WHOLE site,
#     because a renamed id or a moved page breaks links on pages nobody edited;
#   - scripts/site_check* changed: scripts/site_check_test.sh as well;
#   - .claude/hooks/ or .claude/settings.json changed: .claude/hooks/test-hooks.sh.
#   - change set = diff vs the merge-base with origin/main, plus uncommitted and untracked files;
#   - skipped when that change set is identical to the last one that passed;
#   - one retry only: if a stop was already blocked (stop_hook_active) and it still fails, the stop
#     is allowed with a warning, so a broken gate can never loop forever.
# Opt out for one session: CLAUDE_SKIP_STOP_GATES=1.
set -uo pipefail

[ "${CLAUDE_SKIP_STOP_GATES:-}" = "1" ] && exit 0
input=$(cat)
active=$(printf '%s' "$input" | jq -r '.stop_hook_active // false')

root="${CLAUDE_PROJECT_DIR:-$(pwd)}"
cd "$root" || exit 0

base=$(git merge-base HEAD origin/main 2>/dev/null || echo HEAD)
all_changed=$( { git diff --name-only "$base" 2>/dev/null; git ls-files --others --exclude-standard 2>/dev/null; } | sort -u)
[ -z "$all_changed" ] && exit 0

gates=()
printf '%s\n' "$all_changed" | grep -qE '\.(html|css|svg|json|ya?ml)$' && [ -f scripts/site_check.py ] && gates+=("python3 scripts/site_check.py")
printf '%s\n' "$all_changed" | grep -qE '^scripts/site_check' && [ -x scripts/site_check_test.sh ] && gates+=("scripts/site_check_test.sh")
printf '%s\n' "$all_changed" | grep -qE '^\.claude/(hooks/|settings\.json$)' && [ -x .claude/hooks/test-hooks.sh ] && gates+=(".claude/hooks/test-hooks.sh")
[ ${#gates[@]} -eq 0 ] && exit 0

stamp_file="$(git rev-parse --git-dir)/claude-stop-check.stamp"
stamp=$( { printf '%s\n' "${gates[@]}"; for f in $all_changed; do [ -f "$f" ] && { echo "$f"; cat "$f"; }; done; } | sha256sum | cut -d' ' -f1)
[ -f "$stamp_file" ] && [ "$(cat "$stamp_file")" = "$stamp" ] && exit 0

msg=""
for g in "${gates[@]}"; do
  if ! out=$(bash -c "$g" 2>&1); then
    msg+="$g failed:"$'\n'"$(printf '%s' "$out" | tail -40)"$'\n'
  fi
done

if [ -z "$msg" ]; then echo "$stamp" > "$stamp_file"; exit 0; fi
if [ "$active" = "true" ]; then
  jq -n --arg m "$msg" '{systemMessage: ("Stop allowed, but the fast gates still fail — treat this turn as BLOCKED.\n" + $m)}'
  exit 0
fi
jq -n --arg m "$msg" '{decision: "block", reason: ($m + "\nFix these, or if this is attempt 3, stop and write the Blocker summary (CLAUDE.md § \"Autonomous build loop\").")}'
exit 0
