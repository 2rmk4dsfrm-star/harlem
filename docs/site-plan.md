# Harlem Group website plan · v1

_November 2026_

## 1. What the site is for

| Goal | Who | Measure of success |
| --- | --- | --- |
| Turn poster and social traffic into WhatsApp chats with drivers | Self-employed multi-drop drivers around Leeds | WhatsApp chats started from the site |
| Give carriers and retailers a way to ask about delivery capacity | Depot managers, carriers, retailers | Enquiry emails received |

Drivers come first. Most arrive on a phone from a Facebook post, WhatsApp Status or a printed poster, and want four answers fast: **how much, where, what do I need, how do I apply**. Businesses get a section of their own further down the page.

## 2. Structure

The site is a single scrolling page. Everything a driver needs fits on one page, and a single URL is easy to put on posters and in WhatsApp.

| # | Section (anchor) | Job | Key content | Primary action |
|---|---|---|---|---|
| — | Header (sticky) | Brand + navigation | Logo, 5 anchor links, menu on mobile | **WhatsApp to apply** |
| 1 | Hero (`#top`) | Repeat the poster's promise | "Earn up to £200 a day", £75–£200 banner, 80p per parcel, Leeds depot Mon–Sat, van illustration, 4 benefits | WhatsApp to apply · See routes & pay |
| 2 | Routes & pay (`#routes`) | Show every route and rate | 7-route table (80p / £1.00), schematic map from the Leeds depot, LWB van note | "Ask" on each route (pre-filled WhatsApp) |
| 3 | Pay calculator (`#calculator`) | Let drivers see their own numbers | Rate (80p / £1.00), parcels per day (50–300), days per week (1–6) → daily + weekly estimate, £75–£200 meter, costs disclaimer | WhatsApp to apply (mentions the chosen rate) |
| 4 | How to apply (`#requirements`) | Remove doubt before they message | What you need (vehicle, hire & reward insurance, licence, right to work, experience) + the 3 steps | Start step 1 on WhatsApp |
| 5 | FAQ (`#faq`) | Answer objections | 9 questions: self-employment, pay, pay day, vehicle, insurance, depot, days, experience, start date | Ask us on WhatsApp |
| 6 | For businesses (`#business`) | Win capacity work | Route coverage, driver supply, LWB / larger loads | Email enquiries |
| 7 | Apply (`#apply`) | Final push | 3 steps, big WhatsApp number panel, LWB footnote | WhatsApp to apply |
| — | Footer | Trust + legal | Stacked logo, links, contact, registered company details | — |

On phones, a sticky **WhatsApp to apply** bar appears once the hero buttons scroll off-screen and hides again at the final panel.

## 3. Calls to action and WhatsApp messages

Every driver button opens WhatsApp on **07548 547193** with a message already typed, so the first chat tells you where the driver came from.

| Button | Pre-filled message |
| --- | --- |
| Header, hero, steps, final panel, mobile bar | "Hi Harlem Group, I'd like to apply to drive. My vehicle is a (car / SWB van) and I live in (town)." |
| Route "Ask" buttons | "Hi, I'm interested in the Bradford route (80p per parcel)." (one per route) |
| LWB van links | "Hi, I have an LWB van and I'd like to hear about other routes." |
| Calculator | "Hi Harlem Group, I'd like to apply to drive. I'm interested in an 80p route." (follows the rate picked) |
| FAQ | "Hi Harlem Group, I have a question about driving with you:" |
| Businesses | Email to `enquiries@example.com` (placeholder), subject "Delivery capacity enquiry" |

The messages live in the `data-wa` attribute of each link in `index.html`, so you can edit them as plain text.

## 4. Content: confirmed vs. assumed

**From your poster and answers (confirmed)**
- Routes, rates, Mon–Sat, Leeds depot start, £75–£200 per day, 80p per parcel, paid weekly, self-employed
- Car or SWB van, hire & reward insurance, parcel experience preferred, start this week
- LWB vans: message about other routes
- Business offer: route coverage, driver supply, LWB / larger loads

**Added by me, so please check before launch**
- Requirements: _full UK driving licence_ and _right to work in the UK_ ("We check this for every driver")
- FAQ wording on Self Assessment and on hire & reward vs. standard insurance
- "We'll confirm your pay day when you join" and "We'll send you the address and start time…"
- Business card wording: "vetted, insured self-employed drivers… new routes, absences and busy periods"
- Map positions are approximate town centres, not depot postcodes

## 5. SEO and sharing

- **Title:** Delivery Driver Jobs in Leeds · Earn up to £200 a day · Harlem Group
- **Meta description:** lists all seven towns, the rate and the WhatsApp number
- **Google for Jobs:** `JobPosting` structured data (contractor, Leeds, £75–£200 per day). Update `datePosted` whenever you re-advertise.
- **Share image:** `assets/img/og-image.png` (1200 × 630), used by WhatsApp, Facebook and LinkedIn link previews
- **Later:** a Google Business Profile for the depot (if it can be public), and the site URL on every poster

## 6. Technology and hosting

- Plain HTML, CSS and JavaScript with no build step: `index.html`, `assets/css/styles.css`, `assets/js/main.js`
- No forms, no cookies, no tracking, so no cookie banner is needed. Inter loads from Google Fonts; to avoid sending visitor IPs to Google, self-host the font files later.
- Hosting options (all free for a site this size): **Netlify** (drag and drop the folder), **Cloudflare Pages** or **GitHub Pages** (connect this repo)
- Accessibility: semantic table and headings, a skip link, visible focus rings, AA+ contrast on every text pairing, and reduced motion respected

## 7. Launch checklist

- [ ] Replace `enquiries@example.com` with your real business email (search the code for `TODO-LAUNCH`)
- [ ] Fill in the registered company name, number and office in the footer (required for UK limited companies)
- [ ] Confirm or edit the assumed content in section 4
- [ ] Buy and connect a domain, then make the `og:image` URL absolute and add a canonical link
- [ ] Test every WhatsApp button on an iPhone and an Android phone
- [ ] Add the site to Google Search Console and request indexing
- [ ] Optional: privacy-friendly analytics (e.g. Plausible) to count WhatsApp button clicks
- [ ] Poster tweak: "Got **an** LWB van?" (LWB is said "el-double-u-bee")

## 8. Phase 2 ideas

- Real photos of the depot, vans and drivers to sit beside the illustration
- Short driver quotes (with permission)
- A separate `/business` page if enquiries grow, with case studies and coverage maps
- A short online form as a second route in, for drivers who don't want to message first
- One job posting per route for Google for Jobs and Indeed
