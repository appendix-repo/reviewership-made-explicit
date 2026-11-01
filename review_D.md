# Referee report (T5, single pass, style S2)

Manuscript: "Modularity, Not Mimicry: Interoperability Standards and the Diffusion of IT Outsourcing in U.S. Hospitals"

Basis: manuscript text only. No harness run. All formal and numerical findings are `asserted`; arithmetic was done by hand.
Ids: ms:Abs (abstract); ms:S1 to ms:S6 (sections); ms:A3; ms:Prop1; ms:Prop2; ms:H1 to ms:H3; ms:App.P1; ms:App.P2; ms:T2 (Table 2, by model and row).

## 1. Summary

1. Claim: interoperability standards make IT functions modular. Modularity m lowers effective specificity k(1-m) (ms:S2.2). The outsourcing threshold k* rises in m (ms:Prop1). The paper says the effect is larger under uncertainty u (ms:Prop2).
2. Data: hospital panel, 412 hospitals, 2009 to 2019, hospital and year fixed effects (ms:S3). Outsourcing share rises with modularity (ms:T2 Model 2; H1 supported). Peer outsourcing loses significance once modularity enters (ms:T2 Models 1 and 2; H3 not supported). Modularity x uncertainty is negative (ms:T2 Model 3; H2 not supported).
3. Claims: "rule out mimetic isomorphism" (ms:Abs; ms:S5). "First study to adjudicate directly" (ms:Abs; ms:S1).
4. Strengths: the threshold model is short and readable. The Prop 1 proof is correct (ms:App.P1, asserted). The within-hospital design is a sound base. Limitations are stated (ms:S5.2). The state-mandate event study is a useful design if reported in full.

## 2. Major concerns

rv:M1 (damaging). Prop 2 has the wrong sign under the paper's own A3.
- Claim: d2k*/dm du > 0 (ms:Prop2).
- Gap: ms:App.P2 says "Modularity operates on the denominator of k* only through the factor (1-m)". It then differentiates only the numerator in u and drops H'(u) = h1. With N = s+g0+g1u and H = h0+h1u: d2k*/dm du = [g1 h0 - (s+g0) h1] / [(h0+h1u)^2 (1-m)^2]. Under ms:A3 (h1/h0 > g1/(s+g0)) the bracket is negative for all u >= 0. The cross-partial is therefore negative.
- Fix: correct Prop 2 and H2 to a negative sign, or justify a different A3. The verbal reading at ms:S2.3 ("the value of modularity is greatest") concerns the level of hazard, not the threshold effect, which falls in u under A3.
- Check (not run): sympy. Take k = (s+g0+g1*u)/((h0+h1*u)*(1-m)), differentiate in m, then u. Confirm the sign under A3.
- Consequence: the negative estimate at ms:T2 Model 3 is what A3 predicts. The signalling account (ms:S5, para 2) is not needed to explain the sign. Calling it "consistent with our theory" is incorrect.

rv:M2 (damaging). The stated mechanism is not tested.
- Claim: modularity works by lowering effective specificity (ms:S2.2; ms:Abs, "lowering the effective asset specificity").
- Gap: no model uses k(1-m) or an m x specificity term. Specificity enters only as an additive control (ms:T2, "Asset specificity"). In the model, the effect of m on make-or-buy scales with k, so the test is m x specificity.
- Fix: estimate m x specificity. Report the effect of m at low and high specificity. If the term is absent, drop the mechanism claim.

rv:M3 (damaging). H1 holds only below a moderate uncertainty level.
- Claim: modularity is positive "in every specification" (ms:S4, H1).
- Gap: with the interaction, the modularity effect at uncertainty u is b_m + b_mu*u. Model 3: 0.118 - 0.061u, zero at u of about 1.9 SD. Model 4: 0.097 - 0.058u, zero at about 1.7 SD. The reported coefficient is the effect at mean u only.
- Fix: report conditional effects with CIs at u = -1, 0, +1 and +2 SD. Report the share of hospital-years above the zero crossing. Restate H1 as conditional.

