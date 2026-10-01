---
title: "Pending Tasks — U.S. Regression Estimates and Capacity Utilization Reconstruction"
type: note
status: active
project: Chapter2
layer: workflow_control
scope: "United States data reconstruction, regression estimates, and capacity utilization"
repo: Capacity-Utilization-US_Chile
created: 2026-06-10
updated: 2026-06-10
depends_on:
  - S00_US_BEA_provider_import_validation
  - V00_VariableMenu_US_BEA_Repo
  - V01_DataProvenance_Managment
  - A00_Aggregate_Transformation_Benchmark
tags:
  - chapter2
  - united-states
  - capacity-utilization
  - regression-estimates
  - source-of-truth
  - gpim
  - shaikh-correction
  - wage-share
  - accumulated-index
  - pending-tasks
---
# Pending Tasks — U.S. Regression Estimates and Capacity Utilization Reconstruction

## Purpose

This note records the pending work after the downstream import of the locked U.S. BEA provider menu.

The immediate objective is to move from provider-menu validation toward:

1. U.S. source-of-truth data reconstruction.
    
2. U.S. regression-ready variables.
    
3. Distribution-conditioned transformation estimates.
    
4. Reconstructed productive capacity.
    
5. Reconstructed capacity utilization indices.
    

This note is a task-control layer. It does not replace the analytical foundation notes or the data-management notes.

---

## Current baseline

The upstream BEA provider repo has already been locked and imported through downstream S00.

The downstream `main` branch now contains the S00 import/validation layer for the locked U.S. BEA provider artifacts.

S00 is only an import and validation boundary. It does not construct GPIM stocks, Shaikh-adjusted income variables, distributive variables, accumulated indexes, capacity variables, utilization variables, or econometric outputs.

The next construction passes must preserve the following locks:

- The upstream BEA repo is a provider only.
    
- The downstream U.S.–Chile repo owns analytical construction.
    
- Shaikh-adjusted construction remains blocked pending semantic crosswalk.
    
- Preferred productive-capacity capital is `K_cap = K_ME + K_NRC`.
    
- IPP is excluded from `K_cap` and retained as a frontier conditioner.
    
- Government transportation fixed assets are excluded from private `K_cap` and retained as a public-infrastructure frontier conditioner.
    
- Wage share is the preferred distributive state.
    
- Exploitation rate is an alternative proxy.
    
- The active A00 device is the accumulated distribution-conditioned capital-growth index, not a contemporaneous level interaction.
    

---

## Binding econometric object

The active A00 benchmark is:

 $$  
y_t^p = 

\alpha  
+  
\theta_0 k_t  
+  
\theta_\omega q_t^{\omega,h}  
+  
u_t  
$$

with:

$$  
q_t^{\omega,h}

\sum_{s=1}^{t}  
m_{s-1}^{(h)}  
\Delta k_s  
$$

and:

 $$  
\theta_t

\theta_0  
+  
\theta_\omega m_{t-1}^{(h)}  
$$

The benchmark inherited state is:

$$  
m_{t-1}^{(1)}

\omega_{t-1}  
$$

The three-year and five-year memory states are restricted robustness states. They must not be estimated as unrestricted lag weights.

The old level-interaction route is superseded:

$$  
\omega_t k_t  
$$

Variables such as `omega_x_Kcap`, `omega_x_ME`, `omega_x_NRC`, `e_x_Kcap`, `e_x_ME`, and `e_x_NRC` are diagnostic or superseded only. They must not define A00, coefficient promotion, or S40 reconstruction.

---

# Task sequence

## 1. Lock the vault data-management notes

### Goal

Commit the notes that bind the downstream construction to the updated data-management and econometric operationalization.

### Files

- `chapter2_vault/04_data_measurement/V00_VariableMenu_US_BEA_Repo.md`
    
- `chapter2_vault/04_data_measurement/V01_DataProvenance_Managment.md`
    
### Required checks

-  V00 names `q_omega_*` as the preferred accumulated-index family.
    
-  V00 names `q_e_*` as alternative-proxy robustness.
    
-  V00 demotes `omega_x_*` and `e_x_*` to diagnostic/superseded status only.
    
-  V01 says S00 is import/validation only.
    
-  V01 says later construction must preserve the A00 accumulated-index lock.
    
-  V01 preserves the blocked Shaikh semantic gate.
    
-  `.obsidian/workspace.json` is not staged.
    

### Commit target

