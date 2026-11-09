#!/usr/bin/env python3
"""
Agy Local + Portal Archive Unpacker & Stager
Extracts any remaining .zip/.7z/.rar archives in ~/Downloads, _work_logs/portal_downloads,
and /tmp/lut_scavenger/downloads, and also fetches direct 65pt desktop siblings from
public zero-login portals (Luma Dune 65pt, Rodrigo Polo 65pt) for 6_Desktop_Only_65pt.
"""
import os
import shutil
import subprocess
import urllib.request
import zipfile

VAULT = "/Users/hoggormino/projects/iPhone17_LUTs_Vault"
STAGE = os.path.join(VAULT, "_incoming_staging")
os.makedirs(STAGE, exist_ok=True)

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_5)"

# 1. Fetch public zero-login 65pt desktop reference LUTs if not yet downloaded so 6_Desktop_Only_65pt is complete
DESKTOP_65_URLS = [
    ("LumaDune_AppleLog2_to_Rec709_65pt.cube", "https://res.lumadune.com/static-lut-files/AppleLog2ToRec709-v1.0-65.cube"),
    ("LumaDune_AppleLog_to_Rec709_65pt.cube", "https://res.lumadune.com/static-lut-files/AppleLogToRec709-v1.0-65.cube"),
    ("RodrigoPolo_AppleLog2_to_Rec709_65pt.cube", "https://rodrigopolo.com/wp-content/uploads/2025/11/AppleLog2_to_Rec709_65_Grid.cube"),
    ("RodrigoPolo_ProResRAW_AppleLog2_to_Rec709_65pt.cube", "https://rodrigopolo.com/wp-content/uploads/2025/11/OtherProResRAW_AppleLog2_to_Rec709_65_Grid.cube"),
]

d65_stage = os.path.join(STAGE, "portal_65pt")
os.makedirs(d65_stage, exist_ok=True)
for fname, url in DESKTOP_65_URLS:
    dest = os.path.join(d65_stage, fname)
    if not os.path.exists(dest):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=20) as r:
                data = r.read()
            if b"LUT_3D_SIZE" in data[:2048]:
                with open(dest, "wb") as f:
                    f.write(data)
                print(f"Downloaded 65pt reference: {fname} ({len(data)} bytes)")
        except Exception as e:
            print(f"Skip {fname}: {e}")

# 2. Extract any nested .zip archives inside _work_logs/portal_downloads (e.g. IWLTBAP_Free)
portal_dl = os.path.join(VAULT, "_work_logs/portal_downloads")
if os.path.isdir(portal_dl):
    for root, _, files in os.walk(portal_dl):
        for fn in files:
            if fn.lower().endswith(".zip"):
                zp = os.path.join(root, fn)
                out = zp + "_unz"
                if not os.path.isdir(out):
                    os.makedirs(out, exist_ok=True)
                    subprocess.run(["unar", "-q", "-f", "-o", out, zp], check=False)

# 3. Copy prior audit markdowns/jsons from /tmp/lut_scavenger into _work_logs for provenance
if os.path.isdir("/tmp/lut_scavenger"):
    for fn in os.listdir("/tmp/lut_scavenger"):
        if fn.endswith((".md", ".json")) and not fn.startswith("subjob"):
            src = os.path.join("/tmp/lut_scavenger", fn)
            dst = os.path.join(VAULT, "_work_logs", f"scavenger_{fn}")
            if os.path.isfile(src) and not os.path.exists(dst):
                shutil.copy2(src, dst)

# Count .cube files discovered inside portal_downloads (IWLTBAP etc.)
iwl_cubes = []
if os.path.isdir(portal_dl):
    for root, _, files in os.walk(portal_dl):
        for fn in files:
            if fn.lower().endswith(".cube") and not fn.startswith("._"):
                iwl_cubes.append(os.path.join(root, fn))
print(f"Portal downloads unpacked .cube count: {len(iwl_cubes)}")
