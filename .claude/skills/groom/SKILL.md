---
name: groom
description: Review every open issue and PR on enrichmeai.github.io and rewrite the Site board issue — what Claude can take next, what only the founder can do, and which page claims have drifted from the product repos. Use for "groom", "what's pending on the site", "what should I do next", or before picking the next task. Incremental after the first run.
---

# Grooming the site backlog

One pass answers three questions for the founder: **what is wrong on the live site, what Claude
can take next without him, and what only he can do.** The output is one GitHub issue — the
**Site board** (title starts `Site board`, label `board`) — rewritten on every run, so the answer
always lives in one place and survives every session. It never changes code.

## Rules
- **Labels, not new taxonomy.** Owner labels `claude-ready` (buildable unattended, a check can
  prove it) and `founder` (wording in his voice, accounts, DNS, money, a ruling), plus `area:*`.
- **Safe writes happen; closures wait.** The run may add/remove the labels above and post one
  grooming comment per item. It never closes, merges or edits an issue body. Closures are proposed
  on the board as checkboxes; the founder ticks them; the NEXT run closes ticked ones with a
  one-line comment naming the evidence.
- **Evidence or it did not happen.** "Already fixed" needs the merged PR or SHA. "Duplicate" needs
  the other number. "Obsolete" needs the ruling or the deleted page.
- **Usage cap:** more than ~25 open items → fan out to the `groomer` agent in batches of ≤25.
  Later runs groom only items updated since the board's `last-groomed` stamp.

## 1. Snapshot
```bash
R=enrichmeai/enrichmeai.github.io
gh issue list -R $R --state open --limit 200 --json number,title,labels,updatedAt,body,comments
gh pr list -R $R --state open --limit 50 --json number,title,isDraft,updatedAt,headRefName,mergeable,statusCheckRollup,closingIssuesReferences
gh issue list -R $R --label board --state open      # last-groomed stamp, ticked closures
```

## 2. Close what the founder ticked
Re-check each `- [x] close …` line's evidence, then `gh issue close N --reason … --comment …`.
Report anything whose evidence no longer holds instead of closing it.

## 3. Claim drift — the check only this repo needs
Every product page states facts about another repo: a version, a coverage number, a licence, what
works and what does not. For each page, compare those against the product's **latest release
tag** (sibling clones side by side: `../cistern`, `../penstock`, `../culvert`,
`../enrich-test-api`; `git -C ../<repo> fetch --tags && git -C ../<repo> describe --tags --abbrev=0`).
A claim the tag no longer backs becomes a `claude-ready` issue via `/new-issue`, quoting the
sentence and the source. A repo that is not cloned locally is listed as **not checked**, never
as clean.

## 4. Rewrite the board
Body, in this order (scannable on a phone):
1. `last-groomed: <UTC> · main <sha> · live deploy <run id and conclusion>`
2. **Live site** — site_check on `main` (findings count), last Pages deploy, claim drift found.
3. **Founder queue** — each item with the exact next action.
4. **Claude queue (next 5)** — `claude-ready` issues in build order with size. `/build-task` takes the first.
5. **Needs grooming** — the missing template section named.
6. **Proposed closures** — `- [ ] close #N — <duplicate of|fixed by|obsolete because> <evidence>`.
7. **Open PRs** — draft/ready, checks, mergeable, stale (>24 h), what each closes.

Create with `gh issue create --title "Site board (do not close)" --label board --body-file …`,
update with `gh issue edit <n> --body-file …`. Reply to the founder with sections 2–4 only.

## Optional: dispatch
`/groom dispatch N` adds the `claude` label to the top N of the Claude queue, which starts the
GitHub Action builder (one at a time). Only on explicit request: each dispatch spends usage.
