#!/usr/bin/env python3
"""
Agy Wave 1-5 Multi-Threaded Public Portal, Forum & Cloud-Link Scraper
Strictly public HTTP 200 DOM/API inspection only (zero CAPTCHA/login/403 bypass).
"""
import concurrent.futures
import html
import json
import os
import re
import urllib.parse
import urllib.request
import zipfile

VAULT = "/Users/hoggormino/projects/iPhone17_LUTs_Vault"
OUT_DIR = os.path.join(VAULT, "_work_logs/portal_downloads")
REPORT_JSON = os.path.join(VAULT, "_work_logs/portal_forum_audit.json")
os.makedirs(OUT_DIR, exist_ok=True)

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Safari/605.1.15"

TARGETS = [
    ("IWLTBAP_Free", "https://lut.iwltbap.com/"),
    ("FreshLUTs", "https://freshluts.com/"),
    ("GroundControl_Free", "https://groundcontrolcolor.com/collections/free-color-grading-luts"),
    ("PresetPro_Free", "https://www.presetpro.com/free-luts/"),
    ("FixThePhoto_Free", "https://fixthephoto.com/free-luts"),
    ("LiftGammaGain_LUTs", "https://www.liftgammagain.com/forum/index.php?forums/luts-look-management.55/"),
    ("EOSHD_Forum", "https://www.eoshd.com/comments/"),
    ("Cinematography_Forum", "https://cinematography.com/"),
    ("DVXUser_Forum", "https://www.dvxuser.com/"),
    ("Blackmagic_Forum", "https://forum.blackmagicdesign.com/viewforum.php?f=2"),
    ("LumaDune_AppleLog", "https://lumadune.com/luts/apple-log"),
    ("RodrigoPolo_AppleLog2", "https://rodrigopolo.com/2025/11/apple-log-2-to-rec-709-lut/"),
    ("Luttie_Blackmagic", "https://luttie.app/luts/camera/blackmagic"),
    ("FotorGear_LUTs", "https://www.fotorgear.com/pages/luts"),
    ("NoPixels_HLG", "https://nopixels.net/hlg-to-rec709/"),
]


def audit_and_extract(item):
    name, url = item
    res = {
        "name": name,
        "url": url,
        "http_status": None,
        "classification": None,
        "direct_assets": [],
        "cloud_links": [],
        "downloaded": [],
    }
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=12) as resp:
            res["http_status"] = resp.status
            body = html.unescape(resp.read().decode("utf-8", errors="ignore"))
    except urllib.error.HTTPError as e:
        res["http_status"] = e.code
        res["classification"] = f"HTTP_{e.code}_GATED_OR_BLOCKED"
        return res
    except Exception as e:
        res["http_status"] = "ERR"
        res["classification"] = f"ERR: {e}"
        return res

    # Extract direct .cube / .zip / cloud links
    urls = set(re.findall(r'https?://[^\s"\'<>]+', body))
    for href in re.findall(r'href=["\']([^"\']+)["\']', body):
        if href.startswith("/"):
            p = urllib.parse.urlparse(url)
            urls.add(f"{p.scheme}://{p.netloc}{href}")

    direct = sorted(
        u for u in urls
        if re.search(r'\.(?:cube|zip)(?:\?|$)', u, re.I)
        or "luttie.app/api/lut-assets/" in u
    )
    cloud = sorted(
        u for u in urls
        if any(d in u.lower() for d in ("drive.google.com/", "dropbox.com/s/", "dropbox.com/scl/"))
    )
    res["direct_assets"] = direct[:40]
    res["cloud_links"] = cloud[:40]

    low = body.lower()
    if direct or cloud:
        res["classification"] = "PUBLIC_DIRECT_ASSETS"
    elif any(g in low for g in ("hcaptcha", "turnstile", "altcha", "g-recaptcha")):
        res["classification"] = "CAPTCHA_OR_POW_GATED"
    elif any(g in low for g in ("add to cart", "/cart", "sign in", "login", "enter your email")):
        res["classification"] = "LOGIN_EMAIL_OR_CART_GATED"
    else:
        res["classification"] = "PUBLIC_INFO_ONLY"

    # Auto-download any newly discovered small/medium direct .zip/.cube from IWLTBAP/PresetPro/etc.
    if name in ("IWLTBAP_Free", "PresetPro_Free", "GroundControl_Free"):
        for durl in direct[:5]:
            try:
                fn = os.path.basename(urllib.parse.urlparse(durl).path) or f"{name}.bin"
                dest = os.path.join(OUT_DIR, f"{name}__{fn}")
                if not os.path.exists(dest):
                    r2 = urllib.request.Request(durl, headers={"User-Agent": UA})
                    with urllib.request.urlopen(r2, timeout=20) as resp2:
                        data = resp2.read()
                    with open(dest, "wb") as f:
                        f.write(data)
                    res["downloaded"].append({"file": dest, "bytes": len(data)})
                    if dest.lower().endswith(".zip"):
                        with zipfile.ZipFile(dest, "r") as zf:
                            zf.extractall(dest + "_extracted")
            except Exception:
                pass
    return res


def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
        results = list(ex.map(audit_and_extract, TARGETS))
    with open(REPORT_JSON, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    for r in results:
        print(f"{r['name']:24s} | HTTP {str(r['http_status']):4s} | {r['classification']:26s} | direct={len(r['direct_assets'])} cloud={len(r['cloud_links'])} dl={len(r['downloaded'])}")


if __name__ == "__main__":
    main()
