# Master Zero-Login 3D LUT Directory — iPhone 17 Series (Blackmagic Camera iOS)

> **Orchestrator:** Agy (`t19` — Lead Color Architect, Herdr Workspace `LUTs / lut-orchestrator`)  
> **Sub-Agents:** `gemini-scout` (`t1g` — Deep-Web & GuVue Audit; `gemini_scout_findings.md`) · `opencode-extractor` (`t1h` — Live Online Portal Extraction, GitHub Cloning & Binary `.cube` Grid Verification; `guvue_audit.md`, `opencode_verified_luts.md`, `verify_cubes.py`)  
> **Target Hardware:** `iPhone 17`, `iPhone 17 Air`, `iPhone 17 Pro`, `iPhone 17 Pro Max`  
> **Target App:** Blackmagic Camera for iOS (`LUT_3D_SIZE 17` / `LUT_3D_SIZE 33` `.cube` 3D LUTs ONLY)  
> **Live Binary Audit Summary:** **`300`** GitHub/local `.cube`s + **`37`** live-fetched portal URLs + **`22`** user `~/Downloads` `.cube`s parsed → **All `78` bundled `.cube`s strictly binary-verified `33×33×33` (`35,937` RGB triplets)** · **`178+` REJECTED** (`65pt` desktop-only incl. `~/Downloads/Rec.709_Conversion.cube`, `25pt`, `13pt`, `1D`)  
> **Ready-to-AirDrop Local Bundle (`20.79 MB`):** `/tmp/lut_scavenger/IPHONE17_BLACKMAGIC_VERIFIED_33PT_LUTS.zip` (**`78` strict `33×33×33` `.cube` files**, including the **8 official GuVue `F11–F14` Free Sample LUTs** + Illustrated PDF Guide)

---

## 1. iPhone 17 Series Color Pipeline Matrix (Critical Before Importing)

Applying the wrong input-space LUT is the #1 cause of clipped highlights and crushed neon shadows on iPhone footage. Match your iPhone 17 model and Blackmagic Camera **Color Space** setting to the exact LUT bucket below:

| Device Model | Native Blackmagic Camera Color Spaces | Required `.cube` LUT Input Space | Required Grid Size | Critical Color Architect Rule |
| :--- | :--- | :--- | :--- | :--- |
| **iPhone 17 Pro** & **iPhone 17 Pro Max** | **Apple Log 2** (*Apple Wide Gamut*), **Apple Log** (*Rec. 2020*), **ProRes RAW**, **HLG**, **Rec. 709** | **Bucket 1 (`Apple Log 2`)** or **Bucket 2 (`Apple Log`)** | **`33×33×33`** (`35,937` triplets) or `17×17×17` (`4,913` triplets) | **Apple Log 2** reallocates midtones/highlights lower than original Apple Log v1 for wider dynamic range. Use dedicated **Apple Log 2** LUTs when shooting Apple Log 2; do **not** stack two Log-to-709 LUTs. |
| **iPhone 17** & **iPhone 17 Air** | **Rec. 709 SDR** & **Rec. 2020 HLG HDR** *(No native Apple Log / ProRes Log)* | **Bucket 3 (`Rec. 709 SDR`)** or **Bucket 4 (`HLG -> Rec. 709`)** | **`33×33×33`** (`35,937` triplets) or `17×17×17` (`4,913` triplets) | **NEVER** apply an Apple Log or Apple Log 2 LUT to base `iPhone 17` or `17 Air` footage—it will double-expand contrast and clip skin/sky highlights. Shoot **Rec. 709** with Bucket 3 LUTs, or **HLG** with Bucket 4 LUTs. |

> **Why `65×65×65` (`.cube`) LUTs Are Strictly Rejected Here:** Desktop grading suites (DaVinci Resolve, Premiere Pro, Final Cut Pro) use `65pt` grids (`274,625` RGB triplets, ~7–10 MB per file). Blackmagic Camera on iOS is architected for real-time mobile GPU trilinear/tetrahedral viewfinder monitoring using **`17pt` (`4,913` triplets)** and **`33pt` (`35,937` triplets, ~0.5–1.4 MB)** `.cube` files. All `65pt`, `64pt`, `25pt`, and `1D` LUTs discovered during our scavenge were quarantined and rejected (see **Section 7**).

---

## 2. Priority Target Forensic Audit: GuVue LUTs (`guvueluts.com`)

Both `opencode-extractor` (`guvue_audit.md`) and Orchestrator Search Grounding audited `guvueluts.com` (`Shopify shop_id: 71935393875`), its XML sitemaps, `agents.md`, and public product DOMs:

### 2.1 Official GuVue Store Findings
| Product | URL | Documented Specs | Free Trial / Access Status | Zero-Login Binary Link? |
| :--- | :--- | :--- | :--- | :--- |
| **GuVue Film Collection LUT Pack** ($48 USD) | `https://guvueluts.com/products/guvue-film-collection-lut-pack` | **28 `.cube` files**: 14 looks (`F01–F14`) × 2 inputs (**Apple Log 2** + **Rec. 709**) | **"4 Free Trial Looks" (`F11–F14`)** at `#film-samples`: **`F11` Kodak 250D Cinema**, **`F12` Kodak Ektar Daylight**, **`F13` Kodak P800 Documentary**, **`F14` Lomo92 Vintage**. | **NOW BUNDLED LOCALLY (`8/8` Binary-Verified `33pt`)!** Web form is `EMAIL + hCAPTCHA GATED`, and from your downloaded `GuVue_Film_Collection_4_Free_Sample_Looks_EN.zip`, all **8 `.cube` files** (`4× AppleLog2` + `4× Rec709`, `35,937` triplets each) + official PDF guide are verified and packed in `00_GuVue_Official_Film_Samples_33pt/`. |
| **GuVue HK Series LUT Pack** ($38 USD) | `https://guvueluts.com/products/guvue-hk-series-lut-pack` | **12 `33-point .cube` files**: 6 looks (**`HK01` Amber**, **`HK02` Pale Green**, **`HK03` Harbor Blue**, **`HK04` Island Cyan**, **`HK05` Avenue Star**, **`HK06` Mong Kok**) × 2 inputs (**Apple Log** + **`_709` Rec. 709**) | **Paid Commercial Checkout Only.** No free trial form on the HK page and no legitimate zero-login sample `.cube` links on YouTube or Reddit. | **NO (`PAID`).** Replaced below with verified zero-login `33pt` `.cube` matches for every single HK & F11–F14 look. |

