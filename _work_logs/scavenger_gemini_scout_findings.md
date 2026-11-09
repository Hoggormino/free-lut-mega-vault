# Sub-Job 1 Report: Deep-Web LUT Discovery & GuVue Reconnaissance (`gemini-scout`)

- **Worker Agent:** `gemini-scout` (`t1b`, Herdr left pane `pc6c5185d01ced401ad15ca4ab24b6d97`, `gemini-3.5-flash`) + Orchestrator Search Grounding Synthesis (`t19`)
- **Session Note:** `gemini-scout` (`t1b`) read `subjob1_gemini_scout.md` and `master_plan.md` and executed server-side `GoogleSearch` grounding against `site:guvueluts.com`, GuVue YouTube/Reddit mentions, and free Apple Log 2 / Blackmagic Camera LUT portals before local `en0` (`10.40.8.1`) dropped new outbound `WebFetch` TCP 443 sockets. All Sub-Job 1 search-grounding results and portal classifications are consolidated below.

---

## 1. Priority Target Reconnaissance: GuVue LUTs (`guvueluts.com`)

### 1.1 Store Inventory & Architecture
- **Storefront:** Shopify (`shop_id: 71935393875`, Universal Commerce Protocol enabled via `/.well-known/ucp` and `/agents.md`).
- **Catalog (`sitemap_products_1.xml`):** Contains **only 2 commercial LUT products**:
  1. **GuVue Film Collection LUT Pack** (`https://guvueluts.com/products/guvue-film-collection-lut-pack` — **$48.00 USD**)
     - **Full Commercial Pack:** **28 `.cube` files** = 14 film-inspired looks (`F01–F14`) × 2 input color spaces (**Apple Log 2** + **Rec. 709**).
     - **Official "4 Free Trial Looks" (`#film-samples`):** Confirmed in public page DOM as:
       - **`F11` — Kodak 250D Cinema**
       - **`F12` — Kodak Ektar Daylight**
       - **`F13` — Kodak P800 Documentary**
       - **`F14` — Lomo92 Vintage**
     - **Zero-Gate Compliance Verdict (`EMAIL + hCAPTCHA GATED` on web; `8/8` Official `33pt` `.cube`s Verified from User `~/Downloads`):** Web form uses **Shopify Forms (`forms-root-1238194`)** + **Storefront hCaptcha (`ce_storefront_forms_captcha_hcaptcha.v1.5.3.iife.js`)**. The user downloaded the official `GuVue_Film_Collection_4_Free_Sample_Looks_EN.zip` (`2.47 MB`) into `~/Downloads`, and binary inspection confirmed **all 8 official `.cube` files** (`4× 01_AppleLog2` + `4× 02_Rec709`) are strict **`33×33×33` (`35,937` triplets)** — now packed inside `ready_to_airdrop_33pt/00_GuVue_Official_Film_Samples_33pt/`.
  2. **GuVue HK Series LUT Pack** (`https://guvueluts.com/products/guvue-hk-series-lut-pack` — **$38.00 USD**)
     - **Full Commercial Pack:** **12 `33-point .cube` LUT files** = 6 Hong Kong cinema looks × 2 input spaces (**Apple Log** + **`_709` Rec. 709**):
       - **`HK01` — Amber** *(warm tungsten/sodium street glow)*
       - **`HK02` — Pale Green** *(Wong Kar-wai fluorescent jade/sage shadows)*
       - **`HK03` — Harbor Blue** *(Victoria Harbour slate-blue shadows, cool steel midtones)*
       - **`HK04` — Island Cyan** *(teal-cyan night harbour split with clean skin separation)*
       - **`HK05` — Avenue Star** *(theatrical cinema print contrast, warm skin vs. cool night sky)*
       - **`HK06` — Mong Kok** *(dense neon-night cyan shadows + electric magenta signage punch)*
     - **Zero-Gate Compliance Verdict (`PAID ONLY`):** Commercial digital checkout only; no free trial exists on `guvueluts.com` or social channels.

### 1.2 Curated Zero-Login `33-Point .cube` Aesthetic Replacements (`HK01–HK06` & `F11–F14`)

