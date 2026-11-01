# Referee report: "Modularity, Not Mimicry: Interoperability Standards and the Diffusion of IT Outsourcing in U.S. Hospitals"

For the handling editor. Single-pass review, no harness. All formal and numerical findings are worked by hand and marked `asserted`.

## Summary

The paper builds a make-or-buy model in which interoperability standards ("modularity", m) lower effective asset specificity to k(1-m). It derives two propositions: modularity raises the outsourcing threshold (ms:Prop1), and the effect grows with environmental uncertainty (ms:Prop2).

The authors test this on a panel of 412 hospitals, 2009-2019, with hospital and year fixed effects. Modularity is positively associated with the IT outsourcing share (H1 supported). The modularity-by-uncertainty interaction is negative (H2 contradicted). A state-level lagged peer-outsourcing measure loses significance once modularity is added (H3 "not supported").

The authors conclude that mimetic isomorphism is ruled out, that outsourcing is economizing, and that the study is the first direct adjudication of the two accounts.

Strengths:
- The question is clear.
- The model has explicit assumptions.
- The authors report the contrary H2 result instead of dropping it.
- The effect-size arithmetic in Section 4 is correct (0.112 x 0.24 = 0.027; 0.027/0.17 = 0.16 SD) (`asserted`).

The main conclusion is not supported by the design, and one proposition is wrong as proved.

## Major concerns

**1. Proposition 2 is wrong under the authors' own Assumption A3. [damaging] [`asserted`]**
- Locus: ms:A3, ms:Prop2, Appendix proof of Prop 2.
- Commitment: Prop 2 states that the cross-partial of k* in m and u is positive.
- The proof differentiates only the numerator, s + G(u), and treats H(u) as constant. H'(u) = h1 > 0 is dropped.
- Correct result: ∂²k*/∂m∂u = [g1·h0 − h1·(s+g0)] / [H(u)²·(1−m)²].
- The sign is positive only if h1/h0 < g1/(s+g0). A3 states the reverse (h1/h0 > g1/(s+g0)). So under A3 the cross-partial is negative, and the sign does not depend on u.
- Also under A3, ∂k*/∂u < 0 everywhere. The model then predicts a negative uncertainty main effect. Table 2 reports a positive coefficient (ms:T2.M3.uncertainty, but see 6).
- The "intuitive reading" in Section 2.3 confuses two things. The cost saving from modularity, H(u)·k·m, rises with u. The threshold shift depends on the ratio (s+G)/H, which falls with u.
- Consequence: H2 is derived from a false proposition. The negative interaction in Model 3 is what the model predicts once the algebra is fixed.
- Repair: correct Prop 2 and H2 and state the sign condition. Then say plainly that H2 as originally stated was refuted. Do not present the corrected sign as a confirmed prediction, because it is derived after seeing the data. Justify A3, including why s appears in its denominator.

**2. The discussion of the negative interaction is ad hoc and contradicts the paper's own claim. [damaging]**
- Locus: ms:S5 paragraph 2; ms:S4 "H2".
- Commitment: "This interpretation is consistent with our theory." The signalling and legitimacy story is outside the model and untested.
- Legitimacy pressure to keep visible in-house capacity is an institutional mechanism. The paper uses an institutional mechanism to rescue the transaction-cost account while claiming to rule institutional accounts out.
- The abstract and the conclusion do not mention that one of the two model predictions failed.
- Repair: see 1. Drop the signalling story or test it, for example with Peer x u and board-composition measures. Report H2 in the abstract.

**3. The data cannot support "rule out mimetic isomorphism". [fatal for the central claim]**
- Locus: ms:Abstract, ms:S5, ms:S6, ms:S4 "H3".
- Commitment: a null peer coefficient in Model 2 rules out mimicry.
- The authors lack the entitlement for five reasons.
  - (a) Absence of significance is not absence of effect. In Model 2 the Peer coefficient is 0.042 (SE 0.038). Its 95% CI is about (-0.03, 0.12), which includes 85% of the Model 1 estimate of 0.137. No test of the M1-M2 difference is given.
  - (b) The horse race favours modularity. Modularity is contemporaneous and comes from the same CIO survey. Peer is lagged, is a state mean over only the sampled hospitals (412 hospitals across at most 50 states plus DC; the per-state count is not given), and is noisy. Measurement error biases Peer toward zero.
  - (c) State is an arbitrary definition of the "field". Mimicry is usually directed at similar or prestigious organizations, such as system peers, local competitors, large teaching hospitals, or vendors' reference sites (ms:S3.2 Peer). Peer x u is not tested, although the paper's own account of mimicry (ms:S2.4) says it should be stronger under uncertainty.
  - (d) Modularity could itself be adopted by imitation. The drop in the Peer coefficient is equally consistent with mimicry operating through standards adoption. The authors write that the peer effect "reflects the common diffusion of standards across hospitals in the same state". That asserts a mechanism. They never test whether peers' modularity predicts a hospital's modularity.
  - (e) State requirements for certified interfaces (ms:S4 Robustness) and the 2009 federal incentive programme are coercive, not economizing. Coercive isomorphism is a DiMaggio & Powell mechanism. Standards diffused by mandate favour the institutional account, and only the mimetic strand is tested.
