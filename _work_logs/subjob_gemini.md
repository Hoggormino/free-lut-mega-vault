# Sub-Job 1 (`gemini` CLI): HuggingFace, GitLab & Public Portal `.cube` Recon + Auto-Downloader

**CRITICAL RULES**:
1. Use **ONLY** `Shell` (`python3` / `curl`), `ReadFile`, and `WriteFile`. **NEVER** call `GoogleSearch` or `WebFetch` (they hang in CLI mode).
2. **STRICT ZERO-BYPASS COMPLIANCE**: Never submit login/email forms, never solve or bypass CAPTCHAs (`hCaptcha`, `Altcha`, `Turnstile`, `reCAPTCHA`), and never use proxies/caches (`r.jina.ai`) on `403` pages. Only fetch plain public `HTTP 200` APIs and raw files.

## Mission
Write and run a multi-threaded Python script `/Users/hoggormino/projects/iPhone17_LUTs_Vault/_work_logs/run_gemini_hf_gitlab.py` (`concurrent.futures.ThreadPoolExecutor`) that:
1. Creates `/Users/hoggormino/projects/iPhone17_LUTs_Vault/_work_logs/hf_gitlab_downloads`.
2. **HuggingFace Hub Public API Crawl**:
   - Query `https://huggingface.co/api/models?search=<q>&limit=30`, `https://huggingface.co/api/datasets?search=<q>&limit=30`, and `https://huggingface.co/api/spaces?search=<q>&limit=30` for `<q>` in `["lut", "cube", "film-lut", "apple-log", "color-grading", "kodak", "fuji", "rec709", "halation"]`.
   - For each returned repo ID, fetch its file tree (`https://huggingface.co/api/{type}/{repo_id}/tree/main`) and recursively check subfolders (`luts`, `LUT`, `assets`, `data`, `presets`) for any `.cube` or `.zip` files!
   - Download every discovered `.cube` file via `https://huggingface.co/{repo_id}/resolve/main/{path}` (or `datasets/{repo_id}/resolve/main/{path}` / `spaces/...`) into `/Users/hoggormino/projects/iPhone17_LUTs_Vault/_work_logs/hf_gitlab_downloads/`.
3. **GitLab Public API Crawl**:
   - Query `https://gitlab.com/api/v4/projects?search=<q>&per_page=20` for `<q>` in `["cube lut", "film lut", "color grading lut", "apple log", "kodak 2383", "agx lut", "halation lut"]`.
   - For each project, query `https://gitlab.com/api/v4/projects/{id}/repository/tree?recursive=true&per_page=100`, find any `.cube` files, and download via `https://gitlab.com/api/v4/projects/{id}/repository/files/{url_encoded_path}/raw?ref={default_branch}` into `/Users/hoggormino/projects/iPhone17_LUTs_Vault/_work_logs/hf_gitlab_downloads/`.
4. **Header Verification**:
   - Inspect the first 35 lines + triplet count of every downloaded `.cube` for `LUT_3D_SIZE` (`17`, `33`, `65`, etc.) and `TITLE`.
5. Write a complete Markdown report to `/Users/hoggormino/projects/iPhone17_LUTs_Vault/_work_logs/gemini_findings.md` with tables of every HuggingFace & GitLab repo inspected and every `.cube` file downloaded + its `LUT_3D_SIZE`.