### 2.2 Verified Zero-Login `33-Point .cube` Replacements for GuVue *HK Series* (`HK01–HK06`) & *Film Trial* (`F11–F14`)

Every replacement below is **100% free, zero-login**, and **`33×33×33` (`35,937` triplets)**—matched to both **iPhone 17 Pro / Pro Max (`Apple Log 2` / `Apple Log`)** and **iPhone 17 / 17 Air (`Rec. 709 SDR`)**:

| GuVue Look Target | Color Signature | Zero-Login `33pt` Match for **iPhone 17 Pro / Pro Max (`Apple Log 2`)** | Zero-Login `33pt` Match for **iPhone 17 & 17 Air (`Rec. 709 SDR`)** |
| :--- | :--- | :--- | :--- |
| **`HK01` Amber** | Golden-hour tungsten street warmth, soft highlight roll-off | **Luttie — Warm Golden Hour (Apple Log 2)**<br>`https://luttie.app/api/lut-assets/411?download=Warm%20Golden%20Hour%20(Apple%20Log%202).cube` | **slay — `slay-01-amber.cube`** *(CC BY 4.0, Binary-Verified 33pt)*<br>`https://raw.githubusercontent.com/slaycamera/luts/main/luts/slay-01-amber.cube` |
| **`HK02` Pale Green** | Wong Kar-wai fluorescent jade/sage editorial shadows | **Joey-LJ — `FUJI-CN` Classic Neg to Apple Log 2** *(Binary-Verified 33pt)*<br>`https://raw.githubusercontent.com/Joey-LJ/LUTS/main/Fuji_GFX%20to%20Apple_Log_2%20LUT/FUJI-CN_1.A001_11220924_C056.cube` | **Chromasmith — `fuji_pro_400h_ca_maxima.cube`** *(GPL-3.0, Binary-Verified 33pt)*<br>`https://raw.githubusercontent.com/TareqAmeer/Chroma-App/main/tools/calib/LUT%20LIBRARY/fuji_pro_400h_ca_maxima.cube` |
| **`HK03` Harbor Blue** | Deep Victoria Harbour slate-blue shadows, cool steel midtones | **Luttie — Cool Blue Steel (Apple Log 2)**<br>`https://luttie.app/api/lut-assets/404?download=Cool%20Blue%20Steel%20(Apple%20Log%202).cube` | **slay — `slay-04-film.cube`** *(CC BY 4.0, Binary-Verified 33pt)*<br>`https://raw.githubusercontent.com/slaycamera/luts/main/luts/slay-04-film.cube` |
| **`HK04` Island Cyan** | Teal-cyan night harbour split with clean tungsten skin | **Luttie — Moody Cinematic Dark Teal (Apple Log 2)**<br>`https://luttie.app/api/lut-assets/409?download=Moody%20Cinematic%20(Apple%20Log%202).cube` | **Chromasmith — `vision3_500t_2383.cube`** *(GPL-3.0, Binary-Verified 33pt)*<br>`https://raw.githubusercontent.com/TareqAmeer/Chroma-App/main/tools/calib/LUT%20LIBRARY/vision3_500t_2383.cube` |
| **`HK05` Avenue Star** | Cinema print contrast, theatrical D60/ETERNA highlight curve | **Raycal — `Apple Log 2_cinematic.cube`** *(Binary-Verified 33pt)*<br>`https://raw.githubusercontent.com/raycalrui/raycal-luts/main/LUTs/Apple%20Log%202_cinematic.cube` | **imnz730 — `Rec709 Fujifilm 3513DI D60.cube`** *(Binary-Verified 33pt)*<br>`https://raw.githubusercontent.com/imnz730/LUTs/master/Film%20Looks/Rec709%20Fujifilm%203513DI%20D60.cube` |
| **`HK06` Mong Kok** | Dense neon-night cyan shadows + electric magenta signage punch | **Luttie — Cyberpunk Neon (Apple Log 2)**<br>`https://luttie.app/api/lut-assets/405?download=Cyberpunk%20Neon%20(Apple%20Log%202).cube` | **slay — `slay-03-neon.cube`** *(CC BY 4.0, Binary-Verified 33pt)*<br>`https://raw.githubusercontent.com/slaycamera/luts/main/luts/slay-03-neon.cube` |
| **`F11` Kodak 250D** | Daylight motion-picture negative printed on Kodak 2383 | **Joey-LJ — `FUJI-ETERNA` to Apple Log 2** *(Binary-Verified 33pt)*<br>`https://raw.githubusercontent.com/Joey-LJ/LUTS/main/Fuji_GFX%20to%20Apple_Log_2%20LUT/FUJI-ETERNA_1.A001_11220924_C056.cube` | **Chromasmith — `vision3_250d_2383.cube`** *(Binary-Verified 33pt)*<br>`https://raw.githubusercontent.com/TareqAmeer/Chroma-App/main/tools/calib/LUT%20LIBRARY/vision3_250d_2383.cube` |
| **`F12` Kodak Ektar** | Punchy daylight saturation, crisp micro-contrast | **Joey-LJ — `FUJI-VELVIA` to Apple Log 2** *(Binary-Verified 33pt)*<br>`https://raw.githubusercontent.com/Joey-LJ/LUTS/main/Fuji_GFX%20to%20Apple_Log_2%20LUT/FUJI-VELVIA_1.A001_11220924_C056.cube` | **Chromasmith — `ektar_100_endura_premier.cube`** *(Binary-Verified 33pt)*<br>`https://raw.githubusercontent.com/TareqAmeer/Chroma-App/main/tools/calib/LUT%20LIBRARY/ektar_100_endura_premier.cube` |
| **`F13` Kodak P800** | High-speed Portra 800 street/documentary warmth | **Joey-LJ — `FUJI-ASTIA` to Apple Log 2** *(Binary-Verified 33pt)*<br>`https://raw.githubusercontent.com/Joey-LJ/LUTS/main/Fuji_GFX%20to%20Apple_Log_2%20LUT/FUJI-ASTIA_1.A001_11220924_C056.cube` | **Chromasmith — `portra_800_endura_premier.cube`** *(Binary-Verified 33pt)*<br>`https://raw.githubusercontent.com/TareqAmeer/Chroma-App/main/tools/calib/LUT%20LIBRARY/portra_800_endura_premier.cube` |
| **`F14` Lomo92 Vintage** | Lifted matte blacks, nostalgic analog color shift | **Luttie — Faded Kodak (Apple Log 2)**<br>`https://luttie.app/api/lut-assets/406?download=Faded%20Kodak%20(Apple%20Log%202).cube` | **slay — `slay-02-fade.cube`** & **`nostalgic_neg_composed.cube`** *(Binary-Verified 33pt)*<br>`https://raw.githubusercontent.com/slaycamera/luts/main/luts/slay-02-fade.cube` |

