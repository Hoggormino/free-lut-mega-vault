# Sub-Agent 1 (`gemini` CLI): HuggingFace Hub (`HfApi`) & GitLab Open-Source `.cube` Harvester

**RULES**:
- Use **ONLY** `Shell`, `ReadFile`, and `WriteFile` (**NEVER** call `GoogleSearch` or `WebFetch`).
- Do **NOT** use `herdr`. Use only standard public APIs (`huggingface_hub`, `requests`) — never bypass any login, paywall, `403`, or CAPTCHA.

## Exact Task
Write and execute `/Users/hoggormino/projects/iPhone17_LUTs_Vault/_tools/harvest_hf_gitlab.py` using `/Users/hoggormino/projects/iPhone17_LUTs_Vault/_tools/venv/bin/python3`:
1. Create `/Users/hoggormino/projects/iPhone17_LUTs_Vault/_incoming_staging/hf_gitlab`.
2. Using `from huggingface_hub import HfApi, hf_hub_download`:
   - Instantiate `api = HfApi()`.
   - Search `api.list_models(search=q, limit=25)`, `api.list_datasets(search=q, limit=25)`, and `api.list_spaces(search=q, limit=25)` for `q` in `["lut", "3dlut", "cube", "film emulation", "color grading", "kodak", "fujifilm", "comfyui lut"]`, plus explicit HuggingFace repos `("space", "Tenofas/ComfyUI")`.
   - Use `repo.id` (the `owner/name` string, **NOT** `_id`!) and call `api.list_repo_files(repo_id=repo.id, repo_type=rtype)` (catching 401/403/gated repos cleanly and skipping them).
   - For every file ending in `.cube` (up to 60 files per repo so huge CV camera-array datasets don't bloat), download via `https://huggingface.co/{prefix}{repo.id}/resolve/main/{urllib.parse.quote(filepath)}` using `requests.get(..., timeout=20)` into `/Users/hoggormino/projects/iPhone17_LUTs_Vault/_incoming_staging/hf_gitlab/{safe_repo}__{basename}`.
3. Query GitLab Public API (`https://gitlab.com/api/v4/projects?search={q}&per_page=20`) for `q` in `["cubeclut", "3dlut", "haldclut", "opencolorio", "color-lut", "film-emulation"]`, inspect `/repository/tree?recursive=true&per_page=100`, and download any `.cube` files into `/Users/hoggormino/projects/iPhone17_LUTs_Vault/_incoming_staging/hf_gitlab/`.
4. Parse `LUT_3D_SIZE` (`17`, `33`, `65`, etc.) of every downloaded `.cube` and write `/Users/hoggormino/projects/iPhone17_LUTs_Vault/_work_logs/subagent1_gemini_report.md`.
