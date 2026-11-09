# Global LUT Dragnet — Sub-Job 1 (`gemini-scout`): Forum, Creator Portal, Cloud-Folder & GitHub Deep Scout

You are **`gemini-scout`**, running in the left pane of Herdr tab **`global-lut-dragnet`** reporting to **Agy (`t19`)**.
**CRITICAL TOOL & COMPLIANCE RULES:**
- Do **NOT** call built-in `GoogleSearch` or `WebFetch` (their internal grounding endpoint hangs). Use ONLY your **Shell (`run_shell_command`)**, **`ReadFile`**, and **`WriteFile`** tools (`curl -sL --max-time 8` and `python3` execute instantaneously).
- **Zero-Bypass Compliance:** Never submit email forms, paywalls, or anti-bot/CAPTCHA/Cloudflare/Altcha challenges, and never use proxies/caches (`r.jina.ai`, Google cache) to bypass 403s. If a domain returns 403 or a gate, classify it `QUARANTINED` immediately and move on.

## Mission Tasks
1. **Audit Newly Surfaced Creator Portals & Hardware Maker Pages (`curl` + `python3`):**
   - Resolve & inspect public HTTP-200 HTML/sitemaps on:
     - **Lutcraft:** `https://lutcraft.com` (hunt for their free `33-point .cube` Apple Log Natural / Strong / Soft download links)
     - **Prolost (Stu Maschwitz):** `https://prolost.com` & `https://proloststore.com/products/applelog` (check if `PL-HERO` / `PL-OG` `33pt` `.cube` is zero-login direct or Shopify-gated)
     - **Fotorgear (iPhone Cinema Hardware):** `https://www.fotorgear.com` (check support/downloads/pages sitemaps for free Apple Log / Blackmagic Camera `.cube` ZIPs)
     - **Beastgrip / Sandmarc / Moment / SmallRig / Freewell:** Check public support/download pages (`beastgrip.com`, `freewellgear.com`, `sandmarc.com`) for any zero-login free Apple Log / Blackmagic Camera `.cube` LUT packs!
     - **iReelz (`ireelz.com`), Cinecolor (`cinecolor.io`), Sebastian Dylag (`sebastiandylag.com`), YPresets (`ypresets.com`), Absoluts (`absoluts-store.com`), iPhoneographers (`iphoneographers.tv`), Stalman (`stalman.com`):** Classify each strictly as `ZERO-LOGIN DIRECT` (with exact `.cube`/`.zip` URL) or `EMAIL/CART/403 GATED`.
2. **Unfurl Public Google Drive Folder (`1FOziyLgHfKimVunhcF5Ws5ZCcvkZcvEp` — Oleg Nikitin Apple Log & Blackmagic Cam Workflow):**
   - Fetch `https://drive.google.com/drive/folders/1FOziyLgHfKimVunhcF5Ws5ZCcvkZcvEp` over plain HTTPS, extract any public file IDs/names inside, download any public `.cube`/`.zip` files via `https://drive.google.com/uc?export=download&id=<FILE_ID>` into `/tmp/lut_scavenger/downloads/oleg_nikitin_gdrive/`, and binary-verify `LUT_3D_SIZE` (`17pt` / `33pt` PASS vs `65pt` REJECT)!
3. **Crawl GitHub Code/Repo API for Remaining Hidden Gems:**
   - Query `https://api.github.com/search/repositories` for `"LUT_3D_SIZE"`, `"Blackmagic" cube`, `"ProRes Log" lut`, `"Rec.709" lut cube`, `"OpenDRT" cube`, `"AgX" lut cube`, and `"HaldCLUT" cube`, listing any uncloned repos with `.cube` files.
4. **Deliverable:**
   - Write your complete findings & binary verification table to `/tmp/lut_scavenger/dragnet_gemini_scout_report.md`.
   - Notify Agy (`t19`):
     ```bash
     export PATH="$HOME/.local/bin:$PATH"
     hc send t19 "gemini-scout finished global-lut-dragnet -> /tmp/lut_scavenger/dragnet_gemini_scout_report.md"
     ```
