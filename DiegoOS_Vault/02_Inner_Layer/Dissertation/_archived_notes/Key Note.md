---
type: handoff_note
status: active
layer: analytical_foundation
design_role: work_resumption
scope: chapter2_core
created: 2026-06-07
topic: "Fixing the distribution-conditioned transformation elasticity bottleneck"
---

# Handoff — Fixing the $\theta_t$ Identification Bottleneck

## Core diagnosis

The previous estimation bottleneck came from asking the wrong econometric object to carry the theory.

The rejected route was:

$$
y_t = c + \beta_1 k_t + \beta_2(\omega_t k_t) + \xi_t
$$

with:

$$
\theta_t = \beta_1 + \beta_2 \omega_t
$$

This preserved the desired theoretical claim — $\theta_t$ endogenous to distribution — but implemented it through a fragile level interaction between distribution and the capital-stock level.

Locked diagnosis:

> I interacted the wage share with the capital-stock level and hoped the residual would be stationary.

The issue is not that $\theta_t$ should be constant. The issue is that $\omega_t k_t$ is not the right long-run object for identifying a distribution-conditioned transformation elasticity.

---

## Replacement principle

The corrected route is to identify $\theta_t$ through the accumulated contribution of distribution-conditioned capital accumulation.

Define the distribution-conditioned accumulation index:

$$
q_t^{\omega,h}
=
\sum_{s=1}^{t} m_{s-1}^{(h)} \Delta k_s
$$

where $m_{s-1}^{(h)}$ is the inherited distributive state.

The benchmark specification becomes:

$$
y_t^p
=
\alpha
+
\theta_0 k_t
+
\theta_\omega q_t^{\omega,h}
+
u_t
$$

with implied time-varying transformation coefficient:

$$
\theta_t
=
\theta_0
+
\theta_\omega m_{t-1}^{(h)}
$$

This keeps the theoretical claim alive: $\theta_t$ remains endogenous to distribution. But the interaction now occurs where the theory locates it — in the transformation of capital accumulation into productive capacity — rather than in a contemporaneous multiplication between distribution and the capital-stock level.

---

## Locked specification rule

No full-sample centering in the benchmark.

Use uncentered inherited distribution.

Treat rolling/local centering only as a different specification:

$$
\text{distributive deviation from recent norm}
$$

Memory length is a restricted design parameter disciplined by theory and tested through a pre-specified robustness grid, not freely estimated as an unconstrained MA process.

---

## Immediate note updates

### 1. Patch A00

A00 must be updated first.

Tasks:

- Mark the old $\omega_t k_t$ specification as superseded.
- Preserve the core claim: aggregate $K_t$, time-varying $\theta_t$.
- Replace the baseline econometric device with $q_t^{\omega,h}$.
- Clarify that $\theta_t$ is not freely estimated year by year.
- Define $\theta_t$ as a distribution-conditioned law of motion:

$$
\theta_t
=
\theta_0
+
\theta_\omega m_{t-1}^{(h)}
$$

- Clarify that the benchmark does not use full-sample centering.
- Add the old level interaction to a “superseded / rejected route” subsection.

Suggested replacement language:

> A00 remains the aggregate-capital benchmark with time-varying transformation elasticity. The econometric device is no longer the contemporaneous level interaction $\omega_t k_t$. The benchmark now identifies $\theta_t$ through the accumulated contribution of distribution-conditioned capital accumulation, $q_t^{\omega,h} = \sum_{s=1}^{t}m_{s-1}^{(h)}\Delta k_s$. This preserves the theoretical claim that distribution conditions the transformation elasticity, while locating the interaction in capital accumulation rather than in the capital-stock level.

---

### 2. Patch A03

A03 is mostly compatible with the corrected route.

Tasks:

- Add a bridge subsection explaining that the new A00 index is the aggregate reduced-form counterpart of A03’s growth-rate decomposition.
- Emphasize that A03’s $\theta^N(\pi,s)$ is a growth-rate transformation object.
- Clarify that the accumulated index converts a growth-rate theory into an estimable long-run level relation.
- Make explicit that the A00 index is not a substitute for A03’s two-capital decomposition.

Suggested bridge language:

