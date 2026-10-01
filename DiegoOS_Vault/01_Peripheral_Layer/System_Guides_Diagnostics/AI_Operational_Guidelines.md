---
id: ai_operational_guidelines
status: active
type: operational_guide
layer: peripheral_01
last_updated: "2026-05-23"
---

# AI Operational Guidelines

This guide defines the controlled AI operating modes for DiegoOS / LocalNotion work.

## Allowed Modes

| Mode | Scope |
| --- | --- |
| `audit_only` | Read and diagnose; no rewrite. |
| `syntax_only` | Fix typos, punctuation, markdown, and LaTeX syntax; no substantive rewriting. |
| `cadence_compression` | Compress and improve flow while preserving claims, authorial voice, and conceptual structure. |
| `application_packaging` | Extract role requirements, checklists, deadlines, and materials for job/application workflows. |

## Guardrails

* AI does not define the core argument.
* AI does not introduce new claims.
* AI does not rewrite conceptual notes unless explicitly instructed.
* AI must preserve authorial voice.
* AI should operate from a controlled context packet, not the whole vault by default.
* `_Cold_Storage` is archive and should not be treated as active source of truth unless explicitly referenced.
