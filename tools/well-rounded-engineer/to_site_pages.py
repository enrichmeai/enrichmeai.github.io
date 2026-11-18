# Build /well-rounded-engineer/ (a page per section, search.json) from guide.html.in. See README.md.
import re, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, 'guide.html.in')).read()
out_dir = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, '..', '..', 'well-rounded-engineer')

nav = re.search(r'    <nav aria-label="Sections">.*?</nav>', src, re.S).group(0)
mstart = src.index('<main class="wrap">') + len('<main class="wrap">')
mend = src.index('<p class="empty" id="empty"')
body = src[mstart:mend]
script = re.search(r'<script>(.*?)</script>', src, re.S).group(1)

# section ids become the tab ids, so every #tab link resolves to an element on the page
body = re.sub(r'<section class="panel" id="p-([a-z0-9]+)"', r'<section class="panel" id="\1"', body)
script = script.replace('document.getElementById("p-"+t)', 'document.getElementById(t)')
assert 'document.getElementById(t)' in script

# the source must name no private repository and state no Culvert version (the Culvert page keeps it)
assert 'valuedocs' not in body.lower(), 'private repo name in the guide'
assert '0.6.1' not in body

# Versions in example snippets belong to no project: mark them, so the release checker
# (tools/check-release-page.py, culvert "also") can fail on any other version on this page.
def _ov(v): return f'<span data-other-version>{v}</span>'
other = [
 ('version: 0.3.0             # chart version', None, '0.3.0'),
 ('shop-api-0.3.0.tgz', 2, '0.3.0'),
 ('--version 0.3.0</code>', None, '0.3.0'),
 ('pragma solidity ^0.8.24;', None, '0.8.24'),
 ('version: 1.2.0 }', None, '1.2.0'),
 ('openapi: 3.1.0', None, '3.1.0'),
 ('?ref=v1.4.0"', None, 'v1.4.0'),
 ('&lt;modelVersion&gt;4.0.0&lt;/modelVersion&gt;', None, '4.0.0'),
 ('&lt;version&gt;1.0.0-SNAPSHOT&lt;/version&gt;', None, '1.0.0-SNAPSHOT'),
 ('&lt;version&gt;5.11.0&lt;/version&gt;', None, '5.11.0'),
 ('junit = "5.11.0"', None, '5.11.0'),
 ('"express": "^5.1.0"', None, '5.1.0'),
 ('"lodash": "~4.17.21"', None, '4.17.21'),
]
for ctx, count, v in other:
    n = body.count(ctx)
    assert n == (count or 1), (ctx, n)
    body = body.replace(ctx, ctx.replace(v, _ov(v)))


# ---------------------------------------------------------------- split into pages
import html as _html, json, os
BASE = '/well-rounded-engineer/'
SMILE = '<svg class="eg-smile" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="10" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="8.5" cy="9.5" r="1.4" fill="currentColor"/><circle cx="15.5" cy="9.5" r="1.4" fill="currentColor"/><path d="M7.5 14.2c1.1 1.8 2.6 2.8 4.5 2.8s3.4-1 4.5-2.8" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>'

order = re.findall(r'<a href="#([a-z0-9]+)" data-tab="\1">', nav)
labels = dict(re.findall(r'<a href="#([a-z0-9]+)" data-tab="\1">([^<]+)</a>', nav))
sections = {m.group(1): m.group(0) for m in re.finditer(r'<section class="panel" id="([a-z0-9]+)".*?</section>', body, re.S)}
assert order and set(order) == set(sections), set(order) ^ set(sections)

def url(t):
    return BASE if t == 'start' else f'{BASE}{t}/'

def relink(h):
    # a #tab link becomes a link to that tab's page
    return re.sub(r'href="#([a-z0-9]+)"', lambda m: f'href="{url(m.group(1))}"' if m.group(1) in sections else m.group(0), h)

def text(h):
    h = re.sub(r'<(script|style)\b.*?</\1>', ' ', h, flags=re.S)
    return re.sub(r'\s+', ' ', _html.unescape(re.sub(r'<[^>]+>', ' ', h))).strip()

# the nav's groups, in order: [(group name or '', [tab, ...])]
nav_groups, _g = [], ['', []]
for m in re.finditer(r'<span class="navgrp">([^<]+)</span>|<a href="#([a-z0-9]+)" data-tab="\2">', nav):
    if m.group(1):
        if _g[1] or _g[0]: nav_groups.append(tuple(_g))
        _g = [m.group(1), []]
    else:
        _g[1].append(m.group(2))
nav_groups.append(tuple(_g))
group_of = {t: g for g, ts in nav_groups for t in ts}

