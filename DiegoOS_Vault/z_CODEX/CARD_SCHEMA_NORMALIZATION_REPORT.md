# Card Schema Normalization Report

Date: 2026-05-23
Vault root: `C:\ReposGitHub\DiegoOS_Desktop\DiegoOS_Vault`

## Summary

Normalized active mission/application card frontmatter so the card-driven dashboard has meaningful control-surface columns. This pass changed frontmatter only. Card bodies, daily logs, conceptual notes, and `_Cold_Storage` were not modified.

Created a dedicated normalizer:

* `system/scripts/normalize_card_frontmatter.py`

The normalizer defaults to dry-run, supports `--apply`, skips test cards unless `--include-tests` is passed, and creates backups before writing changed cards.

## Files changed

Scripts and audit/report files:

* `system/scripts/normalize_card_frontmatter.py`
* `CARD_SCHEMA_NORMALIZATION_AUDIT.csv`
* `CARD_SCHEMA_NORMALIZATION_REPORT.md`
* `DASHBOARD_CARD_AUDIT.csv`
* `03_Outer_Layer/Dashboards/Active_Dashboard.md`

Frontmatter-only card changes:

* `03_Outer_Layer/Active_Missions/JinanU_3yPostdoc_IERS.md`
* `03_Outer_Layer/Active_Missions/LSE_Fellow_position.md`
* `03_Outer_Layer/Active_Missions/Norwhich_global_development.md`
* `03_Outer_Layer/Active_Missions/Oxford_OSGA_application_card.md`
* `03_Outer_Layer/Active_Missions/Simon_Fraser_VisitingScholar.md`

Backups created:

* `system/backups/card_frontmatter/2026-05-23/JinanU_3yPostdoc_IERS.md.bak.md`
* `system/backups/card_frontmatter/2026-05-23/LSE_Fellow_position.md.bak.md`
* `system/backups/card_frontmatter/2026-05-23/Norwhich_global_development.md.bak.md`
* `system/backups/card_frontmatter/2026-05-23/Oxford_OSGA_application_card.md.bak.md`
* `system/backups/card_frontmatter/2026-05-23/Simon_Fraser_VisitingScholar.md.bak.md`
* `system/backups/card_frontmatter/2026-05-23/LSE_Fellow_position.md.bak.1.md`
* `system/backups/card_frontmatter/2026-05-23/Norwhich_global_development.md.bak.1.md`

## Cards inspected

Seven cards were inspected under `03_Outer_Layer/Active_Missions/`.

| File | Classification | Result |
| --- | --- | --- |
| `2026_Test_Project.md` | test card | skipped |
| `2026_Test_Proposal.md` | test card | skipped |
| `JinanU_3yPostdoc_IERS.md` | active application card | modified |
| `LSE_Fellow_position.md` | active application card | modified |
| `Norwhich_global_development.md` | active application card | modified |
| `Oxford_OSGA_application_card.md` | active application card | modified |
| `Simon_Fraser_VisitingScholar.md` | active application card | modified |

## Cards modified

Five distinct active cards were modified.

Normalized fields included:

* `type: application_card`
* `priority: standard` where missing
* `lane: applications`
* `institution`
* `role`
* `materials_status`
* `dashboard_visible: true`
* `deadlines.portal_submission`
* `deadlines.t_minus_1_freeze`
* `last_reviewed: "2026-05-23"`

The body comparison check passed for all backup files, confirming card bodies were unchanged.

## Cards skipped

Two test cards were skipped by default:

* `2026_Test_Project.md`
* `2026_Test_Proposal.md`

They were not modified. The dashboard compiler still excludes them by default. The optional `--include-tests` dashboard run included them and marked them as `TEST`.

## Fields normalized

All five active dashboard cards now have populated dashboard-facing fields:

| Card | Lane | Institution | Role | Materials |
| --- | --- | --- | --- | --- |
| `Simon_Fraser_VisitingScholar.md` | `applications` | Department of Economics, Simon Fraser University (SFU) | Farley Distinguished Visiting Scholar in Economic History | `research_statement_cv_and_degree_certificates` |
| `Norwhich_global_development.md` | `applications` | University of East Anglia (UEA), Faculty of Social Sciences, School of Global Development | Teaching Fellow in Global Development (Ref: ATS1352) | `cv_and_personal_statement` |
| `LSE_Fellow_position.md` | `applications` | London School of Economics and Political Science (LSE) | LSE Fellow (Band 6) in Economic History | `cv_and_cover_letter` |
| `Oxford_OSGA_application_card.md` | `applications` | Oxford School of Global and Area Studies (OSGA), University of Oxford | Departmental Lecturer in Global and Area Studies | `cv_and_supporting_statement_only` |
| `JinanU_3yPostdoc_IERS.md` | `applications` | Institute for Economic and Social Research (IESR), Jinan University | International Research Fellow | `research_statement_cv_and_degree_certificates` |

