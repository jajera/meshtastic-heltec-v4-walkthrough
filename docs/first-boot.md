# First boot

After flash and **RST**, Meshtastic should start. The OLED should show UI (or a region-unset prompt).

## Expect

- OLED activity on a board that had a working display before the flash.
- Serial boot lines such as `SSD1306 found at address 0x3c`.
- Status LED returns to a normal colour after RST (for example white).
- Bluetooth advertising for the mobile app (typical).

If the OLED worked before flashing and is black afterward, see [Troubleshoot](troubleshoot.md) and reflash from [Identify](identify.md).

## Power

On USB the board stays powered without pressing **PWR**. On battery, hold **PWR** until the board boots (check the silk on your kit).

Next: [Configure](configure.md).
