# Run 06: Simulated Reviewer, Design-based empirical economist (`persp:R-DID`)

**SIMULATED REVIEWER OUTPUT. This is not a review and is never sent to authors.** It simulates a reviewer holding the perspective `persp:R-DID` (lens: *Design-based empirical economist*; relation to focal reviewer: *differing*). Instruction set: Reviewership v0.1 (23 October 2026). Manuscript: `ms:TEST`, "Modularity, Not Mimicry: Interoperability Standards and the Diffusion of IT Outsourcing in U.S. Hospitals".

Conventions. `ms:` ids refer to manuscript elements; `r-did:` ids are mine. Quotations from the manuscript are at most 25 words. "Says" marks what the manuscript states; "infer" marks what I attribute by an inference I name. Every formal, numerical or estimator-property claim is marked `asserted` and comes with a check in Section 3.6 (`r-did:chk:n`); no check has been run by the harness at the time of writing, so **no finding here is `demonstrated` or `refuted-by-check`**. Literature I am not certain of is marked "(to verify)".

Manuscript element ids used below: `ms:Abstract`, `ms:S1` (Introduction), `ms:S2.2`, `ms:A3` (Assumption A3), `ms:S2.3`, `ms:Prop1`, `ms:Prop2`, `ms:S2.4`, `ms:H1`, `ms:H2`, `ms:H3`, `ms:S3.1`, `ms:S3.2`, `ms:S3.3` (estimating equation), `ms:T2` (Table 2; cells as `ms:T2.M<model>.<row>`), `ms:S4.H1`, `ms:S4.H2`, `ms:S4.H3`, `ms:S4.Robust`, `ms:S4.EventStudy` (the event-study sentence in `ms:S4.Robust`), `ms:S5`, `ms:S5.1`, `ms:S5.2`, `ms:S6`, `ms:App.Prop1`, `ms:App.Prop2`.

---

## 1. Claimed contributions

```json
{
  "@type": "ClaimedContributions",
  "source": "ms:TEST",
  "scorekeeper": "persp:R-DID",
  "contributions": [
    {
      "@id": "r-did:ctb:1",
      "text": "\"we formalize the link between modularity and the make-or-buy decision in a simple transaction-cost model, deriving two propositions\"",
      "loci": ["ms:S1", "ms:S2.3", "ms:Prop1", "ms:Prop2", "ms:App.Prop1", "ms:App.Prop2"]
    },
    {
      "@id": "r-did:ctb:2",
      "text": "\"we test these propositions against an institutional rival using a decade-long panel of hospitals\"",
      "loci": ["ms:S1", "ms:S2.4", "ms:S3", "ms:T2"]
    },
    {
      "@id": "r-did:ctb:3",
      "text": "\"once modularity is measured, the apparent peer effects that have motivated institutional accounts disappear\"; \"The results rule out mimetic isomorphism as a driver of IT outsourcing in this setting\"",
      "loci": ["ms:S1", "ms:Abstract", "ms:S4.H3", "ms:S5", "ms:S6"]
    },
    {
      "@id": "r-did:ctb:4",
      "text": "\"a sourcing practice often read as institutional fashion is, on closer inspection, economizing\"; standards \"made IT functions modular, reduced the effective specificity ... and widened the range of functions\"",
      "loci": ["ms:Abstract", "ms:S5", "ms:S6"]
    },
    {
      "@id": "r-did:ctb:5",
      "text": "\"Specificity is not a fixed property of an activity; it is partly a product of interface design\" (contribution to transaction-cost theory)",
      "loci": ["ms:S5.1"]
    },
    {
      "@id": "r-did:ctb:6",
      "text": "\"To our knowledge, this is the first study to adjudicate directly between transaction-cost and institutional explanations of IT outsourcing.\"",
      "loci": ["ms:Abstract", "ms:S1"]
    },
    {
      "@id": "r-did:ctb:7",
      "text": "\"hospital leaders considering outsourcing should attend first to the modularity of their systems\" (implication for practice)",
      "loci": ["ms:S5.1"]
    }
  ]
}
```

Note on `r-did:ctb:4`. The manuscript lists three numbered contributions (`ms:S1`). I separate the causal claim of `ms:S5`/`ms:S6` (`r-did:ctb:4`) from the testing claim (`r-did:ctb:2`) because, from this perspective, they carry different entitlement burdens: an association can be evidenced by a fixed-effects regression; a causal effect needs a design.

---
## 2. Scoreboard (as attributed by `persp:R-DID`)

Material-inference settings that drive attribution: I endorse no catalogue entry and I **reject MI6** (within-unit variation with unit and period fixed effects identifies a causal effect) and **MI7** (non-significance after adding a control means no effect). Where the manuscript relies on MI6 or MI7, I attribute the reliance as a consequential commitment and then challenge it. My consequential attributions otherwise use deductive inference from the manuscript's own model (quotient rule on `k*`), which my perspective admits (INF.1).

### 2.1 Commitments

