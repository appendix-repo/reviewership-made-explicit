# Referee Report

**Manuscript:** "Modularity, Not Mimicry: Interoperability Standards and the Diffusion of IT Outsourcing in U.S. Hospitals"
**To:** The Handling Editor
**Recommendation:** Reject (in its present form)

*Conventions.* No computational harness was available. Every formal or numerical finding below was worked through by hand and is therefore marked `asserted`. Manuscript elements are cited by id (for example `ms:Prop2`, `ms:T2.M3.uncertainty`). My own concerns are numbered and carry ids (`cmt:1` and so on). Literature I cannot vouch for from memory is marked "(to verify)". Severity follows the stated scale: fatal, damaging, fixable, minor.

---

## 1. Summary of the submission and its claimed contributions

The paper asks why IT outsourcing spread through U.S. hospitals after 2009. It contrasts an institutional account (mimetic isomorphism under uncertainty) with a transaction-cost account. The authors build a make-or-buy model (`ms:S2.2`–`ms:S2.3`) in which a hospital's modularity m, the extent to which its systems interact through certified standard interfaces, scales down the effective specificity of a function from k to k(1−m). Functions with k below a threshold k* are bought. The authors state two propositions: modularity raises the threshold (`ms:Prop1`), and this effect is amplified by environmental uncertainty (`ms:Prop2`).

They test the implied hypotheses on a "balanced panel of 412 hospitals, 2009–2019" with hospital and year fixed effects (`ms:S3.3`, `ms:T2`). The main empirical findings, as reported, are these:

- Modularity is positively associated with the outsourcing share (`ms:H1`).
- The modularity-by-uncertainty interaction is negative, the opposite of H2 (`ms:T2.M3.interaction`).
- Lagged state-level peer outsourcing is significant when modularity is omitted and not significant once it is included (`ms:T2.M1.peer`, `ms:T2.M2.peer`).

From this the authors conclude that the results "rule out mimetic isomorphism as a driver of IT outsourcing in this setting" (`ms:Abstract`, `ms:S5`). They also conclude that the practice is "economizing", and they claim to be the first to "adjudicate directly" between the two accounts.

The question is worthwhile, and the explicit statement of a rival hypothesis is the right design instinct. A decade-long hospital panel with CIO-reported specificity ratings is potentially valuable. The authors also report the failure of H2 openly in the Results rather than burying it. I give them credit for these three things.

The manuscript nonetheless does not deliver what it claims. The theoretical result that frames the empirical work is wrong given the authors' own assumptions. The test of the institutional rival cannot bear the weight placed on it. The principal causal safeguard is a bad control. The overall research design does not identify the mechanism asserted.

---

## 2. Major concerns

### M1. Proposition 2 is false under Assumption A3, and its proof is incorrect (`cmt:1`) — severity: fatal for the theoretical contribution; status: `asserted`

*Commitment undertaken.* The authors commit to ∂²k*/∂m∂u > 0 (`ms:Prop2`). They also commit to A3: h₁/h₀ > g₁/(s+g₀) (`ms:A3`). They derive both from k* = (s+G(u)) / (H(u)(1−m)) with H = h₀+h₁u and G = g₀+g₁u.

*Entitlement lacking / incompatibility incurred.* The proof (`ms:AppProof2`) differentiates ∂k*/∂m = (s+G)/(H(1−m)²) with respect to u while treating H(u) as if it did not vary. It reports G′/(H(1−m)²). The quotient rule requires the full expression:

∂²k*/∂m∂u = [g₁H − (s+G)h₁] / [H²(1−m)²] = [g₁h₀ − h₁(s+g₀)] / [H²(1−m)²].

The terms in g₁h₁u cancel. The numerator is positive if and only if g₁/(s+g₀) > h₁/h₀. That is the exact negation of A3. So under A3 the cross-partial is **negative for all m and u**, and Proposition 2 as stated is false. The sentence that "modularity operates on the denominator … only through the factor (1−m)" overlooks that the denominator also contains H(u).

I regard this as the most serious problem in the paper, for four reasons.

