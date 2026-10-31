# Run 03: Simulated Reviewer, Transaction-cost economist (strategy)

**SIMULATED REVIEW. This is not a review and is never sent to authors.** It simulates a reviewer with perspective `persp:R-TCE` for the focal human reviewer, who decides and signs.

- Instruction set: Reviewership v0.1 (23 October 2026), Role 2 (Simulated Reviewer)
- Manuscript: `ms:TEST`, "Modularity, Not Mimicry: Interoperability Standards and the Diffusion of IT Outsourcing in U.S. Hospitals"
- Lens: Transaction-cost economist (strategy). Relation to focal reviewer: resembling
- Weights: EPI 0.9, INF 0.9, TEC 0.7, ONT 0.6, PRA 0.4
- Material inferences: endorsed MI1, MI6, MI8, MI9; rejected MI3, MI7, MI10; neutral on the rest (MI2, MI4, MI5)
- Inputs used: only the run file (instruction set, configuration, manuscript). No other files, no web.
- Check status: every formal or numerical finding below is `asserted`. None has been run by the harness. The checks are in the Annex (`r-tce:chk:1` to `r-tce:chk:4`).

## 0. Standards applied by this simulated reviewer

These are the checkable conditions this perspective brings to `ms:TEST`. They are drawn from the configured parameters and are listed so that a panel can see what each finding is measured against.

```json
[
 {"@id": "r-tce:std:1", "dimension": "INF", "parameter": "INF.3", "text": "Every proposition must have a proof that the scorekeeper can re-derive; a proof that drops a term is not a proof."},
 {"@id": "r-tce:std:2", "dimension": "INF", "parameter": "INF.3", "text": "If an interaction is hypothesized, the derivation must give its sign on the scale on which it is tested."},
 {"@id": "r-tce:std:3", "dimension": "INF", "parameter": "INF.1", "text": "Abductive moves (inference to a best explanation of a result) must be labelled as such and kept out of conclusions unless tested."},
 {"@id": "r-tce:std:4", "dimension": "EPI", "parameter": "EPI.5", "text": "A claim of no effect requires an interval or an equivalence test against a stated smallest effect of interest, not a non-significant coefficient (MI7 rejected)."},
 {"@id": "r-tce:std:5", "dimension": "TEC", "parameter": "TEC.3", "text": "No control that is itself caused by the outcome or by the treatment (no post-treatment or bad controls)."},
 {"@id": "r-tce:std:6", "dimension": "TEC", "parameter": "TEC.3", "text": "Staggered-adoption designs must use an estimator robust to heterogeneous effects, and standard errors must be clustered at the level at which treatment varies."},
 {"@id": "r-tce:std:7", "dimension": "EPI", "parameter": "EPI.3", "text": "Fixed-effects identification (MI6) is accepted only with an argument that excludes time-varying confounders and reverse causation."},
 {"@id": "r-tce:std:8", "dimension": "ONT", "parameter": "ONT.2", "text": "A function-level model tested on hospital-level data needs an explicit aggregation step."},
 {"@id": "r-tce:std:9", "dimension": "TEC", "parameter": "TEC.4", "text": "Reported counts, coefficients, standard errors and significance markers must agree with each other."}
]
```

## 1. Claimed contributions

These are the contributions as the manuscript states them, in its own words, with loci.

```json
[
 {"@id": "r-tce:ctb:1", "locus": "§1 para 3; §2.3", "text": "\"we formalize the link between modularity and the make-or-buy decision in a simple transaction-cost model, deriving two propositions\" (Prop. 1: ∂k*/∂m > 0; Prop. 2: ∂²k*/∂m∂u > 0)"},
 {"@id": "r-tce:ctb:2", "locus": "§1 para 3", "text": "\"we test these propositions against an institutional rival using a decade-long panel of hospitals\""},
 {"@id": "r-tce:ctb:3", "locus": "§1 para 3; §4 (H3)", "text": "\"once modularity is measured, the apparent peer effects that have motivated institutional accounts disappear\""},
 {"@id": "r-tce:ctb:4", "locus": "Abstract; §1 para 3", "text": "\"the first study to adjudicate directly between transaction-cost and institutional explanations of IT outsourcing\""},
 {"@id": "r-tce:ctb:5", "locus": "§5.1", "text": "For TCE: \"Specificity is not a fixed property of an activity; it is partly a product of interface design\", so firm boundaries respond to technological standards"},
 {"@id": "r-tce:ctb:6", "locus": "Abstract; §5; §6", "text": "\"The results rule out mimetic isomorphism as a driver of IT outsourcing in this setting\"; the practice \"is, on closer inspection, economizing\""},
 {"@id": "r-tce:ctb:7", "locus": "§5.1", "text": "For practice: \"hospital leaders considering outsourcing should attend first to the modularity of their systems\""}
]
```

## 2. Scoreboard

The scoreboard records commitments as this scorekeeper attributes them. A commitment is `avowed` when the manuscript states it. It is `consequential` when it follows from avowed commitments by an inference this scorekeeper endorses, and that inference is named. Wherever I give an entitlement status for a formal or numerical commitment, it is my assertion until the matching check has run.

