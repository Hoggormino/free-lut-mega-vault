# Wave 2 Mega-Hunt — Verified LUT Report (`wave2_verified_luts.md`)

- Generated: 2026-11-09T17:01:17+0100 · Agent: opencode-extractor (t1h) → Orchestrator Agy (t19)
- Scope: Task 1 (12 fresh GitHub clones, binary scan) + Task 3 (pack 17pt/33pt, re-zip). Task 2 portals NOT executed per Orchestrator Compliance Order (403/anti-bot sites quarantined).

## 1. Summary

| Metric | Count |
|---|---|
| Repos cloned | 12 |
| Repos containing `.cube` files | 9 |
| `.cube` files scanned | 114 |
| PASS (17pt) | 0 |
| PASS (33pt) | 95 |
| REJECT | 19 |
| Packed into `ready_to_airdrop_33pt/` | 0 |
| Bundle `.cube` total after pack | 173 |
| Bundle sweep | **ALL PASS (17pt or 33pt)** |

## 2. Per-Repo Audit

| Repo | Cubes | PASS | REJECT | License | Classification note |
|---|---|---|---|---|---|
| `cameraluts` | 23 | 23 | 0 | LICENSE (MIT License) | camera-log (Sony) |
| `cinema-lut` | 7 | 7 | 0 | NO LICENSE FILE (unlicensed) | Rec.709 / sRGB |
| `derby` | 7 | 7 | 0 | LICENSE (MIT License) | sRGB (display-referred) |
| `dust` | 1 | 1 | 0 | NO LICENSE FILE (unlicensed) | Rec.709 / sRGB |
| `ffgrade` | 8 | 0 | 8 | NO LICENSE FILE (unlicensed) | Apple Log |
| `filmic` | 11 | 0 | 11 | NO LICENSE FILE (unlicensed; upstream filmic-blender GPL-2.0) | Filmic Base Log (Resolve pipeline utility) |
| `fuji-recipe` | 0 | 0 | 0 | LICENSE (MIT License) | n/a (no .cube files) |
| `glassmeter` | 30 | 30 | 0 | LICENSE (Attribution 4.0 International) | sRGB (display-referred) |
| `loglook` | 5 | 5 | 0 | MIT (per README) | Apple Log |
| `lumix` | 22 | 22 | 0 | LICENSE (MIT License) | sRGB (LUMIX Standard photo style base) |
| `mfilm` | 0 | 0 | 0 | LICENSE (GNU GENERAL PUBLIC LICENSE) | n/a (no .cube files) |
| `moderates` | 0 | 0 | 0 | LICENSE.md (Copyright 2026 Moder4te) | n/a (no .cube files) |

## 3. Packing Map (PASS files only)

