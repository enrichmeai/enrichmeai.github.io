# Well Rounded Engineer: source and build

The guide at [/well-rounded-engineer/](https://enrichmeai.com/well-rounded-engineer/) is generated.
Do not hand-edit `well-rounded-engineer/**/index.html` or `search.json`: edit the source here and rebuild.

| File | What it is |
|---|---|
| `guide.html.in` | The single-file source: every section is a `<section class="panel" id="p-<tab>">`, and links between sections are written `href="#<tab>"`. It also opens on its own in a browser as a one-page guide (the claude.ai artifact is published from it). The `.in` suffix keeps `scripts/site_check.py` off it, since its `#tab` links only resolve once the pages are built. |
| `build.py` | Rebuilds, inside `guide.html.in`, the section nav and its groups, the "Levels" and "Explore further" cards of every section, and Start here's tables, from the lists at its top and `levels_data.py`. Running it twice changes nothing. |
| `levels_data.py` | Per-section levels (Foundation to Expert), topics to study and links. |
| `to_site_pages.py` | Writes `/well-rounded-engineer/`: a page per section, `search.json` for search, and the redirect from old `#tab` links. It refuses a source that names a private repository or states a Culvert version, and marks the example versions in snippets `data-other-version` for the release checker. |
| `engineer.js` | The pages' script (copy buttons, search, the tab row). Copy it to `well-rounded-engineer/engineer.js` when it changes. The stylesheet lives at `well-rounded-engineer/engineer.css`. |

## Change the guide

1. Edit `guide.html.in`. To add a section: write its `<section>`, add it to `groups` and `labels` in `build.py`, give it an entry in `levels_data.py` (and a row in `build.py`'s `newrows` unless it is one of the opening pages).
2. Rebuild, from the repository root:

   ```bash
   python3 tools/well-rounded-engineer/build.py
   python3 tools/well-rounded-engineer/to_site_pages.py
   ```

3. Check, as for any page change (`CLAUDE.md`, rule 2):

   ```bash
   python3 scripts/site_check.py
   python3 -m unittest tools/test_check_release_page.py
   python3 tools/check-release-page.py culvert --repo ../culvert
   ```

   and look at the changed pages at 375 px and 1280 px (`python3 -m http.server 8000`).

Every claim follows the site's rule 1: checked against its source (a product at its latest release tag, a standard
at its own text) before it goes in, and written as the founder's memory where it cannot be sourced.