```json
{
 "@id": "r-tce:sb:1",
 "@type": "Scoreboard",
 "perspective": "persp:R-TCE",
 "manuscript": "ms:TEST",
 "commitments": [
  {"@id": "r-tce:cmt:1", "kind": "avowed", "locus": "Abstract; §1 para 2; §2.2", "content": "Interoperability standards make IT functions modular and lower effective asset specificity; effective specificity is k(1-m).", "entitlement": {"status": "default", "basis": "MI8 (endorsed) for the general claim. In this setting the link from m to measured specificity is not shown; see r-tce:chl:8."}},
  {"@id": "r-tce:cmt:2", "kind": "avowed", "locus": "§1 para 2", "content": "Relationship-specific assets expose parties to hold-up, which markets govern poorly; activities with such assets are kept in-house.", "entitlement": {"status": "default", "basis": "MI1 (endorsed); deferred to Williamson 1975, 1985"}},
  {"@id": "r-tce:cmt:3", "kind": "avowed", "locus": "§2.2, Assumption A3", "content": "h1/h0 > g1/(s+g0): hold-up hazards respond more strongly to uncertainty than in-house adaptation costs do, in proportional terms.", "entitlement": {"status": "deferred", "basis": "Williamson 1991; accepted by this scorekeeper as a faithful formalization"}},
  {"@id": "r-tce:cmt:4", "kind": "avowed", "locus": "§2.3 Prop. 1; Appendix", "content": "∂k*/∂m > 0.", "entitlement": {"status": "argued", "basis": "Appendix, proof of Prop. 1. Re-derivation agrees (asserted; r-tce:chk:1)."}},
  {"@id": "r-tce:cmt:5", "kind": "avowed", "locus": "§2.3 Prop. 2; Appendix", "content": "∂²k*/∂m∂u > 0.", "entitlement": {"status": "unentitled", "basis": "The proof treats H(u) in the denominator as constant in u, saying modularity operates on the denominator 'only through the factor (1-m)'. With H'(u) = h1 included, the sign is negative under A3 (r-tce:cmt:6; asserted; r-tce:chk:1)."}},
  {"@id": "r-tce:cmt:6", "kind": "consequential", "inference": "Deductive: differentiation of k* (§2.3) under A3 (§2.2)", "locus": "derived from §2.2-§2.3", "content": "∂²k*/∂m∂u = (∂k*/∂u)/(1-m) = [g1 h0 - h1(s+g0)] / [H(u)^2 (1-m)^2], which is < 0 under A3. Uncertainty narrows the outsourcing range, and it narrows the modularity effect too.", "entitlement": {"status": "argued", "basis": "By this scorekeeper's derivation from the manuscript's own premises; asserted until r-tce:chk:1 runs."}},
  {"@id": "r-tce:cmt:7", "kind": "avowed", "locus": "§2.4 H1; §4; Table 2", "content": "H1: modularity is positively associated with the outsourcing share.", "entitlement": {"status": "evidenced", "basis": "Table 2, Modularity row, Models 2-4 (0.112, 0.118, 0.097; all ***), as a within-hospital association"}},
  {"@id": "r-tce:cmt:8", "kind": "avowed", "locus": "§2.4 H2; §4", "content": "H2: the modularity-outsourcing association is stronger when uncertainty is high.", "entitlement": {"status": "challenged", "basis": "Contradicted by the manuscript's own evidence: Table 2, Modularity × uncertainty, Model 3, -0.061 (0.019). §4: 'contrary to H2'."}},
  {"@id": "r-tce:cmt:9", "kind": "avowed", "locus": "§3.3", "content": "'Identification therefore comes from within-hospital changes in modularity over time.'", "entitlement": {"status": "challenged", "basis": "See r-tce:cmt:10 and r-tce:chl:5"}},
  {"@id": "r-tce:cmt:10", "kind": "consequential", "inference": "MI6 (endorsed)", "locus": "from §3.3", "content": "β1 identifies the causal effect of modularity on the outsourcing share, provided no time-varying confounders and no reverse causation.", "entitlement": {"status": "challenged", "basis": "The proviso is unargued except for capability, and that argument fails (r-tce:cmt:11)"}},
  {"@id": "r-tce:cmt:11", "kind": "avowed", "locus": "§3.3 para 2; §4 Robustness", "content": "Because the modularity effect survives the in-house IT staffing control, it 'cannot be attributed to capability differences'.", "entitlement": {"status": "unentitled", "basis": "Staffing is caused by outsourcing (r-tce:cmt:12), so it is a bad control; see r-tce:inc:4"}},
  {"@id": "r-tce:cmt:12", "kind": "avowed", "locus": "§3.2 (In-house IT staffing)", "content": "'outsourcing a function transfers its staff to the vendor or eliminates the positions'.", "entitlement": {"status": "default", "basis": "Stated by the manuscript; accepted"}},
  {"@id": "r-tce:cmt:13", "kind": "avowed", "locus": "§4 Robustness", "content": "The event study on staggered state requirements (2011-2016) is 'consistent with a causal effect of modularity'.", "entitlement": {"status": "challenged", "basis": "No estimates are reported. The design is two-way fixed effects (TWFE) with staggered adoption. It is a reduced form of the mandate, with no first stage on m."}},
  {"@id": "r-tce:cmt:14", "kind": "avowed", "locus": "§4 (H3)", "content": "Once modularity enters, the peer coefficient falls and is not significant; 'H3 is not supported'.", "entitlement": {"status": "evidenced", "basis": "Table 2, Peer row: 0.137 (0.031) in Model 1 vs 0.042 (0.038) in Model 2. Evidenced as a description only."}},
  {"@id": "r-tce:cmt:15", "kind": "consequential", "inference": "MI7, used by the manuscript and rejected by this scorekeeper", "locus": "Abstract; §5 para 1", "content": "Peer outsourcing has no effect once modularity is controlled, so mimetic isomorphism is 'ruled out'.", "entitlement": {"status": "unentitled", "basis": "No interval or equivalence argument. The 95% interval for the Model 2 peer coefficient is about [-0.032, 0.116] (asserted; r-tce:chk:3)."}},
  {"@id": "r-tce:cmt:16", "kind": "avowed", "locus": "§4 (H3)", "content": "'the apparent peer effect reflects the common diffusion of standards across hospitals in the same state, not imitation'.", "entitlement": {"status": "challenged", "basis": "An unlabelled abductive move; no test is reported"}},
  {"@id": "r-tce:cmt:17", "kind": "avowed", "locus": "§5 para 2", "content": "The negative interaction reflects 'legitimacy pressures to retain in-house functions' under volatile demand.", "entitlement": {"status": "unentitled", "basis": "No evidence offered; unlabelled abduction (INF.1); invokes MI10, which this scorekeeper rejects"}},
  {"@id": "r-tce:cmt:18", "kind": "avowed", "locus": "§5 para 2", "content": "'This interpretation is consistent with our theory'.", "entitlement": {"status": "unentitled", "basis": "See r-tce:inc:2"}},
  {"@id": "r-tce:cmt:19", "kind": "avowed", "locus": "Abstract; §6", "content": "The spread of IT outsourcing is economizing: 'Its substance is economizing.'", "entitlement": {"status": "challenged", "basis": "Partly evidenced (r-tce:cmt:7); the hold-up channel is not shown (r-tce:cmt:21)"}},
  {"@id": "r-tce:cmt:20", "kind": "consequential", "inference": "MI9 (endorsed)", "locus": "from §2.2-§2.3 and §6", "content": "Observed outsourcing shares are optimal responses to (k, m, u, s). So the model, not an outside mechanism, must account for the sign of the observed m × u interaction.", "entitlement": {"status": "argued", "basis": "Met once Prop. 2 is corrected (r-tce:cmt:6); not met by the manuscript as written"}},
  {"@id": "r-tce:cmt:21", "kind": "consequential", "inference": "Deductive from §2.2: m enters C_B only through H(u)k(1-m)", "locus": "from §2.2", "content": "Modularity affects outsourcing only through effective specificity. If the specificity measure (§3.2) captures effective specificity, the modularity coefficient conditional on it should be near zero.", "entitlement": {"status": "challenged", "basis": "Table 2 shows β1 > 0 conditional on specificity; see r-tce:inc:5. That this measure reads as effective specificity is my inference."}},
  {"@id": "r-tce:cmt:22", "kind": "avowed", "locus": "§2.4 para 1", "content": "Prop. 1 implies H1 and Prop. 2 implies H2 on the spending-weighted share Φ, 'since functions with k<k* are outsourced'.", "entitlement": {"status": "challenged", "basis": "For H1 this holds for any fixed distribution of k (monotone). For H2 it needs an assumption on the distribution of k (r-tce:chl:2)."}},
  {"@id": "r-tce:cmt:23", "kind": "avowed", "locus": "§3.2; Table 2 (Asset specificity row)", "content": "Asset specificity is negatively associated with the outsourcing share.", "entitlement": {"status": "evidenced", "basis": "Table 2: -0.094 to -0.088, all ***. Corroborates the canon (Monteverde & Teece 1982; Masten 1984)."}},
  {"@id": "r-tce:cmt:24", "kind": "avowed", "locus": "§3.1", "content": "A balanced panel of 412 hospitals observed annually 2009-2019, giving 4,712 hospital-year observations.", "entitlement": {"status": "challenged", "basis": "412 × 11 = 4,532, not 4,712 (asserted; r-tce:chk:3)"}},
  {"@id": "r-tce:cmt:25", "kind": "avowed", "locus": "Abstract; §1 para 3", "content": "The first study to adjudicate directly between transaction-cost and institutional explanations of IT outsourcing.", "entitlement": {"status": "challenged", "basis": "Priority not checked by the manuscript; candidate prior studies listed in r-tce:fnd:15 (to verify)"}}
 ],
 "incompatibilities": [
  {"@id": "r-tce:inc:1", "between": ["r-tce:cmt:3", "r-tce:cmt:5"], "reason": "Under A3 the true cross-partial ∂²k*/∂m∂u has the sign of g1 h0 - h1(s+g0), and A3 makes this negative. A3 and Prop. 2 cannot both hold.", "status": "asserted", "check": "r-tce:chk:1"},
  {"@id": "r-tce:inc:2", "between": ["r-tce:cmt:18", "r-tce:cmt:5"], "reason": "The theory as stated (Prop. 2, H2) predicts a positive interaction. A negative interaction explained by a mechanism the model 'abstracts from' is not consistent with that theory. It is consistent with the corrected theory (r-tce:cmt:6), which the manuscript does not state."},
  {"@id": "r-tce:inc:3", "between": ["r-tce:cmt:17", "r-tce:cmt:19"], "reason": "Invoking legitimacy pressures to explain a main estimate concedes that a non-economizing, institutional force shapes sourcing in this setting. That clashes with 'Its substance is economizing' and with the Abstract's claim that a practice 'read as institutional fashion' is economizing. The clash with the narrower claim about mimetic isomorphism is weaker, because legitimacy-signalling and mimicry are distinct institutional mechanisms."},
  {"@id": "r-tce:inc:4", "between": ["r-tce:cmt:11", "r-tce:cmt:12"], "reason": "A control that the outcome mechanically moves cannot show that a treatment effect is free of confounding. Conditioning on it can create bias or hide it.", "status": "asserted", "check": "r-tce:chk:4"},
  {"@id": "r-tce:inc:5", "between": ["r-tce:cmt:21", "Table 2: Modularity and Asset specificity rows"], "reason": "Conditional incompatibility, resting on my reading of the measure. If the CIO rating of transfer cost measures effective specificity k(1-m), the model implies β1 ≈ 0 once it is controlled. Instead β1 = 0.112 (0.024), and the specificity coefficient barely moves when m enters (-0.094 to -0.091). Either the measure does not capture effective specificity, or m works through a channel other than hold-up."},
  {"@id": "r-tce:inc:6", "between": ["r-tce:cmt:24", "§3.1 'balanced panel ... 2009 to 2019'"], "reason": "Eleven waves of 412 hospitals give 4,532 observations. A t-1 peer measure may cost the first wave, giving 4,120. Neither is 4,712.", "status": "asserted", "check": "r-tce:chk:3"}
 ],
 "challenges": [
  {"@id": "r-tce:chl:1", "on": "r-tce:cmt:5", "request": "Re-derive Prop. 2 with H'(u) = h1 included, and state the sign under A3."},
  {"@id": "r-tce:chl:2", "on": "r-tce:cmt:22", "request": "State the (spending-weighted) distribution F of k across functions and derive ∂Φ/∂m and ∂²Φ/∂m∂u, including the case k* ≥ 1. The interaction on the Φ scale contains F''(k*)·k*_m·k*_u + F'(k*)·k*_mu, so its sign is not fixed by k*_mu alone."},
  {"@id": "r-tce:chl:3", "on": "r-tce:cmt:15", "request": "Report confidence intervals and an equivalence test for the Model 2 peer coefficient against a stated smallest effect of interest, plus a formal test of the change from Model 1 to Model 2."},
  {"@id": "r-tce:chl:4", "on": "r-tce:cmt:16", "request": "Show that standards diffused at the state level and that this accounts for the Model 1 peer correlation, for example by adding state-by-year effects or the state-requirement indicator."},
  {"@id": "r-tce:chl:5", "on": "r-tce:cmt:10", "request": "Address reverse causation: vendors may install certified interfaces when they take over functions. Show that changes in m precede changes in Φ."},
  {"@id": "r-tce:chl:6", "on": "r-tce:cmt:11", "request": "Replace in-house staffing with a capability measure fixed before treatment, such as baseline staffing interacted with year."},
  {"@id": "r-tce:chl:7", "on": "r-tce:cmt:13", "request": "Report the event study, using an estimator robust to heterogeneous effects, a first stage of requirement on m, and state-clustered inference."},
  {"@id": "r-tce:chl:8", "on": "r-tce:cmt:1", "request": "Show within hospitals that m lowers measured specificity (the first link of the mechanism), and say whether the specificity measure is nominal k or effective k(1-m)."},
  {"@id": "r-tce:chl:9", "on": "r-tce:cmt:17", "request": "Delete the legitimacy account, or label it as a conjecture and test it."},
  {"@id": "r-tce:chl:10", "on": "r-tce:cmt:25", "request": "Position the priority claim against prior studies of IT-outsourcing diffusion and governance (r-tce:fnd:15)."},
  {"@id": "r-tce:chl:11", "on": "§3.2 Environmental uncertainty", "request": "Argue why demand volatility (coefficient of variation of admissions) is the uncertainty that generates adaptation needs in IT transactions. Reconcile the standardized measure (mean 0, so it takes negative values) with u ≥ 0 and H(u) = h0 + h1 u in the model."},
  {"@id": "r-tce:chl:12", "on": "Table 2, Model 3, Environmental uncertainty", "request": "0.084 (0.051) is marked *** but t ≈ 1.65. Correct the marker or the numbers (asserted; r-tce:chk:3)."}
 ]
}
```

