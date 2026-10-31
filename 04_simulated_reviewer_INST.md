# Run 04: Simulated Reviewer, Institutional theorist (organizational sociology)

**SIMULATED REVIEW. NOT A REVIEW. NEVER TO BE SENT TO AUTHORS.**

- Role: Role 2, Simulated Reviewer (capability 2), instruction set Reviewership v0.1 (23 October 2026)
- Perspective: `persp:R-INST` ("Institutional theorist (organizational sociology)"), owner kind `simulated`
- Relation to focal reviewer: `differing`
- Manuscript: `ms:TEST`, "Modularity, Not Mimicry: Interoperability Standards and the Diffusion of IT Outsourcing in U.S. Hospitals"
- Inputs used: the run file only. No other files and no web.
- Status of formal and numerical findings: every one is `asserted`. None has been run by the harness. Checks are in §3.6.

## 0. Configuration notes

- Weights, in the order this report follows: ONT 0.9, PRA 0.8, INF 0.7, EPI 0.6, TEC 0.3.
- Material inferences. Endorsed: MI3, MI4, MI10. Rejected: MI2, MI7, MI9. Neutral: MI1, MI5, MI6, MI8.
- **The perspective JSON has no `standards` list.** To keep findings checkable, I derived working standards from the parameters. They are *my* derivations, not part of `persp:R-INST`, and the reviewer has to accept or strike them (see Decisions).

```json
{
 "@id": "r-inst:standards",
 "@type": "DerivedStandards",
 "note": "Derived by the simulated reviewer from persp:R-INST parameters; not in the configured perspective. Pending reviewer acceptance.",
 "standards": [
  {"@id": "r-inst:std:1", "dimension": "INF", "parameter": "INF.7", "text": "A rival explanation that the manuscript claims to rule out must be stated in its strongest canonical form and tested on a prediction that discriminates it from the favoured account."},
  {"@id": "r-inst:std:2", "dimension": "INF", "parameter": "INF.2 (MI7 rejected)", "text": "A non-significant coefficient may not be read as evidence of no effect unless an interval or equivalence test excludes effects of substantive size."},
  {"@id": "r-inst:std:3", "dimension": "ONT", "parameter": "ONT.4", "text": "An operational measure of an institutional mechanism (mimetic, coercive, normative) must track the referents and channels the mechanism names, not a proxy that other mechanisms share."},
  {"@id": "r-inst:std:4", "dimension": "ONT", "parameter": "ONT.2", "text": "Where theory and test sit at different levels (function vs. hospital; organization vs. field), the bridge must be explicit. If an interaction is hypothesized, its sign must be derived on the scale on which it is tested."},
  {"@id": "r-inst:std:5", "dimension": "INF", "parameter": "INF.2 (MI9 rejected)", "text": "A claim that a practice is efficient or economizing needs evidence on its consequences. A choice model's equilibrium is not enough."},
  {"@id": "r-inst:std:6", "dimension": "PRA", "parameter": "PRA.3", "text": "Priority and positioning claims are checked against the relevant literature in both traditions."},
  {"@id": "r-inst:std:7", "dimension": "TEC", "parameter": "TEC.3", "text": "No control that is a consequence of the outcome or of the treatment is used to rule out confounding."}
 ]
}
```

## 1. Claimed contributions

Each one is quoted in the manuscript's own words, with its locus.

```json
{
 "@id": "r-inst:contributions",
 "@type": "ClaimedContributions",
 "manuscript": "ms:TEST",
 "contributions": [
  {"@id": "r-inst:ctb:1", "text": "\"we formalize the link between modularity and the make-or-buy decision in a simple transaction-cost model, deriving two propositions\"", "locus": "ms:S1 para 3; ms:S2.3 (ms:Prop1, ms:Prop2); ms:Appendix"},
  {"@id": "r-inst:ctb:2", "text": "\"we test these propositions against an institutional rival using a decade-long panel of hospitals\"", "locus": "ms:S1 para 3; ms:S2.4 (ms:H1, ms:H2, ms:H3); ms:T2"},
  {"@id": "r-inst:ctb:3", "text": "\"once modularity is measured, the apparent peer effects that have motivated institutional accounts disappear\"", "locus": "ms:S1 para 3; ms:S4 (H3 paragraph); ms:T2.M1-M2.Peer"},
  {"@id": "r-inst:ctb:4", "text": "\"The results rule out mimetic isomorphism as a driver of IT outsourcing in this setting\"; the practice \"is, on closer inspection, economizing\"", "locus": "ms:Abstract; ms:S5 para 1; ms:S6"},
  {"@id": "r-inst:ctb:5", "text": "\"the first study to adjudicate directly between transaction-cost and institutional explanations of IT outsourcing\"", "locus": "ms:Abstract; ms:S1 para 3"},
  {"@id": "r-inst:ctb:6", "text": "\"Specificity is not a fixed property of an activity; it is partly a product of interface design, and therefore of standards\"", "locus": "ms:S5.1"},
  {"@id": "r-inst:ctb:7", "text": "\"hospital leaders considering outsourcing should attend first to the modularity of their systems\"", "locus": "ms:S5.1"}
 ]
}
```

## 2. Scoreboard (as attributed by `persp:R-INST`)

Reading guide. `avowed` means stated in the manuscript. `consequential` means attributed by an inference this perspective endorses, which is named. Where an avowed commitment depends on a material inference this perspective *rejects* (MI2, MI7, MI9), that is recorded in `note` and the entitlement is set accordingly. Statements are paraphrases unless they are in quotation marks.

