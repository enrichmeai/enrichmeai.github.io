# CLAUDE.md

enrichmeai.com: a static site. It has hand-written HTML pages, one stylesheet (`assets/site.css`)
and the brand assets. There is no build step. **A merge to `main` is a production deploy**:
`.github/workflows/pages.yml` publishes the repository to GitHub Pages on every push to `main`.

| Page | Path | About |
|---|---|---|
| Home | `index.html` | the register of products, how we build, services |
| Cistern | `cistern/index.html` | `enrichmeai/cistern` |
| Penstock | `penstock/index.html` | `enrichmeai/penstock` |
| Culvert | `culvert/index.html` | `enrichmeai/culvert` |
| enrich-test-api | `enrich-test-api/index.html` | `enrichmeai/enrich-test-api` |
| Brand | `brand/index.html` | `assets/brand/` (see its README) |

## Autonomous build loop (ported from enrichmeai/valuedocs, 2026-09-26)

**Claude builds, the `reviewer` agent verifies, and the founder merges or delegates the merge
through `merge-gate`.** The pipeline and how to port it to another repo are described in
[`docs/AUTONOMOUS_PIPELINE_BLUEPRINT.md`](docs/AUTONOMOUS_PIPELINE_BLUEPRINT.md).

`/new-issue` (idea → ready issue) → `/groom` (Site board) → `/build-task <issue>` → hooks on every
edit → `reviewer` → fix (max 3 attempts) → `/compound` → PR → `merge-gate` → live check

**The four rules. They are not negotiable:**
1. **Verify before you write.** Every factual claim about a product (a version, a number, a
   command, a licence, what works and what does not) is checked against that product's repo **at
   its latest release tag** before it goes on a page. Every HTML, CSS or browser behaviour you rely
   on is checked against § "Pinned docs". Never write from memory.
2. **Done means green.** A task is not done until `python3 scripts/site_check.py` reports 0
   findings, the `Site check` CI run on the PR is green (cite it), and every changed page has been
   looked at in a browser at 375 px and 1280 px. A gate that could not run is reported as not run,
   never as passing.
3. **Three attempts, then stop.** After 3 failed fix attempts at the same gate or reviewer finding,
   stop changing files and write the Blocker summary (format in `.claude/skills/build-task/SKILL.md` § 6).
4. **Pinned docs first.** Prefer the URLs below over open-ended search. When you had to find a new
   one, add it in the `/compound` step.

**Fast gates (exact commands):**

| Changed | Command |
|---|---|
| any page, CSS, SVG, JSON, YAML | `python3 scripts/site_check.py` (the whole site: a moved id breaks links on pages nobody edited) |
| `scripts/site_check*` | `scripts/site_check_test.sh` (add a fixture for every new rule, and prove it RED first) |
| `.claude/hooks/**`, `.claude/settings.json` | `.claude/hooks/test-hooks.sh` (add a case for every new guard, and prove it RED first) |
| a page's look | `python3 -m http.server 8000`, then screenshots at 375 px and 1280 px |
| everything | the `Site check` workflow on the PR runs all three scripted gates |

**Hooks (`.claude/settings.json`, scripts in `.claude/hooks/`)** feed errors straight back:
- **After each edit:** `site_check.py` on the edited page, stylesheet, SVG, JSON or YAML file,
  including its outbound links and `#anchors`. Python and shell files get a syntax check.
- **When the turn ends:** the whole-site check, plus the checker's and the hooks' own fixtures when
  those changed. It skips when nothing changed since the last clean run, blocks the stop at most
  once, and can be turned off with `CLAUDE_SKIP_STOP_GATES=1`.
- **Before a Bash command:** `guard-destructive.sh` asks for approval, even when an allow rule
  matches, before: force pushes, any push to `main` (that is a deploy), deleting refs or tags,
  `reset --hard`, `clean -f`, recursive `rm`, cloud CLIs, `gh release|workflow|secret|variable`,
  and a `gh api` call that writes. The cases are pinned in `.claude/hooks/test-hooks.sh`.

**Agents and models.** `reviewer` and `groomer` run on Sonnet. Use Opus for design work and new pages.

**Where things for the founder go.** Anything that needs the founder (a merge, a wording ruling, DNS)
goes on the PR or issue it belongs to, and `/groom` lists it in the Founder queue of the Site board.
Never post a secret or credential value anywhere on GitHub.

**One writer per repo.** One Claude session works in this repo at a time, and it changes files only
here. A product that needs to change becomes a `/new-issue` in that product's repo, linked from the
issue here. The page waits for the product's release tag. The GitHub Action builder (`claude`
label) counts as this repo's session, so do not start it while a session is working here.

**Reading the product repos.** Clone them side by side and read them at their tags:
```bash
cd .. && for r in cistern penstock culvert enrich-test-api; do [ -d $r ] || git clone https://github.com/enrichmeai/$r; done
git -C ../penstock fetch --tags && git -C ../penstock describe --tags --abbrev=0
```
Or start the session with `claude --add-dir ../penstock` (or `/add-dir` mid-session). A repo that
is not cloned has **not been checked**. Never describe a page's claims as verified without it.

### Pinned docs

Checked 2026-09-26. The row marked ✓ was fetched from this cloud environment. Its network policy
blocked the others, so the first session that can reach them re-checks them and removes this note.

| Area | Doc |
|---|---|
| HTML elements and attributes | https://developer.mozilla.org/en-US/docs/Web/HTML |
| HTML standard (parsing, optional end tags) | https://html.spec.whatwg.org/multipage/ |
| CSS | https://developer.mozilla.org/en-US/docs/Web/CSS |
| WCAG 2.2 | https://www.w3.org/TR/WCAG22/ |
| GitHub Pages with a custom workflow | https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages |
| actions/upload-pages-artifact | https://github.com/actions/upload-pages-artifact |
| GitHub Actions workflow syntax | https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions |
| claude-code-action | https://github.com/anthropics/claude-code-action |
| Claude Code hooks, subagents, permissions ✓ | https://code.claude.com/docs/en/hooks · https://code.claude.com/docs/en/sub-agents · https://code.claude.com/docs/en/permissions |

If a source cannot be read, the "verify before you write" gate **did not run**. Say so and treat
it as a blocker.

## Voice

The site's claim is that nothing was announced before it ran. Every page keeps that promise.
- A page never runs ahead of the product's release tag. "Planned" work is named as planned, and
  it does not appear in a headline.
- The caveat blocks ("what it cannot do", honest status) are part of the product and not decoration.
  Removing one needs the product to have changed, with the tag cited.
- Plain and specific: a number with its source beats an adjective. No superlatives.
- New or rewritten wording in the founder's voice (a headline, positioning, a new section) is
  merged by the founder (`merge-gate` § Autonomy).

## Conventions

- Colours come from the `var(--color-*)` tokens in `assets/site.css`. Do not add raw hex values to pages.
- Every page has `lang`, a `<title>`, a meta description, a viewport meta, the favicon and the
  apple-touch-icon. `site_check.py` enforces the first four.
- Brand SVGs are generated. Edit `assets/brand/generate.py` and regenerate (its README), and
  never hand-edit the SVG output.
- Branches are named `site/<issue>-<slug>`. Each branch holds one concern. Open the PR within about 30
  minutes of the first commit. A branch lives no longer than 24 h.
- Commit subjects follow the existing `site: <what a visitor will notice>` style.
