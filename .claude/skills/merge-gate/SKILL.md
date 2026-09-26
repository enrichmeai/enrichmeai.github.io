---
name: merge-gate
description: The checks to run before merging any PR on enrichmeai.github.io — where a merge to main IS a deploy of enrichmeai.com — and the live-site check after it. Use whenever a PR is about to be merged ("merge this", "can we merge", "land the PR", "ship it"), from any session.
---

# The merge gate

**A merge to `main` is a production deploy.** `.github/workflows/pages.yml` publishes the whole
repository to enrichmeai.com on every push to `main`. There is no staging site, so the gate is
the staging.

Run the checks as **separate commands** and read each output before the next. A check chained
into `gh pr merge` prints its warning after nothing can stop the merge.

## The five checks

### 1. Open-PR overlap
```bash
gh pr list --state open --json number,title,files --jq '.[] | "\(.number) \(.title): \([.files[].path]|join(" "))"'
```
Another open PR on the same page means **serialise, don't race**: agree an order in a PR comment.
`index.html` and `assets/site.css` are touched by most PRs — check every time.

### 2. In-flight deploy
```bash
gh run list --workflow=pages.yml -L 3 --json databaseId,status,conclusion,createdAt
```
A deploy still running → wait for it; the Pages concurrency group cancels it otherwise.

### 3. Recency
```bash
git fetch -q origin && git log origin/main --oneline -5 --format="%h %cr %an %s"
```
A commit from another session inside ~30 minutes means it may be mid-sequence: read its open PRs
before merging anything.

### 4. Review comments — every one, paginated
```bash
gh api --paginate repos/enrichmeai/enrichmeai.github.io/pulls/<PR>/comments \
  --jq '.[] | "[\(.user.login)] \(.path):\(.line // .original_line) — \(.body | gsub("\n";" "))"'
gh api --paginate repos/enrichmeai/enrichmeai.github.io/pulls/<PR>/reviews \
  --jq '.[] | select((.body // "") != "") | "[\(.user.login)/\(.state)] \(.body | gsub("\n";" "))"'
```
Bot reviews do not show in `gh pr checks`. Act on each comment or say why not, in a PR comment,
before merging. "The reviewer was wrong" is a fine answer; silence is not.

### 5. State the order before acting
Post a PR comment with the gate result and what you are about to merge, **before** merging. A
concurrent session reading the repo then sees intent, not just effects.

## Then verify, then merge
```bash
gh pr checks <PR>                         # Site check must be green on the CURRENT head
gh pr merge <PR> --squash --delete-branch
```
A head branch last updated days ago is refreshed first: `MERGEABLE` means no textual conflict,
never "the links still resolve". Update it and let `Site check` run again.

## Autonomy
Merge on your own once the gate passes and `Site check` is green, for: broken links or markup,
accessibility fixes, the checker, the hooks, and a claim corrected to match a product's release
tag with the source cited in the PR. **The founder merges**:
1. New or rewritten wording in his voice — a new page, a new section, a changed headline or
   positioning. The site speaks under his name.
2. Anything touching `CNAME`, `.github/workflows/`, or a process change that **removes** a check
   or loosens a rule. (One that only adds a check may be self-merged.)
3. A PR you did not open, without his word or a check-in with the session that owns it.
Dev-agents never merge.

## A merge is not done until the live site says so
```bash
gh run list --workflow=pages.yml -L 1        # wait for the deploy triggered by the merge
curl -fsS https://enrichmeai.com/<page>/ | grep -F "<a sentence the PR added>"
```
Quote the run ID and the matching line in the PR. A deploy that failed, or a page that does not
show the change, is reported on the PR at once — the site is live with whatever is on `main`.

Then sync local: `git fetch origin --prune`, fast-forward `main`, remove the merged worktree and
branch. If the fast-forward refuses, stop and say so; never reset over uncommitted work.
