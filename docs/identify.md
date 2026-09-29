# Identify the board

Confirm USB and that you are flashing **Heltec V4** (this walkthrough). If your board is **V4 R8**, stop — see the comparison on [Overview](index.md).

## On the board

Silkscreen / packaging should read plain **V4** (for example `HTIT-WB32LAF V4.3`). **V4 R8** / **V4-R8** means a different flasher target.

## Confirm with the chip (recommended)

After the board is on USB:

<div class="run" markdown>

```bash
esptool --chip esp32s3 --port /dev/ttyACM0 chip-id
```

```text {.no-copy}
Features: … Embedded PSRAM 2MB …
```

</div>

**2MB** PSRAM → plain V4 → flasher **Heltec V4**. **8MB** → [Overview](index.md) R8 row.

This desk board reported **2MB**.

## In the flasher

Open [flasher.meshtastic.org](https://flasher.meshtastic.org/) and select **Heltec V4**.

![Heltec V4 selected with firmware 2.7.26 — this desk board’s target](assets/images/identify-flasher-device.png)

Next: [Bootloader mode](bootloader.md).
