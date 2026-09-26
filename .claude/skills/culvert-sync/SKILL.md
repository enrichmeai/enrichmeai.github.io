---
name: culvert-sync
description: Bring the /culvert/ page up to date with a Culvert release — new version numbers, a row for every new library, the pip extras, and a "what's new" block with the release's features from Culvert's CHANGELOG. Use when the `culvert-sync` issue is open, after a Culvert release, when a library is added to Culvert, or for "update the site for the release".
---

# /culvert-sync — the Culvert page follows every release

## 1. See what is behind
```bash
C=${CULVERT_DIR:-../gcp-pipeline-reference}; [ -d "$C" ] || C=../culvert
git -C "$C" fetch -q origin main && git -C "$C" checkout -q --detach origin/main
python3 tools/check-culvert-page.py --culvert "$C"
python3 tools/check-culvert-page.py --culvert "$C" --dump-facts
```
Each ERROR line is one thing to fix. If the facts could not be gathered (exit 2), the check did not run:
say so, never report it as passing.

## 2. Fix each kind of error, from the source, never from memory
- **A version marker is behind:** update the text of every `data-culvert="pypi-version"` /
  `"maven-version"` / `"artifact-version"` element to the registry value. Nothing else on the page
  should carry a version.
- **A new library has no row:** add a `<tr data-culvert-artifact="<artifactId>" data-state="released|unreleased">`
  in the Libraries table, in its area group (Core, GCP, AWS, Azure). Write "What it is" from the module's
  own `pom.xml` `<description>` and its public classes (`grep -rh "public .*class .* implements" <module>/src/main`):
  the cloud service, then the contract(s) it implements. A skeleton says it is a skeleton.
  Also update the contracts table (`#contracts`) and the Status "Clouds" row when a cloud gains an adapter.
- **A removed library:** delete its row, and every other mention of it.
- **Extras changed:** mirror `python-culvert/pyproject.toml` `[project.optional-dependencies]` in the
  Install block, one `data-culvert-extra` per extra, with a one-line comment of what it pulls in.
- **No "what's new" block for the newest release:** add `<section data-culvert-release="X.Y.Z">` at the
  top of `#whats-new`, above the older ones. Take the features from Culvert's `CHANGELOG.md` section
  for that version (Breaking, Added, the fixes a user would notice), rewritten in one or two plain
  sentences each. Say which ecosystem the release is in (Java on Maven Central, Python on PyPI, or
  both). Keep the older blocks.

## 3. Re-check, look, hand over
- `python3 tools/check-culvert-page.py --culvert "$C"` → 0 errors, and `python3 -m unittest tools/test_check_culvert_page.py`.
- Look at the page at 390 px and 1280 px wide (Playwright with `executablePath: '/opt/pw-browsers/chromium'`
  in the cloud). No new horizontal scroll.
- Branch `site/culvert-<version>`, one PR titled `site: Culvert <version> — …`, and `Closes #<culvert-sync issue>`.
  Joseph merges: the merge deploys the site.