```json
{
  "@type": "Scoreboard",
  "@id": "r-did:scoreboard",
  "scorekeeper": "persp:R-DID",
  "manuscript": "ms:TEST",
  "commitments": [
    {"@id": "r-did:cmt:1", "kind": "avowed", "content": "Prop. 1: dk*/dm > 0", "locus": "ms:Prop1",
     "entitlement": "argued", "entitlementBasis": "ms:App.Prop1; correct as far as I can see, asserted pending r-did:chk:1"},
    {"@id": "r-did:cmt:2", "kind": "avowed", "content": "Prop. 2: d2k*/(dm du) > 0", "locus": "ms:Prop2",
     "entitlement": "unentitled", "entitlementBasis": "ms:App.Prop2 differentiates only the numerator's dependence on u and omits H(u) in the denominator; see r-did:inc:1, r-did:chk:1"},
    {"@id": "r-did:cmt:3", "kind": "avowed", "content": "Assumption A3: h1/h0 > g1/(s+g0)", "locus": "ms:A3",
     "entitlement": "deferred", "entitlementBasis": "Williamson (1991), ms:S2.2"},
    {"@id": "r-did:cmt:4", "kind": "consequential", "content": "Under A3, d2k*/(dm du) < 0 for all admissible (m,u): the model predicts that uncertainty WEAKENS the modularity effect on the threshold",
     "inference": "deduction from ms:S2.2 cost functions, ms:S2.3 threshold, and ms:A3 (numerator of the cross-partial is g1*h0 - h1*(s+g0))",
     "entitlement": "argued", "entitlementBasis": "scorekeeper's derivation, asserted pending r-did:chk:1"},
    {"@id": "r-did:cmt:5", "kind": "consequential", "content": "Under A3, dk*/du < 0: uncertainty lowers the outsourcing threshold, so the model's main effect of u on outsourcing is negative wherever k* is interior",
     "inference": "same derivation as r-did:cmt:4",
     "entitlement": "argued", "entitlementBasis": "asserted pending r-did:chk:1"},
    {"@id": "r-did:cmt:6", "kind": "avowed", "content": "Prop. 1 implies H1 and Prop. 2 implies H2 on the scale of Phi, the spending-weighted outsourced share", "locus": "ms:S2.4",
     "entitlement": "challenged", "entitlementBasis": "the move from a threshold k* to Phi = F(k*) needs k* interior to [0,1] and assumptions on the spending-weighted distribution of k; the cross-partial on the Phi scale carries an extra term f'(k*) k*_m k*_u (r-did:chk:5)"},
    {"@id": "r-did:cmt:7", "kind": "avowed", "content": "Modularity is positively associated with the outsourcing share, conditional on hospital and year fixed effects and controls (H1 supported)", "locus": "ms:S4.H1; ms:T2.M2-M4.Modularity",
     "entitlement": "evidenced", "entitlementBasis": "ms:T2 (0.112, SE 0.024 in Model 2); as an association only"},
    {"@id": "r-did:cmt:8", "kind": "avowed", "content": "Interoperability standards CAUSED modularity, which CAUSED the rise in outsourcing", "locus": "ms:S5 \"Interoperability standards made IT functions modular, reduced the effective specificity\"; ms:S6",
     "entitlement": "unentitled", "entitlementBasis": "no design-based identification; see r-did:cmt:9, r-did:cmt:14, r-did:fnd:1"},
    {"@id": "r-did:cmt:9", "kind": "consequential", "content": "Within-hospital changes in modularity are as good as random conditional on hospital FE, year FE and controls",
     "inference": "MI6 (used by the authors: \"Identification therefore comes from within-hospital changes in modularity over time\", ms:S3.3); MI6 is rejected by this perspective",
     "entitlement": "challenged", "entitlementBasis": "time-varying confounding and reverse causality not addressed; r-did:chl:1"},
    {"@id": "r-did:cmt:10", "kind": "avowed", "content": "The Model 1 peer association reflects common state-level diffusion of standards, not imitation", "locus": "ms:S4.H3 \"the apparent peer effect reflects the common diffusion of standards across hospitals in the same state, not imitation\"",
     "entitlement": "unentitled", "entitlementBasis": "no test separates correlated effects from endogenous peer effects; r-did:chl:4"},
    {"@id": "r-did:cmt:11", "kind": "avowed", "content": "The results rule out mimetic isomorphism as a driver of outsourcing in this setting", "locus": "ms:Abstract; ms:S5",
     "entitlement": "unentitled", "entitlementBasis": "rests on MI7 (rejected); no interval or equivalence test; modularity may mediate imitation (r-did:fnd:2, r-did:chk:4, r-did:chk:6)"},
    {"@id": "r-did:cmt:12", "kind": "avowed", "content": "Because the modularity coefficient survives the in-house IT staffing control, it cannot be attributed to capability differences", "locus": "ms:S3.3; ms:S4.Robust",
     "entitlement": "unentitled", "entitlementBasis": "staffing is downstream of the outcome by the authors' own account (r-did:cmt:13); r-did:inc:2"},
    {"@id": "r-did:cmt:13", "kind": "avowed", "content": "Outsourcing a function moves its staff to the vendor or eliminates the positions", "locus": "ms:S3.2 \"outsourcing a function transfers its staff to the vendor or eliminates the positions\"",
     "entitlement": "default"},
    {"@id": "r-did:cmt:14", "kind": "avowed", "content": "A TWFE event study on staggered state requirements for certified interfaces (2011-2016) shows flat leads and rising outsourcing, \"consistent with a causal effect of modularity\"", "locus": "ms:S4.EventStudy",
     "entitlement": "challenged", "entitlementBasis": "results not reported; TWFE under staggered adoption; reduced form with no first stage on modularity; exclusion restriction unargued; clustering level (r-did:fnd:4)"},
    {"@id": "r-did:cmt:15", "kind": "avowed", "content": "Balanced panel of 412 hospitals observed annually 2009-2019, yielding 4,712 hospital-years; all four models use 4,712 observations", "locus": "ms:S3.1; ms:T2.Observations",
     "entitlement": "challenged", "entitlementBasis": "412 x 11 = 4,532, not 4,712; a t-1 peer measure also needs 2008 data or costs a year (r-did:inc:3, r-did:chk:3)"},
    {"@id": "r-did:cmt:16", "kind": "avowed", "content": "Environmental uncertainty main effect in Model 3 is 0.084 (SE 0.051), p < 0.001", "locus": "ms:T2.M3.uncertainty",
     "entitlement": "challenged", "entitlementBasis": "t = 0.084/0.051 = 1.65, two-sided p about 0.10 (r-did:inc:4, r-did:chk:2)"},
    {"@id": "r-did:cmt:17", "kind": "avowed", "content": "The negative modularity x uncertainty interaction reflects legitimacy pressures to retain visible in-house IT under high uncertainty, and this is \"consistent with our theory\"", "locus": "ms:S5 para. 2",
     "entitlement": "unentitled", "entitlementBasis": "post hoc, untested, outside the model by the authors' own statement (\"a feature of the hospital setting that our model abstracts from\"); r-did:inc:5, r-did:inc:6"},
    {"@id": "r-did:cmt:18", "kind": "avowed", "content": "H3 as stated: outsourcing share is positively associated with prior peer outsourcing", "locus": "ms:H3",
     "entitlement": "evidenced", "entitlementBasis": "ms:T2.M1.Peer 0.137 (0.031): H3 as stated is supported, yet ms:S4.H3 reports \"H3 is not supported\" (r-did:inc:7)"},
    {"@id": "r-did:cmt:19", "kind": "avowed", "content": "Same-state mean outsourcing of other sample hospitals at t-1 captures the field to which mimetic isomorphism directs attention", "locus": "ms:S3.2 Peer outsourcing",
     "entitlement": "challenged", "entitlementBasis": "about 8 sample hospitals per state on average if all states are represented (412/50; inferred, not reported); referents in the institutional account are perceived-successful or legitimate peers, not a state mean"},
    {"@id": "r-did:cmt:20", "kind": "avowed", "content": "Standard errors clustered by hospital are appropriate for all coefficients", "locus": "ms:S3.3",
     "entitlement": "challenged", "entitlementBasis": "peer outsourcing varies at state-year level and the event-study treatment at state level; clustering should be at least at state level (r-did:fnd:11)"},
    {"@id": "r-did:cmt:21", "kind": "consequential", "content": "If the CIO's transfer-cost rating measures effective specificity k(1-m), the asset-specificity control is a mediator of modularity",
     "inference": "from ms:S2.2 (effective specificity is k(1-m)) and ms:S3.2 (rating of cost of transferring IT functions to a different provider)",
     "entitlement": "challenged", "entitlementBasis": "the manuscript does not say whether the rating targets nominal k or effective k(1-m)"},
    {"@id": "r-did:cmt:22", "kind": "avowed", "content": "A one-SD increase in modularity is associated with +2.7 pp in the outsourcing share, about one-sixth of an SD; modularity \"strongly predicts\" outsourcing", "locus": "ms:S4.H1; ms:Abstract",
     "entitlement": "evidenced", "entitlementBasis": "arithmetic consistent with ms:T2.M2 and ms:S3.2 (asserted pending r-did:chk:4); \"strongly\" is a characterization of a 0.16 SD effect"},
    {"@id": "r-did:cmt:23", "kind": "avowed", "content": "First study to adjudicate directly between transaction-cost and institutional explanations of IT outsourcing", "locus": "ms:Abstract; ms:S1",
     "entitlement": "challenged", "entitlementBasis": "priority not checked against earlier IS-outsourcing work (r-did:fnd:18)"},
    {"@id": "r-did:cmt:24", "kind": "avowed", "content": "Hospital leaders should attend first to modularity when considering outsourcing", "locus": "ms:S5.1",
     "entitlement": "unentitled", "entitlementBasis": "a policy implication presupposes the causal claim r-did:cmt:8"},
    {"@id": "r-did:cmt:25", "kind": "consequential", "content": "The data and code that produce Table 2 and the event study can be made available for re-running",
     "inference": "required by TEC.1 for this perspective; the manuscript is silent",
     "entitlement": "challenged", "entitlementBasis": "no data or code availability statement; the Hospital IT Sourcing Survey's access terms are not stated"},
    {"@id": "r-did:cmt:26", "kind": "avowed", "content": "If outsourcing reflects economizing, the peer association disappears once modularity is controlled; if mimicry, peer outsourcing predicts over and above modularity", "locus": "ms:S2.4 last paragraph",
     "entitlement": "challenged", "entitlementBasis": "not a discriminating prediction: if hospitals imitate peers in adopting certified interfaces, modularity mediates imitation and the peer coefficient also vanishes (r-did:chk:6, scenario B)"}
  ]
}
```

### 2.2 Incompatibilities and challenges

```json
{
  "@type": "Scoreboard",
  "@id": "r-did:scoreboard",
  "incompatibilities": [
    {"@id": "r-did:inc:1", "between": ["r-did:cmt:2", "r-did:cmt:4"],
     "reason": "Prop. 2 asserts a positive cross-partial; the model's own cost functions plus A3 give a cross-partial whose sign is that of g1*h0 - h1*(s+g0), which A3 makes negative. The authors cannot hold both A3 and Prop. 2. The appendix proof drops the term -(s+G)H'(u) by treating H as constant in u.",
     "status": "asserted", "checks": ["r-did:chk:1"]},
    {"@id": "r-did:inc:2", "between": ["r-did:cmt:12", "r-did:cmt:13"],
     "reason": "Staffing cannot serve as a pre-determined proxy that rules out capability confounding while also being mechanically reduced by the outcome. Conditioning on a descendant of the outcome biases the modularity coefficient in an unknown direction, so its 'survival' is uninformative about confounding.",
     "status": "asserted", "checks": ["r-did:chk:6"]},
    {"@id": "r-did:inc:3", "between": ["r-did:cmt:15", "ms:T2.Observations"],
     "reason": "A balanced panel of 412 hospitals over 11 years (2009-2019 inclusive) has 4,532 observations, not 4,712 (4,712/412 = 11.44). If peer outsourcing at t-1 requires a 2008 survey wave that is not described, 2009 drops and N should be 4,120.",
     "status": "asserted", "checks": ["r-did:chk:3"]},
    {"@id": "r-did:inc:4", "between": ["ms:T2.M3.uncertainty (coefficient and SE)", "ms:T2.M3.uncertainty (*** marker)"],
     "reason": "0.084/0.051 gives |t| = 1.65, two-sided p about 0.10, which does not meet p < 0.05, let alone p < 0.001. Model 4's 0.079 (0.050) is correctly unstarred.",
     "status": "asserted", "checks": ["r-did:chk:2"]},
    {"@id": "r-did:inc:5", "between": ["r-did:cmt:17", "r-did:cmt:11"],
     "reason": "ms:S5 invokes institutional legitimacy pressure as a force that offsets economizing in sourcing decisions; ms:S6 says the outward form is institutional and \"Its substance is economizing\", and the abstract rules out mimicry. A legitimacy mechanism is not mimicry, so this is not a strict contradiction with 'rule out mimetic isomorphism', but it is incompatible with the stronger closing claim that the substance is economizing."},
    {"@id": "r-did:inc:6", "between": ["r-did:cmt:17 ('consistent with our theory')", "r-did:cmt:17 ('a feature ... that our model abstracts from')", "r-did:cmt:2"],
     "reason": "The legitimacy story is presented both as outside the model and as consistent with the theory, while the theory as stated (Prop. 2) predicts the opposite sign. Once r-did:inc:1 is repaired the model itself predicts the negative sign and the legitimacy story is redundant."},
    {"@id": "r-did:inc:7", "between": ["r-did:cmt:18", "ms:S4.H3 'H3 is not supported'"],
     "reason": "H3 is stated as an unconditional positive association, which Model 1 supports. The verdict 'not supported' tests a different, conditional proposition (r-did:cmt:26)."}
  ],
  "challenges": [
    {"@id": "r-did:chl:1", "attachedTo": "r-did:cmt:9",
     "request": "What design rules out (i) reverse causality, i.e. vendors installing certified interfaces when they take over a function, and (ii) hospital-specific, time-varying shocks such as the timing of each hospital's certified-EHR adoption under the 2009 federal incentive programme, which year FE absorb only as a national average?"},
    {"@id": "r-did:chl:2", "attachedTo": "r-did:cmt:14",
     "request": "Report the event study in full: cohorts, never-treated or not-yet-treated controls, each lead and lag with intervals, a pre-trend test with its power, a first stage of state requirements on modularity, and estimates from a heterogeneity-robust estimator (Callaway & Sant'Anna 2021; de Chaisemartin & D'Haultfoeuille 2020)."},
    {"@id": "r-did:chl:3", "attachedTo": "r-did:cmt:11",
     "request": "Give the 95% interval of the Model 2 peer coefficient, and an equivalence test against a stated smallest effect of interest. Which peer effects does the evidence actually exclude?"},
    {"@id": "r-did:chl:4", "attachedTo": "r-did:cmt:10",
     "request": "Separate correlated effects (state-level standards diffusion, state mandates) from endogenous peer effects: add state-by-year fixed effects, define peers by a network that does not coincide with state, or use exogenous shocks to peers."},
    {"@id": "r-did:chl:5", "attachedTo": "r-did:cmt:6",
     "request": "Derive H1 and H2 on the Phi scale on which they are tested, stating the assumptions on the spending-weighted distribution of k and on k* being interior to [0,1]."},
    {"@id": "r-did:chl:6", "attachedTo": "r-did:cmt:5",
     "request": "The corrected model implies a negative main effect of uncertainty on outsourcing; Table 2 reports a positive (imprecise) one. Reconcile, noting that with uncentred m, beta_2 in Models 3-4 is the effect of u at m = 0."},
    {"@id": "r-did:chl:7", "attachedTo": "r-did:cmt:21",
     "request": "Does the transfer-cost rating measure nominal specificity k or effective specificity k(1-m)? Report Models 2-4 with and without it."},
    {"@id": "r-did:chl:8", "attachedTo": "r-did:cmt:15",
     "request": "Reconcile N with the balanced-panel description; report survey response rates and how the all-years-responder restriction relates to outsourcing."},
    {"@id": "r-did:chl:9", "attachedTo": "r-did:cmt:25",
     "request": "Provide a replication package (code for all tables and the event study, and data or a documented access route)."},
    {"@id": "r-did:chl:10", "attachedTo": "r-did:cmt:23",
     "request": "Position the priority claim against earlier work testing economic versus institutional or imitation accounts of IS outsourcing (r-did:fnd:18)."}
  ]
}
```

