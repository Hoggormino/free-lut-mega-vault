# Global LUT Dragnet — Sub-Job 2 Final Report (`opencode-extractor`)

- **Generated:** 2026-11-09T17:12 (CET) · **Agent:** opencode-extractor → **Orchestrator:** Agy (t19)
- **Mission file:** `/tmp/lut_scavenger/dragnet_subjob2_opencode.md` · **Status: ALL TASKS COMPLETE**

## Compliance Statement

No email forms, paywalls, or CAPTCHA/Cloudflare/Altcha challenges were submitted anywhere.
No `r.jina.ai`, caches, or spoofed proxies were used. All downloads were plain HTTP 200 direct
fetches. Gated sites are marked QUARANTINED and never retried:

- `filtergrade.com/free-cinematic-luts-video-editing/` → **QUARANTINED** (Cloudflare challenge, HTTP 403).
- `guvueluts.com` product pages / `.json` endpoints → **QUARANTINED (rate-limit, HTTP 429)**. Official GuVue samples already delivered via `00_GuVue_Official_Film_Samples_33pt/`.
- cinecolor.io, sebastiandylag.com, ypresets.com, absoluts-store.com → dropped from scope by Orchestrator Compliance Order.

## Task 1 — Binary-Verify & Classify (Wave 2 + Wave 3)

**Verdict rule:** `LUT_3D_SIZE 17` → 4,913 triplets PASS · `33` → 35,937 triplets PASS · `65` → 274,625 REJECT (desktop-only) · 1D LUT / no `LUT_3D_SIZE` / count mismatch → REJECT.

### Wave 2 (12 repos already on disk, `clones_wave2/`)

| Metric | Count |
|---|---|
| Repos cloned on disk | 12 |
| Repos containing `.cube` files | 9 |
| `.cube` files scanned | 114 |
| **PASS (all 33pt)** | **95** |
| REJECT (65pt / 1D / mismatch) | 19 |
| Packed into bundle | all PASS files (deduped by SHA256) |

Input spaces confirmed from README/LICENSE: `glassmeter` sRGB (CC-BY-4.0), `derby` sRGB (MIT),
`loglook`/`ffgrade` Apple Log, `cameraluts` Sony Cine4/S-Log2/S-Log3/HLG3, `lumix` LUMIX Standard
photo style, `cinema-lut`/`dust` Rec.709. Full detail: `wave2_verified_luts.md` / `.json`.

### Wave 3 (5 repos freshly shallow-cloned into `clones_wave2/`)

| Repo | Cubes | PASS | REJECT | Input space / note |
|---|---|---|---|---|
| `apyfz/lutty-ios` | 0 | — | — | iOS LUT-consumer app; no `.cube` ships (PolyForm Noncommercial) |
| `TanaTTV/vibe-engine` | 0 | — | — | Runtime LUT generator; no `.cube` ships (MIT) |
| `sohan-shingade/fujiLUT` | 0 | — | — | Runtime recipe→LUT generator; no `.cube` ships (unlicensed) |
| `vecyang1/CineSnap` | 2 | 2 | 0 | `TheOneLUT…AppleLog_Arri709_V5_33pt` → **PACKED to `02_Apple_Log_iPhone17Pro/`**; `Neutral A7s3.cube` = S-Log3 → **doc-only** |
| `JakubOchnik/Cube-LUT-Loader` | 3 | 2 | 1 | `xt3_flog_bt709.cube` F-Log 33pt → **doc-only**; `17p_cmp.cube` 17pt test fixture → **doc-only**; `alog.cube` 1D 4096 → **REJECT** |

- Wave 3 total: **5 cubes scanned, 4 PASS (1×17pt + 3×33pt), 1 REJECT, 1 packed, 3 doc-only**.
- Repo `CineSnap` and `Cube-LUT-Loader` carry no/reference-only licensing for the LUT files themselves; provenance + raw GitHub URLs recorded in `wave3_verified_luts.json`.

## Task 2 — Direct Zero-Login Archives

| Source | Result | Disposition |
|---|---|---|
| **nopixels.net** `https://nopixels.net/hlg-to-rec709/` | HTTP 200 (not gated). `nopixels_net_hlg2020_to_rec709_2.0.zip` (1,812,100 bytes, application/zip) downloaded from `…/download/2241/` | Unpacked: **`LUT_3D_SIZE 65`** → **REJECT (65pt Desktop-Only)**. NOT packed; URL documented for desktop users. |
| **Fujifilm GFX Eterna 55** `dl.fujifilm-x.com` (already on disk) | 56 cubes verified: **28 × 33Grid PASS** (35,937 triplets each, F-Log/F-Log2/F-Log2C) + **28 × 65Grid REJECT** | Camera-log inputs → **DOC-ONLY, never packed**. Official URL documented. |
| **Oleg Nikitin GDrive** (populated at 17:03) | 4 cubes verified: **3 × 33pt PASS** (`Alister_V-Look_V3_-1/-2/-3p00`, S-Log3/S-Gamut3.cine, LUTCalc v3.1.2) + **1 REJECT** (`AppleLogToRec709-v1.0.cube`, 65pt) | S-Log3 → **DOC-ONLY**. 65pt → REJECT. Nothing packed. |

## Task 3 — Bundle Expansion & Re-pack

- **All 6 pre-existing folders preserved and untouched** (`00_GuVue_Official_Film_Samples_33pt`, `01_Apple_Log_2_iPhone17Pro`, `02_Apple_Log_iPhone17Pro`, `03_GuVue_HK_Series_Matches_Rec709_33pt`, `04_Rec709_Film_Stocks_iPhone17_Air_33pt`, `05_HLG_and_HDR_to_SDR_33pt`), plus prior wave-2 folder `06_Wave2_Calibrated_Film_Emulations_Rec709_33pt` — nothing deleted.
- Newly verified files routed strictly by input space with **SHA256 dedup**:
  - `TheOneLUT_iPhone15Pro_AppleLog_Arri709_V5_33pt.cube` (Apple Log) → `02_Apple_Log_iPhone17Pro/` ✅
  - V-Log / F-Log / F-Log2 / F-Log2C / S-Log3 / unknown-input files → **kept OUT of the iPhone bundle**, documented via raw GitHub / official URLs only (see `wave3_verified_luts.md` §5–6) so iPhone users can never misapply camera-log curves.
- **Bundle sweep:** every `.cube` in `ready_to_airdrop_33pt/` re-parsed → **174 / 174 PASS (17pt or 33pt)**.
- **ZIP rebuilt:** `IPHONE17_BLACKMAGIC_VERIFIED_33PT_LUTS.zip` via `zip -r -9` (standard **Deflate**, iOS Files compatible — no LZMA/bzip2).
  - 185 members = 174 `.cube` files + 10 folder entries + 1 GuVue guide PDF.
  - In-memory verification of **every** `.cube` member: **174/174 PASS (0×17pt, 174×33pt), 0 violations**.
  - Test zips (`test_lzma*.zip`, `test_bz2.zip`, `test_z9.zip`) removed per Orchestrator note.

## Artifacts

- `IPHONE17_BLACKMAGIC_VERIFIED_33PT_LUTS.zip` (51,986,350 bytes, Deflate -9)
- `wave2_verified_luts.json` / `.md` · `wave3_verified_luts.json` / `.md`
- `dragnet_opencode_report.json` / `.md` (this report)

**Verdict: PASS. 174 verified 17pt/33pt `.cube` LUTs in the iPhone 17 Blackmagic airdrop bundle; all camera-log/65pt/1D files quarantined or documented-only per compliance rules.**