---

## 3. Bucket 1: Apple Log 2 / Apple Wide Gamut (`33pt` `.cube` — iPhone 17 Pro & 17 Pro Max)

Use these LUTs when Blackmagic Camera **Settings → Record → Color Space** is set to **Apple Log 2** (or **Apple Log 2 - HDR**) on **iPhone 17 Pro** and **iPhone 17 Pro Max**.

### 3.1 Technical Conversion LUTs (`Apple Log 2 -> Rec. 709` Neutral)
| LUT Name | Creator / Source | Grid Size | Verification | Direct Zero-Login `.cube` / `.zip` URL |
| :--- | :--- | :--- | :--- | :--- |
| **AppleLog2ToRec709-v1.0-33.cube** | Luma Dune (`lumadune.com/luts/apple-log`) | `33×33×33` | Public DOM HTTP 200 (`-65.cube` rejected) | `https://res.lumadune.com/static-lut-files/AppleLog2ToRec709-v1.0-33.cube` |
| **AppleLog2_to_Rec709_33_Grid.cube** | Rodrigo Polo (`rodrigopolo.com`) | `33×33×33` | Public DOM HTTP 200 (`_65_Grid` rejected) | `https://rodrigopolo.com/wp-content/uploads/2025/11/AppleLog2_to_Rec709_33_Grid.cube` |
| **OtherProResRAW_AppleLog2_to_Rec709_33_Grid.cube** | Rodrigo Polo (`rodrigopolo.com`) | `33×33×33` | Public DOM HTTP 200 (ProRes RAW -> Log 2) | `https://rodrigopolo.com/wp-content/uploads/2025/11/OtherProResRAW_AppleLog2_to_Rec709_33_Grid.cube` |
| **Apple Log 2_natural.cube** | Raycal Tech (`raycalrui/raycal-luts`) | `33×33×33` | **Binary-Verified** (`35,937` triplets, 867 KB) | `https://raw.githubusercontent.com/raycalrui/raycal-luts/main/LUTs/Apple%20Log%202_natural.cube` |
| **Bransford Media Apple Log 2 Free Pack** | Bransford Media (`bransfordmedia.com`) | `33×33×33` (`.zip`) | Public DOM HTTP 200 (Unzip in iOS Files first) | `https://bransfordmedia.com/luts/free-look/apple-log-2.zip` |

### 3.2 All-in-One Creative & Film Simulation LUTs (`Apple Log 2 -> Graded Rec. 709`)
*(Single-stage LUTs built specifically for **iPhone 17 Pro Apple Log 2**—do NOT stack on top of a technical conversion LUT!)*