| File | Repo | Input space | Grid | Dest folder |
|---|---|---|---|---|
| `Sony_A7III_Cine4_ProGamut_To_Rec709_Filmic.cube` | cameraluts | Cine4 (Pro Gamut) | 33 | 06_Wave2_Calibrated_Film_Emulations_Rec709_33pt |
| `Sony_A7III_Cine4_ProGamut_To_Rec709_Standard.cube` | cameraluts | Cine4 (Pro Gamut) | 33 | 06_Wave2_Calibrated_Film_Emulations_Rec709_33pt |
| `Sony_A7III_HLG3_BT2020_To_Rec709_Filmic.cube` | cameraluts | HLG3 (BT.2020) | 33 | 05_HLG_and_HDR_to_SDR_33pt |
| `Sony_A7III_HLG3_BT2020_To_Rec709_Standard.cube` | cameraluts | HLG3 (BT.2020) | 33 | 05_HLG_and_HDR_to_SDR_33pt |
| `Sony_A7III_SLog2_SGamut3Cine_To_Rec709_Filmic.cube` | cameraluts | S-Log2 | 33 | 06_Wave2_Calibrated_Film_Emulations_Rec709_33pt |
| `Sony_A7III_SLog2_SGamut3Cine_To_Rec709_Standard.cube` | cameraluts | S-Log2 | 33 | 06_Wave2_Calibrated_Film_Emulations_Rec709_33pt |
| `Sony_A7III_SLog2_SGamut_To_Rec709_Filmic.cube` | cameraluts | S-Log2 | 33 | 06_Wave2_Calibrated_Film_Emulations_Rec709_33pt |
| `Sony_A7III_SLog2_SGamut_To_Rec709_Standard.cube` | cameraluts | S-Log2 | 33 | 06_Wave2_Calibrated_Film_Emulations_Rec709_33pt |
| `Sony_A7III_SLog3_SGamut3Cine_To_Rec709_Filmic.cube` | cameraluts | S-Log3 | 33 | 06_Wave2_Calibrated_Film_Emulations_Rec709_33pt |
| `Sony_A7III_SLog3_SGamut3Cine_To_Rec709_Standard.cube` | cameraluts | S-Log3 | 33 | 06_Wave2_Calibrated_Film_Emulations_Rec709_33pt |
| `Sony_FX_A7V_HLG3_BT2020_Standard.cube` | cameraluts | HLG3 (BT.2020) | 33 | 05_HLG_and_HDR_to_SDR_33pt |
| `Sony_FX_A7V_SLog3_SGamut3Cine_709_800.cube` | cameraluts | S-Log3 | 33 | 06_Wave2_Calibrated_Film_Emulations_Rec709_33pt |
| `Sony_FX_A7V_SLog3_SGamut3Cine_LC709TypeA.cube` | cameraluts | S-Log3 | 33 | 06_Wave2_Calibrated_Film_Emulations_Rec709_33pt |
| `Sony_FX_A7V_SLog3_SGamut3Cine_Standard.cube` | cameraluts | S-Log3 | 33 | 06_Wave2_Calibrated_Film_Emulations_Rec709_33pt |
| `Sony_FX_A7V_SLog3_SGamut3Cine_s709.cube` | cameraluts | S-Log3 | 33 | 06_Wave2_Calibrated_Film_Emulations_Rec709_33pt |
| `Sony_A7IV_Cine4_ProGamut_To_Rec709_Filmic.cube` | cameraluts | Cine4 (Pro Gamut) | 33 | 06_Wave2_Calibrated_Film_Emulations_Rec709_33pt |
| `Sony_A7IV_Cine4_ProGamut_To_Rec709_Standard.cube` | cameraluts | Cine4 (Pro Gamut) | 33 | 06_Wave2_Calibrated_Film_Emulations_Rec709_33pt |
| `Sony_A7IV_HLG3_BT2020_To_Rec709_Filmic.cube` | cameraluts | HLG3 (BT.2020) | 33 | 05_HLG_and_HDR_to_SDR_33pt |
| `Sony_A7IV_HLG3_BT2020_To_Rec709_Standard.cube` | cameraluts | HLG3 (BT.2020) | 33 | 05_HLG_and_HDR_to_SDR_33pt |
| `Sony_A7IV_SLog3_SGamut3Cine_To_Rec709_Filmic.cube` | cameraluts | S-Log3 | 33 | 06_Wave2_Calibrated_Film_Emulations_Rec709_33pt |
| `Sony_A7IV_SLog3_SGamut3Cine_To_Rec709_Standard.cube` | cameraluts | S-Log3 | 33 | 06_Wave2_Calibrated_Film_Emulations_Rec709_33pt |
| `Sony_A7IV_SLog3_SGamut3_To_Rec709_Filmic.cube` | cameraluts | S-Log3 | 33 | 06_Wave2_Calibrated_Film_Emulations_Rec709_33pt |
| `Sony_A7IV_SLog3_SGamut3_To_Rec709_Standard.cube` | cameraluts | S-Log3 | 33 | 06_Wave2_Calibrated_Film_Emulations_Rec709_33pt |
| `The Cinema +.cube` | cinema-lut | Rec.709 / sRGB | 33 | 04_Rec709_Film_Stocks_iPhone17_Air_33pt |
| `The Cinema Blue.cube` | cinema-lut | Rec.709 / sRGB | 33 | 04_Rec709_Film_Stocks_iPhone17_Air_33pt |
| `The Cinema Cool.cube` | cinema-lut | Rec.709 / sRGB | 33 | 04_Rec709_Film_Stocks_iPhone17_Air_33pt |
| `The Cinema Green.cube` | cinema-lut | Rec.709 / sRGB | 33 | 04_Rec709_Film_Stocks_iPhone17_Air_33pt |
| `The Cinema Noir.cube` | cinema-lut | Rec.709 / sRGB | 33 | 04_Rec709_Film_Stocks_iPhone17_Air_33pt |
| `The Cinema Purple.cube` | cinema-lut | Rec.709 / sRGB | 33 | 04_Rec709_Film_Stocks_iPhone17_Air_33pt |
| `The Cinema.cube` | cinema-lut | Rec.709 / sRGB | 33 | 04_Rec709_Film_Stocks_iPhone17_Air_33pt |
| `BLUSH.cube` | derby | sRGB (display-referred) | 33 | 06_Wave2_Calibrated_Film_Emulations_Rec709_33pt |
| `CHILLY.cube` | derby | sRGB (display-referred) | 33 | 06_Wave2_Calibrated_Film_Emulations_Rec709_33pt |
| `DREAMY.cube` | derby | sRGB (display-referred) | 33 | 06_Wave2_Calibrated_Film_Emulations_Rec709_33pt |
| `MOONLIT.cube` | derby | sRGB (display-referred) | 33 | 06_Wave2_Calibrated_Film_Emulations_Rec709_33pt |
| `SUNSHINE.cube` | derby | sRGB (display-referred) | 33 | 06_Wave2_Calibrated_Film_Emulations_Rec709_33pt |
| `TOASTY.cube` | derby | sRGB (display-referred) | 33 | 06_Wave2_Calibrated_Film_Emulations_Rec709_33pt |
| `ZESTY.cube` | derby | sRGB (display-referred) | 33 | 06_Wave2_Calibrated_Film_Emulations_Rec709_33pt |
| `The Dust.cube` | dust | Rec.709 / sRGB | 33 | 04_Rec709_Film_Stocks_iPhone17_Air_33pt |
| `cinestill-400d.cube` | glassmeter | sRGB (display-referred) | 33 | 06_Wave2_Calibrated_Film_Emulations_Rec709_33pt |
| `cinestill-50d.cube` | glassmeter | sRGB (display-referred) | 33 | 06_Wave2_Calibrated_Film_Emulations_Rec709_33pt |
| `cinestill-800t.cube` | glassmeter | sRGB (display-referred) | 33 | 06_Wave2_Calibrated_Film_Emulations_Rec709_33pt |
| `fuji-acros-100-ii.cube` | glassmeter | sRGB (display-referred) | 33 | 06_Wave2_Calibrated_Film_Emulations_Rec709_33pt |
| `fuji-industrial-100.cube` | glassmeter | sRGB (display-referred) | 33 | 06_Wave2_Calibrated_Film_Emulations_Rec709_33pt |
| `fuji-pro-400h.cube` | glassmeter | sRGB (display-referred) | 33 | 06_Wave2_Calibrated_Film_Emulations_Rec709_33pt |
| `fuji-provia-100f.cube` | glassmeter | sRGB (display-referred) | 33 | 06_Wave2_Calibrated_Film_Emulations_Rec709_33pt |
| `fuji-superia-xtra-400.cube` | glassmeter | sRGB (display-referred) | 33 | 06_Wave2_Calibrated_Film_Emulations_Rec709_33pt |
| `fuji-velvia-100.cube` | glassmeter | sRGB (display-referred) | 33 | 06_Wave2_Calibrated_Film_Emulations_Rec709_33pt |
| `fuji-velvia-50.cube` | glassmeter | sRGB (display-referred) | 33 | 06_Wave2_Calibrated_Film_Emulations_Rec709_33pt |
| `ilford-delta-100-v2.cube` | glassmeter | sRGB (display-referred) | 33 | 06_Wave2_Calibrated_Film_Emulations_Rec709_33pt |
| `ilford-delta-3200-v2.cube` | glassmeter | sRGB (display-referred) | 33 | 06_Wave2_Calibrated_Film_Emulations_Rec709_33pt |
| `ilford-delta-400.cube` | glassmeter | sRGB (display-referred) | 33 | 06_Wave2_Calibrated_Film_Emulations_Rec709_33pt |
| `ilford-fp4-125-v2.cube` | glassmeter | sRGB (display-referred) | 33 | 06_Wave2_Calibrated_Film_Emulations_Rec709_33pt |
| `ilford-hp5-400-v2.cube` | glassmeter | sRGB (display-referred) | 33 | 06_Wave2_Calibrated_Film_Emulations_Rec709_33pt |
| `ilford-panf-50.cube` | glassmeter | sRGB (display-referred) | 33 | 06_Wave2_Calibrated_Film_Emulations_Rec709_33pt |
| `ilford-xp2-super-400.cube` | glassmeter | sRGB (display-referred) | 33 | 06_Wave2_Calibrated_Film_Emulations_Rec709_33pt |
| `kodak-colorplus-200.cube` | glassmeter | sRGB (display-referred) | 33 | 06_Wave2_Calibrated_Film_Emulations_Rec709_33pt |
| `kodak-double-x-v2.cube` | glassmeter | sRGB (display-referred) | 33 | 06_Wave2_Calibrated_Film_Emulations_Rec709_33pt |
| `kodak-ektachrome-e100.cube` | glassmeter | sRGB (display-referred) | 33 | 06_Wave2_Calibrated_Film_Emulations_Rec709_33pt |
| `kodak-ektar-100.cube` | glassmeter | sRGB (display-referred) | 33 | 06_Wave2_Calibrated_Film_Emulations_Rec709_33pt |
| `kodak-gold-200.cube` | glassmeter | sRGB (display-referred) | 33 | 06_Wave2_Calibrated_Film_Emulations_Rec709_33pt |
| `kodak-portra-160.cube` | glassmeter | sRGB (display-referred) | 33 | 06_Wave2_Calibrated_Film_Emulations_Rec709_33pt |
| `kodak-portra-400.cube` | glassmeter | sRGB (display-referred) | 33 | 06_Wave2_Calibrated_Film_Emulations_Rec709_33pt |
| `kodak-portra-800.cube` | glassmeter | sRGB (display-referred) | 33 | 06_Wave2_Calibrated_Film_Emulations_Rec709_33pt |
| `kodak-tmax-100-v2.cube` | glassmeter | sRGB (display-referred) | 33 | 06_Wave2_Calibrated_Film_Emulations_Rec709_33pt |
| `kodak-tmax-400-v2.cube` | glassmeter | sRGB (display-referred) | 33 | 06_Wave2_Calibrated_Film_Emulations_Rec709_33pt |
| `kodak-tmax-p3200.cube` | glassmeter | sRGB (display-referred) | 33 | 06_Wave2_Calibrated_Film_Emulations_Rec709_33pt |
| `kodak-trix-400-v2.cube` | glassmeter | sRGB (display-referred) | 33 | 06_Wave2_Calibrated_Film_Emulations_Rec709_33pt |
| `kodak-ultramax-400.cube` | glassmeter | sRGB (display-referred) | 33 | 06_Wave2_Calibrated_Film_Emulations_Rec709_33pt |
| `Clean709.cube` | loglook | Apple Log | 33 | 02_Apple_Log_iPhone17Pro |
| `FadedVintage.cube` | loglook | Apple Log | 33 | 02_Apple_Log_iPhone17Pro |
| `MonoBW.cube` | loglook | Apple Log | 33 | 02_Apple_Log_iPhone17Pro |
| `TealOrange.cube` | loglook | Apple Log | 33 | 02_Apple_Log_iPhone17Pro |
| `WarmFilm.cube` | loglook | Apple Log | 33 | 02_Apple_Log_iPhone17Pro |
| `01Glaze.cube` | lumix | sRGB (LUMIX Standard photo style base) | 33 | 04_Rec709_Film_Stocks_iPhone17_Air_33pt |
| `02Burin.cube` | lumix | sRGB (LUMIX Standard photo style base) | 33 | 04_Rec709_Film_Stocks_iPhone17_Air_33pt |
| `03Gilt.cube` | lumix | sRGB (LUMIX Standard photo style base) | 33 | 04_Rec709_Film_Stocks_iPhone17_Air_33pt |
| `04Viride.cube` | lumix | sRGB (LUMIX Standard photo style base) | 33 | 04_Rec709_Film_Stocks_iPhone17_Air_33pt |
| `05Clear.cube` | lumix | sRGB (LUMIX Standard photo style base) | 33 | 04_Rec709_Film_Stocks_iPhone17_Air_33pt |
| `06Almond.cube` | lumix | sRGB (LUMIX Standard photo style base) | 33 | 04_Rec709_Film_Stocks_iPhone17_Air_33pt |
| `07Voile.cube` | lumix | sRGB (LUMIX Standard photo style base) | 33 | 04_Rec709_Film_Stocks_iPhone17_Air_33pt |
| `08Arcade.cube` | lumix | sRGB (LUMIX Standard photo style base) | 33 | 04_Rec709_Film_Stocks_iPhone17_Air_33pt |
| `09Tinsel.cube` | lumix | sRGB (LUMIX Standard photo style base) | 33 | 04_Rec709_Film_Stocks_iPhone17_Air_33pt |
| `10Splice.cube` | lumix | sRGB (LUMIX Standard photo style base) | 33 | 04_Rec709_Film_Stocks_iPhone17_Air_33pt |
| `11Sodium.cube` | lumix | sRGB (LUMIX Standard photo style base) | 33 | 04_Rec709_Film_Stocks_iPhone17_Air_33pt |
| `12Argent.cube` | lumix | sRGB (LUMIX Standard photo style base) | 33 | 04_Rec709_Film_Stocks_iPhone17_Air_33pt |
| `Canopy.cube` | lumix | sRGB (LUMIX Standard photo style base) | 33 | 04_Rec709_Film_Stocks_iPhone17_Air_33pt |
| `DuskTide.cube` | lumix | sRGB (LUMIX Standard photo style base) | 33 | 04_Rec709_Film_Stocks_iPhone17_Air_33pt |
| `Fieldnote.cube` | lumix | sRGB (LUMIX Standard photo style base) | 33 | 04_Rec709_Film_Stocks_iPhone17_Air_33pt |
| `Heartland.cube` | lumix | sRGB (LUMIX Standard photo style base) | 33 | 04_Rec709_Film_Stocks_iPhone17_Air_33pt |
| `Lowsun.cube` | lumix | sRGB (LUMIX Standard photo style base) | 33 | 04_Rec709_Film_Stocks_iPhone17_Air_33pt |
| `Matinee.cube` | lumix | sRGB (LUMIX Standard photo style base) | 33 | 04_Rec709_Film_Stocks_iPhone17_Air_33pt |
| `Meridian.cube` | lumix | sRGB (LUMIX Standard photo style base) | 33 | 04_Rec709_Film_Stocks_iPhone17_Air_33pt |
| `NightMarket.cube` | lumix | sRGB (LUMIX Standard photo style base) | 33 | 04_Rec709_Film_Stocks_iPhone17_Air_33pt |
| `Postcard.cube` | lumix | sRGB (LUMIX Standard photo style base) | 33 | 04_Rec709_Film_Stocks_iPhone17_Air_33pt |
| `Skylight.cube` | lumix | sRGB (LUMIX Standard photo style base) | 33 | 04_Rec709_Film_Stocks_iPhone17_Air_33pt |

