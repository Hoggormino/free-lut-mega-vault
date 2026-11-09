# opencode-extractor — Verified LUT Report (`opencode_verified_luts.md`)

- Generated: 2026-11-09T16:45:57+0100 · Agent: opencode-extractor (Sub-Job 2 / Task 4)
- Network state at verification time: **ONLINE**

## 1. Summary

| Metric | Count |
|---|---|
| Local `.cube` files scanned (clones + downloads) | 300 |
| **PASS (17pt)** | **0** |
| **PASS (33pt)** | **128** |
| PASS total | 128 |
| REJECT total | 172 |
| ├ REJECT 65pt (desktop-only) | 104 |
| ├ REJECT 64pt (non-standard) | 0 |
| ├ REJECT 25pt (non-standard, incl. CineStill IWLTBAP) | 1 |
| └ REJECT other (1D / mismatch / non-standard) | 67 |
| Zero-login portal candidates tracked | 37 |
| ├ Pending (offline at verify time) | 0 |

Rules applied: `LUT_3D_SIZE` 17 → 4,913 triplets PASS · 33 → 35,937 triplets PASS · 65 → 274,625 triplets REJECT (Desktop-Only) · 64/25/non-standard/1D/mismatch → REJECT.

## 2. Zero-Login Portal Candidates (scraped HTTP 200 by orchestrator pre-outage)

Live downloads were attempted where the network probe succeeded; otherwise entries are PENDING.

| # | Candidate | Bucket | Direct URL | Status | Local verdict |
|---|---|---|---|---|---|
| 1 | Luma Dune — Apple Log 2 to Rec.709 v1.0 (33pt) | Apple Log 2 / Apple Wide Gamut | https://res.lumadune.com/static-lut-files/AppleLog2ToRec709-v1.0-33.cube | 200 ✓ | PASS (33pt) |
| 2 | Luma Dune — Apple Log to Rec.709 v1.0 (33pt) | Apple Log / Rec. 2020 | https://res.lumadune.com/static-lut-files/AppleLogToRec709-v1.0-33.cube | 200 ✓ | PASS (33pt) |
| 3 | Rodrigo Polo — Apple Log 2 to Rec.709 (33pt Monitor Grid) | Apple Log 2 / Apple Wide Gamut | https://rodrigopolo.com/wp-content/uploads/2025/11/AppleLog2_to_Rec709_33_Grid.cube | 200 ✓ | PASS (33pt) |
| 4 | Rodrigo Polo — ProRes RAW Apple Log 2 to Rec.709 (33pt Grid) | Apple Log 2 / Apple Wide Gamut | https://rodrigopolo.com/wp-content/uploads/2025/11/OtherProResRAW_AppleLog2_to_Rec709_33_Grid.cube | 200 ✓ | PASS (33pt) |
| 5 | Luttie — Cyberpunk Neon (Apple Log 2) | Apple Log 2 / Apple Wide Gamut (GuVue HK Neon Alternative) | https://luttie.app/api/lut-assets/405?download=Cyberpunk%20Neon%20(Apple%20Log%202).cube | 200 ✓ | PASS (33pt) |
| 6 | Luttie — Moody Cinematic Dark Teal (Apple Log 2) | Apple Log 2 / Apple Wide Gamut (GuVue HK Harbour/Cyan Alternative) | https://luttie.app/api/lut-assets/409?download=Moody%20Cinematic%20(Apple%20Log%202).cube | 200 ✓ | PASS (33pt) |
| 7 | Luttie — Faded Kodak Film (Apple Log 2) | Apple Log 2 / Apple Wide Gamut (GuVue Film Alternative) | https://luttie.app/api/lut-assets/406?download=Faded%20Kodak%20(Apple%20Log%202).cube | 200 ✓ | PASS (33pt) |
| 8 | Luttie — Cool Blue Steel (Apple Log 2) | Apple Log 2 / Apple Wide Gamut (GuVue HK Harbour Blue Alternative) | https://luttie.app/api/lut-assets/404?download=Cool%20Blue%20Steel%20(Apple%20Log%202).cube | 200 ✓ | PASS (33pt) |
| 9 | Luttie — Warm Golden Hour (Apple Log 2) | Apple Log 2 / Apple Wide Gamut (GuVue HK Amber Alternative) | https://luttie.app/api/lut-assets/411?download=Warm%20Golden%20Hour%20(Apple%20Log%202).cube | 200 ✓ | PASS (33pt) |
| 10 | Luttie — Cinematic Teal & Orange (Apple Log 2) | Apple Log 2 / Apple Wide Gamut | https://luttie.app/api/lut-assets/402?download=Cinematic%20Teal%20%26%20Orange%20(Apple%20Log%202).cube | 200 ✓ | PASS (33pt) |
| 11 | Luttie — Matte Fade (Apple Log 2) | Apple Log 2 / Apple Wide Gamut | https://luttie.app/api/lut-assets/408?download=Matte%20Fade%20(Apple%20Log%202).cube | 200 ✓ | PASS (33pt) |
| 12 | Luttie — Soft Portrait (Apple Log 2) | Apple Log 2 / Apple Wide Gamut | https://luttie.app/api/lut-assets/410?download=Soft%20Portrait%20(Apple%20Log%202).cube | 200 ✓ | PASS (33pt) |
| 13 | Luttie — High Contrast (Apple Log 2) | Apple Log 2 / Apple Wide Gamut | https://luttie.app/api/lut-assets/407?download=High%20Contrast%20(Apple%20Log%202).cube | 200 ✓ | PASS (33pt) |
| 14 | Luttie — Bright & Airy (Apple Log 2) | Apple Log 2 / Apple Wide Gamut | https://luttie.app/api/lut-assets/401?download=Bright%20%26%20Airy%20(Apple%20Log%202).cube | 200 ✓ | PASS (33pt) |
| 15 | Luttie — Classic B&W (Apple Log 2) | Apple Log 2 / Apple Wide Gamut | https://luttie.app/api/lut-assets/403?download=Classic%20B%26W%20(Apple%20Log%202).cube | 200 ✓ | PASS (33pt) |
| 16 | Luttie — Cyberpunk Neon (Apple Log) | Apple Log / Rec. 2020 | https://luttie.app/api/lut-assets/394?download=Cyberpunk%20Neon%20(Apple%20Log).cube | 200 ✓ | PASS (33pt) |
| 17 | Luttie — Moody Cinematic (Apple Log) | Apple Log / Rec. 2020 | https://luttie.app/api/lut-assets/398?download=Moody%20Cinematic%20(Apple%20Log).cube | 200 ✓ | PASS (33pt) |
| 18 | Luttie — Faded Kodak (Apple Log) | Apple Log / Rec. 2020 | https://luttie.app/api/lut-assets/395?download=Faded%20Kodak%20(Apple%20Log).cube | 200 ✓ | PASS (33pt) |
| 19 | Luttie — Cool Blue Steel (Apple Log) | Apple Log / Rec. 2020 | https://luttie.app/api/lut-assets/393?download=Cool%20Blue%20Steel%20(Apple%20Log).cube | 200 ✓ | PASS (33pt) |
| 20 | Luttie — Warm Golden Hour (Apple Log) | Apple Log / Rec. 2020 | https://luttie.app/api/lut-assets/400?download=Warm%20Golden%20Hour%20(Apple%20Log).cube | 200 ✓ | PASS (33pt) |
| 21 | Luttie — Cinematic Teal & Orange (Apple Log) | Apple Log / Rec. 2020 | https://luttie.app/api/lut-assets/391?download=Cinematic%20Teal%20%26%20Orange%20(Apple%20Log).cube | 200 ✓ | PASS (33pt) |
| 22 | Luttie — Kodak 2383 Print (Rec.709) | Rec. 709 SDR (iPhone 17 & 17 Air + Post-709) | https://luttie.app/api/lut-assets/721?download=Kodak%202383%20Print.cube | 200 ✓ | PASS (33pt) |
| 23 | Luttie — Kodak Portra 400 (Rec.709) | Rec. 709 SDR (iPhone 17 & 17 Air + Post-709) | https://luttie.app/api/lut-assets/720?download=Portra%20400.cube | 200 ✓ | PASS (33pt) |
| 24 | Luttie — Cyberpunk Neon (Rec.709) | Rec. 709 SDR (GuVue HK Neon Alternative) | https://luttie.app/api/lut-assets/142?download=Cyberpunk%20Neon%20LUT%20%E2%80%94%20Free%20Cyan%20%26%20Magenta%20Night%20Look.cube | 200 ✓ | PASS (33pt) |
| 25 | Luttie — Moody Cinematic Dark Teal (Rec.709) | Rec. 709 SDR (GuVue HK Harbour/Cyan Alternative) | https://luttie.app/api/lut-assets/140?download=Moody%20Cinematic%20LUT%20%E2%80%94%20Free%20Dark%20Teal%20Film%20Look.cube | 200 ✓ | PASS (33pt) |
| 26 | Luttie — Faded Kodak (Rec.709) | Rec. 709 SDR | https://luttie.app/api/lut-assets/6?download=Faded%20Kodak%20%E2%80%94%20Free%20Film%20Emulation%20LUT.cube | 200 ✓ | PASS (33pt) |
| 27 | slay — Amber (Rec.709, CC BY 4.0) | Rec. 709 SDR (GuVue HK Amber Alternative) | https://raw.githubusercontent.com/slaycamera/luts/main/luts/slay-01-amber.cube | 200 ✓ | PASS (33pt) |
| 28 | slay — Fade (Rec.709, CC BY 4.0) | Rec. 709 SDR | https://raw.githubusercontent.com/slaycamera/luts/main/luts/slay-02-fade.cube | 200 ✓ | PASS (33pt) |
| 29 | slay — Neon Night-City (Rec.709, CC BY 4.0) | Rec. 709 SDR (GuVue HK Mong Kok / Avenue Star Alternative) | https://raw.githubusercontent.com/slaycamera/luts/main/luts/slay-03-neon.cube | 200 ✓ | PASS (33pt) |
| 30 | slay — Film Teal/Warm (Rec.709, CC BY 4.0) | Rec. 709 SDR (GuVue HK Island Cyan / Pale Green Alternative) | https://raw.githubusercontent.com/slaycamera/luts/main/luts/slay-04-film.cube | 200 ✓ | PASS (33pt) |
| 31 | slay — Portrait Soft Roll-Off (Rec.709, CC BY 4.0) | Rec. 709 SDR | https://raw.githubusercontent.com/slaycamera/luts/main/luts/slay-05-portrait.cube | 200 ✓ | PASS (33pt) |
| 32 | Luma Dune — Apple Log 2 to Rec.709 v1.0 (65pt Desktop Control) | REJECT CONTROL (65pt) | https://res.lumadune.com/static-lut-files/AppleLog2ToRec709-v1.0-65.cube | 200 ✓ | REJECT (65pt Desktop-Only) |
| 33 | Luma Dune — Apple Log to Rec.709 v1.0 (65pt Desktop Control) | REJECT CONTROL (65pt) | https://res.lumadune.com/static-lut-files/AppleLogToRec709-v1.0-65.cube | 200 ✓ | REJECT (65pt Desktop-Only) |
| 34 | Rodrigo Polo — Apple Log 2 to Rec.709 (65pt Desktop Control) | REJECT CONTROL (65pt) | https://rodrigopolo.com/wp-content/uploads/2025/11/AppleLog2_to_Rec709_65_Grid.cube | 200 ✓ | REJECT (65pt Desktop-Only) |
| 35 | Bransford Media — Apple Log 2 Free Look Pack (.zip) | Apple Log 2 / Apple Wide Gamut | https://bransfordmedia.com/luts/free-look/apple-log-2.zip | 200 ✓ | PASS ZIP (1/2 members mobile 17/33pt) |
|  | └ zip member: BMSoftDocAppleLog2.cube | | | | PASS (33pt) |
|  | └ zip member: BMSoftDocAppleLog265.cube | | | | REJECT (65pt Desktop-Only) |
| 36 | Bransford Media — Apple Log Free Look Pack (.zip) | Apple Log / Rec. 2020 | https://bransfordmedia.com/luts/free-look/apple-log.zip | 200 ✓ | PASS ZIP (1/2 members mobile 17/33pt) |
|  | └ zip member: BMSoftDocAppleLog.cube | | | | PASS (33pt) |
|  | └ zip member: BMSoftDocAppleLog65.cube | | | | REJECT (65pt Desktop-Only) |
| 37 | Fujifilm Official — X-M5 F-Log/F-Log2 3D-LUT pack (.zip) | Official Reference LUTs | https://dl.fujifilm-x.com/lut/x-m5-3d-lut-v100.zip | 200 ✓ | PASS ZIP (8/8 members mobile 17/33pt) |
|  | └ zip member: x-m5-3d-lut-v100\F-Log\XM5_FLog_FGamut_to_ETERNA-BB_BT.709_33grid_V.1.00.cube | | | | PASS (33pt) |
|  | └ zip member: x-m5-3d-lut-v100\F-Log\XM5_FLog_FGamut_to_ETERNA_BT.709_33grid_V.1.00.cube | | | | PASS (33pt) |
|  | └ zip member: x-m5-3d-lut-v100\F-Log\XM5_FLog_FGamut_to_FLog_BT.709_33grid_V.1.00.cube | | | | PASS (33pt) |
|  | └ zip member: x-m5-3d-lut-v100\F-Log\XM5_FLog_FGamut_to_WDR_BT.709_33grid_V.1.00.cube | | | | PASS (33pt) |
|  | └ zip member: x-m5-3d-lut-v100\F-Log2\XM5_FLog2_FGamut_to_ETERNA-BB_BT.709_33grid_V.1.00.cube | | | | PASS (33pt) |
|  | └ zip member: x-m5-3d-lut-v100\F-Log2\XM5_FLog2_FGamut_to_ETERNA_BT.709_33grid_V.1.00.cube | | | | PASS (33pt) |
|  | └ zip member: x-m5-3d-lut-v100\F-Log2\XM5_FLog2_FGamut_to_FLog2_BT.709_33grid_V.1.00.cube | | | | PASS (33pt) |
|  | └ zip member: x-m5-3d-lut-v100\F-Log2\XM5_FLog2_FGamut_to_WDR_BT.709_33grid_V.1.00.cube | | | | PASS (33pt) |

