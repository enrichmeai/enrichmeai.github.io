---
name: build-task
description: The autonomous build loop for ONE site task — spec → verify sources → red check → implement (hooks check each edit) → reviewer agent → fix (max 3 attempts) → /compound → PR. Use for "build #N", "take the next task", "fix the X page", or when the founder hands over a site task to do unattended. With no argument, takes the top item of the Claude queue on the Site board.
---

# /build-task — one task, start to reviewed PR

One task per session: a fresh session per task keeps context small. If the founder asks for a
second task, finish or park this one first.

## 0. Pick and pin the spec
- No argument: the first item of **Claude queue** on the Site board
  (`gh issue list --label board`). Argument: that issue.
- Write the spec down before anything else: acceptance criteria, the pages and files it touches,
  and how a check proves each criterion. Missing or ambiguous → comment the question on the issue,
  stop, and report. Do not guess scope.
- The task needs a product change (the page would have to claim something the product does not
  do yet) → stop; that is a `/new-issue` in the product's repo, and this page waits for its tag.

## 1. Claim, then branch
```bash
gh issue view <N> --json state,title
gh pr list --state open --json number,title,files      # anyone already on these pages?
git fetch -q origin && git log origin/main --oneline -5
```
Comment on the issue what you are about to touch (or open the PR as a draft first). Then branch
from `origin/main`, never a stale local `main`: `git worktree add <scratch>/site-<slug> -b site/<N>-<slug> origin/main`.
One concern per branch; a title that needs "and" is two PRs.

## 2. Verify before writing (CLAUDE.md § "Autonomous build loop")
- **Every factual claim** the change adds or edits — a version, a number, a command, a flag, what
  works, what does not — is checked against the product repo **at its latest release tag**
  (`../<repo>`, cloned side by side), and the file:line or command output is noted for the
  reviewer. The page may not run ahead of the tag.
- **Every HTML, CSS or browser behaviour** you rely on is checked against CLAUDE.md § "Pinned docs"
  (MDN, WHATWG, WCAG, GitHub Pages) with WebFetch. Never guess.
- A source you could not read is a gate that **did not run**: say so and treat it as a blocker.

## 3. Red, then green
Show the check failing for the right reason before the fix: a new case in
`scripts/site_check_test.sh` or a rule in `scripts/site_check.py` for a structural fault, or the
wrong sentence quoted beside the source that contradicts it for a claim. Then implement. The
PostToolUse hook runs site_check on each edited file; the Stop hook checks the whole site before
the turn ends. Fix what they report at once.

## 4. Gates — a task is not done until these pass
`python3 scripts/site_check.py` (whole site, 0 findings), `scripts/site_check_test.sh` when the
checker changed, `.claude/hooks/test-hooks.sh` when hooks or settings changed. Quote the result
lines. Look at every changed page in a browser at 375 px and 1280 px wide
(`python3 -m http.server 8000`, then a Playwright screenshot) and say what you looked at.
Push, open the PR as **draft**, and read the `Site check` run — never claim a run you have not seen green.

## 5. Review
Launch the `reviewer` agent with the spec from step 0 and the sources from step 2. Fix every
BLOCKER/MAJOR and every UNVERIFIED claim; answer MINORs in one line each. Re-run the reviewer after fixing.

## 6. The 3-attempt cap
An **attempt** is one fix-and-recheck cycle against the same failing gate or reviewer finding.
After the 3rd failed attempt, stop changing files and post on the issue (and in your reply):
```
Blocked: <gate or finding>
Tried: 1. … 2. … 3. … (what each changed, what it showed)
Evidence: <error lines, source file:line, run IDs>
Hypothesis: <best guess at the root cause>
Needs: <the decision, access or information that would unblock it>
```
Leave the branch pushed and the PR draft. Do not widen scope to route around the blocker.

## 7. Compound, then hand over
Run `/compound`. Then mark the PR ready and end with: branch, head SHA, files changed, gates run
with their results, what you looked at in the browser, reviewer verdict, Compound lines, and
anything for the founder. Merging follows `merge-gate`.