## 4. REJECT List

| File | Declared size | Triplets | Verdict |
|---|---|---|---|
| `ffgrade/luts/tone/shipped.cube` | None | 4096 | REJECT (1D LUT only, size 4096) |
| `ffgrade/luts/looks/kodak_portra_400_nc.cube` | 13 | 2197 | REJECT (13pt Non-Standard) |
| `ffgrade/luts/looks/negative_color_kodak_portra_160_vc.cube` | 13 | 2197 | REJECT (13pt Non-Standard) |
| `ffgrade/luts/looks/negative_new_kodak_portra_400.cube` | 13 | 2197 | REJECT (13pt Non-Standard) |
| `ffgrade/luts/looks/negative_new_kodak_portra_400_++.cube` | 13 | 2197 | REJECT (13pt Non-Standard) |
| `ffgrade/luts/looks/negative_new_kodak_portra_400_+.cube` | 13 | 2197 | REJECT (13pt Non-Standard) |
| `ffgrade/luts/looks/negative_new_kodak_portra_800_hc.cube` | 13 | 2197 | REJECT (13pt Non-Standard) |
| `ffgrade/luts/looks/negative_old_kodak_portra_400_uc.cube` | 13 | 2197 | REJECT (13pt Non-Standard) |
| `filmic/Filmic Resolve - Base Contrast.cube` | None | 4096 | REJECT (1D LUT only, size 4096) |
| `filmic/Filmic Resolve - Base Encoding to Scene Linear.cube` | None | 4096 | REJECT (1D LUT only, size 4096) |
| `filmic/Filmic Resolve - Filmic Shaper to Chromatic Attenuated.cube` | 65 | 274625 | REJECT (65pt Desktop-Only) |
| `filmic/Filmic Resolve - High Contrast.cube` | None | 4096 | REJECT (1D LUT only, size 4096) |
| `filmic/Filmic Resolve - Low Contrast.cube` | None | 4096 | REJECT (1D LUT only, size 4096) |
| `filmic/Filmic Resolve - Medium High Contrast.cube` | None | 4096 | REJECT (1D LUT only, size 4096) |
| `filmic/Filmic Resolve - Medium Low Contrast.cube` | None | 4096 | REJECT (1D LUT only, size 4096) |
| `filmic/Filmic Resolve - Open Domain to Filmic Shaper.cube` | None | 65536 | REJECT (1D LUT only, size 65536) |
| `filmic/Filmic Resolve - Scene Linear to Base Encoding.cube` | None | 65536 | REJECT (1D LUT only, size 65536) |
| `filmic/Filmic Resolve - Very High Contrast.cube` | None | 4096 | REJECT (1D LUT only, size 4096) |
| `filmic/Filmic Resolve - Very Low Contrast.cube` | None | 4096 | REJECT (1D LUT only, size 4096) |

## 5. Quarantine Log (Compliance Order)

- `filtergrade.com/free-cinematic-luts-video-editing/` → **QUARANTINED** (Cloudflare challenge, HTTP 403). Not touched again.
- `guvueluts.com` product pages / `.json` endpoints → **QUARANTINED (rate-limit)** (HTTP 429 on repeated requests). Official GuVue samples already delivered via `00_GuVue_Official_Film_Samples_33pt/`.
- Task 2 portals (cinecolor.io, sebastiandylag.com, ypresets.com, absoluts-store.com, nopixels.net) → **not executed** (dropped from scope by Orchestrator Compliance Order).

## 6. Re-packed ZIP

- `IPHONE17_BLACKMAGIC_VERIFIED_33PT_LUTS.zip` re-built from `ready_to_airdrop_33pt/` (50.3 MB, 173 `.cube` members): `unzip -t` OK, strict sweep **0 violations** — 100% of members are 17pt or 33pt PASS.

Full data: `wave2_verified_luts.json`
