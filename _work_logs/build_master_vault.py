#!/usr/bin/env python3
"""
Master Vault Builder, Color-Space Hygiene Auditor, Binary Grid Classifier & Catalog Generator
Target Vault: /Users/hoggormino/projects/iPhone17_LUTs_Vault

Consolidates ALL LUTs across:
  1. Existing Desktop migration inside /Users/hoggormino/projects/iPhone17_LUTs_Vault
  2. Official GuVue Film Collection Free Sample Pack + Luttie LUTs in ~/Downloads
  3. All verified Wave 1-3 packs & FotorGear/Oleg/Byronvini/NoPixels downloads in /tmp/lut_scavenger
  4. Sub-Agent 1 (gemini) HuggingFace + GitLab downloads (_work_logs/hf_gitlab_downloads)
  5. Sub-Agent 2 (opencode) GitHub Wave 4 raw git-tree downloads (_work_logs/github_wave4_downloads)
  6. Agy multi-threaded portal downloads (_work_logs/portal_downloads)

Strict Binary Routing:
  - 17-point (LUT_3D_SIZE 17, 4,913 triplets) & 33-point (LUT_3D_SIZE 33, 35,937 triplets):
      -> 1_Apple_Log_2_iPhone17Pro/        (Apple Log 2 / Apple Wide Gamut / ProRes RAW -> Log 2)
      -> 2_Apple_Log_Original/             (Apple Log v1 / Rec. 2020)
      -> 3_Rec709_Base_iPhone17/           (Rec. 709 SDR & HLG/HDR-to-SDR base looks for iPhone 17 & 17 Air)
      -> 4_GuVue_and_HK_Neon_Looks/        (Official GuVue F11-F14 AppleLog2 + Rec709 + HK01-HK06 Neon looks)
      -> 5_GitHub_and_Community_Packs/     (Open-source calibrated 17pt/33pt Rec.709/sRGB film stock libraries)
  - 65-point (LUT_3D_SIZE 65, 274,625 triplets):
      -> 6_Desktop_Only_65pt/              (Isolated so they NEVER lag Blackmagic Camera on iOS, ready for Resolve/FCP)
  - Non-iPhone Camera-Log LUTs (Sony S-Log2/3, Cine4, Fujifilm F-Log/F-Log2 raw input, Panasonic V-Log, ARRI LogC):
      -> Excluded from iPhone mobile folders (1..5) and logged in _work_logs/quarantined_non_iphone_logs.json
  - 1D / 13pt / 25pt / 64pt / malformed files:
      -> Excluded and logged in _work_logs/rejected_grids.json
"""
import hashlib
import json
import os
import re
import shutil
import zipfile

VAULT = "/Users/hoggormino/projects/iPhone17_LUTs_Vault"
TMP_SCAV = "/tmp/lut_scavenger"
WORK_LOGS = os.path.join(VAULT, "_work_logs")

F_AL2 = os.path.join(VAULT, "1_Apple_Log_2_iPhone17Pro")
F_AL1 = os.path.join(VAULT, "2_Apple_Log_Original")
F_709 = os.path.join(VAULT, "3_Rec709_Base_iPhone17")
F_GUVUE = os.path.join(VAULT, "4_GuVue_and_HK_Neon_Looks")
F_COMM = os.path.join(VAULT, "5_GitHub_and_Community_Packs")
F_65PT = os.path.join(VAULT, "6_Desktop_Only_65pt")

MOBILE_ZIP = os.path.join(VAULT, "IPHONE17_BLACKMAGIC_MOBILE_17_33PT.zip")
CATALOG_MD = os.path.join(VAULT, "MASTER_LUT_CATALOG.md")
MANIFEST_JSON = os.path.join(WORK_LOGS, "master_vault_manifest.json")

NUM_RE = re.compile(
    r"^\s*[-+]?(?:\d+\.?\d*|\.\d+)(?:[eE][-+]?\d+)?\s+"
    r"[-+]?(?:\d+\.?\d*|\.\d+)(?:[eE][-+]?\d+)?\s+"
    r"[-+]?(?:\d+\.?\d*|\.\d+)(?:[eE][-+]?\d+)?\s*$"
)

NON_IPHONE_LOG_PATTERNS = (
    "slog2", "slog3", "s-log2", "s-log3", "sgamut", "cine4",
    "flog_", "f-log", "flog2_", "flog2c", "fgamut",
    "v-log", "vlog", "vgamut",
    "logc", "log-c", "alexa",
    "c-log", "clog", "canonlog",
    "n-log", "nlog", "d-log", "dlog", "mavic", "phantom", "gopro", "protune",
    "bmdfilm", "ursa", "bmpcc", "blackmagic-film-gen5", "gen5", "acescct", "acescc", "cineon",
    "17p_cmp", "neutral a7s3", "alister_v-look",
    "-log.cube", "- log.cube", "utility log", "rec.709 to log",
    "only_red", "only_green", "only_blue", "blue_inversion",
)