| GuVue Target Look | Aesthetic Profile | Zero-Login `33pt` Match (`Apple Log 2` / `Apple Log` — iPhone 17 Pro / Pro Max) | Zero-Login `33pt` Match (`Rec. 709 SDR` — iPhone 17 & 17 Air) |
| :--- | :--- | :--- | :--- |
| **`HK01` Amber** | Golden tungsten street glow, soft highlight roll-off | Luttie *Warm Golden Hour* (`Apple Log 2` `#411` / `Apple Log` `#400`) | `slaycamera/luts` **`slay-01-amber.cube`** (`CC BY 4.0`, binary-verified `33pt`) |
| **`HK02` Pale Green** | Wong Kar-wai fluorescent sage/jade shadow cast | `Joey-LJ/LUTS` **`FUJI-CN` (Classic Neg -> Apple Log 2)** (`33pt`) | Chromasmith **`fuji_pro_400h_ca_maxima.cube`** & **`classic_neg.cube`** (`GPL-3.0`, `33pt`) |
| **`HK03` Harbor Blue** | Deep Victoria Harbour slate-blue shadows, cool steel | Luttie *Cool Blue Steel* (`Apple Log 2` `#404` / `Apple Log` `#393`) | `slaycamera/luts` **`slay-04-film.cube`** (`CC BY 4.0`, `33pt`) |
| **`HK04` Island Cyan** | Teal-cyan night harbour split with clean tungsten skin | Luttie *Moody Cinematic Dark Teal* (`Apple Log 2` `#409` / `Apple Log` `#398`) | Chromasmith **`vision3_500t_2383.cube`** (`GPL-3.0`, `33pt`) |
| **`HK05` Avenue Star** | Cinema print contrast, theatrical D60/ETERNA curve | `raycalrui/raycal-luts` **`Apple Log 2_cinematic.cube`** (`33pt`) | `imnz730/LUTs` **`Rec709 Fujifilm 3513DI D60.cube`** (`33pt`) |
| **`HK06` Mong Kok** | Neon cyan shadows + magenta signage punch | Luttie *Cyberpunk Neon* (`Apple Log 2` `#405` / `Apple Log` `#394`) | `slaycamera/luts` **`slay-03-neon.cube`** (`CC BY 4.0`, `33pt`) |
| **`F11` Kodak 250D** | Daylight cinema negative printed on Kodak 2383 | `Joey-LJ/LUTS` **`FUJI-ETERNA` -> Apple Log 2** (`33pt`) | Chromasmith **`vision3_250d_2383.cube`** (`GPL-3.0`, `33pt`) |
| **`F12` Kodak Ektar** | Crisp daylight micro-contrast & punchy primaries | `Joey-LJ/LUTS` **`FUJI-VELVIA` -> Apple Log 2** (`33pt`) | Chromasmith **`ektar_100_endura_premier.cube`** (`GPL-3.0`, `33pt`) |
| **`F13` Kodak P800** | High-speed Portra 800 street/documentary grain color | `Joey-LJ/LUTS` **`FUJI-ASTIA` -> Apple Log 2** (`33pt`) | Chromasmith **`portra_800_endura_premier.cube`** (`GPL-3.0`, `33pt`) |
| **`F14` Lomo92 Vintage** | Lifted matte blacks, nostalgic analog color shift | Luttie *Faded Kodak* (`Apple Log 2` `#406` / `Apple Log` `#395`) | `slaycamera/luts` **`slay-02-fade.cube`** & Chromasmith **`nostalgic_neg_composed.cube`** (`33pt`) |

---

## 2. Deep-Web Portal & Creator Share Discovery Matrix

