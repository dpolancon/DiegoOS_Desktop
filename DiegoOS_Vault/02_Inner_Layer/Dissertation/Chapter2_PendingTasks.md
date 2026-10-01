## Pending Tasks — U.S. Regression Estimates and Capacity Utilization Reconstruction

## 1. Lock the vault data-management notes

- [ ] Confirm `V00_VariableMenu_US_BEA_Repo.md` names `q_omega_*` as the preferred A00 accumulated-index family.
- [ ] Confirm `V00_VariableMenu_US_BEA_Repo.md` names `q_e_*` as alternative-proxy robustness only.
- [ ] Confirm `omega_x_*` and `e_x_*` appear only as superseded/diagnostic level interactions.
- [ ] Confirm `V01_DataProvenance_Managment.md` states that S00 is import/validation only.
- [ ] Confirm `V01_DataProvenance_Managment.md` preserves the A00 accumulated-index lock.
- [ ] Confirm the Shaikh layer is described as a blocked current-release protocol, not as an already admissible formula.
- [ ] Repair the V00 Shaikh section into object-first/protocol-first form.
- [ ] Repair YAML/frontmatter in V01 if needed.
- [ ] Verify `.obsidian/workspace.json` is not staged.
- [ ] Stage only V00 and V01.
- [ ] Commit the vault lock.

## 2. Build a current-release Shaikh-style BEA adjustment protocol

- [ ] Reconstruct the logic of Shaikh’s profit-share adjustment as a conceptual accounting target.
- [ ] Treat Shaikh 2011 as the benchmark logic, not as a line-number recipe to copy mechanically.
- [ ] Identify the named Shaikh-style accounting objects: `BankMonIntPaid_t`, `CorpNFNetImpIntPaid_t`, `CorpImpIntAdj_t`, and adjusted derivatives.
- [ ] Review current BEA candidate lines: `T711_L4`, `T711_L44`, `T711_L73`, `T711_L28`, `T711_L52`, `T711_L91`, `T711_L74`, and `T711_L53`.
- [ ] Document each current candidate line’s description, sector/account meaning, coverage, and possible role.
- [ ] Decide whether each current BEA line is admissible for the intended current-release Shaikh-style object.
- [ ] Identify where current BEA semantics force a modification of Shaikh’s original implementation.
- [ ] Build a protocol table with: Shaikh-style object, accounting role, Shaikh benchmark logic, current BEA candidate line, current semantic interpretation, admissibility decision, and proposed treatment.
- [ ] Decide whether `BankMonIntPaid_t` can be reconstructed with current BEA releases.
- [ ] Decide whether `CorpNFNetImpIntPaid_t` can be reconstructed with current BEA releases.
- [ ] Decide whether `CorpImpIntAdj_t` can be constructed without line-number-only assumptions.
- [ ] If a full adjustment is not admissible, define partial, diagnostic, or blocked alternatives.
- [ ] Keep all Shaikh-adjusted variables blocked until the current-release protocol passes.
- [ ] Produce a current-release Shaikh-style adjustment report.
- [ ] Produce a machine-readable admissibility ledger.

## 3. Construct S10 U.S. source-of-truth dataset

- [ ] Read only from `data/external/us_bea_provider/`.
- [ ] Load staged long data, provenance ledger, locked manifest, and JSON manifest.
- [ ] Validate row counts and variable counts against S00.
- [ ] Join staged data to provenance metadata.
- [ ] Assign analytical role tags to all source ingredients.
- [ ] Preserve table-line-unit-vintage provenance.
- [ ] Build the S10 analytical source-of-truth panel.
- [ ] Build an S10 construction ledger.
- [ ] Build an S10 admissibility/blockage ledger.
- [ ] Mark Shaikh-adjusted objects as `blocked_pending_current_release_protocol`.
- [ ] Produce an S10 validation report.
- [ ] Confirm no new BEA fetch occurred.

## 4. Reconstruct productive-capacity capital

- [ ] Construct `K_ME`.
- [ ] Construct `K_NRC`.
- [ ] Construct `K_cap = K_ME + K_NRC`.
- [ ] Construct log variables: `k_ME`, `k_NRC`, `k_Kcap`.
- [ ] Construct growth rates: `g_K_ME`, `g_K_NRC`, `g_Kcap`.
- [ ] Construct `ME_NRC_gap = log(K_ME) - log(K_NRC)`.
- [ ] Construct `ME_share` and `NRC_share`.
- [ ] Build NFC gross GPIM baseline.
- [ ] Build NFC net GPIM diagnostic.
- [ ] Build CORP comparator.
- [ ] Compare GPIM objects against official BEA chained-real diagnostics.
- [ ] Audit gross-vs-net stock choice.
- [ ] Confirm IPP and GOV_TRANS are excluded from `K_cap`.
- [ ] Confirm IPP and GOV_TRANS are retained only as frontier conditioners.

