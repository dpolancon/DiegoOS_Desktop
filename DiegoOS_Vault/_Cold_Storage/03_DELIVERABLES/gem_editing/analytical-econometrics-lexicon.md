# Analytical Econometrics Lexicon & Jargon Mapping

## 1. Single-Equation Core (Stage S1 - ARDL Grid)
- INSTEAD OF: "The grid search optimization routines find parameter non-uniqueness..."
- USE: "The 500-model ARDL specification space exhibits substantial specification sensitivity and identification fragility."
- INSTEAD OF: "The computer selects different coefficients based on researcher choices..."
- USE: "Long-run parameter estimates are highly dependent on deterministic treatments and information-criterion penalty schedules (AIC, BIC, HQ, ICOMP, RICOMP)."
- INSTEAD OF: "The output-capital multiplier is fluid/unstable..."
- USE: "The recovered parameters reflect a disciplined non-uniqueness that rejects the assumption of an invariant, purely technical production law."

## 2. System-Level Modeling (Stage S2 - VECM)
- INSTEAD OF: "The bivariate model breaks down/fails system optimization..."
- USE: "The bivariate output-capital vector fails the fundamental Johansen rank conditions and companion-matrix stability gates, indicating system-level underidentification."
- INSTEAD OF: "The relationship fails because distribution is missing..."
- USE: "Bivariate cointegration fractures due to severe omitted variable bias (OVB)."
- INSTEAD OF: "We add exploitation after to see how it affects the model..."
- USE: "Joint system survival is achieved exclusively under explicit distributional conditioning, where the logged rate of exploitation ($e_t$) enters the long-run cointegrating space."

## 3. Methodological Framework (Shaikh 1974 / Critique)
- INSTEAD OF: "The utilization residual captures real variance..."
- USE: "The constructed utilization series acts as the stationary component of a flow-stock system, downstream from a distributionally sensitive parameter space."
- INSTEAD OF: "The math models the real production dynamics..."
- USE: "Following classic critiques of aggregate production functions, constant algebraic accounting identities must not be conflated with behavioral or structural laws of production."