```text
Lock U.S. data-management and accumulated-index construction rules
```

---

## 2. Build the Shaikh 2011-release to current-release BEA crosswalk

### Goal

Determine whether Shaikh-style profit-share adjustments can be reconstructed with current BEA releases.

### Status

Blocked until crosswalk passes.

### Required output

A table with:

|Field|Purpose|
|---|---|
|Shaikh object|Named accounting object|
|Formula role|Role inside Shaikh correction|
|2011 BEA table/line/description|Historical release source|
|Current BEA candidate table/line/description|Current release candidate|
|Semantic continuity status|Whether current line matches old role|
|Admissibility decision|Pass, partial, fail, blocked|
|Required action|Manual review, replacement line, formula revision, or unlock|

### Named Shaikh objects to crosswalk

- `BankMonIntPaid_t`
    
- `CorpNFNetImpIntPaid_t`
    
- `CorpImpIntAdj_t`
    
- `GVAcorp_adj_t`
    
- `NOScorp_adj_t`
    
- `VAcorp_adj_t`
    
- `omega_adj_CORP_t`
    
- `pi_adj_res_CORP_t`
    
- `e_adj_CORP_t`
    

### Candidate current BEA lines already gathered

- `T711_L4`
    
- `T711_L44`
    
- `T711_L73`
    
- `T711_L28`
    
- `T711_L52`
    
- `T711_L91`
    
- `T711_L74`
    
- `T711_L53`
### Lock

Until this crosswalk passes, do not construct:

- `BankMonIntPaid`
    
- `CorpNFNetImpIntPaid`
    
- `CorpImpIntAdj_t`
    
- Shaikh-adjusted value added
    
- Shaikh-adjusted operating surplus
    
- Shaikh-adjusted wage share
    
- Shaikh-adjusted profit share
    
- Shaikh-adjusted exploitation rate
    
## 3. Construct S10 U.S. source-of-truth dataset

### Goal

Build the first canonical downstream analytical panel from the imported provider artifacts.

### Input route

Use only:

```text
data/external/us_bea_provider/
```

Do not fetch BEA data again.

Do not ingest raw upstream snapshots except for discrepancy audits.

### Required inputs

- `us_bea_variable_menu_long.csv`
    
- `us_bea_source_provenance_ledger.csv`
    
- `us_bea_variable_menu_locked.csv`
    
- `us_bea_variable_menu_locked.json`
    
- S00 validation report
    
- S00 validation ledger
    

### Required outputs

-  S10 analytical source-of-truth panel.
    
-  S10 construction ledger.
    
-  S10 variable admissibility ledger.
    
-  S10 validation report.
    
-  Clear status labels for constructed, diagnostic, alternative, blocked, and superseded variables.
    

---

## 4. Reconstruct productive-capacity capital

### Goal

Build the U.S. productive-capacity capital objects.

### Preferred baseline

# $$  
K^{cap}_t

K^{ME}_t  
+  
K^{NRC}_t  
$$

### Required objects

- `K_ME`
    
- `K_NRC`
    
- `K_cap`
    
- `k_ME = log(K_ME)`
    
- `k_NRC = log(K_NRC)`
    
- `k_Kcap = log(K_cap)`
    
- `g_K_ME`
    
- `g_K_NRC`
    
- `g_Kcap`
    
- `ME_NRC_gap = log(K_ME) - log(K_NRC)`
    
- `ME_share`
    
- `NRC_share`
    

### Construction variants

-  NFC gross GPIM baseline.
    
-  NFC net GPIM diagnostic.
    
-  CORP comparator.
    
-  Official BEA chained-real diagnostic.
    
-  Gross-vs-net wedge.
    
-  GPIM price-index diagnostics.
    

### Lock

IPP and GOV_TRANS do not enter `K_cap`.

---

## 5. Construct IPP and GOV_TRANS frontier conditioners

### Goal

Retain IPP and government transportation fixed assets as frontier-conditioning variables.

### IPP variables

- `IPP_stock`
    
- `IPP_growth`
    
- `IPP_share_total_fixed_assets`
    
- `IPP_share_capital_plus_IPP`
    
- `IPP_to_Kcap`
    

### GOV_TRANS variables

- `GOV_TRANS_stock`
    
- `GOV_TRANS_growth`
    
- `GOV_TRANS_to_Kcap`
    
- `GOV_TRANS_to_NRC`
    
