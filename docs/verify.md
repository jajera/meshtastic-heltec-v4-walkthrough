# Verify

Prove the node is alive: firmware target, region, then phone over Bluetooth.

## CLI (serial)

Close browser tabs that hold the serial port, then:

<div class="run" markdown>

```bash
meshtastic --port /dev/ttyACM0 --info
```

```text {.no-copy}
Connected to radio
Owner: Desk V4 (DV4)
My info: { … "pioEnv": "heltec-v4", … }
Metadata: { "firmwareVersion": "2.7.26.54e0d8d", "hwModel": "HELTEC_V4", … }
```

</div>

<div class="run" markdown>

```bash
meshtastic --port /dev/ttyACM0 --get lora.region
```

```text {.no-copy}
lora.region: 6
```

</div>

| Check | Expect (this desk) |
| --- | --- |
| `pioEnv` | `heltec-v4` |
| `hwModel` | `HELTEC_V4` |
| `firmwareVersion` | ≥ 2.7.25 (here 2.7.26.54e0d8d) |
| `lora.region` | `6` / ANZ |

## Phone app

Follow the full connect / settings path in [Phone app](phone.md), then confirm:

| Check | Expect |
| --- | --- |
| BLE finds the node | Name matches owner (Desk V4 / DV4) |
| Pair succeeds | Fixed PIN **`123456`** (or OLED PIN) |
| Region in app | **ANZ** |
| Local message | **Messages** → **Primary** → send (for example `ping`) appears locally |
| OLED | Updates / stays awake when you use the node |
| Nodes | Your node listed with battery / last heard |

Wi‑Fi on the node disables Bluetooth on ESP32 — leave Wi‑Fi off for BLE tests.

## Second node (optional — skip with one board)

Needs another Meshtastic node on **ANZ** and the same channel. Not part of this desk pass.

Antennas on before intentional TX. Stuck? [Troubleshoot](troubleshoot.md).