---
## 3. Assessment by dimension

Order follows my weights: EPI (1.0) and TEC (1.0), then INF (0.6), then ONT (0.3) and PRA (0.3). Ties are listed in the schema's order.

### 3.1 EPI, Epistemological (weight 1.0)

The manuscript's empirical core is a two-way fixed-effects regression of a CIO-reported outsourcing share on a CIO-reported modularity share (`ms:S3.3`). From a design-based standpoint (EPI.3), this licenses a conditional association, not a causal effect. The paper's own words move from "strongly predicts" (`ms:Abstract`) to "Interoperability standards made IT functions modular ... and widened the range" (`ms:S5`) without a design that carries the weight.

```json
[
  {"@id": "r-did:fnd:1", "dimension": "EPI", "parameter": "EPI.3", "severity": "fatal",
   "commitment": ["r-did:cmt:8", "r-did:cmt:9"],
   "problem": "The causal claim (the title's 'Modularity') rests on MI6, which this perspective rejects. Two first-order threats are unaddressed. (a) Reverse causality: an outsourcing vendor plausibly migrates a hospital's systems onto certified interfaces when it takes a function over, so Phi can cause m within hospital. (b) Hospital-specific timing of certified-EHR adoption under the 2009 incentive programme (named in ms:S3.3 as absorbed by year FE) varies across hospitals and plausibly drives both m and vendor contracting; year FE remove only its national average. The single design-based element (ms:S4.EventStudy) cannot carry the claim as reported (r-did:fnd:4).",
   "missingEntitlement": "No research design that makes within-hospital changes in m as good as random.",
   "repair": "Make the staggered state requirements the design: report the first stage (requirement on m), the reduced form (requirement on Phi) with a heterogeneity-robust staggered estimator, and the Wald-DiD/IV ratio as the modularity effect; argue the exclusion restriction (requirements affect outsourcing only through modularity); cluster by state. Add a timing test: leads and lags of outsourcing-contract start on m. Add a function-level placebo: modularity of clinical interfaces should not move outsourcing of functions that do not run through clinical interfaces (e.g. help desk). Until then, replace causal language with associational language.",
   "status": "asserted", "checks": []},

  {"@id": "r-did:fnd:2", "dimension": "EPI", "parameter": "EPI.5; INF.2 (MI7 rejected)", "severity": "fatal",
   "commitment": ["r-did:cmt:11", "r-did:cmt:10", "r-did:cmt:26"],
   "problem": "'Rule out mimetic isomorphism' (ms:Abstract, ms:S5) is inferred from a coefficient that loses significance when modularity is added (ms:T2.M2.Peer 0.042, SE 0.038). This is MI7. (i) The 95% interval is about [-0.03, 0.12]; it excludes little, and an equivalence test at conventional bounds cannot be passed (r-did:chk:4). (ii) If hospitals imitate peers in adopting certified interfaces, modularity is a mediator of imitation and conditioning on it removes the peer coefficient even when imitation drives everything (r-did:chk:6, scenario B; Cinelli, Forney & Pearl 2024 on bad controls). (iii) A same-state peer mean with hospital and year FE is exposed to the reflection problem and to state-level correlated shocks, which the authors themselves invoke (r-did:cmt:10); Manski (1993) (to verify). (iv) Hospital clustering understates the uncertainty of a state-year regressor (r-did:fnd:11), so even Model 1's peer significance is overstated.",
   "missingEntitlement": "An inference from 'not significant after a control' to 'no effect', and a design that separates endogenous peer effects from correlated effects and from mediation through modularity.",
   "repair": "Withdraw 'rule out'. Report the interval and a TOST equivalence test against a stated smallest effect of interest; report the change in the peer coefficient with its own standard error. Add state-by-year FE (which absorb the state peer mean; the remaining test is then of network peers). Define peers by networks that cross state lines (system, referral, shared vendor) or use exogenous shocks to peers. State explicitly that controlling for m blocks imitation that runs through standards adoption. The defensible claim is narrower: 'conditional on modularity, the same-state peer association is smaller and imprecisely estimated'.",
   "status": "asserted", "checks": ["r-did:chk:4", "r-did:chk:6"]},

  {"@id": "r-did:fnd:15", "dimension": "EPI", "parameter": "EPI.3; EPI.5", "severity": "fixable",
   "commitment": ["r-did:cmt:15"],
   "problem": "The sample keeps only hospitals that responded in every year (ms:S3.1). Continuous response may correlate with sourcing (for example, CIO turnover or survey burden after outsourcing), so the estimand is defined on a selected population; ms:S5.2 notes over-representation of larger hospitals but not selection on the outcome.",
   "missingEntitlement": "Evidence that panel retention is unrelated to Phi or m.",
   "repair": "Report response rates by year; estimate on the unbalanced panel; model retention on lagged Phi and m; report bounds under selective attrition (e.g. Lee bounds, to verify).",
   "status": "asserted", "checks": ["r-did:chk:3"]},

  {"@id": "r-did:fnd:14", "dimension": "EPI", "parameter": "EPI.5", "severity": "minor",
   "commitment": ["r-did:cmt:22"],
   "problem": "The effect-size arithmetic appears right (0.112 x 0.24 = 0.027; 0.027/0.17 = 0.16 SD), but 'strongly predicts' (ms:Abstract) overstates a one-sixth-SD association, and Model 2 adds 0.05 to within R2. Results are reported with stars, not intervals.",
   "missingEntitlement": "None for the arithmetic; the characterization lacks an anchor.",
   "repair": "Report 95% intervals for all coefficients and describe magnitudes, not significance; drop 'strongly'.",
   "status": "asserted", "checks": ["r-did:chk:4"]},

  {"@id": "r-did:fnd:20", "dimension": "EPI", "parameter": "EPI.6", "severity": "minor",
   "commitment": ["r-did:cmt:7"],
   "problem": "Single-informant measurement is acceptable under this perspective. The residual concern is correlated reporting error: the same CIO reports m (and, as far as the text says, the sourcing data), and reporting styles can change within hospital when the CIO changes.",
   "missingEntitlement": "None required by EPI.6; a robustness check would help.",
   "repair": "Control for CIO turnover, or show that results hold when modularity is taken from certification records rather than self-report, if such records exist.",
   "status": "asserted", "checks": []}
]
```

No pre-registration is reported (EPI.5). I do not count that as a finding on its own, but it bears on `r-did:fnd:9`: H2 failed, and the explanation offered was constructed after the result.

### 3.2 TEC, Technical (weight 1.0)

