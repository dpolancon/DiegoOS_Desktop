# Next-Action Hygiene Report

Date: 2026-05-23
Vault root: `C:\ReposGitHub\DiegoOS_Desktop\DiegoOS_Vault`

## Summary

Implemented the next-action hygiene pass defined by `NEXT_ACTION_HYGIENE_AIM_MAP.md`.

The dashboard can now be used to distinguish what requires action, what is current, what is parked, and what is stale. It no longer silently shows unexplained `Next Action: N/A` for the five visible active cards.

Created:

* `system/scripts/normalize_next_actions.py`

Patched:

* `system/scripts/update_dashboard_from_cards.py`

The dashboard now renders:

* `State`
* `Action Status`
* `Next Action Date`

No card bodies, daily logs, conceptual notes, or `_Cold_Storage` files were changed.

## Files changed

Scripts:

* `system/scripts/normalize_next_actions.py`
* `system/scripts/update_dashboard_from_cards.py`

Frontmatter-only card changes:

* `03_Outer_Layer/Active_Missions/JinanU_3yPostdoc_IERS.md`
* `03_Outer_Layer/Active_Missions/LSE_Fellow_position.md`
* `03_Outer_Layer/Active_Missions/Norwhich_global_development.md`
* `03_Outer_Layer/Active_Missions/Oxford_OSGA_application_card.md`
* `03_Outer_Layer/Active_Missions/Simon_Fraser_VisitingScholar.md`

Generated/updated outputs:

* `03_Outer_Layer/Dashboards/Active_Dashboard.md`
* `NEXT_ACTION_HYGIENE_AUDIT.csv`
* `NEXT_ACTION_HYGIENE_REPORT.md`
* `DASHBOARD_CARD_AUDIT.csv`

Backups:

* `system/backups/next_action_hygiene/2026-05-23/JinanU_3yPostdoc_IERS.md.bak.md`
* `system/backups/next_action_hygiene/2026-05-23/LSE_Fellow_position.md.bak.md`
* `system/backups/next_action_hygiene/2026-05-23/Norwhich_global_development.md.bak.md`
* `system/backups/next_action_hygiene/2026-05-23/Oxford_OSGA_application_card.md.bak.md`
* `system/backups/next_action_hygiene/2026-05-23/Simon_Fraser_VisitingScholar.md.bak.md`

## Cards inspected

Seven cards were inspected:

| Card | Visible by default | Result |
| --- | --- | --- |
| `2026_Test_Project.md` | no | skipped as test |
| `2026_Test_Proposal.md` | no | skipped as test |
| `JinanU_3yPostdoc_IERS.md` | yes | action governance added |
| `LSE_Fellow_position.md` | yes | body next action promoted |
| `Norwhich_global_development.md` | yes | body next action promoted |
| `Oxford_OSGA_application_card.md` | yes | action governance added |
| `Simon_Fraser_VisitingScholar.md` | yes | stale action flagged |

## Cards modified

Five visible active cards were modified.

| Card | Action status | Notes |
| --- | --- | --- |
| `JinanU_3yPostdoc_IERS.md` | `current` | Existing frontmatter action preserved. |
| `LSE_Fellow_position.md` | `current` | Explicit body `Next action` promoted to frontmatter. |
| `Norwhich_global_development.md` | `current` | Explicit body `Next action` promoted to frontmatter. |
| `Oxford_OSGA_application_card.md` | `current` | Existing frontmatter action preserved. |
| `Simon_Fraser_VisitingScholar.md` | `stale_needs_review` | Stale May 4 action preserved and flagged. |

## Cards skipped

Two test cards were skipped by default:

* `2026_Test_Project.md`
* `2026_Test_Proposal.md`

They remain excluded from the default dashboard. The `--include-tests` dashboard dry-run still includes them only when explicitly requested and marks them as `TEST`.

## Action-status vocabulary

Controlled vocabulary used by this pass:

* `current`: the card has a valid next action that can be acted on now.
* `needs_next_action`: the card is active or visible, but no safe current action exists in frontmatter or clearly in the card body.
* `stale_needs_review`: the next action refers to an elapsed date, outdated condition, or no longer-current instruction.
* `blocked`: the card cannot advance until a dependency is resolved.
* `waiting`: the card is waiting on an external response, portal condition, advisor input, institutional reply, or similar event.
* `parked_visible`: the card is intentionally not the immediate work focus but remains visible for monitoring.
* `submitted`: the application has been submitted but remains visible for follow-up.
* `closed`: the card should normally be hidden unless explicitly visible.

No extra action-status values were introduced.

## Stale actions found

