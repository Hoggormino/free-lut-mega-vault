# Global LUT Dragnet — Sub-Job 2 (`opencode-extractor`): Wave 2+3 Multi-Repo Binary Verifier, Cloud/CDN Extractor & Master Packager

You are **`opencode-extractor`**, freshly launched in the right pane of Herdr tab **`global-lut-dragnet`**, reporting to **Agy (`t19`)**. Do NOT spawn subagents.

**STRICT COMPLIANCE RULE:** Never submit email forms, paywalls, or CAPTCHA/Cloudflare/Altcha challenges, and NEVER use `r.jina.ai`, caches, or spoofed proxies to bypass 403/anti-bot gates. Any gated or 403 site is immediately marked `QUARANTINED`.

## Mission Tasks
1. **Binary-Verify & Classify All Cloned Wave 2 Repositories (`/tmp/lut_scavenger/clones_wave2/`) + Clone Wave 3 Repos:**
   - Inspect `/tmp/lut_scavenger/clones_wave2/` (already cloned on disk!) AND also shallow-clone (`git clone --depth 1` into `/tmp/lut_scavenger/clones_wave2/` if missing):
     - `https://github.com/apyfz/lutty-ios`
     - `https://github.com/TanaTTV/vibe-engine`
     - `https://github.com/sohan-shingade/fujiLUT`
     - `https://github.com/vecyang1/CineSnap` *(use `--filter=blob:none` or sparse checkout if large, or inspect `.cube` files)*
     - `https://github.com/JakubOchnik/Cube-LUT-Loader`
   - Parse every `.cube` file across `/tmp/lut_scavenger/clones_wave2/` (`LUT_3D_SIZE 17` -> `4,913` triplets PASS; `LUT_3D_SIZE 33` -> `35,937` triplets PASS; `65pt` -> `274,625` triplets REJECT; any other/mismatch -> REJECT).
   - Read each passing repo's `README` and `LICENSE` to determine its **exact input color space** (`Apple Log 2`, `Apple Log`, `Rec. 709 / sRGB`, `V-Log`, `F-Log2`, `HLG`, etc.)!
2. **Download & Binary-Verify Direct Zero-Login Archives:**
   - Download `https://nopixels.net/wp-content/uploads/` / scrape `https://nopixels.net/hlg-to-rec709/` (plain HTTP 200 only) for `nopixels_net_hlg2020_to_rec709_2.0.zip` into `/tmp/lut_scavenger/downloads/nopixels/`, unpack, and check `LUT_3D_SIZE` + triplet count!
   - Also check `/tmp/lut_scavenger/downloads/fujifilm_gfx_eterna55/` (already downloaded: `28` `33Grid` `35,937`-triplet F-Log/F-Log2/F-Log2C `.cube`s) and `/tmp/lut_scavenger/downloads/oleg_nikitin_gdrive/` (if populated).
3. **Expand `/tmp/lut_scavenger/ready_to_airdrop_33pt/` Without Deleting Any Existing Files:**
   - Preserve ALL existing folders (`00_GuVue_Official_Film_Samples_33pt`, `01_Apple_Log_2_iPhone17Pro`, `02_Apple_Log_iPhone17Pro`, `03_GuVue_HK_Series_Matches_Rec709_33pt`, `04_Rec709_Film_Stocks_iPhone17_Air_33pt`, `05_HLG_and_HDR_to_SDR_33pt`)!
   - Route newly verified `17pt`/`33pt` `.cube`s strictly by input space (SHA256-deduplicated):
     - `Apple Log 2` -> `01_Apple_Log_2_iPhone17Pro/`
     - `Apple Log` -> `02_Apple_Log_iPhone17Pro/`
     - `HLG` -> `05_HLG_and_HDR_to_SDR_33pt/`
     - `Rec. 709 / sRGB` calibrated film packs (e.g., `TrondW/glassmeter-film-looks` 30 `srgb-33` film simulations, `joinfiber/derby-film` 7 film stocks, `apyfz/lutty-ios`, etc.) -> `06_Calibrated_Film_Simulations_Rec709_33pt/`
     - *(Keep V-Log / F-Log2 / S-Log3 LUTs OUT of the iPhone folders—or place only in a clearly labeled `99_Bonus_Other_Camera_Logs_33pt_DO_NOT_USE_RAW_ON_IPHONE/` folder if helpful, or document them via raw GitHub URLs only so iPhone users never misapply V-Log/F-Log curves!)*
   - Rebuild `/tmp/lut_scavenger/IPHONE17_BLACKMAGIC_VERIFIED_33PT_LUTS.zip` and verify **100% of `.cube`s in the ZIP are `17pt` or `33pt`**.
4. **Write Report & Notify Orchestrator (`t19`):**
   - Write `/tmp/lut_scavenger/dragnet_opencode_report.md` + `/tmp/lut_scavenger/dragnet_opencode_report.json`.
   - Run:
     ```bash
     export PATH="$HOME/.local/bin:$PATH"
     hc send t19 "opencode-extractor finished global-lut-dragnet -> /tmp/lut_scavenger/dragnet_opencode_report.md"
     ```