## 3. Assessment by dimension

The dimensions are taken in order of weight. EPI and INF tie at 0.9; EPI comes first because the main conclusion (that mimicry is "ruled out") is an evidential claim. Each finding names the commitment, the missing entitlement or the incompatibility, and the repair. Formal and numerical findings stay `asserted` until the harness runs them.

### 3.1 EPI, Epistemological (weight 0.9)

In summary, H1 is evidenced as a within-hospital association. The two claims that carry the paper's title fall short of what this perspective requires: that mimicry is ruled out, and that the effect is causal. Rejecting MI7 drives the first of these. Requiring an argument against time-varying confounding, even though MI6 is endorsed, drives the second.

```json
[
 {"@id": "r-tce:fnd:4", "dimension": "EPI", "parameter": "EPI.5; INF.2 (MI7 rejected)", "severity": "damaging", "status": "asserted", "check": "r-tce:chk:3",
  "commitment": "r-tce:cmt:15. The Abstract and §5 say the results 'rule out mimetic isomorphism'.",
  "missingEntitlement": "The inference from 'no longer significant' (Table 2, Model 2: 0.042 (0.038)) to 'no effect' is MI7. The approximate 95% interval [-0.032, 0.116] includes economically meaningful peer effects. The change from 0.137 to 0.042 is not tested. Ignoring the covariance of the two estimates gives z ≈ 1.94; the covariance is needed to test it properly.",
  "repair": "Report intervals. Run an equivalence test (TOST) against a declared smallest effect of interest. Test the coefficient change formally, for example by stacked estimation or a decomposition of omitted-variable bias. Rephrase as 'no detectable incremental association of same-state lagged peer outsourcing'."},
 {"@id": "r-tce:fnd:5", "dimension": "EPI", "parameter": "EPI.3; INF.7", "severity": "damaging", "status": "asserted",
  "commitment": "r-tce:cmt:14 and r-tce:cmt:16. H3, tested by adding m, adjudicates between economizing and mimicry (§2.4 last para).",
  "missingEntitlement": "The test does not discriminate between the two accounts. (a) Modularity may itself be the channel of institutional diffusion. State requirements for certified interfaces (§4 Robustness) are what institutional theory calls coercive isomorphism, and interface adoption may also be mimetic. Controlling for m then blocks the institutional pathway rather than testing it. (b) The peer measure is the lagged mean of other sample hospitals in the same state (§3.2). It is not the set of referents 'perceived as legitimate or successful' that the rival names, so the rival is not stated in its strongest form. (c) A same-state mean of sample peers, with year effects, raises the reflection problem (Manski 1993, to verify), and thin state cells add measurement error.",
  "repair": "State the rival in its strongest form, with referent-based peers (system affiliates, prestige or size leaders, CIO networks). Derive predictions on which the two accounts differ: TCE predicts the m effect concentrated in functions whose interfaces were standardized and whose nominal k lies near the threshold; mimicry predicts outsourcing that follows referents whatever the hospital's own m. Note that this perspective rejects MI3, so the Model 1 peer correlation was never evidence of imitation in the first place. The weakness of the test cuts against both readings."},
 {"@id": "r-tce:fnd:6", "dimension": "EPI", "parameter": "EPI.3; INF.2 (MI6 endorsed)", "severity": "damaging", "status": "asserted",
  "commitment": "r-tce:cmt:10. β1 is causal, by MI6, absent time-varying confounders.",
  "missingEntitlement": "The only time-varying confounder addressed is capability, and that attempt fails (r-tce:fnd:7). Reverse causation is not addressed: a vendor taking over a function may install certified interfaces, so outsourcing raises m. Differential exposure to the 2009 federal incentive programme varies within hospitals over time and is not absorbed by year effects (§3.3).",
  "repair": "Show timing: distributed lags of m on Φ, and tests of whether past Φ predicts m. Use the staggered state requirements as an instrument for m and report the first stage and 2SLS. Add hospital-specific trends or interactions of incentive-programme exposure with year."},
 {"@id": "r-tce:fnd:9", "dimension": "EPI", "parameter": "EPI.3; ONT.3 (individual-mechanistic)", "severity": "damaging", "status": "asserted",
  "commitment": "r-tce:cmt:1 and r-tce:cmt:21. Modularity raises outsourcing by lowering effective specificity and so the hold-up hazard (Abstract; §2.2; §5).",
  "missingEntitlement": "The mechanism is not evidenced. Table 2 shows m predicts Φ conditional on measured specificity, and the specificity coefficient is stable when m enters (r-tce:inc:5). This is consistent with m acting through a channel other than hold-up, for example by raising vendors' production-cost advantage s through scale economies. That channel is also economizing, but it is not transaction-cost economizing. Controlling for specificity also conditions on the mediator the model names. The m-specificity correlation is not reported, so the stability reading is my inference.",
  "repair": "Report the within-hospital regression of specificity on m. Estimate H1 with and without specificity and decompose. Say whether the CIO rating measures nominal k or effective k(1-m). Test the hold-up channel against the production-cost channel at the function level (see §5, the rival explanation)."},
 {"@id": "r-tce:fnd:16", "dimension": "EPI", "parameter": "EPI.6", "severity": "minor", "status": "asserted",
  "commitment": "§3.1: hospitals were included only if they 'responded to the survey in every year'.",
  "missingEntitlement": "Selection on response and on survival: closures and mergers drop out (§5.2 concedes over-representation of larger hospitals). Under EPI.6 a single informant is acceptable, but m, specificity and Φ all come from the same CIO survey.",
  "repair": "Report attrition and a robustness check on the unbalanced panel. Validate Φ against administrative spending data where possible."},
 {"@id": "r-tce:fnd:14", "dimension": "EPI", "parameter": "EPI.5", "severity": "minor", "status": "asserted", "check": "r-tce:chk:3",
  "commitment": "The Abstract says modularity 'strongly predicts' outsourcing.",
  "missingEntitlement": "§4 itself reports about one-sixth of an SD per SD of m (0.112 × 0.24 ≈ 0.027; 0.027/0.17 ≈ 0.16). Within R² rises from 0.08 to 0.13. The arithmetic is right (asserted); 'strongly' is not.",
  "repair": "Describe the magnitude as modest, and benchmark it against the decade's doubling of outsourcing (§1)."}
]
```