- `GOV_TRANS_to_ME`
    

### Status

These variables are `frontier_conditioner`, not `direct_productive_capacity_capital`.

### Lock

Do not estimate the additive object as the baseline:

# $$  
g_{Y^p}

\theta g_{Kcap}  
+  
\psi g_{IPP}  
+  
\gamma g_{GOV_TRANS}  
$$

IPP and GOV_TRANS may condition the frontier, but they do not replace the accumulated-index benchmark.

---

## 6. Construct distributive variables

### Goal

Build the wage-share-centered distributive architecture.

### Preferred variables

- `omega_CORP`
    
- `omega_NFC`
    
- `omega_adj_CORP`, only if Shaikh crosswalk unlocks adjusted denominator.
    
- `omega_adj_NFC`, only if implementable.
    

### Derived and diagnostic variables

- `pi_res_CORP = 1 - omega_CORP`
    
- `pi_res_NFC = 1 - omega_NFC`
    
- `pi_NOS_CORP`
    
- `pi_NOS_NFC`
    
- `e_CORP = pi_res_CORP / omega_CORP`
    
- `e_NFC = pi_res_NFC / omega_NFC`
    
- `ln_e_CORP`
    
- `ln_e_NFC`
    

### Lock

The wage share is the preferred distributive state.

The exploitation rate is a controlled alternative proxy. It must not silently replace the wage-share benchmark.

---

## 7. Construct accumulated distribution-conditioned capital-growth indexes

### Goal

Build the variables required by the A00 econometric benchmark.

### Preferred A00 family

- `q_omega_h1_Kcap`
    
- `q_omega_h3_Kcap`
    
- `q_omega_h5_Kcap`
    

### Alternative-proxy family

- `q_e_h1_Kcap`
    
- `q_e_h3_Kcap`
    
- `q_e_h5_Kcap`
    

### Definition

# $$  
q_t^{\omega,h}

\sum_{s=1}^{t}  
m_{s-1}^{(h)}  
\Delta k_s  
$$

### Memory states

|Object|Memory state|Status|
|---|---|---|
|`q_omega_h1_Kcap`|inherited one-period wage share|preferred benchmark|
|`q_omega_h3_Kcap`|restricted three-year wage-share average|robustness|
|`q_omega_h5_Kcap`|restricted five-year wage-share average|robustness|
|`q_e_h1_Kcap`|inherited one-period exploitation rate|alternative proxy|
|`q_e_h3_Kcap`|restricted three-year exploitation-rate average|alternative proxy|
|`q_e_h5_Kcap`|restricted five-year exploitation-rate average|alternative proxy|

### Locks

- No full-sample centering.
    
- No unrestricted lag-weight estimation.
    
- No `omega_t * k_t` benchmark.
    
- No `e_t * k_t` benchmark.
    
- Level interactions are diagnostic or superseded only.
    

---

## 8. Build admissibility and blockage ledgers

### Goal

Make every constructed variable auditable.

### Required status categories

- `constructed`
    
- `preferred_baseline`
    
- `robustness`
    
- `alternative_proxy`
    
- `diagnostic`
    
- `blocked_pending_crosswalk`
    
- `superseded`
    
- `not_in_baseline`
    

### High-priority blocked objects

- Shaikh-adjusted income variables.
    
- Shaikh-adjusted profit-share variables.
    
- Shaikh-adjusted exploitation-rate variables.
    
- Any line-number-only Table 7.11 reconstruction.
    
- Any level-interaction variable promoted as baseline.
    

---

## 9. Re-run integration-order and S30I bottleneck audits

### Goal

Determine whether previous residual-stationarity problems come from data construction, variable definition, sector boundary, or genuine historical behavior.

### Variables to audit

Capital variables:

- `k_ME`
    
- `k_NRC`
    
- `k_Kcap`
    
- `ME_NRC_gap`
    

Accumulated-index variables:

- `q_omega_h1_Kcap`
    
- `q_omega_h3_Kcap`
    
- `q_omega_h5_Kcap`
    
- `q_e_h1_Kcap`
    
- `q_e_h3_Kcap`
    
- `q_e_h5_Kcap`
    

Distribution variables:

- `omega`
    
- `omega_adj`, if admissible.
    
- `e`
    
- `ln_e`
    

Frontier conditioners:

- `IPP_stock`
    
- `IPP_growth`
    
- `GOV_TRANS_stock`
    
- `GOV_TRANS_growth`
    

