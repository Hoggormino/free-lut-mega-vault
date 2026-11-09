#!/usr/bin/env python3
"""
Agy Master 3D LUT Vault Consolidator, Color-Science Auto-Labeler & SHA-256 Deduplicator
Consolidates all LUTs from ~/Downloads, migrated ~/Desktop, /tmp/lut_scavenger,
and newly harvested HuggingFace, GitLab, GitHub Code Search & Public Portals into:
  /Users/hoggormino/projects/iPhone17_LUTs_Vault/
    1_Apple_Log_2_iPhone17Pro/
    2_Apple_Log_Original/
    3_Rec709_Base_iPhone17/
    4_GuVue_and_HK_Neon_Looks/
    5_GitHub_and_Community_Packs/
    6_Desktop_Only_65pt/
"""
import hashlib
import json
import os
import re
import shutil
import zipfile

VAULT = "/Users/hoggormino/projects/iPhone17_LUTs_Vault"

FOLDERS = [
    "1_Apple_Log_2_iPhone17Pro",
    "2_Apple_Log_Original",
    "3_Rec709_Base_iPhone17",
    "4_GuVue_and_HK_Neon_Looks",
    "5_GitHub_and_Community_Packs",
    "6_Desktop_Only_65pt",
]

NUM_RE = re.compile(
    r"^\s*([-+]?(?:\d+\.?\d*|\.\d+)(?:[eE][-+]?\d+)?)\s+"
    r"([-+]?(?:\d+\.?\d*|\.\d+)(?:[eE][-+]?\d+)?)\s+"
    r"([-+]?(?:\d+\.?\d*|\.\d+)(?:[eE][-+]?\d+)?)\s*$"
)


