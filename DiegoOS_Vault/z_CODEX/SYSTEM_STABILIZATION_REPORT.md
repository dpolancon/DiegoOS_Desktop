# DiegoOS / LocalNotion Stabilization Report

Date: 2026-05-23
Vault root: `C:\ReposGitHub\DiegoOS_Desktop\DiegoOS_Vault`

## Summary

This pass stabilized the existing DiegoOS / LocalNotion vault without deleting content, migrating large folder trees, or redesigning the architecture. The active architecture remains:

* `01_Peripheral_Layer/`
* `02_Inner_Layer/`
* `03_Outer_Layer/`
* `system/`
* `_Cold_Storage/`

The main fixes were script-root resolution, live folder-name normalization, frontmatter YAML hardening, Obsidian missing-folder repair, active AI operating-guide placement, and dashboard compile verification.

## Inventory

Top-level vault entries inspected:

* `.obsidian/`
* `01_Peripheral_Layer/`
* `02_Inner_Layer/`
* `03_Outer_Layer/`
* `08_INBOX/`
* `09_ATTACHMENTS/`
* `gemini-scribe/`
* `system/`
* `_Cold_Storage/`
* `_templates/`
* `base_directory.base`

Relevant subfolders:

* `01_Peripheral_Layer/A_Daily_Logs`
* `01_Peripheral_Layer/B_Weekly_Logs`
* `01_Peripheral_Layer/C_Frictions_Logs`
* `01_Peripheral_Layer/System_Diagnosis`
* `01_Peripheral_Layer/System_Guides`
* `02_Inner_Layer/Conceptual_Notes`
* `02_Inner_Layer/Dissertation`
* `02_Inner_Layer/Interesting Positions`
* `02_Inner_Layer/Literature`
* `03_Outer_Layer/Active_Missions`
* `03_Outer_Layer/Dashboards`

Scripts under `system/scripts`:

* `card_tidier.py`
* `interface_purge.py`
* `stage_quarantine.py`
* `validate_frontmatter.py`
* `vault_automation.py`

Obsidian configuration inspected:

* `.obsidian/app.json`
* `.obsidian/appearance.json`
* `.obsidian/backlink.json`
* `.obsidian/command-palette.json`
* `.obsidian/community-plugins.json`
* `.obsidian/core-plugins.json`
* `.obsidian/daily-notes.json`
* `.obsidian/plugins/`
* `.obsidian/themes/`
* `.obsidian/workspace.json`

## Files Changed

* `system/scripts/vault_automation.py`
* `system/scripts/card_tidier.py`
* `system/scripts/validate_frontmatter.py`
* `01_Peripheral_Layer/System_Guides/ingestion_protocols.md`
* `01_Peripheral_Layer/System_Guides/diegoos_architecture.md`
* `01_Peripheral_Layer/System_Guides/AI_Operational_Guidelines.md`
* `03_Outer_Layer/System_Prompts.md`
* `_templates/Template_Today.md`
* `_templates/Template_This_Week.md`
* `_templates/Template_Project.md`
* `_templates/Template_Deliverable.md`
* `_templates/Template_Friction_Entry.md`
* `03_Outer_Layer/Dashboards/Active_Dashboard.md`
* `SYSTEM_STABILIZATION_CHANGELOG.csv`
* `SYSTEM_STABILIZATION_REPORT.md`

Folders created:

* `08_INBOX/`
* `09_ATTACHMENTS/`

## Path-Resolution Fix

`system/scripts/vault_automation.py` previously resolved the default vault root as three levels above `system/scripts`, which could point outside the actual vault. It now resolves two levels above the script path and validates the candidate by checking for the live DiegoOS layer folders. It also walks upward as a fallback if the script is moved.

`--vault-dir <path>` remains supported and is normalized with `abspath` and `expanduser`.

`system/scripts/card_tidier.py` also had a script-safety issue: its default root was the current working directory. It now resolves from the script location unless a caller explicitly passes a vault root.

Commands run:

* `python system\scripts\vault_automation.py --help`
  * Result: passed; command parser displayed expected subcommands.
* `python DiegoOS_Vault\system\scripts\vault_automation.py --help`
  * Result: passed from repository root.
* `python -c "import importlib.util; spec=importlib.util.spec_from_file_location('card_tidier', r'DiegoOS_Vault\system\scripts\card_tidier.py'); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); print(m.DiegoOSCardTidier().vault_root)"`
  * Result: passed; printed `C:\ReposGitHub\DiegoOS_Desktop\DiegoOS_Vault`.

## Folder-Name Normalization

Actual live folders are:

* `01_Peripheral_Layer/A_Daily_Logs`
* `02_Inner_Layer/Literature`

Updated active references:

* `system/scripts/vault_automation.py`
  * `Daily_Logs` to `A_Daily_Logs`
  * `Literature_Anatomy` to `Literature`
* `01_Peripheral_Layer/System_Guides/ingestion_protocols.md`
  * `Daily_Logs` to `A_Daily_Logs`
  * `Literature_Anatomy` to `Literature`
* `01_Peripheral_Layer/System_Guides/diegoos_architecture.md`
  * `Daily_Logs` to `A_Daily_Logs`
  * `Literature_Anatomy` to `Literature`

Dashboard links to source logs were also corrected from `../01_Peripheral_Layer/...` to `../../01_Peripheral_Layer/...` because the dashboard file lives inside `03_Outer_Layer/Dashboards`.

