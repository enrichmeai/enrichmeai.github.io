---
name: release-sync
description: Bring a project page (/culvert/, /enrich-test-api/) up to date with that project's latest release or main branch — version markers, a row for every new library, pip extras, capabilities, and a "what's new" block from the project's CHANGELOG. Use when a `<project>-sync` issue is open, after a release, when a library or capability is added, or for "update the site for the release". Argument: the project (culvert | enrich-test-api).
---

# /release-sync <project> — the page follows every release

Projects and their markers are defined in `PROJECTS` in `tools/check-release-page.py`. Each page marks
the facts it states with its prefix (`data-culvert`, `data-eta`), so the checker can compare them.

## 1. See what is behind
```bash
P=<project>                                    # culvert | enrich-test-api
R=${REPO_DIR:-../$P}; [ "$P" = culvert ] && [ -d ../gcp-pipeline-reference ] && R=../gcp-pipeline-reference
[ -d "$R" ] || git clone -q --depth 1 https://github.com/enrichmeai/$P "$R"
git -C "$R" fetch -q origin main && git -C "$R" checkout -q --detach origin/main
python3 tools/check-release-page.py $P --repo "$R"
python3 tools/check-release-page.py $P --repo "$R" --dump-facts
```
Each ERROR line is one thing to fix. Exit 2 means the facts could not be gathered: the check did not run.
Say so, never report it as passing.

## 2. Fix each kind of error, from the source, never from memory
- **A version marker is behind** (`maven-version`, `pypi-version`, `main-version`, `next-version`,
  `artifact-version`): update its text. Nothing else on the page may carry a version.
- **A new library has no row:** add an element with `<prefix>-artifact="<artifactId>"` and
  `data-state="released|unreleased"` beside the others. Describe it from its `pom.xml` `<description>`
  and its public classes: the service, then the contract or capability it implements. A skeleton says so.
- **A removed library:** delete its row and every other mention of it.
- **Extras or capabilities changed:** mirror the source exactly (`python-culvert/pyproject.toml` extras;
  enrich-test-api's `test-core/.../capability/*` interfaces). A new capability gets its own row saying what
  it does and which service backs it on each provider, with an honest status tag.
- **The newest release has no "what's new" block:** add `<section <prefix>-release="X.Y.Z">` at the top of
  the page's what's-new section, written from the project's `CHANGELOG.md` for that version (Breaking,
  Added, the fixes a user would notice), one or two plain sentences each, naming the ecosystem.
  enrich-test-api's first release also turns its "unpublished" wording (hero caveat, Distribution row,
  FAQ "Can I use this today?", and its entry in the register on `/index.html`) into install instructions,
  and it needs a what's-new section: add one in the style of `/culvert/#whats-new`.
- A new project page: add its entry to `PROJECTS`, its markers to the page, test cases to
  `tools/test_check_release_page.py`, and its name to the matrix in `release-sync.yml`.

## 3. Re-check, look, hand over
- `python3 tools/check-release-page.py $P --repo "$R"` → 0 errors, and `python3 -m unittest tools/test_check_release_page.py`.
- `python3 scripts/site_check.py` → 0 findings (the site's own gate: markup, ids, links, anchors).
- Look at the page at 375 px and 1280 px (Playwright; in the cloud `executablePath: '/opt/pw-browsers/chromium'`).
  No new horizontal scroll.
- Then the site loop's own steps: the `reviewer` agent, `/compound`, and one PR titled `site: <project> <version> — …`
  with `Closes #<the sync issue>`. The founder merges (or delegates through `merge-gate`); the merge deploys.