## 3. GitHub Raw Repos — Verification by Repo

| Repo | License | Cubes | PASS 17/33 | REJECT 65 | REJECT other |
|---|---|---|---|---|---|
| Animesh-Does-Code/HDR-to-SDR-LUTs_YouTube | NONE | 7 | 7 | 0 | 0 |
| Joey-LJ/LUTS | NONE | 8 | 8 | 0 | 0 |
| MokshC/Film-Emulation-LUTs | LICENSE | 94 | 0 | 94 | 0 |
| QuagKhai003/ReinaLook | NONE | 2 | 0 | 2 | 0 |
| Royat07/S-Log3-to-Apple-Log | Creative Commons | 1 | 0 | 1 | 0 |
| TareqAmeer/Chroma-App | GPL-3.0 | 48 | 48 | 0 | 0 |
| YahiaAngelo/Film-Camera-IOS | MIT | 8 | 0 | 0 | 8 |
| imnz730/LUTs | NONE | 100 | 42 | 2 | 56 |
| jfmayeda/FilmFeel | NONE | 4 | 0 | 1 | 3 |
| moritzsalla/LogGrade-macOS | LICENSE | 4 | 0 | 4 | 0 |
| raycalrui/raycal-luts | NONE | 4 | 4 | 0 | 0 |
| scernst13/HaldCLUT-Cube-Files | CC0-1.0 | 14 | 14 | 0 | 0 |
| slaycamera/luts | CC-BY-4.0 | 5 | 5 | 0 | 0 |

## 4. Full PASS List (mobile 17pt / 33pt, GitHub raw + local)

