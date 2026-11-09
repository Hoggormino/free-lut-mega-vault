# Wave 3 + Zero-Login Archives — Verified LUT Report (`wave3_verified_luts.md`)

- Generated: 2026-11-09T17:05:53+0100 · Agent: opencode-extractor → Orchestrator Agy (t19)

## 1. Summary

| Metric | Count |
|---|---|
| Wave 3 repos cloned | 5 |
| Wave 3 repos containing `.cube` files | 2 |
| `.cube` files scanned (Wave 3) | 5 |
| PASS (17pt) | 1 |
| PASS (33pt) | 3 |
| REJECT | 1 |
| Packed into `ready_to_airdrop_33pt/` | 0 |
| Document-only (camera-log / unknown input) | 3 |
| nopixels.net HLG zip | REJECT (65pt Desktop-Only) |
| Fujifilm Eterna 55 33Grid PASS (doc-only) | 28 |
| Fujifilm Eterna 55 65Grid REJECT | 28 |
| Oleg Nikitin GDrive populated | True |
| Oleg GDrive cubes verified (PASS/REJECT) | 3/1 |
| Bundle `.cube` total after pack | 174 |
| Bundle sweep | **ALL PASS (17pt or 33pt)** |

## 2. Wave 3 Per-Repo Audit

| Repo | Cubes | PASS | REJECT | License | Classification note |
|---|---|---|---|---|---|
| `CineSnap` | 2 | 2 | 0 | NO LICENSE FILE (unlicensed repo; reference LUTs are third-party) | per-file (TheOneLUT: Apple Log -> 02_ ; Neutral A7s3: S-Log3 -> doc-only) |
| `Cube-LUT-Loader` | 3 | 2 | 1 | MIT (code) + CC-BY-NC 3.0 (CubeLUT.cpp parser, Adobe spec) | per-file (test fixtures; F-Log -> doc-only, 1D REJECT, 17pt unknown-input -> verify-only) |
| `fujiLUT` | 0 | 0 | 0 | NO LICENSE FILE (unlicensed) | n/a (runtime recipe->.cube generator; no .cube files ship) |
| `lutty-ios` | 0 | 0 | 0 | PolyForm Noncommercial 1.0.0 (LICENSE.md) | n/a (iOS LUT-consumer app; no .cube files ship) |
| `vibe-engine` | 0 | 0 | 0 | MIT (LICENSE) | n/a (runtime LUT generator; no .cube files ship) |

## 3. Wave 3 Packing Map (PASS files only)

| File | Repo | Input space | Grid | Dest |
|---|---|---|---|---|
| `Neutral A7s3.cube` | CineSnap | S-Log3 (Sony A7S III neutral, Resolve-generated) | 33 | (not packed) — DOCUMENT-ONLY: camera log — iPhone users must NOT apply |
| `TheOneLUT_iPhone15Pro_AppleLog_Arri709_V5_33pt.cube` | CineSnap | Apple Log (iPhone 15 Pro) -> Arri709 | 33 | 02_Apple_Log_iPhone17Pro — skipped (byte-identical copy already in bundle) |
| `17p_cmp.cube` | Cube-LUT-Loader | unknown (Resolve-generated regression fixture) | 17 | (not packed) — DOCUMENT-ONLY: test fixture, input space undocumented — not packed |
| `xt3_flog_bt709.cube` | Cube-LUT-Loader | F-Log (Fujifilm X-T3, official FUJIFILM FLog FGamut->BT.709) | 33 | (not packed) — DOCUMENT-ONLY: camera log — iPhone users must NOT apply |

## 4. Wave 3 REJECT List

| File | Declared size | Triplets | Verdict |
|---|---|---|---|
| `Cube-LUT-Loader/src/test/resources/alog.cube` | None | 4096 | REJECT (1D LUT only, size 4096) |

## 5. Document-Only PASS files (camera-log / unknown input — NEVER on iPhone)

| File | Input space | Raw GitHub URL |
|---|---|---|
| `Neutral A7s3.cube` | S-Log3 (Sony A7S III neutral, Resolve-generated) | https://raw.githubusercontent.com/vecyang1/CineSnap/main/CineSnap/reference/Neutral%20A7s3.cube |
| `17p_cmp.cube` | unknown (Resolve-generated regression fixture) | https://raw.githubusercontent.com/JakubOchnik/Cube-LUT-Loader/main/Cube-LUT-Loader/src/test/resources/17p_cmp.cube |
| `xt3_flog_bt709.cube` | F-Log (Fujifilm X-T3, official FUJIFILM FLog FGamut->BT.709) | https://raw.githubusercontent.com/JakubOchnik/Cube-LUT-Loader/main/Cube-LUT-Loader/src/test/resources/xt3_flog_bt709.cube |

## 6. Task 2 — Zero-Login Archives

### 6.1 nopixels.net (HLG→Rec.709)

- Page `https://nopixels.net/hlg-to-rec709/` → **HTTP 200** (not gated).
- Download link `https://nopixels.net/download/2241/?tmstv=1794239028` → **HTTP 200, application/zip**, 1812100 bytes.
- Unpacked `nopixels_net_hlg2020_to_rec709.cube` → `LUT_3D_SIZE 65`, 274625 triplets → **REJECT (65pt Desktop-Only)**.
- NOT packed into the iPhone bundle (65pt desktop-only). Keep source URL for desktop users.

### 6.2 Fujifilm GFX Eterna 55 pack (official)

- `https://dl.fujifilm-x.com/lut/gfx-eterna-55-3d-lut-v100.zip` (already on disk).
- 33Grid: **28** PASS 33pt (35,937 triplets each) — all F-Log/F-Log2/F-Log2C camera-log inputs → **DOC-ONLY, never packed** (iPhone users must NOT apply).
- 65Grid: **28** REJECT (65pt Desktop-Only).

### 6.3 Oleg Nikitin GDrive

- `downloads/oleg_nikitin_gdrive/` populated: **True** (4 `.cube` files).

| File | Input space | Grid | Verdict | Disposition |
|---|---|---|---|---|
| `Alister_V-Look_V3_-1p00.cube` | unknown | 33 | PASS (33pt) | unclassified |
| `Alister_V-Look_V3_-2p00.cube` | unknown | 33 | PASS (33pt) | unclassified |
| `Alister_V-Look_V3_-3p00.cube` | unknown | 33 | PASS (33pt) | unclassified |
| `AppleLogToRec709-v1.0.cube` | Apple Log | 65 | REJECT (65pt Desktop-Only) | 65pt desktop-only — REJECT from iPhone bundle |

Full data: `wave3_verified_luts.json`
