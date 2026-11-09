#!/usr/bin/env python3
"""
Sub-Agent 2 (opencode CLI): Authenticated `gh api` GitHub Code & Tree .cube Indexer.

Uses ONLY official `gh api`, `git` remote metadata, and Python `requests`
against public GitHub repositories. Never bypasses a login, paywall, 403, or CAPTCHA.

Outputs:
  - Downloaded .cube files into _incoming_staging/github_code_search/
  - Provenance sidecar  _work_logs/gh_code_provenance.json
  - Report              _work_logs/subagent2_opencode_report.md
"""

import json
import os
import re
import subprocess
import sys
import time
import urllib.parse

import requests

BASE = "/Users/hoggormino/projects/iPhone17_LUTs_Vault"
STAGING = os.path.join(BASE, "_incoming_staging", "github_code_search")
PROVENANCE_PATH = os.path.join(BASE, "_work_logs", "gh_code_provenance.json")
REPORT_PATH = os.path.join(BASE, "_work_logs", "subagent2_opencode_report.md")

CLONE_DIRS = [
    "/tmp/lut_scavenger/clones",
    "/tmp/lut_scavenger/clones_wave2",
]

CODE_SEARCH_QUERIES = [
    "Apple Log extension:cube",
    "AppleLog2 extension:cube",
    "Kodak 2383 extension:cube",
    "Fujifilm 3513 extension:cube",
    "CineStill 800T extension:cube",
    "Halation extension:cube",
    "OpenDRT extension:cube",
    "AgX extension:cube",
    "Portra 400 extension:cube",
    "Blackmagic Rec709 extension:cube",
]

EXPLICIT_REPOS = [
    "ray-cast/lut",
    "just-a-child/2383LUT",
    "lemonadesaltbagel/GR4-LUTSmith",
    "Sooodx/live-photo-tool",
    "jfmayeda/FilmFeel",
    "o-l-l-i/ComfyUI-OlmLUT",
    "michelerenzullo/LUTify",
    "jedypod/open-display-transform",
]

SESSION = requests.Session()
SESSION.headers.update({
    "User-Agent": "lut-vault-harvester/1.0 (public GitHub raw fetch)",
    "Accept": "application/vnd.github+json",
})


# --------------------------------------------------------------------------- #
# Helpers
# --------------------------------------------------------------------------- #

def log(msg: str):
    print(msg, flush=True)


def gh_api(endpoint: str, tries: int = 4):
    """Run `gh api <endpoint>`, returning (status_ok, parsed_json_or_None, raw_text)."""
    last_err = ""
    for attempt in range(tries):
        r = subprocess.run(
            ["gh", "api", endpoint],
            capture_output=True, text=True, timeout=120,
        )
        if r.returncode == 0:
            try:
                return True, json.loads(r.stdout), r.stdout
            except json.JSONDecodeError:
                return True, None, r.stdout
        last_err = (r.stderr or r.stdout).strip()
        # Retry on rate limit / server errors, never on 401/403 auth-forbidden
        # (we must not bypass a login wall).
        if r.returncode in (1,):
            lowered = last_err.lower()
            if "rate limit" in lowered or "429" in lowered or "secondary rate" in lowered:
                wait = min(70, 8 * (attempt + 1))
                log(f"    (rate-limited on {endpoint}; sleeping {wait}s)")
                time.sleep(wait)
                continue
            # 403 on search can be a search-specific rate limit
            if "403" in lowered and ("search" in endpoint or "rate limit" in lowered):
                wait = min(70, 8 * (attempt + 1))
                log(f"    (search 403 on {endpoint}; sleeping {wait}s)")
                time.sleep(wait)
                continue
        break
    return False, None, last_err


def collect_cloned_fullnames() -> set:
    """Return a lowercase set of 'owner/repo' full names already cloned."""
    names = set()
    for cd in CLONE_DIRS:
        if not os.path.isdir(cd):
            continue
        for entry in sorted(os.listdir(cd)):
            p = os.path.join(cd, entry)
            if not os.path.isdir(p):
                continue
            cfg = os.path.join(p, ".git", "config")
            full = None
            if os.path.isfile(cfg):
                try:
                    text = open(cfg, encoding="utf-8", errors="replace").read()
                except OSError:
                    text = ""
                m = re.search(
                    r"url\s*=\s*(?:https?://github\.com/|git@github\.com:)"
                    r"([^/\s]+)/([^/\s]+?)(?:\.git)?\s*$",
                    text, re.M,
                )
                if m:
                    owner = m.group(1)
                    # group(2) is already clean: the optional (?:\.git)? group
                    # consumes the ".git" suffix when present. Do NOT use
                    # .rstrip(".git") here — it strips trailing chars from the
                    # set {., g, i, t}, corrupting names like "deep-analog".
                    repo = m.group(2)
                    full = f"{owner}/{repo}"
            if full:
                names.add(full.lower())
            else:
                # Fallback: wave2 dirs are named by repo only; keep repo slug.
                names.add(entry.lower())
    return names


