import os, re, json, hashlib, urllib.request, urllib.parse

vault = os.getcwd()
luts_root = os.path.join(vault, "luts")
index_path = os.path.join(vault, "lut_index.json")

catalog = json.load(open(index_path)) if os.path.exists(index_path) else []
seen_sha = {item["sha256"]: True for item in catalog}

token = os.environ.get("GITHUB_TOKEN", "")
headers = {"User-Agent": "LutMegaVaultHarvester/1.0"}
if token:
    headers["Authorization"] = f"Bearer {token}"

queries = ["Apple+Log+2+cube", "Apple+Log+lut+cube", "Kodak+2383+cube", "Fujifilm+lut+cube", "film+emulation+lut+cube"]
added = 0

for q in queries:
    try:
        req = urllib.request.Request(f"https://api.github.com/search/repositories?q={q}&sort=updated&per_page=10", headers=headers)
        repos = json.loads(urllib.request.urlopen(req, timeout=15).read().decode("utf-8", "ignore")).get("items", [])
        for r in repos:
            repo = r["full_name"]
            branch = r.get("default_branch", "main")
            t_req = urllib.request.Request(f"https://api.github.com/repos/{repo}/git/trees/{branch}?recursive=1", headers=headers)
            tree = json.loads(urllib.request.urlopen(t_req, timeout=15).read().decode("utf-8", "ignore")).get("tree", [])
            for node in tree:
                path = node.get("path", "")
                if path.lower().endswith(".cube") and node.get("size", 0) < 15 * 1024 * 1024:
                    raw_url = f"https://raw.githubusercontent.com/{repo}/{branch}/{urllib.parse.quote(path)}"
                    data = urllib.request.urlopen(urllib.request.Request(raw_url, headers=headers), timeout=15).read()
                    sha12 = hashlib.sha256(data).hexdigest()[:12]
                    if sha12 in seen_sha or b"LUT_3D_SIZE" not in data[:3000]:
                        continue
                    text = data.decode("utf-8", "ignore")
                    m = re.search(r"LUT_3D_SIZE\s+(\d+)", text[:3000])
                    grid = int(m.group(1)) if m else 33
                    base = re.sub(r"[^A-Za-z0-9._-]+", "_", f"{repo.replace('/', '__')}__{os.path.basename(path)}")
                    folder = "5_Desktop_Mastering_65pt" if grid >= 64 else "3_Rec709_Creative_Looks"
                    space = "Desktop-65pt" if grid >= 64 else "Rec709-Creative"
                    fname = f"[{space}][Cinematic-Balanced][{grid}pt]_{base}"[:135]
                    if not fname.endswith(".cube"):
                        fname += ".cube"
                    dest = os.path.join(luts_root, folder, fname)
                    os.makedirs(os.path.dirname(dest), exist_ok=True)
                    open(dest, "wb").write(data)
                    seen_sha[sha12] = True
                    added += 1
    except Exception:
        continue

print(f"Weekly harvest complete: +{added} new unique LUTs added.")