### 3.2 INF, Inferential (weight 0.9)

In summary, Prop. 1 is correctly proved (asserted). Prop. 2 is mis-derived: the proof drops the dependence of H(u) on u. Under the manuscript's own A3 the cross-partial is negative. That is the sign the data show (Table 2, Model 3: -0.061). The legitimacy account in §5 is therefore both unlicensed and unnecessary. This is the most consequential finding in the run, and its repair helps the authors.

```json
[
 {"@id": "r-tce:fnd:1", "dimension": "INF", "parameter": "INF.3; TEC.2 (re-derive); TEC.5", "severity": "damaging", "status": "asserted", "check": "r-tce:chk:1",
  "commitment": "r-tce:cmt:5. Prop. 2: ∂²k*/∂m∂u > 0 (§2.3; Appendix).",
  "incompatibility": "r-tce:inc:1. The Appendix proof says modularity operates on the denominator 'only through the factor (1-m)' and writes the cross-partial as g1/[H(u)(1-m)²]. But H(u) = h0 + h1u also sits in the denominator. Differentiating (s+G(u))/[H(u)(1-m)²] in u by the quotient rule gives [g1 h0 - h1(s+g0)]/[H(u)²(1-m)²] = (∂k*/∂u)/(1-m). A3 says exactly that h1(s+g0) > g1 h0, so the cross-partial is negative.",
  "repair": "Correct the proof. Restate Prop. 2 as ∂²k*/∂m∂u < 0 under A3, with the reading that uncertainty shrinks the outsourcing range (Williamson 1991) and the modularity effect with it. Restate H2 with a negative sign. Say plainly that the corrected sign was implied by A3 before the data were seen. Under EPI.2 and EPI.4 the result is then a consequence of a prior assumption, not a novel prediction: the authors stated the opposite sign, and the data were known when the error was corrected. Its corroborating weight is therefore real but moderate."},
 {"@id": "r-tce:fnd:2", "dimension": "INF", "parameter": "INF.3 (r-tce:std:2); ONT.2 (r-tce:std:8)", "severity": "fixable", "status": "asserted", "check": "r-tce:chk:2",
  "commitment": "r-tce:cmt:22. Props 1-2 on the function-level threshold k* imply H1-H2 on the hospital-level, spending-weighted share Φ (§2.4).",
  "missingEntitlement": "There is no aggregation step. With Φ = F(k*), where F is the spending-weighted distribution of k, ∂²Φ/∂m∂u = F''(k*)·k*_m·k*_u + F'(k*)·k*_mu, so its sign depends on F. k* can exceed 1 (Φ saturates at 1). The linear specification in §3.3 imposes a constant interaction.",
  "repair": "Assume F explicitly (uniform gives sign(Φ_mu) = sign(k*_mu) for k* < 1) and derive the prediction on the Φ scale. Better, test at the function level: the probability that function j is bought, as a function of k_j, m, u and k_j × m."},
 {"@id": "r-tce:fnd:3", "dimension": "INF", "parameter": "INF.1 (r-tce:std:3); ONT.1; INF.2 (MI10 rejected)", "severity": "fixable", "status": "asserted",
  "commitment": "r-tce:cmt:17 and r-tce:cmt:18. Legitimacy pressures to keep visible in-house IT explain the negative interaction, and this is 'consistent with our theory' (§5 para 2).",
  "incompatibility": "r-tce:inc:2 and r-tce:inc:3. This is an unlabelled abduction ('We believe it reflects...') with no test. It invokes legitimacy as a force that works independently of efficiency (MI10, which this perspective rejects; legitimacy is not an admissible entity under ONT.1). It clashes with 'Its substance is economizing'. As an auxiliary added after a refutation, it reduces the theory's content (sophisticated falsificationism, EPI.2).",
  "repair": "Delete it. The corrected Prop. 2 (r-tce:fnd:1) accounts for the sign within the model, as MI9 requires (r-tce:cmt:20). If the authors keep it, they should label it a conjecture and test it, for example by checking whether the negative interaction is stronger in non-profit and public hospitals with community boards."}
]
```

### 3.3 TEC, Technical (weight 0.7)

In summary, the main fixed-effects specification is conventional. The two robustness claims meant to secure a causal reading do not do so. The Model 4 staffing control is a bad control. The event study uses an estimator known to be biased under staggered adoption, and its results are not reported. There are also two numerical inconsistencies.

