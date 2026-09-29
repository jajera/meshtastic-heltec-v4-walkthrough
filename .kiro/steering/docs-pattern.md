---
inclusion: fileMatch
fileMatchPattern: "docs/**"
---

# Documentation page pattern

## Shape

1. One H1 (page title).
2. Short lede (outcome for this step).
3. Numbered steps or a symptom table.
4. Screenshot slots under `assets/images/` (use placeholders until the live pass).
5. Link onward to the next nav page — do not repeat other pages.

## Overview (`index.md`)

- What you will do and roughly how long.
- Path cards / links matching nav order.
- Call out R8 vs plain V4.

## Procedural pages

Keep each file one job (bootloader, flash, configure, …). Author the command or UI click;
operator runs it on the desk.

## Troubleshoot

Symptom → likely cause → fix table. No novel procedures that belong on earlier pages.

## Code blocks

Use the route53 `.run` pattern: one command, then its result, each pair in its own card.

````markdown
<div class="run" markdown>

```bash
command here
```

```text {.no-copy}
expected output
```

</div>
````

- Shell the reader runs in `bash` fences.
- Observed output in a following `text {.no-copy}` fence — do not mix stdout into the command.
- One command per `.run` block. Do not stack unrelated commands in a single card.
