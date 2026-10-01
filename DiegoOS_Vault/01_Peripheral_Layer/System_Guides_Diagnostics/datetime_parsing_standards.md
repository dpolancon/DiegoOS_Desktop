---
id: datetime_parsing_standards
status: active
type: processing_constitutions
layer: peripheral_01
last_updated: 2026-05-23
---

# Datetime Parsing & Timeline Standardization Sheet

This document outlines the strict logic rules governing how date configurations are evaluated inside the system backend (`vault_automation.py`) to eliminate fallback estimation anomalies and freeze default states.

## 1. Enforced String Formatting

* **Database Core Standard:** All frontmatter array fields containing date telemetry must strictly use single, unified strings matching the `YYYY-MM-DD` (ISO-8601) format standard.
* **Exclusion Framework:** The United States date structure (`MM/DD/YYYY`) is permanently expunged from the automated processing pipeline. System utilities are blocked from defaulting to or falling back upon an ambiguous month-first reading to prevent day/month inversions during script processing.

## 2. Ingestion Processing Hierarchy

When encountering raw input strings harvested from global job board listings, system utilities execute standard translation passes using the following priority order:

1. **Native ISO Check:** `YYYY-MM-DD` (Evaluated with zero processing overhead).
2. **International Matrix Check:** `DD/MM/YYYY` (Directly parsed to verify that day numbers greater than 12 do not break chronological distance calculations).
3. **Textual Date Normalization:** Text-based listings (e.g., "15th June 2026", "01 June 2026").

### Suffix Stripping Pipeline
Before translating text strings into system-readable dates, an automated normalization process isolates the day value and strips away English ordinal suffixes (`st`, `nd`, `rd`, `th`). 

```
[Raw Text Entry: "15th June 2026"] ──► [Strip Suffix: "15 June 2026"] ──► [ISO Map: "2026-06-15"]
```

## 3. Dynamic Timeline & Freeze Metrics 

To maintain proactive, stress-tested application cycles, the system script applies an automated negative time offset calculation whenever an active mission frontmatter block is successfully populated: 
- *T-1 System Freeze Threshold:** The script automatically takes the validated `deadline` parameters and subtracts exactly 24 hours to construct the `t_minus_1_freeze` indicator. * 
- **Operational Control Gate:** Once the system reference date reaches or passes the computed `t_minus_1_freeze` timestamp, modification rules lock down open prose fields, and the Master Dashboard elevates the mission file status to protect file submission integrity.