### Bottleneck questions

-  Is the I(2) risk concentrated in `K_NRC`?
    
-  Does GPIM reduce or amplify integration-order risk?
    
-  Does gross vs net stock choice matter?
    
-  Does NFC vs CORP boundary matter?
    
-  Does `ME_NRC_gap` behave as a lower-order combination?
    
-  Do accumulated indexes inherit problematic integration behavior?
    
-  Does the wage-share state behave differently from exploitation-rate alternatives?
    

---

## 10. Estimate corrected U.S. A00 regressions

### Goal

Estimate the corrected aggregate transformation relation.

### Baseline relation

# $$  
y_t^p

\alpha  
+  
\theta_0 k_t  
+  
\theta_\omega q_t^{\omega,h}  
+  
u_t  
$$

### Estimator hierarchy

|Estimator|Status|
|---|---|
|FM-OLS|Main estimator|
|IM-OLS|Robustness estimator|
|DOLS|Fragility / robustness check|
|Johansen / VECM|System-level robustness only|

### Required model families

- A00 with `q_omega_h1_Kcap`.
    
- A00 with `q_omega_h3_Kcap`.
    
- A00 with `q_omega_h5_Kcap`.
    
- Alternative-proxy A00 with `q_e_h1_Kcap`.
    
- Alternative-proxy A00 with `q_e_h3_Kcap`.
    
- Alternative-proxy A00 with `q_e_h5_Kcap`.
    

### Promotion rule

No coefficient object may enter S40 until S30/S32 human review explicitly promotes it.

---

## 11. Reconstruct transformation coefficient path

### Goal

Construct the time-varying transformation coefficient.

### Formula

# $$  
\hat{\theta}_t

\hat{\theta}_0  
+  
\hat{\theta}_\omega m_{t-1}^{(h)}  
$$

### Required checks

-  Coefficient object promoted by human review.
    
-  Memory state matches estimated model.
    
-  No full-sample centering.
    
-  No level-interaction coefficient substituted for accumulated-index coefficient.
    
-  Robustness paths documented separately.
    

---

## 12. Reconstruct productive capacity

### Goal

Build the estimated productive-capacity series.

### Sequence

$$  
(k_t, q_t^{\omega,h})  
\rightarrow  
(\hat{\theta}_0, \hat{\theta}_\omega)  
\rightarrow  
\hat{\theta}_t  
\rightarrow  
\hat{Y}_t^p  
$$

### Required outputs

- `theta_hat_t`
    
- `Yp_hat_t`
    
- `Yp_hat_growth`
    
- confidence/robustness variants if defensible
    
- promotion/admissibility ledger
    

---

## 13. Reconstruct U.S. capacity utilization index

### Goal

Construct the final U.S. capacity utilization index.

### Formula

# $$  
\hat{\mu}_t

\frac{Y_t}{\hat{Y}_t^p}  
$$

### Anchor lock

The preferred U.S. anchor remains:

# $$  
\mu_{US,1973}

1  
$$

using the FRB maximum-utilization anchor.

The old Fordist-core mean normalization is diagnostic only.

### Required outputs

- `mu_US_A00_qomega_h1`
    
- robustness variants for h3/h5
    
- alternative-proxy variants for q_e only as diagnostics
    
- anchor validation report
    
- comparison against previous S40 series
    
- final S40 admissibility ledger
    

---

# Immediate next actions

## Protected next deliverable

Commit the vault data-management lock.

## Moves

1. Patch V00 Shaikh section into object-first crosswalk format.
    
2. Fix V01 YAML/frontmatter if needed.
    
3. Stage only V00 and V01, then commit.
    

## Do not do yet

- Do not start S10 before the vault lock is committed.
    
- Do not construct Shaikh-adjusted profit share before the crosswalk.
    
- Do not use `omega_x_*` or `e_x_*` as baseline regressors.
    
- Do not re-fetch BEA data.
    
- Do not add `.obsidian/workspace.json`.
    

---

# Parking lot

- Need historical 2011 BEA release descriptions for Shaikh Table 7.11 lines.
    
- Need decision on whether Shaikh-adjusted wage share can be built for NFC or only CORP.
    
- Need GPIM implementation protocol for gross vs net stock variants.
    
- Need decision on official BEA chained-real stock diagnostics.
    
- Need S10 construction ledger schema.
    
- Need promotion rule from S30/S32 estimates into S40 utilization reconstruction.