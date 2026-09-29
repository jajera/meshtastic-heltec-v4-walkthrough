---
inclusion: always
---

# Tech

## Documentation site

Zensical + `zensical-patina`.

- Python 3 + venv (`requirements.txt`)
- Markdown under `docs/`
- Nav in `zensical.toml` only — never encode order in filenames
- Mermaid via `pymdownx.superfences` custom fence
- GitHub Pages via `actionsforge` `zensical-pages-deploy`
- Custom domain: `meshtastic-heltec-v4-walkthrough.johna.kiwi` (`docs/CNAME` + johna-kiwi-infra)

## Commands

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/zensical serve   # local preview
.venv/bin/zensical build   # CI builds this via the reusable workflow
```

## CI

| Workflow | Purpose |
| --- | --- |
| `docs.yml` | Zensical Pages deploy |
| `markdown-lint.yml` / `commitmsg-conform.yml` | PR hygiene |
| `auto-merge.yml` | Dependabot |

Dependabot watches `github-actions` and `pip` only.
