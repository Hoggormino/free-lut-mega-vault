# Sub-Job 2: Deep Binary Extraction, Open-Directory Dorking, GitHub Code Search & .cube Verification
You are `opencode-extractor`, freshly reopened and reporting to Main Orchestrator **Agy**. Use bash (`curl -sL`, `grep`, `python3`, `jq`, `gh`) to bypass login screens, scrape DOM/JS bundles, crawl GitHub's entire codebase for `.cube` files, unfurl cloud storage links, and verify 3D LUT grid sizes.

Write your complete findings to `/tmp/lut_scavenger/opencode_findings.md`.

## Task 1: GuVue LUTs (`[https://guvueluts.com/](https://guvueluts.com/)`) Deep DOM & Bundle Inspection
- Fetch `[https://guvueluts.com/](https://guvueluts.com/)` and all linked JS/CSS/HTML routes via `curl -sL` or Python to extract the exact download endpoint, form action, or Shopify/CDN asset URL for the **"4 free trial looks"** under the **GuVue Film Collection LUT Pack**, plus any exposed `.cube` or `.zip` previews from the **GuVue HK Series** (*Amber, Pale Green, Harbour Blue, Island Cyan, Avenue Star, Mong Kok*).
- Document the `_709` (Rec. 709) vs. non-suffixed (Apple Log) 33-point `.cube` file structure.

## Task 2: Scrape Direct `.cube` & `.zip` Binaries from Zero-Login Sites
Write a Python or bash scraper to pull the actual `.cube` and `.zip` download `href` URLs directly from:
- `[https://luttie.app/luts/camera/blackmagic](https://luttie.app/luts/camera/blackmagic)`
- `[https://luttie.app/luts/camera/apple-log-2](https://luttie.app/luts/camera/apple-log-2)`
- `[https://lumadune.com/luts/apple-log](https://lumadune.com/luts/apple-log)`
- `[https://rodrigopolo.com/2025/11/04/apple-log-2-to-rec-709-conversion-lut/](https://rodrigopolo.com/2025/11/04/apple-log-2-to-rec-709-conversion-lut/)`
- `[https://bransfordmedia.com/luts/blackmagic-camera-app](https://bransfordmedia.com/luts/blackmagic-camera-app)`
- `[https://fixthephoto.com/blackmagic-luts](https://fixthephoto.com/blackmagic-luts)`
- `[https://filtergrade.com/free-cinematic-luts-video-editing/](https://filtergrade.com/free-cinematic-luts-video-editing/)`

## Task 3: Exhaustive GitHub, GitLab & HuggingFace `.cube` Code Crawl
Use GitHub search API / `gh` / Python scripts to find every public repository hosting `.cube` LUTs across the internet:
- Query terms: `extension:cube "Apple Log"`, `extension:cube "Apple Log 2"`, `extension:cube "2383"`, `extension:cube "3513"`, `extension:cube "Kodak"`, `extension:cube "Fuji"`, `extension:cube "AgX"`, `extension:cube "Halation"`, `extension:cube "Blackmagic"`, `extension:cube "Rec709"`, `extension:cube "Neon"`, `extension:cube "Cineon"`.
- Also inspect known LUT repos (`imnz730/LUTs`, `moritzsalla/LogGrade-macOS`, `stream-labs/obs-studio` LUTs, open-source film emulation repos, and HuggingFace datasets containing `.cube` files).
- Convert every single GitHub file URL into a direct, 1-click `[https://raw.githubusercontent.com/](https://raw.githubusercontent.com/)...` download link.

## Task 4: Reddit JSON API Thread Scraper for Direct Cloud Links
Query Reddit's public `.json` search endpoints via Python/curl (`[https://www.reddit.com/search.json?q=Apple+Log+LUT+drive.google.com+OR+dropbox.com+OR+mega.nz&limit=100](https://www.reddit.com/search.json?q=Apple+Log+LUT+drive.google.com+OR+dropbox.com+OR+mega.nz&limit=100)` with a custom User-Agent) across `r/BlackmagicDesign`, `r/iPhoneography`, `r/colorgrading`, and `r/davinciresolve` to automatically extract every `drive.google.com`, `dropbox.com`, `mega.nz`, `wetransfer.com`, and `github.com` link posted in threads and comments.

## Task 5: Unfurl Redirects & Verify `LUT_3D_SIZE` (17pt / 33pt Mobile Check)
- Unfurl any `bit.ly`, `geni.us`, or `tinyurl` redirects to their final destination URLs.
- Convert Google Drive file links to direct download format (`[https://drive.google.com/uc?export=download&id=](https://drive.google.com/uc?export=download&id=)<FILE_ID>`) and Dropbox links to `?dl=1`.
- For direct `.cube` links, run `curl -sL <url> | head -n 35` to inspect the `LUT_3D_SIZE` header. Flag **17-point (`LUT_3D_SIZE 17`)** and **33-point (`LUT_3D_SIZE 33`)** as `Verified iOS Blackmagic Compatible` and warn if any file is `65` (desktop-only).

Write all extracted direct URLs, Reddit thread cloud links, raw GitHub links, and `LUT_3D_SIZE` verification data to `/tmp/lut_scavenger/opencode_findings.md`.
