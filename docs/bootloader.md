# Bootloader mode

Heltec V4 dropped the CP2102 path — enter download / bootloader mode before the web flasher.

## Steps

Board stays plugged in over USB-C:

1. Hold **USER** (also **PRG** on some silk).
2. Tap **RST** once.
3. Release **USER**.

The serial port name can change after this — reselect the Espressif / `ttyACM*` device in the browser if asked.

Next: [Flash firmware](flash.md).