rv:M4 (damaging). Non-significance is read as absence of mimicry.
- Claim: "rule out mimetic isomorphism" (ms:Abs; ms:S5); "H3 is not supported" (ms:S4).
- Gap: Model 4 peer coefficient is 0.036 (SE 0.036). Its 95% CI is about [-0.035, 0.107]. That range contains the modularity coefficient (0.097). The data do not exclude a peer effect as large as the modularity effect.
- Gap: the peer drop from Model 1 to Model 2 (0.137 to 0.042) compares significance across models. No difference test is reported. An independent-SE calculation gives z of about 1.9. A same-sample test is needed.
- Gap: the claim that the residual peer association "reflects the common diffusion of standards across hospitals in the same state, not imitation" (ms:S4, H3) is not tested.
- Gap: the paper says imitation operates under uncertainty (ms:S2.4, citing DiMaggio and Powell, 1983). The peer x uncertainty term, the institutional account's own moderator, is absent.
- Fix: report the CI. Test equality of peer coefficients. Add peer modularity (state-year mean) to test the standards reading. Add peer x uncertainty. Bound the claim to what the CI supports.

rv:M5 (damaging). The sample count does not match the design.
- Claim: "balanced panel of 412 U.S. general acute-care hospitals" observed 2009 to 2019, with 4,712 hospital-years (ms:S3.1).
- Gap: 412 x 11 = 4,532. 4,712 is not a multiple of 11 or of 412.
- Gap: every model reports N = 4,712 (ms:T2). Peer(t-1) is undefined in 2009, and the uncertainty measure needs three preceding years (ms:S3.2). With Peer(t-1) alone, the maximum estimation N is 412 x 10 = 4,120.
- Fix: give the panel structure, a sample flow table (exclusions, missing data), and N for each model. If the panel is unbalanced, say so and drop the balanced-panel claim.

rv:M6 (damaging). Modularity may be caused by outsourcing, and key variables share a source.
- Claim: within-hospital changes in m identify its effect (ms:S3.3).
- Gap: m, the outsourcing share and specificity all come from the same CIO survey (ms:S3.1 and S3.2). Common-respondent bias is possible.
- Gap: a vendor taking over a function may install certified interfaces. Outsourcing could then raise m mechanically.
- Gap: EHR replacement or upgrades bring certified interfaces and can shift sourcing. Year fixed effects do not absorb hospital-specific EHR changes. None of this is tested.
- Fix: use lagged or pre-period m. Control for EHR vendor change and hosted-EHR use. Validate CIO-reported m against contract or vendor records for a subsample. Use the state mandate as an instrument for m, with a first stage (see rv:M7).