```json
{
 "@id": "r-inst:scoreboard",
 "@type": "Scoreboard",
 "perspective": "persp:R-INST",
 "manuscript": "ms:TEST",
 "commitments": [
  {"@id": "r-inst:cmt:1", "kind": "avowed", "statement": "Certified interoperability standards made hospital IT functions modular and lowered the effective specificity of the hospital-vendor relationship.", "locus": "ms:S1 para 2; ms:S2.2", "entitlement": "deferred", "basis": "Baldwin & Clark 2000; Langlois 2002; Sanchez & Mahoney 1996 (the manuscript's MI8-type inference; this perspective is neutral on MI8)", "note": "The deferral is accepted for the theoretical link. Whether it operates in these data is challenged at r-inst:chl:13."},
  {"@id": "r-inst:cmt:2", "kind": "avowed", "statement": "Proposition 1: dk*/dm > 0.", "locus": "ms:Prop1; ms:Appendix", "entitlement": "argued", "basis": "ms:Appendix proof of Prop. 1", "note": "Status of the derivation: asserted, pending r-inst:chk:1."},
  {"@id": "r-inst:cmt:3", "kind": "avowed", "statement": "Proposition 2: d2k*/dm du > 0.", "locus": "ms:Prop2; ms:Appendix", "entitlement": "unentitled", "basis": "The proof differentiates only the numerator: \"the cross-partial is determined by how the numerator responds to uncertainty\" (ms:Appendix). It drops the H'(u) = h1 term in the denominator.", "note": "Asserted, pending r-inst:chk:1. See r-inst:inc:1."},
  {"@id": "r-inst:cmt:4", "kind": "avowed", "statement": "Assumption A3: h1/h0 > g1/(s + g0).", "locus": "ms:A3, ms:S2.2", "entitlement": "deferred", "basis": "Williamson 1991"},
  {"@id": "r-inst:cmt:5", "kind": "avowed", "statement": "H1: modularity is positively associated with the outsourced share of IT spending.", "locus": "ms:H1; ms:S4", "entitlement": "evidenced", "basis": "ms:T2.M2-M4.Modularity (0.112, 0.118, 0.097; all ***)", "note": "Evidenced as an association. The mechanism is challenged at r-inst:chl:13."},
  {"@id": "r-inst:cmt:6", "kind": "avowed", "statement": "H2: the modularity-outsourcing association is stronger under high uncertainty.", "locus": "ms:H2", "entitlement": "unentitled", "basis": "The data contradict it (ms:T2.M3.MxU = -0.061**) and the derivation behind it fails (r-inst:cmt:3). No sign is derived on the Phi scale.", "note": "See r-inst:chl:2."},
  {"@id": "r-inst:cmt:7", "kind": "avowed", "statement": "The institutional account predicts that hospitals outsource because their peers do (H3), and this is the institutional rival.", "locus": "ms:S2.4; ms:H3", "entitlement": "challenged", "basis": "Only the mimetic mechanism is stated. It is stated without the uncertainty condition and without the two-stage temporal structure in the manuscript's own citations (DiMaggio & Powell 1983; Tolbert & Zucker 1983).", "note": "r-inst:std:1"},
  {"@id": "r-inst:cmt:8", "kind": "avowed", "statement": "Peer outsourcing (the mean of all other *sample* hospitals in the same state at t-1) \"captures the prevalence of the practice in the hospital's immediate field\".", "locus": "ms:S3.2 Peer outsourcing", "entitlement": "challenged", "basis": "Field is equated with state. Referents are not identified. Only survey respondents count as peers.", "note": "r-inst:std:3"},
  {"@id": "r-inst:cmt:9", "kind": "avowed", "statement": "Once modularity enters, the peer coefficient falls and is not significant. \"the apparent peer effect reflects the common diffusion of standards across hospitals in the same state, not imitation\".", "locus": "ms:S4 H3 paragraph; ms:T2.M1-M2.Peer", "entitlement": "challenged", "basis": "The fall in the coefficient is evidenced (0.137 to 0.042). The interpretation 'not imitation' is not evidenced: it is equally what a mediation structure predicts (peer outsourcing leads to own interface certification, which leads to own outsourcing)."},
  {"@id": "r-inst:cmt:10", "kind": "avowed", "statement": "\"The results rule out mimetic isomorphism as a driver of IT outsourcing in this setting.\"", "locus": "ms:Abstract; ms:S5 para 1", "entitlement": "unentitled", "basis": "The only support is the non-significant peer coefficient in ms:T2.M2.", "note": "The inference depends on MI7, which this perspective REJECTS. Its 95% interval is about [-0.032, 0.116] (asserted, r-inst:chk:2)."},
  {"@id": "r-inst:cmt:11", "kind": "avowed", "statement": "The practice \"is, on closer inspection, economizing\"; \"Its substance is economizing.\"", "locus": "ms:Abstract; ms:S6", "entitlement": "unentitled", "basis": "No measure of the cost, quality or performance consequences of outsourcing.", "note": "The step from 'responds to modularity as the model predicts' to 'is economizing' depends on MI9, which this perspective REJECTS. r-inst:std:5."},
  {"@id": "r-inst:cmt:12", "kind": "avowed", "statement": "Because the modularity effect survives the in-house IT staffing control, \"it cannot be attributed to capability differences\".", "locus": "ms:S3.3 para 2; ms:S4 Robustness; ms:T2.M4", "entitlement": "unentitled", "basis": "See r-inst:inc:4."},
  {"@id": "r-inst:cmt:13", "kind": "avowed", "statement": "Under high uncertainty, hospitals face legitimacy pressures to retain functions in-house, which offsets the economizing effect of modularity.", "locus": "ms:S5 para 2", "entitlement": "challenged", "basis": "Post hoc. Untested. Not labelled as an abductive conjecture, apart from \"We believe\"."},
  {"@id": "r-inst:cmt:14", "kind": "avowed", "statement": "The legitimacy interpretation \"is consistent with our theory\".", "locus": "ms:S5 para 2", "entitlement": "unentitled", "basis": "The model (ms:S2.2) has no legitimacy term. See r-inst:inc:2."},
  {"@id": "r-inst:cmt:15", "kind": "avowed", "statement": "This is the first study to adjudicate directly between transaction-cost and institutional explanations of IT outsourcing.", "locus": "ms:Abstract; ms:S1 para 3", "entitlement": "challenged", "basis": "Hedged with \"To our knowledge\". No review of the IS-outsourcing diffusion literature (r-inst:chl:10)."},
  {"@id": "r-inst:cmt:16", "kind": "avowed", "statement": "Identification comes from within-hospital changes in modularity. Year fixed effects absorb national shocks, including the 2009 federal EHR incentive programme.", "locus": "ms:S3.3", "entitlement": "challenged", "basis": "The manuscript relies on MI6 (this perspective is neutral). State-by-year shocks, such as the state certification requirements the manuscript itself reports, are time-varying and not absorbed."},
  {"@id": "r-inst:cmt:17", "kind": "avowed", "statement": "\"outsourcing a function transfers its staff to the vendor or eliminates the positions\".", "locus": "ms:S3.2 In-house IT staffing", "entitlement": "default"},
  {"@id": "r-inst:cmt:18", "kind": "avowed", "statement": "States adopted requirements for certified interfaces at staggered times (2011-2016). Event-study leads are small and outsourcing rises after adoption, \"consistent with a causal effect of modularity\".", "locus": "ms:S4 Robustness", "entitlement": "challenged", "basis": "No coefficients, first stage or estimator details are reported. The exclusion restriction (mandates affect outsourcing only through modularity) is not argued."},
  {"@id": "r-inst:cmt:19", "kind": "avowed", "statement": "Certified interfaces spread under a federal incentive programme (2009) and state requirements (2011-2016).", "locus": "ms:S3.3; ms:S4 Robustness", "entitlement": "default"},
  {"@id": "r-inst:cmt:20", "kind": "avowed", "statement": "Specificity is partly a product of interface design, and therefore of \"standards that firms do not individually control\".", "locus": "ms:S5.1", "entitlement": "argued", "basis": "ms:S1 para 2; ms:S2.2"},
  {"@id": "r-inst:cmt:21", "kind": "consequential", "inference": "MI3 (endorsed), applied to ms:T2.M1.Peer and the manuscript's own phrase \"apparent peer effect\" (ms:S4)", "statement": "The positive, significant peer association in Model 1 is prima facie evidence of imitation under uncertainty. The manuscript bears the burden of defeating it.", "locus": "ms:T2.M1.Peer = 0.137 (0.031)", "entitlement": "evidenced", "basis": "ms:T2.M1"},
  {"@id": "r-inst:cmt:22", "kind": "consequential", "inference": "In words: rules imposed on organizations by the state, or tied to its funding, are coercive isomorphic pressures (DiMaggio & Powell 1983). Applied to r-inst:cmt:19.", "statement": "In this setting, modularity is in part a product of coercive institutional pressure. The manuscript's explanans is therefore partly institutional in origin.", "locus": "ms:S3.3; ms:S4 Robustness", "entitlement": "evidenced", "basis": "The manuscript's own reports (r-inst:cmt:19)."},
  {"@id": "r-inst:cmt:23", "kind": "consequential", "inference": "MI4 (endorsed: formal adoption does not imply implementation)", "statement": "A CIO-reported share of interfaces 'certified to a published standard' measures formal certification. It does not on its own entail implemented, working interoperability.", "locus": "ms:S3.2 Modularity", "entitlement": "challenged", "basis": "No validation of the measure against actual data exchange."},
  {"@id": "r-inst:cmt:24", "kind": "consequential", "inference": "By ms:S2.2 (C_B depends on m only through effective specificity k(1-m)) and ms:S5 para 1 (standards \"reduced the effective specificity\")", "statement": "Conditional on effective specificity, modularity should have little or no further association with outsourcing. Adding modularity should also move the specificity coefficient.", "locus": "ms:S2.2; ms:S5", "entitlement": "challenged", "basis": "ms:T2: modularity stays *** while asset specificity is controlled, and the specificity coefficient barely moves (-0.094 in M1, -0.091 in M2). This is a tension, conditional on the item ('how costly it would be to transfer', ms:S3.2) measuring effective rather than nominal specificity."},
  {"@id": "r-inst:cmt:25", "kind": "consequential", "inference": "Quotient-rule differentiation of k* (ms:S2.3) together with A3 (ms:S2.2)", "statement": "d2k*/dm du = [g1*h0 - h1*(s + g0)] / [H(u)^2 (1-m)^2], which is negative under A3. Correctly derived, the model predicts a negative modularity-by-uncertainty interaction on the threshold.", "locus": "ms:S2.3; ms:A3; ms:Appendix", "entitlement": "argued", "basis": "Scorekeeper's derivation. Asserted, pending r-inst:chk:1."},
  {"@id": "r-inst:cmt:26", "kind": "consequential", "inference": "MI10 (endorsed), applied to r-inst:cmt:13", "statement": "By the authors' own account, legitimacy pressures shape sourcing decisions in this setting independently of efficiency. An institutional mechanism therefore operates on outsourcing.", "locus": "ms:S5 para 2", "entitlement": "challenged", "basis": "Avowed as interpretation only. Untested."}
 ],
 "incompatibilities": [
  {"@id": "r-inst:inc:1", "between": ["r-inst:cmt:3", "r-inst:cmt:4"], "reason": "Under A3 and the linear forms of H(u) and G(u), the cross-partial of k* is negative (r-inst:cmt:25). Proposition 2 cannot hold together with A3. Asserted, pending r-inst:chk:1."},
  {"@id": "r-inst:inc:2", "between": ["r-inst:cmt:11", "r-inst:cmt:26"], "reason": "The manuscript cannot hold that the practice's \"substance is economizing\" (ms:S6) while also explaining a main result by legitimacy pressures that retain functions independently of efficiency (ms:S5 para 2). r-inst:cmt:14 tries to dissolve this by calling the legitimacy story \"consistent with our theory\", but the model contains no such term."},
  {"@id": "r-inst:inc:3", "between": ["r-inst:cmt:10", "r-inst:cmt:22"], "reason": "This is a material incompatibility under ONT.3 (constitutive), not a formal one. ms:S5 para 1 and ms:S6 contrast 'its economics changed' with institutional diffusion. But the change in economics was itself produced by coercive field-level rules that the manuscript reports. The contrast holds only if 'institutional' is narrowed to 'mimetic', and the conclusions are not narrowed that way (ms:S5.1; ms:S6)."},
  {"@id": "r-inst:inc:4", "between": ["r-inst:cmt:12", "r-inst:cmt:17"], "reason": "If outsourcing mechanically removes in-house IT positions (r-inst:cmt:17), staffing is partly a consequence of the outcome. Conditioning on it cannot rule out capability confounding (r-inst:std:7)."},
  {"@id": "r-inst:inc:5", "between": ["r-inst:cmt:1", "r-inst:cmt:24"], "conditional": true, "reason": "If the specificity item measures effective specificity, the stated mechanism (r-inst:cmt:1) predicts mediation that ms:T2 does not show. Either the item measures nominal specificity, which the authors should say and show, or modularity works through some other channel."}
 ],
 "challenges": [
  {"@id": "r-inst:chl:1", "attachedTo": "r-inst:cmt:3", "request": "Re-derive Prop. 2 with the quotient rule, keeping H'(u). State the sign under A3."},
  {"@id": "r-inst:chl:2", "attachedTo": "r-inst:cmt:6", "request": "Derive H1 and H2 on the scale tested: Phi as a spending-weighted share of functions with k < k*. State the distribution of k across functions, and the ceiling where k* >= 1. Explain why modularity is measured over clinical systems only while Phi covers all IT functions."},
  {"@id": "r-inst:chl:3", "attachedTo": "r-inst:cmt:7", "request": "State the institutional rival in its strongest form. Cover (i) coercive and normative as well as mimetic mechanisms; (ii) imitation conditional on uncertainty (peer x uncertainty); (iii) two-stage diffusion, technical for early adopters and legitimacy-driven for later ones (Tolbert & Zucker 1983)."},
  {"@id": "r-inst:chl:4", "attachedTo": "r-inst:cmt:8", "request": "Justify the state mean of sample hospitals as the referent set. Test referent-based measures: system co-members, hospitals tied by shared vendors or executives, and large or successful hospitals (Haveman 1993; Strang & Soule 1998)."},
  {"@id": "r-inst:chl:5", "attachedTo": "r-inst:cmt:10", "request": "What interval or equivalence test supports 'rule out'? The Model 2 interval appears to include most of the Model 1 estimate (r-inst:chk:2)."},
  {"@id": "r-inst:chl:6", "attachedTo": "r-inst:cmt:9", "request": "Does lagged peer outsourcing predict a hospital's later change in modularity? If it does, modularity mediates the peer association and is a bad control for it."},
  {"@id": "r-inst:chl:7", "attachedTo": "r-inst:cmt:11", "request": "Give evidence on the consequences of outsourcing (IT cost per bed, downtime, quality), by adoption timing and modularity, in the design of Westphal, Gulati & Shortell 1997."},
  {"@id": "r-inst:chl:8", "attachedTo": "r-inst:cmt:12", "request": "Given ms:S3.2, justify the staffing control, or replace it with pre-period staffing interacted with year."},
  {"@id": "r-inst:chl:9", "attachedTo": "r-inst:cmt:13", "request": "Label the legitimacy account as a conjecture and either test it (a measure of board or community scrutiny x uncertainty) or withdraw it. Note that r-inst:cmt:25 may make it unnecessary."},
  {"@id": "r-inst:chl:10", "attachedTo": "r-inst:cmt:15", "request": "Position the paper against prior work on IT/IS outsourcing that weighs institutional and economic influences, e.g. Loh & Venkatraman 1992 (to verify) and Ang & Cummings 1997 (to verify)."},
  {"@id": "r-inst:chl:11", "attachedTo": "r-inst:cmt:18", "request": "Report the event-study coefficients, the first stage (mandate to modularity), and a heterogeneity-robust staggered estimator. Argue the exclusion restriction against a coercive-isomorphism reading of the reduced form."},
  {"@id": "r-inst:chl:12", "attachedTo": "r-inst:cmt:23", "request": "Validate CIO-reported certification against use (interface message volumes) or external certification records."},
  {"@id": "r-inst:chl:13", "attachedTo": "r-inst:cmt:24", "request": "Give the wording of the specificity item and its correlation with modularity. Report a mediation analysis."},
  {"@id": "r-inst:chl:14", "attachedTo": "r-inst:cmt:16", "request": "Add state-by-year controls (or mandate timing). Cluster standard errors by state for the state-level peer regressor."},
  {"@id": "r-inst:chl:15", "attachedTo": "ms:T2", "request": "Reconcile 4,712 observations with 412 hospitals x 11 years (4,532) and with the t-1 peer lag. Correct the *** on Model 3 uncertainty (0.084, SE 0.051)."}
 ]
}
```

