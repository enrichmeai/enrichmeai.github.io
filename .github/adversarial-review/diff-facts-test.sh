#!/usr/bin/env bash
# Self-test for diff-facts.sh: a throwaway git repo with a planted diff, and the facts it must print.
# Run: .github/adversarial-review/diff-facts-test.sh  (no network, a second or two)
set -euo pipefail

here=$(cd "$(dirname "$0")" && pwd)
facts="$here/diff-facts.sh"
work=$(mktemp -d)
trap 'rm -rf "$work"' EXIT
cd "$work"
git init -q -b main
git config user.email t@example.invalid
git config user.name test

mkdir -p src/main/java/x src/test/java/x orchestrator/tests client/src/__tests__ .github/workflows
printf 'class A { int f() { return 1; } }\n' > src/main/java/x/A.java
printf 'class ATest {\n  @Test void f() { assertThat(new A().f()).isEqualTo(1); }\n  @Test void g() { assertThat(2).isEqualTo(2); }\n}\n' > src/test/java/x/ATest.java
printf 'def test_one():\n    assert 1 == 1\n' > orchestrator/tests/test_gone.py
printf 'it("works", () => { expect(1).toBe(1) })\n' > client/src/__tests__/page.test.tsx
printf 'name: ci\n' > .github/workflows/ci.yml
printf '# notes\n' > tests_notes.md
git add -A && git commit -qm base

# The planted change: production edited, one assertion removed, one test disabled, a Python test
# file deleted, a JS test focused with .only, the workflow edited.
printf 'class A { int f() { return 2; } }\n' > src/main/java/x/A.java
printf 'class ATest {\n  @Disabled @Test void f() { new A().f(); }\n  @Test void g() { assertThat(2).isEqualTo(2); }\n}\n' > src/test/java/x/ATest.java
git rm -q orchestrator/tests/test_gone.py
printf 'it.only("works", () => { expect(1).toBe(1) })\n' > client/src/__tests__/page.test.tsx
printf 'name: ci\non: push\n' > .github/workflows/ci.yml
git add -A && git commit -qm change

out=$("$facts" main~1 main)
fail=0
expect() {
  if grep -qF -- "$1" <<<"$out"; then echo "ok   $1"; else echo "FAIL $1"; fail=1; fi
}
expect '- files changed: 5, of which test files: 3, production and other files: 2'
expect '- **test files DELETED:**'
expect '  - `orchestrator/tests/test_gone.py`'
expect '  - M `src/test/java/x/ATest.java` +1/-1'
expect '- assertion lines in test files: +1 added, -3 removed'
expect '- **skip or focus markers ADDED:**'
expect '`src/test/java/x/ATest.java`: @Disabled @Test void f() { new A().f(); }'
expect '`client/src/__tests__/page.test.tsx`: it.only("works"'
expect '- **test harness or reviewer changed**'
expect '  - `.github/workflows/ci.yml`'

# Each repo's own layouts: valuedocs' integrationTest and testFixtures source sets and its
# *-selftest.py scripts; the site's checker fixtures, release-page test and hook test; and the
# files that decide what "green" means (the UAT runner, the release-page checker).
mkdir -p mcp/src/integrationTest/java common/src/testFixtures/java scripts tools .claude/hooks
printf 'class McpIntegrationHarness {}\n' > mcp/src/integrationTest/java/McpIntegrationHarness.java
printf 'class LedgerTestDatabase {}\n' > common/src/testFixtures/java/LedgerTestDatabase.java
printf 'print(1)\n' > scripts/corpus-gate-selftest.py
printf 'echo\n' > scripts/site_check_test.sh
printf 'pass\n' > tools/test_check_release_page.py
printf 'echo\n' > .claude/hooks/test-hooks.sh
printf 'echo\n' > scripts/uat-local.sh
printf 'pass\n' > tools/check-release-page.py
git add -A && git commit -qm layouts
out=$("$facts" main~1 main)
expect '- files changed: 8, of which test files: 6, production and other files: 2'
expect '  - A `mcp/src/integrationTest/java/McpIntegrationHarness.java`'
expect '  - A `common/src/testFixtures/java/LedgerTestDatabase.java`'
expect '  - A `scripts/corpus-gate-selftest.py`'
expect '  - A `scripts/site_check_test.sh`'
expect '  - A `tools/test_check_release_page.py`'
expect '  - A `.claude/hooks/test-hooks.sh`'
expect '  - `scripts/uat-local.sh`'
expect '  - `tools/check-release-page.py`'

# dbt keeps its tests in model YAML (data_tests:, unit_tests:), and the terraform config rows are read
# by both test suites: both decide what "green" means. A renamed test file is still a test file.
mkdir -p dbt/fdp/p/models infra/terraform/config
printf 'models:\n  - name: m\n    data_tests:\n      - unique\n' > dbt/fdp/p/models/schema.yml
printf 'x = 1\n' > infra/terraform/config/stages.tf
git add -A && git commit -qm dbt-base
printf 'models:\n  - name: m\n' > dbt/fdp/p/models/schema.yml
printf 'x = 2\n' > infra/terraform/config/stages.tf
git mv tools/test_check_release_page.py tools/test_release_page.py
git commit -qam dbt-change
out=$("$facts" main~1 main)
expect '  - `dbt/fdp/p/models/schema.yml`'
expect '  - `infra/terraform/config/stages.tf`'
expect '`tools/test_release_page.py`'

# More ways to switch a test off, and a deleted test file's assertions counted as removed.
mkdir -p tests
printf 'class T(unittest.TestCase):\n    def test_a(self):\n        self.assertEqual(1, 1)\n' > tests/test_more.py
printf 'class BTest {\n  @Test void b() { assertThat(1).isEqualTo(1); }\n}\n' > src/test/java/x/BTest.java
git add -A && git commit -qm more-base
printf 'class T(unittest.TestCase):\n    def test_a(self):\n        self.skipTest("later")\n        self.assertEqual(1, 1)\n    @EnabledIfEnvironmentVariable\n    def test_b(self): pass\n' > tests/test_more.py
git rm -q src/test/java/x/BTest.java
git add -A && git commit -qm more-change
out=$("$facts" main~1 main)
expect '`tests/test_more.py`: self.skipTest("later")'
expect '`tests/test_more.py`: @EnabledIfEnvironmentVariable'
expect '- assertion lines in test files: +0 added, -1 removed'

# A clean diff says "none" for each fact rather than printing nothing.
printf 'class A { int f() { return 3; } }\n' > src/main/java/x/A.java
git commit -qam prod-only
out=$("$facts" main~1 main)
expect '- test files deleted: none'
expect '- test files changed: none'
expect '- test harness or reviewer changed: none'

# "Cannot see" is an error, never an empty report.
set +e
"$facts" main no-such-ref >/dev/null 2>&1
rc=$?
set -e
if [ "$rc" = 2 ]; then echo "ok   unresolvable ref exits 2"; else echo "FAIL unresolvable ref exited $rc, want 2"; fail=1; fi

[ "$fail" = 0 ] && echo "diff-facts: all cases pass" || { echo "diff-facts: FAILED"; exit 1; }