| File | Repo | License | Size | SHA256 (12) | Raw URL | Verdict |
|---|---|---|---|---|---|---|
| clones/Animesh-Does-Code_HDR-to-SDR-LUTs_YouTube/1000nits_HDR-to-SDR.cube | Animesh-Does-Code/HDR-to-SDR-LUTs_YouTube | NONE | 520904 | 47c8657793f2 | https://raw.githubusercontent.com/Animesh-Does-Code/HDR-to-SDR-LUTs_YouTube/main/1000nits_HDR-to-SDR.cube | PASS (33pt) |
| clones/Animesh-Does-Code_HDR-to-SDR-LUTs_YouTube/1200nits_HDR-to-SDR.cube | Animesh-Does-Code/HDR-to-SDR-LUTs_YouTube | NONE | 522493 | 8ffddb9e1c48 | https://raw.githubusercontent.com/Animesh-Does-Code/HDR-to-SDR-LUTs_YouTube/main/1200nits_HDR-to-SDR.cube | PASS (33pt) |
| clones/Animesh-Does-Code_HDR-to-SDR-LUTs_YouTube/1500nits_HDR-to-SDR.cube | Animesh-Does-Code/HDR-to-SDR-LUTs_YouTube | NONE | 525277 | 8b662e29544f | https://raw.githubusercontent.com/Animesh-Does-Code/HDR-to-SDR-LUTs_YouTube/main/1500nits_HDR-to-SDR.cube | PASS (33pt) |
| clones/Animesh-Does-Code_HDR-to-SDR-LUTs_YouTube/2000nits_HDR-to-SDR.cube | Animesh-Does-Code/HDR-to-SDR-LUTs_YouTube | NONE | 529643 | 7df6e65ef82a | https://raw.githubusercontent.com/Animesh-Does-Code/HDR-to-SDR-LUTs_YouTube/main/2000nits_HDR-to-SDR.cube | PASS (33pt) |
| clones/Animesh-Does-Code_HDR-to-SDR-LUTs_YouTube/400nits_HDR-to-SDR.cube | Animesh-Does-Code/HDR-to-SDR-LUTs_YouTube | NONE | 475808 | 3d817bacc86f | https://raw.githubusercontent.com/Animesh-Does-Code/HDR-to-SDR-LUTs_YouTube/main/400nits_HDR-to-SDR.cube | PASS (33pt) |
| clones/Animesh-Does-Code_HDR-to-SDR-LUTs_YouTube/600nits_HDR-to-SDR.cube | Animesh-Does-Code/HDR-to-SDR-LUTs_YouTube | NONE | 507332 | 562e4f140faf | https://raw.githubusercontent.com/Animesh-Does-Code/HDR-to-SDR-LUTs_YouTube/main/600nits_HDR-to-SDR.cube | PASS (33pt) |
| clones/Animesh-Does-Code_HDR-to-SDR-LUTs_YouTube/800nits_HDR-to-SDR.cube | Animesh-Does-Code/HDR-to-SDR-LUTs_YouTube | NONE | 517180 | c1c8d0bd2874 | https://raw.githubusercontent.com/Animesh-Does-Code/HDR-to-SDR-LUTs_YouTube/main/800nits_HDR-to-SDR.cube | PASS (33pt) |
| clones/Joey-LJ_LUTS/Fuji_GFX to Apple_Log_2 LUT/FUJI-ACROS_1.A001_11220924_C056.cube | Joey-LJ/LUTS | NONE | 999168 | 2956857ff855 | https://raw.githubusercontent.com/Joey-LJ/LUTS/main/Fuji_GFX%20to%20Apple_Log_2%20LUT/FUJI-ACROS_1.A001_11220924_C056.cube | PASS (33pt) |
| clones/Joey-LJ_LUTS/Fuji_GFX to Apple_Log_2 LUT/FUJI-ASTIA_1.A001_11220924_C056.cube | Joey-LJ/LUTS | NONE | 946656 | 7654e69ebeb3 | https://raw.githubusercontent.com/Joey-LJ/LUTS/main/Fuji_GFX%20to%20Apple_Log_2%20LUT/FUJI-ASTIA_1.A001_11220924_C056.cube | PASS (33pt) |
| clones/Joey-LJ_LUTS/Fuji_GFX to Apple_Log_2 LUT/FUJI-CC_1.A001_11220924_C056.cube | Joey-LJ/LUTS | NONE | 1014909 | 4a89bd1a22b3 | https://raw.githubusercontent.com/Joey-LJ/LUTS/main/Fuji_GFX%20to%20Apple_Log_2%20LUT/FUJI-CC_1.A001_11220924_C056.cube | PASS (33pt) |
| clones/Joey-LJ_LUTS/Fuji_GFX to Apple_Log_2 LUT/FUJI-CN_1.A001_11220924_C056.cube | Joey-LJ/LUTS | NONE | 1003724 | 27565b15374b | https://raw.githubusercontent.com/Joey-LJ/LUTS/main/Fuji_GFX%20to%20Apple_Log_2%20LUT/FUJI-CN_1.A001_11220924_C056.cube | PASS (33pt) |
| clones/Joey-LJ_LUTS/Fuji_GFX to Apple_Log_2 LUT/FUJI-ETERNA-BB_1.A001_11220924_C056.cube | Joey-LJ/LUTS | NONE | 994783 | d2c39dc4330e | https://raw.githubusercontent.com/Joey-LJ/LUTS/main/Fuji_GFX%20to%20Apple_Log_2%20LUT/FUJI-ETERNA-BB_1.A001_11220924_C056.cube | PASS (33pt) |
| clones/Joey-LJ_LUTS/Fuji_GFX to Apple_Log_2 LUT/FUJI-ETERNA_1.A001_11220924_C056.cube | Joey-LJ/LUTS | NONE | 996584 | 8317ec5aabd0 | https://raw.githubusercontent.com/Joey-LJ/LUTS/main/Fuji_GFX%20to%20Apple_Log_2%20LUT/FUJI-ETERNA_1.A001_11220924_C056.cube | PASS (33pt) |
| clones/Joey-LJ_LUTS/Fuji_GFX to Apple_Log_2 LUT/FUJI-PROVIA_1.A001_11220924_C056.cube | Joey-LJ/LUTS | NONE | 865078 | c9d20227ffb8 | https://raw.githubusercontent.com/Joey-LJ/LUTS/main/Fuji_GFX%20to%20Apple_Log_2%20LUT/FUJI-PROVIA_1.A001_11220924_C056.cube | PASS (33pt) |
| clones/Joey-LJ_LUTS/Fuji_GFX to Apple_Log_2 LUT/FUJI-VELVIA_1.A001_11220924_C056.cube | Joey-LJ/LUTS | NONE | 944330 | b8889d5a093e | https://raw.githubusercontent.com/Joey-LJ/LUTS/main/Fuji_GFX%20to%20Apple_Log_2%20LUT/FUJI-VELVIA_1.A001_11220924_C056.cube | PASS (33pt) |
| clones/TareqAmeer_Chroma-App/tools/calib/PRINT PROFILES/fuji_print.cube | TareqAmeer/Chroma-App | GPL-3.0 | 970354 | 02a4b914cb2d | https://raw.githubusercontent.com/TareqAmeer/Chroma-App/main/tools/calib/PRINT%20PROFILES/fuji_print.cube | PASS (33pt) |
| clones/TareqAmeer_Chroma-App/tools/calib/PRINT PROFILES/kodak_print.cube | TareqAmeer/Chroma-App | GPL-3.0 | 970355 | dd1d199881bd | https://raw.githubusercontent.com/TareqAmeer/Chroma-App/main/tools/calib/PRINT%20PROFILES/kodak_print.cube | PASS (33pt) |
| clones/TareqAmeer_Chroma-App/tools/calib/LUT LIBRARY/a_beach_preset.cube | TareqAmeer/Chroma-App | GPL-3.0 | 970358 | 1c53556d96d3 | https://raw.githubusercontent.com/TareqAmeer/Chroma-App/main/tools/calib/LUT%20LIBRARY/a_beach_preset.cube | PASS (33pt) |
| clones/TareqAmeer_Chroma-App/tools/calib/LUT LIBRARY/aerocolor_endura_premier.cube | TareqAmeer/Chroma-App | GPL-3.0 | 1078158 | c27b13f88fed | https://raw.githubusercontent.com/TareqAmeer/Chroma-App/main/tools/calib/LUT%20LIBRARY/aerocolor_endura_premier.cube | PASS (33pt) |
| clones/TareqAmeer_Chroma-App/tools/calib/LUT LIBRARY/aerocolor_high_endura_premier.cube | TareqAmeer/Chroma-App | GPL-3.0 | 1078163 | 807beef45029 | https://raw.githubusercontent.com/TareqAmeer/Chroma-App/main/tools/calib/LUT%20LIBRARY/aerocolor_high_endura_premier.cube | PASS (33pt) |
| clones/TareqAmeer_Chroma-App/tools/calib/LUT LIBRARY/agfa_vista_100_ca_dpii.cube | TareqAmeer/Chroma-App | GPL-3.0 | 1078156 | 1af2e0adb269 | https://raw.githubusercontent.com/TareqAmeer/Chroma-App/main/tools/calib/LUT%20LIBRARY/agfa_vista_100_ca_dpii.cube | PASS (33pt) |
| clones/TareqAmeer_Chroma-App/tools/calib/LUT LIBRARY/astia.cube | TareqAmeer/Chroma-App | GPL-3.0 | 1006344 | 6a436a7760ed | https://raw.githubusercontent.com/TareqAmeer/Chroma-App/main/tools/calib/LUT%20LIBRARY/astia.cube | PASS (33pt) |
| clones/TareqAmeer_Chroma-App/tools/calib/LUT LIBRARY/classic_chrome_composed.cube | TareqAmeer/Chroma-App | GPL-3.0 | 970441 | b0992702235e | https://raw.githubusercontent.com/TareqAmeer/Chroma-App/main/tools/calib/LUT%20LIBRARY/classic_chrome_composed.cube | PASS (33pt) |
| clones/TareqAmeer_Chroma-App/tools/calib/LUT LIBRARY/classic_neg.cube | TareqAmeer/Chroma-App | GPL-3.0 | 1006344 | c9a50815e128 | https://raw.githubusercontent.com/TareqAmeer/Chroma-App/main/tools/calib/LUT%20LIBRARY/classic_neg.cube | PASS (33pt) |
| clones/TareqAmeer_Chroma-App/tools/calib/LUT LIBRARY/ektachrome_100d_radiance_iii.cube | TareqAmeer/Chroma-App | GPL-3.0 | 1078162 | bc7522184d2d | https://raw.githubusercontent.com/TareqAmeer/Chroma-App/main/tools/calib/LUT%20LIBRARY/ektachrome_100d_radiance_iii.cube | PASS (33pt) |
| clones/TareqAmeer_Chroma-App/tools/calib/LUT LIBRARY/ektar_100_endura_premier.cube | TareqAmeer/Chroma-App | GPL-3.0 | 1078158 | e2ecc4986b3f | https://raw.githubusercontent.com/TareqAmeer/Chroma-App/main/tools/calib/LUT%20LIBRARY/ektar_100_endura_premier.cube | PASS (33pt) |
| clones/TareqAmeer_Chroma-App/tools/calib/LUT LIBRARY/eterna_bleach_bypass_composed.cube | TareqAmeer/Chroma-App | GPL-3.0 | 970447 | 94db0d51ef1a | https://raw.githubusercontent.com/TareqAmeer/Chroma-App/main/tools/calib/LUT%20LIBRARY/eterna_bleach_bypass_composed.cube | PASS (33pt) |
| clones/TareqAmeer_Chroma-App/tools/calib/LUT LIBRARY/eterna_cinema_composed.cube | TareqAmeer/Chroma-App | GPL-3.0 | 970440 | 33339c46f0d6 | https://raw.githubusercontent.com/TareqAmeer/Chroma-App/main/tools/calib/LUT%20LIBRARY/eterna_cinema_composed.cube | PASS (33pt) |
| clones/TareqAmeer_Chroma-App/tools/calib/LUT LIBRARY/fp100c_fujiflex_new.cube | TareqAmeer/Chroma-App | GPL-3.0 | 1078153 | 41f197c7de4a | https://raw.githubusercontent.com/TareqAmeer/Chroma-App/main/tools/calib/LUT%20LIBRARY/fp100c_fujiflex_new.cube | PASS (33pt) |
| clones/TareqAmeer_Chroma-App/tools/calib/LUT LIBRARY/fuji_c200_ca_dpii.cube | TareqAmeer/Chroma-App | GPL-3.0 | 1078151 | 07b770397435 | https://raw.githubusercontent.com/TareqAmeer/Chroma-App/main/tools/calib/LUT%20LIBRARY/fuji_c200_ca_dpii.cube | PASS (33pt) |
| clones/TareqAmeer_Chroma-App/tools/calib/LUT LIBRARY/fuji_natura_1600_ca_dpii.cube | TareqAmeer/Chroma-App | GPL-3.0 | 1078158 | 263792ff3c34 | https://raw.githubusercontent.com/TareqAmeer/Chroma-App/main/tools/calib/LUT%20LIBRARY/fuji_natura_1600_ca_dpii.cube | PASS (33pt) |
| clones/TareqAmeer_Chroma-App/tools/calib/LUT LIBRARY/fuji_pro_160c_ca_maxima.cube | TareqAmeer/Chroma-App | GPL-3.0 | 1078157 | cb0d9f2bf33e | https://raw.githubusercontent.com/TareqAmeer/Chroma-App/main/tools/calib/LUT%20LIBRARY/fuji_pro_160c_ca_maxima.cube | PASS (33pt) |
| clones/TareqAmeer_Chroma-App/tools/calib/LUT LIBRARY/fuji_pro_160s_ca_dpii.cube | TareqAmeer/Chroma-App | GPL-3.0 | 1078155 | bc0b1ffcbe57 | https://raw.githubusercontent.com/TareqAmeer/Chroma-App/main/tools/calib/LUT%20LIBRARY/fuji_pro_160s_ca_dpii.cube | PASS (33pt) |
| clones/TareqAmeer_Chroma-App/tools/calib/LUT LIBRARY/fuji_pro_400h_ca_maxima.cube | TareqAmeer/Chroma-App | GPL-3.0 | 1078157 | 30addbbfee94 | https://raw.githubusercontent.com/TareqAmeer/Chroma-App/main/tools/calib/LUT%20LIBRARY/fuji_pro_400h_ca_maxima.cube | PASS (33pt) |
| clones/TareqAmeer_Chroma-App/tools/calib/LUT LIBRARY/fuji_superia_reala_ca_pro_pdii.cube | TareqAmeer/Chroma-App | GPL-3.0 | 1078164 | 2d954e2b9a1d | https://raw.githubusercontent.com/TareqAmeer/Chroma-App/main/tools/calib/LUT%20LIBRARY/fuji_superia_reala_ca_pro_pdii.cube | PASS (33pt) |
| clones/TareqAmeer_Chroma-App/tools/calib/LUT LIBRARY/fuji_superia_xtra_400_ca_dpii.cube | TareqAmeer/Chroma-App | GPL-3.0 | 1078163 | 1b96530de5a3 | https://raw.githubusercontent.com/TareqAmeer/Chroma-App/main/tools/calib/LUT%20LIBRARY/fuji_superia_xtra_400_ca_dpii.cube | PASS (33pt) |
| clones/TareqAmeer_Chroma-App/tools/calib/LUT LIBRARY/gold_200_endura_premier.cube | TareqAmeer/Chroma-App | GPL-3.0 | 1078157 | f7d4bc3b8f81 | https://raw.githubusercontent.com/TareqAmeer/Chroma-App/main/tools/calib/LUT%20LIBRARY/gold_200_endura_premier.cube | PASS (33pt) |
| clones/TareqAmeer_Chroma-App/tools/calib/LUT LIBRARY/instax_color_fujiflex_new.cube | TareqAmeer/Chroma-App | GPL-3.0 | 1078159 | 3074aba4b319 | https://raw.githubusercontent.com/TareqAmeer/Chroma-App/main/tools/calib/LUT%20LIBRARY/instax_color_fujiflex_new.cube | PASS (33pt) |
| clones/TareqAmeer_Chroma-App/tools/calib/LUT LIBRARY/kodachrome_64_radiance_iii.cube | TareqAmeer/Chroma-App | GPL-3.0 | 1078160 | 210e40404c7a | https://raw.githubusercontent.com/TareqAmeer/Chroma-App/main/tools/calib/LUT%20LIBRARY/kodachrome_64_radiance_iii.cube | PASS (33pt) |
| clones/TareqAmeer_Chroma-App/tools/calib/LUT LIBRARY/kodak_5222_2302_dev_5.cube | TareqAmeer/Chroma-App | GPL-3.0 | 1078155 | ef11e19a72f2 | https://raw.githubusercontent.com/TareqAmeer/Chroma-App/main/tools/calib/LUT%20LIBRARY/kodak_5222_2302_dev_5.cube | PASS (33pt) |
| clones/TareqAmeer_Chroma-App/tools/calib/LUT LIBRARY/kodak_5222_polymax_grade_2.cube | TareqAmeer/Chroma-App | GPL-3.0 | 1078160 | 34179ac3b962 | https://raw.githubusercontent.com/TareqAmeer/Chroma-App/main/tools/calib/LUT%20LIBRARY/kodak_5222_polymax_grade_2.cube | PASS (33pt) |
| clones/TareqAmeer_Chroma-App/tools/calib/LUT LIBRARY/nostalgic_neg_composed.cube | TareqAmeer/Chroma-App | GPL-3.0 | 970371 | 945eaaa572e5 | https://raw.githubusercontent.com/TareqAmeer/Chroma-App/main/tools/calib/LUT%20LIBRARY/nostalgic_neg_composed.cube | PASS (33pt) |
| clones/TareqAmeer_Chroma-App/tools/calib/LUT LIBRARY/portra_160_endura_premier.cube | TareqAmeer/Chroma-App | GPL-3.0 | 1078159 | f8123a040781 | https://raw.githubusercontent.com/TareqAmeer/Chroma-App/main/tools/calib/LUT%20LIBRARY/portra_160_endura_premier.cube | PASS (33pt) |
| clones/TareqAmeer_Chroma-App/tools/calib/LUT LIBRARY/portra_400_endura_premier.cube | TareqAmeer/Chroma-App | GPL-3.0 | 1078159 | aea5a2aad146 | https://raw.githubusercontent.com/TareqAmeer/Chroma-App/main/tools/calib/LUT%20LIBRARY/portra_400_endura_premier.cube | PASS (33pt) |
| clones/TareqAmeer_Chroma-App/tools/calib/LUT LIBRARY/portra_400_portra_endura.cube | TareqAmeer/Chroma-App | GPL-3.0 | 1078158 | 67cdfe8622f5 | https://raw.githubusercontent.com/TareqAmeer/Chroma-App/main/tools/calib/LUT%20LIBRARY/portra_400_portra_endura.cube | PASS (33pt) |
| clones/TareqAmeer_Chroma-App/tools/calib/LUT LIBRARY/portra_400_supra_endura.cube | TareqAmeer/Chroma-App | GPL-3.0 | 1078157 | 391725945e65 | https://raw.githubusercontent.com/TareqAmeer/Chroma-App/main/tools/calib/LUT%20LIBRARY/portra_400_supra_endura.cube | PASS (33pt) |
| clones/TareqAmeer_Chroma-App/tools/calib/LUT LIBRARY/portra_800_endura_premier.cube | TareqAmeer/Chroma-App | GPL-3.0 | 1078159 | 9ea65a54fb18 | https://raw.githubusercontent.com/TareqAmeer/Chroma-App/main/tools/calib/LUT%20LIBRARY/portra_800_endura_premier.cube | PASS (33pt) |
| clones/TareqAmeer_Chroma-App/tools/calib/LUT LIBRARY/pro_neg_std_composed.cube | TareqAmeer/Chroma-App | GPL-3.0 | 970438 | cb115640f14e | https://raw.githubusercontent.com/TareqAmeer/Chroma-App/main/tools/calib/LUT%20LIBRARY/pro_neg_std_composed.cube | PASS (33pt) |
| clones/TareqAmeer_Chroma-App/tools/calib/LUT LIBRARY/provia_100f_ilfochrome_m.cube | TareqAmeer/Chroma-App | GPL-3.0 | 1078158 | e9b83f757ec4 | https://raw.githubusercontent.com/TareqAmeer/Chroma-App/main/tools/calib/LUT%20LIBRARY/provia_100f_ilfochrome_m.cube | PASS (33pt) |
| clones/TareqAmeer_Chroma-App/tools/calib/LUT LIBRARY/provia_composed.cube | TareqAmeer/Chroma-App | GPL-3.0 | 970433 | d192bea0ce2c | https://raw.githubusercontent.com/TareqAmeer/Chroma-App/main/tools/calib/LUT%20LIBRARY/provia_composed.cube | PASS (33pt) |
| clones/TareqAmeer_Chroma-App/tools/calib/LUT LIBRARY/reala_ace_composed.cube | TareqAmeer/Chroma-App | GPL-3.0 | 970436 | 67aa364ff9e8 | https://raw.githubusercontent.com/TareqAmeer/Chroma-App/main/tools/calib/LUT%20LIBRARY/reala_ace_composed.cube | PASS (33pt) |
| clones/TareqAmeer_Chroma-App/tools/calib/LUT LIBRARY/trix_400_polymax_grade_2.cube | TareqAmeer/Chroma-App | GPL-3.0 | 1078158 | b18bb79af811 | https://raw.githubusercontent.com/TareqAmeer/Chroma-App/main/tools/calib/LUT%20LIBRARY/trix_400_polymax_grade_2.cube | PASS (33pt) |
| clones/TareqAmeer_Chroma-App/tools/calib/LUT LIBRARY/trix_400_polymax_grade_3.cube | TareqAmeer/Chroma-App | GPL-3.0 | 1078158 | 0bf1f38909b5 | https://raw.githubusercontent.com/TareqAmeer/Chroma-App/main/tools/calib/LUT%20LIBRARY/trix_400_polymax_grade_3.cube | PASS (33pt) |
| clones/TareqAmeer_Chroma-App/tools/calib/LUT LIBRARY/ultramax_500_endura_premier.cube | TareqAmeer/Chroma-App | GPL-3.0 | 1078161 | cc5aba7ca9cd | https://raw.githubusercontent.com/TareqAmeer/Chroma-App/main/tools/calib/LUT%20LIBRARY/ultramax_500_endura_premier.cube | PASS (33pt) |
| clones/TareqAmeer_Chroma-App/tools/calib/LUT LIBRARY/velvia.cube | TareqAmeer/Chroma-App | GPL-3.0 | 1006344 | 3258064b4e1e | https://raw.githubusercontent.com/TareqAmeer/Chroma-App/main/tools/calib/LUT%20LIBRARY/velvia.cube | PASS (33pt) |
| clones/TareqAmeer_Chroma-App/tools/calib/LUT LIBRARY/velvia_50_ilfochrome_m.cube | TareqAmeer/Chroma-App | GPL-3.0 | 1078156 | 7726d00436fd | https://raw.githubusercontent.com/TareqAmeer/Chroma-App/main/tools/calib/LUT%20LIBRARY/velvia_50_ilfochrome_m.cube | PASS (33pt) |
| clones/TareqAmeer_Chroma-App/tools/calib/LUT LIBRARY/vericolor_iii_endura_premier.cube | TareqAmeer/Chroma-App | GPL-3.0 | 1078162 | 0e5c38823306 | https://raw.githubusercontent.com/TareqAmeer/Chroma-App/main/tools/calib/LUT%20LIBRARY/vericolor_iii_endura_premier.cube | PASS (33pt) |
| clones/TareqAmeer_Chroma-App/tools/calib/LUT LIBRARY/vision3_200t_2383.cube | TareqAmeer/Chroma-App | GPL-3.0 | 1078151 | b266f025b0a9 | https://raw.githubusercontent.com/TareqAmeer/Chroma-App/main/tools/calib/LUT%20LIBRARY/vision3_200t_2383.cube | PASS (33pt) |
| clones/TareqAmeer_Chroma-App/tools/calib/LUT LIBRARY/vision3_250d_2383.cube | TareqAmeer/Chroma-App | GPL-3.0 | 1078151 | bca1057be8d2 | https://raw.githubusercontent.com/TareqAmeer/Chroma-App/main/tools/calib/LUT%20LIBRARY/vision3_250d_2383.cube | PASS (33pt) |
| clones/TareqAmeer_Chroma-App/tools/calib/LUT LIBRARY/vision3_250d_2393.cube | TareqAmeer/Chroma-App | GPL-3.0 | 1078151 | ad9b7349c0b4 | https://raw.githubusercontent.com/TareqAmeer/Chroma-App/main/tools/calib/LUT%20LIBRARY/vision3_250d_2393.cube | PASS (33pt) |
| clones/TareqAmeer_Chroma-App/tools/calib/LUT LIBRARY/vision3_500t_2383.cube | TareqAmeer/Chroma-App | GPL-3.0 | 1078151 | c2f1975923fd | https://raw.githubusercontent.com/TareqAmeer/Chroma-App/main/tools/calib/LUT%20LIBRARY/vision3_500t_2383.cube | PASS (33pt) |
| clones/TareqAmeer_Chroma-App/tools/calib/LUT LIBRARY/vision3_500t_2393.cube | TareqAmeer/Chroma-App | GPL-3.0 | 1078151 | 0a42958bc222 | https://raw.githubusercontent.com/TareqAmeer/Chroma-App/main/tools/calib/LUT%20LIBRARY/vision3_500t_2393.cube | PASS (33pt) |
| clones/TareqAmeer_Chroma-App/tools/calib/LUT LIBRARY/vision3_50d_2383.cube | TareqAmeer/Chroma-App | GPL-3.0 | 1078150 | b8f9dfde3e66 | https://raw.githubusercontent.com/TareqAmeer/Chroma-App/main/tools/calib/LUT%20LIBRARY/vision3_50d_2383.cube | PASS (33pt) |
| clones/imnz730_LUTs/DCI/Rec709 to DCI-XYZ.cube | imnz730/LUTs | NONE | 1401716 | d65dc2fe2233 | https://raw.githubusercontent.com/imnz730/LUTs/master/DCI/Rec709%20to%20DCI-XYZ.cube | PASS (33pt) |
| clones/imnz730_LUTs/DCI/sRGB to DCI-XYZ.cube | imnz730/LUTs | NONE | 1401718 | 6ce7528ed922 | https://raw.githubusercontent.com/imnz730/LUTs/master/DCI/sRGB%20to%20DCI-XYZ.cube | PASS (33pt) |
| clones/imnz730_LUTs/Film Looks/DCI-P3 Fujifilm 3513DI D55.cube | imnz730/LUTs | NONE | 970583 | a2f26239d56b | https://raw.githubusercontent.com/imnz730/LUTs/master/Film%20Looks/DCI-P3%20Fujifilm%203513DI%20D55.cube | PASS (33pt) |
| clones/imnz730_LUTs/Film Looks/DCI-P3 Fujifilm 3513DI D60.cube | imnz730/LUTs | NONE | 970583 | 975e0ef7bb41 | https://raw.githubusercontent.com/imnz730/LUTs/master/Film%20Looks/DCI-P3%20Fujifilm%203513DI%20D60.cube | PASS (33pt) |
| clones/imnz730_LUTs/Film Looks/DCI-P3 Fujifilm 3513DI D65.cube | imnz730/LUTs | NONE | 970583 | a117b3213354 | https://raw.githubusercontent.com/imnz730/LUTs/master/Film%20Looks/DCI-P3%20Fujifilm%203513DI%20D65.cube | PASS (33pt) |
| clones/imnz730_LUTs/Film Looks/DCI-P3 Kodak 2383 D55.cube | imnz730/LUTs | NONE | 970578 | 5408d249d7b4 | https://raw.githubusercontent.com/imnz730/LUTs/master/Film%20Looks/DCI-P3%20Kodak%202383%20D55.cube | PASS (33pt) |
| clones/imnz730_LUTs/Film Looks/DCI-P3 Kodak 2383 D60.cube | imnz730/LUTs | NONE | 970578 | 0d57c6194ada | https://raw.githubusercontent.com/imnz730/LUTs/master/Film%20Looks/DCI-P3%20Kodak%202383%20D60.cube | PASS (33pt) |
| clones/imnz730_LUTs/Film Looks/DCI-P3 Kodak 2383 D65.cube | imnz730/LUTs | NONE | 970578 | e18fc5b4234a | https://raw.githubusercontent.com/imnz730/LUTs/master/Film%20Looks/DCI-P3%20Kodak%202383%20D65.cube | PASS (33pt) |
| clones/imnz730_LUTs/Film Looks/Rec709 Fujifilm 3513DI D55.cube | imnz730/LUTs | NONE | 970588 | 948f7ef787ac | https://raw.githubusercontent.com/imnz730/LUTs/master/Film%20Looks/Rec709%20Fujifilm%203513DI%20D55.cube | PASS (33pt) |
| clones/imnz730_LUTs/Film Looks/Rec709 Fujifilm 3513DI D60.cube | imnz730/LUTs | NONE | 970588 | 11e842899425 | https://raw.githubusercontent.com/imnz730/LUTs/master/Film%20Looks/Rec709%20Fujifilm%203513DI%20D60.cube | PASS (33pt) |
| clones/imnz730_LUTs/Film Looks/Rec709 Fujifilm 3513DI D65.cube | imnz730/LUTs | NONE | 970588 | ec0be2eeae3a | https://raw.githubusercontent.com/imnz730/LUTs/master/Film%20Looks/Rec709%20Fujifilm%203513DI%20D65.cube | PASS (33pt) |
| clones/imnz730_LUTs/Film Looks/Rec709 Kodak 2383 D55.cube | imnz730/LUTs | NONE | 970583 | a14245cd4092 | https://raw.githubusercontent.com/imnz730/LUTs/master/Film%20Looks/Rec709%20Kodak%202383%20D55.cube | PASS (33pt) |
| clones/imnz730_LUTs/Film Looks/Rec709 Kodak 2383 D60.cube | imnz730/LUTs | NONE | 970583 | 73a1b85a18a4 | https://raw.githubusercontent.com/imnz730/LUTs/master/Film%20Looks/Rec709%20Kodak%202383%20D60.cube | PASS (33pt) |
| clones/imnz730_LUTs/Film Looks/Rec709 Kodak 2383 D65.cube | imnz730/LUTs | NONE | 970583 | d315680d7c6c | https://raw.githubusercontent.com/imnz730/LUTs/master/Film%20Looks/Rec709%20Kodak%202383%20D65.cube | PASS (33pt) |
| clones/imnz730_LUTs/DJI/DJI_Phantom3_DLOG2sRGB_Improv.cube | imnz730/LUTs | NONE | 820142 | 8526b03792fc | https://raw.githubusercontent.com/imnz730/LUTs/master/DJI/DJI_Phantom3_DLOG2sRGB_Improv.cube | PASS (33pt) |
| clones/imnz730_LUTs/DJI/DJI_Phantom4_DLOG2Rec709.cube | imnz730/LUTs | NONE | 662993 | 3747181d1f20 | https://raw.githubusercontent.com/imnz730/LUTs/master/DJI/DJI_Phantom4_DLOG2Rec709.cube | PASS (33pt) |
| clones/imnz730_LUTs/DJI/DJI_Phantom4_DLOG2sRGB_Improv.cube | imnz730/LUTs | NONE | 673471 | 8503de0a9152 | https://raw.githubusercontent.com/imnz730/LUTs/master/DJI/DJI_Phantom4_DLOG2sRGB_Improv.cube | PASS (33pt) |
| clones/imnz730_LUTs/DJI/DJI_X5_DLOG2sRGB_Improv.cube | imnz730/LUTs | NONE | 520339 | e9d1679b043a | https://raw.githubusercontent.com/imnz730/LUTs/master/DJI/DJI_X5_DLOG2sRGB_Improv.cube | PASS (33pt) |
| clones/imnz730_LUTs/DJI/DJI_X7_DLOG2Rec709.cube | imnz730/LUTs | NONE | 1401640 | 0a576b299d8c | https://raw.githubusercontent.com/imnz730/LUTs/master/DJI/DJI_X7_DLOG2Rec709.cube | PASS (33pt) |
| clones/imnz730_LUTs/Blackmagic Design/Blackmagic 4.6K Film to Extended Video v4.cube | imnz730/LUTs | NONE | 1401588 | fdaa7d4b9e06 | https://raw.githubusercontent.com/imnz730/LUTs/master/Blackmagic%20Design/Blackmagic%204.6K%20Film%20to%20Extended%20Video%20v4.cube | PASS (33pt) |
| clones/imnz730_LUTs/Blackmagic Design/Blackmagic 4.6K Film to Rec709 v3.cube | imnz730/LUTs | NONE | 1401746 | 2d069c30ce87 | https://raw.githubusercontent.com/imnz730/LUTs/master/Blackmagic%20Design/Blackmagic%204.6K%20Film%20to%20Rec709%20v3.cube | PASS (33pt) |
| clones/imnz730_LUTs/Blackmagic Design/Blackmagic 4.6K Film to Rec709.cube | imnz730/LUTs | NONE | 1401680 | 10a3f470dde8 | https://raw.githubusercontent.com/imnz730/LUTs/master/Blackmagic%20Design/Blackmagic%204.6K%20Film%20to%20Rec709.cube | PASS (33pt) |
| clones/imnz730_LUTs/Blackmagic Design/Blackmagic 4.6K Film to Video v3.cube | imnz730/LUTs | NONE | 1401780 | 68af6c3ddf14 | https://raw.githubusercontent.com/imnz730/LUTs/master/Blackmagic%20Design/Blackmagic%204.6K%20Film%20to%20Video%20v3.cube | PASS (33pt) |
| clones/imnz730_LUTs/Blackmagic Design/Blackmagic 4.6K Film to Video v4.cube | imnz730/LUTs | NONE | 1401588 | 0e9de21e5011 | https://raw.githubusercontent.com/imnz730/LUTs/master/Blackmagic%20Design/Blackmagic%204.6K%20Film%20to%20Video%20v4.cube | PASS (33pt) |
| clones/imnz730_LUTs/Blackmagic Design/Blackmagic 4.6K Film to Video.cube | imnz730/LUTs | NONE | 1401679 | 84abbde1c030 | https://raw.githubusercontent.com/imnz730/LUTs/master/Blackmagic%20Design/Blackmagic%204.6K%20Film%20to%20Video.cube | PASS (33pt) |
| clones/imnz730_LUTs/Blackmagic Design/Blackmagic 4K Film to Extended Video v4.cube | imnz730/LUTs | NONE | 1401588 | 30ea93aff74f | https://raw.githubusercontent.com/imnz730/LUTs/master/Blackmagic%20Design/Blackmagic%204K%20Film%20to%20Extended%20Video%20v4.cube | PASS (33pt) |
| clones/imnz730_LUTs/Blackmagic Design/Blackmagic 4K Film to Rec709 v2.cube | imnz730/LUTs | NONE | 1401692 | 9ab501cd73ce | https://raw.githubusercontent.com/imnz730/LUTs/master/Blackmagic%20Design/Blackmagic%204K%20Film%20to%20Rec709%20v2.cube | PASS (33pt) |
| clones/imnz730_LUTs/Blackmagic Design/Blackmagic 4K Film to Rec709 v3.cube | imnz730/LUTs | NONE | 1401742 | af6837d939cb | https://raw.githubusercontent.com/imnz730/LUTs/master/Blackmagic%20Design/Blackmagic%204K%20Film%20to%20Rec709%20v3.cube | PASS (33pt) |
| clones/imnz730_LUTs/Blackmagic Design/Blackmagic 4K Film to Rec709.cube | imnz730/LUTs | NONE | 970353 | 7ab59d9f722f | https://raw.githubusercontent.com/imnz730/LUTs/master/Blackmagic%20Design/Blackmagic%204K%20Film%20to%20Rec709.cube | PASS (33pt) |
| clones/imnz730_LUTs/Blackmagic Design/Blackmagic 4K Film to Video v3.cube | imnz730/LUTs | NONE | 1401774 | 5ed0d38ebfa5 | https://raw.githubusercontent.com/imnz730/LUTs/master/Blackmagic%20Design/Blackmagic%204K%20Film%20to%20Video%20v3.cube | PASS (33pt) |
| clones/imnz730_LUTs/Blackmagic Design/Blackmagic Broadcast Film to Extended Video v4.cube | imnz730/LUTs | NONE | 1401588 | caf2dd040c47 | https://raw.githubusercontent.com/imnz730/LUTs/master/Blackmagic%20Design/Blackmagic%20Broadcast%20Film%20to%20Extended%20Video%20v4.cube | PASS (33pt) |
| clones/imnz730_LUTs/Blackmagic Design/Blackmagic Broadcast Film to Rec2020 HLG v4.cube | imnz730/LUTs | NONE | 1401588 | b6f3a3772796 | https://raw.githubusercontent.com/imnz730/LUTs/master/Blackmagic%20Design/Blackmagic%20Broadcast%20Film%20to%20Rec2020%20HLG%20v4.cube | PASS (33pt) |
| clones/imnz730_LUTs/Blackmagic Design/Blackmagic Broadcast Film to Rec2020 PQ v4.cube | imnz730/LUTs | NONE | 1401588 | 941d6944c5d3 | https://raw.githubusercontent.com/imnz730/LUTs/master/Blackmagic%20Design/Blackmagic%20Broadcast%20Film%20to%20Rec2020%20PQ%20v4.cube | PASS (33pt) |
| clones/imnz730_LUTs/Blackmagic Design/Blackmagic Cinema Camera Film to Rec709 v2.cube | imnz730/LUTs | NONE | 1401685 | 2c2a7a04b019 | https://raw.githubusercontent.com/imnz730/LUTs/master/Blackmagic%20Design/Blackmagic%20Cinema%20Camera%20Film%20to%20Rec709%20v2.cube | PASS (33pt) |
| clones/imnz730_LUTs/Blackmagic Design/Blackmagic Cinema Camera Film to Rec709.cube | imnz730/LUTs | NONE | 970353 | 246f01d0ce36 | https://raw.githubusercontent.com/imnz730/LUTs/master/Blackmagic%20Design/Blackmagic%20Cinema%20Camera%20Film%20to%20Rec709.cube | PASS (33pt) |
| clones/imnz730_LUTs/Blackmagic Design/Blackmagic Film to Extended Video v4.cube | imnz730/LUTs | NONE | 1401588 | 8d9c8a04e946 | https://raw.githubusercontent.com/imnz730/LUTs/master/Blackmagic%20Design/Blackmagic%20Film%20to%20Extended%20Video%20v4.cube | PASS (33pt) |
| clones/imnz730_LUTs/Blackmagic Design/Blackmagic Pocket 4K Film to Extended Video v4.cube | imnz730/LUTs | NONE | 1401588 | 263dc0643a21 | https://raw.githubusercontent.com/imnz730/LUTs/master/Blackmagic%20Design/Blackmagic%20Pocket%204K%20Film%20to%20Extended%20Video%20v4.cube | PASS (33pt) |
| clones/imnz730_LUTs/Blackmagic Design/Blackmagic Pocket 4K Film to Video v4.cube | imnz730/LUTs | NONE | 1401588 | 646350bf5be3 | https://raw.githubusercontent.com/imnz730/LUTs/master/Blackmagic%20Design/Blackmagic%20Pocket%204K%20Film%20to%20Video%20v4.cube | PASS (33pt) |
| clones/imnz730_LUTs/Panasonic/VLog_to_V709_forV35_ver100.cube | imnz730/LUTs | NONE | 970363 | b53d6aa6ea76 | https://raw.githubusercontent.com/imnz730/LUTs/master/Panasonic/VLog_to_V709_forV35_ver100.cube | PASS (33pt) |
| clones/imnz730_LUTs/Sony/SLog3SGamut3.CineToLC-709.cube | imnz730/LUTs | NONE | 970424 | d41aeebbca5c | https://raw.githubusercontent.com/imnz730/LUTs/master/Sony/SLog3SGamut3.CineToLC-709.cube | PASS (33pt) |
| clones/imnz730_LUTs/Sony/SLog3SGamut3.CineToLC-709TypeA.cube | imnz730/LUTs | NONE | 970434 | 04066dc0a6d2 | https://raw.githubusercontent.com/imnz730/LUTs/master/Sony/SLog3SGamut3.CineToLC-709TypeA.cube | PASS (33pt) |
| clones/imnz730_LUTs/Sony/SLog3SGamut3.CineToSLog2-709.cube | imnz730/LUTs | NONE | 970430 | 0b241c50e74f | https://raw.githubusercontent.com/imnz730/LUTs/master/Sony/SLog3SGamut3.CineToSLog2-709.cube | PASS (33pt) |
| clones/raycalrui_raycal-luts/LUTs/Apple Log 2_cinematic.cube | raycalrui/raycal-luts | NONE | 867248 | dfdac1e9f9da | https://raw.githubusercontent.com/raycalrui/raycal-luts/main/LUTs/Apple%20Log%202_cinematic.cube | PASS (33pt) |
| clones/raycalrui_raycal-luts/LUTs/Apple Log 2_natural.cube | raycalrui/raycal-luts | NONE | 866650 | f7cd3afb92dc | https://raw.githubusercontent.com/raycalrui/raycal-luts/main/LUTs/Apple%20Log%202_natural.cube | PASS (33pt) |
| clones/raycalrui_raycal-luts/LUTs/Apple Log_cinematic.cube | raycalrui/raycal-luts | NONE | 926408 | bbb35770cdfe | https://raw.githubusercontent.com/raycalrui/raycal-luts/main/LUTs/Apple%20Log_cinematic.cube | PASS (33pt) |
| clones/raycalrui_raycal-luts/LUTs/Apple Log_natural.cube | raycalrui/raycal-luts | NONE | 894044 | 65af08d69561 | https://raw.githubusercontent.com/raycalrui/raycal-luts/main/LUTs/Apple%20Log_natural.cube | PASS (33pt) |
| clones/scernst13_HaldCLUT-Cube-Files/Kodak Converted/Kodak E-100 GX Ektachrome 100.cube | scernst13/HaldCLUT-Cube-Files | CC0-1.0 | 1133336 | 72316a2a622d | https://raw.githubusercontent.com/scernst13/HaldCLUT-Cube-Files/main/Kodak%20Converted/Kodak%20E-100%20GX%20Ektachrome%20100.cube | PASS (33pt) |
| clones/scernst13_HaldCLUT-Cube-Files/Kodak Converted/Kodak Ektachrome 100 VS.cube | scernst13/HaldCLUT-Cube-Files | CC0-1.0 | 1063096 | bf3ee2ef92b9 | https://raw.githubusercontent.com/scernst13/HaldCLUT-Cube-Files/main/Kodak%20Converted/Kodak%20Ektachrome%20100%20VS.cube | PASS (33pt) |
| clones/scernst13_HaldCLUT-Cube-Files/Kodak Converted/Kodak Elite Chrome 200.cube | scernst13/HaldCLUT-Cube-Files | CC0-1.0 | 1087762 | ae2cb1ff5d92 | https://raw.githubusercontent.com/scernst13/HaldCLUT-Cube-Files/main/Kodak%20Converted/Kodak%20Elite%20Chrome%20200.cube | PASS (33pt) |
| clones/scernst13_HaldCLUT-Cube-Files/Kodak Converted/Kodak Elite Chrome 400.cube | scernst13/HaldCLUT-Cube-Files | CC0-1.0 | 1131999 | 4fb8e69ce96b | https://raw.githubusercontent.com/scernst13/HaldCLUT-Cube-Files/main/Kodak%20Converted/Kodak%20Elite%20Chrome%20400.cube | PASS (33pt) |
| clones/scernst13_HaldCLUT-Cube-Files/Kodak Converted/Kodak Elite Color 200.cube | scernst13/HaldCLUT-Cube-Files | CC0-1.0 | 1142177 | 24d7b94db0d3 | https://raw.githubusercontent.com/scernst13/HaldCLUT-Cube-Files/main/Kodak%20Converted/Kodak%20Elite%20Color%20200.cube | PASS (33pt) |
| clones/scernst13_HaldCLUT-Cube-Files/Kodak Converted/Kodak Elite Color 400.cube | scernst13/HaldCLUT-Cube-Files | CC0-1.0 | 1108097 | 9c841714c3e2 | https://raw.githubusercontent.com/scernst13/HaldCLUT-Cube-Files/main/Kodak%20Converted/Kodak%20Elite%20Color%20400.cube | PASS (33pt) |
| clones/scernst13_HaldCLUT-Cube-Files/Kodak Converted/Kodak Kodachrome 200.cube | scernst13/HaldCLUT-Cube-Files | CC0-1.0 | 1150705 | 3a45bea068b4 | https://raw.githubusercontent.com/scernst13/HaldCLUT-Cube-Files/main/Kodak%20Converted/Kodak%20Kodachrome%20200.cube | PASS (33pt) |
| clones/scernst13_HaldCLUT-Cube-Files/Kodak Converted/Kodak Kodachrome 64 Generic.cube | scernst13/HaldCLUT-Cube-Files | CC0-1.0 | 1082744 | a54ac9c0a933 | https://raw.githubusercontent.com/scernst13/HaldCLUT-Cube-Files/main/Kodak%20Converted/Kodak%20Kodachrome%2064%20Generic.cube | PASS (33pt) |
| clones/scernst13_HaldCLUT-Cube-Files/Kodak Converted/Kodak Portra 160 ++.cube | scernst13/HaldCLUT-Cube-Files | CC0-1.0 | 1139283 | e50abd0dc748 | https://raw.githubusercontent.com/scernst13/HaldCLUT-Cube-Files/main/Kodak%20Converted/Kodak%20Portra%20160%20%2B%2B.cube | PASS (33pt) |
| clones/scernst13_HaldCLUT-Cube-Files/Kodak Converted/Kodak Portra 160.cube | scernst13/HaldCLUT-Cube-Files | CC0-1.0 | 1117941 | ed2e011876db | https://raw.githubusercontent.com/scernst13/HaldCLUT-Cube-Files/main/Kodak%20Converted/Kodak%20Portra%20160.cube | PASS (33pt) |
| clones/scernst13_HaldCLUT-Cube-Files/Kodak Converted/Kodak Portra 400 ++.cube | scernst13/HaldCLUT-Cube-Files | CC0-1.0 | 1100601 | eaec044be9be | https://raw.githubusercontent.com/scernst13/HaldCLUT-Cube-Files/main/Kodak%20Converted/Kodak%20Portra%20400%20%2B%2B.cube | PASS (33pt) |
| clones/scernst13_HaldCLUT-Cube-Files/Kodak Converted/Kodak Portra 400.cube | scernst13/HaldCLUT-Cube-Files | CC0-1.0 | 1078650 | bb77590b586b | https://raw.githubusercontent.com/scernst13/HaldCLUT-Cube-Files/main/Kodak%20Converted/Kodak%20Portra%20400.cube | PASS (33pt) |
| clones/scernst13_HaldCLUT-Cube-Files/Kodak Converted/Kodak Portra 800 ++.cube | scernst13/HaldCLUT-Cube-Files | CC0-1.0 | 1080491 | b26173db9447 | https://raw.githubusercontent.com/scernst13/HaldCLUT-Cube-Files/main/Kodak%20Converted/Kodak%20Portra%20800%20%2B%2B.cube | PASS (33pt) |
| clones/scernst13_HaldCLUT-Cube-Files/Kodak Converted/Kodak Portra 800.cube | scernst13/HaldCLUT-Cube-Files | CC0-1.0 | 1039439 | 1400be7bb0ff | https://raw.githubusercontent.com/scernst13/HaldCLUT-Cube-Files/main/Kodak%20Converted/Kodak%20Portra%20800.cube | PASS (33pt) |
| clones/slaycamera_luts/luts/slay-01-amber.cube | slaycamera/luts | CC-BY-4.0 | 970501 | 5912a5761bb9 | https://raw.githubusercontent.com/slaycamera/luts/main/luts/slay-01-amber.cube | PASS (33pt) |
| clones/slaycamera_luts/luts/slay-02-fade.cube | slaycamera/luts | CC-BY-4.0 | 970500 | 0fc029d88a11 | https://raw.githubusercontent.com/slaycamera/luts/main/luts/slay-02-fade.cube | PASS (33pt) |
| clones/slaycamera_luts/luts/slay-03-neon.cube | slaycamera/luts | CC-BY-4.0 | 970500 | 07ac89f666c7 | https://raw.githubusercontent.com/slaycamera/luts/main/luts/slay-03-neon.cube | PASS (33pt) |
| clones/slaycamera_luts/luts/slay-04-film.cube | slaycamera/luts | CC-BY-4.0 | 970500 | d846f24a0ce3 | https://raw.githubusercontent.com/slaycamera/luts/main/luts/slay-04-film.cube | PASS (33pt) |
| clones/slaycamera_luts/luts/slay-05-portrait.cube | slaycamera/luts | CC-BY-4.0 | 970504 | 432898146d41 | https://raw.githubusercontent.com/slaycamera/luts/main/luts/slay-05-portrait.cube | PASS (33pt) |