```json
[
 {"@id": "r-tce:fnd:7", "dimension": "TEC", "parameter": "TEC.3 (r-tce:std:5)", "severity": "damaging", "status": "asserted", "check": "r-tce:chk:4",
  "commitment": "r-tce:cmt:11. Because the modularity effect survives Model 4, 'it cannot be attributed to differences in internal IT capability' (§3.3; §4).",
  "incompatibility": "r-tce:inc:4. §3.2 states that outsourcing moves staffing: 'outsourcing a function transfers its staff to the vendor or eliminates the positions'. Staffing is therefore partly an outcome of Φ, and probably of m through Φ. Conditioning on it is post-treatment conditioning. The coefficient's survival (0.097 (0.023)) is compatible with confounding by capability, and the attenuation from 0.118 to 0.097 is uninterpretable.",
  "repair": "Drop the claim, or control for capability measured before treatment: baseline (2009) staffing or IT budget interacted with year, or hospital-specific trends. Report β1 under each."},
 {"@id": "r-tce:fnd:8", "dimension": "TEC", "parameter": "TEC.3 (r-tce:std:6); TEC.1", "severity": "fixable", "status": "asserted",
  "commitment": "r-tce:cmt:13. A TWFE event study with leads and lags of state requirements (2011-2016) supports a causal effect of modularity (§4).",
  "missingEntitlement": "(a) With staggered timing and heterogeneous effects, TWFE leads and lags are contaminated by already-treated comparisons (Goodman-Bacon 2021; Sun & Abraham 2021; Callaway & Sant'Anna 2021; de Chaisemartin & D'Haultfoeuille 2020; all to verify). (b) It is a reduced form of the mandate on Φ, with no first stage on m. Mandates may also change vendor entry, and so s, which breaks the exclusion restriction for m. (c) No table or figure is reported. (d) The treatment and Peer_{s,t-1} vary at the state level, but standard errors are clustered by hospital (§3.3), which understates uncertainty for state-level regressors.",
  "repair": "Use a heterogeneity-robust estimator. Report the first stage and the event-study plot. Cluster by state, with a wild cluster bootstrap if states are few. Use the mandate as an instrument only after arguing the exclusion restriction. State whether code and survey data are available (TEC.1 preferred)."},
 {"@id": "r-tce:fnd:13", "dimension": "TEC", "parameter": "TEC.4 (r-tce:std:9)", "severity": "fixable", "status": "asserted", "check": "r-tce:chk:3",
  "commitment": "r-tce:cmt:24 (§3.1) and Table 2, Model 3.",
  "incompatibility": "r-tce:inc:6. N = 4,712 is not equal to 412 × 11 = 4,532 for a balanced 2009-2019 panel; 4,712/412 ≈ 11.44 waves. Separately, Table 2, Model 3, Environmental uncertainty, 0.084 (0.051) is marked *** but t ≈ 1.65 (p ≈ 0.10). Model 4's 0.079 (0.050) is correctly unmarked. All other markers in Table 2 agree with their t-ratios (asserted).",
  "repair": "Reconcile N with the panel structure; say how the t-1 peer measure is built for 2009. Correct the significance marker."}
]
```

### 3.4 ONT, Ontological (weight 0.6)

In summary, the ontology is congenial: boundedly rational hospitals choosing governance, with technologies and artifacts (interfaces) as shift parameters. A choice-theoretic model is the preferred model class (ONT.5). The problems are construct individuation (ONT.4, strict) and the bridge between levels, which is covered under r-tce:fnd:2.

```json
[
 {"@id": "r-tce:fnd:10", "dimension": "ONT", "parameter": "ONT.4 (strict); ONT.2", "severity": "fixable", "status": "asserted",
  "commitment": "§2.2 applies m to every function. §3.2 measures m over 'clinical information systems' only, while Φ covers all IT functions, including 'infrastructure hosting, help-desk support' (§2.1).",
  "missingEntitlement": "The construct being measured is not the construct the model uses. Clinical interface standards should not change the specificity of help desk or hosting, so the hospital-level Φ mixes functions the mechanism reaches with functions it does not.",
  "repair": "Use function-level outcomes, or restrict Φ to clinical-application functions. Use non-clinical functions as a placebo: TCE predicts no m effect there."},
 {"@id": "r-tce:fnd:11", "dimension": "ONT", "parameter": "ONT.4 (strict)", "severity": "fixable", "status": "asserted",
  "commitment": "§3.2: u is the coefficient of variation of quarterly admissions over three years, standardized.",
  "missingEntitlement": "In the model, u is the frequency of 'unanticipated adaptations' to the IT transaction (§2.2). Demand volatility is a distal proxy for that, and the manuscript does not argue the link. Standardization gives negative u, whereas the model requires u ≥ 0 and H(u) > 0 (r-tce:chl:11).",
  "repair": "Argue the link, or add a measure of technological or regulatory uncertainty specific to IT (for example, exposure to changing certification rules). Report results with the raw, non-negative measure."}
]
```

### 3.5 PRA, Pragmatic (weight 0.4)

In summary, the paper addresses strategy and organizational-economics readers in a gap-spotting style (PRA.2), which suits this perspective. Its priority and novelty claims are overstated, and its practice implication goes beyond its evidence. The low PRA weight keeps these from driving the verdict.

```json
[
 {"@id": "r-tce:fnd:15", "dimension": "PRA", "parameter": "PRA.3; EPI.4", "severity": "fixable", "status": "asserted",
  "commitment": "r-tce:cmt:25 ('the first study to adjudicate directly', Abstract; §1) and r-tce:ctb:5 (§5.1).",
  "missingEntitlement": "Prior work may already set economic against institutional influences on IT outsourcing. Candidates are Loh & Venkatraman 1992 on diffusion of IT outsourcing and the 'Kodak effect' (to verify) and Ang & Cummings 1997 on institutional influences on IS outsourcing (to verify). TCE make-or-buy has been tested for information services in Poppo & Zenger 1998 (to verify). The modularity-to-disintegration link is established in the paper's own sources (Baldwin & Clark 2000; Langlois 2002; Sanchez & Mahoney 1996) and tested in Hoetker 2006 (to verify). Even without the priority question, 'adjudicate directly' requires predictions on which the accounts differ, and r-tce:fnd:5 finds none.",
  "repair": "Drop or qualify the priority claim, and position the paper against these studies. Present ctb:5 as corroborating a known TCE proposition (MI8) in a new setting, with a formal link to make-or-buy."},
 {"@id": "r-tce:fnd:17", "dimension": "PRA", "parameter": "PRA.4 (low)", "severity": "minor", "status": "asserted",
  "commitment": "r-tce:ctb:7. Leaders 'should attend first to the modularity of their systems' (§5.1).",
  "missingEntitlement": "The advice rests on the causal reading that r-tce:fnd:6 and r-tce:fnd:7 leave open. If m is chosen together with sourcing (see the rival in §5), the advice runs the causation backwards.",
  "repair": "Make the advice conditional, or drop it."}
]
```

### 3.6 Strengths recorded on their merits (L6 Arbiter, Corroborate)

- `r-tce:str:1`: The asset-specificity coefficient is negative and stable across all four models (Table 2, -0.094 to -0.088). This corroborates the canonical finding that specificity predicts integration (Monteverde & Teece 1982; Masten 1984; Klein, Crawford & Alchian 1978 on appropriable quasi-rents). It is relation Corroborate(`ms:TEST`, canon).
- `r-tce:str:2`: A3 is a faithful formalization of Williamson (1991): markets adapt less well than hierarchies to disturbances. The model is closed form, as TEC.5 requires.
- `r-tce:str:3`: Prop. 1 and its proof are correct (asserted; r-tce:chk:1).
- `r-tce:str:4`: The core idea, that standards change the specificity firms face, is assimilable to TCE (INF.6, assimilative: accepted) through MI8. Once Prop. 2 is corrected, model and data agree on all signs. That agreement is a real asset of the paper, which the authors currently hide behind the legitimacy account.

## 4. Contribution verdicts

Each verdict says whether the contribution survives, is qualified or fails from this perspective. Each surviving or qualified contribution is re-voiced in TCE terms (L1), with a note on what the translation loses.

