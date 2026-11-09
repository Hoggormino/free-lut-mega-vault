#!/usr/bin/env python3
"""
Generates MASTER_LUT_CATALOG.md and README.md for /Users/hoggormino/projects/iPhone17_LUTs_Vault
from _work_logs/vault_manifest.json.
"""
import json
import os
from datetime import datetime

VAULT = "/Users/hoggormino/projects/iPhone17_LUTs_Vault"
MANIFEST = os.path.join(VAULT, "_work_logs/vault_manifest.json")
CATALOG_MD = os.path.join(VAULT, "MASTER_LUT_CATALOG.md")
README_MD = os.path.join(VAULT, "README.md")

BUCKET_META = {
    "1_Apple_Log_2_iPhone17Pro": (
        "1. Apple Log 2 — iPhone 17 Pro & 17 Pro Max (`17pt` / `33pt` Mobile)",
        "Use when Blackmagic Camera **Color Space** is set to **Apple Log 2** or **Apple Log 2 - HDR** (*Apple Wide Gamut*).",
    ),
    "2_Apple_Log_Original": (
        "2. Apple Log (Original v1) — iPhone 17 Pro / 15–16 Pro (`17pt` / `33pt` Mobile)",
        "Use when shooting standard **Apple Log (Rec. 2020)** in Blackmagic Camera.",
    ),
    "3_Rec709_Base_iPhone17": (
        "3. Rec. 709 & HLG Base — iPhone 17 & iPhone 17 Air (`17pt` / `33pt` Mobile)",
        "Primary creative & HDR-to-SDR LUTs for base **iPhone 17** and **iPhone 17 Air** (or post-Rec.709 nodes on 17 Pro).",
    ),
    "4_GuVue_and_HK_Neon_Looks": (
        "4. GuVue Official Samples & HK Neon Aesthetic (`33pt` Mobile)",
        "Official **GuVue Film Collection (`F11–F14`)** in both `AppleLog2` & `Rec709` + Illustrated PDF Guide + 1-to-1 **HK Series (`HK01–HK06`)** neon/editorial matches.",
    ),
    "5_GitHub_and_Community_Packs": (
        "5. Open-Source GitHub, HuggingFace & Creator Calibrated Packs (`17pt` / `33pt` Mobile)",
        "Calibrated film stock simulations (`Chromasmith`, `GlassMeter`, `Derby`, `Kodak CC0`, `IWLTBAP`, `LumixStyle`, `GitHub` & `HuggingFace` open-source packs).",
    ),
    "6_Desktop_Only_65pt": (
        "6. Desktop-Only High-Precision Grids (`64pt` / `65pt` — DaVinci Resolve / FCP / Premiere)",
        "**Isolated from iOS folders** (`262,144`–`274,625` triplets) so they never lag Blackmagic Camera on iPhone.",
    ),
}


