"""Builds one landing page per route town from the TOWNS list below.
Run from the repo root:  python3 tools/make_town_pages.py
Each page is written to <slug>/index.html (e.g. york/index.html)."""
import json, re, html
from pathlib import Path

SITE = "https://2rmk4dsfrm-star.github.io/harlem/"   # SITE URL

# PRE-LAUNCH SWITCH: True keeps every page (home + towns) out of Google.
# At launch, set to False and re-run this script, then submit sitemap.xml in Search Console.
HIDE_FROM_GOOGLE = True
NOINDEX_TAG = '<meta name="robots" content="noindex"><!-- PRE-LAUNCH: set by HIDE_FROM_GOOGLE in tools/make_town_pages.py -->\n' 
WA = "447548547193"

TOWNS = [
  # slug, name, region, rate in pence, postcode area, lead line (town-specific).
  # TOWN FACTS: set per town below, then re-run the script. Shared defaults are in
  # FACT_DEFAULTS. postcodes e.g. "YO1, YO10, YO24"; while empty the page says
  # "YO postcodes in York" (no placeholder shown).
  dict(slug="leeds", name="Leeds", region="West Yorkshire", p=80, pc="LS",
       lead="Load at our Leeds depot and deliver in Leeds. Your route starts in the city you work in."),
  dict(slug="bradford", name="Bradford", region="West Yorkshire", p=80, pc="BD",
       lead="Load at our Leeds depot, then deliver a tight Bradford postcode."),
  dict(slug="wakefield", name="Wakefield", region="West Yorkshire", p=80, pc="WF",
       lead="Load at our Leeds depot, then deliver a tight Wakefield postcode."),
  dict(slug="huddersfield", name="Huddersfield", region="West Yorkshire", p=80, pc="HD",
       lead="Load at our Leeds depot, then deliver a tight Huddersfield postcode."),
  dict(slug="halifax", name="Halifax", region="West Yorkshire", p=80, pc="HX",
       lead="Load at our Leeds depot, then deliver a tight Halifax postcode."),
  dict(slug="harrogate", name="Harrogate", region="North Yorkshire", p=100, pc="HG",
       lead="One of our two best-paying routes. £1.00 a parcel, 20p more than our West Yorkshire routes."),
  dict(slug="york", name="York", region="North Yorkshire", p=100, pc="YO",
       lead="One of our two best-paying routes. £1.00 a parcel, 20p more than our West Yorkshire routes."),
]

FACT_DEFAULTS = dict(postcodes="", routes_open="2+ jobs open", start="Start time 7am onwards")

def money(p): return "£1.00" if p == 100 else f"{p}p"
def gbp(x): return f"£{x:,.0f}"

src = Path("index.html").read_text()
sprite = re.search(r'<svg width="0" height="0".*?</svg>\n', src, re.S).group(0)

