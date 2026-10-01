# Application Registry

This registry is the authoritative control layer for the cards in this bundle. Cards should inherit status, priority, deadline, and next action from here before being edited locally.

## Registry Logic

- Central means active command-center application. It owns the application lane until the package is complete.
- Next in lane means ready to activate after the central application is stable.
- Parked means real opportunity, but not allowed to consume new drafting bandwidth this week.
- Submitted successful means the application was completed and logged as done; it is archive-only unless follow-up is needed.
- Closed preserve means the opportunity is no longer active, but its materials remain useful for future applications.

## Registry Table

| ID                       | Application                                          | Status               | Priority | Deadline   | Strategic Role                                                                                                                                                   | Next Action                                                              | Confidence |
| ------------------------ | ---------------------------------------------------- | -------------------- | -------- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ | ---------- |
| uah_fen_gestion_negocios | [[UAH — Academico Gestion y Negocios]]               | submitted_successful | highest  | 2026-05-15 | Local academic track; UAH/FEN becomes the central application around teaching, applied methods, firms/finance/development, and Chile-facing public contribution. | Produce UAH cover letter + targeted CV pass + requested document check.  | high       |
| core                     | [[CORE Econ — Postdoc]]                              | submitted_successful | high     | 2026-05-22 | Second academic/curriculum-facing target after UAH; useful if teaching-first materials can be reused.                                                            | Hold until UAH package exists; then verify role requirements.            | low_medium |
| tue                      | [[TUe — Meta-science Postdoc]]                       | closed_preserve      | medium   | 2026-05-15 | Methods/research-infrastructure adjacency; possible fit through reproducible workflows and science-of-science interest.                                          | Keep parked unless a strong low-cost pivot appears.                      | low        |
| coe                      | [[College of Europe — Academic Assistant]]           | closed_preserve      | low      | 2026-05-18 | International/european studies teaching-administrative option; 100% FTE noted in project log.                                                                    | Do not activate before UAH; verify requirements only if capacity opens.  | low_medium |
| lmu                      | [[LMU — Political Philosophy Postdoc]]               | closed_preserve      | medium   | 2026-05-22 | Political philosophy/state-theory application; strongest if framed through justice traditions, republican freedom, Marxist theory, and teaching breadth.         | Select writing sample and teaching fit only if activated.                | medium     |
| sv                       | [[Southern Voice — Research Officer]]                | submitted_successful | high     | 2026-05-08 | Policy-facing research infrastructure package; generated reusable language for Global Development Center-style policy applications.                              | Keep archived as completed win; reuse only finished fragments.           | high       |
| gdc                      | [[Global Development Center — Policy Analyst GEAPS]] | submitted_successful | high     | —          | Policy analyst application converted from Southern Voice materials; DC/London location and OPT/reallocation notes remain reusable where relevant.                | Keep archived as completed win; preserve final package notes.            | high       |
| kcl                      | [[KCL — POPGOV Research Associate]]                  | closed_preserve      | high     | 2026-05-03 | Theoretical-political economy application around popular government, sovereignty, development, and Global South/Third World distinction.                         | No active work; preserve conceptual materials for future adjacent roles. | high       |

## Registry Warnings

- Southern Voice and Global Development Center are logged as done successfully. Do not reopen them unless a follow-up or confirmation receipt must be filed.
- KCL is closed because the deadline passed, but it is not deleted. Its conceptual architecture should be preserved as a reusable reservoir for political economy, Global South, and sovereignty-focused roles.
- CORE and TUe remain thinly populated because the project registry contains limited role-specific details. Their cards are usable for triage, not submission.
- UAH should not be framed as generic heterodox macroeconomics. The application must translate the profile into teaching contribution, applied methods, firm/finance/development vocabulary, Chilean public-facing research, and institutional fit.
