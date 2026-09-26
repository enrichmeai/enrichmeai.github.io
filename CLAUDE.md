# CLAUDE.md — enrichmeai.github.io

The EnrichMeAI site: static HTML pages, one per project (`culvert/`, `cistern/`, `penstock/`,
`enrich-test-api/`), the register at `index.html`, `brand/`, and `assets/site.css`. `pages.yml` deploys
`main` to GitHub Pages; there is no build step.

## How changes move

One concern per PR, titled `site: …`, as the history shows. Every fact a page states about a project is
checked against that project's source or its registry, never copied from an older page. Say what a
project cannot do yet (see #18, "say on the page what the library cannot do"). Keep the layout at phone
width with no new horizontal scroll, and keep the colours on the tokens in `assets/site.css`.

## Project releases (Joseph, 2026-09-26)

**Every release of a project reaches its page: the new version, every new library, and the new features.**
Covered today: Culvert (`/culvert/`) and enrich-test-api (`/enrich-test-api/`).

- Each page marks the facts it states (prefix `data-culvert` / `data-eta`): the released versions, the
  version on main, one row per library, the pip extras or the capabilities, and a "what's new" block per
  release. `tools/check-release-page.py <project>` compares those markers with Maven Central, PyPI and
  the project's `main`. Never hard-code a project version outside a marker: the checker fails on it.
- `.github/workflows/release-sync.yml` runs the check every day and on every PR that touches a page.
  When a page is behind, it opens (or updates) one issue labelled `<project>-sync` saying what is missing,
  and closes it once the page is back in step.
- The fix is the `/release-sync <project>` skill (`.claude/skills/release-sync/SKILL.md`). Adding the
  `claude` label to the sync issue has the builder (`.github/workflows/claude.yml`) do it.

Run locally: `python3 tools/check-release-page.py culvert --repo ../gcp-pipeline-reference` (Joseph's local
Culvert folder), `python3 tools/check-release-page.py enrich-test-api --repo ../enrich-test-api`.
Tests: `python3 -m unittest tools/test_check_release_page.py`.
