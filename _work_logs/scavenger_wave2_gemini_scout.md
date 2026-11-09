# Wave 2 Deep Hunt (`gemini-scout`): Reddit Communities, Official Camera `33pt` Packs & More GitHub `.cube`s

You are **`gemini-scout`**, running in the left pane of `LUTs / lut-orchestrator` reporting to **Agy (`t19`)**.
**IMPORTANT TOOL RULE:** Do **NOT** call the built-in `GoogleSearch` or `WebFetch` tools (their internal grounding endpoint hangs). Instead, use ONLY your **Shell (`run_shell_command`)**, **`ReadFile`**, and **`WriteFile`** tools (`curl -sL --max-time 8` and `python3` work instantaneously!).

## Mission Tasks
1. **Mine Public Reddit Threads (`curl` + `python3` against JSON endpoints):**
   - Query public Reddit search JSON (`User-Agent: lut-scout/1.0`):
     - `https://www.reddit.com/r/BlackmagicDesign/search.json?q=Apple+Log+free+LUT&restrict_sr=1&limit=25`
     - `https://www.reddit.com/r/colorgrading/search.json?q=Apple+Log+free+LUT&restrict_sr=1&limit=25`
     - `https://www.reddit.com/r/iPhoneography/search.json?q=Apple+Log+LUT&restrict_sr=1&limit=25`
     - `https://www.reddit.com/r/Lumix/search.json?q=free+.cube+LUT+33&restrict_sr=1&limit=25`
   - Extract any direct Google Drive, Dropbox, GitHub, Gumroad `$0`, or creator website links shared in posts/descriptions (never bypass login/CAPTCHA gates).
2. **Download & Binary-Check Official Fujifilm GFX ETERNA 55 `33grid` `.cube` Pack:**
   - Download `https://dl.fujifilm-x.com/lut/gfx-eterna-55-3d-lut-v100.zip` into `/tmp/lut_scavenger/downloads/fujifilm_gfx_eterna55/` and inspect every `.cube` inside (`LUT_3D_SIZE` and triplet count — separate `33grid` `35,937`-triplet mobile PASS files from `65grid` desktop REJECT files!).
3. **Mine Additional GitHub `.cube` Repositories via GitHub API:**
   - Query `https://api.github.com/search/repositories` for `"kodak" lut cube`, `"fuji" lut cube`, `"halation" lut cube`, `"bleach bypass" lut cube`, `"teal orange" lut cube`, and `"iphone" lut cube` (excluding repos already in `/tmp/lut_scavenger/clones/` and `/tmp/lut_scavenger/clones_wave2/`).
4. **Deliverable:**
   - Write your complete Wave 2 discovery & binary-verification table to `/tmp/lut_scavenger/wave2_gemini_findings.md`.
   - Notify Agy (`t19`):
     ```bash
     export PATH="$HOME/.local/bin:$PATH"
     hc send t19 "gemini-scout completed Wave 2 -> /tmp/lut_scavenger/wave2_gemini_findings.md"
     ```