def page(t):
    r = money(t["p"]); n = t["name"]
    day200 = gbp(200 * t["p"] / 100)  # pay for 200 parcels: £160 at 80p, £200 at £1.00
    rows = "".join(
        f'<tr><th scope="row">{q}</th><td class="num">{gbp(q*t["p"]/100)}</td><td class="num">{gbp(q*t["p"]/100*5)}</td></tr>'
        for q in (100, 150, 200))
    towns_line = ' · '.join(f'<a href="../{o["slug"]}/">{o["name"]}</a>' for o in TOWNS)
    others = "".join(
        f'<li><a href="../{o["slug"]}/"><b>{o["name"]}</b><span class="{"up" if o["p"]==100 else ""}">{money(o["p"])}</span></a></li>'
        for o in TOWNS if o is not t)
    wa_msg = html.escape(f"Hi Harlem Group, I'd like to apply for the {n} route ({r} per parcel).\nVehicle: \nI live in: ")
    url = f"{SITE}{t['slug']}/"
    if t['routes_open']:
        routes_li = f'<li><span class="tile" aria-hidden="true"><svg class="ic"><use href="#i-check"/></svg></span><div><b>{t["routes_open"]}</b><small>Message us to claim one</small></div></li>'
    else:
        routes_li = ''
    ld = {
      "@context": "https://schema.org",
      "@graph": [
        {"@type": "JobPosting",
         "title": f"Self-employed multi-drop delivery driver, {n}",
         "description": f"<p>Permanent Monday to Saturday parcel delivery route in {n} ({t['pc']} postcodes), starting from our Leeds depot.</p><p>Paid {r} per parcel, paid weekly. 200 parcels a day makes {day200}. Self-employed.</p><p>New drivers start on 100 to 120 parcels a day, rising to 200+ once you're settled in. Experienced parcel drivers can start on a high-volume route straight away.</p><p>You need a car or SWB van, hire &amp; reward insurance, a full UK driving licence with no more than 6 points and the right to work in the UK. Parcel experience preferred, not essential.</p><p>WhatsApp 07548 547193 to apply.</p>",
         "identifier": {"@type": "PropertyValue", "name": "Harlem Group", "value": f"HG-{t['slug'].upper()}"},
         "datePosted": "2026-11-23", "employmentType": "CONTRACTOR", "directApply": False,
         "hiringOrganization": {"@type": "Organization", "@id": f"{SITE}#org", "name": "Harlem Group", "sameAs": SITE, "logo": f"{SITE}assets/img/logo-mark-512.png"},
         "jobLocation": {"@type": "Place", "address": {"@type": "PostalAddress", "addressLocality": n, "addressRegion": t["region"], "addressCountry": "GB"}},
         "baseSalary": {"@type": "MonetaryAmount", "currency": "GBP", "value": {"@type": "QuantitativeValue", "minValue": t["p"], "maxValue": 2 * t["p"], "unitText": "DAY"}}},
        {"@type": "BreadcrumbList", "itemListElement": [
          {"@type": "ListItem", "position": 1, "name": "Routes", "item": f"{SITE}#routes"},
          {"@type": "ListItem", "position": 2, "name": n, "item": url}]}
      ]}
    return f'''<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Delivery Driver Jobs in {n} · {r} a parcel · Harlem Group</title>
<meta name="description" content="Self-employed multi-drop delivery driver jobs in {n} ({t['pc']} postcodes). {r} per parcel, paid weekly, Mon–Sat. Start at our Leeds depot. WhatsApp 07548 547193 to apply.">
{NOINDEX_TAG if HIDE_FROM_GOOGLE else ""}<meta name="theme-color" content="#0C2543">
<link rel="icon" href="../assets/img/favicon.svg" type="image/svg+xml">
<link rel="canonical" href="{url}">
<meta property="og:url" content="{url}">
<meta property="og:title" content="Drivers wanted in {n} · {r} a parcel · Harlem Group">
<meta property="og:image" content="{SITE}assets/img/og-image.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap">
<link rel="stylesheet" href="../assets/css/styles.css">
<script type="application/ld+json">
{json.dumps(ld, ensure_ascii=False, indent=2)}
</script>
</head>
<body class="town-page">
<a class="skip" href="#main">Skip to content</a>
{sprite}
<header class="site-header" id="top">
  <div class="wrap header-in">
    <a class="brand" href="../" aria-label="Harlem Group home">
      <img src="../assets/img/logo-horizontal-white.svg" width="191" height="34" alt="Harlem Group">
    </a>
    <a class="back-link" href="../#routes"><svg class="ic" aria-hidden="true"><use href="#i-arrow"/></svg>All routes</a>
  </div>
</header>

<main id="main">
<section class="hero town-hero">
  <div class="wrap">
    <div class="eyebrow-row">
      <span class="where"><svg class="ic" aria-hidden="true"><use href="#i-pin"/></svg>{n} route · from our Leeds depot</span>
    </div>
    <h1 class="town-title">Delivery driver jobs in {n}</h1>
    <div class="banner"><b>{r} a parcel</b><span>200 parcels a day makes {day200}</span></div>
    <p class="lead">{t['lead']}</p>
  </div>
</section>

<section class="section" aria-labelledby="glance-h">
  <div class="wrap">
    <div class="sec-head"><span class="label">The {n} route</span><h2 id="glance-h">Mon–Sat. Paid weekly. {t['pc']} postcodes.</h2></div>
    <ul class="ticks">
      <li><span class="tile" aria-hidden="true"><svg class="ic"><use href="#i-wallet"/></svg></span><div><b>{r} per parcel</b><small>Paid weekly, self-employed</small></div></li>
      <li><span class="tile" aria-hidden="true"><svg class="ic"><use href="#i-calendar"/></svg></span><div><b>Monday to Saturday</b><small>Permanent route, tell us your days</small></div></li>
      <li><span class="tile" aria-hidden="true"><svg class="ic"><use href="#i-pin"/></svg></span><div><b>{(t['postcodes'] or t['pc'] + ' postcodes in ' + n)}</b><small>Exact postcodes confirmed when you're offered the route</small></div></li>
      <li><span class="tile" aria-hidden="true"><svg class="ic"><use href="#i-route"/></svg></span><div><b>Load at our Leeds depot</b><small>{t['start'] or 'Address and start time sent once your packs are done'}</small></div></li>
      {routes_li}
    </ul>
  </div>
</section>

<section class="section" aria-labelledby="pay-h">
  <div class="wrap">
    <div class="sec-head"><span class="label">Pay in {n}</span><h2 id="pay-h">200 parcels × {r} = {day200} a day.</h2></div>
    <ul class="ticks ramp">
      <li><span class="tile" aria-hidden="true"><svg class="ic"><use href="#i-box"/></svg></span><div><b>Start on 100–120 parcels a day</b><small>Then up to 200+ once you've settled in</small></div></li>
      <li><span class="tile" aria-hidden="true"><svg class="ic"><use href="#i-bolt"/></svg></span><div><b>Experienced? Start on high volume</b><small>Tell us your experience when you message</small></div></li>
    </ul>
    <div class="route-table-wrap">
      <table class="rtable town-pay">
        <caption class="sr">What you could earn on the {n} route</caption>
        <thead><tr><th scope="col">Parcels a day</th><th scope="col" class="num">Per day</th><th scope="col" class="num">5 days</th></tr></thead>
        <tbody>{rows}</tbody>
      </table>
    </div>
    <p class="small-print">Before costs. You pay your own fuel, vehicle, insurance, tax and National Insurance. <a href="../#calculator">Open the full pay calculator</a></p>
  </div>
</section>

<section class="section" aria-labelledby="apply-h">
  <div class="wrap">
    <div class="sec-head"><span class="label">How to apply</span><h2 id="apply-h">Car or SWB van + hire &amp; reward insurance.</h2></div>
    <ol class="track">
      <li class="go"><span class="d" aria-hidden="true">1</span><b>WhatsApp<br> us</b></li>
      <li><span class="d" aria-hidden="true">2</span><b>Fill in<br> packs</b></li>
      <li><span class="d" aria-hidden="true">3</span><b>Collect<br> your route</b></li>
    </ol>
    <p class="small-print"><a href="../#requirements">Everything you need, and where to get insurance</a></p>
  </div>
</section>

<section class="section" aria-labelledby="other-h">
  <div class="wrap">
    <div class="sec-head"><span class="label">Other routes</span><h2 id="other-h">Not {n}? We have 6 more.</h2></div>
    <ul class="town-links">{others}</ul>
  </div>
</section>
</main>

<footer class="site-footer">
  <div class="wrap legal">
    <p>Drivers: WhatsApp <a href="https://wa.me/{WA}" target="_blank" rel="noopener">07548 547193</a> · Businesses: <a href="mailto:harlemgroupltd@gmail.com">harlemgroupltd@gmail.com</a></p>
    <p class="f-towns">Towns we cover: {towns_line}</p>
    <p>© 2026 Harlem Group Ltd. Registered in England and Wales, company no. 17192003. Registered office: 17 Hilton Road, Leeds, England, LS8 4HB.</p>
  </div>
</footer>

<div class="mobile-bar">
  <a class="btn sky" href="https://wa.me/{WA}" data-wa="{wa_msg}" target="_blank" rel="noopener"><svg class="ic wa" aria-hidden="true"><use href="#i-wa"/></svg>WhatsApp about {n}</a>
</div>
<script src="../assets/js/main.js" defer></script>
</body>
</html>
'''

for t in TOWNS:
    for k, v in FACT_DEFAULTS.items(): t.setdefault(k, v)

for t in TOWNS:
    d = Path(t["slug"]); d.mkdir(exist_ok=True)
    (d / "index.html").write_text(page(t))
# Apply the same switch to the home page
home = Path("index.html").read_text()
home = home.replace(NOINDEX_TAG, "")
if HIDE_FROM_GOOGLE:
    home = home.replace('<meta name="theme-color"', NOINDEX_TAG + '<meta name="theme-color"', 1)
Path("index.html").write_text(home)

urls = [SITE] + [f"{SITE}{t['slug']}/" for t in TOWNS]
Path("sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<!-- SITE URL: built by tools/make_town_pages.py. If you move to your own domain, change SITE there and re-run. -->\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'  <url>\n    <loc>{u}</loc>\n    <lastmod>2026-11-23</lastmod>\n  </url>\n' for u in urls) + '</urlset>\n')
print("built", len(TOWNS))
