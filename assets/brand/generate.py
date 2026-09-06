#!/usr/bin/env python3
"""Generate the EnrichMeAI / Good Shepherd brand family.

Marks are drawn on a 64-unit grid as stroked glyphs so they survive 16 px.
Wordmarks are outlined from the Barlow fonts (OFL) via HarfBuzz shaping, so the
SVGs carry no font dependency.  Outputs land in out/brand/.
"""
import os, shutil, subprocess, json
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

try:
    import uharfbuzz as hb
except ImportError:  # advances-only fallback
    hb = None

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = HERE
FONTS = os.path.join(HERE, "fonts")
os.makedirs(os.path.join(OUT, "png"), exist_ok=True)

INK = "#1d1f20"        # enrichmeai --color-text
LIGHT = "#f5f5f8"      # enrichmeai --color-neutral-100
STROKE = 4.5

# ── Brand definitions ──────────────────────────────────────────────────────────
# Each glyph: list of (kind, data) where kind ∈ {"path", "dot"}.
BRANDS = {
    "enrichmeai": {
        "title": "EnrichMeAI",
        "tile": "#5980a6",   # steel blue — the existing site accent
        "role": "The umbrella. A drop of water, and the point where it is accounted for.",
        "glyph": [
            ("path", "M32 10 C32 10 14.5 29.5 14.5 41 A17.5 17.5 0 0 0 49.5 41 C49.5 29.5 32 10 32 10 Z"),
            ("dot", (32, 42, 5)),
        ],
        "stroke": STROKE,
    },
    "cistern": {
        "title": "Cistern",
        "tile": "#3d7c8a",   # still-water teal
        "role": "The store. A tank with its inlet and the level inside it.",
        "glyph": [
            ("path", "M32 9 V19"),
            ("path", "M17 19 H47 A4 4 0 0 1 51 23 V48 A4 4 0 0 1 47 52 H17 A4 4 0 0 1 13 48 V23 A4 4 0 0 1 17 19 Z"),
            ("path", "M19 38 Q22.25 34 25.5 38 T32 38 T38.5 38 T45 38"),
        ],
        "stroke": STROKE,
    },
    "penstock": {
        "title": "Penstock",
        "tile": "#a4712f",   # brass — the valve
        "role": "The gate. A channel, a gate lowered into it, and the flow it holds.",
        "glyph": [
            ("path", "M10 24 H54"),
            ("path", "M10 44 H54"),
            ("path", "M32 10 V38"),
            ("path", "M25 10 H39"),
            ("path", "M15 34 H25"),
        ],
        "stroke": STROKE,
    },
    "culvert": {
        "title": "Culvert",
        "tile": "#6e7466",   # concrete
        "role": "The channel. An arch carrying water under the road above it.",
        "glyph": [
            ("path", "M9 13 H55"),
            ("path", "M17 51 V37 A15 15 0 0 1 47 37 V51"),
            ("path", "M9 51 H55"),
            ("path", "M24 45 H40"),
        ],
        "stroke": STROKE,
    },
    "goodshepherd": {
        "title": "Good Shepherd Software Consultancy",
        "tile": "#2e6b4e",   # pasture green
        "role": "The company. A shepherd's crook, drawn in one stroke.",
        "glyph": [
            ("path", "M38 57 V21.5 A10.5 10.5 0 0 0 17 21.5 V28"),
        ],
        "stroke": 5,
    },
}

# ── Font shaping ───────────────────────────────────────────────────────────────
_font_cache = {}

def _load(fname):
    if fname not in _font_cache:
        path = os.path.join(FONTS, fname)
        tt = TTFont(path)
        hbf = None
        if hb is not None:
            blob = hb.Blob.from_file_path(path)
            face = hb.Face(blob)
            hbf = hb.Font(face)
        _font_cache[fname] = (tt, hbf)
    return _font_cache[fname]

def text_path(fname, text, size, x, baseline, tracking=0.0):
    """Return (svg path d, end x) for `text` set at `size` px with baseline at y."""
    tt, hbf = _load(fname)
    upem = tt["head"].unitsPerEm
    scale = size / upem
    gs = tt.getGlyphSet()
    order = tt.getGlyphOrder()
    parts = []
    cx = x
    if hbf is not None:
        buf = hb.Buffer(); buf.add_str(text); buf.guess_segment_properties()
        hb.shape(hbf, buf, {"kern": True, "liga": True})
        for info, pos in zip(buf.glyph_infos, buf.glyph_positions):
            gname = order[info.codepoint]
            pen = SVGPathPen(gs)
            tpen = TransformPen(pen, (scale, 0, 0, -scale, cx + pos.x_offset * scale, baseline - pos.y_offset * scale))
            gs[gname].draw(tpen)
            d = pen.getCommands()
            if d:
                parts.append(d)
            cx += pos.x_advance * scale + tracking
    else:
        cmap = tt.getBestCmap(); hmtx = tt["hmtx"]
        for ch in text:
            gname = cmap[ord(ch)]
            pen = SVGPathPen(gs)
            tpen = TransformPen(pen, (scale, 0, 0, -scale, cx, baseline))
            gs[gname].draw(tpen)
            d = pen.getCommands()
            if d:
                parts.append(d)
            cx += hmtx[gname][0] * scale + tracking
    return " ".join(parts), cx

# ── SVG builders ───────────────────────────────────────────────────────────────
def glyph_svg(b, stroke_color):
    sw = b["stroke"]
    out = []
    for kind, data in b["glyph"]:
        if kind == "path":
            out.append(f'<path d="{data}" fill="none" stroke="{stroke_color}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"/>')
        else:
            cx, cy, r = data
            out.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{stroke_color}"/>')
    return "\n  ".join(out)

