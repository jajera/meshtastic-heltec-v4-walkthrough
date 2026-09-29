# Hooks

Kiro v1 hooks ([reference](https://kiro.dev/docs/hooks/)). Pattern adapted from
[aws-route53-central-outbound](https://github.com/jajera/aws-route53-central-outbound)
(AWS mutation guard omitted — this repo has no cloud lab).

| File | Trigger | Blocks | Purpose |
| --- | --- | --- | --- |
| `cite-product-claims.json` | `PostFileSave` | no | Reminds the agent to ground Heltec/Meshtastic claims after editing `docs/**` |
| `format-markdown-tables.json` | `PostFileSave` | no | Repairs broken GFM tables in dirty Markdown |