```json
[
  {"@id": "r-did:fnd:4", "dimension": "TEC", "parameter": "TEC.3", "severity": "damaging",
   "commitment": ["r-did:cmt:14"],
   "problem": "The event study (ms:S4.EventStudy) is estimated 'by two-way fixed effects with leads and lags' under staggered adoption (2011-2016). With heterogeneous or dynamic effects, TWFE uses already-treated units as controls and its event-time coefficients mix effects across cohorts and periods, so leads can look flat or not for reasons unrelated to pre-trends (Goodman-Bacon 2021; de Chaisemartin & D'Haultfoeuille 2020; Callaway & Sant'Anna 2021; Sun & Abraham 2021, to verify). No coefficients, intervals, cohort sizes or control group are reported. It is a reduced form of state requirements on outsourcing, which is evidence about 'a causal effect of modularity' only with a first stage and an exclusion restriction, and certified-interface requirements could change vendor markets directly. Treatment varies by state but SEs are clustered by hospital.",
   "missingEntitlement": "A reported, heterogeneity-robust event study with a first stage and a defended exclusion restriction.",
   "repair": "Re-estimate with Callaway & Sant'Anna (2021) or de Chaisemartin & D'Haultfoeuille (2020) using never-treated or not-yet-treated states; report all leads and lags with intervals, a pre-trend test with power or a sensitivity analysis for pre-trend violations (Rambachan & Roth 2023, to verify); report the first stage; cluster by state with a wild-cluster bootstrap if states are few.",
   "status": "asserted", "checks": ["r-did:chk:7"]},

  {"@id": "r-did:fnd:3", "dimension": "TEC", "parameter": "TEC.3", "severity": "fixable",
   "commitment": ["r-did:cmt:12", "r-did:cmt:13"],
   "problem": "Model 4 controls for in-house IT staffing, which the authors say outsourcing mechanically reduces (ms:S3.2). It is a descendant of the outcome, a bad control. The coefficient's 'survival' (0.118 to 0.097) neither shows nor rules out capability confounding (r-did:inc:2). The claim that the effect 'cannot be attributed to differences in internal IT capability' (ms:S4.Robust) is unentitled.",
   "missingEntitlement": "A pre-determined measure of capability.",
   "repair": "Drop Model 4 as evidence on confounding. Use pre-period (e.g. 2009) staffing interacted with year dummies, or lagged staffing measured before modularity changes, and show sensitivity to an unobserved confounder (e.g. Cinelli & Hazlett 2020 robustness values, to verify).",
   "status": "asserted", "checks": ["r-did:chk:6"]},

  {"@id": "r-did:fnd:5", "dimension": "TEC", "parameter": "TEC.4", "severity": "fixable",
   "commitment": ["r-did:cmt:15"],
   "problem": "412 hospitals x 11 years = 4,532, not the 4,712 reported in ms:S3.1 and in every column of ms:T2. If the t-1 peer measure needs a 2008 wave, the usable N would be 4,120. Either the panel is not balanced as described, the year range is misstated, or N is misreported. I grade this fixable, but it is damaging if it reveals an unbalanced or differently defined sample.",
   "missingEntitlement": "Internally consistent sample counts.",
   "repair": "Reconcile N with the sample definition and the lag structure; report the number of years per hospital.",
   "status": "asserted", "checks": ["r-did:chk:3"]},

  {"@id": "r-did:fnd:11", "dimension": "TEC", "parameter": "TEC.3", "severity": "fixable",
   "commitment": ["r-did:cmt:20"],
   "problem": "Peer outsourcing is a state-year variable and the event-study treatment is assigned by state, yet SEs are clustered by hospital (ms:S3.3). Hospital clustering ignores within-state-year correlation and likely understates SEs for these coefficients, including Model 1's peer coefficient on which the H3 narrative partly rests.",
   "missingEntitlement": "Inference at the level of treatment assignment.",
   "repair": "Cluster by state (two-way state and hospital if needed); use a wild-cluster bootstrap if fewer than about 40 states are represented; report the number of states and hospitals per state.",
   "status": "asserted", "checks": []},

  {"@id": "r-did:fnd:12", "dimension": "TEC", "parameter": "TEC.3", "severity": "fixable",
   "commitment": ["r-did:cmt:21"],
   "problem": "The asset-specificity control is the CIO's rating of the cost of transferring IT functions to another provider (ms:S3.2). If it captures effective specificity k(1-m), the mechanism the model posits (ms:S2.2), then it is a mediator of modularity and conditioning on it biases the modularity coefficient toward the direct effect net of the mechanism.",
   "missingEntitlement": "A statement that the rating measures nominal, pre-modularity specificity.",
   "repair": "Clarify what the rating measures; report Models 2-4 without it; if it is effective specificity, use it as an outcome in a mechanism test (m should reduce it).",
   "status": "asserted", "checks": []},

  {"@id": "r-did:fnd:6", "dimension": "TEC", "parameter": "TEC.4", "severity": "minor",
   "commitment": ["r-did:cmt:16"],
   "problem": "ms:T2.M3.uncertainty reports 0.084 (0.051) with ***; |t| = 1.65, p about 0.10. All other stars in Table 2 appear consistent with their coefficient/SE ratios (r-did:chk:2 covers every cell).",
   "missingEntitlement": "Consistency between estimate, SE and significance marker.",
   "repair": "Correct the marker or the SE; report intervals instead of stars.",
   "status": "asserted", "checks": ["r-did:chk:2"]},

  {"@id": "r-did:fnd:13", "dimension": "TEC", "parameter": "TEC.1", "severity": "fixable",
   "commitment": ["r-did:cmt:25"],
   "problem": "No data or code availability statement. Under TEC.1 (required) and TEC.2 (re-run), I cannot re-run Table 2 or the event study. The survey's access terms are not given.",
   "missingEntitlement": "A replication package.",
   "repair": "Deposit code for all tables and the event study; deposit the data or document an access route and provide synthetic data that reproduces the pipeline.",
   "status": "asserted", "checks": []}
]
```

---
### 3.3 INF, Inferential (weight 0.6)

Derivation standard is proof (INF.3); enthymeme tolerance is low (INF.4).

```json
[
  {"@id": "r-did:fnd:7", "dimension": "INF", "parameter": "INF.3", "severity": "damaging",
   "commitment": ["r-did:cmt:2", "r-did:cmt:3", "r-did:cmt:4"],
   "problem": "The proof of Prop. 2 (ms:App.Prop2) says 'the cross-partial is determined by how the numerator responds to uncertainty'. But H(u) = h0 + h1 u sits in the denominator of k*, so differentiating dk*/dm = (s+G)/(H(1-m)^2) in u gives [G'H - (s+G)H'] / (H^2 (1-m)^2) = [g1 h0 - h1 (s+g0)] / (H^2 (1-m)^2). Assumption A3 is exactly the condition that makes this numerator negative. So, by my derivation, the model with A3 predicts a NEGATIVE interaction, the sign found in ms:T2.M3 and ms:T2.M4. Prop. 2 is false as stated under the paper's own assumption (r-did:inc:1). Prop. 1 and its proof appear correct.",
   "missingEntitlement": "A valid proof of Prop. 2; none exists under A3 if my derivation is right.",
   "repair": "Correct the proof and restate Prop. 2 with the sign implied by A3 (or drop A3 and state the condition under which each sign obtains: the sign is that of g1 h0 - h1 (s+g0)). Restate H2. Report transparently that H2 was formulated with the opposite sign and that the corrected prediction was derived after the results were seen; a design-based reader will treat the interaction result as accommodation, not as a confirmed prediction.",
   "status": "asserted", "checks": ["r-did:chk:1"]},

  {"@id": "r-did:fnd:8", "dimension": "INF", "parameter": "INF.3; INF.4", "severity": "fixable",
   "commitment": ["r-did:cmt:6", "r-did:cmt:5"],
   "problem": "Propositions concern the threshold k*; hypotheses are tested on Phi, the spending-weighted outsourced share (ms:S2.4). With Phi = F(k*) for the spending-weighted distribution F of k on [0,1], dPhi/dm = f(k*) k*_m (positive only if k* < 1 and f(k*) > 0) and the cross-partial is f'(k*) k*_m k*_u + f(k*) k*_mu. Its sign depends on f', so neither the original nor the corrected Prop. 2 fixes the sign of the interaction on the scale tested. The step from proposition to hypothesis is an enthymeme. Also, m is a share that can reach 1 in the data (mean 0.46, SD 0.24) while the model requires m < 1.",
   "missingEntitlement": "A derivation that gives the interaction's sign on the scale on which it is tested.",
   "repair": "State conditions on F (e.g. f non-increasing near k*, or a parametric family) under which the Phi-scale signs follow; or test at the function level, where the threshold prediction applies directly; address m = 1.",
   "status": "asserted", "checks": ["r-did:chk:5"]},

  {"@id": "r-did:fnd:9", "dimension": "INF", "parameter": "INF.1; INF.7", "severity": "fixable",
   "commitment": ["r-did:cmt:17"],
   "problem": "When H2 fails, ms:S5 offers a legitimacy-signalling explanation that is untested, sits outside the model, is called 'consistent with our theory', and uses causal language ('legitimacy pressures to retain in-house functions') without any design (INF.1). It also strains the conclusion that the 'substance is economizing' (r-did:inc:5, r-did:inc:6). Given r-did:fnd:7, the explanation is also unnecessary.",
   "missingEntitlement": "Any evidence for the legitimacy mechanism.",
   "repair": "After correcting Prop. 2, delete the legitimacy account or present it as a labelled conjecture with a test that discriminates it from the corrected model (e.g. the legitimacy account predicts retention of visible functions specifically; the corrected model predicts the dampening across all functions in proportion to specificity).",
   "status": "asserted", "checks": ["r-did:chk:1"]},

  {"@id": "r-did:fnd:10", "dimension": "INF", "parameter": "INF.7", "severity": "minor",
   "commitment": ["r-did:cmt:18", "r-did:cmt:26"],
   "problem": "H3 is stated unconditionally (ms:H3), and Model 1 supports it (0.137, SE 0.031). The verdict 'H3 is not supported' (ms:S4.H3) tests a conditional reformulation (ms:S2.4 last paragraph). The rival is also not stated in its strongest form: an institutional account in which standards adoption itself diffuses mimetically predicts the same Model 2 pattern (r-did:fnd:2 (ii)).",
   "missingEntitlement": "Agreement between the hypothesis as stated and as tested; a discriminating prediction.",
   "repair": "Restate H3 as the conditional proposition actually tested, and state the strongest institutional rival with a prediction that differs from the transaction-cost account (Section 5 below gives one).",
   "status": "asserted", "checks": ["r-did:chk:6"]}
]
```

