# Universal Open-Source 3D LUT Mega-Vault (10,500+ All-Camera, Film Stock & Cinema Edition)

**Total Verified & Auto-Labeled `.cube` LUTs:** `10,795` | **Unique SHA-256 3D Color Matrices:** `10,695`

The largest open-source, SHA-256 deduplicated, and mathematically auto-labeled `.cube` 3D LUT library on GitHub—engineered for **Apple iPhone (Rec.709, HLG, Apple Log 1 & 2)**, **Sony (S-Log2/3, Venice)**, **ARRI (LogC3/4)**, **RED (RWG/Log3G10)**, **Canon (C-Log)**, **Panasonic (V-Log)**, **Fujifilm (F-Log/2/C)**, **Blackmagic Design**, **DJI (D-Log/M)**, **DaVinci Resolve**, **Premiere Pro**, **Final Cut Pro**, **OBS Studio**, **ReShade**, and **ComfyUI**.

## Universal 10-Category Architecture

| Category Folder | Verified `.cube` Count | Supported Cameras, Color Spaces & Workflows |
| :--- | :--- | :--- |
| [`luts/00_Base_iPhone17_Starter_Pack/`](luts/00_Base_iPhone17_Starter_Pack) | **100** | Curated Top 100 Ready-to-AirDrop 33pt LUTs for Base iPhone 17 (10-bit HEVC Rec.709 & HLG) |
| [`luts/01_Apple_Log_1_and_2/`](luts/01_Apple_Log_1_and_2) | **484** | iPhone 15/16/17 Pro & Pro Max — Apple Log 2 (Wide Gamut) & Original Apple Log |
| [`luts/02_Sony_SLog2_SLog3_Cine/`](luts/02_Sony_SLog2_SLog3_Cine) | **203** | Sony Alpha, FX3, FX6, FX9, Venice — S-Log2, S-Log3, S-Gamut3.Cine & S-Cinetone |
| [`luts/03_ARRI_RED_Cinema/`](luts/03_ARRI_RED_Cinema) | **48** | ARRI Alexa LogC3 / LogC4 & RED RWG / Log3G10 Cinema Transforms |
| [`luts/04_Canon_Panasonic_Fuji_BMD_DJI_Logs/`](luts/04_Canon_Panasonic_Fuji_BMD_DJI_Logs) | **334** | Canon C-Log, Lumix V-Log, Fujifilm F-Log/F-Log2/GFX, BMD Film & DJI D-Log/D-Log M |
| [`luts/05_Analog_Film_Print_Stocks/`](luts/05_Analog_Film_Print_Stocks) | **4,409** | Kodak 2383/2393, Vision3, Portra, Ektar, CineStill 800T, Fuji 3513DI/Eterna/Velvia, Agfa & Polaroid |
| [`luts/06_Monochrome_Noir_BW/`](luts/06_Monochrome_Noir_BW) | **691** | Ilford HP5/Delta/FP4, Kodak Tri-X/T-Max/Double-X, Fuji Acros & Leica Monochrome |
| [`luts/07_Rec709_Creative_Director_Looks/`](luts/07_Rec709_Creative_Director_Looks) | **3,261** | GuVue, HK Neon, Teal & Orange, Cyberpunk, Golden Hour, Halation & Calibrated Opacity/WB Blends |
| [`luts/08_ACES_AgX_OpenDRT_HDR_HLG/`](luts/08_ACES_AgX_OpenDRT_HDR_HLG) | **276** | ACEScct/cg, AgX, OpenDRT, Rec.2020 HLG-to-SDR, PQ ST.2084-to-SDR & Linear Utility LUTs |
| [`luts/09_VFX_Game_OBS_ComfyUI_Desktop65pt/`](luts/09_VFX_Game_OBS_ComfyUI_Desktop65pt) | **989** | High-Precision 64pt/65pt Desktop Mastering, ComfyUI, OBS Studio & ReShade Shader LUTs |

## Visual 3D LUT Contact Sheets

![Rec709 Previews](previews/preview_rec709_creative.png)

![Apple Log 2 Previews](previews/preview_apple_log_2.png)

![Apple Log Previews](previews/preview_apple_log_v1.png)

![Camera Log Previews](previews/preview_camera_log_print.png)

## Base iPhone 17 Optimal Blackmagic Camera Settings (Internal Storage)
- **Codec:** `HEVC (H.265)` (10-bit 4:2:0) | **Bitrate:** `Max` | **Resolution:** `4K` | **Shutter:** `1/48s` (`180°`)
- **Color Space:** `Rec. 709` (use with `00_Base_iPhone17_Starter_Pack`, `05_Analog_Film_Print_Stocks`, `06_Monochrome_Noir_BW`, `07_Rec709_Creative_Director_Looks`) or `Rec. 2020 - HDR` (use with HLG LUTs in `08_ACES_AgX_OpenDRT_HDR_HLG`)

> **Full Searchable JSON Index:** Browse or query all 10,500+ LUTs programmatically via [`lut_index.json`](lut_index.json).
