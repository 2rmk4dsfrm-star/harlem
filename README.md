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

The site is hosted on **GitHub Pages**, deployed from the `main` branch, root folder:

- Website: https://2rmk4dsfrm-star.github.io/harlem/
- Brand board: https://2rmk4dsfrm-star.github.io/harlem/brand/

Every push to `main` republishes the site within a minute or two. `.nojekyll` tells GitHub to serve the files as they are.

The site is static, so it would also run on Netlify or Cloudflare Pages without changes. If you move to your own domain, update the three `github.io` URLs at the top of `index.html`.

Before launch, work through the checklist in `docs/site-plan.md`. Search the code for `TODO-LAUNCH` to find every placeholder.

## Common edits

| To change | Edit |
| --- | --- |
| A route or its rate | The `<tbody>` rows in the `#routes` table in `index.html`, the map labels below it, and the calculator's rate options in `#calc` |
| A pre-filled WhatsApp message | The `data-wa="…"` text on that link in `index.html` |
| The WhatsApp number | `WHATSAPP_NUMBER` in `assets/js/main.js`, then find and replace `447548547193` and `07548 547193` in `index.html` |
| Colours | The `--hg-*` tokens at the top of `assets/css/styles.css` (keep them in step with the brand board) |
| The business email | Search for `enquiries@example.com` |

## Photos

The page has four photo slots. Each one holds a brand-style stand-in illustration until a real photo is taken:

| Slot | Where | Stand-in file | Real photo to take |
| --- | --- | --- | --- |
| 1 | Top of the page, under the buttons | `assets/img/photos/depot-van.svg` | A van loading at the depot |
| 2 | Routes, under the heading | `assets/img/photos/loading-bay.svg` | The loading bay in the morning, cages and parcels |
| 3 | What you need | `assets/img/photos/car-boot.svg` | A car boot full of parcels |
| 4 | For businesses | `assets/img/photos/vans-row.svg` | A row of vans, or the team at the depot |

To swap in a real photo:
1. Blur number plates, parcel labels and anyone who hasn't agreed to be shown, and keep client logos out of shot.
2. Strip location data, resize to about 1280px wide (landscape) and save as JPEG at about 150KB, e.g. `assets/img/photos/depot-van.jpg`.
3. In `index.html`, search for `PHOTO SLOT`, change the `img` `src` (and `width`/`height` to the photo's), and add `real` to the figure's class for the light navy tint.

Keep one photo per slot, with no text on top and no slideshows.

## Brand at a glance

| Colour | Hex | Job |
| --- | --- | --- |
| Depot Navy | `#0C2543` | Background |
| Hi-Vis Lime | `#C6F432` | Money only (pay figures and rates) |
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