### 3.4 ONT, Ontological (weight 0.3)

My construct-individuation standard is loose (ONT.4) and I am indifferent to level of analysis (ONT.2), so most construct questions that a field-theoretic reviewer would press are minor for me.

```json
[
  {"@id": "r-did:fnd:16", "dimension": "ONT", "parameter": "ONT.4", "severity": "minor",
   "commitment": ["ms:S3.2 Environmental uncertainty"],
   "problem": "The model's u is uncertainty that triggers unanticipated adaptations in IT governance (ms:S2.2); the measure is the coefficient of variation of quarterly admissions (ms:S3.2). Demand volatility is a loose proxy for adaptation uncertainty in IT. Under a loose individuation standard I accept it, but the interaction result depends on it.",
   "missingEntitlement": "An argument that admissions volatility moves IT adaptation needs.",
   "repair": "One sentence of argument plus an alternative proxy (e.g. frequency of IT system changes or regulatory changes) as a robustness check.",
   "status": "asserted", "checks": []},

  {"@id": "r-did:fnd:17", "dimension": "ONT", "parameter": "ONT.5", "severity": "minor",
   "commitment": ["r-did:cmt:17"],
   "problem": "The legitimacy-signalling explanation in ms:S5 is functional in form (in-house IT persists because it serves to signal resilience), a model class this perspective treats as suspect. It does not name the individual-level mechanism (ONT.3) by which boards or stakeholders reward visible in-house IT.",
   "missingEntitlement": "A mechanism at the level of decision-makers.",
   "repair": "Either drop the explanation (see r-did:fnd:9) or specify who decides, on what information, and what observable follows.",
   "status": "asserted", "checks": []}
]
```

On ONT.1, the model's entities (boundedly rational hospital decision-makers choosing governance; technologies and interfaces as artifacts) are admissible for me. No material finding there.

### 3.5 PRA, Pragmatic (weight 0.3)

```json
[
  {"@id": "r-did:fnd:18", "dimension": "PRA", "parameter": "PRA.3", "severity": "minor",
   "commitment": ["r-did:cmt:23"],
   "problem": "The priority claim is checked only 'sometimes' under my standard, but this one is checkable and I doubt it. Earlier work tested economic versus institutional or imitation accounts of IS outsourcing, for example Loh & Venkatraman (1992) on imitation in IT outsourcing diffusion (Information Systems Research, to verify) and Ang & Cummings (1997) on institutional versus economic influences on IS outsourcing (Organization Science, to verify).",
   "missingEntitlement": "A literature check supporting 'first'.",
   "repair": "Remove the priority claim or position the paper against that literature.",
   "status": "asserted", "checks": []},

  {"@id": "r-did:fnd:19", "dimension": "PRA", "parameter": "PRA.4; INF.1", "severity": "minor",
   "commitment": ["r-did:cmt:24"],
   "problem": "The practice implication (ms:S5.1) presupposes the causal claim. I put little weight on practice implications (PRA.4 low), so this is minor, but it repeats r-did:fnd:1 in prescriptive form.",
   "missingEntitlement": "As r-did:fnd:1.",
   "repair": "Condition the implication on a design-based estimate, or phrase it as an association.",
   "status": "asserted", "checks": []}
]
```

For an applied-economics audience (PRA.1) the contribution is a gap-spotting one (PRA.2): a hospital panel linking an interoperability measure to sourcing, with a potential quasi-experiment in the state requirements. That is a publishable contribution in my community *if* the design is delivered. The "adjudication" framing addresses the organization-theory conversation and is not what my community would read the paper for.

---
### 3.6 Checks for the harness

Each check is self-contained and uses only `sympy`, `numpy`, `scipy`, `statsmodels`, `pandas`. Each states the outcome that would **support** my finding and the outcome that would **refute** it. All linked findings stay `asserted` until the harness reports.

```json
[
  {"@id": "r-did:chk:1", "tests": ["r-did:fnd:7", "r-did:inc:1", "r-did:cmt:1", "r-did:cmt:4", "r-did:cmt:5"], "status": "asserted",
   "supportsFindingIf": "symbolic numerator of d2k*/(dm du) equals g1*h0 - h1*(s+g0); it differs from the appendix expression; it is negative under A3 symbolically and at every sampled parameter point",
   "refutesFindingIf": "the cross-partial equals g1/(H(1-m)^2) or is positive for some A3-satisfying point"},
  {"@id": "r-did:chk:2", "tests": ["r-did:fnd:6", "r-did:inc:4"], "status": "asserted",
   "supportsFindingIf": "ms:T2.M3.uncertainty implies p > 0.05 under every rounding of the reported coefficient and SE, and all other cells' markers match",
   "refutesFindingIf": "the cell implies p < 0.001 under some admissible rounding"},
  {"@id": "r-did:chk:3", "tests": ["r-did:fnd:5", "r-did:inc:3"], "status": "asserted",
   "supportsFindingIf": "412 x 11 != 4712 and 4712/412 is not an integer",
   "refutesFindingIf": "the balanced-panel count equals 4712"},
  {"@id": "r-did:chk:4", "tests": ["r-did:fnd:2", "r-did:fnd:14", "r-did:cmt:22"], "status": "asserted",
   "supportsFindingIf": "the Model 2 peer 95% interval includes effects of substantive size, and the smallest equivalence bound passable at alpha = 0.05 is a large fraction of the Model 1 estimate; the effect-size arithmetic reproduces 2.7 pp and about 1/6 SD",
   "refutesFindingIf": "an equivalence test passes at a bound well below the Model 1 estimate"},
  {"@id": "r-did:chk:5", "tests": ["r-did:fnd:8"], "status": "asserted",
   "supportsFindingIf": "for A3-satisfying parameters with k*_mu < 0, the Phi-scale cross-partial is negative for some spending distributions F and positive for others",
   "refutesFindingIf": "the Phi-scale cross-partial has the sign of k*_mu for every F tried"},
  {"@id": "r-did:chk:6", "tests": ["r-did:fnd:3", "r-did:inc:2", "r-did:fnd:2", "r-did:fnd:10"], "status": "asserted",
   "supportsFindingIf": "A: with a true modularity effect of zero and capability confounding, the modularity coefficient is clearly nonzero both without and with the staffing control; B: with diffusion of modularity driven entirely by peer outsourcing, the peer coefficient is positive without m and near zero with m",
   "refutesFindingIf": "A: adding staffing drives the confounded coefficient to about zero; B: the peer coefficient stays positive after controlling for m"},
  {"@id": "r-did:chk:7", "tests": ["r-did:fnd:4"], "status": "asserted",
   "supportsFindingIf": "static TWFE under staggered adoption with dynamic, cohort-heterogeneous effects departs materially from the true ATT",
   "refutesFindingIf": "TWFE recovers the true ATT closely in this design"}
]
```

#### `r-did:chk:1` Propositions 1 and 2 (symbolic and numeric)

```python
import sympy as sp
import numpy as np

m, u = sp.symbols('m u', real=True)
s, h0, g0, g1, d = sp.symbols('s h0 g0 g1 delta', positive=True)
h1 = sp.symbols('h1', positive=True)

H = h0 + h1*u
G = g0 + g1*u
kstar = (s + G) / (H*(1 - m))

k_m  = sp.simplify(sp.diff(kstar, m))
k_u  = sp.simplify(sp.diff(kstar, u))
k_mu = sp.simplify(sp.diff(kstar, m, u))

# Prop. 1: compare with the appendix expression
app_k_m = (s + G) / (H*(1 - m)**2)
print("Prop1 matches appendix:", sp.simplify(k_m - app_k_m) == 0)

# Prop. 2: appendix expression versus the full derivative
app_k_mu = g1 / (H*(1 - m)**2)
print("Prop2 appendix expression equals full derivative:", sp.simplify(k_mu - app_k_mu) == 0)

num_mu = sp.expand(sp.simplify(k_mu * H**2 * (1 - m)**2))
num_u  = sp.expand(sp.simplify(k_u  * H**2 * (1 - m)))
print("numerator of k_mu:", num_mu)
print("numerator of k_u :", num_u)
target = sp.expand(g1*h0 - h1*(s + g0))
print("k_mu numerator == g1*h0 - h1*(s+g0):", sp.simplify(num_mu - target) == 0)
print("k_u  numerator == g1*h0 - h1*(s+g0):", sp.simplify(num_u - target) == 0)

# Impose A3 as h1 = h0*g1*(1+delta)/(s+g0), delta > 0
A3 = {h1: h0*g1*(1 + d)/(s + g0)}
num_A3 = sp.simplify(target.subs(A3))
print("numerator under A3:", num_A3, "| is_negative:", num_A3.is_negative)

# Numeric sweep over A3-satisfying parameters, m in [0, 0.99), u in [0, 5]
rng = np.random.default_rng(0)
f_kmu = sp.lambdify((m, u, s, h0, h1, g0, g1), k_mu, 'numpy')
signs = []
for _ in range(20000):
    S, H0, G0, G1 = rng.uniform(0.01, 3, 4)
    H1 = H0*G1/(S + G0)*(1 + rng.uniform(0.001, 5))
    M, U = rng.uniform(0, 0.99), rng.uniform(0, 5)
    signs.append(np.sign(f_kmu(M, U, S, H0, H1, G0, G1)))
signs = np.array(signs)
print("share of A3 draws with k_mu < 0:", np.mean(signs < 0))
print("share of A3 draws with k_mu > 0:", np.mean(signs > 0))
```

