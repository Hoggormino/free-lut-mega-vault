# Wave 3B Task for `gemini-scout`: Unfurl & Binary-Verify Official FotorGear + Byronvini Public Google Drive LUTs

**STRICT COMPLIANCE**: Use **ONLY** `Shell` (`python3` / `curl` / `unzip`), `ReadFile`, and `WriteFile`. **NEVER** call `GoogleSearch` or `WebFetch`. **NEVER** bypass any login, paywall, CAPTCHA, or `403`.

## Target Zero-Login Public Google Drive Links (Discovered on `https://www.fotorgear.com/pages/luts` & YouTube)
1. **FotorGear Apple Log & Classic Fuji Folder**: `https://drive.google.com/drive/folders/1pPrzZgAMvyXCmH0TL0zUIAwsVMYtUrbY`
2. **FotorGear KODAK Charmera Folder**: `https://drive.google.com/drive/folders/1EF-QU1gkJmt2pA3urQRYMmucsgYFJLbk`
3. **FotorGear Love Letter (Shunji Iwai)**: File ID `1vsb6D897wksXh3AC7eiMb8STyxUDFYMB` (`https://drive.google.com/uc?export=download&id=1vsb6D897wksXh3AC7eiMb8STyxUDFYMB`)
4. **FotorGear Rec.709 Fujifilm Simulate**: File ID `1HVfCAiVn4qbTtfyho6_1X18mEsT1frr3` (`https://drive.google.com/uc?export=download&id=1HVfCAiVn4qbTtfyho6_1X18mEsT1frr3`)
5. **Byronvini Apple Log LUT**: File ID `1cN5Lfhk28d1XshVWJkJh8qWbzto-aO3j` (`https://drive.google.com/uc?export=download&id=1cN5Lfhk28d1XshVWJkJh8qWbzto-aO3j`)

## Exact Instructions
Write and run a Python script `/tmp/lut_scavenger/unfurl_fotorgear.py` that:
1. Creates `/tmp/lut_scavenger/downloads/fotorgear` and `/tmp/lut_scavenger/downloads/byronvini`.
2. Fetches the HTML of the two Google Drive folders (`1pPrzZgAMvyXCmH0TL0zUIAwsVMYtUrbY` and `1EF-QU1gkJmt2pA3urQRYMmucsgYFJLbk`), decodes `\x22` / HTML entities (`window['_DRIVE_ivd']` or `data-id="..."`), recursively unfurls any nested Google Drive subfolders inside them (`application/vnd.google-apps.folder`), and extracts every `(file_id, filename)` pair!
3. Downloads every public file (`https://drive.google.com/uc?export=download&id=<FILE_ID>`, handling Google Drive's `confirm=t` / `drive.usercontent.google.com/download?id=<FILE_ID>&export=download&confirm=t` if needed for larger `.zip` files) for all 5 targets above!
4. Unzips any `.zip` files (note: handle UTF-8 / GBK Chinese filenames cleanly if present, and also check if `.rar` or `.cube` or `.fgl` files are inside).
5. Runs strict binary `.cube` verification on every extracted `.cube` file:
   - Parse `LUT_3D_SIZE N`, `LUT_1D_SIZE`, `TITLE`, header `#` comments, and exact RGB floating-point triplet count (`N^3`).
   - Classify `17` (`4,913` triplets) or `33` (`35,937` triplets) as **PASS**, and `65` (`274,625` triplets) or `64`/`25`/`1D` as **REJECT**.
6. Appends Section 4 (`## 4. Official FotorGear, Oleg Nikitin & Byronvini Google Drive Binary Audit`) to `/tmp/lut_scavenger/dragnet_gemini_scout_report.md` (also documenting Oleg Nikitin's 4 downloaded `.cube`s in `/tmp/lut_scavenger/downloads/oleg_nikitin_gdrive/`: 3x `33pt` Sony S-Log3 `Alister_V-Look_V3` + 1x `65pt` `AppleLogToRec709-v1.0.cube` REJECT).
7. When finished, run:
   ```bash
   export PATH="$HOME/.local/bin:$PATH"
   hc send t19 "gemini-scout completed Wave 3B FotorGear + Byronvini Drive extraction -> /tmp/lut_scavenger/dragnet_gemini_scout_report.md"
   ```
