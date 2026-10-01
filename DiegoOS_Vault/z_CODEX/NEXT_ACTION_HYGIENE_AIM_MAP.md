# LocalNotion Next-Action Hygiene — Aim Map

Date: 2026-05-23  
Aim toggle: `next_action_hygiene`  
System: DiegoOS / LocalNotion  
Scope: Active mission/application cards and dashboard action layer

---

## 1. Core Aim

Turn the active LocalNotion dashboard from a deadline/materials ledger into an operational execution surface.

Every visible active mission/application card must have either:

1. a current next action;
2. a dated next action;
3. an explicit action status explaining why it has no current action;
4. or a governed visible-but-parked / waiting / blocked state.

The dashboard should no longer silently show `Next Action: N/A` for active cards without explanation.

---

## 2. Operational Principle

The dashboard must distinguish between:

- active and actionable;
- active but needing next-action definition;
- stale action needing review;
- waiting;
- blocked;
- parked but still visible;
- inactive/closed and normally hidden.

Do not collapse these into generic `N/A`.

---

## 3. Hard Constraints

- Do not delete files.
- Do not move files.
- Do not touch `_Cold_Storage`.
- Do not rewrite card bodies.
- Do not rewrite daily logs.
- Do not rewrite conceptual notes.
- Do not change deadlines.
- Do not change application materials.
- Do not redesign the dashboard beyond minimal action-field rendering.
- Do not invent new next actions unless they are explicitly present in card frontmatter or clearly present in card body text.
- If uncertain, mark the card as needing review rather than inventing content.
- Test cards must remain excluded by default.
- Backups must be created before any frontmatter mutation.
- Preserve Windows compatibility.
- Preserve Obsidian markdown compatibility.
- Use dry-run before apply.

---

## 4. Accepted System State Before This Pass

Previous accepted passes:

1. Vault stabilization pass.
2. Dashboard-from-cards pass.
3. Card schema normalization pass.

Current active dashboard compiler:

`system/scripts/update_dashboard_from_cards.py`

Current active cards:

`03_Outer_Layer/Active_Missions/`

Current dashboard output:

`03_Outer_Layer/Dashboards/Active_Dashboard.md`

Accepted state:

- 7 cards parsed.
- 5 active application cards included.
- 2 test cards excluded by default.
- 0 metadata repair items.
- All visible cards now have:
  - `lane`
  - `institution`
  - `role`
  - `materials_status`
  - canonical nested deadlines
  - `last_reviewed`
- Test cards remain excluded.
- `_Cold_Storage` must not be touched.

Known action-layer problems:

1. `Simon_Fraser_VisitingScholar.md` has a stale `next_action` referring to “before review starts on May 4,” while the reference date is 2026-05-23.
2. `LSE_Fellow_position.md` has `Next Action` as `N/A`.
3. `Norwhich_global_development.md` has `Next Action` as `N/A`.
4. Simon Fraser has `state: parked` while `status: pipeline_eval`, so this pass must define whether parked state affects dashboard visibility.
5. The dashboard does not yet display `action_status` or `next_action_date`.

---

# 5. Aim Map

## Core Aim → Auxiliary Aims → Tasks

---

## Auxiliary Aim A — Define Action-Status Semantics

### Purpose

Create a controlled action-status vocabulary so the dashboard can distinguish different kinds of non-action.

### Required action-status vocabulary

`current`  
The card has a valid next action that can be acted on now.

`needs_next_action`  
The card is active or visible, but no safe current action exists in frontmatter or clearly in the card body.

`stale_needs_review`  
The next action refers to an elapsed date, outdated condition, or no longer-current instruction.

`blocked`  
The card cannot advance until a dependency is resolved.

`waiting`  
The card is waiting on an external response, portal condition, advisor input, institutional reply, or similar event.

`parked_visible`  
The card is intentionally not the immediate work focus but remains visible for monitoring.

`submitted`  
The application has been submitted but remains visible for follow-up.

`closed`  
The card should normally be hidden unless explicitly visible.

### Tasks

A1. Define this vocabulary in the pass report.  
A2. Use only these values for `action_status`.  
A3. Do not invent additional values unless absolutely necessary.  
A4. If a value must be added, document it explicitly in the report.

### Acceptance criteria

- The report contains the full action-status vocabulary.
- Every visible active card receives one valid `action_status`.
- No card is left with unexplained `N/A`.

