# GuVue LUTs — Public DOM & Sitemap Audit (`opencode-extractor`, Sub-Job 2, Task 1)

Date: 2026-11-09 · Auditor: opencode-extractor · Site: https://guvueluts.com (Shopify store, shop id `71935393875`)

> Method note: direct `curl` fetches of guvueluts.com were rate-limited (HTTP 429 `local_rate_limited`).
> This audit was completed from the orchestrator's clean HTTP-200 snapshots in
> `/tmp/lut_scavenger/orchestrator_audit/` (`guvue_home.html`, `guvue_film.html`, `guvue_hk.html`, `guvue_agents.md`),
> plus sitemap XMLs fetched directly (`sitemap.xml` index → HTTP 200).
> The source HTML snapshots are stored alongside this audit for re-verification.

## 1. Sitemap structure

`https://guvueluts.com/sitemap.xml` (HTTP 200) is a Shopify sitemap index:

| Sitemap | Content |
|---|---|
| `sitemap_agentic_discovery.xml` | `https://guvueluts.com/agents.md` |
| `sitemap_products_1.xml` | 3 URLs: home, HK Series pack, Film Collection pack |
| `sitemap_pages_1.xml` | `/pages/data-sharing-opt-out` |
| `sitemap_collections_1.xml` | `/collections/frontpage` |
| `sitemap_blogs_1.xml` | `/blogs/news` |

**Product inventory is only 2 LUT products.** There is no `/collections/all` bulk page and no
`cdn.shopify.com` digital-asset link exposed anywhere in the sitemaps (only image CDN URLs).

## 2. GuVue Film Collection LUT Pack (`/products/guvue-film-collection-lut-pack`)

### The "4 free trial looks" — confirmed in DOM
The free trial is real and consists of exactly **F11–F14** of the 14-look Film Collection:

| Look | Name (as rendered in DOM) |
|---|---|
| F11 | **Kodak 250D Cinema** |
| F12 | **Kodak Ektar Daylight** |
| F13 | **Kodak P800 Documentary** |
| F14 | **Lomo92 Vintage** |

DOM copy: *"F11-F14, selected from the complete Film Collection. Enter your email to download the
four looks here and receive a confirmation email."* — *"The US$48 pack includes all 14 looks. No
purchase is needed to try these four."*

### Delivery mechanism: email-gated, NOT zero-login — CONFIRMED
The trial section (`#film-samples` anchor exists in the DOM) is delivered through **Shopify Forms**:

- `<div id='ARHBkejM5aTN4RUxrR__film_trial_form' data-form-root='true' data-forms-id='forms-root-1238194' ...>`
- Shopify Forms storefront script loaded; **hCaptcha** is wired in
  (`hcaptcha/ce_storefront_forms_captcha_hcaptcha.v1.5.3.iife.js`, `h-captcha-response` field).
- Delivery = **email confirmation link**, not a public binary URL.

**Verdict: NO zero-login binary download exists.** Per the strict rules we did **not** submit the
form and did **not** attempt to bypass hCaptcha. F11–F14 files are only obtainable via email
signup → confirmation email, which violates the "zero-gate" requirement for the final pack.

### Documented specs (Film Collection)
- 14 looks × 2 input versions = **28 CUBE files** (`Log 2 / 709` — Apple Log 2 + Rec.709 inputs).
- DOM does **not** state "33-point" explicitly on this page (the HK page does).
- Digital download (ZIP delivered via Shopify order link after purchase), $48.00 USD.
- Page warns the iPhone native camera app cannot import CUBE files directly (needs Blackmagic Camera etc.).

## 3. GuVue HK Series LUT Pack (`/products/guvue-hk-series-lut-pack`)

### The 6 HK looks — confirmed in DOM
**Amber (HK01), Pale Green (HK02), Harbor Blue (HK03), Island Cyan (HK04), Avenue Star (HK05), Mong Kok (HK06)** — all present as named comparison sections with real-footage before/after.

### Documented specs — CONFIRMED
- **"12 33-point .cube LUT files — Six Apple Log files and six Rec.709 files. Two input versions of each look."**
- File naming documented in DOM: `GuVue•HK01 Amber.cube`, `GuVue•HK02 Pale Green.cube`, `GuVue•HK03 Harbor Blue.cube`, `GuVue•HK05 Avenue Star.cube`, `GuVue•HK06 Mong Kok.cube` (+ `_709` suffixed Rec.709 versions).
- $38.00 USD, delivered as a **digital ZIP package via Shopify order delivery link after purchase** (paywalled — no free tier, no zero-login link; HK page has **no** trial form).
- Includes 10-page illustrated English PDF guide.

## 4. Home page & agents.md
- Home page shows a **"4 free trial looks"** collection card linking to the Film Collection product.
- `https://guvueluts.com/agents.md` instructs AI agents to shop via the Shopify **Shop skill** and
  **Universal Commerce Protocol** (`GET /.well-known/ucp` → `https://guvueluts.com/api/ucp/mcp`).
  This is a purchasing pathway for agents, **not** a free asset endpoint.

## 5. Conclusion for the scavenger hunt
| Requirement | Status |
|---|---|
| Free trial looks F11–F14 (4 names) | ✅ Confirmed, but **email + hCaptcha gated** (Shopify Forms `forms-root-1238194`) |
| HK Series 6 look names | ✅ Confirmed (Amber, Pale Green, Harbor Blue, Island Cyan, Avenue Star, Mong Kok) |
| 33-point .cube spec | ✅ HK page explicitly: "12 33-point .cube LUT files" (film page says "CUBE files" only) |
| Apple Log 2 / Apple Log / Rec.709 inputs | ✅ Film: Apple Log 2 + Rec.709. HK: Apple Log + Rec.709 |
| Zero-login direct .cube URL | ❌ **None exists** — trial = email form; packs = paid Shopify checkout |