- Repair:
  - Report the M1-M2 difference test and CIs.
  - Use several peer definitions, and peer modularity.
  - Add Peer x u.
  - Test whether hospital modularity follows peer modularity.
  - Soften the claim to "peer outsourcing adds little beyond modularity in this specification".

**4. Modularity is endogenous and measured by the same source as the outcome. [damaging]**
- Locus: ms:S3.2 Modularity, ms:S3.3.
- Commitment: within-hospital variation in m identifies the effect of modularity on outsourcing.
- Both m and Φ are CIO-reported in the same survey and year. A CIO who outsources to a vendor-hosted platform also reports more certified interfaces, because vendor platforms ship them. This gives reverse causality, joint determination, and common-method bias.
- Hospital FE do not remove time-varying confounders: EHR vendor migration, joining a system, CIO turnover, and hospital-specific timing of the incentive programme. Year FE only absorb national shocks.
- Repair:
  - Lag m.
  - Use an instrument or a policy source of variation, and report the first stage.
  - Use a non-survey measure of m, such as vendor or certification records.
  - Show a table of m and Φ over time to show the two series moving together.

**5. Model 4's control is a bad control, and the inference drawn from it does not follow. [damaging] [`asserted`]**
- Locus: ms:S3.2 In-house IT staffing, ms:S3.3 last paragraph, ms:T2.M4.
- Commitment: "If the modularity effect survives this control, it cannot be attributed to capability differences."
- The paper itself says outsourcing "transfers its staff to the vendor or eliminates the positions". Staffing is therefore a consequence of the outcome. Conditioning on it biases the modularity coefficient in an unknown direction.
- The within-R² jump from 0.14 to 0.19 is consistent with a near-mechanical link.
- Staffing per bed is also a weak proxy for unobserved capability, so surviving the control proves nothing about capability. The modularity coefficient moves from 0.118 to 0.097, so it did not "survive" unchanged.
- Repair: drop the control or use pre-period (baseline) staffing interacted with year. Remove the "cannot be attributed" sentence.