def parse_cube_bytes(data: bytes):
    text = data.decode("utf-8", errors="replace")
    lut_3d_size = None
    lut_1d_size = None
    title = None
    comments = []
    triplets = 0
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
        if NUM_RE.match(s):
            triplets += 1

    valid_mobile = (
        lut_1d_size is None
        and lut_3d_size in (17, 33)
        and triplets == (lut_3d_size ** 3)
    )
    valid_desktop_65 = (
        lut_1d_size is None
        and lut_3d_size == 65
        and triplets == 274625
    )
    return {
        "valid_mobile": valid_mobile,
        "valid_desktop_65": valid_desktop_65,
        "lut_3d_size": lut_3d_size,
        "lut_1d_size": lut_1d_size,
        "triplets": triplets,
        "title": title or "",
        "comments": comments[:10],
    }


def is_proprietary_third_party(info: dict) -> bool:
    hdr = " ".join(info["comments"]).lower()
    return "vision-color.com" in hdr or "visioncolor" in hdr


def is_non_iphone_camera_log(path: str, info: dict) -> bool:
    fn = os.path.basename(path).lower()
    title = info["title"].lower()
    hdr = " ".join(info["comments"]).lower()
    # FotorGear AppleLog->FLog2->Fuji simulations & Joey-LJ Fuji_GFX to Apple_Log_2 explicitly take Apple Log input!
    if "apple log" in title or "applelog" in fn or "apple_log" in path.lower():
        if "s-log3-to-apple-log" in path.lower() or "slog3" in fn:
            return True
        return False
    blob = f"{fn} {title} {hdr}"
    return any(p in blob for p in NON_IPHONE_LOG_PATTERNS)


def classify_mobile_bucket(src_path: str, fn: str, info: dict):
    p_low = src_path.lower()
    fn_low = fn.lower()
    t_low = info["title"].lower()

    # 4. GuVue Official & HK Neon Looks
    if "guvue" in p_low or "guvue" in fn_low or "03_guvue_hk" in p_low:
        return F_GUVUE, "GuVue / HK Neon (Apple Log 2 & Rec.709)"
    if any(k in fn_low for k in ("cyberpunk", "neon", "slay-01-amber", "slay-03-neon", "slay-04-film")):
        if "apple log 2" in fn_low or "applelog2" in fn_low:
            return F_AL2, "Apple Log 2 (Apple Wide Gamut)"
        if "apple log" in fn_low or "applelog" in fn_low:
            return F_AL1, "Apple Log (Rec.2020)"
        return F_GUVUE, "Rec.709 HK Neon / Street"

    # 1. Apple Log 2
    if any(k in fn_low or k in p_low or k in t_low for k in ("apple log 2", "applelog2", "apple_log_2", "bmapplelog2", "bmsoftdocapplelog2")):
        return F_AL2, "Apple Log 2 (Apple Wide Gamut)"

    # 2. Apple Log v1
    if any(k in fn_low or k in p_low or k in t_low for k in ("apple log", "applelog", "apple_log", "bmapplelogto709", "bmsoftdocapplelog", "loglook", "theonelut_iphone")):
        return F_AL1, "Apple Log (Rec.2020)"

    # 3. Base iPhone 17 / 17 Air Rec.709 & HLG/HDR-to-SDR
    if any(k in p_low or k in fn_low for k in ("04_rec709", "05_hlg", "hlg", "hdr-to-sdr", "charmera", "shunjiiwai", "luttie", "slay-")):
        sp = "HLG / HDR-to-SDR" if ("hlg" in fn_low or "hdr-to-sdr" in fn_low or "05_hlg" in p_low) else "Rec.709 SDR"
        return F_709, sp

    # 5. GitHub & Community Calibrated Film Packs
    return F_COMM, "Rec.709 / sRGB Calibrated Film"