## 3. Assessment by dimension (in order of weight)

Each finding names (a) the commitment, (b) the missing entitlement or the incompatibility, and (c) the repair. The JSON block at the end of §3 collects all findings in machine-readable form.

### 3.1 ONT, Ontological (weight 0.9)

**r-inst:fnd:1 — Standards are institutions. The manuscript's explanans is partly institutional. Severity: `damaging`.**
- (a) Commitment: `r-inst:cmt:10`, `r-inst:cmt:11`. "A practice that appears to spread by imitation spreads, on closer inspection, because its economics changed" (ms:S5 para 1). Institutional theory is told to "measure the economics of a practice before attributing its spread to imitation" (ms:S5.1).
- (b) Incompatibility `r-inst:inc:3`. By the manuscript's own reports, certified interfaces spread under a federal incentive programme (ms:S3.3) and staggered state requirements (ms:S4 Robustness). Under ONT.1 (fields, logics and legitimacy) and ONT.3 (constitutive), interoperability standards, certification regimes and mandates are field-level institutions. The manuscript itself says specificity is shaped by "standards that firms do not individually control" (ms:S5.1). So the account in which 'economics, not institutions' explains diffusion has an institutional cause at its root: coercive isomorphism, plausibly together with normative isomorphism through standard-setting bodies and CIO professional networks. That second part is my inference and is not in the manuscript. The opposition in the title holds only against *mimetic* isomorphism. The conclusions (ms:S5.1, ms:S6) speak of "institutional fashion" and "institutional theory" in general.
- (c) Repair: Narrow the claim to mimetic isomorphism throughout, including the title's framing, or recast it as complementary. In that version, field-level rule change (standards, certification, mandates) reconstitutes what is relationship-specific, and organizations then economize within the new rules. Then test coercive pressure separately from modularity, using mandate timing as a coercive measure, not only as an instrument.

**r-inst:fnd:2 — The measure of mimetic isomorphism does not individuate the construct. Severity: `damaging`.**
- (a) Commitment: `r-inst:cmt:8`. Peer outsourcing "captures the prevalence of the practice in the hospital's immediate field, the population to which mimetic isomorphism directs attention" (ms:S3.2).
- (b) Missing entitlement (ONT.4 moderate; `r-inst:std:3`). Mimetic isomorphism is modelling on referents *perceived as legitimate or successful* under uncertainty (DiMaggio & Powell 1983; MI3). The measure has four problems. (i) It equates the field with the state. (ii) It weights every in-state hospital equally, with no referent structure: no prestige, size, system ties or shared vendors (cf. Haveman 1993; Strang & Soule 1998; Westphal, Gulati & Shortell 1997). (iii) It counts only *sample* hospitals, which ms:S5.2 says may over-represent larger hospitals. Peers are therefore a selected subset, and state peer groups may be small, which plausibly attenuates the coefficient. This is my inference, since state cell sizes are not reported. (iv) With hospital and year fixed effects, a state-level lagged mean is identified from state-by-year variation. That is the same variation carried by the state certification mandates (ms:S4 Robustness). The variable therefore does not discriminate mimetic from coercive pressure.
- (c) Repair: Use referent-based exposure measures: system co-members, hospitals sharing the same vendor, structurally equivalent hospitals, and large or high-status hospitals. Build peer prevalence from the full hospital population if administrative data allow. Add state-by-year controls or mandate indicators. Report state cell sizes.