1. The model, correctly solved, predicts the negative interaction the authors found (`ms:T2.M3.uncertainty`: −0.061). Under A3 the model also predicts a negative main effect of uncertainty on k*, since the same bracket governs ∂k*/∂u. The "failure" of H2 is therefore a failure of the algebra, not of the data. The Discussion's long account of legitimacy pressures and signalling (`ms:S5`, second paragraph) is an ad hoc patch for a result the model already implied. Conversely, if A3 were reversed the model would predict a positive interaction. The model thus delivers no unambiguous prediction without an independent warrant for A3, and none is offered.
2. The "intuitive reading" offered for the proposition (`ms:S2.3`) conflates two objects. The cost saving from modularity, ∂(C_M−C_B)/∂m = H(u)k, does rise in u. The comparative static in the proposition concerns the *threshold*, and its sign depends on how fast (s+G) grows relative to H.
3. A3 appeals to Williamson (1991) for the claim that markets adapt less well than hierarchies. My recollection is that Williamson (1991) argues the opposite for autonomous adaptation, where markets excel, and favours hierarchy only for cooperative adaptation (to verify). At minimum A3 needs a more careful justification. Note also that the numbering jumps to "A3": Assumptions A1 and A2 never appear.
4. Even a correct cross-partial of k* does not map into the sign of an interaction in the *spending share* Φ. For any increasing function F relating k* to Φ, ∂²F(k*)/∂m∂u = F″·k*ₘ·k*ᵤ + F′·k*ₘᵤ. The second term has the sign of the cross-partial of k*; the first need not. The step from `ms:Prop2` to `ms:H2` in `ms:S2.4` is therefore not licensed, and the corner at k* ≥ 1 (full outsourcing) is not addressed.

*Repair.* Correct the proposition and proof. State the parameter condition that governs the sign and give independent grounds for it. Derive the hospital-level Φ explicitly from a distribution of k and spending weights. Rewrite the hypothesis set and abstract accordingly. Drop the signalling story unless it is built into the model and tested.

### M2. The inference "rules out mimetic isomorphism" does not follow from the evidence (`cmt:2`) — severity: fatal for the central claim as phrased; status: `asserted`

*Commitment undertaken.* The abstract, Discussion and Conclusion state flatly that the results "rule out mimetic isomorphism" and show that the practice is "economizing". The Results (`ms:S4`, H3 paragraph) state that the pattern is "exactly what the transaction-cost account predicts and the institutional account does not".

*Entitlement lacking.* There are five separate gaps.

1. *Absence of significance is not evidence of absence.* The Model 2 peer coefficient is 0.042 (SE 0.038). Its 95% interval is roughly (−0.03, 0.12), which includes about 85% of the Model 1 magnitude (0.137). The data do not exclude a substantial peer effect. The Model 1 versus Model 2 drop is itself not tested; the difference between a significant and a non-significant estimate is not necessarily significant (Gelman & Stern, 2006, to verify). The two estimates also come from different specifications, so a joint test is needed.
2. *Conditioning on a mediator or consequence of imitation.* The movement of the peer coefficient on adding modularity is equally what one expects if modularity is a *channel* of peer influence. Hospitals may adopt certified interfaces because their peers did, or because peers' vendors pushed them. The authors assert that "the apparent peer effect reflects the common diffusion of standards across hospitals in the same state, not imitation", but the common diffusion of a standard across a field is the canonical object of institutional diffusion theory. The paper never tests whether peers' modularity predicts own modularity, which is the obvious test of whether standards themselves spread mimetically. Nor does it consider the coercive channel: certification and interface requirements are federal and state regulatory artefacts, and the authors use state mandates themselves in the event study (`ms:S4.robust`). "Certified" interfaces are an institution in precisely Powell and DiMaggio's sense.
3. *The year fixed effects absorb the diffusion curve that is the stated explanandum.* The paper sets out to explain the national, roughly twofold rise in outsourcing (`ms:S1`). Year dummies remove any common trend, mimetic or not. After they are removed, the peer variable carries only state-specific deviations from the national path. The design cannot say what drove the national diffusion. No decomposition shows how much of the rise in Φ is attributable to the observed rise in m. With a slope of about 0.11, even a large increase in mean modularity would explain only a modest fraction of a rise of the size described. The authors should report this accounting.
4. *The institutional account's own discriminating prediction is not tested.* Mimetic pressure is hypothesized to intensify under uncertainty (DiMaggio & Powell 1983, cited by the authors in `ms:S2.4`). The obvious test is Peer × uncertainty. It is not run, though the variables are in hand.
5. *The two accounts are not mutually exclusive.* Imitation can be a rational response to uncertainty, and a technologically efficient practice can be legitimated institutionally. Showing that modularity predicts outsourcing does not show that peers do not.

