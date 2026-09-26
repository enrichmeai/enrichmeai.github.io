---
name: compound
description: Turn what went wrong (or was learned) in the site task just finished into a permanent guard, so the next task cannot repeat it. Use as the last step of every task before opening the PR — after the reviewer's verdict — and whenever the founder corrects you. Part of the /build-task loop.
---

# Compound: every mistake becomes a guard

A task is not finished when it works; it is finished when the next task is easier. This step is
short — usually one small addition, sometimes nothing — but it is never skipped silently.

## 1. Collect the lessons of this task
From this session only: every **reviewer finding**; every **hook or site_check failure** that took
more than one attempt; every **wrong assumption** (a claim, a CSS behaviour, a link you had to
correct after reading the source); every **founder correction**; anything that took **3 attempts**
or ended BLOCKED.

## 2. For each lesson, pick the strongest guard that fits — in this order
1. **A site_check rule** in `scripts/site_check.py` plus its fixture in
   `scripts/site_check_test.sh` — the fault becomes impossible to ship. Prove it RED first.
2. **A hook check** in `.claude/hooks/` (with a case in `test-hooks.sh`) — if a fast mechanical
   check would have caught it at edit time.
3. **A reviewer checklist line** in `.claude/agents/reviewer.md` — if only judgement catches it
   (tone, an over-claim, a caveat that went missing).
4. **A pinned doc URL** in CLAUDE.md § "Pinned docs" — if you had to search for the right doc.
5. **A CLAUDE.md rule** — one or two lines, in the section it belongs to, with the date and the
   issue/PR number. Last resort: prose is the weakest guard.
Skip a lesson only if an existing guard already covers it — name that guard.

## 3. Keep the guards lean
Grep for an existing rule before adding one; sharpen it rather than adding a second. Delete any
rule this lesson proves wrong. A small guard goes in the **same PR** as the fix; a larger one in
its own PR titled `compound: …`.

## 4. Record it
Add a `## Compound` section to the PR body: `lesson → guard added (file:line)` per lesson, or
`none — <why>` if the task went clean.