| LUT Name | Aesthetic / Film Simulation | Grid Size | Verification | Direct Zero-Login `.cube` URL |
| :--- | :--- | :--- | :--- | :--- |
| **FUJI-ETERNA (Apple Log 2)** | Fujifilm GFX ETERNA Cinema soft highlight roll-off | `33×33×33` | **Binary-Verified** (`35,937` triplets, 997 KB) | `https://raw.githubusercontent.com/Joey-LJ/LUTS/main/Fuji_GFX%20to%20Apple_Log_2%20LUT/FUJI-ETERNA_1.A001_11220924_C056.cube` |
| **FUJI-ETERNA-BB (Apple Log 2)** | Fujifilm GFX ETERNA Bleach Bypass gritty silver | `33×33×33` | **Binary-Verified** (`35,937` triplets, 995 KB) | `https://raw.githubusercontent.com/Joey-LJ/LUTS/main/Fuji_GFX%20to%20Apple_Log_2%20LUT/FUJI-ETERNA-BB_1.A001_11220924_C056.cube` |
| **FUJI-CC Classic Chrome (Apple Log 2)** | Documentary muted editorial chroma, rich shadows | `33×33×33` | **Binary-Verified** (`35,937` triplets, 1.01 MB) | `https://raw.githubusercontent.com/Joey-LJ/LUTS/main/Fuji_GFX%20to%20Apple_Log_2%20LUT/FUJI-CC_1.A001_11220924_C056.cube` |
| **FUJI-CN Classic Neg (Apple Log 2)** | Street photography sage-green shadows & warm reds | `33×33×33` | **Binary-Verified** (`35,937` triplets, 1.00 MB) | `https://raw.githubusercontent.com/Joey-LJ/LUTS/main/Fuji_GFX%20to%20Apple_Log_2%20LUT/FUJI-CN_1.A001_11220924_C056.cube` |
| **FUJI-ASTIA (Apple Log 2)** | Soft portrait skin tones & smooth pastel saturation | `33×33×33` | **Binary-Verified** (`35,937` triplets, 947 KB) | `https://raw.githubusercontent.com/Joey-LJ/LUTS/main/Fuji_GFX%20to%20Apple_Log_2%20LUT/FUJI-ASTIA_1.A001_11220924_C056.cube` |
| **FUJI-PROVIA (Apple Log 2)** | Standard slide film balanced natural color | `33×33×33` | **Binary-Verified** (`35,937` triplets, 865 KB) | `https://raw.githubusercontent.com/Joey-LJ/LUTS/main/Fuji_GFX%20to%20Apple_Log_2%20LUT/FUJI-PROVIA_1.A001_11220924_C056.cube` |
| **FUJI-VELVIA (Apple Log 2)** | Vivid landscape & golden-hour saturation | `33×33×33` | **Binary-Verified** (`35,937` triplets, 944 KB) | `https://raw.githubusercontent.com/Joey-LJ/LUTS/main/Fuji_GFX%20to%20Apple_Log_2%20LUT/FUJI-VELVIA_1.A001_11220924_C056.cube` |
| **FUJI-ACROS (Apple Log 2)** | Fine-grain medium-format monochrome B&W | `33×33×33` | **Binary-Verified** (`35,937` triplets, 999 KB) | `https://raw.githubusercontent.com/Joey-LJ/LUTS/main/Fuji_GFX%20to%20Apple_Log_2%20LUT/FUJI-ACROS_1.A001_11220924_C056.cube` |
| **Apple Log 2_cinematic.cube** | Raycal Tech stylized teal-and-orange cinema grade | `33×33×33` | **Binary-Verified** (`35,937` triplets, 867 KB) | `https://raw.githubusercontent.com/raycalrui/raycal-luts/main/LUTs/Apple%20Log%202_cinematic.cube` |
| **Luttie — Cyberpunk Neon (Log 2)** | Cyan & magenta night-street neon (`HK06` match) | `33×33×33` | Public DOM HTTP 200 (`luttie.app`) | `https://luttie.app/api/lut-assets/405?download=Cyberpunk%20Neon%20(Apple%20Log%202).cube` |
| **Luttie — Moody Cinematic (Log 2)** | Dark teal film shadow curve (`HK04` match) | `33×33×33` | Public DOM HTTP 200 (`luttie.app`) | `https://luttie.app/api/lut-assets/409?download=Moody%20Cinematic%20(Apple%20Log%202).cube` |
| **Luttie — Faded Kodak (Log 2)** | Vintage analog film emulation (`F14` match) | `33×33×33` | Public DOM HTTP 200 (`luttie.app`) | `https://luttie.app/api/lut-assets/406?download=Faded%20Kodak%20(Apple%20Log%202).cube` |
| **Luttie — Cool Blue Steel (Log 2)** | Cold harbour slate tone (`HK03` match) | `33×33×33` | Public DOM HTTP 200 (`luttie.app`) | `https://luttie.app/api/lut-assets/404?download=Cool%20Blue%20Steel%20(Apple%20Log%202).cube` |
| **Luttie — Warm Golden Hour (Log 2)** | Sunset amber warmth (`HK01` match) | `33×33×33` | Public DOM HTTP 200 (`luttie.app`) | `https://luttie.app/api/lut-assets/411?download=Warm%20Golden%20Hour%20(Apple%20Log%202).cube` |
| **Luttie — Cinematic Teal & Orange (Log 2)** | Blockbuster complementary contrast | `33×33×33` | Public DOM HTTP 200 (`luttie.app`) | `https://luttie.app/api/lut-assets/402?download=Cinematic%20Teal%20%26%20Orange%20(Apple%20Log%202).cube` |
| **Luttie — Matte Fade (Log 2)** | Soft lifted-black editorial matte | `33×33×33` | Public DOM HTTP 200 (`luttie.app`) | `https://luttie.app/api/lut-assets/408?download=Matte%20Fade%20(Apple%20Log%202).cube` |
| **Luttie — Soft Portrait (Log 2)** | Gentle skin-tone rolloff | `33×33×33` | Public DOM HTTP 200 (`luttie.app`) | `https://luttie.app/api/lut-assets/410?download=Soft%20Portrait%20(Apple%20Log%202).cube` |
| **Luttie — Bright & Airy (Log 2)** | Clean daylight lifestyle lift | `33×33×33` | Public DOM HTTP 200 (`luttie.app`) | `https://luttie.app/api/lut-assets/401?download=Bright%20%26%20Airy%20(Apple%20Log%202).cube` |
| **Luttie — High Contrast (Log 2)** | Punchy dramatic contrast | `33×33×33` | Public DOM HTTP 200 (`luttie.app`) | `https://luttie.app/api/lut-assets/407?download=High%20Contrast%20(Apple%20Log%202).cube` |
| **Luttie — Classic B&W (Log 2)** | Silver-gelatin monochrome | `33×33×33` | Public DOM HTTP 200 (`luttie.app`) | `https://luttie.app/api/lut-assets/403?download=Classic%20B%26W%20(Apple%20Log%202).cube` |

---

## 4. Bucket 2: Apple Log / Rec. 2020 (`33pt` `.cube` — iPhone 17 Pro & 17 Pro Max)

Use these when shooting standard **Apple Log (v1 / Rec. 2020)** in Blackmagic Camera on **iPhone 17 Pro** or **17 Pro Max** (or matching legacy iPhone 15 Pro / 16 Pro B-cam footage).

| LUT Name | Function / Style | Grid Size | Verification | Direct Zero-Login `.cube` / `.zip` URL |
| :--- | :--- | :--- | :--- | :--- |
| **AppleLogToRec709-v1.0-33.cube** | Neutral technical conversion (`Apple Log -> Rec. 709`) | `33×33×33` | Public DOM HTTP 200 (`lumadune.com`) | `https://res.lumadune.com/static-lut-files/AppleLogToRec709-v1.0-33.cube` |
| **Apple Log_natural.cube** | Raycal Tech natural Rec. 709 restoration | `33×33×33` | **Binary-Verified** (`35,937` triplets, 894 KB) | `https://raw.githubusercontent.com/raycalrui/raycal-luts/main/LUTs/Apple%20Log_natural.cube` |
| **Apple Log_cinematic.cube** | Raycal Tech stylized cinema look | `33×33×33` | **Binary-Verified** (`35,937` triplets, 926 KB) | `https://raw.githubusercontent.com/raycalrui/raycal-luts/main/LUTs/Apple%20Log_cinematic.cube` |
| **Raycal-LUT-Pack.zip** | Complete 4-LUT Apple Log + Log 2 ZIP release | `33×33×33` (`.zip`) | GitHub Release Asset | `https://github.com/raycalrui/raycal-luts/releases/latest/download/Raycal-LUT-Pack.zip` |
| **Bransford Media Apple Log Pack** | Blackmagic Camera monitoring `.zip` | `33×33×33` (`.zip`) | Public DOM HTTP 200 (`bransfordmedia.com`) | `https://bransfordmedia.com/luts/free-look/apple-log.zip` |
| **Luttie — Cyberpunk Neon (Apple Log)** | Neon cyan/magenta night look | `33×33×33` | Public DOM HTTP 200 (`luttie.app`) | `https://luttie.app/api/lut-assets/394?download=Cyberpunk%20Neon%20(Apple%20Log).cube` |
| **Luttie — Moody Cinematic (Apple Log)** | Dark teal atmospheric cinema | `33×33×33` | Public DOM HTTP 200 (`luttie.app`) | `https://luttie.app/api/lut-assets/398?download=Moody%20Cinematic%20(Apple%20Log).cube` |
| **Luttie — Faded Kodak (Apple Log)** | Analog Kodak fade | `33×33×33` | Public DOM HTTP 200 (`luttie.app`) | `https://luttie.app/api/lut-assets/395?download=Faded%20Kodak%20(Apple%20Log).cube` |
| **Luttie — Cool Blue Steel (Apple Log)** | Cold slate blue | `33×33×33` | Public DOM HTTP 200 (`luttie.app`) | `https://luttie.app/api/lut-assets/393?download=Cool%20Blue%20Steel%20(Apple%20Log).cube` |
| **Luttie — Warm Golden Hour (Apple Log)** | Amber sunset glow | `33×33×33` | Public DOM HTTP 200 (`luttie.app`) | `https://luttie.app/api/lut-assets/400?download=Warm%20Golden%20Hour%20(Apple%20Log).cube` |
| **Luttie — Cinematic Teal & Orange (Log)** | Hollywood color contrast | `33×33×33` | Public DOM HTTP 200 (`luttie.app`) | `https://luttie.app/api/lut-assets/391?download=Cinematic%20Teal%20%26%20Orange%20(Apple%20Log).cube` |
| **Luttie — Matte Fade / Soft Portrait / Bright & Airy / High Contrast / Classic B&W (Apple Log)** | Remaining 5 Luttie Apple Log 33pt looks (`390, 392, 396, 397, 399`) | `33×33×33` | Public DOM HTTP 200 (`luttie.app/luts/camera/blackmagic`) | `https://luttie.app/api/lut-assets/397?download=Matte%20Fade%20(Apple%20Log).cube` *(plus IDs `390`, `392`, `396`, `399`)* |