`Simon_Fraser_VisitingScholar.md` was flagged as stale.

Reason:

* `next_action` says: `Initiate formal match inquiry with Dr. Guillaume Blanc and Dr. Steeve Mongrain before review starts on May 4.`
* Reference date is `2026-05-23`.

Treatment:

* Preserved the stale action text.
* Set `action_status: stale_needs_review`.
* Set `last_action_reviewed: "2026-05-23"`.
* Preserved `state: parked`.
* Kept the card visible because `status: pipeline_eval` and `dashboard_visible: true`.

## Cards needing next action

No visible card remains in an unexplained missing-action state.

LSE and Norwich previously displayed `Next Action: N/A`. Both had explicit body-level `Current Working Block` next actions, so those were promoted to frontmatter:

* `LSE_Fellow_position.md`: `Convert the UAH teaching experience and your core dissertation narrative into an Economic History framework`
* `Norwhich_global_development.md`: `Reframe your Post-Keynesian Structuralist and historical macro-political economy frameworks into the interdisciplinary language of Global Development`

No new action was invented.

## Parked-state rule

Parked-state semantics used in this pass:

* `status` controls lifecycle.
* `state` controls operational intensity.
* `dashboard_visible` controls visibility.

Therefore:

* `status: pipeline_eval` + `state: parked` + `dashboard_visible: true` means visible but parked.
* `state: parked` is not treated as equivalent to closed, inactive, or archived.
* A parked visible card receives `parked_visible` unless a stronger condition applies.
* Simon Fraser received the stronger status `stale_needs_review`.

## Dashboard result

Command:

* `python system\scripts\update_dashboard_from_cards.py --dry-run --current-date 2026-05-23`

Result:

* Cards parsed: 7
* Cards included: 5
* Cards skipped: 2
* Metadata repair items: 0

Dashboard changes:

* Added `State`.
* Added `Action Status`.
* Added `Next Action Date`.
* Marked Simon Fraser as `stale_needs_review`.
* Preserved test-card exclusion by default.

## Commands run

Required command sequence:

* `python system\scripts\normalize_next_actions.py --dry-run --current-date 2026-05-23`
  * Result: passed.
  * Proposed 5 visible card changes and 2 test-card skips.
* `python system\scripts\normalize_next_actions.py --apply --current-date 2026-05-23`
  * Result: initially exited with a body-preservation helper error after writing the first four backed-up cards.
  * Follow-up comparison confirmed actual card bodies were unchanged.
  * The helper was patched to use the same frontmatter boundary logic as the reader.
* `python system\scripts\normalize_next_actions.py --apply --current-date 2026-05-23`
  * Result: passed.
  * Finished Simon Fraser, wrote `NEXT_ACTION_HYGIENE_AUDIT.csv`.
* `python system\scripts\update_dashboard_from_cards.py --dry-run --current-date 2026-05-23`
  * Result: passed; 7 parsed, 5 included, 2 skipped, 0 repair.
* `python system\scripts\update_dashboard_from_cards.py --current-date 2026-05-23`
  * Result: passed; dashboard and `DASHBOARD_CARD_AUDIT.csv` written.
* `python system\scripts\update_dashboard_from_cards.py --include-tests --dry-run --current-date 2026-05-23`
  * Result: passed; 7 parsed, 7 included, 0 skipped, 0 repair; test cards marked `TEST`.
* `python system\scripts\validate_frontmatter.py`
  * Result: passed; `43 frontmatter block(s), 60 active markdown file(s) checked.`
* `python -m py_compile system\scripts\normalize_next_actions.py system\scripts\update_dashboard_from_cards.py`
  * Result: passed.
  * Generated `system/scripts/__pycache__` artifact was removed afterward.

Safety checks:

* Backup/body comparison passed for 5 backup files.
* `NEXT_ACTION_HYGIENE_AUDIT.csv` parsed successfully: 7 rows, 5 changed, 2 skipped, 1 stale.

## Remaining risks

* Simon Fraser still needs human review because the action itself is stale; no replacement action was invented.
* `next_action_date` remains blank for all visible cards because no safe current action date was clearly inferable.
* Oxford has no `state` field, so the dashboard displays `N/A` in the State column for that card.
* Test cards remain ungoverned by default because they were intentionally skipped.
* The dashboard does not sort by action status; it preserves deadline/priority sorting.

## Recommended next pass

Run a narrow action-date and state pass:

* add `next_action_date` only where explicit dates exist;
* decide whether cards with missing `state` should default to `active`;
* decide whether `stale_needs_review` should sort above all other dashboard rows;
* optionally normalize test cards with `dashboard_visible: false` so their exclusion is self-documenting.