#### `r-did:chk:2` Significance markers in Table 2

```python
import numpy as np
import pandas as pd
from scipy import stats

cells = [
    ("M1", "Peer", 0.137, 0.031, "***"), ("M2", "Peer", 0.042, 0.038, ""),
    ("M3", "Peer", 0.039, 0.037, ""),    ("M4", "Peer", 0.036, 0.036, ""),
    ("M2", "Modularity", 0.112, 0.024, "***"), ("M3", "Modularity", 0.118, 0.025, "***"),
    ("M4", "Modularity", 0.097, 0.023, "***"),
    ("M3", "Uncertainty", 0.084, 0.051, "***"), ("M4", "Uncertainty", 0.079, 0.050, ""),
    ("M3", "Mod x Unc", -0.061, 0.019, "**"),   ("M4", "Mod x Unc", -0.058, 0.019, "**"),
    ("M1", "Specificity", -0.094, 0.027, "***"), ("M2", "Specificity", -0.091, 0.027, "***"),
    ("M3", "Specificity", -0.090, 0.026, "***"), ("M4", "Specificity", -0.088, 0.026, "***"),
    ("M4", "Staffing", -0.143, 0.029, "***"),
]
df_t = 412 - 1  # clusters - 1

def stars(p):
    return "***" if p < 0.001 else "**" if p < 0.01 else "*" if p < 0.05 else ""

rows = []
for mdl, var, b, se, rep in cells:
    # rounding interval: reported to 3 decimals
    t_lo = (abs(b) - 0.0005) / (se + 0.0005)
    t_hi = (abs(b) + 0.0005) / (se - 0.0005)
    t = abs(b) / se
    p_z  = 2*stats.norm.sf(t)
    p_t  = 2*stats.t.sf(t, df_t)
    p_lo = 2*stats.t.sf(t_hi, df_t)   # most significant admissible
    p_hi = 2*stats.t.sf(t_lo, df_t)   # least significant admissible
    rows.append(dict(model=mdl, var=var, b=b, se=se, t=round(t, 3), p_t=p_t, p_z=p_z,
                     reported=rep, implied=stars(p_t),
                     implied_range=(stars(p_hi), stars(p_lo)),
                     consistent=(rep in {stars(p_hi), stars(p_lo), stars(p_t)})))
out = pd.DataFrame(rows)
pd.set_option("display.width", 200)
print(out.to_string(index=False))
print("\nInconsistent cells:\n", out.loc[~out.consistent, ["model", "var", "b", "se", "t", "p_t", "reported", "implied"]])
```

#### `r-did:chk:3` Sample size arithmetic

```python
hospitals, first, last, N_reported = 412, 2009, 2019, 4712
years = last - first + 1
print("years:", years)
print("balanced N:", hospitals*years, "| reported:", N_reported, "| equal:", hospitals*years == N_reported)
print("reported N / hospitals:", N_reported/hospitals, "| integer:", N_reported % hospitals == 0)
print("balanced N if 2009 lost to the t-1 peer lag:", hospitals*(years - 1))
print("excess of reported over balanced N:", N_reported - hospitals*years)
```

#### `r-did:chk:4` Effect size, peer-coefficient interval and equivalence bound

```python
from scipy import stats

b_mod, sd_m, sd_phi = 0.112, 0.24, 0.17
eff = b_mod*sd_m
print("1-SD modularity effect (pp):", round(100*eff, 2), "| in outcome SDs:", round(eff/sd_phi, 3))

b1_peer, b2_peer, se2 = 0.137, 0.042, 0.038
print("relative fall in peer coefficient M1 -> M2:", round((b1_peer - b2_peer)/b1_peer, 3))
z95, z90 = stats.norm.ppf(0.975), stats.norm.ppf(0.95)
print("M2 peer 95% CI:", (round(b2_peer - z95*se2, 4), round(b2_peer + z95*se2, 4)))
print("M2 peer 90% CI:", (round(b2_peer - z90*se2, 4), round(b2_peer + z90*se2, 4)))

def tost_p(b, se, delta):
    p_lower = stats.norm.sf((b + delta)/se)   # H0: beta <= -delta
    p_upper = stats.norm.cdf((b - delta)/se)  # H0: beta >= +delta
    return max(p_lower, p_upper)

for delta in [0.02, 0.05, 0.0685, 0.10, 0.137]:
    print(f"TOST p at bound +/-{delta}: {tost_p(b2_peer, se2, delta):.4f}")
delta_min = max(abs(b2_peer - z90*se2), abs(b2_peer + z90*se2))
print("smallest bound passable at alpha=0.05:", round(delta_min, 4),
      "| as share of M1 estimate:", round(delta_min/b1_peer, 3))
```

#### `r-did:chk:5` Sign of the interaction on the Phi scale

```python
import numpy as np
from scipy import stats

# Parameters chosen to satisfy A3: h1/h0 = 0.5 > g1/(s+g0) = 0.2
s, g0, g1, h0, h1 = 0.2, 0.3, 0.1, 1.0, 0.5
assert h1/h0 > g1/(s + g0)

def kstar(m, u):
    return (s + g0 + g1*u) / ((h0 + h1*u) * (1 - m))

def Phi(m, u, dist):
    # spending-weighted share of functions with k < k*, k distributed on [0,1]
    return dist.cdf(np.minimum(kstar(m, u), 1.0))

def cross(f, m, u, e=1e-4):
    return (f(m+e, u+e) - f(m+e, u-e) - f(m-e, u+e) + f(m-e, u-e)) / (4*e*e)

dists = {"uniform": stats.uniform(0, 1), "beta(2,2)": stats.beta(2, 2),
         "beta(5,2)": stats.beta(5, 2), "beta(1,3)": stats.beta(1, 3), "beta(2,5)": stats.beta(2, 5)}

for M, U in [(0.3, 0.0), (0.2, 0.5), (0.1, 1.0)]:
    ks = kstar(M, U)
    print(f"\nm={M}, u={U}: k*={ks:.3f} (interior: {ks < 1}), k*_mu={cross(kstar, M, U):+.4f}")
    for name, dist in dists.items():
        val = cross(lambda a, b: Phi(a, b, dist), M, U)
        print(f"  {name:10s} Phi_mu = {val:+.5f}")
```

#### `r-did:chk:6` Bad control (staffing) and mediator (modularity) simulations

```python
import numpy as np

rng = np.random.default_rng(42)

def twoway_demean(x):
    return x - x.mean(1, keepdims=True) - x.mean(0, keepdims=True) + x.mean()

def ols(y, *xs):
    X = np.column_stack([twoway_demean(x).ravel() for x in xs])
    return np.linalg.lstsq(X, twoway_demean(y).ravel(), rcond=None)[0]

# Scenario A: true modularity effect = 0; time-varying capability w confounds m and Phi;
# staffing is reduced one-for-one by outsourcing (the manuscript's own account, ms:S3.2).
N, T, R = 412, 11, 200
resA = []
for _ in range(R):
    alpha = rng.normal(0, 0.1, (N, 1))
    w = np.cumsum(rng.normal(0, 0.3, (N, T)), axis=1)          # time-varying capability
    m = 0.4 + 0.5*w + rng.normal(0, 0.5, (N, T))
    phi = alpha + 0.0*m + 0.3*w + rng.normal(0, 0.5, (N, T))   # beta_m = 0
    staff = -1.0*phi + 0.2*w + rng.normal(0, 0.2, (N, T))
    resA.append((ols(phi, m)[0], ols(phi, m, staff)[0]))
resA = np.array(resA)
print("Scenario A (true beta_m = 0)")
print("  beta_m without staffing: mean %.3f, sd %.3f" % (resA[:, 0].mean(), resA[:, 0].std()))
print("  beta_m with staffing   : mean %.3f, sd %.3f" % (resA[:, 1].mean(), resA[:, 1].std()))

# Scenario B: no direct peer effect on Phi. Modularity diffuses ONLY by imitation of
# peers' lagged outsourcing (leave-one-out same-state mean), and Phi depends on m.
S, T, R = 50, 11, 200
resB = []
for _ in range(R):
    state = np.concatenate([np.arange(S), rng.integers(0, S, 412 - S)])   # every state >= 1, most >= 2
    N = state.size
    a_s = rng.normal(0, 0.1, S)
    alpha = 0.3 + a_s[state] + rng.normal(0, 0.05, N)
    beta, kappa = 0.1, 0.1
    m = np.zeros((N, T + 1)); phi = np.zeros((N, T + 1)); peer = np.full((N, T + 1), np.nan)
    m[:, 0] = rng.uniform(0.1, 0.4, N)
    phi[:, 0] = alpha + beta*m[:, 0] + rng.normal(0, 0.03, N)
    for t in range(1, T + 1):
        tot = np.bincount(state, phi[:, t-1], minlength=S)
        cnt = np.bincount(state, minlength=S)
        loo = np.where(cnt[state] > 1, (tot[state] - phi[:, t-1]) / np.maximum(cnt[state] - 1, 1), np.nan)
        peer[:, t] = loo
        m[:, t] = m[:, t-1] + kappa*np.nan_to_num(loo, nan=phi[:, t-1]) + rng.normal(0, 0.02, N)
        phi[:, t] = alpha + beta*m[:, t] + rng.normal(0, 0.03, N)
    keep = ~np.isnan(peer[:, 1:]).any(axis=1)          # drop single-hospital states
    P, M_, F = peer[keep, 1:], m[keep, 1:], phi[keep, 1:]
    resB.append((ols(F, P)[0], ols(F, P, M_)[0], ols(F, P, M_)[1]))
resB = np.array(resB)
print("Scenario B (all diffusion of m is imitation; no direct peer effect on Phi)")
print("  peer coef without m: mean %.3f, sd %.3f" % (resB[:, 0].mean(), resB[:, 0].std()))
print("  peer coef with m   : mean %.3f, sd %.3f" % (resB[:, 1].mean(), resB[:, 1].std()))
print("  m coef with peer   : mean %.3f (true beta = 0.1)" % resB[:, 2].mean())
```