---

## 5. Bucket 3: Rec. 709 SDR Creative & Film Print (`33pt` `.cube` — iPhone 17, iPhone 17 Air, & Post-709)

**Primary Pack for base `iPhone 17` and `iPhone 17 Air`** (set Blackmagic Camera **Color Space → Rec. 709**), and also usable as a creative second node **after** converting Log to Rec. 709 on `17 Pro / Pro Max`.

### 5.1 `slaycamera/luts` — Open-Source iPhone Camera LUTs (`CC BY 4.0`, Binary-Verified `33pt`)
| LUT Name | Look Profile | Triplets / Size | Direct Zero-Login `.cube` URL |
| :--- | :--- | :--- | :--- |
| **`slay-01-amber.cube`** | Golden-hour sunset warmth, gentle contrast (*GuVue HK01 Amber match*) | `35,937` (`33pt`) | `https://raw.githubusercontent.com/slaycamera/luts/main/luts/slay-01-amber.cube` |
| **`slay-02-fade.cube`** | Lifted matte blacks, muted analog film starter (*GuVue F14 match*) | `35,937` (`33pt`) | `https://raw.githubusercontent.com/slaycamera/luts/main/luts/slay-02-fade.cube` |
| **`slay-03-neon.cube`** | Cyan shadows + magenta highlights night-city punch (*GuVue HK06 Mong Kok match*) | `35,937` (`33pt`) | `https://raw.githubusercontent.com/slaycamera/luts/main/luts/slay-03-neon.cube` |
| **`slay-04-film.cube`** | Deep contrast, harbour teal shadows, warm skin (*GuVue HK03/HK04 match*) | `35,937` (`33pt`) | `https://raw.githubusercontent.com/slaycamera/luts/main/luts/slay-04-film.cube` |
| **`slay-05-portrait.cube`** | Flattering warm skin tones & soft highlight roll-off | `35,937` (`33pt`) | `https://raw.githubusercontent.com/slaycamera/luts/main/luts/slay-05-portrait.cube` |