def parse_and_profile_cube(data: bytes):
    text = data.decode("utf-8", errors="replace")
    lut_3d_size = None
    lut_1d_size = None
    title = ""
    comments = []
    rows = []

    for raw in text.splitlines():
        s = raw.strip()
        if not s:
            continue
        if s.startswith("#"):
            comments.append(s)
            continue
        u = s.upper()
        if u.startswith("TITLE"):
            parts = s.split(None, 1)
            title = parts[1].strip().strip('"') if len(parts) > 1 else ""
            continue
        if u.startswith("LUT_3D_SIZE"):
            parts = s.split()
            if len(parts) >= 2 and parts[1].isdigit():
                lut_3d_size = int(parts[1])
            continue
        if u.startswith("LUT_1D_SIZE"):
            parts = s.split()
            if len(parts) >= 2 and parts[1].isdigit():
                lut_1d_size = int(parts[1])
            continue
        if u.startswith(("DOMAIN_MIN", "DOMAIN_MAX", "LUT_3D_INPUT_RANGE", "LUT_1D_INPUT_RANGE")):
            continue
        m = NUM_RE.match(s)
        if m:
            rows.append((float(m.group(1)), float(m.group(2)), float(m.group(3))))

    triplets = len(rows)
    if lut_1d_size is not None or lut_3d_size is None or triplets != lut_3d_size ** 3:
        return {
            "valid_3d": False,
            "lut_3d_size": lut_3d_size,
            "lut_1d_size": lut_1d_size,
            "triplets": triplets,
            "title": title,
            "comments": comments[:6],
        }

    # Sample key 3D lattice coordinates (R varies fastest, then G, then B in .cube spec)
    n = lut_3d_size

    def sample(ri, gi, bi):
        idx = ri + gi * n + bi * n * n
        return rows[idx]

    blk = sample(0, 0, 0)
    shd = sample(n // 5, n // 5, n // 5)
    mid = sample(n // 2, n // 2, n // 2)
    hi = sample((n * 4) // 5, (n * 4) // 5, (n * 4) // 5)
    red_pt = sample((n * 3) // 4, n // 4, n // 4)

    # Check monochrome: saturated red input maps to R≈G≈B
    is_mono = (max(red_pt) - min(red_pt)) < 0.035
    blk_luma = 0.2126 * blk[0] + 0.7152 * blk[1] + 0.0722 * blk[2]
    is_matte = blk_luma > 0.025

    shd_rb = shd[0] - shd[2]
    mid_rb = mid[0] - mid[2]
    mid_g_bias = mid[1] - 0.5 * (mid[0] + mid[2])

    if is_mono:
        style = "Monochrome-BW"
    elif shd_rb < -0.025 and hi[0] - hi[2] > 0.02:
        style = "Teal-Orange"
    elif mid_rb > 0.035:
        style = "Warm-Amber"
    elif mid_rb < -0.03:
        style = "Cool-Cyan"
    elif mid_g_bias > 0.02:
        style = "Jade-Editorial"
    elif is_matte:
        style = "Matte-Film"
    else:
        style = "Natural-Cinema"

    return {
        "valid_3d": True,
        "lut_3d_size": lut_3d_size,
        "lut_1d_size": None,
        "triplets": triplets,
        "title": title,
        "comments": comments[:6],
        "visual_style": style,
    }


def sanitize_slug(text: str) -> str:
    s = re.sub(r"\.cube$", "", text, flags=re.I)
    s = s.replace("&", "And")
    s = re.sub(r"[^A-Za-z0-9._-]+", "_", s)
    s = re.sub(r"_+", "_", s).strip("._-")
    return s[:95] or "LUT"


def is_commercial_third_party(info: dict, src_path: str) -> bool:
    blob = (" ".join(info.get("comments", [])) + " " + (info.get("title") or "") + " " + src_path).lower()
    # Filter out stray commercial third-party LUTs accidentally nested in user community zips (e.g. VisionColor ImpulZ)
    if "vision-color.com" in blob or "visioncolor" in blob:
        return True
    # Filter out raw computer-vision multi-camera rig matrices (e.g., danceNet3D camera01..camera20)
    if "dancenet3d" in blob or re.search(r"cam(?:era)?_?\d{2}", os.path.basename(src_path).lower()):
        return True
    # Filter out parser unit-test fixtures
    if os.path.basename(src_path).lower() in ("17p_cmp.cube", "identity.cube", "test.cube"):
        return True
    return False


def detect_color_space_and_bucket(src_path: str, info: dict):
    p_low = src_path.lower()
    fn = os.path.basename(src_path)
    fn_low = fn.lower()
    hdr_low = (" ".join(info.get("comments", [])) + " " + (info.get("title") or "")).lower()
    combined = p_low + " " + hdr_low
    sz = info["lut_3d_size"]

    # Reject / quarantine non-iPhone camera logs (S-Log, V-Log, raw F-Log without Apple Log input, C-Log, LogC, Gen5 BMD Film)
    is_apple_log2 = any(k in combined for k in (
        "apple log 2", "apple_log_2", "applelog2", "01_apple_log_2", "1_apple_log_2", "01_applelog2"
    ))
    is_apple_log1 = (not is_apple_log2) and any(k in combined for k in (
        "apple log", "apple_log", "applelog", "02_apple_log", "2_apple_log", "loggrade", "loglook", "theonelut_iphone"
    ))

    # Non-iPhone camera logs check (only if NOT explicitly an Apple Log -> X LUT!)
    if not (is_apple_log2 or is_apple_log1):
        non_iphone_markers = [
            "slog2", "slog3", "s-log2", "s-log3", "sgamut", "cine4",
            "v-log", "vlog", "f-log", "flog", "fgamut",
            "canonlog", "c-log", "logc", "arri log", "n-log", "d-log", "dlog",
            "blackmagic-film-gen5", "gen5", "bmdfilm", "davinci wide gamut", "acescct", "acescc", "cineon"
        ]
        if any(m in combined for m in non_iphone_markers):
            # Allow Blackmagic Gen5 or desktop 65pt LUTs into 6_Desktop_Only_65pt ONLY if 65pt desktop reference
            if sz == 65 and ("apple" in combined or "gen5" in combined):
                return ("BMD_Gen5_Desktop", "6_Desktop_Only_65pt")
            return ("Non_iPhone_Camera_Log", None)

    # Desktop-only grids (65pt or 64pt HaldCLUT)
    if sz in (64, 65):
        if is_apple_log2:
            return ("AppleLog2", "6_Desktop_Only_65pt")
        if is_apple_log1:
            return ("AppleLog", "6_Desktop_Only_65pt")
        if "hlg" in combined or "hdr" in combined or "2020" in combined:
            return ("HLG_BT2020", "6_Desktop_Only_65pt")
        return ("Rec709", "6_Desktop_Only_65pt")

    # Mobile-compatible grids ONLY: 17pt and 33pt! (Reject 13pt, 25pt, etc. from mobile pack)
    if sz not in (17, 33):
        return (f"NonStandard_{sz}pt", None)

    # Priority Bucket 4: GuVue Official & HK Neon Looks
    if "guvue" in p_low or "03_guvue_hk" in p_low or "4_guvue" in p_low:
        cspace = "AppleLog2" if is_apple_log2 else ("AppleLog" if is_apple_log1 else "Rec709")
        return (cspace, "4_GuVue_and_HK_Neon_Looks")

    # Bucket 1: Apple Log 2 (iPhone 17 Pro / Pro Max)
    if is_apple_log2:
        return ("AppleLog2", "1_Apple_Log_2_iPhone17Pro")

    # Bucket 2: Apple Log Original (iPhone 17 Pro / 15-16 Pro)
    if is_apple_log1:
        return ("AppleLog", "2_Apple_Log_Original")

    # HLG / HDR-to-SDR
    if any(k in combined for k in ("hlg", "hdr-to-sdr", "hdr_to_sdr", "rec2020")):
        return ("HLG_HDR", "3_Rec709_Base_iPhone17")

    # Bucket 3 vs Bucket 5 for Rec.709 / sRGB mobile LUTs:
    # Put core Luttie Rec.709, slaycamera, FotorGear Charmera/ShunjiIwai, and imnz730 2383/3513 prints in 3_Rec709_Base_iPhone17;
    # Put large open-source calibrated repositories (Chromasmith, GlassMeter, Derby, KodakCC0, LUMIX, Cinema-LUT, HF/GitLab/GHCode, IWLTBAP 33pt) in 5_GitHub_and_Community_Packs!
    if any(k in p_low for k in (
        "chroma-app", "chroma_", "glassmeter", "derby", "haldclut-cube-files", "kodakcc0",
        "06_calibrated", "06_wave2", "lumix", "cinema-lut", "the cinema", "the dust",
        "hf_gitlab", "github_code_search", "portal_downloads"
    )):
        return ("Rec709", "5_GitHub_and_Community_Packs")

    return ("Rec709", "3_Rec709_Base_iPhone17")


def infer_pack_tag(src_path: str) -> str:
    p = src_path.lower()
    fn = os.path.basename(src_path)
    if "guvue" in p:
        return "GuVue"
    if "03_guvue_hk" in p:
        return "HKNeon"
    if "fotorgear" in p:
        return "FotorGear"
    if "lumadune" in p or "applelog2torec709-v1.0" in p or "applelogtorec709-v1.0-" in p:
        return "LumaDune"
    if "rodrigopolo" in p or "_grid.cube" in p:
        return "RodrigoPolo"
    if "bransford" in p or fn.startswith("BM"):
        return "Bransford"
    if "raycal" in p:
        return "Raycal"
    if "joey-lj" in p or "fuji-" in fn.lower():
        return "FujiGFX"
    if "luttie" in p:
        return "Luttie"
    if "loglook" in p:
        return "LogLook"
    if "loggrade" in p:
        return "LogGrade"
    if "cinesnap" in p or "theonelut" in p:
        return "TheOneLUT"
    if "slay" in p:
        return "SlayCam"
    if "chroma-app" in p or fn.startswith("Chroma_"):
        return "Chromasmith"
    if "glassmeter" in p:
        return "GlassMeter"
    if "derby" in p:
        return "DerbyFilm"
    if "haldclut-cube-files" in p or fn.startswith("KodakCC0_"):
        return "KodakCC0"
    if "imnz730" in p or "2383" in fn or "3513" in fn:
        return "CinemaPrint"
    if "hdr-to-sdr" in p:
        return "HDRtoSDR"
    if "lumix" in p:
        return "LumixStyle"
    if "iwltbap" in p:
        return "IWLTBAP"
    if "mokshc" in p or "film-emulation-luts" in p:
        return "FilmEmulation65"
    if "nopixels" in p:
        return "NoPixels"
    if "byronvini" in p:
        return "Byronvini"
    if "hf_gitlab" in p:
        return fn.split("__")[0][:24] if "__" in fn else "HuggingFace"
    if "github_code_search" in p:
        parts = fn.split("__")
        return parts[1][:24] if len(parts) >= 3 else "GitHubOSS"
    return "Community"


def collect_candidate_paths():
    """Gather all candidate .cube paths in priority order (Official GuVue -> Curated Mobile -> Downloads -> Staging -> Clones)."""
    ordered_roots = [
        # 1. Official GuVue free sample pack from user's ~/Downloads
        "/tmp/lut_scavenger/downloads/user_downloads",
        "/tmp/lut_scavenger/ready_to_airdrop_33pt/00_GuVue_Official_Film_Samples_33pt",
        "/tmp/lut_scavenger/ready_to_airdrop_33pt/03_GuVue_HK_Series_Matches_Rec709_33pt",
        # 2. Existing migrated vault folders (from ~/Desktop/iPhone17_LUTs_Pack)
        os.path.join(VAULT, "1_Apple_Log_2_iPhone17Pro"),
        os.path.join(VAULT, "2_Apple_Log_Original"),
        os.path.join(VAULT, "3_Rec709_Base_iPhone17"),
        os.path.join(VAULT, "4_GuVue_and_HK_Neon_Looks"),
        os.path.join(VAULT, "5_GitHub_and_Community_Packs"),
        os.path.join(VAULT, "6_Desktop_Only_65pt"),
        # 3. User's ~/Downloads standalone .cube files
        os.path.expanduser("~/Downloads"),
        # 4. Curated /tmp/lut_scavenger folders & FotorGear Google Drive packs
        "/tmp/lut_scavenger/downloads/fotorgear_folders",
        "/tmp/lut_scavenger/ready_to_airdrop_33pt/01_Apple_Log_2_iPhone17Pro",
        "/tmp/lut_scavenger/ready_to_airdrop_33pt/02_Apple_Log_iPhone17Pro",
        "/tmp/lut_scavenger/ready_to_airdrop_33pt/04_Rec709_Film_Stocks_iPhone17_Air_33pt",
        "/tmp/lut_scavenger/ready_to_airdrop_33pt/05_HLG_and_HDR_to_SDR_33pt",
        "/tmp/lut_scavenger/ready_to_airdrop_33pt/06_Wave2_Calibrated_Film_Emulations_Rec709_33pt",
        "/tmp/lut_scavenger/ready_to_airdrop_33pt/06_Calibrated_Film_Emulations_Rec709_33pt",
        "/tmp/lut_scavenger/downloads/verified",
        # 5. Newly staged Sub-Agent 1 (HF/GitLab), Sub-Agent 2 (gh api Code Search), Portal Downloads (IWLTBAP), & 65pt refs
        os.path.join(VAULT, "_incoming_staging/portal_65pt"),
        os.path.join(VAULT, "_incoming_staging/github_code_search"),
        os.path.join(VAULT, "_incoming_staging/hf_gitlab"),
        os.path.join(VAULT, "_work_logs/portal_downloads"),
        # 6. All GitHub clones & extra downloads in /tmp/lut_scavenger
        "/tmp/lut_scavenger/downloads/fotorgear",
        "/tmp/lut_scavenger/downloads/byronvini",
        "/tmp/lut_scavenger/downloads/oleg_nikitin_gdrive",
        "/tmp/lut_scavenger/clones",
        "/tmp/lut_scavenger/clones_wave2",
    ]

    candidates = []
    for r in ordered_roots:
        if not os.path.exists(r):
            continue
        if r == os.path.expanduser("~/Downloads"):
            # Only top-level .cube files + GuVue folder in ~/Downloads so we don't scan unrelated user folders
            for fn in sorted(os.listdir(r)):
                full = os.path.join(r, fn)
                if os.path.isfile(full) and fn.lower().endswith(".cube") and not fn.startswith("._"):
                    candidates.append(full)
            continue
        for root, _, files in os.walk(r):
            for fn in sorted(files):
                if fn.lower().endswith(".cube") and not fn.startswith("._"):
                    candidates.append(os.path.join(root, fn))
    return candidates


def main():
    # First snapshot existing .cube files in VAULT/1_..6_ into a temporary buffer so we can cleanly rebuild 1_..6_
    snap_dir = os.path.join(VAULT, "_incoming_staging/_vault_pre_snapshot")
    if os.path.exists(snap_dir):
        shutil.rmtree(snap_dir)
    os.makedirs(snap_dir, exist_ok=True)

    for fld in FOLDERS:
        fp = os.path.join(VAULT, fld)
        os.makedirs(fp, exist_ok=True)
        dst_sub = os.path.join(snap_dir, fld)
        os.makedirs(dst_sub, exist_ok=True)
        for root, _, files in os.walk(fp):
            for fn in files:
                full = os.path.join(root, fn)
                if fn.lower().endswith(".cube"):
                    shutil.copy2(full, os.path.join(dst_sub, fn))
                elif fn.lower().endswith(".zip"):
                    # Move raw .zip bundles from 5_ into _work_logs/archived_zips so 1_..6_ contain clean ready-to-use .cube files!
                    zdir = os.path.join(VAULT, "_work_logs/archived_zips")
                    os.makedirs(zdir, exist_ok=True)
                    shutil.move(full, os.path.join(zdir, fn))

    # Gather all candidates (replacing VAULT/1_..6_ references with snap_dir/1_..6_)
    raw_candidates = collect_candidate_paths()
    candidates = []
    for c in raw_candidates:
        replaced = False
        for fld in FOLDERS:
            prefix = os.path.join(VAULT, fld) + os.sep
            if c.startswith(prefix):
                candidates.append(os.path.join(snap_dir, fld, os.path.basename(c)))
                replaced = True
                break
        if not replaced:
            candidates.append(c)

    # Clear 1_..6_ cleanly before writing deduplicated, auto-labeled .cube files
    for fld in FOLDERS:
        fp = os.path.join(VAULT, fld)
        shutil.rmtree(fp)
        os.makedirs(fp, exist_ok=True)

    # Copy Official GuVue PDF Guide into 4_GuVue_and_HK_Neon_Looks
    guvue_pdf = "/tmp/lut_scavenger/downloads/user_downloads/GuVue_Film_Collection_4_Free_Sample_Looks_EN/GuVue_Film_Collection_Illustrated_Guide_EN.pdf"
    if os.path.isfile(guvue_pdf):
        shutil.copy2(guvue_pdf, os.path.join(VAULT, "4_GuVue_and_HK_Neon_Looks/GuVue_Film_Collection_Illustrated_Guide_EN.pdf"))

    seen_sha256 = {}
    duplicate_count = 0
    quarantined_stats = {
        "non_iphone_camera_log": 0,
        "non_standard_grid": 0,
        "invalid_or_1d": 0,
        "commercial_or_fixture": 0,
    }
    accepted = []

    for src in candidates:
        if not os.path.isfile(src):
            continue
        try:
            with open(src, "rb") as f:
                data = f.read()
        except Exception:
            continue

        digest = hashlib.sha256(data).hexdigest()
        if digest in seen_sha256:
            duplicate_count += 1
            continue

        info = parse_and_profile_cube(data)
        if not info["valid_3d"]:
            quarantined_stats["invalid_or_1d"] += 1
            continue

        if is_commercial_third_party(info, src):
            quarantined_stats["commercial_or_fixture"] += 1
            continue

        cspace, bucket = detect_color_space_and_bucket(src, info)
        if bucket is None:
            if cspace == "Non_iPhone_Camera_Log":
                quarantined_stats["non_iphone_camera_log"] += 1
            else:
                quarantined_stats["non_standard_grid"] += 1
            continue

        pack = infer_pack_tag(src)
        raw_base = os.path.basename(src)
        if "__" in raw_base:
            raw_base = raw_base.split("__")[-1]
        base_slug = sanitize_slug(raw_base)
        # Strip redundant prefixes if already in base_slug
        for pref in (f"{pack}_", "Chroma_", "KodakCC0_"):
            if base_slug.lower().startswith(pref.lower()):
                base_slug = base_slug[len(pref):]

        sz = info["lut_3d_size"]
        style = info["visual_style"]

        # Keep Official GuVue filenames crisp & recognizable while still tagged
        if pack == "GuVue":
            out_name = f"{cspace}__{base_slug}__{style}__{sz}pt.cube"
        else:
            out_name = f"{cspace}__{pack}__{base_slug}__{style}__{sz}pt.cube"

        dest_dir = os.path.join(VAULT, bucket)
        out_path = os.path.join(dest_dir, out_name)
        if os.path.exists(out_path):
            stem, ext = os.path.splitext(out_name)
            out_path = os.path.join(dest_dir, f"{stem}_{digest[:6]}{ext}")

        with open(out_path, "wb") as f:
            f.write(data)

        seen_sha256[digest] = out_path
        accepted.append({
            "filename": os.path.basename(out_path),
            "relpath": os.path.relpath(out_path, VAULT),
            "bucket": bucket,
            "color_space": cspace,
            "pack": pack,
            "visual_style": style,
            "lut_3d_size": sz,
            "triplets": info["triplets"],
            "title": info["title"],
            "bytes": len(data),
            "sha256": digest,
            "source_origin": src,
        })

    # Remove temporary pre-snapshot
    shutil.rmtree(snap_dir, ignore_errors=True)

    # Build mobile-only AirDrop ZIP (folders 1_ through 5_ ONLY — zero 65pt lag!)
    mobile_zip = os.path.join(VAULT, "IPHONE17_BLACKMAGIC_MOBILE_17_33PT.zip")
    with zipfile.ZipFile(mobile_zip, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for fld in FOLDERS[:5]:
            fp = os.path.join(VAULT, fld)
            for root, _, files in os.walk(fp):
                for fn in sorted(files):
                    if fn == ".DS_Store":
                        continue
                    full = os.path.join(root, fn)
                    zf.write(full, os.path.relpath(full, VAULT))

    # Summary stats
    by_bucket = {fld: 0 for fld in FOLDERS}
    by_grid = {}
    for e in accepted:
        by_bucket[e["bucket"]] += 1
        gk = f"{e['lut_3d_size']}pt"
        by_grid[gk] = by_grid.get(gk, 0) + 1

    manifest = {
        "total_unique_cubes": len(accepted),
        "mobile_17_33pt_cubes": sum(by_bucket[f] for f in FOLDERS[:5]),
        "desktop_64_65pt_cubes": by_bucket["6_Desktop_Only_65pt"],
        "sha256_duplicates_purged": duplicate_count,
        "quarantined_stats": quarantined_stats,
        "bucket_counts": by_bucket,
        "grid_counts": by_grid,
        "mobile_zip_bytes": os.path.getsize(mobile_zip),
        "mobile_zip_mb": round(os.path.getsize(mobile_zip) / (1024 * 1024), 2),
        "entries": accepted,
    }

    manifest_path = os.path.join(VAULT, "_work_logs/vault_manifest.json")
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)

    print(json.dumps({k: v for k, v in manifest.items() if k != "entries"}, indent=2))


if __name__ == "__main__":
    main()
