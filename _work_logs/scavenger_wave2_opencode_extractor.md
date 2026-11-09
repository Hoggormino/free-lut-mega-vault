# Wave 2 Mega-Hunt (`opencode-extractor`): Expand Zero-Login `17pt`/`33pt` `.cube` Library to 150+ LUTs

You are **`opencode-extractor`** (`t1h`) reporting to Orchestrator **Agy (`t19`)**. Do NOT spawn subagents.

## Task 1: Clone & Audit 12 Brand-New Public `.cube` Repositories
Clone (`git clone --depth 1`) into `/tmp/lut_scavenger/clones_wave2/` and binary-scan every `.cube` file (`LUT_3D_SIZE 17` -> `4,913` triplets PASS; `LUT_3D_SIZE 33` -> `35,937` triplets PASS; `65pt`/other -> REJECT):
1. `https://github.com/haji-mi/loglook` *(iPhone Apple Log LUTs!)*
2. `https://github.com/moritzsalla/ffgrade` *(iPhone Apple Log LUTs!)*
3. `https://github.com/TrondW/glassmeter-film-looks` *(30 film simulations `.cube`!)*
4. `https://github.com/joinfiber/derby-film` *(7 modelled film stocks `.cube`!)*
5. `https://github.com/cgardev/cameraluts` *(Mathematically calibrated 3D `.cube` camera LUTs!)*
6. `https://github.com/t0saki/lumix-original-looks` *(10 original `33pt` `.cube` looks)*
7. `https://github.com/userle3252352/the-cinema-lut` *(`33pt` cinema `.cube` LUTs)*
8. `https://github.com/userle3252352/dust` *(`33pt` `.cube` LUT)*
9. `https://github.com/HNGSeries/mfilm-canon-film-simulation` *(72 film simulations)*
10. `https://github.com/efriedman-student/filmic-resolve` *(Filmic `.cube` LUTs)*
11. `https://github.com/Moder4te/moderates-film-simulator` *(TDS D-logE characteristic curve film simulations `.cube`)*
12. `https://github.com/sadziu/Fuji-Recipe-Converter` *(Check if any `.cube` files exist)*

## Task 2: Scrape & Binary-Verify New Apple Log / Apple Log 2 Web Portals (Zero-Login ONLY)
Inspect public DOMs (never submit email forms, paywalls, or CAPTCHA/Altcha gates!) and download + binary-verify any direct zero-login `.cube` or `.zip` URLs from:
1. `https://www.cinecolor.io` (search their site/sitemap for free Apple Log / Apple Log 2 / free sample `.cube` downloads)
2. `https://sebastiandylag.com` (check free Apple Log LUT page for direct `.cube`/`.zip` links)
3. `https://ypresets.com` (check free Apple Log 2 LUT page for direct `.cube`/`.zip` links)
4. `https://absoluts-store.com` (check free Blackmagic Camera / Apple Log LUTs)
5. `https://nopixels.net/hlg-to-rec709/` (download `nopixels_net_hlg2020_to_rec709_2.0.zip` if zero-login direct and verify its `.cube` grid size!)

## Task 3: Pack Verified `17pt`/`33pt` LUTs & Report
1. Read `README` / `LICENSE` / headers of every passing repo so you classify input space accurately (`Apple Log 2`, `Apple Log`, `Rec. 709 / sRGB`, `V-Log`, `HLG`, etc.) — **CRITICAL:** Do NOT mix V-Log or S-Log3 LUTs into Apple Log or Rec.709 folders! Only put `Rec. 709 / sRGB` creative LUTs into `04_Rec709_Film_Stocks_iPhone17_Air_33pt/`, `Apple Log 2` into `01_Apple_Log_2_iPhone17Pro/`, `Apple Log` into `02_Apple_Log_iPhone17Pro/`, `HLG` into `05_HLG_and_HDR_to_SDR_33pt/`, and if there are great `33pt` camera-log LUTs (or specialized film packs like GlassMeter / Derby / M-Film Rec.709), organize a clean `06_Wave2_Calibrated_Film_Emulations_Rec709_33pt/` folder inside `/tmp/lut_scavenger/ready_to_airdrop_33pt/`!
2. Do **NOT** delete existing files in `/tmp/lut_scavenger/ready_to_airdrop_33pt/` (especially `00_GuVue_Official_Film_Samples_33pt/`!). Re-pack `/tmp/lut_scavenger/IPHONE17_BLACKMAGIC_VERIFIED_33PT_LUTS.zip` and verify **100% of `.cube`s in the ZIP are `17pt` or `33pt`**.
3. Write `/tmp/lut_scavenger/wave2_verified_luts.md` + `.json`, then run:
   ```bash
   export PATH="$HOME/.local/bin:$PATH"
   hc send t19 "opencode-extractor completed Wave 2 -> /tmp/lut_scavenger/wave2_verified_luts.md"
   ```
