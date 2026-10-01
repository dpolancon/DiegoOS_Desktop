---
type: handoff_note
status: active
layer: implementation_precheck
design_role: work_resumption
scope: chapter2_core
created: 2026-06-08
topic: "Next tasks after locking distribution-conditioned q-index identification"
---
# Handoff — Next Tasks for q-Index Implementation

## What was locked

The Chapter 2 vault now treats the accumulated distribution-conditioned capital-growth index as the binding benchmark object for identifying the time-varying transformation elasticity.

The old level-interaction route,

$$
\omega_t k_t
$$

is superseded as the benchmark. It may remain only as a rejected, historical, or exploratory comparison.

The binding aggregate object is:

$$
q_t^{\omega,h}
=
\sum_{s=1}^{t}
m_{s-1}^{(h)}\Delta k_s.
$$

The benchmark relation is:

$$
y_t^p
=
\alpha
+
\theta_0 k_t
+
\theta_\omega q_t^{\omega,h}
+
\nu_t.
$$

The implied time-varying transformation coefficient is:

$$
\theta_t
=
\theta_0
+
\theta_\omega m_{t-1}^{(h)}.
$$

A00, A03, A05, econometric notes, data-measurement notes, implementation notes, and paper-facing notes were patched accordingly. The governing rule, audit report, and patch ledger were committed and merged into `main` through PR #2.

S40 remains blocked. No S40 reconstruction should be opened until S30/S32 human review promotes a corrected coefficient object.

---

## Next protected deliverable

Build the first q-index implementation and diagnostic package.

The goal is not yet estimation. The goal is to create the generated variables and decide whether they are empirically feasible enough to enter S30/S32 estimation.

Protected output:

> A q-index construction and feasibility diagnostic package for aggregate and machinery-channel specifications.

## Immediate task sequence

### 1. Identify source variables

Start from the current U.S. source-of-truth dataset.

Confirm the exact variable names for:

- productive-capacity target or proxy, if already present;
- aggregate productive capital stock;
- machinery/equipment capital stock;
- nonresidential construction or structures capital stock;
- wage share;
- profit share, if available;
- year/time index.

Do not construct indexes until the exact source columns are confirmed.

Create a small variable provenance table listing:

```text
target_variable
source_column
transformation
price_basis
notes
```