def parse_html_url(html_url: str):
    """https://github.com/{owner}/{repo}/blob/{ref}/{path} -> (owner, repo, ref, path)."""
    m = re.match(r"https://github\.com/([^/]+)/([^/]+)/blob/([^/]+)/(.+)$", html_url)
    if not m:
        return None
    owner, repo, ref, path = m.groups()
    return owner, repo, ref, path


def raw_url_for(owner: str, repo: str, ref: str, path: str) -> str:
    return f"https://raw.githubusercontent.com/{owner}/{repo}/{ref}/{urllib.parse.quote(path, safe='/')}"


def get_repo_meta(full_name: str):
    """Fetch default_branch and license for a repo. Returns dict or None."""
    ok, data, _ = gh_api(f"/repos/{full_name}")
    if not ok or not isinstance(data, dict):
        return None
    lic = data.get("license")
    lic_str = None
    if isinstance(lic, dict):
        lic_str = lic.get("spdx_id") or lic.get("name")
    return {
        "full_name": data.get("full_name"),
        "default_branch": data.get("default_branch"),
        "license": lic_str,
    }


def extract_lut_size(text: str):
    """Return dict with LUT_1D_SIZE / LUT_3D_SIZE (ints or None)."""
    out = {"LUT_1D_SIZE": None, "LUT_3D_SIZE": None}
    for line in text.splitlines():
        s = line.strip()
        if s.startswith("#"):
            # allow leading comment? LUT_3D_SIZE is not commented normally
            pass
        m3 = re.match(r"^LUT_3D_SIZE\s+(\d+)", s, re.I)
        m1 = re.match(r"^LUT_1D_SIZE\s+(\d+)", s, re.I)
        if m3 and out["LUT_3D_SIZE"] is None:
            out["LUT_3D_SIZE"] = int(m3.group(1))
        if m1 and out["LUT_1D_SIZE"] is None:
            out["LUT_1D_SIZE"] = int(m1.group(1))
    return out


# --------------------------------------------------------------------------- #
# Discovery
# --------------------------------------------------------------------------- #

def discover_code_search(cloned: set):
    """Yield candidate dicts from GitHub code search."""
    seen = set()
    for query in CODE_SEARCH_QUERIES:
        q = urllib.parse.quote_plus(query)
        endpoint = f"/search/code?q={q}&per_page=30"
        log(f"[search] {query!r}")
        ok, data, err = gh_api(endpoint)
        if not ok:
            log(f"    ERROR: {err[:200]}")
            continue
        if not isinstance(data, dict):
            log("    ERROR: non-object response")
            continue
        items = data.get("items") or []
        log(f"    total_count={data.get('total_count')} returned={len(items)}")
        for it in items:
            repo = it.get("repository") or {}
            full_name = repo.get("full_name")
            path = it.get("path")
            html_url = it.get("html_url")
            name = it.get("name")
            if not full_name or not path:
                continue
            if not path.lower().endswith(".cube"):
                continue
            parsed = parse_html_url(html_url or "")
            ref = parsed[2] if parsed else repo.get("default_branch")
            if not ref:
                ref = repo.get("default_branch")
            key = (full_name.lower(), path)
            if key in seen:
                continue
            seen.add(key)
            yield {
                "full_name": full_name,
                "path": path,
                "name": name or os.path.basename(path),
                "ref": ref,
                "html_url": html_url,
                "default_branch": repo.get("default_branch"),
                "license": None,
                "source": f"code_search:{query}",
                "already_cloned": full_name.lower() in cloned,
            }
        time.sleep(2)