def main():
    with open(MANIFEST, "r", encoding="utf-8") as f:
        m = json.load(f)

    entries = m["entries"]
    by_bucket = {}
    style_counts = {}
    for e in entries:
        by_bucket.setdefault(e["bucket"], []).append(e)
        st = e["visual_style"]
        style_counts[st] = style_counts.get(st, 0) + 1

    ts = datetime.now().strftime("%Y-%m-%d %H:%M")

    # Build MASTER_LUT_CATALOG.md
    lines = [
        "# iPhone 17 Series — Master 3D LUT Vault & Color Science Catalog",
        "",
        f"> **Generated:** `{ts}` · **Orchestrator:** Agy (`macOS zsh` + `gemini` CLI + `opencode` CLI + Python 3 Color Indexer)  ",
        f"> **Vault Path:** `/Users/hoggormino/projects/iPhone17_LUTs_Vault`  ",
        f"> **Total Unique SHA-256 Verified 3D `.cube` LUTs:** **`{m['total_unique_cubes']}`** (`{m['mobile_17_33pt_cubes']}` Mobile `17pt`/`33pt` + `{m['desktop_64_65pt_cubes']}` Desktop `64pt`/`65pt`)  ",
        f"> **SHA-256 Duplicates Purged:** **`{m['sha256_duplicates_purged']}`** · **Non-iPhone Camera-Log / 1D / Invalid Quarantined:** **`{sum(m['quarantined_stats'].values())}`**  ",
        f"> **Ready-to-AirDrop Mobile Bundle (`{m['mobile_zip_mb']} MB`):** `IPHONE17_BLACKMAGIC_MOBILE_17_33PT.zip` *(Folders `1`–`5` only; zero `65pt` lag)*",
        "",
        "---",
        "",
        "## 1. Vault Overview & Grid Breakdown",
        "",
        "| Folder | Purpose | Verified `.cube` Count | Grid Sizes |",
        "| :--- | :--- | ---: | :--- |",
    ]

    for bkey, (title, desc) in BUCKET_META.items():
        items = by_bucket.get(bkey, [])
        grids = sorted({f"{x['lut_3d_size']}pt" for x in items}) or ["—"]
        lines.append(f"| `{bkey}/` | {desc} | **{len(items)}** | `{', '.join(grids)}` |")

    lines.extend([
        "",
        "### Auto-Labeled Visual Style Distribution (3D Lattice Sampled)",
        "",
        "| Visual Style Tag | Count | Lattice Detection Criterion |",
        "| :--- | ---: | :--- |",
        f"| `Natural-Cinema` | **{style_counts.get('Natural-Cinema', 0)}** | Balanced neutral grey axis & natural highlight roll-off |",
        f"| `Warm-Amber` | **{style_counts.get('Warm-Amber', 0)}** | Positive R-B midtone warmth (`mid_R - mid_B > +0.035`) |",
        f"| `Cool-Cyan` | **{style_counts.get('Cool-Cyan', 0)}** | Cool harbour/cyan midtone balance (`mid_R - mid_B < -0.030`) |",
        f"| `Teal-Orange` | **{style_counts.get('Teal-Orange', 0)}** | Split-complementary cool cyan shadows + warm skin/highlights |",
        f"| `Jade-Editorial` | **{style_counts.get('Jade-Editorial', 0)}** | Wong Kar-wai / Fuji pale-green midtone bias |",
        f"| `Matte-Film` | **{style_counts.get('Matte-Film', 0)}** | Lifted analog black floor (`Y_black > 0.025`) |",
        f"| `Monochrome-BW` | **{style_counts.get('Monochrome-BW', 0)}** | Achromatic R≈G≈B response across saturated chroma inputs |",
        "",
        "---",
        "",
        "## 2. iPhone 17 Series Color Space Routing Guide (Blackmagic Camera iOS)",
        "",
        "| iPhone Model | Blackmagic Camera Color Space | Vault Folders to Import | Critical Color Rule |",
        "| :--- | :--- | :--- | :--- |",
        "| **iPhone 17 Pro / 17 Pro Max** | **Apple Log 2** (*Apple Wide Gamut*) | `1_Apple_Log_2_iPhone17Pro/` & `4_GuVue_and_HK_Neon_Looks/` (`AppleLog2__*`) | Do **not** apply Rec.2020 Apple Log v1 LUTs onto Apple Log 2 clips—gamut mismatch shifts skin tones. Set LUTs Manager **Color Space Tag → `Rec.709`**. |",
        "| **iPhone 17 Pro / 17 Pro Max** | **Apple Log** (*Rec. 2020*) | `2_Apple_Log_Original/` | Single-stage Log-to-Rec.709 + creative look LUTs; do not stack two Log conversion LUTs. |",
        "| **iPhone 17 & iPhone 17 Air** | **Rec. 709 SDR** / **HLG HDR** | `3_Rec709_Base_iPhone17/`, `4_GuVue_and_HK_Neon_Looks/` (`Rec709__*`), `5_GitHub_and_Community_Packs/` | Base iPhone 17 & 17 Air do not shoot Apple Log—never apply Log LUTs to Rec.709 footage. |",
        "| **macOS Desktop NLE** | **DaVinci Resolve / Final Cut Pro / Premiere** | `6_Desktop_Only_65pt/` (+ all `33pt` folders) | `65×65×65` (`274,625` triplets) LUTs are isolated here for desktop grading precision without lagging iOS viewfinders. |",
        "",
        "---",
        "",
        "## 3. Public Cloud, Creator Portal & Open-Source Source Registry",
        "",
        "| Source / Creator | Type | Input Space(s) | Public URL |",
        "| :--- | :--- | :--- | :--- |",
        "| **GuVue Film Collection (`F11–F14`)** | Creator Sample ZIP (`~/Downloads`) | `Apple Log 2`, `Rec. 709` | `https://guvueluts.com/products/guvue-film-collection-lut-pack` |",
        "| **FotorGear Apple Log -> Fujifilm (10 LUTs)** | Public Google Drive Folder | `Apple Log` | `https://drive.google.com/drive/folders/1pPrzZgAMvyXCmH0TL0zUIAwsVMYtUrbY` |",
        "| **FotorGear Kodak Charmera (4 LUTs)** | Public Google Drive Folder | `Rec. 709` | `https://drive.google.com/drive/folders/1EF-QU1gkJmt2pA3urQRYMmucsgYFJLbk` |",
        "| **FotorGear Shunji Iwai Love Letter** | Public Google Drive ZIP | `Rec. 709` | `https://drive.google.com/file/d/1vsb6D897wksXh3AC7eiMb8STyxUDFYMB/view` |",
        "| **FotorGear Rec.709 Fujifilm Simulate** | Public Google Drive ZIP | `Rec. 709` | `https://drive.google.com/file/d/1HVfCAiVn4qbTtfyho6_1X18mEsT1frr3/view` |",
        "| **Byronvini Apple Log LUT (`65pt`)** | Public Google Drive File | `Apple Log` (Desktop `65pt`) | `https://drive.google.com/file/d/1cN5Lfhk28d1XshVWJkJh8qWbzto-aO3j/view` |",
        "| **Oleg Nikitin Blackmagic Cam Drive** | Public Google Drive Folder | `Apple Log` (`65pt`), `S-Log3` (`33pt`) | `https://drive.google.com/drive/folders/1FOziyLgHfKimVunhcF5Ws5ZCcvkZcvEp` |",
        "| **Luma Dune Apple Log & Apple Log 2** | Creator Direct CDN (`33pt` & `65pt`) | `Apple Log 2`, `Apple Log` | `https://lumadune.com/luts/apple-log` |",
        "| **Rodrigo Polo Apple Log 2 & ProRes RAW** | Creator Direct (`33pt` & `65pt`) | `Apple Log 2`, `ProRes RAW` | `https://rodrigopolo.com` |",
        "| **Bransford Media Tech & FreeLook** | Creator Direct ZIPs (`33pt` & `65pt`) | `Apple Log 2`, `Apple Log` | `https://bransfordmedia.com` |",
        "| **Luttie Blackmagic Camera LUTs** | Public Direct Asset API (`33pt`) | `Apple Log 2`, `Apple Log`, `Rec. 709` | `https://luttie.app/luts/camera/blackmagic` |",
        "| **IWLTBAP Free LUT Pack** | Creator Public ZIP | `Rec. 709` / `Log` | `https://lut.iwltbap.com/` |",
        "| **NoPixels HLG BT.2020 -> Rec.709 v2.0** | Creator Public ZIP (`65pt`) | `HLG BT.2020` (Desktop `65pt`) | `https://nopixels.net/hlg-to-rec709/` |",
        "| **`Joey-LJ/LUTS`** | GitHub Open Repo (`33pt`) | `Apple Log 2` (Fuji GFX 100 sims) | `https://github.com/Joey-LJ/LUTS` |",
        "| **`raycalrui/raycal-luts`** | GitHub Open Repo (`33pt`) | `Apple Log 2`, `Apple Log` | `https://github.com/raycalrui/raycal-luts` |",
        "| **`haji-mi/loglook`** | GitHub MIT (`33pt`) | `Apple Log` | `https://github.com/haji-mi/loglook` |",
        "| **`slaycamera/luts`** | GitHub CC-BY-4.0 (`33pt`) | `Rec. 709` | `https://github.com/slaycamera/luts` |",
        "| **`TareqAmeer/Chroma-App`** | GitHub GPL-3.0 (`48× 33pt`) | `Rec. 709` (Kodak Vision3 / Portra / Fuji) | `https://github.com/TareqAmeer/Chroma-App` |",
        "| **`TrondW/glassmeter-film-looks`** | GitHub CC-BY-4.0 (`30× 33pt`) | `sRGB / Rec. 709` | `https://github.com/TrondW/glassmeter-film-looks` |",
        "| **`joinfiber/derby-film`** | GitHub MIT (`7× 33pt`) | `sRGB / Rec. 709` | `https://github.com/joinfiber/derby-film` |",
        "| **`scernst13/HaldCLUT-Cube-Files`** | GitHub CC0-1.0 (`14× 33pt`) | `Rec. 709` | `https://github.com/scernst13/HaldCLUT-Cube-Files` |",
        "| **`imnz730/LUTs`** | GitHub (`33pt` 2383 / 3513DI / HLG) | `Rec. 709`, `HLG` | `https://github.com/imnz730/LUTs` |",
        "| **`Animesh-Does-Code/HDR-to-SDR-LUTs_YouTube`** | GitHub (`7× 33pt`) | `HDR PQ -> SDR` | `https://github.com/Animesh-Does-Code/HDR-to-SDR-LUTs_YouTube` |",
        "| **`MokshC/Film-Emulation-LUTs`** | GitHub (`94× 65pt`) | `Rec. 709` (Desktop `65pt`) | `https://github.com/MokshC/Film-Emulation-LUTs` |",
        "",
        "---",
        "",
        "## 4. Complete Verified `.cube` Catalog (Auto-Labeled & SHA-256 Deduplicated)",
        "",
    ]

    for bkey, (title, desc) in BUCKET_META.items():
        items = sorted(by_bucket.get(bkey, []), key=lambda x: x["filename"].lower())
        lines.append(f"### {title} — `{len(items)}` Files")
        lines.append(f"*{desc}*")
        lines.append("")
        lines.append("| Auto-Labeled `.cube` File | Color Space | Pack / Origin | Style | Grid (`Triplets`) | SHA-256 (`[:10]`) |")
        lines.append("| :--- | :--- | :--- | :--- | :--- | :--- |")
        for it in items:
            rel = it["relpath"]
            abs_url = f"file://{VAULT}/{rel}"
            lines.append(
                f"| [{it['filename']}]({abs_url}) | `{it['color_space']}` | `{it['pack']}` | `{it['visual_style']}` | `{it['lut_3d_size']}pt` (`{it['triplets']:,}`) | `{it['sha256'][:10]}` |"
            )
        lines.append("")

    with open(CATALOG_MD, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    # Build clean top-level README.md for GitHub
    readme = [
        "# iPhone 17 Series — 3D LUT Vault (Blackmagic Camera iOS & Desktop Grading)",
        "",
        f"Curated, binary-verified, SHA-256 deduplicated, and color-science auto-labeled 3D LUT (`.cube`) library for the **iPhone 17**, **iPhone 17 Air**, **iPhone 17 Pro**, and **iPhone 17 Pro Max** in **Blackmagic Camera** and **DaVinci Resolve / Final Cut Pro**.",
        "",
        "## Vault Summary",
        f"- **Total Unique 3D `.cube` LUTs:** **{m['total_unique_cubes']}**",
        f"- **iOS Blackmagic Camera Ready (`17×17×17` & `33×33×33`):** **{m['mobile_17_33pt_cubes']}** *(Folders `1`–`5`)*",
        f"- **Desktop NLE High-Precision (`64×64×64` & `65×65×65`):** **{m['desktop_64_65pt_cubes']}** *(Isolated in `6_Desktop_Only_65pt/`)*",
        f"- **SHA-256 Duplicates Purged:** **{m['sha256_duplicates_purged']}**",
        "",
        "## Directory Structure",
    ]
    for bkey, (title, desc) in BUCKET_META.items():
        cnt = len(by_bucket.get(bkey, []))
        readme.append(f"- **`{bkey}/`** (**{cnt}** LUTs) — {desc}")

    readme.extend([
        "",
        "## Naming Convention",
        "Every `.cube` file is auto-labeled by binary header & 3D lattice color inspection:",
        "```text",
        "<ColorSpace>__<CreatorOrPack>__<LookName>__<VisualStyle>__<GridSize>pt.cube",
        "```",
        "",
        "See **[`MASTER_LUT_CATALOG.md`](./MASTER_LUT_CATALOG.md)** for the full file-by-file index, color pipeline matrix, and source registry.",
    ])

    with open(README_MD, "w", encoding="utf-8") as f:
        f.write("\n".join(readme) + "\n")

    print(f"Wrote {CATALOG_MD} ({os.path.getsize(CATALOG_MD)} bytes) and {README_MD}")


if __name__ == "__main__":
    main()
