---
inclusion: fileMatch
fileMatchPattern: "docs/**"
---

# Lab safety (desk hardware)

- Use a **data** USB-C cable.
- Confirm **LoRa region** before any intentional TX.
- Do not leave the board transmitting into an unattached antenna if the hardware requires one.
- Flash the **matching** Meshtastic target (**Heltec V4** or **Heltec V4 R8**). Wrong target blanks the OLED (Vext GPIO) even though the radio may still work.
- Serial access needs membership in `dialout` (or equivalent) on Linux.
