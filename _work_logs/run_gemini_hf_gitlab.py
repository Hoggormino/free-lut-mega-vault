import os
import sys
import json
import urllib.request
import urllib.parse
import urllib.error
import concurrent.futures
import base64
import time

DOWNLOAD_DIR = "/Users/hoggormino/projects/iPhone17_LUTs_Vault/_work_logs/hf_gitlab_downloads"
REPORT_PATH = "/Users/hoggormino/projects/iPhone17_LUTs_Vault/_work_logs/gemini_findings.md"

os.makedirs(DOWNLOAD_DIR, exist_ok=True)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*"
}

def http_get_json(url):
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=10) as resp:
            if resp.status == 200:
                return json.loads(resp.read().decode('utf-8', errors='ignore'))
    except Exception as e:
        # print(f"Error fetching JSON {url}: {e}")
        pass
    return None

def http_download(url, dest_path):
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=15) as resp:
            if resp.status == 200:
                content = resp.read()
                with open(dest_path, "wb") as f:
                    f.write(content)
                return True
    except Exception as e:
        # print(f"Error downloading {url}: {e}")
        pass
    return False

def parse_cube_header(file_path):
    size = "Unknown"
    title = "Unknown"
    triplet_count = 0
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()
        
        for line in lines[:35]:
            l = line.strip()
            if l.upper().startswith("LUT_3D_SIZE"):
                parts = l.split()
                if len(parts) > 1:
                    size = parts[1]
            elif l.upper().startswith("TITLE"):
                parts = l.split(" ", 1)
                if len(parts) > 1:
                    title = parts[1].strip('"\'')
        
        # count triplets (lines with 3 floats)
        for line in lines:
            l = line.strip()
            if not l or l.startswith("#") or l.startswith("LUT_") or l.startswith("TITLE") or l.startswith("DOMAIN_"):
                continue
            parts = l.split()
            if len(parts) == 3:
                try:
                    float(parts[0])
                    float(parts[1])
                    float(parts[2])
                    triplet_count += 1
                except ValueError:
                    pass
    except Exception as e:
        pass
    return size, title, triplet_count

def crawl_huggingface():
    queries = ["lut", "cube", "film-lut", "apple-log", "color-grading", "kodak", "fuji", "rec709", "halation"]
    hf_repos = set() # (repo_type, repo_id)
    
    print("Crawling HuggingFace API...")
    for q in queries:
        for rtype in ["models", "datasets", "spaces"]:
            url = f"https://huggingface.co/api/{rtype}?search={urllib.parse.quote(q)}&limit=30"
            data = http_get_json(url)
            if data and isinstance(data, list):
                for item in data:
                    repo_id = item.get("_id") or item.get("id") or item.get("name")
                    if repo_id:
                        hf_repos.add((rtype, repo_id))
            time.sleep(0.1)
    
    print(f"Found {len(hf_repos)} unique HuggingFace repos.")
    
    downloaded_files = []
    inspected_repos = []
    
    def process_hf_repo(rtype, repo_id):
        repo_findings = {"type": rtype, "repo_id": repo_id, "cubes": []}
        # Fetch tree
        # e.g. https://huggingface.co/api/models/{repo_id}/tree/main
        tree_url = f"https://huggingface.co/api/{rtype}/{repo_id}/tree/main"
        tree_data = http_get_json(tree_url)
        
        paths_to_check = []
        if tree_data and isinstance(tree_data, list):
            stack = list(tree_data)
            while stack:
                node = stack.pop()
                path = node.get("path")
                ntype = node.get("type")
                if ntype == "file" and path:
                    if path.lower().endswith(".cube") or path.lower().endswith(".zip"):
                        paths_to_check.append(path)
                elif ntype == "directory" and path:
                    # check if directory name suggests luts or recurse if needed
                    # To avoid deep infinite recursion, let's fetch subdirectory if path matches or if general
                    sub_url = f"https://huggingface.co/api/{rtype}/{repo_id}/tree/main/{urllib.parse.quote(path)}"
                    sub_data = http_get_json(sub_url)
                    if sub_data and isinstance(sub_data, list):
                        for sub_node in sub_data:
                            sub_path = sub_node.get("path")
                            sub_type = sub_node.get("type")
                            if sub_type == "file" and sub_path:
                                if sub_path.lower().endswith(".cube") or sub_path.lower().endswith(".zip"):
                                    paths_to_check.append(sub_path)
                            elif sub_type == "directory" and sub_path:
                                # one level deeper if needed
                                deep_url = f"https://huggingface.co/api/{rtype}/{repo_id}/tree/main/{urllib.parse.quote(sub_path)}"
                                deep_data = http_get_json(deep_url)
                                if deep_data and isinstance(deep_data, list):
                                    for deep_node in deep_data:
                                        deep_path = deep_node.get("path")
                                        if deep_node.get("type") == "file" and deep_path and deep_path.lower().endswith((".cube", ".zip")):
                                            paths_to_check.append(deep_path)
        
        for path in set(paths_to_check):
            if path.lower().endswith(".cube"):
                # resolve URL
                if rtype == "models":
                    resolve_url = f"https://huggingface.co/{repo_id}/resolve/main/{urllib.parse.quote(path)}"
                elif rtype == "datasets":
                    resolve_url = f"https://huggingface.co/datasets/{repo_id}/resolve/main/{urllib.parse.quote(path)}"
                else:
                    resolve_url = f"https://huggingface.co/spaces/{repo_id}/resolve/main/{urllib.parse.quote(path)}"
                
                filename = f"hf_{rtype}_{repo_id.replace('/', '_')}_{os.path.basename(path)}"
                dest = os.path.join(DOWNLOAD_DIR, filename)
                if http_download(resolve_url, dest):
                    size, title, triplets = parse_cube_header(dest)
                    repo_findings["cubes"].append({"path": path, "filename": filename, "size": size, "title": title, "triplets": triplets})
                    downloaded_files.append((filename, size, title, triplets, f"HuggingFace {rtype}/{repo_id}"))
        
        return repo_findings

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(process_hf_repo, rtype, repo_id) for rtype, repo_id in hf_repos]
        for f in concurrent.futures.as_completed(futures):
            res = f.result()
            if res:
                inspected_repos.append(res)
                
    return inspected_repos, downloaded_files