---

## Auxiliary Aim B — Normalize Action Fields on Visible Cards

### Purpose

Ensure every visible active card has a governed action layer.

### Target fields

- `next_action`
- `next_action_date`
- `action_status`
- `last_action_reviewed`
- `state`

### Tasks

B1. Inspect all cards under `03_Outer_Layer/Active_Missions/`.  
B2. Use the dashboard compiler’s visibility logic to identify visible active cards.  
B3. Inventory for each card:
- `file`
- `id`
- `project_id`
- `type`
- `status`
- `state`
- `priority`
- `lane`
- `institution`
- `role`
- `dashboard_visible`
- `deadlines.portal_submission`
- `deadlines.t_minus_1_freeze`
- `materials_status`
- `next_action`
- `next_action_date`
- `action_status`
- `last_action_reviewed`
- `last_reviewed`
- `conceptual_anchor`

B4. Set `last_action_reviewed` to the supplied `--current-date`.  
B5. Preserve existing `next_action` unless it is exactly `N/A`, blank, or mechanically stale.  
B6. Do not invent replacement actions.  
B7. Add `next_action_date` only when safely inferable.  
B8. If no safe date exists, omit `next_action_date` or leave it blank.

### Acceptance criteria

- All 5 visible active cards have `action_status`.
- All 5 visible active cards have `last_action_reviewed`.
- No active card silently displays `Next Action: N/A` without an explanatory `action_status`.

---

## Auxiliary Aim C — Resolve Stale Action Detection

### Purpose

Flag stale action instructions without fabricating replacement actions.

### Tasks

C1. Detect next actions that refer to dates or conditions already elapsed by the reference date.  
C2. Specifically detect Simon Fraser’s “before review starts on May 4” action as stale when current date is 2026-05-23.  
C3. Preserve the stale action text unless a safe current replacement is already present in card frontmatter/body.  
C4. Set `action_status: stale_needs_review`.  
C5. Set `last_action_reviewed: "2026-05-23"`.  
C6. Add a warning to the audit/report.

### Acceptance criteria

- Simon Fraser is flagged as `stale_needs_review`.
- The stale action is not silently treated as current.
- No replacement action is invented.

---

## Auxiliary Aim D — Govern Cards With Missing Actions

### Purpose

Prevent `Next Action: N/A` from functioning as a silent failure.

### Tasks

D1. Inspect cards where `next_action` is missing, blank, or `N/A`.  
D2. If a safe action exists in frontmatter/body, use it.  
D3. If no safe action exists, set `action_status: needs_next_action`.  
D4. Set `last_action_reviewed` to the supplied current date.  
D5. Do not invent actions.

### Known target cards

- `LSE_Fellow_position.md`
- `Norwhich_global_development.md`

### Acceptance criteria

- LSE no longer has unexplained `N/A`.
- Norwich no longer has unexplained `N/A`.
- Both are either assigned a safe action or marked `needs_next_action`.

---

## Auxiliary Aim E — Define Parked-State Visibility Semantics

### Purpose

Clarify how `state: parked` interacts with dashboard visibility.

### Rule

`status` controls lifecycle.  
`state` controls operational intensity.  
`dashboard_visible` controls visibility.

Therefore:

`status: pipeline_eval` + `state: parked` + `dashboard_visible: true`

means:

visible but parked.

Do not automatically hide a card only because `state: parked`.

Hide a card only if:

- `dashboard_visible: false`; or
- `status` is `archived`, `archive`, `inactive`, `parked`, `done`, `closed`, or `rejected`; or
- it is a test card and `--include-tests` is not passed.

### Tasks

E1. Preserve `state: parked` where already present.  
E2. Do not hide Simon Fraser solely because it is parked.  
E3. If visible and parked with no stronger issue, assign `action_status: parked_visible`.  
E4. If visible and parked but stale, assign the stronger status `stale_needs_review`.  
E5. Document the rule in the report.

### Acceptance criteria

- Simon Fraser remains visible unless explicitly hidden by lifecycle status or `dashboard_visible: false`.
- Parked visibility semantics are documented.
- Parked state is not treated as equivalent to closed/inactive.

---

## Auxiliary Aim F — Patch Dashboard Rendering Minimally

### Purpose

Make action governance visible without redesigning the dashboard.

### Required dashboard additions

Add columns:

- `State`
- `Action Status`
- `Next Action Date`

Recommended dashboard columns:

1. `Mission ID`
2. `Lane`
3. `Status`
4. `State`
5. `Priority`
6. `Institution / Target`
7. `Role / Object`
8. `Submission Deadline`
9. `T-1 Lockout Freeze`
10. `Materials`
11. `Action Status`
12. `Next Action Date`
13. `Next Action`

### Tasks

F1. Patch `system/scripts/update_dashboard_from_cards.py` only enough to display the new fields.  
F2. Preserve current sorting unless adding action-status sorting is trivial and safe.  
F3. If `action_status: stale_needs_review`, visually mark the row or field.  
F4. If `action_status: parked_visible`, visually mark the state/action field but do not hide the card.  
F5. Keep test cards excluded unless `--include-tests` is passed.

### Acceptance criteria

- Dashboard displays `State`, `Action Status`, and `Next Action Date`.
- Dashboard still includes 5 active cards and excludes 2 test cards by default.
- Metadata repair items remain 0.
- Dashboard remains readable as a control surface.

---

## Auxiliary Aim G — Create the Next-Action Hygiene Script

### Purpose

Make the pass reproducible and inspectable.

### Script to create

`system/scripts/normalize_next_actions.py`

### Required CLI

- `python system/scripts/normalize_next_actions.py --dry-run --current-date 2026-05-23`
- `python system/scripts/normalize_next_actions.py --apply --current-date 2026-05-23`

### Required flags

- `--vault-dir PATH`
- `--dry-run`
- `--apply`
- `--include-tests`
- `--current-date YYYY-MM-DD`

### Behavior

G1. Default to dry-run if neither `--dry-run` nor `--apply` is provided.  
G2. `--dry-run` prints intended changes and writes no files.  
G3. `--apply` modifies frontmatter only.  
G4. `--include-tests` allows explicit inspection/normalization of test cards.  
G5. Test cards should remain `dashboard_visible: false` if modified.  
G6. `--current-date` controls `last_action_reviewed` and stale-action checks.  
G7. Use robust vault-root detection:
- normal root is two levels above `system/scripts`;
- verify candidate root by checking:
  - `01_Peripheral_Layer`
  - `02_Inner_Layer`
  - `03_Outer_Layer`
  - `system`
- walk upward as fallback.
G8. Use PyYAML.
G9. If PyYAML is unavailable, fail clearly:
`PyYAML is required for next-action hygiene normalization. Install it or run inside the configured environment.`

### Acceptance criteria

- Script is created.
- It defaults to dry-run.
- It modifies only frontmatter in apply mode.
- It produces clear per-card summaries.
- It handles Windows paths.

---

## Auxiliary Aim H — Preserve Bodies and Create Backups

### Purpose

Protect card content from accidental mutation.

### Tasks

H1. Before writing in `--apply` mode, create backups under:

`system/backups/next_action_hygiene/YYYY-MM-DD/`

H2. Use original filename plus `.bak.md`.  
H3. If backup already exists, append `.bak.1.md`, `.bak.2.md`, etc.  
H4. Preserve markdown body exactly.  
H5. Compare body text against backup after writing and confirm unchanged.

### Acceptance criteria

- Backups are created before mutation.
- Card bodies are unchanged.
- Report records body-preservation check.

---

## Auxiliary Aim I — Generate Audit CSV

### Purpose

Make the pass inspectable without opening every card.

### Output file

`NEXT_ACTION_HYGIENE_AUDIT.csv`

### Required columns

- `file`
- `id`
- `project_id`
- `status`
- `state`
- `dashboard_visible`
- `next_action_before`
- `next_action_after`
- `next_action_date_before`
- `next_action_date_after`
- `action_status_before`
- `action_status_after`
- `last_action_reviewed`
- `stale_flag`
- `changed`
- `warning`

### Acceptance criteria

- CSV is created.
- It includes all inspected cards.
- It clearly flags stale and missing-action cases.

---

## Auxiliary Aim J — Generate Acceptance Report

### Purpose

Document whether the dashboard can now guide execution.

### Output file

`NEXT_ACTION_HYGIENE_REPORT.md`

### Required sections

