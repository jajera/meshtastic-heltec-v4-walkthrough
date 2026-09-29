# meshtastic-heltec-v4-walkthrough

Flash and first setup for Heltec WiFi LoRa 32 **V4** on Meshtastic (and how **V4 R8** differs).

**Live (after Pages + DNS):** <https://meshtastic-heltec-v4-walkthrough.johna.kiwi/>

## Stack

- [Zensical](https://zensical.org/) + Patina
- GitHub Pages via `actionsforge` `zensical-pages-deploy`
- Agent context: `AGENTS.md`, `.kiro/steering/`, `.cursor/rules/`

## Quick start

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/zensical serve
```

Build:

```bash
.venv/bin/zensical build
```