def crawl_gitlab():
    queries = ["cube lut", "film lut", "color grading lut", "apple log", "kodak 2383", "agx lut", "halation lut"]
    gl_projects = []
    
    print("Crawling GitLab API...")
    for q in queries:
        url = f"https://gitlab.com/api/v4/projects?search={urllib.parse.quote(q)}&per_page=20"
        data = http_get_json(url)
        if data and isinstance(data, list):
            for proj in data:
                pid = proj.get("id")
                if pid and pid not in [p.get("id") for p in gl_projects]:
                    gl_projects.append(proj)
        time.sleep(0.1)
        
    print(f"Found {len(gl_projects)} unique GitLab projects.")
    
    downloaded_files = []
    inspected_projects = []
    
    def process_gl_project(proj):
        pid = proj.get("id")
        pname = proj.get("name_with_namespace") or proj.get("path_with_namespace")
        default_branch = proj.get("default_branch") or "main"
        
        proj_findings = {"id": pid, "name": pname, "cubes": []}
        
        tree_url = f"https://gitlab.com/api/v4/projects/{pid}/repository/tree?recursive=true&per_page=100"
        tree_data = http_get_json(tree_url)
        
        if tree_data and isinstance(tree_data, list):
            for node in tree_data:
                path = node.get("path")
                if node.get("type") == "blob" and path and path.lower().endswith(".cube"):
                    encoded_path = urllib.parse.quote(path, safe='')
                    raw_url = f"https://gitlab.com/api/v4/projects/{pid}/repository/files/{encoded_path}/raw?ref={default_branch}"
                    filename = f"gl_{pid}_{os.path.basename(path)}"
                    dest = os.path.join(DOWNLOAD_DIR, filename)
                    if http_download(raw_url, dest):
                        size, title, triplets = parse_cube_header(dest)
                        proj_findings["cubes"].append({"path": path, "filename": filename, "size": size, "title": title, "triplets": triplets})
                        downloaded_files.append((filename, size, title, triplets, f"GitLab {pname}"))
        return proj_findings

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(process_gl_project, proj) for proj in gl_projects]
        for f in concurrent.futures.as_completed(futures):
            res = f.result()
            if res:
                inspected_projects.append(res)
                
    return inspected_projects, downloaded_files

def main():
    print("Starting HuggingFace and GitLab .cube crawl...")
    hf_repos, hf_cubes = crawl_huggingface()
    gl_projs, gl_cubes = crawl_gitlab()
    
    all_cubes = hf_cubes + gl_cubes
    print(f"Total downloaded .cube files: {len(all_cubes)}")
    
    # Generate Markdown Report
    report = []
    report.append("# HuggingFace & GitLab .cube Reconnaissance & Auto-Downloader Report\n")
    report.append(f"**Execution Date:** 2026-11-09\n")
    report.append(f"**Total HuggingFace Repos Inspected:** {len(hf_repos)}")
    report.append(f"**Total GitLab Projects Inspected:** {len(gl_projs)}")
    report.append(f"**Total `.cube` Files Downloaded:** {len(all_cubes)}\n")
    
    report.append("## Downloaded `.cube` Files Summary\n")
    report.append("| Filename | Source | LUT_3D_SIZE | Title | Triplet Count |")
    report.append("|---|---|---|---|---|")
    for filename, size, title, triplets, source in all_cubes:
        report.append(f"| `{filename}` | {source} | `{size}` | {title} | {triplets} |")
        
    report.append("\n## HuggingFace Inspected Repositories\n")
    for r in hf_repos:
        cubes_str = ", ".join([c["path"] for c in r["cubes"]]) if r["cubes"] else "None"
        report.append(f"- **{r['type']}/{r['repo_id']}**: {len(r['cubes'])} .cube files found ({cubes_str})")
        
    report.append("\n## GitLab Inspected Projects\n")
    for p in gl_projs:
        cubes_str = ", ".join([c["path"] for c in p["cubes"]]) if p["cubes"] else "None"
        report.append(f"- **{p['name']} (ID: {p['id']})**: {len(p['cubes'])} .cube files found ({cubes_str})")
        
    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(report))
        
    print(f"Report written to {REPORT_PATH}")

if __name__ == "__main__":
    main()