### 5.2 Chromasmith Calibrated Motion-Picture & Still Film Stocks (`TareqAmeer/Chroma-App`, `GPL-3.0`, All 48 Binary-Verified `33pt`)
| Stock Category | LUT Filename | Triplets / Size | Direct Zero-Login `.cube` URL |
| :--- | :--- | :--- | :--- |
| **Kodak Vision3 500T -> 2383 Print** | `vision3_500t_2383.cube` | `35,937` (`33pt`) | `https://raw.githubusercontent.com/TareqAmeer/Chroma-App/main/tools/calib/LUT%20LIBRARY/vision3_500t_2383.cube` |
| **Kodak Vision3 250D -> 2383 Print** | `vision3_250d_2383.cube` | `35,937` (`33pt`) | `https://raw.githubusercontent.com/TareqAmeer/Chroma-App/main/tools/calib/LUT%20LIBRARY/vision3_250d_2383.cube` |
| **Kodak Vision3 200T -> 2383 Print** | `vision3_200t_2383.cube` | `35,937` (`33pt`) | `https://raw.githubusercontent.com/TareqAmeer/Chroma-App/main/tools/calib/LUT%20LIBRARY/vision3_200t_2383.cube` |
| **Kodak Vision3 50D -> 2383 Print** | `vision3_50d_2383.cube` | `35,937` (`33pt`) | `https://raw.githubusercontent.com/TareqAmeer/Chroma-App/main/tools/calib/LUT%20LIBRARY/vision3_50d_2383.cube` |
| **Kodak Vision3 500T -> 2393 Premier** | `vision3_500t_2393.cube` | `35,937` (`33pt`) | `https://raw.githubusercontent.com/TareqAmeer/Chroma-App/main/tools/calib/LUT%20LIBRARY/vision3_500t_2393.cube` |
| **Fujifilm ETERNA Cinema** | `eterna_cinema_composed.cube` | `35,937` (`33pt`) | `https://raw.githubusercontent.com/TareqAmeer/Chroma-App/main/tools/calib/LUT%20LIBRARY/eterna_cinema_composed.cube` |
| **Fujifilm ETERNA Bleach Bypass** | `eterna_bleach_bypass_composed.cube` | `35,937` (`33pt`) | `https://raw.githubusercontent.com/TareqAmeer/Chroma-App/main/tools/calib/LUT%20LIBRARY/eterna_bleach_bypass_composed.cube` |
| **Fujifilm Classic Neg** | `classic_neg.cube` | `35,937` (`33pt`) | `https://raw.githubusercontent.com/TareqAmeer/Chroma-App/main/tools/calib/LUT%20LIBRARY/classic_neg.cube` |
| **Fujifilm Nostalgic Neg** | `nostalgic_neg_composed.cube` | `35,937` (`33pt`) | `https://raw.githubusercontent.com/TareqAmeer/Chroma-App/main/tools/calib/LUT%20LIBRARY/nostalgic_neg_composed.cube` |
| **Fujifilm Classic Chrome** | `classic_chrome_composed.cube` | `35,937` (`33pt`) | `https://raw.githubusercontent.com/TareqAmeer/Chroma-App/main/tools/calib/LUT%20LIBRARY/classic_chrome_composed.cube` |
| **Fujifilm Reala Ace** | `reala_ace_composed.cube` | `35,937` (`33pt`) | `https://raw.githubusercontent.com/TareqAmeer/Chroma-App/main/tools/calib/LUT%20LIBRARY/reala_ace_composed.cube` |
| **Fujifilm Pro 400H (*Pale Green*)** | `fuji_pro_400h_ca_maxima.cube` | `35,937` (`33pt`) | `https://raw.githubusercontent.com/TareqAmeer/Chroma-App/main/tools/calib/LUT%20LIBRARY/fuji_pro_400h_ca_maxima.cube` |
| **Fujifilm Natura 1600 Low-Light** | `fuji_natura_1600_ca_dpii.cube` | `35,937` (`33pt`) | `https://raw.githubusercontent.com/TareqAmeer/Chroma-App/main/tools/calib/LUT%20LIBRARY/fuji_natura_1600_ca_dpii.cube` |
| **Kodak Portra 400 Endura Premier** | `portra_400_endura_premier.cube` | `35,937` (`33pt`) | `https://raw.githubusercontent.com/TareqAmeer/Chroma-App/main/tools/calib/LUT%20LIBRARY/portra_400_endura_premier.cube` |
| **Kodak Portra 800 Endura Premier** | `portra_800_endura_premier.cube` | `35,937` (`33pt`) | `https://raw.githubusercontent.com/TareqAmeer/Chroma-App/main/tools/calib/LUT%20LIBRARY/portra_800_endura_premier.cube` |
| **Kodak Portra 160 Endura Premier** | `portra_160_endura_premier.cube` | `35,937` (`33pt`) | `https://raw.githubusercontent.com/TareqAmeer/Chroma-App/main/tools/calib/LUT%20LIBRARY/portra_160_endura_premier.cube` |
| **Kodak Ektar 100 Endura Premier** | `ektar_100_endura_premier.cube` | `35,937` (`33pt`) | `https://raw.githubusercontent.com/TareqAmeer/Chroma-App/main/tools/calib/LUT%20LIBRARY/ektar_100_endura_premier.cube` |
| **Kodak Gold 200 Endura Premier** | `gold_200_endura_premier.cube` | `35,937` (`33pt`) | `https://raw.githubusercontent.com/TareqAmeer/Chroma-App/main/tools/calib/LUT%20LIBRARY/gold_200_endura_premier.cube` |
| **Kodachrome 64 Radiance III** | `kodachrome_64_radiance_iii.cube` | `35,937` (`33pt`) | `https://raw.githubusercontent.com/TareqAmeer/Chroma-App/main/tools/calib/LUT%20LIBRARY/kodachrome_64_radiance_iii.cube` |
| **Kodak Double-X 5222 Cinema B&W** | `kodak_5222_polymax_grade_2.cube` | `35,937` (`33pt`) | `https://raw.githubusercontent.com/TareqAmeer/Chroma-App/main/tools/calib/LUT%20LIBRARY/kodak_5222_polymax_grade_2.cube` |
| **Kodak Tri-X 400 Street B&W** | `trix_400_polymax_grade_2.cube` | `35,937` (`33pt`) | `https://raw.githubusercontent.com/TareqAmeer/Chroma-App/main/tools/calib/LUT%20LIBRARY/trix_400_polymax_grade_2.cube` |

### 5.3 Theatre Print & Public-Domain Kodak Stocks (`imnz730/LUTs`, `scernst13`, & `Luttie` Rec. 709)
| LUT Name | Source / License | Grid Size | Direct Zero-Login `.cube` URL |
| :--- | :--- | :--- | :--- |
| **Rec709 Kodak 2383 D65.cube** *(also D55 / D60)* | `imnz730/LUTs` (Binary-Verified `35,937` triplets) | `33×33×33` | `https://raw.githubusercontent.com/imnz730/LUTs/master/Film%20Looks/Rec709%20Kodak%202383%20D65.cube` |
| **Rec709 Fujifilm 3513DI D65.cube** *(also D55 / D60)* | `imnz730/LUTs` (Binary-Verified `35,937` triplets) | `33×33×33` | `https://raw.githubusercontent.com/imnz730/LUTs/master/Film%20Looks/Rec709%20Fujifilm%203513DI%20D65.cube` |
| **Kodak Portra 400 / 800 / Ektachrome 100 VS** | `scernst13/HaldCLUT-Cube-Files` (**CC0 1.0 Public Domain**, 14 `33pt` LUTs) | `33×33×33` | `https://raw.githubusercontent.com/scernst13/HaldCLUT-Cube-Files/main/Kodak%20Converted/Kodak%20Portra%20400.cube` |
| **Luttie — Kodak 2383 Print (Rec. 709)** | `luttie.app/luts/kodak-2383` (Zero-Login Direct) | `33×33×33` | `https://luttie.app/api/lut-assets/721?download=Kodak%202383%20Print.cube` |
| **Luttie — Kodak Portra 400 (Rec. 709)** | `luttie.app/luts/portra-400` (Zero-Login Direct) | `33×33×33` | `https://luttie.app/api/lut-assets/720?download=Portra%20400.cube` |
| **Luttie — Cyberpunk Neon (Rec. 709)** | `luttie.app/luts/cyberpunk-neon` (Zero-Login Direct) | `33×33×33` | `https://luttie.app/api/lut-assets/142?download=Cyberpunk%20Neon%20LUT%20%E2%80%94%20Free%20Cyan%20%26%20Magenta%20Night%20Look.cube` |
| **Luttie — Moody Cinematic Dark Teal (Rec. 709)** | `luttie.app/luts/moody-cinematic` (Zero-Login Direct) | `33×33×33` | `https://luttie.app/api/lut-assets/140?download=Moody%20Cinematic%20LUT%20%E2%80%94%20Free%20Dark%20Teal%20Film%20Look.cube` |
| **Luttie — Faded Kodak (Rec. 709)** | `luttie.app/luts/faded-kodak` (Zero-Login Direct) | `33×33×33` | `https://luttie.app/api/lut-assets/6?download=Faded%20Kodak%20%E2%80%94%20Free%20Film%20Emulation%20LUT.cube` |

