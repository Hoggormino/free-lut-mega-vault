import os
import urllib.parse
import requests
from huggingface_hub import HfApi

STAGING_DIR = "/Users/hoggormino/Projects/iPhone17_LUTs_Vault/_incoming_staging/hf_gitlab"
REPORT_PATH = "/Users/hoggormino/Projects/iPhone17_LUTs_Vault/_work_logs/subagent1_gemini_report.md"

def main():
    os.makedirs(STAGING_DIR, exist_ok=True)
    api = HfApi()

    queries = ["lut", "3dlut", "cube", "film emulation", "color grading", "kodak", "fujifilm", "comfyui lut"]
    
    repos_to_scan = [] # list of tuples: (rtype, repo_id)
    
    # 1. HuggingFace search
    for q in queries:
        print(f"Searching HF models, datasets, spaces for query: {q}")
        try:
            models = list(api.list_models(search=q, limit=25))
            for m in models:
                repos_to_scan.append(("model", m.id))
        except Exception as e:
            print(f"Error searching models for {q}: {e}")

        try:
            datasets = list(api.list_datasets(search=q, limit=25))
            for d in datasets:
                repos_to_scan.append(("dataset", d.id))
        except Exception as e:
            print(f"Error searching datasets for {q}: {e}")

        try:
            spaces = list(api.list_spaces(search=q, limit=25))
            for s in spaces:
                repos_to_scan.append(("space", s.id))
        except Exception as e:
            print(f"Error searching spaces for {q}: {e}")

    # Explicit repo requested
    repos_to_scan.append(("space", "Tenofas/ComfyUI"))

    # Deduplicate repos
    unique_repos = list(set(repos_to_scan))
    print(f"Found {len(unique_repos)} unique HuggingFace repos to inspect.")

    downloaded_files = []

    for rtype, repo_id in unique_repos:
        print(f"Inspecting {rtype} repo: {repo_id}")
        try:
            files = api.list_repo_files(repo_id=repo_id, repo_type=rtype)
        except Exception as e:
            print(f"Skipping {repo_id} ({rtype}) due to error/gated: {e}")
            continue

        cube_files = [f for f in files if f.lower().endswith('.cube')]
        if not cube_files:
            continue

        print(f"Found {len(cube_files)} .cube files in {repo_id}")
        # limit to 60 files per repo
        cube_files = cube_files[:60]

        if rtype == "model":
            prefix = ""
        elif rtype == "dataset":
            prefix = "datasets/"
        elif rtype == "space":
            prefix = "spaces/"
        else:
            prefix = ""

        safe_repo = repo_id.replace("/", "__")
        for filepath in cube_files:
            basename = os.path.basename(filepath)
            dest_name = f"{safe_repo}__{basename}"
            dest_path = os.path.join(STAGING_DIR, dest_name)
            
            encoded_path = "/".join([urllib.parse.quote(part) for part in filepath.split("/")])
            url = f"https://huggingface.co/{prefix}{repo_id}/resolve/main/{encoded_path}"
            
            print(f"Downloading {url} -> {dest_path}")
            try:
                resp = requests.get(url, timeout=20)
                if resp.status_code == 200:
                    with open(dest_path, "wb") as f:
                        f.write(resp.content)
                    downloaded_files.append(dest_path)
                else:
                    print(f"Failed to download {url}: status {resp.status_code}")
            except Exception as e:
                print(f"Exception downloading {url}: {e}")

    # 2. GitLab Public API search
    gitlab_queries = ["cubeclut", "3dlut", "haldclut", "opencolorio", "color-lut", "film-emulation"]
    for gq in gitlab_queries:
        print(f"Searching GitLab for: {gq}")
        try:
            url = f"https://gitlab.com/api/v4/projects?search={gq}&per_page=20"
            resp = requests.get(url, timeout=15)
            if resp.status_code != 200:
                print(f"GitLab API status {resp.status_code} for query {gq}")
                continue
            projects = resp.json()
            for p in projects:
                pid = p.get("id")
                pname = p.get("path_with_namespace", str(pid)).replace("/", "__")
                # fetch repository tree recursive
                tree_url = f"https://gitlab.com/api/v4/projects/{pid}/repository/tree?recursive=true&per_page=100"
                tree_resp = requests.get(tree_url, timeout=15)
                if tree_resp.status_code != 200:
                    continue
                items = tree_resp.json()
                if not isinstance(items, list):
                    continue
                cube_items = [item for item in items if item.get("type") == "blob" and item.get("path", "").lower().endswith(".cube")]
                for item in cube_items[:30]:
                    path = item.get("path")
                    basename = os.path.basename(path)
                    dest_name = f"gitlab__{pname}__{basename}"
                    dest_path = os.path.join(STAGING_DIR, dest_name)
                    
                    raw_url = f"https://gitlab.com/api/v4/projects/{pid}/repository/files/{urllib.parse.quote(path, safe='')}/raw?ref=main"
                    print(f"Downloading GitLab file {path} from project {pid} -> {dest_path}")
                    try:
                        r_file = requests.get(raw_url, timeout=20)
                        if r_file.status_code != 200:
                            # try ref=master
                            raw_url = f"https://gitlab.com/api/v4/projects/{pid}/repository/files/{urllib.parse.quote(path, safe='')}/raw?ref=master"
                            r_file = requests.get(raw_url, timeout=20)
                        if r_file.status_code == 200:
                            with open(dest_path, "wb") as f:
                                f.write(r_file.content)
                            downloaded_files.append(dest_path)
                    except Exception as e:
                        print(f"Error downloading gitlab file {path}: {e}")
        except Exception as e:
            print(f"Error querying GitLab for {gq}: {e}")

    # 3. Parse LUT_3D_SIZE and write report
    report_lines = [
        "# Sub-Agent 1 (Gemini) Harvesting Report",
        "",
        f"Total downloaded `.cube` files: {len(downloaded_files)}",
        "",
        "| File Name | Size (bytes) | Detected LUT_3D_SIZE |",
        "|---|---|---|"
    ]

    all_downloaded = os.listdir(STAGING_DIR)
    for fname in sorted(all_downloaded):
        if not fname.lower().endswith('.cube'):
            continue
        fpath = os.path.join(STAGING_DIR, fname)
        fsize = os.path.getsize(fpath)
        lut_size = "Unknown"
        try:
            with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
                for _ in range(50):
                    line = f.readline()
                    if not line:
                        break
                    if "LUT_3D_SIZE" in line.upper():
                        parts = line.split()
                        if len(parts) > 1:
                            lut_size = parts[1]
                        break
        except Exception:
            pass
        report_lines.append(f"| {fname} | {fsize} | {lut_size} |")

    os.makedirs(os.path.dirname(REPORT_PATH), exist_ok=True)
    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(report_lines))

    print(f"Harvesting complete. Report written to {REPORT_PATH}")

if __name__ == "__main__":
    main()
