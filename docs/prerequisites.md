# Prerequisites

Gather these before you open the flasher.

## Hardware

| Item | Notes |
| --- | --- |
| Heltec WiFi LoRa 32 **V4** | This walkthrough; V4 R8 differs — [Overview](index.md) |
| USB-C **data** cable | Charge-only cables do not expose serial |
| LoRa antenna | Fit it before you transmit |

## Computer

Host checks below are from **Fedora**. On another OS, use the matching browser and serial permissions.

| Item | Notes |
| --- | --- |
| Chrome, Chromium, or Edge | Web Serial required — Firefox alone is not enough |
| Serial access on Linux | User in `dialout` (or equivalent); re-login after adding |
| `usbutils` | Provides `lsusb` |

Confirm the package (Fedora):

<div class="run" markdown>

```bash
rpm -q usbutils
```

```text {.no-copy}
usbutils-017-3.fc41.x86_64
```

</div>

If missing:

<div class="run" markdown>

```bash
sudo dnf install usbutils
```

```text {.no-copy}
Complete!
```

</div>

USB identity after you plug the board in:

<div class="run" markdown>

```bash
lsusb | grep -i espressif
```

```text {.no-copy}
Bus 003 Device 007: ID 303a:1001 Espressif USB JTAG/serial debug unit
```

</div>

Serial node (path can differ):

<div class="run" markdown>

```bash
ls -l /dev/ttyACM* /dev/serial/by-id/ 2>/dev/null
```

```text {.no-copy}
crw-rw---- 1 root dialout 166, 0 Sep 29 08:30 /dev/ttyACM0

/dev/serial/by-id/:
total 0
lrwxrwxrwx 1 root root 13 Sep 29 08:30 usb-Espressif_USB_JTAG_serial_debug_unit_10:BD:A3:5B:13:E0-if00 -> ../../ttyACM0
```

</div>

That proves USB — next, [identify](identify.md) and select **Heltec V4**.

## Tools

- [Meshtastic Web Flasher](https://flasher.meshtastic.org/)
- **Meshtastic** mobile app (Android / iOS) — BLE pair and day-to-day use ([Phone app](phone.md))
- [Meshtastic web client](https://client.meshtastic.org/) or CLI (`meshtastic`) after flash

Next: [Identify the board](identify.md).
