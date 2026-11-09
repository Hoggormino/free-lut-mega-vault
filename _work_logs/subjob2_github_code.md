# Sub-Agent 2 (`opencode` CLI): Authenticated `gh api` GitHub Code & Tree `.cube` Indexer

**RULES**:
- Do **NOT** use `herdr` or `hc`.
- Use ONLY official `gh api`, `git`, and Python `requests` against public GitHub repositories — never bypass any login, paywall, `403`, or CAPTCHA.

## Exact Task
Write and execute `/Users/hoggormino/projects/iPhone17_LUTs_Vault/_tools/harvest_gh_code.py` using `/Users/hoggormino/projects/iPhone17_LUTs_Vault/_tools/venv/bin/python3`:
1. Create `/Users/hoggormino/projects/iPhone17_LUTs_Vault/_incoming_staging/github_code_search`.
2. Collect already-cloned repo names in `/tmp/lut_scavenger/clones` and `/tmp/lut_scavenger/clones_wave2` so you don't re-download identical repos.
3. Run `gh api` (`subprocess.run(["gh", "api", endpoint], capture_output=True, text=True)`) for:
   - **GitHub Code Search** (`/search/code?q=...&per_page=30`):
     - `Apple+Log+extension:cube`
     - `AppleLog2+extension:cube`
     - `Kodak+2383+extension:cube`
     - `Fujifilm+3513+extension:cube`
     - `CineStill+800T+extension:cube`
     - `Halation+extension:cube`
     - `OpenDRT+extension:cube`
     - `AgX+extension:cube`
     - `Portra+400+extension:cube`
     - `Blackmagic+Rec709+extension:cube`
   - **Explicit Repositories** (`/repos/{owner}/{repo}/git/trees/{default_branch}?recursive=1`):
     - `ray-cast/lut`
     - `just-a-child/2383LUT`
     - `lemonadesaltbagel/GR4-LUTSmith`
     - `Sooodx/live-photo-tool`
     - `jfmayeda/FilmFeel`
     - `o-l-l-i/ComfyUI-OlmLUT`
     - `michelerenzullo/LUTify`
     - `jedypod/open-display-transform`
4. For every discovered `.cube` item, fetch its raw content via `https://raw.githubusercontent.com/{full_name}/{branch_or_sha}/{urllib.parse.quote(path)}` (for `/search/code` items, parse the `html_url` `https://github.com/{owner}/{repo}/blob/{ref}/{path}` -> `https://raw.githubusercontent.com/{owner}/{repo}/{ref}/{path}`!) and save to `/Users/hoggormino/projects/iPhone17_LUTs_Vault/_incoming_staging/github_code_search/{owner}__{repo}__{basename}` (recording its repo license and source URL in a sidecar JSON `/Users/hoggormino/projects/iPhone17_LUTs_Vault/_work_logs/gh_code_provenance.json`).
5. Inspect `LUT_3D_SIZE` (`17`, `33`, `65`, etc.) and write `/Users/hoggormino/projects/iPhone17_LUTs_Vault/_work_logs/subagent2_opencode_report.md`.
