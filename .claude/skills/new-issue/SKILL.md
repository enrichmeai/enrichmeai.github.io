---
name: new-issue
description: Turn a rough idea, bug report or page request for enrichmeai.com into ready-to-build GitHub issue(s) in the claude-task template's shape, de-duplicated, split to S/M size and labelled. Use for "new issue", "log this", "create a task for …", "turn this into issues", or when the founder describes site work in a sentence.
---

# /new-issue — from a sentence to ready issue(s)

The definition of **ready** is the `claude-task` template (`.github/ISSUE_TEMPLATE/claude-task.md`):
Goal · Measure · Evidence of done · Risk · Surface · Out of scope · Stop and ask if. `/groom` and
`/build-task` both rely on it, so every issue this skill writes fills every section — or says in
the section why it cannot yet.

## 1. De-duplicate first
`gh issue list -R enrichmeai/enrichmeai.github.io --search "<symptom words> in:title,body" --state all`
Search by **symptom, not diagnosis** ("penstock page says v0.1.1", not "version drift").
- An open near-duplicate → add the new information as a comment there; do not create.
- A closed one → read why it closed. Fixed and regressed → new issue that links it. Declined by a
  ruling → tell the founder, do not create.

## 2. Place it
- Wording, layout, links, brand assets, the checker, the hooks → **this repo**.
- The page is right but the product is wrong (a bug, a missing feature, a claim the code does not
  back yet) → the **product's repo** (`cistern`, `penstock`, `culvert`, `enrich-test-api`). This
  session does not write there: draft the issue for that repo's session and link it both ways.
- A page claim that follows a product change (new release, new coverage number) → one issue here
  that names the product tag it waits for under **Stop and ask if**.

## 3. Size and split
- **S/M** (≤ ½ day, one concern, usually one page): one issue.
- **Bigger** (a new product page, a redesign): a parent issue with an ordered checklist, plus
  sub-issues that each ship on their own.

## 4. Write it (claude-task template)
- **Goal** — one sentence, what a visitor will see or be able to do.
- **Measure** — e.g. site_check findings, broken links, a Lighthouse score, a claim now sourced.
- **Evidence of done** — the red check that fails on `main` today (a site_check case, a fixture
  in `scripts/site_check_test.sh`, or the exact wrong sentence quoted with the source that
  contradicts it), and the green proof.
- **Risk** — exactly one of docs / copy / code / deploy.
- **Surface** — the files, found with `grep`, not guessed.
- **Out of scope** and **Stop and ask if** — every question you could not answer from the page,
  the product repo or a founder ruling. Never invent an answer to fill a section.

## 5. Label, never dispatch
The owner (`claude-ready` / `founder`) and one `area:*` that already exists (`gh label list`).
**Never** add the `claude` label: that starts a paid build and is the founder's call.

## 6. Draft or create
Default: show the drafts and wait for "go". When the founder said "create" (or "just log it"):
`gh issue create -R enrichmeai/enrichmeai.github.io --title … --body-file … --label …`.
Reply with the links, the owner each got, and anything under "Stop and ask if".
