#!/usr/bin/env bash
# render-verdict.sh OUT_FILE: turn the review's structured output into the PR comment, and print the
# verdict the check must act on: PASS, BLOCK or NOT RUN. The workflow posts OUT_FILE and fails the
# check unless this prints PASS. Tested by render-verdict-test.sh.
#
# Environment: VERDICT_JSON (the action's structured_output, maybe empty), PREPARE and OUTCOME (step
# outcomes), HEAD_SHA, RUN_URL, REVIEW_DIR (default .review).
#
# Fails closed three ways:
#   - no parseable verdict, or one that is neither PASS nor BLOCK: NOT RUN.
#   - PASS with any finding not marked optional: BLOCK. The schema cannot tie the two together, so this does.
#   - a PR that changes this reviewer is told, in the comment, that its verdict is advisory, because the
#     workflow file it runs is the PR's own copy (GitHub runs a pull_request workflow from the PR).
set -euo pipefail

out=${1:?usage: render-verdict.sh OUT_FILE}
dir=${REVIEW_DIR:-.review}
marker='<!-- adversarial-review -->'
sha=${HEAD_SHA:0:12}
limit=60000   # GitHub refuses a comment body over 65,536 characters.

verdict="NOT RUN"
note=""
# The shape is checked before anything reads it: a verdict that is not PASS or BLOCK, or findings that
# are not a list of objects, is no verdict.
shape='(.verdict == "PASS" or .verdict == "BLOCK") and ((.findings // []) | type == "array" and all(type == "object"))'
if [ -n "${VERDICT_JSON:-}" ] && jq -e "$shape" <<<"$VERDICT_JSON" >/dev/null 2>&1; then
  verdict=$(jq -r '.verdict' <<<"$VERDICT_JSON")
  # Anything not marked optional counts as blocking: "Blocking", a typo or a missing severity included.
  blocking=$(jq -r '[(.findings // [])[] | select(.severity != "optional")] | length' <<<"$VERDICT_JSON")
  if [ "$verdict" = PASS ] && [ "$blocking" -gt 0 ]; then
    verdict=BLOCK
    note="The reviewer said PASS with ${blocking} blocking finding(s); a blocking finding is a BLOCK."
  fi
  body=$(jq -r '
    def row: "- **\(.severity)** `\(.file)\(if .line then ":\(.line)" else "" end)`: \(.claim)\n  - fails when: \(.failure_scenario)\(if .fix then "\n  - fix: \(.fix)" else "" end)";
    "\(.summary // "")\n\n" +
    (if ((.findings // []) | length) == 0 then "No findings.\n" else
      ([.findings[] | select(.severity != "optional") | row] + [.findings[] | select(.severity == "optional") | row] | join("\n")) + "\n" end) +
    "\n<details><summary>What the reviewer checked</summary>\n\n\(.checked // "")\n</details>"' <<<"$VERDICT_JSON")
else
  body="No verdict: the prepare step ended \`${PREPARE:-unknown}\` and the review step \`${OUTCOME:-skipped}\`. This is not a pass: the diff was not reviewed. Re-run the job, or read the [run](${RUN_URL:-})."
fi

{
  echo "$marker"
  echo "### Adversarial review: ${verdict} at \`${sha}\`"
  echo
  if [ -s "$dir/self-change.txt" ]; then
    echo "> **This PR changes the reviewer itself** ($(paste -sd, "$dir/self-change.txt" | sed 's/,/, /g')). GitHub runs the PR's own copy of the workflow, so this verdict is advisory: the founder reviews these by hand."
    echo
  fi
  [ -n "$note" ] && { echo "> ${note}"; echo; }
  echo "$body"
  echo
  if [ -s "$dir/test-facts.md" ]; then
    echo "<details><summary>Test facts (git, not the model)</summary>"
    echo
    sed '1,2d' "$dir/test-facts.md"
    echo "</details>"
    echo
  fi
  if [ -s "$dir/sources.txt" ]; then
    echo "Rules read:"
    cat "$dir/sources.txt"
    echo
  fi
  echo "[run](${RUN_URL:-})"
} > "$out"

if [ "$(wc -c < "$out")" -gt "$limit" ]; then
  head -c "$limit" "$out" > "$out.cut"
  printf '\n\n…cut at %s characters; the whole verdict is in the [run](%s) summary.\n' "$limit" "${RUN_URL:-}" >> "$out.cut"
  mv "$out.cut" "$out"
fi

echo "$verdict"
