#!/usr/bin/env bash
# ==============================================================================
# 3-LAYER SYSTEM INITIALIZATION SCRIPT (Windows Repository Routing)
# Coordinates folders, establishes default files, templates, and quarantine.
# Targets the absolute path of DiegoOS_Vault directly.
# ==============================================================================

set -euo pipefail

# Absolute path configuration for your Windows setup
VAULT_DIR="/c/ReposGitHub/DiegoOS_Desktop/DiegoOS_Vault"

echo "Initializing 3-Layer System Directory Architecture inside:"
echo "-> $VAULT_DIR"

# 1. Directory Shell Execution targeting the Vault safely
mkdir -p "$VAULT_DIR/01_Peripheral_Layer/Daily_Logs"
mkdir -p "$VAULT_DIR/02_Inner_Layer/Conceptual_Notes"
mkdir -p "$VAULT_DIR/02_Inner_Layer/Literature_Anatomy"
mkdir -p "$VAULT_DIR/03_Outer_Layer/Dashboards"
mkdir -p "$VAULT_DIR/03_Outer_Layer/Active_Missions"
mkdir -p "$VAULT_DIR/_Cold_Storage"

echo "Directory hierarchy constructed."

# 2. Initialize Layer 1: System Diagnostics Ledger
cat << 'EOF' > "$VAULT_DIR/01_Peripheral_Layer/System_Diagnostics.md"
---
type: diagnostic_ledger
status: active
layer: 01_peripheral
---

# System Diagnostics Ledger

Use this register to document workflow drift, deadline compression, or systemic friction. 
Treat failures strictly as technical telemetry to guide future optimization.

| Timestamp | Project Target | Friction Category | Observed Drift / System Failure |
| :--- | :--- | :--- | :--- |
| 2026-05-23 01:55 | [System Init] | System Transition | Initializing clean 3-layer layout; historical archive quarantined. |

EOF

# 3. Initialize Layer 3: System Prompts (The System Constitution)
cat << 'EOF' > "$VAULT_DIR/03_Outer_Layer/System_Prompts.md"
---
type: system_prompt
layer: 03_outer
status: active
---

# System Prompts & Directives

## 1. Objective
Protect absolute human authorial sovereignty, eliminate deadline compression, and maximize AI token efficiency.

## 2. Interaction Constraints (System Guardrails)
* **Reject Prose Inflation:** Truncate all conversational filler, meta-commentary, or politeness routines. 
* **Enforce Conceptual Friction:** If prompt logic attempts to offload primary reasoning or conceptual formulation, flag potential loss of rigor immediately.
* **Scannability First:** Prioritize clear headings, bullet points, and highly dense tables over paragraphs.
* **Context Boundary Rules:** Work strictly within the provided prompt parameters. Do not reference external vault structures or historical files unless commanded.

## 3. Operations Protocol
* **Inner Layer (02_Inner):** Human-led creation, high-friction development, no AI processing.
* **Outer Layer (03_Outer):** AI-assisted packaging, strict constraint parsing, formatting, compression, and $T-1$ deadline compliance checking.

EOF

# 4. Initialize Layer 3: Active Mission Template with Frontmatter Logic
cat << 'EOF' > "$VAULT_DIR/03_Outer_Layer/Active_Missions/Template_Mission.md"
---
system_layer: 03_Outer
project_id: "YYYY_ProjectName"
status: active # [active | cold_storage | stabilized]
deadlines:
  portal_submission: YYYY-MM-DD
  t_minus_1_freeze: YYYY-MM-DD # Automatically calculated: portal_submission minus 24h
ai_engagement:
  allowance: restricted # [syntax_only | cadence_compression | structural_audit | restricted]
  gatekeeper_prompt: "03_Outer_Layer/System_Prompts.md"
conceptual_anchor: "02_Inner_Layer/Conceptual_Notes/Anchor_Note.md"
---

# Project Name: Mission File

## 1. Outer Layer Execution Pipeline
* **Target Objective:** [Define submission goal]
* **Syntactical Constraint:** [Character/word counts, specific institutional rules]

## 2. Structural Assembly Area
## 3. System Validation Checks
- [ ] Layer 2 Conceptual Anchor verified and linked?
- [ ] Current date < `t_minus_1_freeze`?
- [ ] AI execution limited to syntax/cadence?

EOF

echo "System initialized successfully. Place old files in _Cold_Storage/ for quarantine."