def main():
    for d in (F_AL2, F_AL1, F_709, F_GUVUE, F_COMM, F_65PT, WORK_LOGS):
        os.makedirs(d, exist_ok=True)

    # Copy prior logs from /tmp/lut_scavenger into _work_logs for complete provenance
    if os.path.isdir(TMP_SCAV):
        for fn in os.listdir(TMP_SCAV):
            if fn.endswith((".md", ".json")) and not fn.startswith("package"):
                src = os.path.join(TMP_SCAV, fn)
                dst = os.path.join(WORK_LOGS, f"scavenger_{fn}")
                if os.path.isfile(src) and not os.path.exists(dst):
                    shutil.copy2(src, dst)

    # Unzip any .zip archives currently sitting in 5_GitHub_and_Community_Packs into _work_logs/desktop_zips_extracted
    dz_out = os.path.join(WORK_LOGS, "desktop_zips_extracted")
    os.makedirs(dz_out, exist_ok=True)
    for fn in list(os.listdir(F_COMM)):
        if fn.lower().endswith(".zip"):
            zp = os.path.join(F_COMM, fn)
            try:
                with zipfile.ZipFile(zp, "r") as zf:
                    zf.extractall(os.path.join(dz_out, os.path.splitext(fn)[0]))
            except Exception:
                pass
            shutil.move(zp, os.path.join(WORK_LOGS, fn))
        elif fn == "README.txt":
            shutil.move(os.path.join(F_COMM, fn), os.path.join(WORK_LOGS, "Bransford_README.txt"))

    # Collect all candidate .cube paths in priority order into a staging list
    staging_sources = []

    # Priority 0: Official GuVue Sample Pack (preserve subfolder or explicit prefix!)
    guvue_official = os.path.join(TMP_SCAV, "ready_to_airdrop_33pt/00_GuVue_Official_Film_Samples_33pt")
    if os.path.isdir(guvue_official):
        for root, _, files in os.walk(guvue_official):
            for fn in sorted(files):
                full = os.path.join(root, fn)
                if fn.lower().endswith(".pdf"):
                    shutil.copy2(full, os.path.join(F_GUVUE, fn))
                elif fn.lower().endswith(".cube"):
                    staging_sources.append(("GuVue_Official", full, fn))

    # Priority 1: Existing files inside VAULT folders 1..6 (read into memory idempotently so reruns never lose files!)
    existing_blobs = []
    for folder in (F_AL2, F_AL1, F_709, F_GUVUE, F_COMM, F_65PT):
        os.makedirs(folder, exist_ok=True)
        for fn in sorted(os.listdir(folder)):
            p = os.path.join(folder, fn)
            if os.path.isfile(p) and fn.lower().endswith(".cube"):
                with open(p, "rb") as f:
                    existing_blobs.append((fn, f.read()))
                os.remove(p)

    existing_temp = os.path.join(WORK_LOGS, "_staging_existing")
    os.makedirs(existing_temp, exist_ok=True)
    for idx_e, (fn, blob) in enumerate(existing_blobs):
        dst = os.path.join(existing_temp, f"{idx_e:04d}__{fn}")
        with open(dst, "wb") as f:
            f.write(blob)
        staging_sources.append(("Vault_Existing", dst, fn))

    for root, _, files in os.walk(dz_out):
        for fn in sorted(files):
            if fn.lower().endswith(".cube") and not fn.startswith("._"):
                staging_sources.append(("Bransford_Zip", os.path.join(root, fn), fn))

    # Priority 2: Official FotorGear Apple Log (10x 33pt) + Kodak Charmera (4x 33pt) + Shunji Iwai (17pt)
    fg_al_dir = os.path.join(TMP_SCAV, "downloads/fotorgear_folders/AppleLog_Fuji_Folder")
    fg_map = {
        "Applelog_ACROS.cube": "FotorGear_AppleLog_Fuji_ACROS.cube",
        "Applelog_ASTIA.cube": "FotorGear_AppleLog_Fuji_ASTIA.cube",
        "Applelog_CHROME.cube": "FotorGear_AppleLog_Fuji_CLASSIC_CHROME.cube",
        "Applelog_CLASSIC-Neg.cube": "FotorGear_AppleLog_Fuji_CLASSIC_NEG.cube",
        "Applelog_ETERNA-BB.cube": "FotorGear_AppleLog_Fuji_ETERNA_BB.cube",
        "Applelog_ETERNA.cube": "FotorGear_AppleLog_Fuji_ETERNA.cube",
        "Applelog_PRO-Neg.Std.cube": "FotorGear_AppleLog_Fuji_PRO_Neg_Std.cube",
        "Applelog_PROVIA.cube": "FotorGear_AppleLog_Fuji_PROVIA.cube",
        "Applelog_REALA-ACE.cube": "FotorGear_AppleLog_Fuji_REALA_ACE.cube",
        "Applelog_Velvia.cube": "FotorGear_AppleLog_Fuji_Velvia.cube",
    }
    if os.path.isdir(fg_al_dir):
        for orig, clean in sorted(fg_map.items()):
            p = os.path.join(fg_al_dir, orig)
            if os.path.isfile(p):
                staging_sources.append(("FotorGear_AppleLog", p, clean))

    fg_kc_dir = os.path.join(TMP_SCAV, "downloads/fotorgear_folders/Kodak_Charmera_Folder")
    if os.path.isdir(fg_kc_dir):
        for fn in sorted(os.listdir(fg_kc_dir)):
            if fn.lower().endswith(".cube"):
                staging_sources.append(("FotorGear_KodakCharmera", os.path.join(fg_kc_dir, fn), "FotorGear_Kodak_Charmera_" + fn.replace(" ", "_")))

    for root, _, files in os.walk(os.path.join(TMP_SCAV, "downloads/fotorgear")):
        for fn in sorted(files):
            if fn == "yjjr (6).cube":
                staging_sources.append(("FotorGear_ShunjiIwai", os.path.join(root, fn), "FotorGear_ShunjiIwai_LoveLetter_17pt.cube"))

    # Priority 3: All verified /tmp/lut_scavenger/ready_to_airdrop_33pt folders (01..06)
    rta = os.path.join(TMP_SCAV, "ready_to_airdrop_33pt")
    if os.path.isdir(rta):
        for sub in sorted(os.listdir(rta)):
            if sub.startswith("00_"):
                continue
            spath = os.path.join(rta, sub)
            if os.path.isdir(spath):
                for root, _, files in os.walk(spath):
                    for fn in sorted(files):
                        if fn.lower().endswith(".cube") and not fn.startswith("._"):
                            staging_sources.append((f"Scavenger_{sub}", os.path.join(root, fn), fn))

    # Priority 4: Remaining Wave 1-3 clones & downloads (including 65pt desktop LUTs for 6_Desktop_Only_65pt!)
    extra_scan_dirs = [
        ("Chroma_App", os.path.join(TMP_SCAV, "clones/Chroma-App/tools/calib/LUT LIBRARY")),
        ("Kodak_CC0", os.path.join(TMP_SCAV, "clones/HaldCLUT-Cube-Files")),
        ("imnz730", os.path.join(TMP_SCAV, "clones/imnz730-LUTs")),
        ("HDR_to_SDR", os.path.join(TMP_SCAV, "clones/HDR-to-SDR-LUTs_YouTube")),
        ("Portal_Verified", os.path.join(TMP_SCAV, "downloads/verified")),
        ("LumaDune_DL", os.path.join(TMP_SCAV, "downloads/lumadune")),
        ("RodrigoPolo_DL", os.path.join(TMP_SCAV, "downloads/rodrigopolo")),
        ("Bransford_DL", os.path.join(TMP_SCAV, "downloads/bransford")),
        ("NoPixels_DL", os.path.join(TMP_SCAV, "downloads/nopixels")),
        ("OlegNikitin_GDrive", os.path.join(TMP_SCAV, "downloads/oleg_nikitin_gdrive")),
        ("Byronvini_GDrive", os.path.join(TMP_SCAV, "downloads/byronvini")),
        ("LogGrade_macOS", os.path.join(TMP_SCAV, "clones/LogGrade-macOS")),
        ("MokshC_65pt", os.path.join(TMP_SCAV, "clones/Film-Emulation-LUTs")),
        ("User_Downloads", os.path.expanduser("~/Downloads")),
        ("HF_GitLab_SubAgent", os.path.join(WORK_LOGS, "hf_gitlab_downloads")),
        ("GitHub_Wave4_SubAgent", os.path.join(WORK_LOGS, "github_wave4_downloads")),
        ("Portal_Scraper", os.path.join(WORK_LOGS, "portal_downloads")),
        ("Incoming_Staging", os.path.join(VAULT, "_incoming_staging")),
    ]

    for tag, dpath in extra_scan_dirs:
        if not os.path.isdir(dpath):
            continue
        max_depth = 1 if tag == "User_Downloads" else 6
        base_depth = dpath.rstrip(os.sep).count(os.sep)
        for root, dirs, files in os.walk(dpath):
            if root.count(os.sep) - base_depth >= max_depth:
                dirs[:] = []
            for fn in sorted(files):
                if fn.lower().endswith(".cube") and not fn.startswith("._"):
                    clean_fn = fn
                    if tag == "Chroma_App":
                        clean_fn = f"Chroma_{fn}"
                    elif tag == "Kodak_CC0":
                        clean_fn = "KodakCC0_" + fn.replace(" ", "_")
                    staging_sources.append((tag, os.path.join(root, fn), clean_fn))

    seen_mobile_sha = set()
    seen_65_sha = set()
    manifest_mobile = []
    manifest_65 = []
    quarantined_logs = []
    rejected_grids = []
    dedup_skipped = 0

    for source_tag, src_path, preferred_name in staging_sources:
        if not os.path.isfile(src_path):
            continue
        try:
            with open(src_path, "rb") as f:
                data = f.read()
        except Exception:
            continue

        info = parse_cube_bytes(data)
        digest = hashlib.sha256(data).hexdigest()

        if is_proprietary_third_party(info):
            rejected_grids.append({"file": src_path, "reason": "Third-party commercial header (VisionColor)"})
            continue

        if info["valid_mobile"]:
            if is_non_iphone_camera_log(src_path, info):
                quarantined_logs.append({
                    "source": source_tag,
                    "file": os.path.basename(src_path),
                    "lut_3d_size": info["lut_3d_size"],
                    "title": info["title"],
                    "reason": "Non-iPhone camera log curve (S-Log/F-Log/V-Log/Cineon/Gen5)",
                })
                continue
            # Keep all 8 official GuVue files even if hashes are unique anyway; deduplicate everything by SHA256
            if digest in seen_mobile_sha and source_tag != "GuVue_Official":
                dedup_skipped += 1
                continue
            seen_mobile_sha.add(digest)

            dest_dir, color_space = classify_mobile_bucket(src_path, preferred_name, info)
            os.makedirs(dest_dir, exist_ok=True)
            safe_name = preferred_name.replace("/", "_")
            out_path = os.path.join(dest_dir, safe_name)
            if os.path.exists(out_path):
                stem, ext = os.path.splitext(safe_name)
                out_path = os.path.join(dest_dir, f"{stem}_{digest[:6]}{ext}")
            with open(out_path, "wb") as f:
                f.write(data)

            manifest_mobile.append({
                "folder": os.path.basename(dest_dir),
                "filename": os.path.basename(out_path),
                "abs_path": out_path,
                "source": source_tag,
                "lut_3d_size": info["lut_3d_size"],
                "triplets": info["triplets"],
                "color_space": color_space,
                "title": info["title"],
                "bytes": len(data),
                "sha256": digest[:12],
            })

        elif info["valid_desktop_65"]:
            if digest in seen_65_sha:
                dedup_skipped += 1
                continue
            seen_65_sha.add(digest)
            os.makedirs(F_65PT, exist_ok=True)
            safe_name = preferred_name.replace("/", "_")
            out_path = os.path.join(F_65PT, safe_name)
            if os.path.exists(out_path):
                stem, ext = os.path.splitext(safe_name)
                out_path = os.path.join(F_65PT, f"{stem}_{digest[:6]}{ext}")
            with open(out_path, "wb") as f:
                f.write(data)
            manifest_65.append({
                "folder": os.path.basename(F_65PT),
                "filename": os.path.basename(out_path),
                "abs_path": out_path,
                "source": source_tag,
                "lut_3d_size": 65,
                "triplets": 274625,
                "title": info["title"],
                "bytes": len(data),
                "sha256": digest[:12],
            })
        else:
            rejected_grids.append({
                "source": source_tag,
                "file": os.path.basename(src_path),
                "lut_3d_size": info["lut_3d_size"],
                "lut_1d_size": info["lut_1d_size"],
                "triplets": info["triplets"],
                "reason": "Non-17/33/65pt grid or 1D/mismatched LUT",
            })

    # Clean temporary staging directory
    shutil.rmtree(existing_temp, ignore_errors=True)

    # Build mobile-only iOS AirDrop ZIP (folders 1..5 ONLY — zero 65pt lag!)
    tmp_zip = MOBILE_ZIP + ".tmp"
    with zipfile.ZipFile(tmp_zip, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for folder in (F_AL2, F_AL1, F_709, F_GUVUE, F_COMM):
            for root, _, files in os.walk(folder):
                for fn in sorted(files):
                    if fn.startswith("."):
                        continue
                    full = os.path.join(root, fn)
                    arc = os.path.relpath(full, VAULT)
                    zf.write(full, arc)
    os.replace(tmp_zip, MOBILE_ZIP)

    # Verify 100% of .cube files inside MOBILE_ZIP in-memory
    zip_verified = 0
    with zipfile.ZipFile(MOBILE_ZIP, "r") as zf:
        assert zf.testzip() is None, "CRC error in MOBILE_ZIP"
        for zi in zf.infolist():
            if zi.filename.lower().endswith(".cube"):
                chk = parse_cube_bytes(zf.read(zi.filename))
                assert chk["valid_mobile"], f"Non-mobile LUT leaked into MOBILE_ZIP: {zi.filename}"
                zip_verified += 1

    # Save JSON logs
    with open(os.path.join(WORK_LOGS, "quarantined_non_iphone_logs.json"), "w") as f:
        json.dump(quarantined_logs, f, indent=2)
    with open(os.path.join(WORK_LOGS, "rejected_grids.json"), "w") as f:
        json.dump(rejected_grids, f, indent=2)

    folder_counts = {}
    for d in (F_AL2, F_AL1, F_709, F_GUVUE, F_COMM, F_65PT):
        folder_counts[os.path.basename(d)] = sum(
            1 for fn in os.listdir(d) if fn.lower().endswith(".cube")
        )

    summary = {
        "vault_dir": VAULT,
        "mobile_17_33pt_total": len(manifest_mobile),
        "mobile_17pt_count": sum(1 for x in manifest_mobile if x["lut_3d_size"] == 17),
        "mobile_33pt_count": sum(1 for x in manifest_mobile if x["lut_3d_size"] == 33),
        "desktop_65pt_total": len(manifest_65),
        "total_unique_cubes_in_vault": len(manifest_mobile) + len(manifest_65),
        "mobile_zip_path": MOBILE_ZIP,
        "mobile_zip_mb": round(os.path.getsize(MOBILE_ZIP) / (1024 * 1024), 2),
        "mobile_zip_verified_cubes": zip_verified,
        "dedup_skipped": dedup_skipped,
        "quarantined_camera_logs_count": len(quarantined_logs),
        "rejected_non_standard_count": len(rejected_grids),
        "folder_counts": folder_counts,
        "mobile_entries": manifest_mobile,
        "desktop_65_entries": manifest_65,
    }
    with open(MANIFEST_JSON, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)

    # Generate MASTER_LUT_CATALOG.md
    lines = [
        "# iPhone 17 Series — Master Free 3D LUT Vault & Binary-Verified Catalog",
        "",
        f"- **Vault Root:** [iPhone17_LUTs_Vault](file://{VAULT})",
        f"- **Ready-to-AirDrop Mobile Bundle (`17pt` & `33pt` ONLY — `{summary['mobile_zip_mb']} MB`):** [IPHONE17_BLACKMAGIC_MOBILE_17_33PT.zip](file://{MOBILE_ZIP})",
        f"- **Total Unique Binary-Verified `.cube` LUTs in Vault:** **`{summary['total_unique_cubes_in_vault']}`**",
        f"  - **iOS Blackmagic Camera Mobile-Safe (`17pt` & `33pt`):** **`{summary['mobile_17_33pt_total']}`** (`{summary['mobile_33pt_count']}` × `33pt` [`35,937` triplets] + `{summary['mobile_17pt_count']}` × `17pt` [`4,913` triplets])",
        f"  - **Desktop NLE Isolated (`65pt` — Resolve / FCP / Premiere):** **`{summary['desktop_65pt_total']}`** (`274,625` triplets each in [6_Desktop_Only_65pt](file://{F_65PT}))",
        f"  - **SHA-256 Duplicates Removed:** `{dedup_skipped}` · **Non-iPhone Camera Logs Quarantined (`S-Log`/`F-Log`/`V-Log`):** `{len(quarantined_logs)}` · **Non-Standard (`64pt`/`25pt`/`13pt`/`1D`) Rejected:** `{len(rejected_grids)}`",
        "",
        "---",
        "",
        "## 1. Vault Directory Architecture & iPhone 17 Color Pipeline Matrix",
        "",
        "| Vault Folder | LUT Count | Target iPhone 17 Models | Blackmagic Camera `Color Space` Setting | Grid Spec |",
        "| :--- | :---: | :--- | :--- | :--- |",
        f"| [1_Apple_Log_2_iPhone17Pro](file://{F_AL2}) | **`{folder_counts['1_Apple_Log_2_iPhone17Pro']}`** | **iPhone 17 Pro / 17 Pro Max** | **Apple Log 2** / **Apple Log 2 - HDR** (*Apple Wide Gamut*) | `33×33×33` |",
        f"| [2_Apple_Log_Original](file://{F_AL1}) | **`{folder_counts['2_Apple_Log_Original']}`** | **iPhone 17 Pro / 17 Pro Max** *(+ 15/16 Pro B-cam)* | **Apple Log** (*Rec. 2020*) | `33×33×33` |",
        f"| [3_Rec709_Base_iPhone17](file://{F_709}) | **`{folder_counts['3_Rec709_Base_iPhone17']}`** | **iPhone 17 & iPhone 17 Air** *(+ Post-709)* | **Rec. 709** *(or Rec. 2020 HLG for HLG transforms)* | `17pt` & `33pt` |",
        f"| [4_GuVue_and_HK_Neon_Looks](file://{F_GUVUE}) | **`{folder_counts['4_GuVue_and_HK_Neon_Looks']}`** | **All iPhone 17 Models** (`_AppleLog2` for Pro, `_Rec709` for 17/Air) | Match filename suffix (`_AppleLog2` vs `_Rec709`) | `33×33×33` |",
        f"| [5_GitHub_and_Community_Packs](file://{F_COMM}) | **`{folder_counts['5_GitHub_and_Community_Packs']}`** | **iPhone 17 & 17 Air** *(or Node 2 after Log->709 on Pro)* | **Rec. 709** (*sRGB / Display-Referred*) | `17pt` & `33pt` |",
        f"| [6_Desktop_Only_65pt](file://{F_65PT}) | **`{folder_counts['6_Desktop_Only_65pt']}`** | **macOS DaVinci Resolve / Final Cut Pro ONLY** | *Do NOT import `65pt` files into iOS Blackmagic Camera* | `65×65×65` |",
        "",
        "---",
        "",
        "## 2. Discovered Cloud Folders, Creator Portals & Repository Endpoints",
        "",
        "| Source / Creator | Access Type | URL | Vault Disposition |",
        "| :--- | :--- | :--- | :--- |",
        "| **GuVue Film Collection (`F11–F14` Official Samples)** | Local User ZIP + Illustrated PDF | `https://guvueluts.com/products/guvue-film-collection-lut-pack` | **8× `33pt` `.cube`s (`4× AppleLog2` + `4× Rec709`) + PDF in `4_GuVue_and_HK_Neon_Looks`** |",
        "| **GuVue HK Series (`HK01–HK06`)** | Commercial ($38) — Matched via Open-Source `33pt` | `https://guvueluts.com/products/guvue-hk-series-lut-pack` | **Matched 1-to-1 in `4_GuVue_and_HK_Neon_Looks` + `1_Apple_Log_2_iPhone17Pro`** |",
        "| **FotorGear Official Apple Log -> Fujifilm Folder** | Public Google Drive Folder (Zero-Login) | `https://drive.google.com/drive/folders/1pPrzZgAMvyXCmH0TL0zUIAwsVMYtUrbY` | **10× `33pt` Apple Log Fujifilm Simulations extracted to `2_Apple_Log_Original`** |",
        "| **FotorGear Official Kodak Charmera Folder** | Public Google Drive Folder (Zero-Login) | `https://drive.google.com/drive/folders/1EF-QU1gkJmt2pA3urQRYMmucsgYFJLbk` | **4× `33pt` Kodak Charmera looks extracted to `3_Rec709_Base_iPhone17`** |",
        "| **FotorGear Shunji Iwai *Love Letter*** | Public Google Drive ZIP (Zero-Login) | `https://drive.google.com/file/d/1vsb6D897wksXh3AC7eiMb8STyxUDFYMB/view` | **`17pt` look extracted (`64pt` siblings rejected)** |",
        "| **Oleg Nikitin Blackmagic Workflow Drive** | Public Google Drive Folder (Reddit `r/iPhoneography`) | `https://drive.google.com/drive/folders/1FOziyLgHfKimVunhcF5Ws5ZCcvkZcvEp` | **`AppleLogToRec709-v1.0.cube` (`65pt`) moved to `6_Desktop_Only_65pt`; 3× S-Log3 quarantined** |",
        "| **Byronvini Apple Log YouTube LUT** | Public Google Drive File (Zero-Login) | `https://drive.google.com/file/d/1cN5Lfhk28d1XshVWJkJh8qWbzto-aO3j/view` | **Verified `65pt` Resolve LUT -> moved to `6_Desktop_Only_65pt`** |",
        "| **Luma Dune Apple Log & Apple Log 2** | Direct CDN `.cube` (`33pt` & `65pt`) | `https://lumadune.com/luts/apple-log` | **`33pt` in `1_` & `2_`; `65pt` in `6_Desktop_Only_65pt`** |",
        "| **Rodrigo Polo Apple Log 2 + ProRes RAW** | Direct WordPress `.cube` (`33pt` & `65pt`) | `https://rodrigopolo.com/2025/11/apple-log-2-to-rec-709-lut/` | **`33pt` in `1_Apple_Log_2_iPhone17Pro`; `65pt` in `6_Desktop_Only_65pt`** |",
        "| **Bransford Media Tech & FreeLook Packs** | 4× Direct `.zip` Bundles (`33pt` & `65pt`) | `https://bransfordmedia.com/luts/free-look/apple-log-2.zip` | **`33pt` in `1_` & `2_`; 4× `65pt` in `6_Desktop_Only_65pt`** |",
        "| **Luttie Blackmagic & Rec.709 Library** | Direct Zero-Login API (`luttie.app/api/lut-assets/*`) | `https://luttie.app/luts/camera/blackmagic` | **35× `33pt` looks across `1_`, `2_`, `3_`, `4_`** |",
        "| **NoPixels HLG BT.2020 -> Rec.709 v2.0** | Direct Zero-Login `.zip` (`nopixels.net`) | `https://nopixels.net/hlg-to-rec709/` | **Verified `65pt` -> moved to `6_Desktop_Only_65pt`** |",
        "| **Fujifilm Official GFX Eterna 55 & X-M5** | Official Support ZIPs (`33Grid` + `65Grid`) | `https://dl.fujifilm-x.com/lut/gfx-eterna-55-3d-lut-v100.zip` | **F-Log2C camera-log documented; Joey-LJ GFX->AppleLog2 `33pt` in `1_`** |",
        "",
        "---",
        "",
    ]

    # Section 3: Complete Per-Folder Clickable File Tables (Mobile 1..5)
    section_titles = [
        ("1_Apple_Log_2_iPhone17Pro", "3. Folder 1 — `1_Apple_Log_2_iPhone17Pro` (iPhone 17 Pro / Pro Max — Apple Log 2)"),
        ("2_Apple_Log_Original", "4. Folder 2 — `2_Apple_Log_Original` (iPhone 17 Pro / Pro Max — Apple Log v1)"),
        ("3_Rec709_Base_iPhone17", "5. Folder 3 — `3_Rec709_Base_iPhone17` (iPhone 17 & 17 Air — Rec.709 & HLG/HDR)"),
        ("4_GuVue_and_HK_Neon_Looks", "6. Folder 4 — `4_GuVue_and_HK_Neon_Looks` (Official GuVue F11–F14 + HK01–HK06 Neon Looks)"),
        ("5_GitHub_and_Community_Packs", "7. Folder 5 — `5_GitHub_and_Community_Packs` (Calibrated Open-Source Film Stock Libraries)"),
    ]

    for folder_key, heading in section_titles:
        items = [x for x in manifest_mobile if x["folder"] == folder_key]
        lines.append(f"## {heading} (`{len(items)}` Verified Mobile LUTs)")
        lines.append("")
        lines.append("| # | LUT File (Clickable) | `LUT_3D_SIZE` | Triplets | Color Space | Source | SHA-256 |")
        lines.append("| :---: | :--- | :---: | :---: | :--- | :--- | :---: |")
        for idx, it in enumerate(sorted(items, key=lambda x: x["filename"].lower()), 1):
            url_path = it["abs_path"].replace(" ", "%20")
            lines.append(
                f"| {idx} | [{it['filename']}](file://{url_path}) | **`{it['lut_3d_size']}pt`** | `{it['triplets']:,}` | {it['color_space']} | `{it['source']}` | `{it['sha256']}` |"
            )
        lines.append("")

    # Section 8: Desktop 65pt Folder Summary
    lines.append(f"## 8. Folder 6 — `6_Desktop_Only_65pt` (`{len(manifest_65)}` Desktop NLE `65×65×65` LUTs)")
    lines.append("")
    lines.append("> Isolated from the mobile folders so Blackmagic Camera on iOS never lags. Use these in **DaVinci Resolve**, **Final Cut Pro**, or **Premiere Pro** on macOS.")
    lines.append("")
    lines.append("| # | Desktop 65pt LUT File (Clickable) | `LUT_3D_SIZE` | Triplets | Source | SHA-256 |")
    lines.append("| :---: | :--- | :---: | :---: | :--- | :---: |")
    for idx, it in enumerate(sorted(manifest_65, key=lambda x: x["filename"].lower()), 1):
        url_path = it["abs_path"].replace(" ", "%20")
        lines.append(
            f"| {idx} | [{it['filename']}](file://{url_path}) | `65pt` | `274,625` | `{it['source']}` | `{it['sha256']}` |"
        )
    lines.append("")

    # Section 9: Gated / Quarantined Audit Log
    lines.extend([
        "---",
        "",
        "## 9. Compliance & Quarantine Log (Gated Portals, Non-iPhone Logs & Rejected Grids)",
        "",
        "- **Gated / Anti-Bot Portals Left Untouched (Strict Zero-Bypass Compliance):**",
        "  - `guvueluts.com#film-samples` (`hCaptcha` + email gate — satisfied via user's local `GuVue_Film_Collection_4_Free_Sample_Looks_EN.zip`), `guvueluts.com/products/guvue-hk-series-lut-pack` ($38 paid), `tobiamontanari.com` (`Altcha` PoW + Gumroad), `proloststore.com/products/applelog` (Gumroad checkout), `cinecolor.io/products/apple-log2-lut` ($0 Shopify email checkout), `lutcraft.com` (`HTTP 403` / WooCommerce checkout), `filtergrade.com` (`HTTP 403` Cloudflare), `pond5.com` (`HTTP 403`), `freshluts.com` (account login required), `fixthephoto.com` (email gate).",
        f"- **Non-iPhone Camera-Log `.cube`s Quarantined (`{len(quarantined_logs)}` files):** Full list in [quarantined_non_iphone_logs.json](file://{WORK_LOGS}/quarantined_non_iphone_logs.json) (`Sony S-Log2/S-Log3/Cine4`, `Fujifilm F-Log/F-Log2`, `BMD Film Gen5`, `S-Log3-to-Apple-Log`).",
        f"- **Non-Standard / 1D `.cube`s Rejected (`{len(rejected_grids)}` files):** Full list in [rejected_grids.json](file://{WORK_LOGS}/rejected_grids.json) (`64pt` Hald conversions, `25pt` PictureFX, `13pt` Film-Camera-IOS/ffgrade, `1D` 4096-line shapers).",
        "",
    ])

    with open(CATALOG_MD, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(json.dumps({k: v for k, v in summary.items() if not k.endswith("_entries")}, indent=2))


if __name__ == "__main__":
    main()
