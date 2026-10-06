---
type: "career_mission"
system_layer: "03_Outer"
project_id: "JOB_MARKET_2026_27"
status: "active"
state: "active"
priority: "high"
lane: "career_strategy"
dashboard_visible: "true"
conceptual_anchor: "02_Inner_Layer/Notes/JobMarket_2026_27_Positioning_Strategy"
next_action: "Lock market identity, JMP positioning, and materials hierarchy before further application-specific drafting."
action_status: "current"
last_action_reviewed: "2026-10-06"
last_reviewed: "2026-10-06"
ai_allowance: "application_packaging"
gatekeeper_prompt: "03_Outer_Layer/System_Prompts"
tags:
  - job_market
  - academic_career
  - applications
  - 2026_27
---

# Job Market 2026–27 — Control Mission

---

## Registry Sync

* **Mission Type:** Operational Command & Tracking Hub (Job Market Cycle 2026–2027).
* **Registry Status:** Active Execution Mission.
* **Dashboard Anchor:** [[Dashboard]] (Listed under `## Active`).
* **Governance Directive:** This note is thin, operational, and deadline-driven. It manages dossiers, timelines, application cards, and execution checkpoints.

---

## Mission Objective

Coordinate, track, and package all academic employment dossiers for the 2026–2027 hiring cycle across North American, European, and Latin American institutions, ensuring strict compliance with portal deadlines and preventing profile fragmentation.

---

## Strategic Anchor

* **Conceptual Anchor:** [[JobMarket_2026_27_Positioning_Strategy]]

> [!IMPORTANT] System Boundary
> This note does not redefine research identity. It executes the strategy defined in the Inner Layer anchor.

All portfolio hierarchies, theoretical formulations, research problem definitions, and packaging lanes are strictly authored in and governed by the Inner Layer anchor.

---

## Current State

* **Phase:** Dossier Construction & Early Target Ingestion.
* **Active Dossiers in Pipeline:** 3 active tenure-track applications.
* **Immediate Deadlines:**
  * Franklin & Marshall College: **2026-10-30** (T-24 days)
  * UC Berkeley: **2026-11-02** (T-27 days)
  * John Jay College (CUNY): **2026-11-15** (T-40 days)
* **Readiness Level:** Strategy anchored; individual cards initialized; statement drafting underway.

---

## Active Applications

The following applications are currently live and tracked on the master [[Dashboard]]:

| Application Card | Target Institution | Role & Call Ref | Target Lane | Submission Deadline | Freeze (T-1) | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [[App_HECON_TT_PennUS]] | Franklin & Marshall College | TT Assistant Professor of Economics (`JOE_2026-02_111477725`) | Lane A (Heterodox Econ / LAC) | 2026-10-30 | 2026-10-29 | Draft Phase |
| [[App_Berkley_PE5050]] | UC Berkeley | TT Assistant Professor in Political Economy (`JPF05425`) | Lane B/C (Interdisciplinary PE) | 2026-11-02 | 2026-11-01 | Draft Phase |
| [[APP_JJCC_CUNY]] | John Jay College of Criminal Justice (CUNY) | TT Assistant Professor in Economics (`JJC_ECON_TT_2027`) | Lane A (Heterodox Econ / CUNY) | 2026-11-15 | 2026-11-14 | Draft Phase |

```dataview
TABLE institution, role, portal_submission_deadline AS Deadline, priority AS Priority
FROM "03_Outer_Layer/A_Active_Missions"
WHERE lane = "applications" AND state = "active"
SORT portal_submission_deadline ASC
```

---

## Materials Workstreams

```
                                    [CONTROL MISSION]
                                            │
        ┌───────────────────┬───────────────┴───────────────┬───────────────────┐
        ▼                   ▼                               ▼                   ▼
   [WS-1: JMP]         [WS-2: CV]                   [WS-3: Statements]   [WS-4: Referees]
 Standalone paper     Thematic ordering,             Research, Teaching,  3 letters primed,
   40-55 pages       Econ vs Interdisc.              DEI tailored        portals mapped
```

* **WS-1: Job Market Paper (JMP):**
  * Target: Standalone draft of Chapter 2 (clean math, autonomous introduction and conclusion, 40–55 pages).
  * Status: In preparation.
* **WS-2: Curriculum Vitae:**
  * Target: Align sections with Section 10 of [[JobMarket_2026_27_Positioning_Strategy]] (foreground Flagships, subordinate auxiliary projects).
  * Status: Needs review.
* **WS-3: Core Statements Package:**
  * Master Research Statement (3 pages; Lane variations).
  * Master Teaching Statement (heterodox/pluralist pedagogy; syllabi samples).
  * Institution-specific DEI Statements (UC Berkeley inclusive practices vs. John Jay Seven Principles vs. F&M inclusive community).
* **WS-4: Referee Management:**
  * Referees identified: 3 letters required across all three portals (AP Recruit, Interfolio, CUNY).
  * Referees coordinated with upcoming deadlines.

---

## Current Bottlenecks

1. **JMP Standalone Manuscript Finalization:** Need clean standalone text uncoupled from Chapter 1/3 references for writing-sample uploads.
2. **Berkeley Word Count Constraint:** UC Berkeley enforces a strict 5,000–15,000 word writing sample limit; requires an excerpted version with an abstract of the full work.
3. **Institutional DEI Variation:** Distinct mandates across portals: F&M requires an integrated inclusive paragraph, Berkeley mandates DEI woven across three distinct contribution statements, John Jay requires alignment with its specific Seven Principles.

---

## Next Actions

- [ ] **A-01:** Finalize standalone version of JMP (Chapter 2) and verify word counts.
- [ ] **A-02:** Coordinate with referees regarding the F&M (Oct 30) and Berkeley (Nov 2) deadlines.
- [ ] **A-03:** Draft F&M cover letter and inclusive excellence statement.
- [ ] **A-04:** Draft UC Berkeley Research, Teaching/Mentoring, and Service statements.
- [ ] **A-05:** Draft John Jay cover letter and pluralist teaching statement.
- [ ] **A-06:** Complete administrative forms (UC Berkeley Authorization to Release Information Form).

---

## Review Cadence

* **Frequency:** Weekly operational triage; daily check during final 72 hours before each portal deadline.
* **Next Review Date:** 2026-10-13.
* **Escalation Protocol:** Any mission within 48 hours of deadline without uploaded referee letters or finalized statements moves to `URGENT` priority on [[Dashboard]].