---

## 6. Bucket 4: HLG & HDR-to-SDR Conversion (`33pt` `.cube` — iPhone 17 & 17 Air HDR Workflows)

When shooting **Rec. 2020 HLG / HDR** on **iPhone 17** or **iPhone 17 Air** (to capture extra highlight headroom on non-Pro models without Apple Log), use an **HLG-to-Rec. 709** transform for SDR delivery, or attach **HDR-to-SDR** tone-mapping LUTs for SDR down-conversion:

| LUT / Archive Name | Transfer Curve Mapping | Grid Size | Verification | Direct Zero-Login URL |
| :--- | :--- | :--- | :--- | :--- |
| **NoPixels HLG BT.2020 to Rec. 709 v2.0** | `Rec. 2020 HLG -> Rec. 709 SDR` | `.cube` in `.zip` | Community standard HLG -> 709 LUT | `https://nopixels.net/hlg-to-rec709/` *(archive: `nopixels_net_hlg2020_to_rec709_2.0.zip`)* |
| **Blackmagic Broadcast Film to Rec2020 HLG v4** | `BMD Film -> Rec. 2020 HLG` | `33×33×33` | **Binary-Verified** (`35,937` triplets, 1.40 MB) | `https://raw.githubusercontent.com/imnz730/LUTs/master/Blackmagic%20Design/Blackmagic%20Broadcast%20Film%20to%20Rec2020%20HLG%20v4.cube` |
| **1000nits_HDR-to-SDR.cube** *(+ `400`, `600`, `800`, `1200`, `1500`, `2000` nits)* | `Rec. 2100 PQ (ST.2084) -> Rec. 709 Gamma 2.4` | `33×33×33` | **Binary-Verified** (`35,937` triplets, 521 KB) | `https://raw.githubusercontent.com/Animesh-Does-Code/HDR-to-SDR-LUTs_YouTube/main/1000nits_HDR-to-SDR.cube` |
| **HDR-to-SDR-LUTs_YouTube.zip** *(All 7 peak-nit `.cube`s)* | `Rec. 2100 PQ -> Rec. 709 SDR` | `33×33×33` (`.zip`) | GitHub Release Asset | `https://github.com/Animesh-Does-Code/HDR-to-SDR-LUTs_YouTube/releases/latest/download/HDR-to-SDR-LUTs_YouTube.zip` |
| **Fujifilm Official Support 3D-LUTs (`X-M5` / `GFX ETERNA 55`)** | `F-Log / F-Log2 -> ETERNA & Rec. 709` (`33grid` folder inside ZIP) | `33×33×33` & `65×65×65` | Official HTTP 200 (`fujifilm-x.com`) — **import ONLY `33grid` `.cube`s** | `https://dl.fujifilm-x.com/lut/x-m5-3d-lut-v100.zip`<br>`https://dl.fujifilm-x.com/lut/gfx-eterna-55-3d-lut-v100.zip` |

> **Color Architect Note on HLG vs. PQ (`ST.2084`):** The `Animesh-Does-Code` `400nits–2000nits` LUTs are generated for **Rec. 2100 ST.2084 (PQ)** HDR masters/YouTube tone-mapping. Do not apply PQ-input LUTs directly onto raw **Rec. 2020 HLG** camera clips in-camera without an HLG-to-PQ transform; for in-camera iPhone 17 / 17 Air shooting, **Rec. 709 SDR + Bucket 3 `33pt` LUTs** gives the cleanest real-time monitoring and skin roll-off.

---

## 7. Orchestrator Quality Audit: Quarantined & Rejected Sources

Every candidate source below was inspected and **excluded** from the active iPhone 17 zero-login directory for failing at least one strict requirement (`LUT_3D_SIZE` mobile compatibility, zero-login access, or anti-bot/email gating):

| Quarantined Source / Repo | Exact Failure Reason | Forensic Proof |
| :--- | :--- | :--- |
| **GuVue `#film-samples` (`F11–F14`)** | `EMAIL + hCAPTCHA GATED` | Uses Shopify Forms `forms-root-1238194` + `ce_storefront_forms_captcha_hcaptcha.v1.5.3.iife.js` email confirmation; no public `.cube` URL in DOM or sitemaps. |
| **GuVue `HK Series` (`HK01–HK06`)** | `PAID ($38 USD)` | Commercial Shopify digital download; no free tier. |
| **Tobia Montanari (`tobiamontanari.com`)** | `ALTCHA POW GATE + GUMROAD` | Uses `wp-content/plugins/altcha/` proof-of-work gate + external `logflowtools.gumroad.com` checkout. |
| **Apple Official Developer LUTs** | `APPLE ID LOGIN + 65pt` | Hosted behind `developer.apple.com/download/` sign-in and ships `65×65×65` desktop `.cube` tables. |
| **FixThePhoto Free LUTs** | `EMAIL-GATED` | Requires email form submission to receive download link. |
| **Pond5 / RocketStock 35 Free LUTs** | `HTTP 403 FORBIDDEN` | `https://www.pond5.com/blog/35-free-luts-color-grade-videos/` blocked automated public HTTP fetch (`403`). |
| **Luma Dune `-65.cube` & Rodrigo Polo `_65_Grid.cube`** | `REJECT (65pt Desktop-Only)` | `274,625`-triplet desktop NLE variants; only their `-33.cube` / `_33_Grid.cube` siblings are approved. |
| **`MokshC/Film-Emulation-LUTs` (GitHub)** | `REJECT (94/94 are 65pt)` | Binary header scan confirmed `LUT_3D_SIZE 65` (`274,625` triplets) across all 94 `.cube` files. |
| **`moritzsalla/LogGrade-macOS` (GitHub)** | `REJECT (4/4 are 65pt)` | All 4 Apple Log `.cube` files are `LUT_3D_SIZE 65` desktop macOS LUTs. |
| **`Royat07/S-Log3-to-Apple-Log` & `QuagKhai003/ReinaLook`** | `REJECT (65pt Desktop-Only)` | Confirmed `LUT_3D_SIZE 65` (`274,625` triplets). |
| **`YahiaAngelo/Film-Camera-IOS` (GitHub)** | `REJECT (8/8 are 13pt)` | Binary header scan confirmed `LUT_3D_SIZE 13` (`2,197` triplets, coarse non-standard mobile grid) rather than SMPTE/Blackmagic `17pt`/`33pt`. |
| **PictureFX CineStill 800T v2.0 (`drive_file_2.bin`)** | `REJECT (Non-standard 25pt)` | Downloaded binary (`437,658` bytes) has header `LUT_3D_SIZE 25` (`15,625` triplets, IWLTBAP non-standard grid); `drive_file_1.bin` is a `125×125` Hald PNG, not a `.cube`. |
| **`imnz730/LUTs` (58 of 100 files)** | `REJECT (Mixed 65pt / 1D / Non-33pt)` | Only the **42 binary-verified `33pt` (`35,937`-triplet)** files from `imnz730/LUTs` were accepted; the remaining 58 non-33pt files were filtered out. |
| **`~/Downloads/Rec.709_Conversion.cube`** | `REJECT (65pt Desktop + Wrong Input Curve)` | Binary scan of user `~/Downloads` caught `7.4 MB`, `LUT_3D_SIZE 65` (`274,625` triplets), `TITLE "luttie-Blackmagic-Film-Gen5-Rec709-Conversion"` (built for Blackmagic Pocket/URSA Film Gen 5 desktop grading, **not** iPhone Apple Log / Rec. 709). Excluded from mobile bundle! |
| **Bransford Media `.zip` (`65pt` members)** | `REJECT (65pt Desktop Members Only)` | Live ZIP unpack kept only the `33×33×33` (`35,937`-triplet) Blackmagic Camera `.cube` members and rejected the 2 `65pt` desktop members. |