| Source / Portal | Access Classification | Color Pipeline Coverage | Mobile Grid Compatibility Notes |
| :--- | :--- | :--- | :--- |
| **Luma Dune (`lumadune.com/luts/apple-log`)** | **`ZERO-LOGIN DIRECT`** (`res.lumadune.com`) | `Apple Log 2 -> Rec.709` & `Apple Log -> Rec.709` | Ships both `-33.cube` (**PASS** for Blackmagic Camera iOS) and `-65.cube` (**REJECT** desktop-only). |
| **Rodrigo Polo (`rodrigopolo.com`)** | **`ZERO-LOGIN DIRECT`** (`wp-content/uploads/2025/11/`) | `Apple Log 2 -> Rec.709` & `ProRes RAW -> Apple Log 2 -> Rec.709` | Ships `_33_Grid.cube` (**PASS** mobile monitoring) and `_65_Grid.cube` (**REJECT** desktop NLE). |
| **Luttie (`luttie.app/luts/camera/blackmagic`)** | **`ZERO-LOGIN DIRECT`** (`/api/lut-assets/<id>?download=...cube`) | `Apple Log 2` (`401–411`), `Apple Log` (`390–400`), `Rec. 709` (`3–8`, `140–142`, `629`, `720–721`) | 34 zero-signup `33-point` `.cube` endpoints built specifically for Blackmagic Camera iOS. |
| **Bransford Media (`bransfordmedia.com/luts/blackmagic-camera-app`)** | **`ZERO-LOGIN DIRECT (.zip)`** | `apple-log-2.zip` & `apple-log.zip` | Free `33-point` monitoring LUTs for Blackmagic Camera app (extract `.zip` in iOS Files before importing). |
| **Joey-LJ (`github.com/Joey-LJ/LUTS`)** | **`ZERO-LOGIN GITHUB RAW`** | **Fuji GFX -> Apple Log 2** (`iPhone 17 Pro`) | All 8 `.cube`s (`ETERNA`, `ETERNA-BB`, `CC`, `CN`, `ASTIA`, `PROVIA`, `VELVIA`, `ACROS`) are `33×33×33`. |
| **Raycal Tech (`github.com/raycalrui/raycal-luts`)** | **`ZERO-LOGIN GITHUB RAW + RELEASE ZIP`** | `Apple Log 2` & `Apple Log` (`natural` + `cinematic`) | All 4 `.cube`s are `33×33×33`. |
| **slay (`github.com/slaycamera/luts`)** | **`ZERO-LOGIN GITHUB RAW (`CC BY 4.0`)`** | `Rec. 709 SDR` (`iPhone 17` & `17 Air`) | All 5 `.cube`s (`amber`, `fade`, `neon`, `film`, `portrait`) are `33×33×33`. |
| **Chromasmith (`github.com/TareqAmeer/Chroma-App`)** | **`ZERO-LOGIN GITHUB RAW (`GPL-3.0`)`** | `Rec. 709 SDR` Film & Print Emulations | All 48 calibrated Kodak Vision3 / Portra / Ektar / Fuji `.cube`s are `33×33×33`. |
| **scernst13 (`github.com/scernst13/HaldCLUT-Cube-Files`)** | **`ZERO-LOGIN GITHUB RAW (`CC0 1.0`)`** | `Rec. 709 SDR` Kodak Still Stocks | All 14 Kodak Portra / Ektachrome `.cube`s are `33×33×33`. |
| **NoPixels (`nopixels.net/hlg-to-rec709/`)** | **`ZERO-LOGIN DIRECT (.zip)`** | `Rec. 2020 HLG -> Rec. 709 SDR` | Community standard HLG-to-709 transform (`nopixels_net_hlg2020_to_rec709_2.0.zip`). |
| **Animesh-Does-Code (`HDR-to-SDR-LUTs_YouTube`)** | **`ZERO-LOGIN GITHUB RAW + RELEASE ZIP`** | `Rec. 2100 PQ (ST.2084) -> Rec. 709 SDR` (`400–2000 nits`) | All 7 `.cube`s are `33×33×33` (note: PQ-input HDR tone-mapping, distinct from raw camera HLG). |
| **Fujifilm Official Support (`fujifilm-x.com`)** | **`ZERO-LOGIN DIRECT (.zip)`** | `F-Log / F-Log2 -> ETERNA & Rec. 709` | Official archives contain both `33grid` (**PASS**) and `65grid` (**REJECT**); expects F-Log/F-Log2 input unless CST-adapted. |
| **Tobia Montanari (`tobiamontanari.com`)** | **`QUARANTINED (ALTCHA + GUMROAD)`** | Apple Log LUTs | Gated behind WordPress Altcha proof-of-work + Gumroad checkout. |
| **FixThePhoto (`fixthephoto.com/free-luts`)** | **`QUARANTINED (EMAIL-GATED)`** | Generic Rec. 709 LUTs | Requires email form submission. |
| **Apple Developer (`developer.apple.com/download/`)** | **`QUARANTINED (APPLE ID + 65pt)`** | Official Apple Log LUTs | Requires Apple Developer sign-in and ships `65×65×65` desktop `.cube` files. |
| **Pond5 / RocketStock** | **`QUARANTINED (HTTP 403)`** | Generic Rec. 709 pack | Public HTTP access blocked (`403 Forbidden`). |