- `# Next-Action Hygiene Report`
- `## Summary`
- `## Files changed`
- `## Cards inspected`
- `## Cards modified`
- `## Cards skipped`
- `## Action-status vocabulary`
- `## Stale actions found`
- `## Cards needing next action`
- `## Parked-state rule`
- `## Dashboard result`
- `## Commands run`
- `## Remaining risks`
- `## Recommended next pass`

### Required question to answer

Can the dashboard now be used to decide what requires action, what is parked, and what is stale?

### Acceptance criteria

- Report is concrete.
- Commands and results are documented.
- Remaining risks are explicit.

---

# 6. Card-Specific Instructions

## Simon_Fraser_VisitingScholar.md

Known issue:

`next_action` refers to “before review starts on May 4,” while current date is 2026-05-23.

Required treatment:

- Preserve stale `next_action` unless a safe current action is already present elsewhere in the card.
- Set `action_status: stale_needs_review`.
- Set `last_action_reviewed: "2026-05-23"`.
- Preserve `state: parked` if present.
- Do not hide the card solely because `state: parked`.
- Add warning in audit/report:
  - stale action;
  - parked-visible ambiguity preserved.

## LSE_Fellow_position.md

Known issue:

`Next Action` is `N/A`.

Required treatment:

- Inspect body for explicit current next action.
- If none exists, set `action_status: needs_next_action`.
- Set `last_action_reviewed: "2026-05-23"`.
- Do not invent action.

## Norwhich_global_development.md

Known issue:

`Next Action` is `N/A`.

Required treatment:

- Inspect body for explicit current next action.
- If none exists, set `action_status: needs_next_action`.
- Set `last_action_reviewed: "2026-05-23"`.
- Do not invent action.

## Oxford_OSGA_application_card.md

Current next action appears substantive.

Required treatment:

- If the action remains current relative to 2026-05-23, set `action_status: current`.
- Add `next_action_date` only if clearly inferable.
- Set `last_action_reviewed: "2026-05-23"`.

## JinanU_3yPostdoc_IERS.md

Current next action appears substantive.

Required treatment:

- If the action remains current relative to 2026-05-23, set `action_status: current`.
- Add `next_action_date` only if clearly inferable.
- Set `last_action_reviewed: "2026-05-23"`.

---

# 7. Required Commands

Run from the vault root:

1. `python system\scripts\normalize_next_actions.py --dry-run --current-date 2026-05-23`
2. Review dry-run output.
3. `python system\scripts\normalize_next_actions.py --apply --current-date 2026-05-23`
4. `python system\scripts\update_dashboard_from_cards.py --dry-run --current-date 2026-05-23`
5. `python system\scripts\update_dashboard_from_cards.py --current-date 2026-05-23`
6. `python system\scripts\update_dashboard_from_cards.py --include-tests --dry-run --current-date 2026-05-23`
7. `python system\scripts\validate_frontmatter.py`
8. Optional but recommended:
   `python -m py_compile system\scripts\normalize_next_actions.py system\scripts\update_dashboard_from_cards.py`

Remove any generated `__pycache__` test artifacts afterward.

---

# 8. Pass Acceptance Criteria

This pass is successful only if:

- All 5 visible active cards have `action_status`.
- All 5 visible active cards have `last_action_reviewed`.
- LSE and Norwich no longer silently show `Next Action: N/A` without `action_status` explaining why.
- Simon Fraser stale action is flagged as `stale_needs_review`.
- Simon Fraser remains visible unless explicitly hidden by `dashboard_visible` or lifecycle status.
- Oxford and Jinan remain current if their next actions are still valid.
- Test cards remain excluded by default.
- Dashboard still parses 7 cards and includes 5 active cards.
- Metadata repair items remain 0.
- Frontmatter validation passes.
- Backups are created before mutation.
- Card bodies remain unchanged.
- `_Cold_Storage` remains untouched.

---

# 9. Expected Final Codex Response

When finished, Codex should report:

1. Files changed.
2. Whether `normalize_next_actions.py` was created.
3. Whether `update_dashboard_from_cards.py` was changed.
4. How many cards were inspected.
5. How many cards were modified.
6. How many cards were skipped.
7. Action status assigned to each visible card.
8. Whether Simon Fraser stale action was flagged.
9. Whether LSE and Norwich now have governed action states.
10. Whether test cards remain excluded.
11. Whether backups were created.
12. Commands run and results.
13. Remaining risks.
14. Recommended next pass.

Do not overstate success. If an action could not be inferred safely, report that explicitly.