rv:M7 (damaging). The only causal evidence is not reported.
- Claim: leads are "small and insignificant" and outsourcing rises after adoption, "consistent with a causal effect of modularity" (ms:S4, Robustness).
- Gap: no table, figure, coefficient, SE, event window or state count is given.
- Gap: no first stage. The paper does not show that a state requirement raised hospital m.
- Gap: staggered two-way fixed effects with leads and lags can give biased averages when effects differ by adoption cohort (recent difference-in-differences literature, e.g., Goodman-Bacon, 2021; Callaway and Sant'Anna, 2021 (to verify)).
- Gap: treatment varies by state, but SEs are clustered by hospital (ms:S3.3). This understates uncertainty when the number of states is small.
- Fix: report the full event study. Show the first stage on m. Use a heterogeneity-robust estimator. Cluster by state, or use a wild cluster bootstrap. Report a pre-trend test.

rv:M8 (damaging). The peer variable may capture state-level supply or policy.
- Claim: peer outsourcing is the state mean of other hospitals (ms:S3.2). It stands for the "population to which mimetic isomorphism directs attention" (ms:S3.2).
- Gap: state-year means also pick up state regulation, local vendor supply and IT labour markets. None is controlled.
- Gap: the state may be the wrong "field". Other definitions (referral region, system, nearby hospitals) are not tested.
- Fix: add vendor-market density and state policy controls. Repeat H3 with alternative peer definitions.

rv:M9 (damaging). The staffing control is a bad control.
- Claim: the modularity effect "cannot be attributed to differences in internal IT capability" (ms:S4, Robustness; ms:S3.3).
- Gap: the paper states that outsourcing transfers staff or eliminates positions (ms:S3.2). In-house staffing is therefore partly caused by the outcome. A coefficient that survives a control set by the outcome does not rule out capability confounding. The staffing coefficient (-0.143***, ms:T2 Model 4) is partly mechanical.
- Fix: use predetermined capability measures, such as staffing lagged or fixed at 2009, or baseline IT budget. Otherwise drop the claim.

rv:M10 (fixable). Prop 1 rests on unstated assumptions.
- Claim: modularity widens outsourcing (ms:Prop1).
- Gap: m enters only the hold-up term (ms:S2.2). If standards also lower in-house cost G, change vendor cost p or scale s, or raise vendor competition, the sign of dk*/dm is not fixed by the algebra.
- Gap: the step from threshold to hospital share (ms:S2.4) needs a distribution of k and spending weights that do not depend on m or u. None is stated. With uniform k and equal weights, the share is min(k*, 1), so the linear share model fails when k* > 1.
- Gap: the domain m in [0,1) excludes m = 1, which the measure allows (ms:S3.2).
- Fix: state these assumptions. Derive the share mapping. Let m shift G or s, and show the sign in each case.

## 3. Minor concerns

rv:m1. ms:T2 Model 3, "Environmental uncertainty 0.084*** (0.051)". t of about 1.65, p of about 0.10 (asserted). The star is wrong. Model 4 (0.079, 0.050) is correctly unstarred.

rv:m2. ms:T2 lacks a constant, a cluster count and a descriptive-statistics or correlation table. The SDs in ms:S3.2 appear to be total SDs. The 2.7 pp effect (ms:S4, H1) needs the within-hospital SD.

rv:m3. Asset specificity is a CIO rating used as a control in fixed-effects models (ms:S3.2). A time-invariant variable cannot be estimated under hospital fixed effects. State whether it varies within hospital.

rv:m4. Ownership, teaching status and system membership are listed as controls (ms:S3.2) and marked "Yes" (ms:T2). The time-invariant ones are absorbed by hospital fixed effects. State which controls vary over time.

rv:m5. The uncertainty measure is the three-year coefficient of variation of quarterly admissions (ms:S3.2). This is demand volatility. The model's u raises hold-up hazards and in-house costs (ms:S2.2). Justify the proxy. Remove seasonal variation from the CV.

rv:m6. "Certified to a published standard" (ms:S3.2) names no standard and no certifier. The denominator (clinical systems) can change mechanically when a system is outsourced. Name the standard and define the denominator.

rv:m7. The sample is limited to hospitals that responded in every year (ms:S3.1). Compare responders and non-responders on sourcing and size. ms:S5.2 mentions only size.

rv:m8. Robustness results ("similar" with licences included; non-system hospitals) are given without numbers (ms:S4). Report them in tables.

rv:m9. Priority claim, "first study to adjudicate directly" (ms:Abs; ms:S1). The paper cites no prior empirical IT-outsourcing study. Address the IS outsourcing literature (e.g., Dibbern et al., 2004 (to verify)). Narrow or support the claim.

rv:m10. The abstract says "prior adoption by peer hospitals". The variable is the peer outsourcing share (ms:S3.2). Use one term.

rv:m11. Overstated wording. "Strongly predicts" (ms:Abs) with within R2 of 0.13 and an effect of about one-sixth SD (ms:S4, H1). "Its substance is economizing" (ms:S6) is not tested against vendor competition or cost channels (rv:M10).

rv:m12. Williamson (1991) is cited for the claim that markets adapt less well than hierarchies (ms:S2.2). Check the attribution at page level (to verify).

## 4. Recommendation

Major revision.

Rationale:
- The result that Prop 2 and H2 rely on is wrong under the paper's own assumption (rv:M1).
- The headline claim that mimicry is ruled out is not supported (rv:M4, rv:M8). The claim as written does not stand, though its repair leaves the modularity-outsourcing association intact.
- The causal claim depends on an unreported event study and on a measure that outsourcing may itself produce (rv:M6, rv:M7).
- The sample description is internally inconsistent (rv:M5).
- The staffing robustness check is a bad control (rv:M9).

No single finding is fatal, and each can in principle be fixed with the authors' data. If rv:M5 and rv:M7 cannot be resolved, the paper does not support its main claim, and the recommendation should move to reject and resubmit.

## 5. Decisions for the reviewer

1. Accept rv:M1 and request a corrected Prop 2 and H2 with a negative sign, or ask the authors to justify A3 differently.
2. Request the sample flow table and N for each model before further review (rv:M5).
3. Make the full event study and first stage a condition for any causal claim (rv:M7).
4. Replace or drop the staffing control (rv:M9).
5. Recommendation: major revision as drafted, or reject and resubmit if rv:M5 or rv:M7 stays unresolved.
6. Whether to run the sympy check for rv:M1 before the report goes to the editor. Until it runs, rv:M1 stays `asserted`.
7. The priority claim (rv:m9) needs a literature check outside this pass.
