# Reference

## Links

| Resource | URL |
| --- | --- |
| Meshtastic web flasher | https://flasher.meshtastic.org/ |
| Meshtastic web client | https://client.meshtastic.org/ |
| Meshtastic docs | https://meshtastic.org/docs/ |
| Heltec Meshtastic (V4) | https://wiki.heltec.org/docs/devices/open-source-hardware/esp32-series/esp32-quick-start?esp32=meshtastic |
| Heltec WiFi LoRa 32 V4 (wiki) | https://wiki.heltec.org/docs/devices/open-source-hardware/esp32-series/lora-32/wifi-lora-32-v4/ |

## Verified on this walkthrough

| Item | Value |
| --- | --- |
| Desk board | **Heltec V4** (esptool: 2MB PSRAM, 16MB flash) |
| Working flash | `heltec-v4` **2.7.26.54e0d8d** (Full Erase, MUI off) |
| OLED after correct flash | `SSD1306 found at address 0x3c` |
| USB ID | `303a:1001` Espressif USB JTAG/serial |
| Example serial | `/dev/ttyACM0` or `/dev/ttyACM1` |
| NZ LoRa region | **ANZ** (915); `lora.region` = `6` |
| Firmware floor | ≥ 2.7.25 |
| Phone BLE (desk) | Owner **Desk V4** / **DV4**; `FIXED_PIN` **123456** (change off-desk) — see [Phone app](phone.md) |
| Desk GPS | `gpsMode` ENABLED; Quectel L76K on Expansion Kit ribbon |

V4 vs V4 R8 targets: [Overview](index.md).

## Buttons

| Control | Role |
| --- | --- |
| USER / PRG | Bootloader hold; wake / menu |
| RST | Reset; bootloader partner |
| PWR | Long press to boot on battery (USB stays powered without it) |