## Deadline conversions

Legacy top-level deadline fields were converted to canonical nested fields:

* `JinanU_3yPostdoc_IERS.md`
  * `deadline: 2026-12-31` to `deadlines.portal_submission: "2026-12-31"`
  * derived `deadlines.t_minus_1_freeze: "2026-12-30"`
* `Oxford_OSGA_application_card.md`
  * `deadline: 2026-06-15` to `deadlines.portal_submission: "2026-06-15"`
  * derived `deadlines.t_minus_1_freeze: "2026-06-14"`
* `Simon_Fraser_VisitingScholar.md`
  * `deadline: 2026-05-31` to `deadlines.portal_submission: "2026-05-31"`
  * `t_minus_1_freeze: 2026-05-30` to `deadlines.t_minus_1_freeze: "2026-05-30"`

Cards that already had nested deadlines retained them, now emitted as quoted date strings.

Verification:

* `rg -n "^deadline:|^t_minus_1_freeze:" 03_Outer_Layer\Active_Missions --glob '*.md'`
  * Result: no top-level legacy deadline fields found.

## Institution and role inference

Institution and role values were inferred only from explicit Snapshot fields or clear card titles/body text.

No `TODO` institution or role values were needed for the five active cards.

Materials inference:

* Jinan, Oxford, and Simon Fraser used existing `output_target`.
* LSE used explicit body text naming CV and covering letter.
* Norwich/UEA used explicit body text naming CV and personal statement.

## Dashboard result after normalization

Command:

* `python system\scripts\update_dashboard_from_cards.py --dry-run --current-date 2026-05-23`

Result:

* Cards parsed: 7
* Cards included: 5
* Cards skipped: 2
* Metadata repair items: 0

The active dashboard now displays populated values for lane, institution, role, and materials across the five visible cards. Test cards remain excluded by default.

## Commands run

Inspection and dry-run:

* `python system\scripts\normalize_card_frontmatter.py --dry-run --current-date 2026-05-23`
  * Result: passed.
  * Initial dry-run: 7 inspected, 5 proposed modifications, 2 skipped test cards.
* `python system\scripts\normalize_card_frontmatter.py --apply --current-date 2026-05-23`
  * Result: passed.
  * Initial apply: 5 modified, 2 skipped; backups created.
* `python system\scripts\normalize_card_frontmatter.py --dry-run --current-date 2026-05-23`
  * Result: passed.
  * Refinement dry-run: 2 proposed materials-status changes, 2 skipped test cards.
* `python system\scripts\normalize_card_frontmatter.py --apply --current-date 2026-05-23`
  * Result: passed.
  * Refinement apply: 2 modified, 2 skipped; incremental backups created.

Dashboard and validation:

* `python system\scripts\update_dashboard_from_cards.py --dry-run --current-date 2026-05-23`
  * Result: passed; 7 parsed, 5 included, 2 skipped, 0 repair.
* `python system\scripts\update_dashboard_from_cards.py --current-date 2026-05-23`
  * Result: passed; dashboard and `DASHBOARD_CARD_AUDIT.csv` written.
* `python system\scripts\validate_frontmatter.py`
  * Result: passed; `38 frontmatter block(s), 51 active markdown file(s) checked.`
* `python system\scripts\update_dashboard_from_cards.py --include-tests --dry-run --current-date 2026-05-23`
  * Result: passed; 7 parsed, 7 included, 0 skipped, 0 repair; test cards marked `TEST`.

Safety checks:

* body comparison across backup files and current cards
  * Result: passed for 7 backup files.
* CSV parse check for `CARD_SCHEMA_NORMALIZATION_AUDIT.csv`
  * Result: passed; 7 rows, 5 changed, 2 skipped.

## Remaining risks

* `Simon_Fraser_VisitingScholar.md` still has a stale `next_action` mentioning "before review starts on May 4" while the reference date is 2026-05-23. This was flagged but not rewritten.
* `LSE_Fellow_position.md` and `Norwhich_global_development.md` still have `next_action: N/A` in the dashboard because no safe replacement was already present in frontmatter.
* `state: parked` remains preserved on Simon Fraser while `status: pipeline_eval` keeps it visible. A future pass should decide whether `state` should also affect dashboard filtering.
* Test cards remain intentionally unnormalized because default behavior skips them.
* `output_target` was preserved for backward compatibility where it already existed, while `materials_status` is now the dashboard-facing canonical field.

## Recommended next pass

Run a narrow next-action hygiene pass:

* add `next_action_date` where it is explicitly known;
* replace stale `next_action` only when a current action is already present in the card;
* decide whether `state: parked` should hide or visually mark otherwise active cards;
* optionally normalize test-card frontmatter with `dashboard_visible: false` if test fixtures should become self-documenting.