```json
[
 {"@id": "r-tce:vrd:1", "contribution": "r-tce:ctb:1", "verdict": "qualified",
  "narrowedClaim": "A closed-form TCE model in which modularity raises the make-or-buy threshold (Prop. 1). Under A3, uncertainty lowers the threshold and dampens the modularity effect (corrected Prop. 2: ∂²k*/∂m∂u < 0).",
  "basis": "r-tce:fnd:1, r-tce:fnd:2 (asserted pending r-tce:chk:1, r-tce:chk:2)",
  "revoiced": "Modularity is a shift parameter in Williamson's (1991) reduced-form comparison of governance costs. It moves the market-hierarchy crossover in asset specificity outward, and uncertainty moves it inward.",
  "lostInTranslation": "The claim that modularity is most valuable where uncertainty is greatest (§2.3 'intuitive reading') does not survive. Under A3 it is reversed."},
 {"@id": "r-tce:vrd:2", "contribution": "r-tce:ctb:2", "verdict": "qualified",
  "narrowedClaim": "In a decade-long hospital panel with fixed effects, modularity is associated with outsourcing (H1). The m × u interaction is negative, which matches the corrected Prop. 2. The test against the institutional rival does not discriminate between the accounts.",
  "basis": "r-tce:fnd:4, r-tce:fnd:5, r-tce:fnd:6, r-tce:fnd:9",
  "revoiced": "A within-firm panel test of the comparative-statics of a discrete structural alternatives model.",
  "lostInTranslation": "The 'against an institutional rival' framing. TCE does not need a peer test to be corroborated, and this peer test cannot refute the rival."},
 {"@id": "r-tce:vrd:3", "contribution": "r-tce:ctb:3", "verdict": "qualified",
  "narrowedClaim": "With modularity controlled, same-state lagged peer outsourcing has no statistically detectable incremental association with a hospital's outsourcing share. The interval still admits sizeable effects.",
  "basis": "r-tce:fnd:4 (MI7 rejected), r-tce:fnd:5",
  "revoiced": "Once the transaction attribute is measured, a diffusion covariate adds no detectable explanatory power.",
  "lostInTranslation": "'Disappear'. Losing significance is not disappearing."},
 {"@id": "r-tce:vrd:4", "contribution": "r-tce:ctb:4", "verdict": "fails",
  "basis": "The design does not adjudicate (r-tce:fnd:5). The priority claim is likely contradicted by prior studies (r-tce:fnd:15, to verify). It fails on the first ground even if the priority check comes out in the authors' favour.",
  "revoiced": null, "lostInTranslation": null},
 {"@id": "r-tce:vrd:5", "contribution": "r-tce:ctb:5", "verdict": "qualified",
  "narrowedClaim": "Field evidence that interface standardization is associated with vertical disintegration of IT functions. This is consistent with MI8, but the hold-up channel is not yet distinguished from a production-cost channel.",
  "basis": "r-tce:fnd:9, r-tce:fnd:15; Assimilate(ms:TEST, Langlois 2002 / Baldwin & Clark 2000)",
  "revoiced": "Specificity is partly a design variable, and standards that no single firm controls shift the specificity firms face. This is a special case of the TCE claim that standardization reduces asset specificity.",
  "lostInTranslation": "The novelty. 'Specificity is not a fixed property' is already in Langlois (2002) and Baldwin & Clark (2000). What is new here is the hospital IT setting and the closed-form link to make-or-buy."},
 {"@id": "r-tce:vrd:6", "contribution": "r-tce:ctb:6", "verdict": "fails",
  "basis": "'Rule out' rests on MI7 (rejected) and on a test that does not discriminate (r-tce:fnd:4, r-tce:fnd:5). §5's appeal to legitimacy pressures undercuts 'Its substance is economizing' (r-tce:inc:3). In a narrower form ('diffusion that looks mimetic can be accounted for by economizing on changed transaction attributes') it would be a qualified, plausible claim, once r-tce:fnd:6 and r-tce:fnd:9 are repaired.",
  "revoiced": null, "lostInTranslation": null},
 {"@id": "r-tce:vrd:7", "contribution": "r-tce:ctb:7", "verdict": "qualified",
  "narrowedClaim": "If the modularity effect is causal, modularity is a precondition for economical outsourcing.",
  "basis": "r-tce:fnd:17",
  "revoiced": "Invest in interface safeguards before contracting out.",
  "lostInTranslation": "The unconditional 'attend first'."}
]
```

## 5. Rival explanation (L10, within TCE)

The manuscript is written in my own tradition, so the strongest rival comes from inside TCE (L10).

**`r-tce:alt:1`, joint choice of governance and safeguard (with a production-cost variant).** Hospitals decide to outsource because vendors' production-cost advantage s rose over 2009-2019 (scale, hosted and cloud delivery). Having decided to buy, they invest in certified interfaces as a contractual safeguard. Modularity then works as an ex ante choice of technology that limits the appropriable quasi-rent (Klein, Crawford & Alchian 1978). Technology and governance are chosen together (Williamson 1985, the idea of simultaneous choice to verify). By MI9, the observed pairs (m, Φ) are joint optimal responses to rising s. In that case β1 measures joint determination, not the effect of exogenous modularity. A variant with weaker endogeneity has standards raising Φ mainly by raising s (vendor scale economies), not by cutting hold-up hazards. That variant is economizing, but through production costs rather than transaction costs (r-tce:fnd:9).

**Discriminating observations.**
1. *Timing.* The manuscript predicts that exogenous increases in m precede increases in Φ. The rival predicts that m rises in the year a sourcing contract starts, or after it.
2. *Mandate-induced variation.* The manuscript predicts that state requirements raise m (first stage) and that the induced m raises Φ (2SLS). The rival predicts a weak response among hospitals that had no plans to outsource.
3. *Function-level pattern (the sharpest test).* The hold-up account predicts the m effect concentrated in functions with high nominal specificity k near the threshold, mainly clinical applications, and growing with k up to the point where k(1-m) crosses k*. The production-cost variant predicts the largest effects in low-k commodity functions (hosting, help desk), where scale economies dominate and hold-up is negligible.

**Model re-specification in the tradition's model class (L12).** The canonical TCE test works at the level of the transaction (Monteverde & Teece 1982; Masten 1984). The re-specified model is a discrete choice of buy or make for each function j of hospital i in year t, on k_j, m_it, u_it, k_j × m_it and k_j × m_it × u_it, with hospital and year effects. The model predicts a positive sign on k_j × m_it and a negative sign on the triple interaction under A3. This replaces the aggregation step that r-tce:fnd:2 finds missing.

## 6. What would change my mind

What would lead this simulated reviewer to withdraw each damaging finding. None of the findings is rated fatal.

```json
[
 {"finding": "r-tce:fnd:1", "wouldWithdrawIf": "The harness runs r-tce:chk:1 and shows the true cross-partial is positive under A3, so my algebra is wrong. Or the authors show the model is specified differently, for example with H independent of u in the term modularity acts on."},
 {"finding": "r-tce:fnd:4", "wouldWithdrawIf": "An equivalence test rejects peer effects larger than a declared and defensible smallest effect of interest (for example, half the Model 1 estimate), and the change in the coefficient is significant once its covariance is accounted for. The claim would then need wording no stronger than 'no meaningful incremental peer effect'."},
 {"finding": "r-tce:fnd:5", "wouldWithdrawIf": "With referent-based peer measures and a test that controls for modularity in a way that does not block institutional pathways (for example, m fixed before peer exposure), the peer effect stays near zero, and the function-level pattern matches the TCE account rather than following referents."},
 {"finding": "r-tce:fnd:6", "wouldWithdrawIf": "Distributed-lag evidence shows changes in m precede changes in Φ and past Φ does not predict m, or a 2SLS estimate using state requirements has a strong first stage, a defended exclusion restriction and an effect similar to β1."},
 {"finding": "r-tce:fnd:7", "wouldWithdrawIf": "β1 is stable once capability is measured before treatment (baseline staffing or IT budget × year, hospital trends), and the staffing-control claim is dropped."},
 {"finding": "r-tce:fnd:9", "wouldWithdrawIf": "Within hospitals, m lowers measured specificity; β1 shrinks when specificity is treated as the mediator; and function-level effects are concentrated in high-k functions rather than commodity ones. Or the authors show the CIO rating measures nominal k, which would dissolve r-tce:inc:5."}
]
```

**L5 Deconstructor: what would have to hold for this tradition to be persuaded.** (i) The corrected Prop. 2 is stated, and the negative interaction is presented as a corroborated consequence of A3. (ii) Modularity is shown to lower effective specificity. (iii) Exogenous variation in m, through the mandates, raises Φ. (iv) The effect is concentrated where hold-up hazards were binding. With (i) to (iv) in place, this tradition would accept the economizing account without needing a verdict on mimicry.