## 5. REJECT Summary (top offenders)

| File | Declared size | Triplets | Verdict |
|---|---|---|---|
| clones/MokshC_Film-Emulation-LUTs/Hald_CLUT_Identity_12 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Color/Fuji/Fuji 160C 1 - 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Color/Fuji/Fuji 400H 1 - 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Color/Fuji/Fuji Astia 100 Generic 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Color/Fuji/Fuji Astia 100F 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Color/Fuji/Fuji FP-100c 1 -- 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Color/Fuji/Fuji FP-100c 4 Alt 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Color/Fuji/Fuji FP-100c Cool 1 -- 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Color/Fuji/Fuji Provia 100 Generic 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Color/Fuji/Fuji Provia 100F 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Color/Fuji/Fuji Provia 400F 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Color/Fuji/Fuji Provia 400X 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Color/Fuji/Fuji Sensia 100 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Color/Fuji/Fuji Superia 100 1 - 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Color/Fuji/Fuji Superia 200 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Color/Fuji/Fuji Superia 200 XPRO 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Color/Fuji/Fuji Superia HG 1600 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Color/Fuji/Fuji Superia Reala 100 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Color/Fuji/Fuji Superia X-Tra 800 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Color/Fuji/Fuji Velvia 100 Generic 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Color/Fuji/Fuji Velvia 50 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Color/Lomography/Lomography Redscale 100 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Color/Lomography/Lomography X-Pro Slide 200 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Color/Agfa/Agfa Precisa 100 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Color/Agfa/Agfa Ultra Color 100 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Color/Agfa/Agfa Vista 200 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Color/Polaroid/Polaroid 669 Cold 1 -- 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Color/Polaroid/Polaroid 690 1 -- 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Color/Polaroid/Polaroid 690 Cold 1 -- 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Color/Polaroid/Polaroid 690 Warm 1 -- 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Color/Polaroid/Polaroid PX-100UV+ Cold 1 -- 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Color/Polaroid/Polaroid PX-680 Cold 1 -- 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Color/Polaroid/Polaroid PX-70 1 -- 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Color/Polaroid/Polaroid PX-70 Cold 1 -- 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Color/Polaroid/Polaroid PX-70 Warm 1 -- 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Color/Polaroid/Polaroid Polachrome 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Color/Kodak/Kodak E-100 GX Ektachrome 100 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Color/Kodak/Kodak Ektachrome 100 VS 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Color/Kodak/Kodak Ektachrome 100 VS Generic 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Color/Kodak/Kodak Ektar 100 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Color/Kodak/Kodak Elite 100 XPRO 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Color/Kodak/Kodak Elite Chrome 200 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Color/Kodak/Kodak Elite Chrome 400 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Color/Kodak/Kodak Elite Color 200 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Color/Kodak/Kodak Elite Color 400 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Color/Kodak/Kodak Elite ExtraColor 100 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Color/Kodak/Kodak Kodachrome 200 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Color/Kodak/Kodak Kodachrome 25 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Color/Kodak/Kodak Kodachrome 64 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Color/Kodak/Kodak Kodachrome 64 Generic 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Color/Kodak/Kodak Portra 160 1 - 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Color/Kodak/Kodak Portra 160 NC 1 - 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Color/Kodak/Kodak Portra 160 VC 1 - 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Color/Kodak/Kodak Portra 400 1 - 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Color/Kodak/Kodak Portra 400 NC 1 - 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Color/Kodak/Kodak Portra 400 UC 1 - 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Color/Kodak/Kodak Portra 400 VC 1 - 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Color/Kodak/Kodak Portra 800 1 - 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Color/CreativePack-1/CrispWarm 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Color/CreativePack-1/CrispWinter 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Color/CreativePack-1/LateSunset 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Color/CreativePack-1/Moonlight 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Color/CreativePack-1/NightFromDay 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Color/CreativePack-1/Smokey 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Color/CreativePack-1/TealMagentaGold 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Black-and-White/Fuji/Fuji FP-3000b 1 -- 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Black-and-White/Fuji/Fuji Neopan Acros 100 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Black-and-White/Ilford/Ilford Delta 100 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Black-and-White/Ilford/Ilford Delta 400 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Black-and-White/Ilford/Ilford FP4 Plus 125 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Black-and-White/Ilford/Ilford HP5 1 - 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Black-and-White/Ilford/Ilford HP5 Plus 400 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Black-and-White/Ilford/Ilford HPS 800 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Black-and-White/Ilford/Ilford Pan F Plus 50 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Black-and-White/Ilford/Ilford XP2 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Black-and-White/Agfa/Agfa APX 100 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Black-and-White/Agfa/Agfa APX 25 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Black-and-White/Polaroid/Polaroid 664 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Black-and-White/Polaroid/Polaroid 665 1 -- 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| clones/MokshC_Film-Emulation-LUTs/Black-and-White/Polaroid/Polaroid 665 Negative 1 - 65x.cube | 65 | 274625 | REJECT (65pt Desktop-Only) |
| … 92 more REJECT entries in the JSON | | | |