**r-inst:fnd:3 — The function-level model is tested at hospital level without an explicit bridge. Severity: `fixable`.**
- (a) Commitment: `r-inst:cmt:5`, `r-inst:cmt:6`. "Proposition 1 implies that hospitals with higher modularity outsource a larger share ... Proposition 2 implies that this association is stronger" (ms:S2.4).
- (b) Missing entitlement (ONT.2 same level required; `r-inst:std:4`). The propositions concern the threshold k* for single functions. The test concerns Phi, a spending-weighted aggregate. With Phi = F(k*), where F is the spending-weighted distribution of k, dPhi/dm = f(k*) dk*/dm, which is at least 0. So H1 survives aggregation, weakly. But d2Phi/dm du = f'(k*) (dk*/dm)(dk*/du) + f(k*) d2k*/dm du, and the sign depends on f'. That is a statement about how functions are distributed, which the manuscript does not give. There is also a ceiling once k* >= 1. A second mismatch: modularity is measured over *clinical information systems* (ms:S3.2), but Phi covers all functions, including hosting and help desk (ms:S2.1), which clinical interface certification plausibly does not affect.
- (c) Repair: Derive H2 on the Phi scale under a stated distribution of k, or move the test to the function level. Decompose Phi into clinical applications versus infrastructure and help desk (this links to the rival test in §5).

### 3.2 PRA, Pragmatic (weight 0.8)

**r-inst:fnd:4 — The priority claim is unchecked. Severity: `damaging` for `r-inst:ctb:5`, `fixable` for the paper. Uncertain.**
- (a) Commitment: `r-inst:cmt:15`, "the first study to adjudicate directly between transaction-cost and institutional explanations of IT outsourcing" (ms:Abstract; ms:S1).
- (b) Missing entitlement (PRA.3 always; `r-inst:std:6`). The manuscript cites no IS-outsourcing literature. I believe, but am not certain, that earlier studies modelled IT outsourcing diffusion as internal (imitative) versus external influence, or weighed institutional against economic drivers of IS outsourcing: Loh & Venkatraman 1992 (to verify); Ang & Cummings 1997 (to verify); Ang & Straub 1998 (to verify). In organization theory more broadly, several studies weigh efficiency against institutional explanations of structural diffusion, e.g. Fligstein 1985 (to verify) and Palmer, Jennings & Zhou 1993 (to verify). Westphal, Gulati & Shortell 1997, which the manuscript cites, already separates technical customization from conformity.
- (c) Repair: Delete the priority claim, or position the paper explicitly against this literature once it is verified.

**r-inst:fnd:5 — The argument is aimed at a weaker institutional theory than the one in the cited corpus. Severity: `fixable`.**
- (a) Commitment: `r-inst:cmt:7`, and the framing "institutional fashion" against "economizing" (ms:Abstract; ms:S6).
- (b) Missing entitlement (PRA.2 problematization). The manuscript's own citations do not oppose technical merit to diffusion. Tolbert & Zucker 1983 argue that early adoption tracks technical and organizational need and later adoption tracks legitimacy. Westphal et al. 1997 show early adopters customizing and later adopters conforming. The institutional-logics literature (Thornton, Ocasio & Lounsbury 2012) treats efficiency itself as a logic that is institutionalized in a field. Opposing fashion to economizing therefore adds little for an organizational-sociology readership (PRA.1). The paper's more interesting claim is `r-inst:ctb:6`: specificity is produced by standards. That is a problematization of TCE's assumption that transaction attributes are given, and it is undersold.
- (c) Repair: Reframe the contribution to institutional theory around the two-stage, technical-then-legitimacy model and test it (see `r-inst:fnd:7`). Lead with `r-inst:ctb:6`.

**r-inst:fnd:6 — The implication for practice is not entitled. Severity: `minor`.**
- (a) Commitment: `r-inst:ctb:7` (ms:S5.1).
- (b) There is no evidence that outsourcing under high modularity improved any outcome (`r-inst:cmt:11`, `r-inst:chl:7`).
- (c) Repair: Condition the advice on outcome evidence, or drop it.

### 3.3 INF, Inferential (weight 0.7)