# Pages outside the guide that belong in a sidebar group: the open-source projects each have their own
# page on the site. Each entry is (insert before this tab, or None for the end of the group, label, href).
# The order follows the home page: Cistern, Penstock, Headworks, Persona, Culvert, enrich-test-api.
SIDE_EXTRA = {
    "EnrichMeAI open source": [
        ("culvert", "Cistern", "/cistern/"),
        ("culvert", "Penstock", "/penstock/"),
        ("culvert", "Headworks", "/headworks/"),
        ("culvert", "Persona", "/persona/"),
        (None, "enrich-test-api", "/enrich-test-api/"),
    ],
}

def side_items(g, ts):
    # the group's links, in order: its tabs, with the extra pages placed among them
    extra = SIDE_EXTRA.get(g, [])
    items = []
    for t in ts:
        items += [(None, label, href) for before, label, href in extra if before == t]
        items.append((t, labels[t], url(t)))
    items += [(None, label, href) for before, label, href in extra if before is None or before not in ts]
    return items

def side_for(cur):
    # the sidebar: the opening pages, then one collapsible group each; the current group is open
    out = ['<nav class="eg-side" id="topics" aria-label="Guide sections">']
    for g, ts in nav_groups:
        items = side_items(g, ts)
        links = ''.join(f'<a href="{href}"' + (' aria-current="page"' if t is not None and t == cur else '') + f'>{label}</a>'
                        for t, label, href in items)
        if not g:
            out.append(f'<div class="side-top">{links}</div>')
        else:
            op = ' open' if cur in ts else ''
            out.append(f'<details class="side-grp"{op}><summary>{g}<span class="n">{len(items)}</span></summary><div class="side-links">{links}</div></details>')
    out.append('</nav>')
    return '\n'.join(out)

def toc_for(main_html):
    # "On this page": every card heading, linked by the card's id
    items = re.findall(r'<article class="card[^"]*" id="([a-z0-9-]+)"><h3>(.*?)</h3>', main_html, re.S)
    if len(items) < 3: return ''
    li = ''.join(f'<a href="#{i}">{text(h)}</a>' for i, h in items)
    return f'<aside class="eg-toc" aria-label="On this page"><p class="toc-h">On this page</p><div class="toc-links">{li}</div></aside>'

def card_ids(html):
    # give every card without an id one, from its heading, unique on the page
    used = set(re.findall(r'id="([a-z0-9-]+)"', html))
    def add(m):
        base = 'c-' + (re.sub(r'[^a-z0-9]+', '-', text(m.group(2)).lower()).strip('-')[:48] or 'card')
        i, k = base, 2
        while i in used: i, k = f'{base}-{k}', k + 1
        used.add(i)
        return f'<article class="{m.group(1)}" id="{i}"><h3>{m.group(2)}</h3>'
    return re.sub(r'<article class="(card[^"]*)"><h3>(.*?)</h3>', add, html, flags=re.S)

def nav_for(cur):
    n = nav.replace('<nav aria-label="Sections">', '<nav aria-label="Guide sections">')
    def a(m):
        t = m.group(1)
        cur_attr = ' aria-current="page"' if t == cur else ''
        return f'<a href="{url(t)}"{cur_attr}>'
    return re.sub(r'<a href="#([a-z0-9]+)" data-tab="\1">', a, n)