Full structured data (every file, SHA256, domains, raw URLs): `opencode_verified_luts.json`


## 6. Live Sub-Job 2 Run (2026-11-09, network ONLINE) — Portal Verification & Airdrop Expansion

### 6.1 Live Portal Downloads — 37/37 candidates HTTP 200, 0 PENDING
- **31 direct `.cube` URLs** → all `PASS (33pt)` (35,937 triplets): Luma Dune ×2, Rodrigo Polo ×2, Luttie ×22, slay ×5.
- **Negative controls rejected as expected:** Luma Dune 65pt ×2, Rodrigo Polo 65pt ×1 → `REJECT (65pt Desktop-Only)` (274,625 triplets).
- **Bransford `apple-log-2.zip`** → `BMSoftDocAppleLog2.cube` PASS (33pt) + `BMSoftDocAppleLog265.cube` REJECT (65pt).
- **Bransford `apple-log.zip`** → `BMSoftDocAppleLog.cube` PASS (33pt) + `BMSoftDocAppleLog65.cube` REJECT (65pt).
- **Fujifilm `x-m5-3d-lut-v100.zip`** → 8/8 F-Log/F-Log2 members PASS (33pt) (official reference; F-Log input → excluded from iPhone bundle).
- All downloads + SHA256s saved under `downloads/verified/`; full triplet counts in `opencode_verified_luts.json`.