> The revised A00 accumulation-weighted index is the aggregate reduced-form counterpart of A03’s transformation-elasticity decomposition. A03 defines $\theta^N(\pi,s)$ as the mapping from capital accumulation growth to productive-capacity growth. The A00 index cumulates this logic into a level-compatible econometric object by weighting each capital-growth increment by the inherited distributive state.

---

### 3. Patch A05

A05 currently repeats the old level-interaction logic in the mechanization-bias channel.

Current stale object:

$$
\omega_{m,t}
=
\omega_t m_t
$$

where:

$$
m_t
=
k_t^{ME}
-
k_t^{NRC}
$$

This should not be promoted as the preferred A03 empirical bridge without qualification.

Tasks:

- Mark $\omega_t m_t$ as an exploratory level-interaction candidate, not the preferred corrected route.
- Add an accumulation-weighted machinery channel.
- Preserve the NRC envelope as non-distributive.
- Make distribution operate through machinery accumulation, not through the NRC envelope.

Preferred A05-compatible object:

$$
q_t^{ME,\omega,h}
=
\sum_{s=1}^{t}
m_{s-1}^{(h)}
\Delta k_s^{ME}
$$

where $m_{s-1}^{(h)}$ is the inherited distributive state.

Candidate decomposed specification:

$$
y_t^p
=
\alpha
+
\beta_{NRC}k_t^{NRC}
+
\beta_{ME}k_t^{ME}
+
\beta_{\omega ME}q_t^{ME,\omega,h}
+
u_t
$$

Interpretation:

- $k_t^{NRC}$ captures the extensive envelope.
- $k_t^{ME}$ captures the machinery stock channel.
- $q_t^{ME,\omega,h}$ captures distribution-conditioned machinery accumulation.
- Distribution does not directly interact with the NRC envelope.

Optional ratio-based variant:

$$
q_t^{m,\omega,h}
=
\sum_{s=1}^{t}
m_{s-1}^{(h)}
\Delta m_s
$$

where:

$$
m_s
=
k_s^{ME}
-
k_s^{NRC}
$$

This version is less preferred because the theory locates distribution more directly in the machinery accumulation channel than in the ME/NRC ratio itself.

---

## Memory-state menu

The distributive state $m_{t-1}^{(h)}$ must be pre-specified.

### Benchmark

One-period inherited distribution:

$$
m_{t-1}^{(1)}
=
\omega_{t-1}
$$

### Restricted moving-average robustness

Three-year distributive climate:

$$
m_{t-1}^{(3)}
=
\frac{1}{3}
\left(
\omega_{t-1}
+
\omega_{t-2}
+
\omega_{t-3}
\right)
$$

Five-year distributive climate:

$$
m_{t-1}^{(5)}
=
\frac{1}{5}
\sum_{j=1}^{5}
\omega_{t-j}
$$

### Optional exponential-memory robustness

$$
m_{t-1}^{(\lambda)}
=
(1-\lambda)\omega_{t-1}
+
\lambda m_{t-2}^{(\lambda)}
$$

with restricted values only:

$$
\lambda
\in
\{0.25, 0.50, 0.75\}
$$

Do not estimate unrestricted lag weights in the benchmark.

Rejected unrestricted form:

$$
m_{t-1}
=
a_1\omega_{t-1}
+
a_2\omega_{t-2}
+
a_3\omega_{t-3}
+
\cdots
$$

Reason: this would reintroduce degrees-of-freedom loss, multicollinearity, and specification fishing.

---

## Empirical bottlenecks this fixes

### Bottleneck 1: residual nonstationarity from level interactions

The old object $\omega_t k_t$ created a fragile long-run regressor.

The corrected index uses accumulated weighted increments:

$$
q_t^{\omega,h}
=
q_{t-1}^{\omega,h}
+
m_{t-1}^{(h)}\Delta k_t
$$

This is closer to the theoretical growth closure:

$$
g_{Y^p,t}
=
\theta_t g_{K,t}
$$

### Bottleneck 2: unclear interpretation of $\theta_t$

The old route implied:

$$
\theta_t
=
\beta_1
+
\beta_2\omega_t
$$

but obtained it through a level product.

The corrected route implies:

$$
\theta_t
=
\theta_0
+
\theta_\omega m_{t-1}^{(h)}
$$

through the accumulated transformation of capital growth.

### Bottleneck 3: excessive reliance on Johansen/VECM

Do not move to Johansen as benchmark.