## YAML/Frontmatter Hardening

The following templates now quote `{{date}}` in frontmatter:

* `_templates/Template_Today.md`
* `_templates/Template_This_Week.md`
* `_templates/Template_Project.md`
* `_templates/Template_Deliverable.md`
* `_templates/Template_Friction_Entry.md`

Created `system/scripts/validate_frontmatter.py` to validate active markdown frontmatter with a normal YAML parser while excluding `_Cold_Storage`, `.git`, Obsidian plugins, and Obsidian themes.

Command run:

* `python system\scripts\validate_frontmatter.py`
  * Result: passed; `31 frontmatter block(s), 42 active markdown file(s) checked`.

## Obsidian Settings Check

`.obsidian/app.json` points new files and attachments to:

* `newFileFolderPath`: `08_INBOX`
* `attachmentFolderPath`: `./09_ATTACHMENTS`

Those folders were missing. Minimal fix chosen: create the folders and leave settings unchanged.

Command run:

* `New-Item -ItemType Directory -Force 08_INBOX,09_ATTACHMENTS`
  * Result: passed; both folders created inside the vault.

`.obsidian/daily-notes.json` already points daily notes to `01_Peripheral_Layer/A_Daily_Logs`, which matches the live tree.

## Plugin State

Installed:

* Gemini Scribe `4.9.1`
* Calendar `1.5.10`
* Kanban `2.0.51`
* Tasks `8.0.0`
* Templater `2.20.5`

Enabled:

* `gemini-scribe`
* `calendar`

Recommendation:

Do not enable or disable plugins during stabilization. Kanban, Tasks, and Templater are installed but disabled; enable them only after a deliberate workflow/configuration pass.

## Gemini / AI Operating Guide

Created active guide:

* `01_Peripheral_Layer/System_Guides/AI_Operational_Guidelines.md`

It defines these allowed modes:

* `audit_only`
* `syntax_only`
* `cadence_compression`
* `application_packaging`

It also records the operating guardrails: AI does not define the core argument, introduce new claims, rewrite conceptual notes without explicit instruction, or treat `_Cold_Storage` as active source of truth unless explicitly referenced.

`03_Outer_Layer/System_Prompts.md` was minimally aligned to the same four-mode policy.

## Dashboard Compilation Test

Commands run:

* `python system\scripts\vault_automation.py compile-dashboard`
  * Result: passed.
  * Output path: `C:\ReposGitHub\DiegoOS_Desktop\DiegoOS_Vault\03_Outer_Layer\Dashboards\Active_Dashboard.md`
* `python DiegoOS_Vault\system\scripts\vault_automation.py --vault-dir C:\ReposGitHub\DiegoOS_Desktop\DiegoOS_Vault compile-dashboard`
  * Result: passed from repository root with explicit `--vault-dir`.

Dashboard verification:

* Output is inside the vault.
* Compiler uses `01_Peripheral_Layer/A_Daily_Logs`.
* Compiler no longer depends on `Daily_Logs`.
* Output contains 7 active mission rows from 7 active mission markdown files.
* Pending logistics section is present but has no rows because no matching pending urgency tasks were parsed during this run.

## Obsolete-Path Audit

Search command:

* `rg -n "05_ACTIONS|03_DELIVERABLES|07_CAPACITY_POOL|Daily_Logs|Literature_Anatomy" --glob '!_Cold_Storage/**'`

Patched active broken references:

* `Daily_Logs` in active automation and active guides.
* `Literature_Anatomy` in active automation and active guides.

Left untouched as harmless historical or legacy references:

* `01_Peripheral_Layer/System_Diagnosis/System_Diagnostics_need_update.md`
  * Historical telemetry row mentioning `01_Peripheral_Layer\Daily_Logs\...`.
* `system/scripts/stage_quarantine.py`
  * Legacy staging branch that checks old `05_ACTIONS` only if it exists.
* `01_Peripheral_Layer/A_Daily_Logs/2026-05-11.md`
  * Closed daily log with historical `03_DELIVERABLES/...` pointer.

Search command:

* `rg -n "_Cold_Storage" --glob '!_Cold_Storage/**'`

Classification:

* Active references to `_Cold_Storage` are archive/quarantine behaviors or search exclusions, not active source-of-truth reads.
* The new AI guide explicitly states that `_Cold_Storage` is archive and should not be treated as active source of truth unless explicitly referenced.

## Remaining Risks

* The repository worktree was already dirty before this pass, including many staged adds/deletes and untracked vault folders. This report only documents stabilization changes made during this pass.
* `stage_quarantine.py` still contains legacy-path checks for old root folders such as `02_AREAS` and `05_ACTIONS`. They are inert if those folders do not exist, but the script should be reviewed before any future migration run.
* `card_tidier.py` still archives expired cards into `_Cold_Storage/02_AREAS/Application_Pipeline/legacy`, preserving the existing archive layout. That is consistent with treating `_Cold_Storage` as archive, but a future pass may want a named archive policy.
* The dashboard parser depends on specific checklist syntax for logistics extraction. It now compiles reliably, but broader task parsing was not redesigned.

## Recommended Next Pass

Run a dedicated automation-safety pass on the remaining scripts:

* add dry-run support before any move/delete operation;
* standardize shared vault-root resolution across all scripts;
* review `stage_quarantine.py` and `interface_purge.py` for destructive move behavior;
* decide whether disabled installed plugins, especially Templater and Tasks, should become part of the active LocalNotion workflow.