**6. The event-study evidence is unreported and cannot carry a causal claim. [damaging]**
- Locus: ms:S4 Robustness.
- Commitment: "consistent with a causal effect of modularity".
- No table, figure, or coefficients are given. There are no counts of treated, early-treated, or never-treated states.
- The estimator is two-way FE with staggered adoption (2011-2016). It is biased under heterogeneous effects (Goodman-Bacon 2021; Sun & Abraham 2021; Callaway & Sant'Anna 2021; all to verify).
- The design estimates the effect of the state requirement on outsourcing, which is a reduced form. Treating it as a modularity effect needs two things the paper does not provide: a first stage (requirement to m) and an exclusion restriction. The exclusion restriction is implausible, since compliance burden alone could push hospitals toward vendors.
- The requirement is a state-level event. It also moves state-level Peer, so it confounds the H3 test as well.
- "Leads small and insignificant" is weak evidence without power and CIs.
- Repair: report the full event study with a heterogeneity-robust estimator, the first stage, and an IV or reduced-form interpretation, with clustering at the state level.

**7. Standard errors are clustered at the wrong level. [fixable]**
- Locus: ms:S3.3.
- Peer is a state-level variable, and the policy variation is state-level.
- Clustering by hospital understates the SE of state-level regressors (Bertrand, Duflo & Mullainathan 2004, to verify).
- Repair: cluster by state, or report two-way clustering, and report the number of states. This may change the significance of Peer in M1 and of the event-study leads.

**8. Construct validity of "modularity" and "asset specificity", and the mechanism is not tested. [damaging]**
- Locus: ms:S2.2, ms:S3.2 Modularity and Asset specificity, ms:T2.
- Commitment: certified standard interfaces measure Baldwin-Clark modularity and reduce k proportionally.
- The measure counts the share of systems with certified interfaces. That is interoperability, not modularity in the sense of design rules and information hiding.
- The paper's own examples of specificity (ms:S2.1) include configuration and tacit knowledge of workflows. Standard interfaces do not affect these, so the factor k(1-m) is a strong assumption.
- The model implies an interaction: modularity matters most where nominal k is high, and outsourcing depends on k(1-m). Table 2 uses additive terms and no m x k term.
- The CIO specificity rating should fall with modularity if the mechanism holds. The specificity coefficient is stable when modularity enters (-0.094 in M1 to -0.091 in M2), which suggests the two measures share little. The authors never regress specificity on modularity. The specificity measure is also ambiguous for hospitals that have not outsourced.
- Repair: show m lowers measured specificity, add the m x k test, and discuss construct validity.

**9. The paper does not explain "diffusion". [damaging]**
- Locus: ms:Abstract first sentence, ms:S1 first paragraph, ms:S3.3.
- Commitment: the study explains why outsourcing spread rapidly after 2009.
- Year FE absorb the national trend, which is the doubling the paper starts from. The regression explains cross-hospital and within-hospital deviations, not the aggregate rise.
- There is no adoption-timing or hazard analysis, and no time series of Φ or m.
- Within R² of 0.13-0.19 is small.
- Repair: decompose the rise in Φ between 2009 and 2019 into the part accounted for by changes in m, using the estimates without year FE or a counterfactual, or restate the claim as a cross-sectional association.

**10. Data inconsistencies in the sample and in Table 2. [fixable] [`asserted`]**
- (a) 412 hospitals x 11 years (2009-2019) = 4,532, not 4,712 (ms:S3.1, ms:T2). The panel is described as balanced. Peer is lagged one year, which should lose another year (4,120). The paper does not explain either difference.
- (b) ms:T2.M3.uncertainty reads 0.084*** (0.051). The t-ratio is 1.65 (p about 0.10), which fits no star. The same variable in Model 4 (0.079, SE 0.050) has no star. Other stars match their t-ratios.
- Other entries I checked are consistent.
- The sample of CIO respondents in all 11 years is highly selected, and the limitation section says so only in one sentence. No comparison to non-responders is given. The survey ("Hospital IT Sourcing Survey") is not identified, and its response rate and linkage are not described.
- Repair: reconcile N, correct Table 2, and describe the survey. Analyze attrition.

**11. The novelty claim is unsupported. [fixable]**
- Locus: ms:Abstract, ms:S1 last paragraph.
- Commitment: "first study to adjudicate directly between transaction-cost and institutional explanations of IT outsourcing".
- The reference list has 9 items and none is on IT outsourcing. Prior work I recall tests institutional and TCE accounts of IT outsourcing: Loh & Venkatraman (1992), Ang & Cummings (1997), Poppo & Zenger (1998) (all to verify).
- Repair: add the IT-outsourcing literature and delete or qualify "first".

## Minor concerns

12. "Strongly" (abstract, ms:S4) overstates a 0.16 SD effect for one cross-sectional SD of m. Identification is within-hospital, and the within-hospital SD of m is not reported and is probably smaller.
13. "In every specification" (ms:S4 H1) is wrong: modularity is not in Model 1.
14. Because m is uncentered, the u main effect in Model 3 is the effect at m = 0, outside the typical range. At m = 0.46 the effect is about 0.056. At u = +2 SD the modularity effect is about zero (0.118 - 2 x 0.061 = -0.004). Report marginal effects at meaningful values.
15. The uncertainty measure (admissions CV over three years) is demand volatility. The model's u is the frequency of unanticipated contract adaptations. Justify the mapping. The rolling window overlaps across years.
16. The share of functions outsourced depends on the distribution of k, and k* may exceed 1, so Prop 1 gives a threshold, not a share. Φ is spending-weighted. State what the mapping from k* to Φ is.
17. Peer is built only from sampled hospitals and is unweighted. Report the number of hospitals per state.
18. No descriptive statistics or correlation table. Means and SDs are given in the text for three variables only. Controls are not named in the table, and their coefficients are not shown.
19. The practice recommendation ("hospital leaders ... should attend first to the modularity of their systems", ms:S5.1) assumes a causal effect that Concerns 4-6 undermine.
20. The limitations section omits endogeneity, reverse causality, same-source bias, and peer-definition choice.
21. Section 2.2 normalizes p, which cancels in the threshold. Say so, or drop it.
22. TCE and institutional theory are not mutually exclusive. The framing as winner and loser ("Modularity, Not Mimicry") should be tempered.

## Recommendation: major revision

- The question is worthwhile, and the within-hospital panel is a reasonable start.
- Three problems must be fixed before the conclusions stand: the proof of Prop 2 is wrong (1), the claim to rule out mimicry is not supported (3), and the causal interpretation of modularity rests on a bad control and unreported event-study evidence (4-6).
- If the authors cannot show that modularity is not driven by the outcome or by coercive mandates, the contribution is limited to an association. If they restate the claims accordingly, fix the model, and resolve the data inconsistencies, the paper could be publishable.
- Reject is not warranted at this stage. Every problem has a stated repair, and the H1 association is the finding most likely to survive them.

## Decisions for the reviewer

- D1: Accept, reject, or modify the claim that Prop 2 flips sign under A3 (Concern 1). A symbolic check by the harness (sympy, derivative of (s+G)/H with respect to u) would move it from `asserted` to `demonstrated`.
- D2: Confirm the arithmetic findings in Concern 10 (4,532 versus 4,712; the t-ratio for the uncertainty coefficient) before sending them to the authors.
- D3: Decide whether Concern 3 is rated fatal for the central claim or damaging.
- D4: Decide whether to name the three IT-outsourcing papers in Concern 11. All need verification before they are cited.
- D5: Decide whether the recommendation is major revision or reject.