The Discussion itself concedes the force of the rival. To explain the negative interaction it invokes "legitimacy pressures to retain in-house functions", which is an institutional mechanism operating on the outsourcing decision. A paper that has just argued that institutional forces are ruled out cannot also rely on them to rescue its model.

*Repair.* Retitle and reframe the claim: modularity is a robust correlate of outsourcing, and the data show no *incremental* state-level peer association under this specification. Add the tests listed above (peer → modularity, Peer × uncertainty, a formal test of the coefficient difference, power or confidence-interval based statements). Add the accounting exercise for the national trend.

### M3. The peer variable and the standard errors cannot support a null result (`cmt:3`) — severity: damaging; status: `asserted`

*Commitment undertaken.* The test of H3 rests on "the mean outsourcing share of all other sample hospitals in the same state in year t−1" (`ms:S3.2.peer`). Standard errors are clustered by hospital (`ms:S3.3`).

*Entitlement lacking.* Six problems follow.

1. The reference group is asserted, not justified. Mimetic theory points to *salient* peers: similar size, system affiliation, the same referral region, or high-status organizations. Many states would be the wrong unit. A null on one arbitrary peer definition is a null on that definition.
2. The measure is computed from a sample of 412 hospitals spread across states. For small states it will rest on very few hospitals, and for a state with one sample hospital it is undefined. Sampling noise in a regressor attenuates its coefficient and reduces power, which is exactly the direction in which a null "emerges". The paper does not report the distribution of peer-group sizes.
3. The variable has state-by-year variation only. Any state-year shock (state policy, a dominant vendor's regional push, Medicaid changes, the 2011–2016 state interface mandates themselves) enters peer outsourcing and own outsourcing together. Hospital and year fixed effects do not remove state-year shocks. This is Manski's reflection and correlated-effects problem, and nothing in the paper separates it from imitation.
4. A regressor that varies at the state level requires clustering at the state level (or an appropriate small-cluster correction such as wild-bootstrap, to verify), not at the hospital level. Hospital clustering understates the uncertainty of the peer coefficient and of the state-mandate event study.
5. Hospitals within a system plausibly share IT sourcing decisions, so same-system "peers" in the same state generate a correlation that is not imitation. The sample restriction to non-system hospitals is mentioned in a single sentence without figures. System-level clustering is not used.
6. Mimetic diffusion is usually an adoption-threshold or S-curve process; a linear effect of the mean share is a questionable functional form.

*Repair.* Define peers in several theoretically motivated ways, including out-of-state and similar-hospital reference groups. Report group sizes. Cluster at the state or system level as appropriate. Consider a design in which peer variation is plausibly exogenous to common shocks.

### M4. The key causal safeguard (Model 4) conditions on a mechanical consequence of the dependent variable (`cmt:4`) — severity: damaging; status: `asserted`

*Commitment undertaken.* The authors write: "If the modularity effect survives this control, it cannot be attributed to capability differences" (`ms:S3.3`). They repeat the claim in `ms:S4.robust`.

*Entitlement lacking.* In-house IT staffing is, by the authors' own description (`ms:S3.2.staffing`), reduced by outsourcing: "outsourcing a function transfers its staff to the vendor or eliminates the positions". It is thus an outcome of the dependent variable, close to an accounting relationship with it, and not a pre-determined proxy for capability. Conditioning on it is a bad control that can induce bias in either direction. The large coefficient (−0.143) and the jump in within-R² from 0.14 to 0.19 in Table 2 are exactly what this mechanical relationship would produce. Survival of the modularity coefficient therefore says nothing about confounding by capability. Notably, the modularity coefficient does fall by roughly 18% (0.118 → 0.097), which is not obviously reassuring either. Hospital fixed effects remove only *time-invariant* capability, while the stated concern (`ms:S3.3`) is *time-varying* capability.

*Repair.* Use a pre-determined capability measure (baseline or lagged staffing, CIO tenure, prior IT investment), hospital-specific trends, or an instrument. Remove the sentence that the effect "cannot be attributed to capability differences".

### M5. The proposed mechanism is not tested, and the specificity variable is used in a way that contradicts the theory (`cmt:5`) — severity: damaging; status: `asserted`

*Commitment undertaken.* The theory says modularity works by reducing effective specificity from k to k(1−m) (`ms:S2.2`), and that the resulting hold-up hazard is what kept functions in-house.

*Entitlement lacking.* Four points.

1. *Asset specificity is entered as a control in every model, but it is the mechanism.* The measure is the CIO's rating of "how costly it would be to transfer the hospital's IT functions to a different provider" (`ms:S3.2.specificity`). That is a measure of *effective* specificity (a switching cost), which on the authors' theory modularity itself reduces. If it is measured well, the modularity coefficient conditional on it should approach zero. That it remains positive and significant in every column is more naturally read as evidence that modularity affects outsourcing through something *other* than the hold-up channel. The authors must clarify which concept (nominal or effective) the survey item taps and report the specificity regressions with and without modularity.
2. *The signature prediction is never tested.* In the model the benefit of modularity is proportional to nominal specificity (H(u)·k·m). The data on specificity permit a Modularity × Specificity test, and it is absent.
3. *Rival economizing channels are not excluded.* Standards may raise vendor scale economies (the parameter s in the authors' own notation), lower coordination and monitoring costs, or simply expand vendor availability. Each produces a positive modularity-outsourcing association without any change in hold-up exposure. These channels are economizing, but they are not the transaction-cost hold-up mechanism the paper claims to show.
4. *"Economizing" is asserted without any performance outcome.* An efficiency claim in the transaction-cost tradition requires evidence that aligned governance performs better than misaligned governance. No cost, quality, or performance measure appears.

Construct validity compounds the problem. The outsourcing measure covers functions such as data-centre hosting and help desk (`ms:S1`), for which clinical interface standards are largely irrelevant. The modularity measure, the share of clinical systems connected through certified interfaces, captures interoperability, and not obviously Baldwin and Clark's (2000) modularity in the sense of design rules, information hiding and independence of components. Disaggregating outsourcing by function type, and testing whether modularity matters for the clinical-application functions that the theory describes, would be the natural validation.

*Repair.* As above: test M × k, relabel or re-measure specificity, run function-level analyses, and temper "economizing" to what the data show.

### M6. Within-hospital identification is not credible as presented, and the event study is under-reported and mis-specified for the claim made (`cmt:6`) — severity: damaging; status: `asserted`

*Commitment undertaken.* The authors write that "Identification therefore comes from within-hospital changes in modularity" (`ms:S3.3`), and that the event study is "consistent with a causal effect of modularity" (`ms:S4.robust`).

*Entitlement lacking.* Five points.

1. Hospital fixed effects do not address time-varying confounders: a new CIO, a change of EHR vendor, a system acquisition (which changes sourcing and interfaces together), a merger, a strategic shift.
2. *Reverse causality.* When a vendor takes over a function it commonly installs standards-based interfaces. Outsourcing may thus *raise* measured modularity. The paper discusses direction nowhere.
3. Outsourcing share, modularity and specificity all come from the same CIO in the same survey, with no external validation. Within-hospital variation will therefore be contaminated by CIO turnover, changes in reporting practice and common-method response style. The Limitations section acknowledges CIO reporting (`ms:S5.2`) in one sentence and does nothing to address it.
4. The paper itself says (`ms:S5.1`) that standards are something "firms do not individually control", yet the identifying variable is the hospital's *own* share of certified-interface connections, which the hospital chooses. If the argument is that external standards drive modularity, then the exogenous variation should be measured at that level.
5. The event study is reported in a single sentence: no figure, no coefficients, no number of treated states or hospitals, no confidence bands. It is estimated by two-way fixed effects with leads and lags under staggered adoption (2011–2016), which is known to produce contaminated lead and lag coefficients when treatment effects are heterogeneous (Goodman-Bacon 2021; Sun & Abraham 2021; Callaway & Sant'Anna 2021, all to verify). More fundamentally it estimates the effect of a *state requirement* on outsourcing, which is a reduced form. A state mandate could raise outsourcing directly, through compliance burden on smaller hospitals or by raising vendor demand, which is a coercive-institutional channel. No first stage (mandate → modularity) is shown, and the exclusion restriction is neither stated nor defended. The state-level timing is also confounded with the state-level peer variable of M3.

*Repair.* Report the event study in full using a heterogeneity-robust estimator; show the first stage; state and defend the exclusion restriction; address the direction of causation; report any external validation of the CIO measures. Otherwise the language of causation (including the practice recommendation in `ms:S5.1`) should be withdrawn.

### M7. Treatment of the contradicted hypothesis H2 is post hoc and the abstract is not faithful to the results (`cmt:7`) — severity: damaging; status: `asserted`

*Commitment undertaken.* The abstract states: "The model predicts that modularity increases outsourcing, and that this effect is stronger where environmental uncertainty is high." The Results say the interaction is negative, "contrary to H2", and the Discussion calls the proposed explanation "consistent with our theory".

*Entitlement lacking.* The abstract reports the theory's prediction without reporting its rejection, and the headline claims in the abstract and conclusion do not mention that one of the paper's two own predictions failed. The signalling account in `ms:S5` is introduced after the fact, is not formalized, and is not tested (no board, stakeholder, or visibility measure appears). It is unfalsifiable as presented, and, as noted under M2, it is itself institutional. The statement that it is "consistent with our theory" is not available, since the paper's theory as stated predicted the opposite. A reader is entitled to be told, in the abstract, that H2 was contradicted. The coefficient implies that the modularity effect (0.118 − 0.061·u) vanishes at about +1.9 SD of uncertainty, which is a substantive result and should be reported with marginal effects.

*Repair.* Report H2's failure in the abstract; reconcile it with the corrected model of M1; report marginal effects; either test the signalling story or label it speculation.

### M8. Internal inconsistencies in the reported data and tables (`cmt:8`) — severity: fixable, but a signal of insufficient care; status: `asserted`

1. *Sample arithmetic.* A balanced panel of 412 hospitals observed annually for 2009–2019 (11 years) has 412 × 11 = 4,532 observations, not 4,712 (`ms:S3.1`, `ms:T2`). The figure 4,712 is not an integer multiple of 412 (4,712/412 ≈ 11.44). Either the panel is unbalanced, the number of hospitals is different, or there is an error that touches every estimate.
2. *Significance stars.* In Table 2, Model 3, "Environmental uncertainty 0.084*** (0.051)" gives t ≈ 1.65 and p ≈ 0.10, which is not significant at conventional levels, and certainly not at p < 0.001. In Model 4 the nearly identical 0.079 (0.050) carries no stars. The other coefficients' stars are consistent with their standard errors by my calculation.
3. *No descriptive table.* The first table is "Table 2". There is no Table 1 of descriptive statistics and correlations (nor, therefore, any check on collinearity between peer outsourcing and modularity, which matters for M2 and M3).
4. *Effect-size language.* The abstract says modularity "strongly predicts" outsourcing. The text itself computes 2.7 percentage points for a one-SD change, "about one-sixth of a standard deviation" (`ms:S4`, H1). This is statistically clear but substantively modest.
5. *Selection.* The sample is restricted to hospitals that responded to the survey in every one of 11 years. That excludes closures, mergers and attriters, which are plausibly related to IT sourcing and financial condition. The limitation is noted (`ms:S5.2`) but nothing is done about it.

*Repair.* Reconcile the counts; correct the table; add Table 1; calibrate the language; investigate attrition (for example inverse-probability weights or an unbalanced-panel check).

---

## 3. Minor concerns

**m1. Priority claim and literature (`cmt:9`).** "To our knowledge, this is the first study to adjudicate directly between transaction-cost and institutional explanations of IT outsourcing" appears twice (`ms:Abstract`, `ms:S1`) and is, I believe, not accurate. The reference list contains only general theory and no empirical IT-outsourcing work. I recall prior work on the diffusion of IT outsourcing and the "Kodak effect" (Loh & Venkatraman, 1992, to verify), on institutional influences on IS outsourcing (Ang & Cummings, 1997, to verify), and on testing transaction-cost against alternative accounts of make-or-buy decisions in information services (Poppo & Zenger, 1998, to verify). The authors should locate their paper in this literature and either substantiate or remove the priority claim.

**m2. Uncertainty measure (`cmt:10`).** The coefficient of variation of twelve quarterly admission counts (`ms:S3.2.uncertainty`) is dominated by seasonality (anticipated variation, not uncertainty) and by Poisson noise that is mechanically larger in small hospitals. It is backward-looking and says little about *technological* or regulatory uncertainty, which is the construct in DiMaggio and Powell (1983). The same variable is asked to serve both the transaction-cost hazard (demand volatility) and the institutional trigger (ambiguity about means and ends). Please deseasonalize, control for size, and justify the construct for each theory.

**m3. Model scope (`cmt:11`).** Proposition 1 is true by construction, because modularity is defined as multiplying specificity by (1−m). The formalization therefore adds less than claimed under the first contribution. The model treats m as exogenous, though the paper's empirical object is a chosen hospital-level variable. It has no role for modularity in s or G, and it contains no institutional term, so the "adjudication" is purely empirical.

**m4. Estimation details (`cmt:12`).** The outsourcing share is bounded on [0,1]. Report a fractional-response check. Report the marginal effect of modularity at several values of uncertainty, with a figure. Report control coefficients in an appendix. State the number of states and hospitals per state, and how the peer variable is defined where the state contains a single sample hospital.

**m5. Survey documentation (`cmt:13`).** The "Hospital IT Sourcing Survey" is described only generically (`ms:S3.1`). Provide the response rate, sampling frame, item wording, the definition of "certified standard" and by whom the certification is granted, and any validation against administrative or vendor records.

**m6. Unit of decision (`cmt:14`).** For system hospitals the IT sourcing decision may be made at the system level. The unit of analysis, clustering and the peer measure should reflect this.

**m7. Calibration of language (`cmt:15`).** "Rule out", "exactly what the transaction-cost account predicts", "on closer inspection" and "fashion" should be replaced with language proportionate to a single correlational panel. The advice that hospital leaders "should attend first to the modularity of their systems" (`ms:S5.1`) is not supported by evidence of causal or performance effects.

**m8. Limitations (`cmt:16`).** The Limitations section (`ms:S5.2`) is three sentences and omits the threats set out above: reverse causality, common-source reporting, state-year shocks, mediator and bad-control problems, and the absorbed national trend.

---

## 4. Recommendation and rationale

**Reject.**

*Rationale.* The paper's central claim is that modularity, and not mimicry, drove the diffusion of IT outsourcing, and that the data "rule out" the institutional account. That claim fails on its own terms, for five reasons.

- The theoretical anchor is internally inconsistent. Proposition 2 contradicts Assumption A3, and the appendix proof contains an algebraic error (M1).
- The reading of the peer result confuses a non-significant estimate with a demonstrated zero. It treats a plausible mediator as a rival. It tests a single arbitrary peer definition with understated standard errors. It uses year effects that absorb the very diffusion curve it claims to explain (M2, M3).
- The main safeguard against capability confounding is a bad control (M4).
- The mechanism is untested and partly contradicted by the paper's own use of the specificity variable (M5).
- Causal identification rests on within-hospital variation in a self-reported, plausibly endogenous variable, with a one-sentence event study of a reduced form that cannot, as described, isolate modularity (M6).

On top of this, the failed hypothesis is not reported in the abstract (M7), and basic arithmetic and table inconsistencies appear in the data description (M8).

None of these problems is merely cosmetic, and several are mutually reinforcing. The corrected model happens to be consistent with the data (the negative interaction), and the dataset is potentially valuable. A *fundamentally* reworked paper could therefore be publishable at a good outlet. Such a paper would make a more modest claim: modularity is a robust correlate of outsourcing, and state-level peer prevalence adds little under a given definition. It would correct the model; test the specificity mechanism directly; use pre-determined controls; treat standards adoption as potentially itself institutional; and report identification properly. That is a new paper rather than a revision, and I would be willing to review it. If the editor prefers to offer major revision, the minimum conditions are M1 (correct the model and re-derive the hypotheses), M2 and M3 (reframe the null and add the listed tests), M4 (replace the control), M6 (full, robust event study with first stage) and M8 (reconcile the data), together with a withdrawal of the "rule out" and "first study" language.

---

## Decisions for the reviewer

1. **Accept, reject or modify `cmt:1` (the Prop 2 reversal).** This is the finding I most want checked. My derivation is by hand and `asserted`. A short sympy check of d²k*/dm du under A3 would settle it, and I recommend running one before the report is signed.
2. **Severity ratings.** Confirm whether M1 and M2 are rated "fatal" or downgraded to "damaging". M2's rating depends on how much weight you give the "rule out" language, versus the more modest claim a revised paper could support.
3. **Recommendation.** Choose between Reject (my recommendation) and Major Revision with the stated minimum conditions.
4. **Literature in m1.** I could not verify Loh & Venkatraman (1992), Ang & Cummings (1997), Poppo & Zenger (1998), Gelman & Stern (2006), Goodman-Bacon (2021), Sun & Abraham (2021) or Callaway & Sant'Anna (2021) from the manuscript, and the reading of Williamson (1991) in M1 point 3 is from memory. Please confirm or delete each before signing.
5. **Table arithmetic in M8.** Confirm the 4,532 versus 4,712 discrepancy and the t-statistic for the uncertainty coefficient against your own reading of Table 2. Decide whether to raise them as numerical errors or as questions for the authors.
6. **Tone.** Decide how much of M6's critique of the event study you wish to put to the authors as requests for information (full results) and how much as a finding that the design cannot isolate modularity.