def discover_explicit_repos(cloned: set):
    """Yield candidate dicts from explicit repository trees."""
    for full_name in EXPLICIT_REPOS:
        log(f"[tree] {full_name}")
        meta = get_repo_meta(full_name)
        default_branch = (meta or {}).get("default_branch") or "main"
        license_str = (meta or {}).get("license")
        ok, data, err = gh_api(
            f"/repos/{full_name}/git/trees/{urllib.parse.quote(default_branch, safe='')}?recursive=1"
        )
        if not ok or not isinstance(data, dict):
            log(f"    ERROR: {err[:200]}")
            continue
        tree = data.get("tree") or []
        count = 0
        for node in tree:
            if node.get("type") != "blob":
                continue
            path = node.get("path", "")
            if not path.lower().endswith(".cube"):
                continue
            count += 1
            yield {
                "full_name": full_name,
                "path": path,
                "name": os.path.basename(path),
                "ref": default_branch,
                "html_url": f"https://github.com/{full_name}/blob/{default_branch}/{urllib.parse.quote(path, safe='/')}",
                "default_branch": default_branch,
                "license": license_str,
                "source": f"explicit_repo:{full_name}",
                "already_cloned": full_name.lower() in cloned,
            }
        log(f"    {count} .cube blob(s) in tree")


# --------------------------------------------------------------------------- #
# Download
# --------------------------------------------------------------------------- #

def fetch_raw(raw_url: str):
    try:
        r = SESSION.get(raw_url, timeout=60)
    except requests.RequestException as e:
        return None, f"request_error: {e}"
    if r.status_code != 200:
        return None, f"http_{r.status_code}"
    return r.content, None


def sanitize_filename(s: str) -> str:
    s = s.replace("/", "__").replace("\\", "__")
    s = re.sub(r"[^A-Za-z0-9._-]", "_", s)
    return s


def main():
    os.makedirs(STAGING, exist_ok=True)

    cloned = collect_cloned_fullnames()
    log(f"Already-cloned repos (case-normalized): {len(cloned)}")

    # Load prior provenance if it exists (merge by source_url).
    existing_records = []
    if os.path.isfile(PROVENANCE_PATH):
        try:
            existing_records = json.load(open(PROVENANCE_PATH, encoding="utf-8"))
            if not isinstance(existing_records, list):
                existing_records = []
        except (OSError, json.JSONDecodeError):
            existing_records = []
    existing_by_raw = {r.get("source_url"): r for r in existing_records if isinstance(r, dict)}

    records = list(existing_records)
    used_targets = set()
    used_keys = set()

    candidates = list(discover_code_search(cloned)) + list(discover_explicit_repos(cloned))
    log(f"Total candidate .cube items: {len(candidates)}")

    stats = {
        "discovered": len(candidates),
        "skipped_cloned": 0,
        "downloaded": 0,
        "failed": 0,
        "duplicate": 0,
    }

    for c in candidates:
        full_name = c["full_name"]
        owner, repo = full_name.split("/", 1)
        path = c["path"]
        ref = c["ref"]
        name = c["name"]

        if c.get("already_cloned"):
            stats["skipped_cloned"] += 1
            log(f"  SKIP (already cloned): {full_name} :: {path}")
            continue

        key = (full_name.lower(), path)
        if key in used_keys:
            stats["duplicate"] += 1
            continue
        used_keys.add(key)

        raw_url = raw_url_for(owner, repo, ref, path)

        # Resolve license if unknown (code search items).
        license_str = c.get("license")
        if license_str is None:
            meta = get_repo_meta(full_name)
            if meta:
                license_str = meta.get("license")
                if meta.get("default_branch"):
                    c["default_branch"] = meta["default_branch"]

        content, err = fetch_raw(raw_url)
        if content is None:
            stats["failed"] += 1
            log(f"  FAIL {full_name} :: {path} -> {err}")
            records.append({
                "full_name": full_name,
                "path": path,
                "name": name,
                "source_url": raw_url,
                "html_url": c.get("html_url"),
                "license": license_str,
                "source": c["source"],
                "status": "failed",
                "error": err,
            })
            continue

        text = content.decode("utf-8", errors="replace")
        sizes = extract_lut_size(text)

        base = sanitize_filename(f"{owner}__{repo}__{name}")
        target = os.path.join(STAGING, base)
        if target in used_targets or os.path.exists(target):
            stem, ext = os.path.splitext(base)
            n = 2
            while True:
                target = os.path.join(STAGING, f"{stem}_{n}{ext}")
                if target not in used_targets and not os.path.exists(target):
                    break
                n += 1
        used_targets.add(target)

        with open(target, "wb") as f:
            f.write(content)

        stats["downloaded"] += 1
        log(f"  OK  {full_name} :: {path}  LUT_3D_SIZE={sizes['LUT_3D_SIZE']}")

        rec = {
            "full_name": full_name,
            "path": path,
            "name": name,
            "local_file": os.path.relpath(target, BASE),
            "source_url": raw_url,
            "html_url": c.get("html_url"),
            "license": license_str,
            "default_branch": c.get("default_branch"),
            "source": c["source"],
            "status": "downloaded",
            "LUT_1D_SIZE": sizes["LUT_1D_SIZE"],
            "LUT_3D_SIZE": sizes["LUT_3D_SIZE"],
        }
        records.append(rec)

    with open(PROVENANCE_PATH, "w", encoding="utf-8") as f:
        json.dump(records, f, indent=2, ensure_ascii=False)

    write_report(records, stats, cloned)

    log(f"\nDone. downloaded={stats['downloaded']} failed={stats['failed']} "
        f"skipped_cloned={stats['skipped_cloned']} duplicate={stats['duplicate']}")
    log(f"Provenance -> {PROVENANCE_PATH}")
    log(f"Report     -> {REPORT_PATH}")