### 6.2 `ready_to_airdrop_33pt` Expansion — 28 new 33pt portal LUTs
- `01_Apple_Log_2_iPhone17Pro/` +15 (Luma Dune AL2, Rodrigo Polo AL2 ×2, Bransford AL2, Luttie AL2 ×11) → 25 files
- `02_Apple_Log_iPhone17Pro/` +8 (Luma Dune AL, Bransford AL, Luttie AL ×6) → 10 files
- `03_GuVue_HK_Series_Matches_Rec709_33pt/` +2 (Luttie Rec.709 Cyberpunk Neon, Moody Dark Teal) → 8 files
- `04_Rec709_Film_Stocks_iPhone17_Air_33pt/` +3 (Luttie Kodak 2383 Print, Portra 400, Faded Kodak) → 16 files
- `05_HLG_and_HDR_to_SDR_33pt/` unchanged → 3 files
- **Strictly excluded:** all 5 × 65pt files; slay ×5 (already in bundle, byte-identical); Fujifilm X-M5 F-Log ×8 (no matching iPhone input-space folder).
- Post-copy sweep: every `.cube` in the bundle is 33pt with 35,937 triplets (0 violations). Expansion log: `airdrop_expansion_live.json`.

### 6.3 Re-packed Airdrop ZIP
- `IPHONE17_BLACKMAGIC_VERIFIED_33PT_LUTS.zip` re-built from `ready_to_airdrop_33pt/`: **62 `.cube` files**, `unzip -t` OK, strict 33pt sweep 0 violations.
