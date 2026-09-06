# EnrichMeAI brand assets

One family, named for water: Cistern stores it, Penstock gates it, Culvert carries it.
Every mark is a stroked glyph on a 64-unit grid with an 8-unit margin, 4.5-unit stroke,
round caps and joins, on a square tile of one colour. The page that explains them is
[/brand/](https://enrichmeai.com/brand/).

| Brand | Tile | Files |
|---|---|---|
| EnrichMeAI | `#5980a6` steel blue | `enrichmeai-mark.svg`, `-mark-mono.svg`, `-lockup.svg`, `-lockup-light.svg`, `-wordmark.svg`, `-wordmark-light.svg` |
| Cistern | `#3d7c8a` still water | `cistern-mark.svg`, `-mark-mono.svg`, `-lockup.svg`, `-lockup-light.svg` |
| Penstock | `#a4712f` brass | `penstock-mark.svg`, `-mark-mono.svg`, `-lockup.svg`, `-lockup-light.svg` |
| Culvert | `#6e7466` concrete | `culvert-mark.svg`, `-mark-mono.svg`, `-lockup.svg`, `-lockup-light.svg` |
| Good Shepherd Software Consultancy | `#2e6b4e` pasture green | `goodshepherd-*.svg` (the company's own mark; used on goodshepherdconsultancy.com) |

- `*-mark.svg` is the tile version; `*-mark-mono.svg` draws in `currentColor` for inline use.
- `*-lockup.svg` sets the name in ink for light grounds; `*-lockup-light.svg` in near-white for dark.
- `png/` holds each mark at 512, 180 and 32 px (org avatar, apple-touch-icon, favicon) and each lockup at 128 px tall.
- `favicon.svg` is the EnrichMeAI mark. `symbols.svg` carries every glyph as an SVG `<symbol>` for inlining.

## Regenerating

Type is outlined from Barlow and Barlow Condensed (SIL OFL) with HarfBuzz shaping, so the
SVGs carry no font dependency. To rebuild after editing `generate.py`:

```bash
cd assets/brand
mkdir -p fonts && for f in barlowcondensed/BarlowCondensed-SemiBold.ttf barlowcondensed/BarlowCondensed-Bold.ttf barlow/Barlow-Medium.ttf barlow/Barlow-Regular.ttf; do
  curl -sL -o "fonts/$(basename $f)" "https://raw.githubusercontent.com/google/fonts/main/ofl/$f"; done
python3 -m venv .venv && .venv/bin/pip install -q fonttools uharfbuzz
.venv/bin/python generate.py      # needs rsvg-convert on PATH for the PNGs
```

`fonts/` and `.venv/` are build inputs, not assets; keep them out of the commit.
