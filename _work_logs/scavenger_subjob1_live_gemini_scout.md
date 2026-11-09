# Live Sub-Job 1 (`gemini-scout`): Deep-Web Search Grounding & iPhone 17 LUT Discovery

You are **`gemini-scout`**, running live inside Herdr (`lut-orchestrator` left pane) reporting to Orchestrator **Agy (`t19`)**.
Network connectivity is now **ONLINE**. Do NOT spawn subagents.

## Mission Tasks
1. **Live Google Search Grounding (`GoogleSearch`):**
   - Run targeted searches for:
     - `site:guvueluts.com` and `"GuVue" LUT "Apple Log"` / `"HK Series"` / `"Film Collection"`
     - `"Apple Log 2" free LUT ".cube" "33" OR "Blackmagic Camera"`
     - `"iPhone 17 Pro" "Apple Log 2" free LUT download`
     - `"Blackmagic Camera" iOS free 33-point ".cube" LUT pack`
2. **Verify Zero-Gate Compliance:**
   - Never submit email forms, paywalls, or CAPTCHA/Altcha gates.
   - Classify every discovered source strictly as `ZERO-LOGIN DIRECT`, `EMAIL/CAPTCHA GATED`, or `PAID`, and flag whether it targets `Apple Log 2` (`iPhone 17 Pro / Pro Max`), `Apple Log` (`iPhone 17 Pro / Pro Max`), `Rec. 709 SDR` (`iPhone 17 / 17 Air`), or `Rec. 2020 HLG` (`iPhone 17 / 17 Air`).
3. **Deliverable:**
   - Write your complete, structured live-grounded findings report to `/tmp/lut_scavenger/gemini_scout_findings.md` (preserving the GuVue `F11–F14` & `HK01–HK06` breakdown plus any newly discovered zero-login `17pt`/`33pt` `.cube` sources).
   - When finished, run via shell tool:
     ```bash
     export PATH="$HOME/.local/bin:$PATH"
     hc send t19 "gemini-scout completed live Sub-Job 1 -> /tmp/lut_scavenger/gemini_scout_findings.md"
     ```
