# Live Sub-Job 2 (`opencode-extractor`): Live Online Portal Extraction & Binary `.cube` Verification

You are **`opencode-extractor`**, running live inside Herdr (`lut-orchestrator` right pane) reporting to Orchestrator **Agy (`t19`)**.
Network connectivity is now **ONLINE** (earlier run had `network_online: false`, leaving 37 portal candidates `PENDING (offline)`). Do NOT spawn subagents.

## Mission Tasks
1. **Run Live Online Portal Extraction & Grid Verification:**
   - Execute `python3 /tmp/lut_scavenger/verify_cubes.py` now that HTTPS egress is online so all **37 zero-login portal `.cube` and `.zip` candidates** (`Luma Dune`, `Rodrigo Polo`, `Luttie`, `Bransford Media`, `Fujifilm Official X-M5 3D-LUT ZIP`, plus the 3 `65pt` negative controls) are live-downloaded into `/tmp/lut_scavenger/downloads/verified/`, SHA256-hashed, and binary-verified (`LUT_3D_SIZE 17` -> `4,913` triplets PASS; `LUT_3D_SIZE 33` -> `35,937` triplets PASS; `LUT_3D_SIZE 65` -> `274,625` triplets REJECT).
   - Inspect any failed URLs or ZIP members and record exact HTTP status codes and triplet counts in `/tmp/lut_scavenger/opencode_verified_luts.json` and `/tmp/lut_scavenger/opencode_verified_luts.md`.
2. **Expand the Ready-to-AirDrop `33pt` Bundle:**
   - Copy the newly verified `33×33×33` (`PASS (33pt)`) portal `.cube` files from `/tmp/lut_scavenger/downloads/verified/` into the matching folders inside `/tmp/lut_scavenger/ready_to_airdrop_33pt/` (`01_Apple_Log_2_iPhone17Pro`, `02_Apple_Log_iPhone17Pro`, `03_GuVue_HK_Series_Matches_Rec709_33pt`, `04_Rec709_Film_Stocks_iPhone17_Air_33pt`) — strictly excluding any `65pt` files!
   - Re-pack `/tmp/lut_scavenger/IPHONE17_BLACKMAGIC_VERIFIED_33PT_LUTS.zip` from `/tmp/lut_scavenger/ready_to_airdrop_33pt/`.
3. **Notify Orchestrator (`t19`):**
   - Run:
     ```bash
     export PATH="$HOME/.local/bin:$PATH"
     hc send t19 "opencode-extractor completed live online verification -> /tmp/lut_scavenger/opencode_verified_luts.md"
     ```
