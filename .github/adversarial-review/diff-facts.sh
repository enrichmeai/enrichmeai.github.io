#!/usr/bin/env bash
# diff-facts.sh BASE HEAD: the facts about a diff's TESTS, read by git and not by a model.
#
# The adversarial review (.github/workflows/adversarial-review.yml) gets this output as evidence
# and the PR comment repeats it verbatim, so a human sees it without trusting the model's reading.
# Why it exists (Vaccari, "Tests as data", martinfowler.com, 2026-11-11): an agent that writes the
# code also rewrites the tests, a weakened test reads like any other diff line, and the check that
# helps is a CI step saying which test files a change touched, against what the task should touch.
#
# What it cannot see: an assertion swapped for a weaker one on the same line count (isEqualTo(1) to
# isNotNull()) nets to zero, and dbt YAML is reported as harness, not counted assertion by assertion.
# The reviewer reads the diff for those.
#
# It reports, never judges: it always exits 0 when git can answer, and 2 when it cannot (a missing
# ref), so "cannot see" is never printed as "no test changes".
set -euo pipefail

base=${1:?usage: diff-facts.sh BASE HEAD}
head=${2:?usage: diff-facts.sh BASE HEAD}
for ref in "$base" "$head"; do
  git rev-parse --verify --quiet "${ref}^{commit}" >/dev/null || { echo "diff-facts: cannot resolve ${ref}" >&2; exit 2; }
done
range="${base}...${head}"

# A test file, by path, in any of the three repos' layouts: src/test/, src/integrationTest/,
# src/testFixtures/, tests/, __tests__/, selenium-tests/, test_*.py, *_test.*, *.test.*, *.spec.*,
# *Test.java, *IT.java, *-test.sh, test-*.sh, *-selftest.py.
test_path='(^|/)(src/(test|integrationTest|testFixtures)|tests?|__tests__|selenium-tests)/|(^|/)test_[^/]*\.py$|_test\.[a-z]+$|\.(test|spec)\.[a-z]+$|(Test|IT|Tests)\.(java|kt)$|(^|/)test-[^/]*\.sh$|-test\.sh$|-selftest\.py$'
# Code that RUNS tests or reviews them: changing it changes what "green" means.
harness_path='^\.github/workflows/|^\.github/adversarial-review/|^\.claude/(hooks|agents|settings\.json)|(^|/)conftest\.py$|(^|/)(pytest\.ini|setup\.cfg|tox\.ini|vitest\.config\.[a-z]+|playwright\.config\.[a-z]+)$|(^|/)build\.gradle(\.kts)?$|^scripts/(site_check|ci-|uat-local\.sh$)|^tools/check-release-page\.py$|^dbt/.*\.ya?ml$|^infra/terraform/config/'
# A test switched off, or a run narrowed to one test.
skip_marker='@Disabled|@Ignore\b|@EnabledIf|@EnabledOn|skipTest\(|Assumptions?\.assume|assumeTrue\(|pytest\.mark\.(skip|xfail)|pytest\.skip\(|unittest\.skip|\b(it|describe|test)\.(skip|only|todo)\(|\bx(it|describe|test)\(|\bfit\(|\bfdescribe\('
assertion='assert|expect\(|verify\(|\.should|assertThat|StepVerifier|fail\(|pytest\.raises|assertRaises|data_tests:|unit_tests:'

changed=$(git diff --name-status -M "$range")
# Matched on the path alone (the last field: a rename's new name), never on the whole status line,
# where a leading tab would stop every `(^|/)` alternative from matching.
tests=$(while IFS= read -r line; do
  [ -n "$line" ] || continue
  path=${line##*$'\t'}
  if grep -qE "$test_path" <<<"$path" && ! grep -qE '\.(md|txt)$' <<<"$path"; then printf '%s\n' "$line"; fi
done <<<"$changed")
harness=$(awk -F'\t' '{print $NF}' <<<"$changed" | grep -E "$harness_path" || true)
n_all=$(grep -c . <<<"$changed" || true)
n_tests=$(grep -c . <<<"$tests" || true)

echo "## Test facts (git, not a model): ${range}"
echo
echo "- files changed: ${n_all}, of which test files: ${n_tests}, production and other files: $((n_all - n_tests))"

deleted=$(awk -F'\t' '$1=="D"{print $2}' <<<"$tests")
if [ -n "$deleted" ]; then
  echo "- **test files DELETED:**"
  sed 's/^/  - `/; s/$/`/' <<<"$deleted"
else
  echo "- test files deleted: none"
fi

if [ -n "$tests" ]; then
  added_asserts=0; removed_asserts=0; skips=""
  echo "- test files changed (status, +lines/-lines):"
  while IFS=$'\t' read -r status path rest; do
    file=${rest:-$path}
    stat=$(git diff --numstat -M "$range" -- "$file" ${rest:+"$path"} | awk '{a+=$1; d+=$2} END {printf "+%d/-%d", a, d}')
    echo "  - ${status} \`${file}\` ${stat}"
    # A deleted file's lines all come back as removed, so its assertions count as removed.
    hunk=$(git diff -U0 -M "$range" -- "$file" ${rest:+"$path"})
    added_asserts=$((added_asserts + $(grep -E '^\+[^+]' <<<"$hunk" | grep -cE "$assertion" || true)))
    removed_asserts=$((removed_asserts + $(grep -E '^-[^-]' <<<"$hunk" | grep -cE "$assertion" || true)))
    new_skips=$(grep -E '^\+[^+]' <<<"$hunk" | grep -E "$skip_marker" | sed "s|^+[[:space:]]*|\`${file}\`: |" || true)
    [ -n "$new_skips" ] && skips+="${new_skips}"$'\n'
  done <<<"$tests"
  echo "- assertion lines in test files: +${added_asserts} added, -${removed_asserts} removed"
  if [ -n "$skips" ]; then
    echo "- **skip or focus markers ADDED:**"
    sed '/^$/d; s/^/  - /' <<<"$skips"
  else
    echo "- skip or focus markers added: none"
  fi
else
  echo "- test files changed: none"
fi

if [ -n "$harness" ]; then
  echo "- **test harness or reviewer changed** (what \"green\" means may have moved):"
  sed 's/^/  - `/; s/$/`/' <<<"$harness"
else
  echo "- test harness or reviewer changed: none"
fi
