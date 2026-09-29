---
inclusion: always
---

# Source lock

Ground hardware and firmware claims here. Unsourced behaviour does not ship as verified.

## Citation rules

1. Prefer primary docs: Heltec wiki / product pages, Meshtastic docs, flasher UI labels from
   screenshots taken in this repo.
2. When a live setup contradicts a draft number, update this file and the page in the same change.
3. Mark uncertain lines clearly until observed on the board.

## Verified facts

| Fact | Status | Source notes |
| --- | --- | --- |
| Desk unit is plain **Heltec V4** (2MB PSRAM, 16MB flash), not R8 | observed | `esptool` Features / serial `Total PSRAM: 2095103` |
| Board USB ID `303a:1001` Espressif JTAG/serial | observed | `lsusb` / `ttyACM*` |
| Bootloader: hold USER/PRG, tap RST, release USER | Heltec + live | Heltec QS; flash pass |
| Wrong target `heltec-v4-r8-oled` on this V4 → blank OLED; I2C finds no `0x3c` | observed | Vext GPIO40 vs GPIO36 |
| Correct target `heltec-v4` 2.7.26.54e0d8d → `SSD1306 found at address 0x3c` | observed | serial boot after reflash |
| Full Erase + MESHTASTIC/UI off required for clean web flash (update.bin / oled-tft 404s) | observed | flasher console + CDN |
| NZ region **ANZ** (`lora.region` = 6) | observed | `meshtastic --set lora.region ANZ` |
| BLE fixed PIN + owner for phone pair | observed (CLI) | `bluetooth.enabled` true; `FIXED_PIN` 123456; owner Desk V4 / DV4; Wi‑Fi off |
| Desk GPS mode enabled (L76K Expansion Kit) | observed (CLI) | `position.gpsMode` ENABLED; `gpsEnGpio` 34; position empty until outdoor lock |
| Battery power: long **PWR** hold boots the kit; USB keeps the board powered without it | observed | desk battery kit |
| Meshtastic R8 variant uses `VEXT_ENABLE 40`; plain V4 uses `36` | firmware source | `variants/esp32s3/heltec_v4(_r8)/variant.h` |

## Open TBDs

- Phone BLE pair + Primary send: steps in `phone.md` / `verify.md` — confirm on your handset (not simulatable from the desk agent).
- Second-node OT verify — skipped (no second node on this pass).
