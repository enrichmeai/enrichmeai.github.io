#!/usr/bin/env bash
# Self-test for render-verdict.sh: the verdict the check acts on, for each shape the review can return.
# Run: .github/adversarial-review/render-verdict-test.sh  (no network)
set -euo pipefail

here=$(cd "$(dirname "$0")" && pwd)
work=$(mktemp -d)
trap 'rm -rf "$work"' EXIT
export REVIEW_DIR="$work/review" HEAD_SHA=0123456789abcdef RUN_URL=https://run PREPARE=success OUTCOME=success
mkdir -p "$REVIEW_DIR"
fail=0

check() { # name, VERDICT_JSON, expected verdict, text the comment must contain
  local got
  got=$(VERDICT_JSON="$2" "$here/render-verdict.sh" "$work/out.md")
  if [ "$got" = "$3" ] && grep -qF -- "$4" "$work/out.md"; then
    echo "ok   $1 -> $got"
  else
    echo "FAIL $1: got '$got', want '$3' with '$4'"; fail=1
  fi
}

check pass '{"verdict":"PASS","summary":"s","checked":"c","findings":[]}' PASS 'No findings.'
check block '{"verdict":"BLOCK","summary":"s","checked":"c","findings":[{"severity":"blocking","file":"a.sh","line":3,"claim":"x","failure_scenario":"y"}]}' BLOCK '- **blocking** `a.sh:3`: x'
check pass-with-blocking '{"verdict":"PASS","summary":"s","checked":"c","findings":[{"severity":"blocking","file":"a","claim":"x","failure_scenario":"y"}]}' BLOCK 'a blocking finding is a BLOCK'
check empty '' 'NOT RUN' 'This is not a pass'
check malformed '{"verdict":' 'NOT RUN' 'This is not a pass'
check lowercase '{"verdict":"pass","summary":"s","checked":"c","findings":[]}' 'NOT RUN' 'This is not a pass'
check optional-only '{"verdict":"PASS","summary":"s","checked":"c","findings":[{"severity":"optional","file":"a","claim":"x","failure_scenario":"y"}]}' PASS '- **optional** `a`: x'

check findings-not-objects '{"verdict":"PASS","summary":"s","checked":"c","findings":["x"]}' 'NOT RUN' 'This is not a pass'
check severity-capitalised '{"verdict":"PASS","summary":"s","checked":"c","findings":[{"severity":"Blocking","file":"a","claim":"x","failure_scenario":"y"}]}' BLOCK 'a blocking finding is a BLOCK'
check severity-missing '{"verdict":"PASS","summary":"s","checked":"c","findings":[{"file":"a","claim":"x","failure_scenario":"y"}]}' BLOCK 'a blocking finding is a BLOCK'
SELFTEST=failure check selftest-failed '' 'NOT RUN' 'the self-test of the review scripts failed'

printf '.github/workflows/adversarial-review.yml\n' > "$REVIEW_DIR/self-change.txt"
check self-change '{"verdict":"PASS","summary":"s","checked":"c","findings":[]}' PASS 'this verdict is advisory'
rm "$REVIEW_DIR/self-change.txt"

big=$(python3 -c 'print("x" * 70000)')
check oversized "{\"verdict\":\"PASS\",\"summary\":\"$big\",\"checked\":\"c\",\"findings\":[]}" PASS 'cut at 60000 characters'
size=$(wc -c < "$work/out.md")
if [ "$size" -le 65536 ]; then echo "ok   oversized comment is $size bytes"; else echo "FAIL oversized comment is $size bytes"; fail=1; fi

[ "$fail" = 0 ] && echo "render-verdict: all cases pass" || { echo "render-verdict: FAILED"; exit 1; }