Reason:

- Johansen/VECM estimates the short-run adjustment system.
- It consumes degrees of freedom.
- It is fragile under short annual samples.
- It is not required to identify the single-equation long-run transformation object.

Preferred estimator family:

- FM-OLS
- DOLS
- IM-OLS

Use these for the single-equation cointegrating regression after constructing the corrected index.

### Bottleneck 4: unrestricted MA temptation

Memory length should not be freely estimated.

Use a restricted robustness grid:

$$
h
\in
\{1,3,5\}
$$

Optional exponential-memory grid:

$$
\lambda
\in
\{0.25,0.50,0.75\}
$$

The goal is robustness, not selecting the memory length that mechanically gives the best residual-stationarity outcome.

---

## Next implementation steps

### Step 1 — Patch notes

Patch in order:

1. A00
2. A03
3. A05
4. governing rule note for specification layering

Do not touch S40 until S30/S32 human review promotes a corrected coefficient object.

---

### Step 2 — Create generated variables

For aggregate A00:

$$
q_t^{\omega,1}
=
\sum_{s=1}^{t}
\omega_{s-1}\Delta k_s
$$

$$
q_t^{\omega,3}
=
\sum_{s=1}^{t}
m_{s-1}^{(3)}\Delta k_s
$$

$$
q_t^{\omega,5}
=
\sum_{s=1}^{t}
m_{s-1}^{(5)}\Delta k_s
$$

For decomposed A03/A05:

$$
q_t^{ME,\omega,1}
=
\sum_{s=1}^{t}
\omega_{s-1}\Delta k_s^{ME}
$$

$$
q_t^{ME,\omega,3}
=
\sum_{s=1}^{t}
m_{s-1}^{(3)}\Delta k_s^{ME}
$$

$$
q_t^{ME,\omega,5}
=
\sum_{s=1}^{t}
m_{s-1}^{(5)}\Delta k_s^{ME}
$$

---

### Step 3 — Run feasibility diagnostics before estimation

For each generated index, check:

- missingness and sample loss from lagging;
- integration order;
- correlation with $k_t$;
- VIF / collinearity diagnostics;
- visual inspection of index path;
- sensitivity to capital-stock definition;
- sensitivity to wage-share versus profit-share version.

---

### Step 4 — Estimate corrected single-equation candidates

Aggregate benchmark:

$$
y_t^p
=
\alpha
+
\theta_0 k_t
+
\theta_\omega q_t^{\omega,h}
+
u_t
$$

Decomposed machinery-channel candidate:

$$
y_t^p
=
\alpha
+
\beta_{NRC}k_t^{NRC}
+
\beta_{ME}k_t^{ME}
+
\beta_{\omega ME}q_t^{ME,\omega,h}
+
u_t
$$

Alternative ratio candidate:

$$
y_t^p
=
\alpha
+
\beta_{NRC}k_t^{NRC}
+
\beta_m m_t
+
\beta_{\omega m}q_t^{m,\omega,h}
+
u_t
$$

Estimator family:

- FM-OLS
- DOLS
- IM-OLS

---

### Step 5 — Apply admissibility gates

For every estimated candidate:

- residual ADF stationarity gate;
- Phillips-Ouliaris or equivalent cointegration admissibility gate if available;
- outlier screen;
- dummy robustness only after theoretical adjudication;
- coefficient sign coherence;
- estimator-family agreement;
- historical interpretability.

Do not interpret a coefficient as dissertation-binding only because it passes one gate.

---

## Promotion rule

A corrected specification can only be promoted if it satisfies all of the following:

1. It preserves the theoretical object: $\theta_t$ endogenous to distribution.
2. It avoids the rejected level interaction $\omega_t k_t$ as the benchmark device.
3. Its generated index has a clear timing rule.
4. Its memory filter is pre-specified.
5. Its residuals pass stationarity/admissibility checks.
6. Its coefficients are stable across reasonable estimator variants.
7. Its historical path is interpretable.
8. Human review explicitly promotes it from candidate to reconstruction input.

---

## Locked assessment sentence

The accumulated distribution-conditioned capital-growth index is theoretically superior to the level interaction because it identifies $\theta_t$ where the theory locates it: in the transformation of capital accumulation into productive capacity, not in a contemporaneous multiplication between distribution and the capital-stock level.