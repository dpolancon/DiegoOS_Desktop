# LocalNotion Next-Action Hygiene Bundle

This bundle contains two repo-ready artifacts.

## Files

1. `NEXT_ACTION_HYGIENE_AIM_MAP.md`

A durable specification file. Place it in the repo, recommended path:

`docs/localnotion/NEXT_ACTION_HYGIENE_AIM_MAP.md`

2. `CODEX_ROUTER_PROMPT_NEXT_ACTION_HYGIENE.md`

A short Codex prompt. It tells Codex to read the aim map from the repo and implement the pass from that document.

## Recommended workflow

1. Create the folder if needed:

`docs/localnotion/`

2. Copy `NEXT_ACTION_HYGIENE_AIM_MAP.md` into:

`docs/localnotion/NEXT_ACTION_HYGIENE_AIM_MAP.md`

3. Open Codex from the vault/repo root.

4. Paste the content of:

`CODEX_ROUTER_PROMPT_NEXT_ACTION_HYGIENE.md`

5. Let Codex route through the repo artifact instead of pasting a very long prompt.

## Purpose

This keeps the Codex prompt parsimonious while preserving a detailed, inspectable, versionable aim map inside the repo.
