# Troubleshoot

| Symptom | Likely cause | Fix |
| --- | --- | --- |
| Browser never lists a port | Firefox, or charge-only cable | Chrome/Chromium/Edge + data cable |
| Flash fails to connect | Not in bootloader | Hold USER → tap RST → release USER |
| Port missing after bootloader | Port renamed | Reselect `ttyACM*` |
| Permission denied on `/dev/ttyACM*` | Not in `dialout` | Add user to `dialout`, re-login |
| Serial busy / CLI cannot open port | Flasher or web client still connected | Close that tab, retry |
| `…-oled-tft-…-update.bin` HTTP 404 | **MESHTASTIC/UI** on | Turn UI **off**, Full Erase **on**, retry |
| `*-update.bin` HTTP 404 | Release has factory only | Turn **Full Erase and Install** on |
| OLED blank after flash, but worked before | Wrong flasher target (see [Overview](index.md)) | Confirm PSRAM / silk; reflash **Heltec V4** for this walkthrough |
| OLED blank; serial shows no `SSD1306 found` | Display rail not powered (wrong target) | Same as above |
| Phone cannot find node over BLE | Wi‑Fi enabled on node, or another client holds BLE | Disable node Wi‑Fi; disconnect web/other phone; rescan |
| BLE pair fails / wrong PIN | Random PIN, or fixed PIN mismatch | Read OLED code, or set `bluetooth.mode FIXED_PIN` + known `fixed_pin` via CLI |
| `pioEnv` / `hwModel` not what you expected | Wrong image installed | Reflash correct target; check with `meshtastic --info` |
| No mesh traffic | Region / channel mismatch | Confirm **ANZ** (or correct band) under [Configure](configure.md) |
