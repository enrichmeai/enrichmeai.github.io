# CLAUDE.md — enrichmeai.github.io

The EnrichMeAI site: static HTML pages, one per project (`culvert/`, `cistern/`, `penstock/`,
`enrich-test-api/`), the register at `index.html`, `brand/`, and `assets/site.css`. `pages.yml` deploys
`main` to GitHub Pages; there is no build step.

## How changes move

One concern per PR, titled `site: …`, as the history shows. Every fact a page states about a project is
checked against that project's source or its registry, never copied from an older page. Say what a
project cannot do yet (see #18, "say on the page what the library cannot do"). Keep the layout at phone
width with no new horizontal scroll, and keep the colours on the tokens in `assets/site.css`.

## Culvert releases (Joseph, 2026-09-26)

**Every Culvert release reaches `/culvert/`: the new version, every new library, and the new features.**

- The page marks each fact it states (`data-culvert="pypi-version"`, `data-culvert="maven-version"`,
  a `data-culvert-artifact` row per library, `data-culvert-extra` per pip extra, and a
  `data-culvert-release` "what's new" block per release). `tools/check-culvert-page.py` compares those
  markers with PyPI, Maven Central and Culvert's `main`. Never hard-code a Culvert version outside a
  marker: the checker fails on it.
- `.github/workflows/culvert-sync.yml` runs the check every day and on every PR that touches the page.
  When the page is behind, it opens (or updates) one issue labelled `culvert-sync` that says what is
  missing, and it closes that issue once the page is back in step.
- The fix is the `/culvert-sync` skill (`.claude/skills/culvert-sync/SKILL.md`).

Run locally: `python3 tools/check-culvert-page.py --culvert ../gcp-pipeline-reference` (Joseph's local
Culvert folder; `../culvert` in a fresh clone). Tests: `python3 -m unittest tools/test_check_culvert_page.py`.