---

## 8. Blackmagic Camera iOS Import & On-Set Monitoring Workflow

### Fast Local AirDrop Install (`78` Strict `33×33×33` `.cube` LUTs Ready Now)
We binary-verified and packaged **78 `33×33×33` (`35,937`-triplet) `.cube` LUTs** locally on your Mac:
- **ZIP Archive (`20.79 MB`):** `/tmp/lut_scavenger/IPHONE17_BLACKMAGIC_VERIFIED_33PT_LUTS.zip`
- **Unzipped Folder:** `/tmp/lut_scavenger/ready_to_airdrop_33pt/`
  - `00_GuVue_Official_Film_Samples_33pt/` *(**8 Official GuVue `33pt` LUTs** extracted & verified from `~/Downloads/GuVue_Film_Collection_4_Free_Sample_Looks_EN.zip`: `01_AppleLog2_iPhone17Pro` [`F11` Kodak 250D, `F12` Kodak Ektar, `F13` Kodak P800, `F14` Lomo92] + `02_Rec709_iPhone17_Air` [`F11–F14` Rec.709] + `GuVue_Film_Collection_Illustrated_Guide_EN.pdf`)*
  - `01_Apple_Log_2_iPhone17Pro/` *(**25 LUTs**: Luma Dune AL2 33pt, Rodrigo Polo AL2 + ProRes RAW 33pt, Bransford AL2 33pt, Raycal Natural/Cinematic AL2, all 8 Fuji GFX-to-Apple Log 2 simulations, and all 11 Luttie Apple Log 2 33pt looks)*
  - `02_Apple_Log_iPhone17Pro/` *(**10 LUTs**: Luma Dune AL 33pt, Bransford AL 33pt, Raycal Natural/Cinematic AL, and 6 Luttie Apple Log 33pt looks)*
  - `03_GuVue_HK_Series_Matches_Rec709_33pt/` *(**8 LUTs** mapped 1-to-1 to GuVue `HK01` Amber through `HK06` Mong Kok)*
  - `04_Rec709_Film_Stocks_iPhone17_Air_33pt/` *(**24 LUTs**: Kodak Vision3 250D/500T 2383, Ektar 100, Portra 400/800, Gold 200, Fuji ETERNA, Classic Neg, Nostalgic Neg, Natura 1600, Tri-X 400, slay Fade/Portrait, plus all 13 verified `33pt` Luttie Rec.709 LUTs from `~/Downloads`)*
  - `05_HLG_and_HDR_to_SDR_33pt/` *(**3 LUTs**: HLG & HDR-to-SDR `33pt` transforms)*

### Step-by-Step Setup in Blackmagic Camera (iOS)
1. **Transfer to iPhone:** AirDrop `/tmp/lut_scavenger/ready_to_airdrop_33pt` (or `/tmp/lut_scavenger/IPHONE17_BLACKMAGIC_VERIFIED_33PT_LUTS.zip`, then tap once in iOS **Files** to extract).
2. **Configure Color Space (`Settings → Record → Color Space`):**
   - **iPhone 17 Pro / 17 Pro Max:** Choose **Apple Log 2 - HDR** (or **Apple Log 2**) and import from `00_GuVue_Official_Film_Samples_33pt/01_AppleLog2_iPhone17Pro/` or `01_Apple_Log_2_iPhone17Pro/`. *(If shooting original Apple Log v1, use `02_Apple_Log_iPhone17Pro/`.)*
   - **iPhone 17 / 17 Air:** Choose **Rec. 709** and import from `00_GuVue_Official_Film_Samples_33pt/02_Rec709_iPhone17_Air/`, `03_GuVue_HK_Series_Matches_Rec709_33pt/`, or `04_Rec709_Film_Stocks_iPhone17_Air_33pt/`.
3. **Import & Tag (`Settings → LUTs → LUTs Manager → Import LUT`):** Select the matching `.cube` files, enable **Enable Imported LUTs** if shown, and if **Color Space Tag** appears in LUTs Manager, set it to **`Rec.709`** (describes the LUT's output display space, per GuVue's official guide p. 5).
4. **Monitor vs. Bake (`Settings → LUTs`):**
   - **Pro Grading Workflow (Recommended for 17 Pro / Pro Max):** Turn **`Display LUT` = ON** and **`Record LUT to Clip` = OFF**. Your viewfinder displays normalized film color so you nail exposure and white balance on set, while the recorded `.mov` preserves full unclipped Apple Log 2 latitude for post.
   - **Instant Social / Turnkey Delivery (Great for 17 / 17 Air or fast turnarounds):** Turn **`Display LUT` = ON** and **`Record LUT to Clip` = ON** to bake the `33pt` look directly into the recorded clip ready to post.