def write_report(records, stats, cloned):
    downloaded = [r for r in records if r.get("status") == "downloaded"]
    failed = [r for r in records if r.get("status") == "failed"]

    size_buckets = {}
    lic_counts = {}
    repo_counts = {}
    for r in downloaded:
        s = r.get("LUT_3D_SIZE")
        size_buckets[s] = size_buckets.get(s, 0) + 1
        lic = r.get("license") or "(unknown)"
        lic_counts[lic] = lic_counts.get(lic, 0) + 1
        repo_counts[r["full_name"]] = repo_counts.get(r["full_name"], 0) + 1

    lines = []
    lines.append("# Sub-Agent 2 (`opencode` CLI): GitHub Code & Tree `.cube` Index — Report")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(f"- Candidate `.cube` items discovered: **{stats['discovered']}**")
    lines.append(f"- Downloaded: **{stats['downloaded']}**")
    lines.append(f"- Failed: **{stats['failed']}**")
    lines.append(f"- Skipped (already-cloned repo): **{stats['skipped_cloned']}**")
    lines.append(f"- Duplicate (same repo+path): **{stats['duplicate']}**")
    lines.append(f"- Already-cloned repos known at start: **{len(cloned)}**")
    lines.append("")

    lines.append("## LUT_3D_SIZE distribution (downloaded)")
    lines.append("")
    lines.append("| LUT_3D_SIZE | Count |")
    lines.append("|---|---|")
    for s in sorted(size_buckets, key=lambda x: (x is None, x or 0)):
        label = "n/a" if s is None else str(s)
        lines.append(f"| {label} | {size_buckets[s]} |")
    lines.append("")

    lines.append("## License distribution (downloaded)")
    lines.append("")
    lines.append("| License | Count |")
    lines.append("|---|---|")
    for lic in sorted(lic_counts, key=lambda x: -lic_counts[x]):
        lines.append(f"| {lic} | {lic_counts[lic]} |")
    lines.append("")

    lines.append("## Downloaded files")
    lines.append("")
    if downloaded:
        lines.append("| Repo | Path | LUT_3D_SIZE | License | Source |")
        lines.append("|---|---|---|---|---|")
        for r in sorted(downloaded, key=lambda x: (x["full_name"].lower(), x["path"])):
            lines.append(
                f"| `{r['full_name']}` | `{r['path']}` | "
                f"{r.get('LUT_3D_SIZE')} | {r.get('license') or '-'} | "
                f"{r['source']} |"
            )
    else:
        lines.append("_(none)_")
    lines.append("")

    if failed:
        lines.append("## Failures (NOT bypassed — logged only)")
        lines.append("")
        lines.append("| Repo | Path | Error |")
        lines.append("|---|---|---|")
        for r in failed:
            lines.append(f"| `{r['full_name']}` | `{r['path']}` | {r.get('error')} |")
        lines.append("")

    lines.append("## Already-cloned repos (skipped as duplicates)")
    lines.append("")
    lines.append(f"```\n" + "\n".join(sorted(cloned)) + "\n```\n")

    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


if __name__ == "__main__":
    main()
