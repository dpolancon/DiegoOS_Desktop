Codex Task — Route Through Aim Map

AIM TOGGLE: next_action_hygiene

You are working inside my local Obsidian vault for the DiegoOS / LocalNotion system.

Primary instruction source:

"C:\ReposGitHub\DiegoOS_Desktop\DiegoOS_Vault\NEXT_ACTION_HYGIENE_AIM_MAP.md"

Read that file first. Treat it as the binding task specification for this pass.

Do not proceed from memory. Do not redesign the system. Do not expand scope.

Your task is to implement the pass defined in the aim map.

Minimum expected outputs:

- `system/scripts/normalize_next_actions.py`
- patched `system/scripts/update_dashboard_from_cards.py` only if needed to render action fields
- updated `03_Outer_Layer/Dashboards/Active_Dashboard.md`
- `NEXT_ACTION_HYGIENE_AUDIT.csv`
- `NEXT_ACTION_HYGIENE_REPORT.md`
- backups under `system/backups/next_action_hygiene/YYYY-MM-DD/` before any mutation

Hard constraints:

- No file deletion.
- No file moves.
- Do not touch `_Cold_Storage`.
- Do not rewrite card bodies.
- Do not rewrite daily logs.
- Do not rewrite conceptual notes.
- Do not change deadlines.
- Do not invent next actions.
- Default to dry-run unless `--apply` is explicitly used.
- Test cards remain excluded by default.
- Preserve Windows and Obsidian compatibility.

Run the command sequence required by the aim map.

After completion, report:

1. Files changed.
2. Cards inspected, modified, and skipped.
3. Action status assigned to each visible active card.
4. Whether Simon Fraser stale action was flagged.
5. Whether LSE and Norwich now have governed action states.
6. Whether test cards remain excluded.
7. Whether backups were created.
8. Commands run and results.
9. Remaining risks.
10. Recommended next pass.

Do not claim success unless the acceptance criteria in the aim map pass.
