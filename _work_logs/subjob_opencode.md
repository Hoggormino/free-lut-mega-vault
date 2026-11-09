# Sub-Job 2 (`opencode` CLI): Deep GitHub Raw `.cube` Tree Crawler & Binary Extractor

**STRICT ZERO-BYPASS COMPLIANCE**: Never submit login/email forms, never solve or bypass CAPTCHAs (`hCaptcha`, `Altcha`, `Turnstile`, `reCAPTCHA`), and never use `r.jina.ai` or caches on `403` pages. Fetch only public HTTP 200 APIs and raw GitHub files. Do NOT use `herdr` or `hc`.

## Mission
Write and execute a multi-threaded Python 3 script `/Users/hoggormino/projects/iPhone17_LUTs_Vault/_work_logs/run_opencode_gh_trees.py` (`concurrent.futures.ThreadPoolExecutor`) that:
1. Creates `/Users/hoggormino/projects/iPhone17_LUTs_Vault/_work_logs/github_wave4_downloads`.
2. Crawls the **Git Trees** (`https://api.github.com/repos/{owner}/{repo}/git/trees/{branch}?recursive=1` or shallow `git clone --depth 1` if rate-limited by GitHub API!) of:
   - Explicit unverified repos from `previous_scrape.md`:
     - `ray-cast/lut`
     - `just-a-child/2383LUT`
     - `lemonadesaltbagel/GR4-LUTSmith`
     - `Sooodx/live-photo-tool`
     - `jfmayeda/FilmFeel`
     - `o-l-l-i/ComfyUI-OlmLUT`
     - `michelerenzullo/LUTify`
     - `yoonsikp/pycubelut`
   - Plus GitHub `/search/repositories` results (`per_page=15`) for new color-science queries:
     - `"Kodak 2383" lut`
     - `"Fuji 3513" lut`
     - `"Halation" lut cube`
     - `"AgX" lut cube`
     - `"Cineon" lut cube`
     - `"Teal Orange" lut cube`
     - `"OpenDRT" cube`
     - `"Blackmagic" "Apple Log" lut`
   *(Skip repos already cloned in `/tmp/lut_scavenger/clones/` and `/tmp/lut_scavenger/clones_wave2/` so you only extract NEW repos!)*
3. Downloads every `.cube` file found in those repositories from `https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{path}` (or copies from shallow clone) into `/Users/hoggormino/projects/iPhone17_LUTs_Vault/_work_logs/github_wave4_downloads/{owner}__{repo}__{filename}`.
4. Inspects `LUT_3D_SIZE` (`17`, `33`, `65`, or non-standard/1D), exact RGB triplet count (`N^3`), `TITLE`, and repository license/input color space.
5. Writes a complete Markdown & JSON summary to:
   - `/Users/hoggormino/projects/iPhone17_LUTs_Vault/_work_logs/opencode_findings.md`
   - `/Users/hoggormino/projects/iPhone17_LUTs_Vault/_work_logs/opencode_findings.json`