## 7. Recommendation

```json
{"@id": "r-tce:rec:1", "recommendation": "major revision", "simulated": true}
```

**Major revision (simulated).** The paper's core argument is congenial to this tradition and well grounded: interoperability standards lower effective specificity (MI8) and so widen the make-or-buy threshold. H1 is evidenced as a within-hospital association, and the specificity result corroborates the canon. No finding is fatal. Six findings are damaging, though, and they reach the paper's headline claims.

- Prop. 2 is mis-derived and conflicts with the paper's own A3 (r-tce:fnd:1, asserted).
- "Rule out mimetic isomorphism" rests on MI7, which this tradition rejects, and on a test that does not tell the two accounts apart (r-tce:fnd:4, r-tce:fnd:5).
- The causal reading is open to reverse causation and joint choice (r-tce:fnd:6).
- The capability robustness claim depends on a bad control (r-tce:fnd:7).
- The hold-up mechanism itself is not evidenced (r-tce:fnd:9).

So ctb:1, 2, 3, 5 and 7 survive only in qualified form, and ctb:4 and 6 fail as stated (§4). Each repair is concrete and within reach. The most important one, correcting Prop. 2, turns the paper's awkward H2 result into agreement between model and data, and removes the need for the legitimacy account. Rejection is not warranted, because the repaired paper would make a sound, if modest, contribution to strategy and organizational economics. Minor revision is not enough, because the title claim and the causal claim need new analyses, not just new wording.

## 8. Self-location

These are the parameters that most drive the verdicts, so a panel can trace disagreements to them.

1. **INF.3 = proof, with TEC.2 = re-derive and TEC.5 = closed form required.** These produce r-tce:fnd:1 and r-tce:fnd:2, the qualified verdict on ctb:1, and the finding that model and data in fact agree. A reviewer who trusts derivations (TEC.2 = trust) would take Prop. 2 as stated, see H2 as a refutation, and might accept the legitimacy account.
2. **MI7 rejected, with EPI.5 (effect sizes) and EPI.2 (sophisticated falsificationism).** These produce r-tce:fnd:4 and the failure of ctb:6. A reviewer who accepts MI7 would read Model 2 as the authors do and let "rule out" stand. Rejecting MI3 also makes this reviewer indifferent to whether the peer test favours imitation at all.
3. **TEC.3 = high estimator discipline.** This produces r-tce:fnd:7 and r-tce:fnd:8.

Sources of leniency a panel should note: the endorsements of **MI8** and **MI6**. A reviewer who rejects MI8 would treat the claim that modularity lowers specificity as unentitled (r-tce:cmt:1) and could rate r-tce:fnd:9 fatal. A reviewer who rejects MI6 would weigh r-tce:fnd:6 more heavily. Because this perspective resembles the focal reviewer's, a panel should expect it to share the focal reviewer's sympathy for the economizing account. A differing (institutional) simulation is the natural counterweight on r-tce:fnd:3 and r-tce:fnd:5.

## Annex. Checks for the harness

None of these checks has been run. Each states what output would bear out the finding it supports. Until the harness reports, every linked finding stays `asserted`. Only `sympy`, `numpy`, `scipy` and `statsmodels` are used.

```json
[
 {"@id": "r-tce:chk:1", "tests": ["r-tce:fnd:1", "r-tce:inc:1", "r-tce:cmt:4", "r-tce:cmt:6"], "expected": "P1 equals the manuscript's expression: True. P2 equals the manuscript's expression: False. Scaled numerator equals g1*h0 - h1*(s+g0): True. True k*_mu at the illustration point = -1.5, versus 1.0 for the manuscript's expression. Among A3 draws, share with k*_mu < 0 = 1.0."},
 {"@id": "r-tce:chk:2", "tests": ["r-tce:fnd:2"], "expected": "Under uniform F, the sign of Phi_mu equals the sign of k*_mu wherever k* < 1. For at least one non-uniform F and one grid point, the two signs differ. I have not computed which cells differ; this part is asserted with low confidence."},
 {"@id": "r-tce:chk:3", "tests": ["r-tce:fnd:4", "r-tce:fnd:13", "r-tce:fnd:14", "r-tce:inc:6"], "expected": "Exactly one significance-marker mismatch (M3 Uncertainty, t ≈ 1.65). 412*11 = 4532, not 4712. 1-SD effect ≈ 0.027, ≈ 0.16 SD. Decline ≈ 0.69 > 2/3. M2 Peer 95% CI ≈ [-0.032, 0.116]. TOST fails at ±0.05 and ±0.0685 but succeeds at ±0.137. So the data can reject a peer effect as large as the Model 1 estimate, but cannot reject a peer effect half that size; r-tce:fnd:4 should be read with this in mind."},
 {"@id": "r-tce:chk:4", "tests": ["r-tce:fnd:7", "r-tce:inc:4"], "expected": "Scenario A (no true effect, confounding by capability): the modularity coefficient stays clearly non-zero, with most p < .05, after the staffing control. Survival of the coefficient therefore does not rule out confounding. Scenario B (true effect 0.1, no confounding): the coefficient with the staffing control departs from 0.1."}
]
```

### r-tce:chk:1. Re-derive Propositions 1 and 2 (sympy)

```python
import sympy as sp
import numpy as np

m, u, s, g0, g1, h0, h1 = sp.symbols('m u s g0 g1 h0 h1', positive=True)
G = g0 + g1*u
H = h0 + h1*u
kstar = (s + G) / (H * (1 - m))          # ms:TEST §2.3

# Proposition 1
k_m = sp.diff(kstar, m)
ms_k_m = (s + G) / (H * (1 - m)**2)       # ms:TEST Appendix
print("P1 equals manuscript expression:", sp.simplify(k_m - ms_k_m) == 0)

# Proposition 2
k_mu = sp.diff(kstar, m, u)
ms_k_mu = g1 / (H * (1 - m)**2)           # ms:TEST Appendix
print("P2 equals manuscript expression:", sp.simplify(k_mu - ms_k_mu) == 0)
scaled = sp.simplify(k_mu * H**2 * (1 - m)**2)
print("k*_mu * H^2 (1-m)^2 =", sp.expand(scaled))
print("Scaled numerator equals g1*h0 - h1*(s+g0):", sp.simplify(scaled - (g1*h0 - h1*(s + g0))) == 0)
print("Identity k*_mu == k*_u/(1-m):", sp.simplify(k_mu - sp.diff(kstar, u)/(1 - m)) == 0)
# A3: h1/h0 > g1/(s+g0)  <=>  g1*h0 - h1*(s+g0) < 0  <=>  k*_mu < 0

vals = {s: 1.0, g0: 1.0, g1: 0.5, h0: 1.0, h1: 1.0, m: 0.5, u: 1.0}
print("A3 holds at illustration point:", vals[h1]/vals[h0] > vals[g1]/(vals[s] + vals[g0]))
print("true k*_mu:", float(k_mu.subs(vals)), " manuscript k*_mu:", float(ms_k_mu.subs(vals)))

rng = np.random.default_rng(0)
f = sp.lambdify((m, u, s, g0, g1, h0, h1), k_mu, 'numpy')
D = rng.uniform(0.01, 3, size=(100000, 7))
D[:, 0] = rng.uniform(0, 0.99, 100000)    # m in [0,1)
a3 = D[:, 6]/D[:, 5] > D[:, 4]/(D[:, 2] + D[:, 3])
v = f(*D.T)
print("A3 draws:", int(a3.sum()), " share with k*_mu < 0:", float(np.mean(v[a3] < 0)))
print("non-A3 draws: share with k*_mu > 0:", float(np.mean(v[~a3] > 0)))
```

### r-tce:chk:2. Sign of the interaction on the share scale (numpy, scipy)