#### `r-did:chk:7` Static TWFE under staggered adoption with dynamic, heterogeneous effects

```python
import numpy as np

rng = np.random.default_rng(7)
years = np.arange(2009, 2020)
S, per = 40, 10
cohorts = np.array([2011]*5 + [2012]*5 + [2013]*5 + [2014]*5 + [2015]*6 + [2016]*6 + [0]*8)  # 0 = never
assert cohorts.size == S
g = np.repeat(cohorts, per)
N, T = g.size, years.size

def twoway_demean(x):
    return x - x.mean(1, keepdims=True) - x.mean(0, keepdims=True) + x.mean()

R, est, att = 200, [], []
for _ in range(R):
    t = np.broadcast_to(years, (N, T))
    D = ((g[:, None] > 0) & (t >= g[:, None])).astype(float)
    slope = np.where(g > 0, 0.01*(2017 - g), 0.0)[:, None]     # earlier cohorts gain faster
    tau = D * slope * (t - g[:, None] + 1)
    y = rng.normal(0, 0.1, (N, 1)) + 0.01*(t - 2009) + tau + rng.normal(0, 0.05, (N, T))
    yd, Dd = twoway_demean(y).ravel(), twoway_demean(D).ravel()
    est.append((Dd @ yd) / (Dd @ Dd))
    att.append(tau[D == 1].mean())
print("true ATT over treated cells: %.4f" % np.mean(att))
print("static TWFE estimate       : %.4f (sd %.4f)" % (np.mean(est), np.std(est)))
print("TWFE / ATT                 : %.2f" % (np.mean(est)/np.mean(att)))
```

Harness note. `r-did:chk:7` tests only the static-TWFE part of `r-did:fnd:4`. The claim that TWFE event-time coefficients are contaminated under cohort heterogeneity is `deferred` to the corpus (Goodman-Bacon 2021; de Chaisemartin & D'Haultfoeuille 2020; Callaway & Sant'Anna 2021) and to Sun & Abraham (2021) (to verify), and stays `asserted` here.

---
### 3.7 Findings at a glance

| Id | Dim. | Severity | Short form | Status |
|---|---|---|---|---|
| `r-did:fnd:1` | EPI.3 | fatal | Causal modularity effect rests on MI6; reverse causality and hospital-specific EHR timing unaddressed | asserted |
| `r-did:fnd:2` | EPI.5 / INF.2 | fatal | "Rule out mimetic isomorphism" rests on MI7; wide interval; modularity may mediate imitation; reflection problem | asserted (chk:4, chk:6) |
| `r-did:fnd:7` | INF.3 | damaging | Prop. 2 proof omits H'(u); under A3 the cross-partial is negative | asserted (chk:1) |
| `r-did:fnd:4` | TEC.3 | damaging | Event study: TWFE under staggered adoption, unreported, no first stage, wrong cluster level | asserted (chk:7, partly deferred) |
| `r-did:fnd:3` | TEC.3 | fixable | In-house staffing is a bad control (descendant of outcome) | asserted (chk:6) |
| `r-did:fnd:5` | TEC.4 | fixable | 412 x 11 = 4,532, not 4,712 | asserted (chk:3) |
| `r-did:fnd:8` | INF.3 | fixable | Threshold-scale propositions do not fix signs on the Phi scale | asserted (chk:5) |
| `r-did:fnd:9` | INF.1 | fixable | Post hoc legitimacy account, untested and redundant once Prop. 2 is corrected | asserted |
| `r-did:fnd:11` | TEC.3 | fixable | Hospital clustering for state-level regressors | asserted |
| `r-did:fnd:12` | TEC.3 | fixable | Asset-specificity control may be a mediator | asserted |
| `r-did:fnd:13` | TEC.1 | fixable | No replication package | asserted |
| `r-did:fnd:15` | EPI.3 | fixable | All-years-responder sample may select on outcome | asserted |
| `r-did:fnd:6` | TEC.4 | minor | Model 3 uncertainty *** inconsistent with t = 1.65 | asserted (chk:2) |
| `r-did:fnd:10` | INF.7 | minor | H3 stated unconditionally, tested conditionally | asserted |
| `r-did:fnd:14` | EPI.5 | minor | "Strongly predicts" for a 0.16 SD association; stars, no intervals | asserted (chk:4) |
| `r-did:fnd:16` | ONT.4 | minor | Admissions volatility as uncertainty proxy | asserted |
| `r-did:fnd:17` | ONT.5 | minor | Legitimacy account is functional in form | asserted |
| `r-did:fnd:18` | PRA.3 | minor | Priority claim doubtful (to verify) | asserted |
| `r-did:fnd:19` | PRA.4 | minor | Practice implication presupposes causality | asserted |
| `r-did:fnd:20` | EPI.6 | minor | Correlated single-informant reporting | asserted |

---

## 4. Contribution verdicts

```json
[
  {"@id": "r-did:vrd:1", "contribution": "r-did:ctb:1", "verdict": "qualified",
   "narrowerForm": "A transaction-cost threshold model in which modularity raises the make-or-buy threshold (Prop. 1). Under the paper's own Assumption A3, uncertainty WEAKENS that effect on the threshold (corrected Prop. 2, pending r-did:chk:1). Neither sign carries over to the spending-weighted share without assumptions on the distribution of k.",
   "basis": ["r-did:fnd:7", "r-did:fnd:8", "r-did:inc:1"],
   "reVoicing": "A comparative-statics device that generates sign restrictions for a reduced-form regression: dPhi/dm > 0, and under A3 d2Phi/(dm du) < 0 given conditions on F.",
   "lostInTranslation": "The hold-up and governance vocabulary does no work in my test; only the signs matter. The paper's claim to have 'formalized' the transaction-cost logic is, for me, a claim about two signs, one of which was derived wrongly."},

  {"@id": "r-did:vrd:2", "contribution": "r-did:ctb:2", "verdict": "qualified",
   "narrowerForm": "Conditional on hospital and year fixed effects and controls, within-hospital increases in CIO-reported modularity are associated with higher outsourcing shares (about 0.16 SD per SD of modularity), and the association is weaker where admissions are volatile. These are associations, not tests of causal propositions.",
   "basis": ["r-did:fnd:1", "r-did:fnd:4", "r-did:fnd:14"],
   "reVoicing": "Descriptive panel evidence on a new hospital-level interoperability measure.",
   "lostInTranslation": "'Testing against a rival' is lost: no discriminating design is offered, and the rival is not tested in its strongest form."},

  {"@id": "r-did:vrd:3", "contribution": "r-did:ctb:3", "verdict": "fails",
   "reason": "'Rule out' rests on MI7, which I reject; the 95% interval for the Model 2 peer coefficient (about -0.03 to 0.12) reaches close to the Model 1 estimate of 0.137; controlling for modularity may block imitation that runs through standards adoption; correlated state-level effects are not separated from peer effects; and SEs are clustered below the level of the regressor.",
   "survivingRemnant": "Conditional on modularity, the same-state lagged peer association is smaller and imprecisely estimated.",
   "basis": ["r-did:fnd:2", "r-did:fnd:10", "r-did:fnd:11"],
   "reVoicing": "Adding m to the regression attenuates the coefficient on the state-year peer mean.",
   "lostInTranslation": "Everything about mimicry. My tradition can say nothing about the mechanism behind the peer coefficient without a design for peer effects."},

  {"@id": "r-did:vrd:4", "contribution": "r-did:ctb:4", "verdict": "fails",
   "reason": "Causal language ('standards made IT functions modular ... widened the range') without a design. The state-requirement event study could become that design but, as reported, it is TWFE, unreported, reduced form, and clustered at the wrong level.",
   "conditionForSurvival": "A heterogeneity-robust staggered DiD on state requirements with a first stage on modularity, a defended exclusion restriction, and state-level inference.",
   "basis": ["r-did:fnd:1", "r-did:fnd:4", "r-did:fnd:3"]},

  {"@id": "r-did:vrd:5", "contribution": "r-did:ctb:5", "verdict": "qualified",
   "narrowerForm": "A conjecture that interface standards lower the relationship-specificity of IT investments, consistent with the associations reported but not tested: the manuscript does not show that modularity lowers measured specificity.",
   "basis": ["r-did:fnd:12", "r-did:fnd:1"],
   "reVoicing": "Interface standardization shifts a cost parameter of the outsourcing decision. I am neutral on MI8 (standardized interfaces reduce specificity): it is a hypothesis here, not a premise.",
   "lostInTranslation": "The general claim that 'specificity is not a fixed property of an activity'; my tradition would want the first stage (m on measured specificity) before saying so."},

  {"@id": "r-did:vrd:6", "contribution": "r-did:ctb:6", "verdict": "qualified",
   "narrowerForm": "Priority not established; earlier work appears to test economic against imitation or institutional accounts of IS outsourcing (to verify).",
   "basis": ["r-did:fnd:18"]},

  {"@id": "r-did:vrd:7", "contribution": "r-did:ctb:7", "verdict": "fails",
   "reason": "A prescription requires the causal effect the paper has not identified.",
   "basis": ["r-did:fnd:19", "r-did:fnd:1"]}
]
```

