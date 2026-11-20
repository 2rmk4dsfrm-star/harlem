# Harlem Group

Brand board and website for Harlem Group, a last-mile parcel delivery subcontractor working from a depot in Leeds.

```
index.html               the website (one page)
assets/css/styles.css    all styles; brand colours are the --hg-* tokens at the top
assets/js/main.js        WhatsApp links, mobile menu, pay calculator
assets/img/              logo files (SVG), favicon, social share image
brand/index.html         brand board: logo, hex codes, type, components, voice
docs/site-plan.md        site plan, content notes and launch checklist
```

## Preview

Open `index.html` in a browser, or run a local server:

```bash
python3 -m http.server 8000   # then visit http://localhost:8000
```

## Publish

The site is static, so any static host works:

- **Netlify:** drag the project folder onto app.netlify.com/drop
- **Cloudflare Pages / GitHub Pages:** connect this repository and set the root folder as the site

Before launch, work through the checklist in `docs/site-plan.md`. Search the code for `TODO-LAUNCH` to find every placeholder.

## Common edits

| To change | Edit |
| --- | --- |
| A route or its rate | The `<tbody>` rows in the `#routes` table in `index.html`, the map labels below it, and the calculator's rate options in `#calc` |
| A pre-filled WhatsApp message | The `data-wa="…"` text on that link in `index.html` |
| The WhatsApp number | `WHATSAPP_NUMBER` in `assets/js/main.js`, then find and replace `447548547193` and `07548 547193` in `index.html` |
| Colours | The `--hg-*` tokens at the top of `assets/css/styles.css` (keep them in step with the brand board) |
| The business email | Search for `enquiries@example.com` |

## Brand at a glance

| Colour | Hex | Job |
| --- | --- | --- |
| Depot Navy | `#0C2543` | Background |
| Hi-Vis Lime | `#C6F432` | Money and emphasis |
| Signal Sky | `#5FCFFA` | Action and contact |
| Van White | `#FFFFFF` | Headlines, logo |
| Night Run | `#081B33` | Deepest panels |
| Route Navy | `#102F52` | Diagonal panels, alternate rows |
| Lane Blue | `#13335A` | Tiles, cards |
| Kerb Line | `#2B4D78` | Borders |
| Mist | `#C9D6E6` | Body text |
| Slate | `#A9BCD3` | Captions |
| Steel | `#8FA3BC` | Muted details |
| Brake Light | `#F2545B` | Errors only |

Typeface: **Inter** (Google Fonts). The logo wordmark uses Montserrat SemiBold, already converted to outlines in the SVG files.
