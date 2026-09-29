---
inclusion: always
---

# Product

`meshtastic-heltec-v4-walkthrough` is a Zensical guide for flashing and first-configuring a
**Heltec WiFi LoRa 32 V4** (and distinguishing **V4 R8**) with official Meshtastic firmware.

## The story

Brand-new board on the desk. Confirm plain V4 vs V4 R8, enter bootloader, flash with the
Meshtastic web flasher (matching target), reset, set region, then prove the node is alive.

Live evidence on this repo used a **plain V4** (2MB PSRAM). R8 remains documented as a
different target — do not collapse them.

## Audience

Someone with the board, a data USB-C cable, and a Chromium browser — not assumed to know
Meshtastic already.

## Shape of the project

- **Zensical + Patina** docs under `docs/`.
- No Terraform, no cloud lab.
- Live site: `https://meshtastic-heltec-v4-walkthrough.johna.kiwi/`.

## In scope

- Identify hardware (V4 vs V4 R8), bootloader, web flash, first boot, basic config, verify,
  troubleshoot.
- Screenshots and serial notes captured during a live setup pass.

## Out of scope (v1)

- Custom firmware builds / PlatformIO trees.
- MeshCore or Heltec F&T firmware paths.
- Enclosure/solar/GPS accessory deep dives beyond first-config mention.
- Multi-node network design.

## Visual bias

Prefer screenshots, short numbered steps, and tables. One job per page.
