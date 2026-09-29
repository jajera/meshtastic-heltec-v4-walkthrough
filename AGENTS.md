# Agent Context

Zensical walkthrough for **Heltec WiFi LoRa 32 V4** first flash and Meshtastic setup
(with **V4 R8** as a distinct target) — published at
[meshtastic-heltec-v4-walkthrough.johna.kiwi](https://meshtastic-heltec-v4-walkthrough.johna.kiwi/).

## Read these first

Kiro loads `.kiro/steering/` automatically; other agents should read them directly.
Cursor also has `.cursor/rules/` for the same conventions.

| File | When it applies | What it covers |
| --- | --- | --- |
| `.kiro/steering/product.md` | always | Story, scope, non-goals, visual bias |
| `.kiro/steering/tech.md` | always | Stack, commands, CI |
| `.kiro/steering/structure.md` | always | Layout, reading order, naming |
| `.kiro/steering/source-lock.md` | always | Citation rules, verified facts, open TBDs |
| `.kiro/steering/docs-pattern.md` | `docs/**` | Page shapes for this walkthrough |
| `.kiro/steering/markdown-tables.md` | `docs/**` | GFM table hygiene |
| `.kiro/steering/lab-safety.md` | flash / serial / RF | USB, region, TX caution |

Start readers at **Overview**, then follow nav order through flash and verify.

## Non-negotiables

1. **Cite product behaviour.** Do not invent firmware floors, bootloader steps, or
   region rules from recall — check `source-lock.md` and official Heltec / Meshtastic docs.
2. **Mark unverified work.** Steps not yet run on the physical board stay marked
   unverified until the live evidence pass.
3. **Prefer visuals.** Screenshots, short numbered steps, and tables over paragraphs.
4. **Respect reading order.** Overview → Prerequisites → Identify → Bootloader → Flash →
   First boot → Configure → Phone app → Verify → Troubleshoot → Reference.
5. **R8 is not plain V4.** Firmware target, PSRAM, and Vext GPIO differ — never collapse them.

## Facts that trip people up

- Desk evidence board was **plain V4** (2MB PSRAM) → flash **Heltec V4** / `heltec-v4`.
- V4 R8 (8MB PSRAM) → **Heltec V4 R8** / `heltec-v4-r8-oled`. Wrong way around blanks the OLED.
- V4 dropped CP2102 — enter **bootloader** before the web flasher (USER hold, RST, release USER).
- Web Serial needs **Chrome / Chromium / Edge**, not Firefox.
- First flash: **Full Erase** on, **MESHTASTIC/UI** off (UI-on can request nonexistent `oled-tft`).
- After bootloader entry the serial port name may change — reselect it.
- Set **LoRa region** correctly before transmitting (**ANZ** for NZ 915).
- Firmware floor **≥ 2.7.25** (live pass: 2.7.26.54e0d8d).

The complete list, with sources, is in `.kiro/steering/source-lock.md`.

## Plan of record

`.kiro/specs/meshtastic-heltec-v4-walkthrough/` holds `requirements.md`, `design.md`,
and `tasks.md`. Work phases in order; the live board evidence pass is last.

## Validation

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/zensical build
```
