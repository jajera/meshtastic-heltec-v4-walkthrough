# Configure

Set LoRa region before any transmit. On this NZ 915 MHz unit the correct value is **ANZ** (there is no region named “NZ”). Use **NZ_865** only on 865/868 modules.

After a full erase, region starts as `UNSET` and the radio will not TX until you set it.

Also set a node name and a **fixed Bluetooth PIN** so the phone app can pair without chasing a random OLED code. Full phone connect and day-to-day use: [Phone app](phone.md).

## CLI (serial) — region, name, BLE PIN

Close any browser tab that holds the port, then:

<div class="run" markdown>

```bash
meshtastic --port /dev/ttyACM0 \
  --set lora.region ANZ \
  --set-owner "Desk V4" \
  --set-owner-short "DV4" \
  --set bluetooth.enabled true \
  --set bluetooth.mode FIXED_PIN \
  --set bluetooth.fixed_pin 123456
```

```text {.no-copy}
Set lora.region to ANZ
Setting device owner to Desk V4 and short name to DV4
Set bluetooth.mode to FIXED_PIN
Set bluetooth.fixed_pin to 123456
Writing modified preferences to device
```

</div>

Confirm region:

<div class="run" markdown>

```bash
meshtastic --port /dev/ttyACM0 --get lora.region
```

```text {.no-copy}
lora.region: 6
```

</div>

(`6` is ANZ. Port may be `/dev/ttyACM1` after reconnect.)

Change `123456` before you take the node off the desk — it is the Meshtastic default fixed PIN.

## Web client (optional)

1. Close the flasher so it releases serial.
2. Open [client.meshtastic.org](https://client.meshtastic.org/) in Chrome / Chromium / Edge.
3. **Add Connection** → **Serial** → Connect.
4. **Settings** → **LoRa** → **Region** → **ANZ** → **Save**.

Optional: match channel / PSK to the mesh you join.

Next: [Phone app](phone.md).
