# Phone app

Day-to-day control is the **Meshtastic** mobile app over Bluetooth. After [Configure](configure.md) has region, owner, and a fixed PIN, you do not need the web client or serial CLI for normal use.

This desk node is prepared as **Desk V4** / **DV4**, BLE **on**, fixed PIN **`123456`**, region **ANZ**, Wi‑Fi **off**.

## Install

1. Install **Meshtastic** from the Play Store (Android) or App Store (iOS).
2. Grant Bluetooth (and Location if the OS asks — required for BLE scan on many phones).
3. Power the node (USB or battery). Antenna fitted. OLED should show Meshtastic / status.

## Connect and pair

1. Open the app → **Connect** (or the radio / link icon) → **Bluetooth**.
2. Scan and select **Desk V4** (or your owner name; stock name looks like `Meshtastic xxxx`).
3. Enter PIN **`123456`** if you set `FIXED_PIN` under [Configure](configure.md).
4. Wait until the connected card shows the node name, firmware, and battery.

| Check | Expect |
| --- | --- |
| Node in scan list | **Desk V4** / **DV4** (or your rename) |
| Pair | PIN accepted; status Connected |
| Region on device | **ANZ** (set in app if still unset) |

One client at a time: close the web flasher / web client / another phone if the node does not appear. On ESP32, **Wi‑Fi on the node disables Bluetooth** — leave Wi‑Fi off for phone use.

Change `123456` before you take the node off the desk — it is the Meshtastic default fixed PIN.

## First settings in the app

With the phone connected:

1. Open **Settings** (gear) for the connected node.
2. **LoRa** → **Region** → **ANZ** → save (skip if CLI already set it).
3. Optional: **User** → long / short name (match **Desk V4** / **DV4** or your callsign).
4. Optional: **Channels** → Primary — leave default PSK for a private desk test; match a local mesh if you join one.
5. **Position** → GPS / Device GPS **Enabled** if you have a Quectel L76K (or other GNSS) on the Expansion Kit ribbon. This desk unit has GPS mode enabled in firmware config.

Outdoor clear sky helps first GNSS lock. Indoors the app may show the node with empty or stale position until a fix.

## How to use it day to day

| Task | Where in the app |
| --- | --- |
| Send a message | **Messages** → **Primary** → type and send |
| See yourself / neighbours | **Nodes** — tap a node for battery, last heard, position |
| Map | **Map** — your node and others with position appear when GPS (or phone location sharing) has a fix |
| Change region / power / role | **Settings** → **LoRa** / **Device** → save (node may reboot) |
| Bluetooth PIN / name | **Settings** → **Bluetooth** / **User** |
| Disconnect | Connect screen → disconnect (node keeps running on mesh) |

With only one node you will not get a mesh reply to a Primary send; the app should still accept the message and show it locally. A second Meshtastic node on **ANZ** and the same channel is needed for over-the-air delivery.

## Position and the map

If your kit includes a **Quectel L76K** (or other GNSS) on the ribbon — this desk Expansion Kit does — GPS is configuration on **Heltec V4**, not a different flasher image.

1. Take the node outdoors with a clear view of the sky.
2. Confirm **Position** / GPS is enabled in app settings.
3. Wait for a lock (first fix can take several minutes).
4. Open **Map** — your node should move as you walk when smart position / broadcast intervals allow.

Live position sharing on the mesh is the intended use. The app is not a full hiking GPX logger; use a phone trail app if you need an archived track file.

## If connect fails

| Symptom | Fix |
| --- | --- |
| No devices in scan | Power node; Bluetooth on phone; stay near; rescan |
| Node missing after earlier connect | Disconnect other clients; toggle phone Bluetooth; wake OLED (USER) |
| Wrong PIN | OLED random code, or re-set `FIXED_PIN` via [Configure](configure.md) |
| Connects then drops | Keep Wi‑Fi off on the node; avoid sleep during first setup |

More rows: [Troubleshoot](troubleshoot.md).

Next: [Verify](verify.md).
