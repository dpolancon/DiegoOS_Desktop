# Dashboard-from-Cards Pass Report

Date: 2026-05-23
Vault root: `C:\ReposGitHub\DiegoOS_Desktop\DiegoOS_Vault`

## Summary

Created a dedicated card-driven dashboard compiler:

* `system/scripts/update_dashboard_from_cards.py`

The dashboard is now compiled from frontmatter in:

* `03_Outer_Layer/Active_Missions/`

and written to:

* `03_Outer_Layer/Dashboards/Active_Dashboard.md`

The existing `vault_automation.py compile-dashboard` command was preserved and now delegates to the new card compiler. No cards, daily logs, conceptual notes, or `_Cold_Storage` files were rewritten or moved.

## Files changed

* `system/scripts/update_dashboard_from_cards.py`
* `system/scripts/vault_automation.py`
* `03_Outer_Layer/Dashboards/Active_Dashboard.md`
* `DASHBOARD_CARD_AUDIT.csv`
* `DASHBOARD_FROM_CARDS_REPORT.md`

## Card inventory

Seven markdown cards were found under `03_Outer_Layer/Active_Missions/`.

| File | Classification | ID / Project ID | Status | Deadline source | Included |
| --- | --- | --- | --- | --- | --- |
| `2026_Test_Project.md` | test card | `2026_Test_Project` | `active` | `deadlines.portal_submission` | no |
| `2026_Test_Proposal.md` | test card | `2026_Test_Proposal` | `active` | `deadlines.portal_submission` | no |
| `JinanU_3yPostdoc_IERS.md` | active mission/application card | `jnu_iesr_irf` | `pipeline_eval` | legacy `deadline` | yes |
| `LSE_Fellow_position.md` | active mission/application card | `2026_LSE_Fellow` | `active` | `deadlines.portal_submission` | yes |
| `Norwhich_global_development.md` | active mission/application card | `2026_global_development_Norwhich` | `active` | `deadlines.portal_submission` | yes |
| `Oxford_OSGA_application_card.md` | active mission/application card | `oxford_osga_dl` | `pipeline_eval` | legacy `deadline` | yes |
| `Simon_Fraser_VisitingScholar.md` | active mission/application card | `sfu_farley_visiting_scholar` | `pipeline_eval` | legacy `deadline` | yes |

Observed frontmatter keys included:

* `id`
* `project_id`
* `status`
* `priority`
* `complexity`
* `activation_cost`
* `deadline`
* `deadline_time_uk`
* `deadline_status`
* `output_target`
* `next_action`
* `conceptual_anchor`
* `state`
* `system_layer`
* `deadlines.portal_submission`
* `deadlines.t_minus_1_freeze`
* `ai_engagement.allowance`
* `ai_engagement.gatekeeper_prompt`

Not observed in current cards:

* `type`
* `dashboard_visible`
* `lane`
* `institution`
* `role`
* `materials_status`

## Canonical schema

The compiler accepts the target schema:

* `type`: `mission_card` or `application_card`; optional for legacy cards.
* `id` or `project_id`: required.
* `status`: required.
* `priority`: optional; defaults to `standard`.
* `dashboard_visible`: optional; defaults to true unless filtered by status/test rules.
* `lane`: optional.
* `deadlines.portal_submission`: canonical deadline field.
* `deadlines.t_minus_1_freeze`: optional; derived as portal submission minus one day if missing.
* `next_action`: optional; displays `N/A` if missing.
* `institution`: optional.
* `role`: optional.
* `materials_status`: optional.
* `conceptual_anchor`: optional.

Legacy tolerance:

* top-level `portal_submission` is accepted;
* top-level `deadline` is accepted;
* no fake fallback deadline is used.

Cards without a parseable portal deadline are routed to `Cards Needing Metadata Repair`, not the active ledger.

## Filtering rules

Cards are excluded from the main dashboard when:

* status is `test`, `archived`, `archive`, `inactive`, `parked`, `done`, `closed`, or `rejected`;
* `dashboard_visible` is false;
* the card is in a folder named `_tests` or `archive`;
* the filename starts with `_`;
* filename, `id`, or `project_id` contains `test`, unless `--include-tests` is passed;
* required metadata is missing or malformed.