---

## 5. Rival explanation (L11: from a tradition other than the manuscript's)

**`r-did:rival:1` Vendor-led bundling around hospital-specific EHR adoption (reverse causality plus a common, hospital-specific driver).** The 2009 federal incentive programme required certified EHR technology, and hospitals reached each stage at different times. I conjecture (an empirical premise of the rival, to verify) that many met the requirement by contracting with a vendor that hosted or managed the systems, and that this vendor connected the hospital's clinical systems through its own certified interfaces. On this account a single hospital-specific event (the vendor contract that accompanies EHR adoption) raises measured modularity and the outsourced share in the same year. Modularity need not have any causal effect on the make-or-buy margin. Hospital fixed effects do not remove the event, because its timing varies within hospital. Year fixed effects remove only the national average of the timing. The rival also accounts for the peer pattern: hospitals in the same state face the same state requirements and the same regional vendor markets, so their adoption dates cluster. That makes the state peer mean correlated with own modularity without any imitation and without any economizing on hold-up.

**Discriminating observations.**

1. *Timing within hospital.* The transaction-cost account says a rise in modularity precedes the outsourcing of the functions it affects. The rival says modularity jumps in the year a vendor contract starts or after it, and in the systems the vendor took over. Test: an event study of modularity around vendor-contract start dates, and of outsourcing around changes in modularity, with leads.
2. *Spillover across functions.* The transaction-cost account says certified interfaces on system A make it cheaper to outsource function B, which connects to A, so the effect appears in functions that were not the ones re-interfaced. The rival says modularity rises only in the functions that were outsourced. Function-level data would separate the two.
3. *Exogenous mandates with a first stage.* Both accounts predict that state requirements raise modularity. Only the transaction-cost account predicts that the induced modularity raises outsourcing in hospitals that had already adopted certified EHR before the mandate. The rival predicts no outsourcing response in that subgroup.
4. *A sign the corrected model fixes.* The corrected model predicts that uncertainty lowers the outsourcing threshold (`r-did:cmt:5`). The rival makes no prediction about admissions volatility. A well-identified negative main effect of uncertainty would favour the manuscript's model; a null would not discriminate.

---
## 6. What would change my mind

```json
[
  {"finding": "r-did:fnd:1", "severity": "fatal",
   "wouldWithdrawIf": "A heterogeneity-robust staggered DiD on the state certified-interface requirements (Callaway & Sant'Anna 2021 or de Chaisemartin & D'Haultfoeuille 2020) shows a strong first stage on modularity, flat pre-trends that survive a sensitivity analysis for pre-trend violations, a reduced-form outsourcing response whose Wald-DiD ratio is close to the FE estimate, state-clustered inference, and a credible exclusion argument. Alternatively, within-hospital timing evidence that modularity rises before outsourcing of the affected functions, together with a function-level placebo. Either would move the causal claim from unentitled to evidenced."},
  {"finding": "r-did:fnd:2", "severity": "fatal",
   "wouldWithdrawIf": "(a) The authors drop 'rule out' and adopt the narrower claim in r-did:vrd:3, which turns the finding into a fixable presentation matter; or (b) an equivalence test excludes peer effects of substantive size (for example a state-clustered interval of roughly +/-0.03 around zero) in a design where modularity cannot be a channel of imitation, for instance with modularity instrumented by state mandates and peers defined by networks that cross state lines, or with exogenous shocks to peers."},
  {"finding": "r-did:fnd:7", "severity": "damaging",
   "wouldWithdrawIf": "The harness runs r-did:chk:1 and reports that the cross-partial equals the appendix expression, or is positive for some parameters satisfying A3; or the authors show that H does not depend on u in the way ms:S2.2 writes it (which would require changing the model, not the proof)."},
  {"finding": "r-did:fnd:4", "severity": "damaging",
   "wouldWithdrawIf": "The full event study is reported with a heterogeneity-robust estimator and never-treated or not-yet-treated controls, with leads and lags and intervals clustered by state, and the estimates agree with the TWFE version."}
]
```

---

## 7. Recommendation

**Major revision** (simulated; at the boundary with reject).

The associational core survives (`r-did:vrd:2`): within-hospital changes in CIO-reported modularity are associated with higher outsourcing shares, by about one-sixth of a standard deviation per standard deviation. Neither of the two claims the title advertises stands as written. "Modularity" as a cause fails for want of a design (`r-did:fnd:1`, `r-did:vrd:4`). "Not mimicry" fails because it infers absence from non-significance after conditioning on a plausible channel of imitation (`r-did:fnd:2`, `r-did:vrd:3`). The formal contribution is half wrong: by my derivation Prop. 2 has the opposite sign under the paper's own A3 (`r-did:fnd:7`). Ironically, the corrected model predicts the negative interaction the authors found and explained away with an untested legitimacy story (`r-did:fnd:9`). There are also numerical inconsistencies (`r-did:fnd:5`, `r-did:fnd:6`), a bad control used as the only answer to time-varying confounding (`r-did:fnd:3`), and inference at the wrong cluster level (`r-did:fnd:11`). I recommend major revision rather than rejection because the manuscript already contains the ingredients of a credible design: staggered state requirements for certified interfaces, 2011 to 2016. Each fatal finding has a concrete repair, and the theory error is a correction that helps the paper. If the editor treats building a new identification strategy as beyond the scope of a revision, the same reasoning supports reject and resubmit. Acceptance should be conditional on a replication package (`r-did:fnd:13`, TEC.1).

---

## 8. Self-location

The parameters that most drive my verdicts, so that a panel can trace disagreements to them:

1. **EPI.3 = design-based, together with the rejection of MI6.** This parameter alone turns the FE estimates from evidence of a causal effect into evidence of an association. It drives `r-did:fnd:1`, `r-did:fnd:4`, `r-did:vrd:4` and `r-did:vrd:7`. A reviewer who endorses MI6, or who accepts model-based identification, would grade `r-did:fnd:1` damaging or fixable rather than fatal.
2. **Rejection of MI7, together with EPI.5 (intervals and equivalence tests over significance).** This drives `r-did:fnd:2` and the failure of `r-did:ctb:3`. A reviewer who reads a vanishing coefficient as disconfirmation would let "not mimicry" stand, at least in a qualified form.
3. **TEC.3 = very high and TEC.4 = always, with INF.3 = proof.** These parameters generate the bad-control, clustering, staggered-TWFE, sample-count and star findings, and the Prop. 2 finding. Under TEC.2 = trust, most of them would not be raised.

Where I expect to differ from the focal reviewer (relation: differing). My ONT.4 is loose and my PRA.4 is low, so I raise construct validity (whether a same-state mean captures mimetic referents; what "legitimacy" means in `ms:S5`) only as minor findings. A reviewer from organization theory would likely make the construct critique of the peer measure central to `r-did:fnd:2` and weigh identification less. My positive verdict on the associational core does not depend on the theory at all, which such a reviewer may regard as a weakness of my reading.

---

## Decisions for the reviewer

1. **`r-did:fnd:1` (fatal, identification).** Accept as fatal, downgrade to damaging (if you endorse MI6 or model-based identification), or reject.
2. **`r-did:fnd:2` (fatal, "rule out mimicry").** Accept as fatal, or treat it as damaging overstatement repairable by the narrower wording in `r-did:vrd:3`.
3. **`r-did:fnd:7` (Prop. 2 sign).** Have the harness run `r-did:chk:1` before raising it. If the check confirms it, decide whether to tell authors that the corrected model predicts their negative interaction, which helps them, while noting that the corrected prediction was derived after the results were seen.
4. **Numerical checks.** Have the harness run `r-did:chk:2` to `r-did:chk:4`. Include `r-did:fnd:5` (N) and `r-did:fnd:6` (stars) only if confirmed.
5. **Simulations.** Decide whether the simulations in `r-did:chk:5` to `r-did:chk:7` should be run and cited in your report, or kept as internal support.
6. **Priority claim (`r-did:fnd:18`).** Verify Loh & Venkatraman (1992) and Ang & Cummings (1997) before citing either; both are marked "(to verify)".
7. **Rival `r-did:rival:1`.** Decide whether to put the vendor-bundling rival and its discriminating tests to the authors. Its empirical premise about how hospitals met EHR requirements is my conjecture and needs checking.
8. **Recommendation.** Choose between major revision and reject and resubmit. The deciding question is whether you will ask the authors to make the state-requirement design the paper's core.
9. **Weighting against the focal perspective.** Decide how much weight this simulated, differing perspective should carry relative to your own on construct-validity questions, which it deliberately underweights (Section 8).