## 5. Construct IPP and GOV_TRANS frontier conditioners

- [ ] Construct `IPP_stock`.
- [ ] Construct `IPP_growth`.
- [ ] Construct `IPP_share_total_fixed_assets`.
- [ ] Construct `IPP_share_capital_plus_IPP`.
- [ ] Construct `IPP_to_Kcap`.
- [ ] Construct `GOV_TRANS_stock`.
- [ ] Construct `GOV_TRANS_growth`.
- [ ] Construct `GOV_TRANS_to_Kcap`.
- [ ] Construct `GOV_TRANS_to_NRC`.
- [ ] Construct `GOV_TRANS_to_ME`.
- [ ] Tag all IPP and GOV_TRANS variables as `frontier_conditioner`.
- [ ] Confirm none of these variables enter preferred `K_cap`.
- [ ] Mark additive specifications involving IPP/GOV_TRANS as extension or diagnostic only.

## 6. Construct distributive variables in two tiers

- [ ] Construct immediately admissible unadjusted wage-share variables: `omega_CORP` and `omega_NFC`.
- [ ] Construct residual profit-share complements: `pi_res_CORP = 1 - omega_CORP` and `pi_res_NFC = 1 - omega_NFC`.
- [ ] Construct NOS-based surplus-share diagnostics.
- [ ] Construct unadjusted exploitation-rate alternatives: `e_CORP`, `e_NFC`, `ln_e_CORP`, and `ln_e_NFC`.
- [ ] Keep wage share as the preferred distributive state.
- [ ] Mark exploitation-rate variables as alternative proxies.
- [ ] Mark Shaikh-adjusted distributive variables as blocked until the current-release protocol passes.
- [ ] If the Shaikh protocol passes, construct `omega_adj_CORP`, `pi_adj_res_CORP`, `e_adj_CORP`, and related adjusted variants.
- [ ] Keep unadjusted and adjusted distributive families separate in the variable ledger.
- [ ] Do not silently replace unadjusted wage-share variables with adjusted variables.

## 7. Construct accumulated distribution-conditioned capital-growth indexes

- [ ] Construct unadjusted wage-share baseline: `q_omega_h1_Kcap`.
- [ ] Construct unadjusted wage-share robustness states: `q_omega_h3_Kcap` and `q_omega_h5_Kcap`.
- [ ] Construct unadjusted exploitation-rate alternative proxies: `q_e_h1_Kcap`, `q_e_h3_Kcap`, and `q_e_h5_Kcap`.
- [ ] Verify `h1` uses one-period inherited distributive state.
- [ ] Verify `h3` and `h5` are restricted moving-average robustness states.
- [ ] Verify no full-sample centering is used.
- [ ] Verify no unrestricted lag weights are estimated.
- [ ] Verify `omega_t * k_t` and `e_t * k_t` are not used as baseline objects.
- [ ] If the Shaikh protocol passes, construct adjusted variants such as `q_omega_adj_h1_Kcap`, `q_omega_adj_h3_Kcap`, and `q_omega_adj_h5_Kcap`.
- [ ] Mark adjusted accumulated indexes as a separate Shaikh-adjusted robustness family.
- [ ] Add all accumulated indexes to the construction ledger.

## 8. Build admissibility and blockage ledgers

- [ ] Define status categories: `constructed`, `preferred_baseline`, `robustness`, `alternative_proxy`, `diagnostic`, `blocked_pending_current_release_protocol`, `superseded`, and `not_in_baseline`.
- [ ] Assign one status to every constructed variable.
- [ ] Mark unadjusted wage-share variables as immediately admissible, if source data pass validation.
- [ ] Mark Shaikh-adjusted variables as `blocked_pending_current_release_protocol`.
- [ ] Mark `q_omega_h1_Kcap` as preferred baseline.
- [ ] Mark `q_omega_h3_Kcap` and `q_omega_h5_Kcap` as robustness.
- [ ] Mark `q_e_*` variables as alternative-proxy robustness.
- [ ] Mark adjusted `q_omega_adj_*` variables as blocked until the Shaikh protocol passes.
- [ ] Mark level interactions as superseded/diagnostic only.
- [ ] Mark IPP and GOV_TRANS variables as frontier conditioners.
- [ ] Produce a machine-readable admissibility ledger.
- [ ] Produce a human-readable validation report.

## 9. Re-run integration-order and S30I bottleneck audits

