# Autonomous workflow pipeline: the blueprint

This describes the build loop that `enrichmeai/valuedocs` runs (its CLAUDE.md § "Autonomous build
loop", `docs/DEV_PROCESS.md`, `.claude/`). It also shows how this repository ports that loop, and
how to port it to another repository. The parts are the same everywhere. What changes per repo is
the **gates** (what "green" means) and the **risks** (what only a human may release).

## The loop

```
idea ──/new-issue──▶ ready issue ──/groom──▶ board (Claude queue · Founder queue)
                                                   │
                         /build-task <issue>  ◀────┘   (or the `claude` label → GitHub Action)
                                │
   claim ▶ branch off origin/main ▶ verify sources ▶ RED check ▶ implement
                                │        ▲
                    hooks on every edit ─┘  (PostToolUse: file check · Stop: whole-repo gates)
                                │
                  reviewer agent ─▶ fix (≤ 3 attempts, else Blocker summary)
                                │
                  /compound (lesson → strongest guard) ─▶ draft PR ─▶ CI green ─▶ ready
                                │
                  merge-gate (overlap · in-flight deploy · recency · review comments · intent)
                                │
                  merge (autonomous within its risk class) ─▶ post-merge check ─▶ sync local
```

## The four rules

1. **Verify before you write.** External facts (APIs, flags, versions, and on this site the product
   claims) are checked against a pinned source at the version in use. They are never recalled from memory.
2. **Done means green.** A task is done when the fast gates pass locally and CI passes on the PR. A gate that did not
   run is reported as not run.
3. **Three attempts, then stop.** After that, write a Blocker summary: what was tried, the evidence, a hypothesis, and what is needed.
4. **Pinned docs first.** A short list of vetted URLs beats open-ended search, and it grows through `/compound`.

## Components

| Component | valuedocs | this site | Purpose |
|---|---|---|---|
| Rules and gates | `CLAUDE.md` § Autonomous build loop | `CLAUDE.md` § Autonomous build loop | the contract every session loads |
| Ready definition | `.github/ISSUE_TEMPLATE/claude-task.md` | same file, with site risks | Goal · Measure · Evidence · Risk · Surface · Out of scope · Stop-and-ask |
| Intake | `new-issue` skill | `new-issue` skill | de-duplicates, places, sizes and labels the issue. It never dispatches |
| Backlog | `groom` skill + `groomer` agent → Go-live board | `groom` → Site board, plus a claim-drift check | a single place that says what is next and who does it |
| Build | `build-task` skill (+ `ship-change`) | `build-task` skill | spec → verify → red → green → review → compound → PR |
| Edit-time check | `post-edit-check.sh`: ESLint, tsc, JSON/YAML/Py | `post-edit-check.sh`: `site_check.py`, Py/sh syntax | catches the error on the edit that caused it |
| Turn-end check | `stop-fast-gates.sh`: `compileTestJava`, fast pytest | `stop-fast-gates.sh`: whole-site check + fixtures | nothing ends a turn red. It blocks once, then warns |
| Command guard | `guard-destructive.sh` + `ask` rules | same, minus Gradle; push to main = deploy | destructive or prod commands always prompt |
| Guard tests | `.claude/hooks/test-hooks.sh` | same, with site fixtures | the guards are proven RED, so they cannot silently regress |
| Review | `reviewer` agent (Sonnet) | `reviewer` agent: claims, voice, markup, a11y, layout | an independent, read-only verdict in a fixed shape |
| Learning | `compound` skill | `compound` skill | each mistake becomes a test, a hook, a checklist line or a doc pin |
| Merge | `merge-gate` skill (six checks, sprint branch) | `merge-gate` (five checks + live-site check) | coordination across sessions sharing one `main` |
| CI | `Run Tests`, `Work surface` (collisions, acceptance) | `Site check` | the same gates, run where nobody's laptop matters |
| Headless builder | `.github/workflows/claude.yml` | `.github/workflows/claude.yml` | founder-only trigger, no merge/deploy/workflow edits, SHA-pinned action |
| PR shape | `.github/pull_request_template.md` | same, with Sources and Compound | one issue threads the branch, the PR and the evidence |

## Porting it to another repository

1. **Copy the invariant parts unchanged:** `guard-destructive.sh` and its test cases, the `compound`
   skill, the Blocker summary format, the `claude.yml` shape (only the actor and the disallowed tools change),
   and the PR and issue templates.
2. **Define the fast gates.** List the commands that finish in seconds to a couple of minutes and prove the edited
   thing is not broken (lint, typecheck, compile, a checker). Put them in `post-edit-check.sh`
   (one file) and `stop-fast-gates.sh` (the change set). Full suites stay in CI.
3. **Give every gate fixtures that prove it RED.** A gate that has only been seen green is not a gate. See
   `scripts/site_check_test.sh` and `.claude/hooks/test-hooks.sh`.
4. **Name the risk classes** in the issue template, and decide in `merge-gate` § Autonomy which ones
   Claude may merge. Changes that are prod, deploy or process-loosening always go to the human.
5. **Write the reviewer's checklist** for what only judgement catches in this repo, such as schema ownership in
   valuedocs, or claim sourcing and voice on this site.
6. **Pin the docs** at the versions the build resolves. Mark each one ✓ only once it has actually been fetched.
7. **One writer per repo.** A change another repo owns becomes an issue there, and the owning side lands first.

## Deliberate differences from valuedocs

- **No sprint branch.** valuedocs integrates on `sprint-N` and releases to `bld` first. This site has
  no staging, so `merge-gate` ends with a live-site check (the Pages run and a `curl` of the page).
- **No work-surface or acceptance scripts yet.** Those scripts exist for many concurrent sessions on one
  large repo. Add them here if more than one session starts working on the site.
- **Claims are the risky surface**, not schema or infrastructure. The gate for a claim is the product repo at
  its release tag, read from a clone next to this one.

## Known gaps (founder actions)

- `pages.yml` uploads the whole repository, so `CLAUDE.md`, `docs/`, `scripts/` and `.claude/` are
  also served on enrichmeai.com. The repository is public, so nothing new is exposed, but a
  publish step that ships only the site files would be tidier. That is a deploy change, so the founder decides.
- `claude.yml` needs the `CLAUDE_CODE_OAUTH_TOKEN` secret, and branch protection on `main` should
  require `Site check`. Both are repository settings.
- Labels `claude`, `claude-ready`, `founder`, `board` and `area:*` need to exist (`gh label create`).