**r-inst:fnd:7 — "Rule out mimetic isomorphism" rests on a rejected material inference, a likely bad control, and a weak form of the rival. Severity: `fatal` for the central claim (`r-inst:ctb:3`, `r-inst:ctb:4`, and the title's "Not Mimicry"). Repairable by narrowing the claim and testing it further.**
- (a) Commitment: `r-inst:cmt:10`. "The results rule out mimetic isomorphism as a driver of IT outsourcing in this setting" (ms:Abstract; ms:S5 para 1).
- (b) Missing entitlement. There are three independent problems.
  1. *MI7, which this perspective rejects.* The only evidence is that the peer coefficient is non-significant in Model 2: 0.042 (0.038) (ms:T2.M2.Peer). A normal-approximation 95% interval is about [-0.032, 0.116]. Its upper end is about 85% of the Model 1 point estimate (0.137). So the data appear compatible with a peer association of most of its unconditional size. All of this is asserted, pending `r-inst:chk:2`. 'Not significant' is not 'ruled out' (`r-inst:std:2`). The manuscript also gives no SD for the peer variable, so its effect cannot be compared in size with modularity's.
  2. *Conditioning on a possible mediator.* The manuscript reads the drop in the peer coefficient as showing that "the apparent peer effect reflects the common diffusion of standards ... not imitation" (ms:S4). That reading assumes modularity is causally upstream of the peer association. An institutional account predicts the same drop if peer outsourcing leads hospitals to adopt the vendor-favoured, certified interfaces that make outsourcing feasible (peer outsourcing at t-1, then own certification, then own outsourcing). In that case modularity is the channel through which imitation operates, and controlling for it removes the peer effect by construction. Model 2 cannot tell these structures apart (`r-inst:chl:6`).
  3. *The rival is not in its strongest form (INF.7 required; `r-inst:std:1`; INF.6: the eliminative strategy is suspect).* MI3, which this perspective endorses, says imitation happens *under uncertainty*. Yet H3 is not conditioned on uncertainty: there is no peer-by-uncertainty term, although uncertainty is measured. The canonical two-stage prediction (Tolbert & Zucker 1983) is not tested: technical predictors such as modularity should dominate among early adopters, and peer prevalence among later adopters. Only one of the three isomorphic mechanisms is considered (see `r-inst:fnd:1`).
- (c) Repair: (i) Restate the finding as "conditional on modularity, state-level lagged peer prevalence among sample hospitals is not distinguishable from zero", and report its interval. (ii) Run an equivalence test against a smallest effect size of interest, stated in advance. (iii) Test whether lagged peer outsourcing predicts later modularity, and present mediation estimates. (iv) Add peer x uncertainty, and interact peer and modularity with adoption timing or calendar period. (v) Use referent-based peer measures (`r-inst:fnd:2`). If the claim is narrowed accordingly, this finding drops to `fixable`.

**r-inst:fnd:8 — The proof of Proposition 2 omits a term. Correctly derived, the model predicts the negative interaction that was observed. Severity: `damaging`. Status: `asserted` (pending `r-inst:chk:1`).**
- (a) Commitment: `r-inst:cmt:3`, Proposition 2, d2k*/dm du > 0, proved in ms:Appendix as g1 / [H(u)(1-m)^2].
- (b) Incompatibility `r-inst:inc:1`. The proof states that "the cross-partial is determined by how the numerator responds to uncertainty" (ms:Appendix). It does not differentiate H(u) in the denominator. Differentiating dk*/dm = (s + G(u)) / [H(u)(1-m)^2] with respect to u by the quotient rule gives d2k*/dm du = [g1 H(u) - (s + G(u)) h1] / [H(u)^2 (1-m)^2]. The numerator simplifies to g1*h0 - h1*(s + g0), with the u terms cancelling. A3 (h1/h0 > g1/(s + g0)) says exactly that this is negative. **So under the manuscript's own assumption, Proposition 2 is false and the sign is reversed** (`r-inst:cmt:25`). The intuitive reading in ms:S2.3 also fails. Since dk*/dm = k*/(1-m), modularity's effect on the threshold is proportional to the threshold. Under A3, uncertainty lowers the threshold and therefore shrinks modularity's effect. Proposition 1's proof is correct as given.
- Consequences, inferred and not stated in the manuscript. (i) `r-inst:ctb:1` survives only in a corrected form. (ii) H2 is not derived. A corrected H2 would predict a negative sign on the threshold scale, though not necessarily on the Phi scale (`r-inst:fnd:3`). (iii) The negative Model 3 interaction (-0.061**) is what the corrected model predicts at the threshold level. So the post hoc legitimacy explanation in ms:S5 para 2 is not needed to reconcile model and data (`r-inst:fnd:9`). I record this even though it weakens an opening for my own tradition: the manuscript's legitimacy story is redundant, not vindicated.
- (c) Repair: Correct the proof. Restate Prop. 2: negative under A3, positive only if A3 is reversed. Re-derive on the Phi scale. Rewrite ms:S5 para 2.
- Weighting note: my perspective accepts verbal derivations (INF.3 verbal). The finding stands because a formal proof is offered and is wrong, not because a proof was required.

**r-inst:fnd:9 — Post hoc legitimacy account: unlabelled abduction, and incompatible with the economizing conclusion. Severity: `damaging`.**
- (a) Commitments: `r-inst:cmt:13`, `r-inst:cmt:14` ("This interpretation is consistent with our theory", ms:S5 para 2), and `r-inst:cmt:11` ("Its substance is economizing", ms:S6).
- (b) Incompatibility `r-inst:inc:2`. By MI10, which this perspective endorses, the authors' own interpretation commits them to legitimacy pressures that shape sourcing independently of efficiency (`r-inst:cmt:26`). The TCE model (ms:S2.2) has no legitimacy term, so the interpretation is not "consistent with" the theory in any sense stronger than 'not formally contradicted by it'. INF.1 accepts abduction *for interpretation*, but it must be labelled and kept apart from the conclusions. Here it is used to protect the conclusions. If `r-inst:fnd:8` is confirmed, the abduction is also unmotivated.
- (c) Repair: If the corrected derivation holds, withdraw the legitimacy account. Otherwise label it as a conjecture, test it (for example nonprofit or public ownership, or board composition, interacted with uncertainty), and drop "Its substance is economizing".

**r-inst:fnd:10 — "Economizing" depends on MI9, which this perspective rejects, and the specificity channel is not shown. Severity: `damaging`.**
- (a) Commitments: `r-inst:cmt:11`, the practice "is, on closer inspection, economizing" (ms:Abstract), and `r-inst:cmt:1`, standards "reduced the effective specificity" (ms:S5 para 1).
- (b) Missing entitlement (`r-inst:std:5`). (i) Going from 'outsourcing co-varies with modularity as a cost-minimizing model predicts' to 'outsourcing is economizing' assumes that observed choices are optimal responses (MI9). No cost, quality or performance consequences are measured. (ii) Mechanism. In the model, m enters buy costs only through effective specificity k(1-m) (ms:S2.2). If the specificity item ("how costly it would be to transfer the hospital's IT functions to a different provider", ms:S3.2) measures effective specificity, modularity should be largely absorbed by it, and adding modularity should move the specificity coefficient. Neither happens: modularity stays *** with specificity controlled, and the specificity coefficient goes from -0.094 to -0.091 between M1 and M2 (ms:T2). This is `r-inst:inc:5`, conditional on what the item measures. If modularity works through some other channel, that channel may be institutional: for example, certified vendors become legitimate exchange partners.
- (c) Repair: Report the item wording, the correlation of modularity with specificity, and a formal mediation analysis. Measure outcomes of outsourcing (IT cost per bed, downtime, quality) and compare them by modularity and adoption timing, as Westphal et al. 1997 did. Without this, say "consistent with an economizing account", not "is economizing".

### 3.4 EPI, Epistemological (weight 0.6)

**r-inst:fnd:11 — Single-informant measures, and possibly ceremonial certification. Severity: `fixable`.**
- (a) Commitment: `r-inst:cmt:23`. Modularity "as reported by the CIO" (ms:S3.2). Specificity is also a CIO rating, and the outsourcing share comes from the same CIO survey (ms:S3.1).
- (b) Missing entitlement (EPI.6, multi-informant preferred; MI4 endorsed). One informant supplies the outcome, the focal regressor and the main control, so common-method variance is plausible. Under MI4, a reported "certified" interface may reflect formal conformity with the incentive programme or a state mandate rather than working interoperability, in other words decoupling. If so, part of the 'modularity' coefficient could measure a hospital's responsiveness to field demands, not technical modularity. ms:S5.2 acknowledges reliance on CIO reports but does not draw this implication.
- (c) Repair: Validate modularity against external certification records or interface message volumes. Use a second informant for spending (for example finance). Test whether certified-but-low-use interfaces predict outsourcing (see §5).

**r-inst:fnd:12 — The balanced-panel requirement selects on continued survival and survey compliance. Severity: `fixable`.**
- (a) Commitment: "Hospitals were included if they responded to the survey in every year" (ms:S3.1).
- (b) Missing entitlement (EPI.3; MI10 endorsed). Hospitals that closed, merged or stopped responding are dropped. Under MI10, survival is partly a function of legitimacy. Field-embedded hospitals may also be likelier to respond every year. Both selections bear on the institutional rival. ms:S5.2 notes the possible over-representation of larger hospitals but not the survivorship issue.
- (c) Repair: Use the unbalanced panel, model attrition, and use inverse-probability weights.

**r-inst:fnd:13 — Identification and the event study: time-varying state shocks, and a reduced form that also fits coercive isomorphism. Severity: `fixable`.**
- (a) Commitments: `r-inst:cmt:16` (identification from within-hospital change; MI6, on which this perspective is neutral) and `r-inst:cmt:18` (event study "consistent with a causal effect of modularity").
- (b) Missing entitlement. Year fixed effects do not absorb state-specific timing such as the 2011-2016 mandates. Those mandates move both modularity and the state-level peer variable. The event study is a reduced form, from mandate to outsourcing. Reading it as an effect *of modularity* requires that mandates affect outsourcing only through modularity. That is not argued, and an institutional reading in which the mandate itself legitimates or prompts outsourcing predicts the same pattern. No first stage and no coefficients are reported.
- (c) Repair: Report the first stage and the event-study estimates. Discuss the exclusion restriction. Add state-by-year controls in the main models.

### 3.5 TEC, Technical (weight 0.3)

**r-inst:fnd:14 — In-house IT staffing is a bad control (Model 4). Severity: `fixable`.**
- (a) Commitment: `r-inst:cmt:12`. "If the modularity effect survives this control, it cannot be attributed to capability differences" (ms:S3.3).
- (b) Incompatibility `r-inst:inc:4` (TEC.3; `r-inst:std:7`). The manuscript says outsourcing "transfers its staff to the vendor or eliminates the positions" (ms:S3.2). Staffing is therefore partly an outcome of Phi, and conditioning on it can bias the modularity coefficient in either direction. The Model 4 robustness claim is unentitled. Models 2 and 3 do not depend on it.
- (c) Repair: Drop the claim, or control for pre-period (2009) staffing interacted with year.

**r-inst:fnd:15 — Clustering and the staggered-adoption estimator. Severity: `fixable`.**
- (a) Commitments: standard errors "clustered by hospital" (ms:S3.3) for a state-level regressor. The event study is "estimated by two-way fixed effects with leads and lags" under staggered adoption (ms:S4).
- (b) Missing entitlement (TEC.3). A state-level regressor needs state-level clustering, with a small-cluster correction if the number of states is small. That number is not reported. Clustering by state would probably widen the peer standard errors in both Model 1 and Model 2, which cuts against both sides of the H3 argument. TWFE event studies under staggered adoption can be biased when effects are heterogeneous (Goodman-Bacon 2021; Sun & Abraham 2021; Callaway & Sant'Anna 2021; all to verify).
- (c) Repair: Cluster by state (wild-cluster bootstrap if there are few clusters). Re-estimate the event study with a heterogeneity-robust estimator.

**r-inst:fnd:16 — Numerical inconsistencies in Table 2 and the sample. Severity: `minor`. Status: `asserted` (pending `r-inst:chk:2`).**
- Model 3 environmental uncertainty is reported as 0.084*** with SE 0.051. The z-ratio is about 1.65 and the two-sided p about 0.10, so the stars are inconsistent with the SE. Model 4 (0.079, SE 0.050, no stars) looks consistent.
- Observations: 412 hospitals x 11 years (2009-2019 inclusive) = 4,532, not 4,712 (ms:S3.1; ms:T2). If the t-1 peer lag drops 2009, the count would be 4,120. Either way 4,712 does not reconcile.
- Reported numbers that look consistent: 0.112 x 0.24 = 0.027 (the "2.7 percentage points"); 0.027 / 0.17 = 0.16 (about "one-sixth of a standard deviation"); (0.137 - 0.042) / 0.137 = 0.69 ("more than two-thirds"). The stars on the other cells look consistent with their SEs.
- Rhetoric: "strongly predicts" (ms:Abstract) for an effect of about one-sixth of an SD, with within R-squared 0.13. That is a presentation issue.
- Repair: Correct the table and the observation count, and temper "strongly".

**r-inst:fnd:17 — Code and data availability are not stated. Severity: `minor`.**
- TEC.1 is set to "preferred". The survey may be proprietary (inferred). Repair: state access conditions and provide code.

### 3.6 Checks for the harness

None of these checks has been run. Every finding that depends on them stays `asserted` until the harness reports.

**r-inst:chk:1 — Propositions 1 and 2 (supports `r-inst:fnd:8`, `r-inst:inc:1`, `r-inst:cmt:25`).** Expected: Prop. 1 confirmed. The cross-partial differs from the manuscript's formula, equals [g1*h0 - h1*(s+g0)] / [H^2 (1-m)^2], and is negative under A3.

```python
import sympy as sp

s, g0, g1, h0, h1, u, m = sp.symbols('s g0 g1 h0 h1 u m', positive=True)
G = g0 + g1*u
H = h0 + h1*u
kstar = (s + G) / (H*(1 - m))                      # ms:S2.3

# Proposition 1
d_m = sp.diff(kstar, m)
assert sp.simplify(d_m - (s + G)/(H*(1 - m)**2)) == 0
print("P1: dk*/dm =", sp.simplify(d_m), "(positive for m<1)")

# Proposition 2
d_mu = sp.diff(kstar, m, u)
ms_claim = g1/(H*(1 - m)**2)                       # ms:Appendix
print("P2: true cross-partial =", sp.factor(sp.simplify(d_mu)))
print("P2: true minus manuscript formula =", sp.simplify(d_mu - ms_claim))
target = (g1*h0 - h1*(s + g0)) / (H**2 * (1 - m)**2)
assert sp.simplify(d_mu - target) == 0
print("Numerator g1*h0 - h1*(s+g0) < 0  <=>  h1/h0 > g1/(s+g0)  (= A3)")

# Numeric spot-check at a point where A3 holds
vals = {s: 1, g0: 1, g1: 0.5, h0: 1, h1: 2, u: 0.7, m: 0.3}
assert vals[h1]/vals[h0] > vals[g1]/(vals[s] + vals[g0])
print("true value:", float(d_mu.subs(vals)), " manuscript formula:", float(ms_claim.subs(vals)))
```

**r-inst:chk:2 — Table 2 stars, intervals, sample size and effect sizes (supports `r-inst:fnd:7`(b)1 and `r-inst:fnd:16`).** Expected: only M3.U mismatches. M2 peer 95% CI is about [-0.032, 0.116]. 412 x 11 = 4,532, which is not 4,712.

```python
from scipy import stats

cells = {  # ms:T2: (coef, SE, reported stars)
    "M1.Peer": (0.137, 0.031, "***"), "M2.Peer": (0.042, 0.038, ""),
    "M3.Peer": (0.039, 0.037, ""),    "M4.Peer": (0.036, 0.036, ""),
    "M2.Mod":  (0.112, 0.024, "***"), "M3.Mod":  (0.118, 0.025, "***"),
    "M4.Mod":  (0.097, 0.023, "***"), "M3.U":    (0.084, 0.051, "***"),
    "M4.U":    (0.079, 0.050, ""),    "M3.MxU":  (-0.061, 0.019, "**"),
    "M4.MxU":  (-0.058, 0.019, "**"), "M1.Spec": (-0.094, 0.027, "***"),
    "M2.Spec": (-0.091, 0.027, "***"), "M3.Spec": (-0.090, 0.026, "***"),
    "M4.Spec": (-0.088, 0.026, "***"), "M4.Staff": (-0.143, 0.029, "***"),
}
def stars(p): return "***" if p < 0.001 else "**" if p < 0.01 else "*" if p < 0.05 else ""
df = 412 - 1  # hospital clusters - 1
for k, (b, se, rep) in cells.items():
    z = b / se
    p_n = 2*stats.norm.sf(abs(z)); p_t = 2*stats.t.sf(abs(z), df)
    flag = "" if stars(p_n) == rep and stars(p_t) == rep else "   <-- MISMATCH"
    print(f"{k:9s} z={z:+.2f} p_norm={p_n:.4f} p_t={p_t:.4f} reported='{rep}' implied='{stars(p_t)}'{flag}")

tcrit = stats.t.ppf(0.975, df)
for k in ("M1.Peer", "M2.Peer"):
    b, se, _ = cells[k]
    print(k, "95% CI:", round(b - tcrit*se, 3), round(b + tcrit*se, 3))
print("M2 upper bound / M1 point estimate:", round((0.042 + tcrit*0.038)/0.137, 2))
print("Obs: 412x11 =", 412*11, "| 412x10 =", 412*10, "| reported 4712 | 4712/412 =", round(4712/412, 3))
print("1-SD modularity effect:", round(0.112*0.24, 4), "| in SDs of Phi:", round(0.112*0.24/0.17, 3))
print("Peer decline M1->M2:", round((0.137 - 0.042)/0.137, 3))
for uu in (-1, 0, 1, 2):  # M3 marginal effect of modularity; u standardized
    print(f"u={uu:+d}: dPhi/dm = {0.118 - 0.061*uu:+.3f}")
```

**r-inst:chk:3 — The sign of the interaction on the Phi scale depends on the distribution of k (supports `r-inst:fnd:3`).** Parameters satisfy A3. Expected: d2Phi/dm du is negative under a uniform k, and can be positive under Beta(2,5) at some interior points. My hand calculation at m=0.1, u=5 gives about +0.06. This is asserted.

```python
from scipy import stats

s, g0, g1, h0, h1 = 1.0, 1.0, 0.5, 1.0, 2.0      # A3: h1/h0 = 2 > g1/(s+g0) = 0.25
def kstar(m, u): return (s + g0 + g1*u) / ((h0 + h1*u) * (1 - m))
def Phi(m, u, dist): return dist.cdf(min(kstar(m, u), 1.0))
def cross(m, u, dist, e=1e-4):
    return (Phi(m+e, u+e, dist) - Phi(m+e, u-e, dist)
            - Phi(m-e, u+e, dist) + Phi(m-e, u-e, dist)) / (4*e*e)

dists = {"Uniform(0,1)": stats.uniform(), "Beta(2,5)": stats.beta(2, 5), "Beta(5,2)": stats.beta(5, 2)}
for name, dist in dists.items():
    for m, u in [(0.1, 5.0), (0.1, 3.0), (0.2, 2.0), (0.3, 3.0)]:
        print(f"{name:12s} m={m} u={u} k*={kstar(m, u):.3f} d2Phi/dmdu={cross(m, u, dist):+.4f}")
```

### 3.7 Findings (machine-readable)

```json
{
 "@id": "r-inst:findings",
 "@type": "FindingSet",
 "perspective": "persp:R-INST",
 "simulated": true,
 "findings": [
  {"@id": "r-inst:fnd:1", "dimension": "ONT", "parameter": ["ONT.1", "ONT.3"], "severity": "damaging", "status": "asserted", "commitment": ["r-inst:cmt:10", "r-inst:cmt:11"], "incompatibility": "r-inst:inc:3", "locus": ["ms:S3.3", "ms:S4 Robustness", "ms:S5.1", "ms:S6"], "repair": "Narrow to mimetic isomorphism, or recast as field-level rule change enabling economizing. Test coercive pressure separately."},
  {"@id": "r-inst:fnd:2", "dimension": "ONT", "parameter": ["ONT.4"], "standard": "r-inst:std:3", "severity": "damaging", "status": "asserted", "commitment": "r-inst:cmt:8", "missingEntitlement": "State mean of sample hospitals does not track referents and shares state-by-year variation with mandates.", "locus": "ms:S3.2 Peer outsourcing", "repair": "Referent-based exposure measures; full-population peers; state-by-year controls; report cell sizes."},
  {"@id": "r-inst:fnd:3", "dimension": "ONT", "parameter": ["ONT.2"], "standard": "r-inst:std:4", "severity": "fixable", "status": "asserted", "check": "r-inst:chk:3", "commitment": ["r-inst:cmt:5", "r-inst:cmt:6"], "missingEntitlement": "No bridge from the function-level threshold to hospital-level Phi. H2 sign depends on f'(k*). Modularity measured over clinical systems only.", "locus": ["ms:S2.4", "ms:S3.2"], "repair": "Derive on the Phi scale, or test at function level; decompose Phi by function type."},
  {"@id": "r-inst:fnd:4", "dimension": "PRA", "parameter": ["PRA.3"], "standard": "r-inst:std:6", "severity": "damaging", "status": "asserted", "uncertain": true, "commitment": "r-inst:cmt:15", "missingEntitlement": "Priority claim unchecked against IS-outsourcing and efficiency-vs-institutional diffusion literatures (citations to verify).", "locus": ["ms:Abstract", "ms:S1"], "repair": "Delete or position after verification."},
  {"@id": "r-inst:fnd:5", "dimension": "PRA", "parameter": ["PRA.2", "PRA.1"], "severity": "fixable", "status": "asserted", "commitment": "r-inst:cmt:7", "missingEntitlement": "Argues against a fashion-versus-merit version of institutional theory weaker than the cited corpus.", "locus": ["ms:Abstract", "ms:S6"], "repair": "Engage the two-stage model; lead with r-inst:ctb:6."},
  {"@id": "r-inst:fnd:6", "dimension": "PRA", "parameter": ["PRA.4"], "severity": "minor", "status": "asserted", "commitment": "r-inst:cmt:11", "locus": "ms:S5.1", "repair": "Condition on outcome evidence or drop."},
  {"@id": "r-inst:fnd:7", "dimension": "INF", "parameter": ["INF.2", "INF.6", "INF.7"], "standard": ["r-inst:std:1", "r-inst:std:2"], "materialInference": {"usedByManuscript": "MI7", "stance": "rejected"}, "severity": "fatal", "severityIfNarrowed": "fixable", "status": "asserted", "check": "r-inst:chk:2", "commitment": "r-inst:cmt:10", "missingEntitlement": "Non-significance read as absence; modularity possibly a mediator of peer influence; rival not stated in strongest form.", "locus": ["ms:Abstract", "ms:S4 H3", "ms:S5 para 1", "ms:T2.M2.Peer"], "repair": "Narrow the claim; equivalence test; peer-to-modularity test and mediation; peer x uncertainty; timing heterogeneity; referent measures."},
  {"@id": "r-inst:fnd:8", "dimension": "INF", "parameter": ["INF.3"], "severity": "damaging", "status": "asserted", "check": "r-inst:chk:1", "commitment": "r-inst:cmt:3", "incompatibility": "r-inst:inc:1", "consequential": "r-inst:cmt:25", "locus": ["ms:Prop2", "ms:A3", "ms:Appendix"], "repair": "Correct the proof; restate Prop. 2 as negative under A3; re-derive on the Phi scale; revise ms:S5 para 2."},
  {"@id": "r-inst:fnd:9", "dimension": "INF", "parameter": ["INF.1", "INF.5"], "materialInference": {"usedByScorekeeper": "MI10", "stance": "endorsed"}, "severity": "damaging", "status": "asserted", "commitment": ["r-inst:cmt:13", "r-inst:cmt:14", "r-inst:cmt:11"], "incompatibility": "r-inst:inc:2", "locus": ["ms:S5 para 2", "ms:S6"], "repair": "Withdraw if r-inst:fnd:8 is confirmed; otherwise label, test, and drop 'Its substance is economizing'."},
  {"@id": "r-inst:fnd:10", "dimension": "INF", "parameter": ["INF.2"], "standard": "r-inst:std:5", "materialInference": {"usedByManuscript": "MI9", "stance": "rejected"}, "severity": "damaging", "status": "asserted", "commitment": ["r-inst:cmt:11", "r-inst:cmt:1"], "incompatibility": "r-inst:inc:5", "locus": ["ms:Abstract", "ms:S2.2", "ms:S3.2", "ms:T2.M1-M2.Spec"], "repair": "Item wording, correlation, mediation; outcome evidence; soften to 'consistent with'."},
  {"@id": "r-inst:fnd:11", "dimension": "EPI", "parameter": ["EPI.6"], "materialInference": {"usedByScorekeeper": "MI4", "stance": "endorsed"}, "severity": "fixable", "status": "asserted", "commitment": "r-inst:cmt:23", "locus": ["ms:S3.1", "ms:S3.2", "ms:S5.2"], "repair": "External validation; second informant; test certified-but-unused interfaces."},
  {"@id": "r-inst:fnd:12", "dimension": "EPI", "parameter": ["EPI.3"], "materialInference": {"usedByScorekeeper": "MI10", "stance": "endorsed"}, "severity": "fixable", "status": "asserted", "commitment": "ms:S3.1 inclusion rule", "locus": ["ms:S3.1", "ms:S5.2"], "repair": "Unbalanced panel; attrition model; IPW."},
  {"@id": "r-inst:fnd:13", "dimension": "EPI", "parameter": ["EPI.3"], "materialInference": {"usedByManuscript": "MI6", "stance": "neutral"}, "severity": "fixable", "status": "asserted", "commitment": ["r-inst:cmt:16", "r-inst:cmt:18"], "locus": ["ms:S3.3", "ms:S4 Robustness"], "repair": "First stage; event-study estimates; exclusion argument; state-by-year controls."},
  {"@id": "r-inst:fnd:14", "dimension": "TEC", "parameter": ["TEC.3"], "standard": "r-inst:std:7", "severity": "fixable", "status": "asserted", "commitment": "r-inst:cmt:12", "incompatibility": "r-inst:inc:4", "locus": ["ms:S3.2", "ms:S3.3", "ms:T2.M4"], "repair": "Drop the claim or use pre-period staffing x year."},
  {"@id": "r-inst:fnd:15", "dimension": "TEC", "parameter": ["TEC.3"], "severity": "fixable", "status": "asserted", "commitment": "ms:S3.3 clustering; ms:S4 event study", "locus": ["ms:S3.3", "ms:S4 Robustness"], "repair": "Cluster by state (wild bootstrap if few); heterogeneity-robust staggered estimator."},
  {"@id": "r-inst:fnd:16", "dimension": "TEC", "parameter": ["TEC.4"], "severity": "minor", "status": "asserted", "check": "r-inst:chk:2", "commitment": "ms:T2; ms:S3.1", "locus": ["ms:T2.M3.U", "ms:T2.Observations", "ms:S3.1"], "repair": "Correct stars and observation count; temper 'strongly'."},
  {"@id": "r-inst:fnd:17", "dimension": "TEC", "parameter": ["TEC.1"], "severity": "minor", "status": "asserted", "commitment": "none stated", "locus": "ms (no availability statement)", "repair": "State data access and share code."}
 ]
}
```

## 4. Contribution verdicts, with re-voicing (L1)

- **r-inst:ctb:1 (the formal model and two propositions): `qualified`.** Proposition 1 survives. Proposition 2 as stated fails under A3 (`r-inst:fnd:8`, pending `r-inst:chk:1`). Narrower form: "a TCE model in which modularity raises the outsourcing threshold. Under A3, its effect on the threshold *falls* with uncertainty." *Re-voiced:* when field-level standards make a function's interfaces public and rule-governed, more functions fall within the set an organization can legitimately and practically place outside its boundary. *Lost in translation:* the threshold arithmetic and the hazard-rate parameterization. My tradition has no use for k*, and so cannot say by how much.
- **r-inst:ctb:2 (testing the propositions against an institutional rival): `qualified`.** The H1 association survives as an association, and it survives the controls reported (`r-inst:cmt:5`). The 'test against an institutional rival' stands only as a test against a mimetic-only, state-mean, unconditional version of that rival (`r-inst:fnd:2`, `r-inst:fnd:7`). *Re-voiced:* hospitals that formally adopted the field's certified interface standard outsourced more IT spending. *Lost:* the claim that the adoption reflects technical modularity rather than formal conformity (`r-inst:fnd:11`), and the claim that the test discriminates between traditions.
- **r-inst:ctb:3 (peer effects disappear once modularity is measured): `qualified`.** Narrower form: "conditional on modularity, lagged state-level peer prevalence among sample hospitals is not statistically distinguishable from zero. The interval includes most of the unconditional estimate." The word "disappear" does not stand (`r-inst:fnd:7`). *Re-voiced:* the observable channel of field-level diffusion runs through the standard. *Lost:* the reading of the result as evidence *against* imitation. In my tradition the result is equally a description of how imitation travels.
- **r-inst:ctb:4 ("rule out mimetic isomorphism"; "economizing"): `fails`.** It depends on MI7 and MI9, both rejected (`r-inst:fnd:7`, `r-inst:fnd:10`). It conditions on a possible mediator. The manuscript's own explanans has coercive institutional origins (`r-inst:fnd:1`). Its own post hoc account invokes legitimacy pressure (`r-inst:fnd:9`).
- **r-inst:ctb:5 ("first study to adjudicate directly"): `qualified`, uncertain.** It stands at most as "among the studies that weigh…", pending verification of prior work (`r-inst:fnd:4`). If the candidate studies are confirmed, it fails.
- **r-inst:ctb:6 (specificity is partly a product of standards): `survives`.** It is the manuscript's strongest idea from this perspective. *Re-voiced:* transaction attributes are institutionally constituted, so what counts as 'specific' depends on the field's rules of interconnection. That is an Assimilate move, and it is one INF.6 marks as suspect for my own reasoning, so I flag it rather than lean on it. *Lost:* TCE's claim that the account stays free of institutional explanation. The re-voicing turns the paper's main contrast into a complementarity.
- **r-inst:ctb:7 (implication for practice): `qualified`.** Narrower form: "hospitals with more certified interfaces outsource more". The normative advice is not entitled without outcome evidence (`r-inst:fnd:6`).

```json
{
 "@id": "r-inst:verdicts",
 "@type": "ContributionVerdicts",
 "verdicts": [
  {"contribution": "r-inst:ctb:1", "verdict": "qualified", "narrowed": "Prop. 1 holds; under A3 the modularity effect on k* decreases in uncertainty (pending r-inst:chk:1).", "findings": ["r-inst:fnd:8"]},
  {"contribution": "r-inst:ctb:2", "verdict": "qualified", "narrowed": "H1 holds as an association; the rival tested is a weak mimetic-only form.", "findings": ["r-inst:fnd:2", "r-inst:fnd:7", "r-inst:fnd:11"]},
  {"contribution": "r-inst:ctb:3", "verdict": "qualified", "narrowed": "Conditional peer coefficient not distinguishable from zero; interval includes most of the unconditional estimate.", "findings": ["r-inst:fnd:7"]},
  {"contribution": "r-inst:ctb:4", "verdict": "fails", "findings": ["r-inst:fnd:1", "r-inst:fnd:7", "r-inst:fnd:9", "r-inst:fnd:10"]},
  {"contribution": "r-inst:ctb:5", "verdict": "qualified", "uncertain": true, "findings": ["r-inst:fnd:4"]},
  {"contribution": "r-inst:ctb:6", "verdict": "survives", "revoiced": "Transaction attributes are institutionally constituted by field-level interconnection rules.", "lostInTranslation": "TCE's independence from institutional explanation."},
  {"contribution": "r-inst:ctb:7", "verdict": "qualified", "findings": ["r-inst:fnd:6"]}
 ]
}
```

## 5. Rival explanation (L11, cross-tradition)

**The rival: the field-template bundle.** From 2009, a federal incentive programme and staggered state certification requirements (coercive pressure, ms:S3.3, ms:S4), reinforced by vendors, consultancies and CIO professional networks (normative pressure; my inference), built a new field template: the *certified, vendor-integrated hospital*. In that template, certified interfaces and outsourced IT come as one package. Hospitals adopt the package at times set by their position in the field: system membership, ties to referent hospitals, and exposure to vendors. Under this account, modularity and outsourcing co-move because they are parts of the same template, not because one lowers the cost of the other. Adding modularity absorbs the peer coefficient because certification is the leading, observable element of the package. The negative modularity-by-uncertainty interaction fits as well. Under volatile demand, the template's promise of efficiency competes with the logic of community resilience (Thornton, Ocasio & Lounsbury 2012). This is my extension of the manuscript's own ms:S5 para 2.

**Observations that would discriminate** (each with what TCE predicts and what the bundle rival predicts):
1. *Function-level incidence.* TCE predicts the modularity effect is concentrated in the clinical-application functions whose interfaces were certified, since modularity is measured over clinical systems (ms:S3.2). The bundle rival predicts that outsourcing of infrastructure hosting and help desk (ms:S2.1), which clinical interface certification plausibly does not affect, rises with modularity just as much. **This is the sharpest test, and the authors' data may already support it** if Phi can be broken down by function.
2. *Decoupling.* Under the bundle rival, interfaces that are certified but carry little traffic predict outsourcing as well as heavily used ones do. Under TCE, only interfaces in actual use lower specificity (MI4).
3. *Order of events.* TCE predicts a rise in modularity *precedes* outsourcing of the affected functions. The bundle rival predicts the two co-occur in adoption episodes, and that lagged peer outsourcing predicts *later* certification (`r-inst:chl:6`).
4. *Referent structure and timing.* The bundle rival predicts peer effects through referent ties (same system, same vendor, high-status hospitals) that are stronger under uncertainty and among later adopters (Tolbert & Zucker 1983). TCE predicts no such pattern once modularity is held fixed.
5. *Consequences.* TCE predicts IT cost savings among hospitals that outsource with high modularity, whenever they adopt. The bundle rival predicts smaller or no savings among late, conforming adopters (Westphal, Gulati & Shortell 1997).

## 6. What would change my mind

| Finding | Severity | What would lead me to withdraw it |
|---|---|---|
| `r-inst:fnd:7` | fatal | Any one of the following: (i) an equivalence test that excludes peer effects of substantive size (for example, upper bound below a third of the Model 1 estimate) under referent-based peer measures and state-clustered SEs; (ii) evidence that lagged peer outsourcing does not predict later modularity, so mediation is unlikely; (iii) no peer x uncertainty effect and no rise in peer effects among later adopters. Alternatively, narrowing the claim as in §3.3(c) drops the finding to `fixable`. |
| `r-inst:fnd:1` | damaging | Evidence that interface certification was driven mainly by hospital-level technical choice and not by the incentive programme or mandates (for example, certification well ahead of state requirements and unrelated to incentive receipt). Or a reframing that confines the contrast to mimetic isomorphism. |
| `r-inst:fnd:2` | damaging | Results that hold with referent-based exposure measures and state-by-year controls. |
| `r-inst:fnd:4` | damaging | Verification that the candidate prior studies (Loh & Venkatraman 1992; Ang & Cummings 1997; Ang & Straub 1998) do not weigh institutional against economic explanations of IT outsourcing. I am uncertain about them. |
| `r-inst:fnd:8` | damaging | A harness result from `r-inst:chk:1` showing the cross-partial is positive under A3, or a corrected model in which it is. |
| `r-inst:fnd:9` | damaging | Removal of the legitimacy account, or a test of it, together with removal of "Its substance is economizing". |
| `r-inst:fnd:10` | damaging | Outcome evidence showing cost or performance gains from outsourcing under high modularity, not limited to early adopters. Also evidence that the specificity item measures nominal specificity, or a mediation analysis showing modularity working through effective specificity. |

## 7. Recommendation (simulated): **major revision**

The H1 association is a solid, well-powered descriptive result. The idea that standards produce asset specificity (`r-inst:ctb:6`) is a real contribution that an organizational-sociology readership would value. Neither depends on the paper's headline. The headline, "Modularity, Not Mimicry", together with the claims to "rule out mimetic isomorphism" and that the practice "is economizing", does not stand from this perspective, for four reasons. It reads a non-significant coefficient as an absence (MI7, rejected). It conditions on a variable that may carry the peer influence it claims to exclude. It tests the institutional rival in a mimetic-only, unconditional, state-mean form. And it moves from fit with a cost model to efficiency without outcome evidence (MI9, rejected) (`r-inst:fnd:7`, `r-inst:fnd:10`). The manuscript's own explanans has coercive institutional origins (`r-inst:fnd:1`). Its own post hoc account of the H2 reversal invokes legitimacy (`r-inst:fnd:9`). That account is in any case unnecessary if, as I assert pending `r-inst:chk:1`, the correctly derived model predicts the negative interaction (`r-inst:fnd:8`). The repairs are feasible with the authors' data and design: narrow the claim, use function-level outcomes, run mediation and referent tests, model timing heterogeneity, and correct the proof. That is why I recommend major revision and not rejection. If the authors keep the headline claims without these analyses, this perspective would recommend rejection.

## 8. Self-location

The parameters that most drive these verdicts are:

1. **ONT.3 = constitutive, with ONT.1 including fields, logics and legitimacy.** This makes me treat standards and mandates as institutions, which drives `r-inst:fnd:1`, the re-voicing of `r-inst:ctb:6`, and the rival in §5. A reviewer with an individual-mechanistic ontology would treat modularity as an exogenous technological shock and would not count `r-inst:inc:3`.
2. **Material inferences: MI7 and MI9 rejected, MI3 and MI4 endorsed.** Rejecting MI7 makes `r-inst:fnd:7` fatal rather than minor. Rejecting MI9 makes "economizing" unentitled (`r-inst:fnd:10`). Endorsing MI3 puts the burden of proof on the authors for the Model 1 peer association. Endorsing MI4 motivates the decoupling challenge (`r-inst:fnd:11`). A reviewer who endorses MI7 or MI9 would accept the headline much more readily.
3. **INF.7 = rival-handling required, together with INF.6 eliminative = suspect.** These make the weak statement of H3 decisive. A reviewer with INF.7 = "not required" would read Model 2 as an adequate test.

## Decisions for the reviewer

1. Accept, modify or strike the derived standards `r-inst:std:1` to `r-inst:std:7`. They are not in `persp:R-INST` as configured.
2. Should `r-inst:fnd:7` stay `fatal` for the central claim, given that it drops to `fixable` if the claim is narrowed? Or would you rate the headline overclaim `damaging`?
3. Send `r-inst:chk:1` to `r-inst:chk:3` to the harness before relying on `r-inst:fnd:8`, `r-inst:fnd:3` and `r-inst:fnd:16`. All three are `asserted`.
4. Verify the literature marked "(to verify)": Loh & Venkatraman 1992, Ang & Cummings 1997, Ang & Straub 1998, Fligstein 1985, Palmer, Jennings & Zhou 1993, and the staggered-DiD papers. Keep `r-inst:fnd:4` only if they are confirmed.
5. Decide whether to put the function-level decomposition test (§5, observation 1) to the authors as the main discriminating analysis.
6. Decide how much weight this simulated institutional perspective should carry against the focal (differing) perspective, especially on `r-inst:fnd:1`, which depends on ONT.3.
7. Note that `r-inst:fnd:8` cuts against an opening for the institutional tradition: the legitimacy account becomes redundant. Decide whether to raise it in the review regardless of perspective.
8. This output is simulated and must not be sent to the authors. Confirm it is used only for panel calibration.