- [ ] Audit `k_ME`.
- [ ] Audit `k_NRC`.
- [ ] Audit `k_Kcap`.
- [ ] Audit `ME_NRC_gap`.
- [ ] Audit unadjusted `q_omega_*` variables.
- [ ] Audit unadjusted `q_e_*` variables.
- [ ] Audit wage-share variables.
- [ ] Audit exploitation-rate alternatives.
- [ ] Audit IPP frontier conditioners.
- [ ] Audit GOV_TRANS frontier conditioners.
- [ ] Compare gross vs net capital variants.
- [ ] Compare NFC vs CORP boundary variants.
- [ ] Identify whether I(2) risk is concentrated in NRC, ME, Kcap, or the accumulated indexes.
- [ ] Decide whether unadjusted variables are admissible for first-pass S30/S32 estimation.
- [ ] Keep Shaikh-adjusted audits parked until adjusted variables are unlocked.
- [ ] Produce an S30I integration-risk report.

## 10. Estimate corrected U.S. A00 regressions

- [ ] Estimate baseline A00 with `q_omega_h1_Kcap`.
- [ ] Estimate robustness A00 with `q_omega_h3_Kcap`.
- [ ] Estimate robustness A00 with `q_omega_h5_Kcap`.
- [ ] Estimate alternative-proxy A00 with `q_e_h1_Kcap`.
- [ ] Estimate alternative-proxy A00 with `q_e_h3_Kcap`.
- [ ] Estimate alternative-proxy A00 with `q_e_h5_Kcap`.
- [ ] Use FM-OLS as main estimator.
- [ ] Use IM-OLS as robustness estimator.
- [ ] Use DOLS as fragility/robustness check.
- [ ] Use Johansen/VECM only as system-level robustness.
- [ ] Run residual diagnostics.
- [ ] Run cointegration/admissibility checks.
- [ ] Produce S30/S32 model-choice report.
- [ ] Promote no coefficient object without human review.
- [ ] If the Shaikh protocol later passes, estimate adjusted-distribution robustness models separately.

## 11. Reconstruct transformation coefficient path

- [ ] Select only a human-promoted coefficient object.
- [ ] Recover `theta_0_hat`.
- [ ] Recover `theta_omega_hat`.
- [ ] Match the memory state to the promoted regression.
- [ ] Construct `theta_hat_t = theta_0_hat + theta_omega_hat * m_{t-1}^{(h)}`.
- [ ] Verify no centered memory state is used.
- [ ] Verify no level-interaction coefficient is substituted.
- [ ] Build robustness paths for h3/h5 separately.
- [ ] Build alternative-proxy paths only as diagnostics.
- [ ] Keep adjusted-distribution theta paths separate if the Shaikh protocol later passes.
- [ ] Produce a transformation-coefficient validation report.

## 12. Reconstruct productive capacity

- [ ] Use the promoted A00 coefficient object.
- [ ] Use the matching `k_t` and `q_t^{omega,h}` variables.
- [ ] Construct `Yp_hat_t`.
- [ ] Construct `Yp_hat_growth`.
- [ ] Compare productive-capacity path across h1/h3/h5 variants.
- [ ] Compare wage-share baseline against exploitation-rate alternatives.
- [ ] Check whether the reconstructed capacity path is economically interpretable.
- [ ] Document sensitivity to GPIM, gross/net, and sector boundary choices.
- [ ] Keep Shaikh-adjusted productive-capacity variants separate if later unlocked.
- [ ] Produce a productive-capacity reconstruction report.
- [ ] Mark admissible and diagnostic variants separately.

## 13. Reconstruct U.S. capacity utilization index

- [ ] Construct `mu_t = Y_t / Yp_hat_t`.
- [ ] Apply the locked U.S. anchor `mu_US,1973 = 1`.
- [ ] Use the FRB maximum-utilization anchor as preferred.
- [ ] Keep Fordist-core mean normalization as diagnostic only.
- [ ] Construct baseline `mu_US_A00_qomega_h1`.
- [ ] Construct h3 and h5 robustness variants.
- [ ] Construct q_e variants only as diagnostics.
- [ ] Compare the new utilization index against previous S40 series.
- [ ] Validate level, trend, turning points, and historical plausibility.
- [ ] If Shaikh-adjusted variables are later unlocked, construct adjusted-distribution utilization variants separately.
- [ ] Produce an S40 utilization reconstruction report.
- [ ] Produce an S40 admissibility ledger.
- [ ] Promote only the final admissible utilization series.

## 14. Parallel dependency map

- [ ] Treat S00 provider import as complete.
- [ ] Treat vault-lock notes as the immediate next commit.
- [ ] Allow unadjusted wage-share S10/S30/S40 pipeline to proceed after vault lock.
- [ ] Keep Shaikh-style current-release protocol as a parallel blocked lane.
- [ ] Do not let the Shaikh protocol block first-pass U.S. regression estimates.
- [ ] Do not let first-pass U.S. regressions silently use Shaikh-adjusted variables before the protocol passes.
- [ ] If the Shaikh protocol passes, reopen adjusted-distribution robustness estimates.
- [ ] If the Shaikh protocol fails, preserve unadjusted-distribution baseline and document blocked adjusted variants.