def mark_svg(name, b):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64" role="img" aria-label="{b["title"]} mark">\n'
            f'  <rect width="64" height="64" fill="{b["tile"]}"/>\n  {glyph_svg(b, LIGHT)}\n</svg>\n')

def mark_mono_svg(name, b):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64" role="img" aria-label="{b["title"]} mark">\n'
            f'  {glyph_svg(b, "currentColor")}\n</svg>\n')

def symbol(name, b):
    return f'<symbol id="glyph-{name}" viewBox="0 0 64 64">{glyph_svg(b, "currentColor")}</symbol>'

def lockup_svg(name, b, text_color, accent):
    """Tile mark + outlined name. Returns svg string."""
    GAP = 18
    x0 = 64 + GAP
    paths = []
    if name == "enrichmeai":
        # enrichme·ai — Barlow Condensed Bold, lowercase, the dot in accent (matches the site header)
        d1, x1 = text_path("BarlowCondensed-Bold.ttf", "enrichme", 56, x0, 49)
        dd, x2 = text_path("BarlowCondensed-Bold.ttf", "·", 56, x1, 49)
        d2, x3 = text_path("BarlowCondensed-Bold.ttf", "ai", 56, x2, 49)
        paths.append(f'<path d="{d1}" fill="{text_color}"/>')
        paths.append(f'<path d="{dd}" fill="{accent}"/>')
        paths.append(f'<path d="{d2}" fill="{text_color}"/>')
        width = x3 + 6
    elif name == "goodshepherd":
        d1, x1 = text_path("BarlowCondensed-SemiBold.ttf", "Good Shepherd", 38, x0, 33)
        d2, x2 = text_path("Barlow-Medium.ttf", "SOFTWARE CONSULTANCY", 14.5, x0 + 1, 54, tracking=2.2)
        paths.append(f'<path d="{d1}" fill="{text_color}"/>')
        paths.append(f'<path d="{d2}" fill="{text_color}" fill-opacity="0.78"/>')
        width = max(x1, x2) + 6
    else:
        d1, x1 = text_path("BarlowCondensed-SemiBold.ttf", b["title"], 48, x0, 49)
        paths.append(f'<path d="{d1}" fill="{text_color}"/>')
        width = x1 + 6
    width = round(width, 1)
    body = "\n  ".join(paths)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} 64" width="{width}" height="64" role="img" aria-label="{b["title"]}">\n'
            f'  <rect width="64" height="64" fill="{b["tile"]}"/>\n  {glyph_svg(b, LIGHT)}\n  {body}\n</svg>\n'), width

def wordmark_only_svg(name, b, text_color, accent):
    """Text-only wordmark (no tile), for the enrichmeai header etc."""
    if name != "enrichmeai":
        return None
    d1, x1 = text_path("BarlowCondensed-Bold.ttf", "enrichme", 56, 2, 49)
    dd, x2 = text_path("BarlowCondensed-Bold.ttf", "·", 56, x1, 49)
    d2, x3 = text_path("BarlowCondensed-Bold.ttf", "ai", 56, x2, 49)
    width = round(x3 + 4, 1)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} 64" width="{width}" height="64" role="img" aria-label="enrichme·ai">\n'
            f'  <path d="{d1}" fill="{text_color}"/>\n  <path d="{dd}" fill="{accent}"/>\n  <path d="{d2}" fill="{text_color}"/>\n</svg>\n')

# ── Emit ───────────────────────────────────────────────────────────────────────
def write(rel, s):
    p = os.path.join(OUT, rel)
    with open(p, "w") as f:
        f.write(s)
    return p

def png(svg_rel, size, png_rel):
    subprocess.run(["rsvg-convert", "-w", str(size), "-h", str(size),
                    os.path.join(OUT, svg_rel), "-o", os.path.join(OUT, png_rel)], check=True)

symbols = []
manifest = {}
for name, b in BRANDS.items():
    accent = BRANDS["enrichmeai"]["tile"]
    write(f"{name}-mark.svg", mark_svg(name, b))
    write(f"{name}-mark-mono.svg", mark_mono_svg(name, b))
    lk, w = lockup_svg(name, b, INK, accent)
    write(f"{name}-lockup.svg", lk)
    lkl, _ = lockup_svg(name, b, LIGHT, "#94bce3" if name == "enrichmeai" else accent)
    write(f"{name}-lockup-light.svg", lkl)
    wm = wordmark_only_svg(name, b, INK, accent)
    if wm:
        write(f"{name}-wordmark.svg", wm)
        write(f"{name}-wordmark-light.svg", wordmark_only_svg(name, b, LIGHT, "#94bce3"))
    for size in (512, 180, 32):
        png(f"{name}-mark.svg", size, f"png/{name}-mark-{size}.png")
    subprocess.run(["rsvg-convert", "-h", "128", os.path.join(OUT, f"{name}-lockup.svg"),
                    "-o", os.path.join(OUT, "png", f"{name}-lockup.png")], check=True)
    symbols.append(symbol(name, b))
    manifest[name] = {"title": b["title"], "tile": b["tile"], "role": b["role"], "lockup_width": w}

shutil.copyfile(os.path.join(OUT, "enrichmeai-mark.svg"), os.path.join(OUT, "favicon.svg"))
write("symbols.svg", '<svg xmlns="http://www.w3.org/2000/svg" style="display:none" aria-hidden="true">\n  ' + "\n  ".join(symbols) + "\n</svg>\n")
with open(os.path.join(OUT, "manifest.json"), "w") as f:
    json.dump(manifest, f, indent=2)
print("shaping:", "harfbuzz" if hb else "advances-only")
for name, m in manifest.items():
    print(f"{name:14s} tile {m['tile']}  lockup width {m['lockup_width']}")