```python
import numpy as np
from scipy import stats

def kstar(m, u, s, g0, g1, h0, h1):
    return (s + g0 + g1*u) / ((h0 + h1*u) * (1 - m))

def kmu(m, u, s, g0, g1, h0, h1):        # closed form from r-tce:chk:1
    H = h0 + h1*u
    return (g1*h0 - h1*(s + g0)) / (H**2 * (1 - m)**2)

def Phi(m, u, F, p):
    return F.cdf(np.clip(kstar(m, u, **p), 0.0, 1.0))

def cross(m, u, F, p, e=1e-3):
    f = lambda a, b: Phi(a, b, F, p)
    return (f(m+e, u+e) - f(m+e, u-e) - f(m-e, u+e) + f(m-e, u-e)) / (4*e*e)

params = {"A3 holds":    dict(s=0.2, g0=0.2, g1=0.05, h0=1.0, h1=0.5),
          "A3 violated": dict(s=0.2, g0=0.2, g1=0.30, h0=1.0, h1=0.05)}
dists = {"uniform": stats.beta(1, 1), "Beta(2,5)": stats.beta(2, 5), "Beta(5,2)": stats.beta(5, 2)}
grid = [(mm, uu) for mm in (0.1, 0.3, 0.5) for uu in (0.2, 0.5, 1.0)]
for pn, p in params.items():
    ksign = ["+" if kmu(mm, uu, **p) > 0 else "-" for mm, uu in grid]
    for dn, F in dists.items():
        psign = ["sat" if kstar(mm, uu, **p) >= 1 else ("+" if cross(mm, uu, F, p) > 0 else "-") for mm, uu in grid]
        diff = sum(a != b for a, b in zip(ksign, psign) if b != "sat")
        print(f"{pn:12s} {dn:10s} k*_mu: {ksign}  Phi_mu: {psign}  sign differences: {diff}")
```

### r-tce:chk:3. Numerical consistency of §3.1, §4 and Table 2 (numpy, scipy)

```python
import numpy as np
from scipy import stats

table = {  # row: (coef, se, reported stars)
 "M1 Peer": (0.137, 0.031, "***"), "M2 Peer": (0.042, 0.038, ""), "M3 Peer": (0.039, 0.037, ""), "M4 Peer": (0.036, 0.036, ""),
 "M2 Modularity": (0.112, 0.024, "***"), "M3 Modularity": (0.118, 0.025, "***"), "M4 Modularity": (0.097, 0.023, "***"),
 "M3 Uncertainty": (0.084, 0.051, "***"), "M4 Uncertainty": (0.079, 0.050, ""),
 "M3 MxU": (-0.061, 0.019, "**"), "M4 MxU": (-0.058, 0.019, "**"),
 "M1 Specificity": (-0.094, 0.027, "***"), "M2 Specificity": (-0.091, 0.027, "***"),
 "M3 Specificity": (-0.090, 0.026, "***"), "M4 Specificity": (-0.088, 0.026, "***"),
 "M4 Staffing": (-0.143, 0.029, "***"),
}
df = 412 - 1   # hospital clusters - 1
def stars(p): return "***" if p < 0.001 else "**" if p < 0.01 else "*" if p < 0.05 else ""
for k, (b, se, rep) in table.items():
    t = b / se
    p = 2 * stats.t.sf(abs(t), df)
    print(f"{k:16s} t={t:6.2f} p={p:.4f} implied='{stars(p)}' reported='{rep}' {'OK' if stars(p) == rep else 'MISMATCH'}")

print("N, balanced 2009-2019 (11 waves):", 412*11, "| reported 4712 | implied waves:", round(4712/412, 3))
print("N if 2009 is lost to the t-1 peer lag:", 412*10)
print("1-SD effect of m (Model 2):", 0.112*0.24, "| in SDs of Phi:", 0.112*0.24/0.17)
print("Peer decline M1->M2:", (0.137-0.042)/0.137, "| > 2/3:", (0.137-0.042)/0.137 > 2/3)
b, se = 0.042, 0.038
z = stats.norm.ppf(0.975)
print("M2 Peer 95% CI:", (b - z*se, b + z*se))
for sesoi in (0.05, 0.137/2, 0.137):
    p_tost = max(stats.norm.sf((b + sesoi)/se), stats.norm.cdf((b - sesoi)/se))
    print(f"TOST vs +/-{sesoi:.4f}: p = {p_tost:.4f} (equivalence at 5% iff p < 0.05)")
print("Naive z for change 0.137 -> 0.042 (ignores covariance):", (0.137-0.042)/np.sqrt(0.031**2 + 0.038**2))
```

### r-tce:chk:4. Bad-control simulation for Model 4 (numpy, statsmodels)

```python
import numpy as np
import statsmodels.api as sm

rng = np.random.default_rng(1)
N, T = 412, 11
ids = np.repeat(np.arange(N), T)

def within(x):   # two-way demeaning, balanced panel ordered by hospital then year
    X = x.reshape(N, T)
    return (X - X.mean(1, keepdims=True) - X.mean(0, keepdims=True) + X.mean()).ravel()

def fe(y, *xs):
    X = np.column_stack([within(x) for x in xs])
    return sm.OLS(within(y), X).fit(cov_type="cluster", cov_kwds={"groups": ids})

def simulate(beta, conf, reps=200):
    out = []
    for _ in range(reps):
        a = rng.normal(size=N).repeat(T)
        tau = np.tile(np.linspace(0, 1, T), N)
        c = a + rng.normal(size=N*T)                       # time-varying capability
        m = 0.5*c + rng.normal(size=N*T)                   # capability raises modularity
        phi = beta*m + conf*c + a + tau + rng.normal(size=N*T)
        staff = -0.8*phi + 0.5*c + rng.normal(size=N*T)    # outsourcing cuts in-house staff (ms §3.2)
        r_without, r_with = fe(phi, m), fe(phi, m, staff)
        out.append((r_without.params[0], r_without.pvalues[0], r_with.params[0], r_with.pvalues[0]))
    o = np.array(out)
    print(f"true beta={beta}, confounding={conf}: b without staffing={o[:,0].mean():.3f} (share p<.05: {np.mean(o[:,1] < .05):.2f}); "
          f"b with staffing={o[:,2].mean():.3f} (share p<.05: {np.mean(o[:,3] < .05):.2f})")

simulate(beta=0.0, conf=0.3)   # A: confounding by capability, no true effect
simulate(beta=0.1, conf=0.0)   # B: true effect, no confounding
```

## Decisions for the reviewer

1. **Prop. 2 (r-tce:fnd:1).** Have the harness run r-tce:chk:1. If the result is `demonstrated`, decide whether to raise this as the lead point. It is damaging to the paper as written, but its repair brings model and data into agreement and makes the legitimacy account (r-tce:fnd:3) unnecessary.
2. **"Rule out mimetic isomorphism" (r-tce:fnd:4, r-tce:fnd:5).** This simulation rejects MI7. Decide whether your own perspective does too. Also weigh the nuance in r-tce:chk:3: the data appear able to reject a peer effect as large as the Model 1 estimate, but not one half that size.
3. **Causal reading (r-tce:fnd:6, r-tce:fnd:7, r-tce:fnd:8).** Decide whether to demand function-level evidence, a 2SLS estimate using the mandates and timing tests, or to accept a narrowed, associational claim.
4. **Mechanism (r-tce:fnd:9).** r-tce:inc:5 rests on my reading of the specificity measure as effective specificity. Decide whether you share that reading before raising it.
5. **Numerical inconsistencies (r-tce:fnd:13).** If r-tce:chk:3 confirms them, raise the N discrepancy and the Model 3 significance marker as fixable.
6. **Priority (r-tce:fnd:15).** The prior studies named there are marked "(to verify)". Verify them before citing any to the editor.
7. **Recommendation.** This simulation recommends major revision with no fatal finding. Decide whether you agree. Bear in mind that this perspective resembles yours and may share its sympathy for the economizing account (§8); a differing simulation would be the counterweight.