Sort order:

1. parsed submission deadline ascending;
2. priority rank: `critical`, `high`, `standard`, `low`;
3. mission id.

## Dashboard sections

The rendered dashboard contains:

* `# 3-Layer System Master Dashboard`
* last compiled timestamp and reference date
* `## Active Mission Tracking Ledger`
* `## Cards Needing Metadata Repair`, only when repair items exist
* `## Pending Logistics Ledger`

No metadata repair section was rendered in the final dashboard because all seven current cards had parseable frontmatter and deadlines.

The pending logistics parser reads:

* `01_Peripheral_Layer/A_Daily_Logs/`

and recognizes:

* `- [ ] [Task]: description | [Urgency: High]`
* `* [ ] [Task]: description | [Urgency: High]`

No pending logistics matched during this pass, so the dashboard renders:

`No pending logistics parsed from active daily logs.`

## Test-card handling

Chosen option: Option B.

No test cards were modified. The compiler excludes cards whose filename, `id`, or `project_id` contains `test` unless `--include-tests` is passed.

Observed test cards:

* `2026_Test_Project.md`
* `2026_Test_Proposal.md`

Default run:

* cards parsed: 7
* cards included: 5
* cards skipped: 2
* skipped cards: the two test fixtures

`--include-tests` run:

* cards parsed: 7
* cards included: 7
* cards skipped: 0
* test cards were clearly marked as `TEST`

## Commands run

From the vault root:

* `python system\scripts\update_dashboard_from_cards.py --dry-run`
  * Result: passed.
  * Cards parsed: 7.
  * Cards included: 5.
  * Cards skipped: 2.
  * Metadata repair items: 0.
* `python system\scripts\update_dashboard_from_cards.py`
  * Result: passed.
  * Dashboard written to `C:\ReposGitHub\DiegoOS_Desktop\DiegoOS_Vault\03_Outer_Layer\Dashboards\Active_Dashboard.md`.
  * Audit written to `C:\ReposGitHub\DiegoOS_Desktop\DiegoOS_Vault\DASHBOARD_CARD_AUDIT.csv`.
* `python system\scripts\update_dashboard_from_cards.py --current-date 2026-05-23 --dry-run`
  * Result: passed.
  * Cards parsed: 7.
  * Cards included: 5.
  * Cards skipped: 2.
  * Metadata repair items: 0.
* `python system\scripts\update_dashboard_from_cards.py --include-tests --dry-run`
  * Result: passed.
  * Cards parsed: 7.
  * Cards included: 7.
  * Cards skipped: 0.
  * Metadata repair items: 0.
* `python system\scripts\vault_automation.py compile-dashboard`
  * Result: passed.
  * Delegated to `update_dashboard_from_cards.py`.
  * Cards parsed: 7.
  * Cards included: 5.
  * Cards skipped: 2.
  * Metadata repair items: 0.
* `python system\scripts\validate_frontmatter.py`
  * Result: passed.
  * `31 frontmatter block(s), 43 active markdown file(s) checked.`

## Results

The live dashboard now excludes test fixtures by default and is generated from card frontmatter. It includes five active mission/application cards and skips two test cards.

Final dashboard counts:

* Cards parsed: 7
* Cards included: 5
* Cards skipped: 2
* Metadata repair items: 0

## Remaining risks

* Current cards do not yet populate `institution`, `role`, `lane`, or `materials_status`, so those dashboard columns show `N/A` except where legacy `output_target` can fill the materials column.
* Three active cards still use legacy top-level `deadline` rather than canonical `deadlines.portal_submission`.
* The compiler is intentionally frontmatter-driven; it does not extract institution or role from card bodies.
* Pending logistics extraction only recognizes the existing bracketed urgency syntax and does not attempt broader task parsing.

## Recommended next pass

Normalize active card frontmatter fields without touching card bodies:

* add `type: application_card` or `type: mission_card`;
* add `institution`;
* add `role`;
* add `lane`;
* add `materials_status`;
* convert legacy top-level `deadline` fields into `deadlines.portal_submission`;
* decide whether `state: parked` should affect dashboard inclusion separately from `status`.
