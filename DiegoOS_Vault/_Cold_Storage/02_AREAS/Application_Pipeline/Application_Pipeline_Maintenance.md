# Application Pipeline: Usage and Maintenance Guidelines

This document outlines best practices for maintaining the `02_AREAS/Application_Pipeline` to ensure it remains a high-integrity, low-friction system for managing your academic job applications.

## 1. Core Principles
*   **Single Source of Truth:** The Kanban (`01_Kanban`), Dashboard (`00_Dashboard`), and Registry (`00_Application_Registry`) must always reflect each other. Any change in one should trigger a corresponding update in the others.
*   **Timeliness:** Update application statuses immediately upon submission, rejection, interview invitation, or withdrawal.
*   **Capacity Alignment:** Use this pipeline to manage your "three moves max" and "one protected deliverable per day" rules from [[Anti_Overcapacity_Rules]]. Do not overload the system.

## 2. Workflow for New Applications
1.  **Create Card:** For each new application, create a dedicated card in `02_AREAS/Application_Pipeline/Cards/` (e.g., `[[New University — Position.md]]`). Populate its YAML frontmatter with `status`, `deadline`, `next_action`, `fit_signal`, and a `package_checklist`.
2.  **Add to Registry:** Add a new entry to `[[00_Application_Registry]]` with the application name, status, and deadline.
3.  **Update Kanban:** Place the new card in the appropriate column in `[[01_Kanban]]` (e.g., "Active," "Submitted").
4.  **Update Dashboard:** Add the application to `[[00_Dashboard]]` in the relevant section.

## 3. Workflow for Status Updates (Submission, Closure, etc.)
1.  **Update Card:** Modify the `status` and `next_action` properties in the application's card (e.g., `[[CORE Econ — Postdoc]]`).
2.  **Update Registry:** Change the status in `[[00_Application_Registry]]`.
3.  **Move Kanban Card:** Drag and drop the card to the appropriate column in `[[01_Kanban]]` (e.g., "Submitted," "Closed - Preserve").
4.  **Update Dashboard:** Adjust the dashboard to reflect the new status.

## 4. Archiving and Preservation
*   **`closed_preserve`:** Use this status for applications that are no longer active but contain valuable information or contacts you may need to reference later (e.g., for future applications, networking).
*   **Regular Review:** Periodically review `[[00_Dashboard]]` and `[[01_Kanban]]` to ensure all statuses are current and no applications are lingering beyond their natural lifecycle.

## 5. Leveraging Downstream Deliverables
*   **Link Deliverables:** Always link specific deliverables (e.g., `[[pedagogical_profile]]`, `[[mentoring_capacities]]`, `[[strategic_design]]`) to their respective application cards. This provides a clear audit trail and contextualizes supporting documents.
*   **Maintain Consistency:** Ensure that the strategies and narratives developed in your deliverables are consistently reflected in the application materials themselves (Cover Letter, Research Statement, etc.).