def page(t, title, desc, main_html, extra_head='', hero=''):
    label = 'Well Rounded Engineer'
    crumb = f'<span class="product-label">{label}</span>' if t == 'start' else f'<a class="product-label" href="{BASE}">{label}</a>'
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{_html.escape(desc, quote=True)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow:ital,wght@0,400;0,500;0,600;1,400&family=Barlow+Condensed:wght@500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/site.css">
<link rel="stylesheet" href="{BASE}engineer.css">
<link rel="icon" href="/assets/brand/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/assets/brand/png/enrichmeai-mark-180.png">
{extra_head}<script src="{BASE}engineer.js" defer></script>
</head>
<body data-tab="{t}" class="eg-page">
<a class="skip-link" href="#main">Skip to content</a>

<header class="eg-top">
  <div class="eg-wrap eg-top-in">
    <a href="/" class="wordmark eg-mark">enrichme<span class="dot">·</span>ai</a>
    {crumb}
    <div class="search"><input id="q" type="search" aria-label="Search the guide" placeholder="Search {len(order)} pages, e.g. merge" autocomplete="off"></div>
    <button type="button" class="eg-topics-btn" aria-controls="topics" aria-expanded="false" hidden>Topics</button>
  </div>
</header>
{hero}
<div class="eg-wrap eg-layout">
{side_for(t)}
<main id="main" class="eg">
{main_html}
<p class="empty" id="empty" hidden>Nothing on this page matches.</p>
<div class="elsewhere" id="elsewhere" hidden aria-live="polite"></div>
</main>
{toc_for(main_html)}
</div>

<footer class="site-footer">
  <div class="container">
    <div style="display:flex;flex-direction:column;gap:12px">
      <a href="/" class="wordmark">enrichme<span class="dot">·</span>ai</a>
      <span class="reg">Well Rounded Engineer · more human<br>EnrichMeAI is a trading name of Good Shepherd Software Consultancy Limited,<br>registered in England &amp; Wales, company no. 09702990.</span>
    </div>
  </div>
</footer>
</body>
</html>
'''

def prev_next(t):
    i = order.index(t)
    parts = []
    if i > 0:
        p = order[i - 1]; parts.append(f'<a class="pn-prev" href="{url(p)}">← {labels[p]}</a>')
    if i < len(order) - 1:
        n = order[i + 1]; parts.append(f'<a class="pn-next" href="{url(n)}">{labels[n]} →</a>')
    return '<nav class="eg-pn" aria-label="Previous and next section">' + ''.join(parts) + '</nav>'

n_groups = sum(1 for g, _ in nav_groups if g)
hero_html = f'''<section class="eg-hero" aria-labelledby="hero-h">
  <div class="eg-wrap eg-hero-in">
    <div class="hero-main">
      <p class="hero-eyebrow">A free field guide · <span>More human</span></p>
      <h1 id="hero-h">Well Rounded Engineer</h1>
      <p class="hero-lead">A field guide for engineers in the AI era, and for anyone who wants to do good work and live well. AI hands everyone a bulldozer; this is about being the site manager: clear thinking and good character first, fundamentals before shortcuts, and every claim checked against its source.</p>
      <p class="hero-go"><a class="btn-light" href="#guide-map">Pick a path</a> <a class="btn-line" href="{BASE}aiworry/">Worried about AI?</a></p>
    </div>
    <div class="hero-stats">
      <p><b>{len(order)}</b> pages</p>
      <p><b>{n_groups}</b> paths</p>
      <p class="wide">Every page: four levels, what to study next, and its sources</p>
    </div>
  </div>
</section>'''

# old single-page links (/well-rounded-engineer/#kubernetes) still land on the right page
redirect = ('<script>(function(){var t=location.hash.slice(1),k=' + json.dumps([t for t in order if t != 'start'])
            + ';if(k.indexOf(t)>=0)location.replace("' + BASE + '"+t+"/");})();</script>\n')

index, total = [], 0
os.makedirs(out_dir, exist_ok=True)
for t in order:
    sec = relink(sections[t])
    head_p = re.search(r'<div class="panel-head"><h2>(.*?)</h2><p>(.*?)</p></div>', sec, re.S)
    h2, lead = head_p.group(1), head_p.group(2)
    desc = text(lead)
    if len(desc) > 158:
        desc = desc[:155].rsplit(' ', 1)[0] + '…'
    sec = card_ids(sec)
    hero = ''
    if t == 'start':
        title = 'Well Rounded Engineer · more human, for the AI era'
        main_html = sec + '\n' + prev_next(t)
        extra = redirect
        hero = hero_html
    else:
        title = f'{text(labels[t])} · Well Rounded Engineer'
        # the tab's heading is the page's h1
        sec = sec.replace(f'<div class="panel-head"><h2>{h2}</h2>', f'<div class="panel-head"><h1>{h2}</h1>', 1)
        g = group_of.get(t, '')
        crumb = f'<p class="eg-crumb"><a href="{BASE}">Guide</a>' + (f' / <span>{g}</span>' if g else '') + f' / <span aria-current="page">{labels[t]}</span></p>'
        main_html = crumb + '\n' + sec + '\n' + prev_next(t)
        extra = ''
    out = os.path.join(out_dir, 'index.html') if t == 'start' else os.path.join(out_dir, t, 'index.html')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    html_out = page(t, title, desc, main_html, extra, hero)
    open(out, 'w').write(html_out)
    total += len(html_out)
    cards = [{'h': text(m.group(1)), 'x': text(m.group(0)).lower()}
             for m in re.finditer(r'<article class="card[^"]*"[^>]*><h3>(.*?)</h3>.*?</article>', sec, re.S)]
    index.append({'t': t, 'l': text(labels[t]), 'u': url(t), 'c': cards})

json.dump(index, open(os.path.join(out_dir, 'search.json'), 'w'), separators=(',', ':'), ensure_ascii=False)
print('wrote', len(order), 'pages,', total, 'bytes of HTML; search.json', os.path.getsize(os.path.join(out_dir, 'search.json')))
