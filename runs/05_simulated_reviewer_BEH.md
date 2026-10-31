# Run 05: Simulated Reviewer, Behavioral theorist (Carnegie tradition)

> **SIMULATED REVIEWER OUTPUT.** This is a simulation of a reviewer holding perspective `persp:R-BEH` (relation to focal reviewer: *differing*). It is not a review, is never sent to authors, and decides nothing. The human reviewer accepts, rejects or modifies each item.

- Instruction set: Reviewership v0.1 (23 October 2026), Role 2 (Simulated Reviewer)
- Manuscript: `ms:TEST`, "Modularity, Not Mimicry: Interoperability Standards and the Diffusion of IT Outsourcing in U.S. Hospitals"
- Lens: Behavioral theorist (Carnegie tradition). Corpus: Simon 1955; March & Simon 1958; Cyert & March 1963; Nelson & Winter 1982; Argyres 1996; Greve 2003
- Dimension order used in step 3 (by weight; ties kept in schema order): ONT 0.7, EPI 0.7, INF 0.7, PRA 0.6, TEC 0.4
- Material inferences: endorsed MI4, MI5; rejected MI2, MI7, MI9; neutral on the rest (including MI1, MI3, MI6, MI8, MI10)
- Status conventions: every formal or numerical finding is `asserted` until the harness runs the attached check (`r-beh:chk:n`). Nothing here is `demonstrated` or `refuted-by-check`.
- Basis conventions: **[MS]** marks what the manuscript says (with locus); **[INF]** marks what this scorekeeper infers from it.

---

## Step 1. Claimed contributions (Summarizer)

```json
[
 {"@id": "r-beh:ctb:1", "@type": "ClaimedContribution",
  "statement": "we formalize the link between modularity and the make-or-buy decision in a simple transaction-cost model, deriving two propositions",
  "locus": "ms:§1 para 3; ms:§2.3 (ms:Prop1, ms:Prop2); ms:Appendix"},
 {"@id": "r-beh:ctb:2", "@type": "ClaimedContribution",
  "statement": "we test these propositions against an institutional rival using a decade-long panel of hospitals",
  "locus": "ms:§1 para 3; ms:§2.4 (ms:H1, ms:H2, ms:H3); ms:T2"},
 {"@id": "r-beh:ctb:3", "@type": "ClaimedContribution",
  "statement": "once modularity is measured, the apparent peer effects that have motivated institutional accounts disappear",
  "alsoAvowedAs": "The results rule out mimetic isomorphism as a driver of IT outsourcing in this setting",
  "locus": "ms:§1 para 3; ms:Abstract; ms:§4 H3; ms:§5 para 1; title"},
 {"@id": "r-beh:ctb:4", "@type": "ClaimedContribution",
  "statement": "the boundaries of the firm respond not only to the attributes of transactions but to the technological standards that shape those attributes",
  "alsoAvowedAs": "Specificity is not a fixed property of an activity; it is partly a product of interface design",
  "locus": "ms:§5.1 sentences 1-2"},
 {"@id": "r-beh:ctb:5", "@type": "ClaimedContribution",
  "statement": "diffusion patterns that look mimetic may reflect the common adoption of efficiency-enhancing technologies",
  "alsoAvowedAs": "a sourcing practice often read as institutional fashion is, on closer inspection, economizing",
  "locus": "ms:§5.1 sentence 3; ms:Abstract; ms:§6"},
 {"@id": "r-beh:ctb:6", "@type": "ClaimedContribution",
  "statement": "the first study to adjudicate directly between transaction-cost and institutional explanations of IT outsourcing",
  "locus": "ms:Abstract (last sentence); ms:§1 para 3 (last sentence)"},
 {"@id": "r-beh:ctb:7", "@type": "ClaimedContribution",
  "statement": "hospital leaders considering outsourcing should attend first to the modularity of their systems",
  "locus": "ms:§5.1 last sentence"}
]
```

## Step 2. Scoreboard (as attributed by `persp:R-BEH`)

Commitments 1 to 20 are avowed. Commitments 21 to 28 are consequential: this scorekeeper attributes them, and names the inference used for each. Entitlement statuses are this scorekeeper's.

```json
{
 "@id": "r-beh:sb:1", "@type": "Scoreboard", "scorekeeper": "persp:R-BEH", "manuscript": "ms:TEST",
 "commitments": [
  {"@id": "r-beh:cmt:1", "kind": "avowed", "locus": "ms:§2.3",
   "content": "The hospital buys a function iff C_B < C_M, i.e. sourcing is a cost-minimizing choice made function by function.",
   "entitlement": "challenged",
   "basis": "Default inside TCE. Challenged here: ONT.5 marks choice-theoretic models suspect, and no evidence is offered on how sourcing decisions were actually made (see r-beh:chl:1)."},
  {"@id": "r-beh:cmt:2", "kind": "avowed", "locus": "ms:§2.2; ms:§1 para 2",
   "content": "Modularity m lowers effective specificity to k(1-m); m enters the model only through this term.",
   "entitlement": "deferred",
   "basis": "Cites Baldwin & Clark 2000; Langlois 2002; Sanchez & Mahoney 1996. Functional form is a modelling choice, not argued."},
  {"@id": "r-beh:cmt:3", "kind": "avowed", "locus": "ms:§2.2 Assumption A3",
   "content": "A3: h1/h0 > g1/(s+g0); hold-up hazards respond more strongly to uncertainty than in-house adaptation costs, in proportional terms.",
   "entitlement": "deferred", "basis": "Cites Williamson 1991. [INF] A3 is used in no proof in the Appendix."},
  {"@id": "r-beh:cmt:4", "kind": "avowed", "locus": "ms:Prop1; ms:Appendix",
   "content": "Proposition 1: dk*/dm > 0.",
   "entitlement": "argued", "basis": "Appendix proof. Looks correct given m<1, H>0, s+G>0; asserted pending r-beh:chk:1."},
  {"@id": "r-beh:cmt:5", "kind": "avowed", "locus": "ms:Prop2; ms:Appendix",
   "content": "Proposition 2: d2k*/dm du > 0.",
   "entitlement": "unentitled",
   "basis": "The proof differentiates as if H(u) did not depend on u (Appendix: 'determined by how the numerator responds to uncertainty'). Incompatible with cmt:3 (r-beh:inc:1). Asserted pending r-beh:chk:1."},
  {"@id": "r-beh:cmt:6", "kind": "avowed", "locus": "ms:H1; ms:T2 Models 2-4; ms:§4 H1",
   "content": "Modularity is positively associated with outsourcing share (beta1 = 0.112, SE 0.024, Model 2).",
   "entitlement": "evidenced", "basis": "ms:T2.M2-M4.Modularity. Association evidenced; causal reading challenged (chl:6)."},
  {"@id": "r-beh:cmt:7", "kind": "avowed", "locus": "ms:§2.4",
   "content": "H2 follows from Prop 2 on the scale of the outsourcing share Phi.",
   "entitlement": "challenged",
   "basis": "Passing from the threshold k* to the spending-weighted share Phi requires the curvature of the distribution of k; not stated (chl:3)."},
  {"@id": "r-beh:cmt:8", "kind": "avowed", "locus": "ms:H3; ms:§3.2 Peer outsourcing",
   "content": "H3 (lagged mean outsourcing of other sample hospitals in the same state) represents the institutional account.",
   "entitlement": "challenged",
   "basis": "Mimetic theory directs imitation at referents seen as successful or legitimate (MI3; ms:§1 para 1 says so itself); a state mean of sample hospitals is not that referent set (chl:4)."},
  {"@id": "r-beh:cmt:9", "kind": "avowed", "locus": "ms:§2.4 last para",
   "content": "Discriminating criterion: under economizing, H1 holds and the H3 association disappears once modularity is controlled; under mimicry, peers predict over and above modularity.",
   "entitlement": "challenged",
   "basis": "Not discriminating if modularity is itself a channel of peer influence or of state-level institutional pressure (chl:5)."},
  {"@id": "r-beh:cmt:10", "kind": "avowed", "locus": "ms:§3.3 para 2; ms:§4 Robustness",
   "content": "Because the modularity effect survives the in-house IT staffing control (Model 4), it cannot be attributed to capability differences.",
   "entitlement": "unentitled",
   "basis": "The manuscript itself says outsourcing transfers or eliminates IT staff (ms:§3.2), so staffing is partly an outcome (r-beh:inc:4)."},
  {"@id": "r-beh:cmt:11", "kind": "avowed", "locus": "ms:§3.3 para 1",
   "content": "Identification comes from within-hospital changes in modularity over time.",
   "entitlement": "challenged",
   "basis": "Within-hospital variation does not address reverse causation (vendors installing certified interfaces) or time-varying confounders. MI6 is neutral for this perspective and does not reach reverse causation (chl:6)."},
  {"@id": "r-beh:cmt:12", "kind": "avowed", "locus": "ms:§4 H3",
   "content": "The apparent peer effect reflects the common diffusion of standards across hospitals in the same state, not imitation.",
   "entitlement": "challenged",
   "basis": "No analysis separates diffusion of standards from imitation; the manuscript's own identifying variation for standards is state mandates (ms:§4 Robustness)."},
  {"@id": "r-beh:cmt:13", "kind": "avowed", "locus": "ms:Abstract; ms:§5 para 1",
   "content": "The results rule out mimetic isomorphism as a driver of IT outsourcing in this setting.",
   "entitlement": "unentitled",
   "basis": "Rests on a non-significant coefficient after adding a control (ms:T2.M2.Peer = 0.042, SE 0.038), i.e. on MI7, which this perspective rejects; no equivalence test."},
  {"@id": "r-beh:cmt:14", "kind": "avowed", "locus": "ms:Abstract; ms:§6 ('Its substance is economizing')",
   "content": "The spread of IT outsourcing is economizing, not institutional fashion.",
   "entitlement": "unentitled",
   "basis": "No cost, performance or hold-up outcome is measured. The step from 'fits TCE comparative statics' to 'is economizing' is MI9 (and, for persistence, MI2), both rejected here."},
  {"@id": "r-beh:cmt:15", "kind": "avowed", "locus": "ms:§5 para 2",
   "content": "The negative modularity x uncertainty interaction reflects legitimacy pressures to retain visible in-house IT under volatile demand.",
   "entitlement": "challenged",
   "basis": "Post hoc, unlabelled abductive move (INF.1); no evidence offered."},
  {"@id": "r-beh:cmt:16", "kind": "avowed", "locus": "ms:§5 para 2",
   "content": "This legitimacy interpretation is consistent with our theory.",
   "entitlement": "unentitled", "basis": "See r-beh:inc:2."},
  {"@id": "r-beh:cmt:17", "kind": "avowed", "locus": "ms:§4 Robustness",
   "content": "The staggered-mandate event study is consistent with a causal effect of modularity.",
   "entitlement": "challenged",
   "basis": "Reduced form (mandate on outsourcing); no first stage on m is reported; TWFE with staggered adoption; estimates not shown (chl:7)."},
  {"@id": "r-beh:cmt:18", "kind": "avowed", "locus": "ms:Abstract; ms:§1 para 3",
   "content": "First study to adjudicate directly between TCE and institutional explanations of IT outsourcing.",
   "entitlement": "challenged",
   "basis": "Prior work on imitative diffusion of, and institutional influence on, IT outsourcing appears to exist (chl:10; citations to verify)."},
  {"@id": "r-beh:cmt:19", "kind": "avowed", "locus": "ms:§3.2 Modularity",
   "content": "m_it, the CIO-reported share of clinical systems exchanging data through certified interfaces, measures the modularity of the model.",
   "entitlement": "challenged", "basis": "See cmt:23 (MI4) and EPI.6 (single informant)."},
  {"@id": "r-beh:cmt:20", "kind": "avowed", "locus": "ms:§3.1; ms:T2",
   "content": "Balanced panel of 412 hospitals, 2009-2019, yielding 4,712 hospital-years; Table 2 entries and significance stars as reported.",
   "entitlement": "challenged",
   "basis": "412 x 11 = 4,532, not 4,712; Model 3 uncertainty starred *** at t of about 1.65 (r-beh:inc:6; r-beh:chk:2)."}
  ,
  {"@id": "r-beh:cmt:21", "kind": "consequential", "locus": "ms:§2.2-2.3 (k*, H, G, A3)",
   "inference": "Differentiation of the manuscript's own k* (algebra, r-beh:chk:1) together with ms:A3",
   "content": "d2k*/dm du = [g1*h0 - h1*(s+g0)] / [H(u)^2 (1-m)^2]. The u-terms cancel in the numerator, so the sign is the same for every u >= 0, and A3 makes it negative. Correctly derived, the model predicts a NEGATIVE modularity x uncertainty effect on the threshold.",
   "entitlement": "argued (by this scorekeeper; asserted pending r-beh:chk:1)"},
  {"@id": "r-beh:cmt:22", "kind": "consequential", "locus": "ms:§2.3; ms:§2.4; ms:T2.M3.uncertainty",
   "inference": "From cmt:21: dk*/du = [g1*h0 - h1*(s+g0)] / [H^2 (1-m)] < 0 under A3. Phi = F(k*) with F non-decreasing, so dPhi/du <= 0.",
   "content": "The model commits the authors to uncertainty REDUCING the outsourcing share at every level of m. Table 2 Model 3 reports +0.084 (SE 0.051) at m = 0; at mean m (0.46) the implied effect is 0.084 - 0.061*0.46, about +0.056. Wrong direction, but not significant.",
   "entitlement": "challenged (tension with ms:T2; asserted pending r-beh:chk:1, r-beh:chk:2)"},
  {"@id": "r-beh:cmt:23", "kind": "consequential", "locus": "ms:§3.2 Modularity",
   "inference": "MI4 (formal adoption does not imply implementation; endorsed)",
   "content": "CIO-reported certified interfaces (formal adoption, often certified to qualify for federal incentives; see ms:§3.3) do not entail that data actually flow through them in a way that lowers switching costs. m_it may therefore be decoupled from the effective-specificity reduction that the model requires.",
   "entitlement": "challenged"},
  {"@id": "r-beh:cmt:24", "kind": "consequential", "locus": "ms:§2.3; ms:§1 para 1 ('Why did ... spread so rapidly')",
   "inference": "cmt:1 (continuous cost-minimizing re-choice) read against MI5 (adaptation by local search triggered by performance below aspiration; endorsed)",
   "content": "Because the manuscript explains sourcing change by changes in relative costs alone, it is committed to the modularity effect NOT depending on performance relative to aspiration. A Carnegie scorekeeper expects the opposite. This is a testable commitment that the manuscript has not tested.",
   "entitlement": "challenged"},
  {"@id": "r-beh:cmt:25", "kind": "consequential", "locus": "ms:§3.2 In-house IT staffing; ms:§3.3 para 2",
   "inference": "A variable mechanically caused by the outcome is a bad control (TEC.3), applied to the manuscript's own statement that outsourcing transfers or eliminates IT positions",
   "content": "Model 4 conditions on a consequence of Phi. Its estimates are not informative about capability confounding, and beta1 in Model 4 is not a total effect.",
   "entitlement": "argued (by this scorekeeper)"},
  {"@id": "r-beh:cmt:26", "kind": "consequential", "locus": "ms:§2.2 (m enters only via k(1-m)); ms:§3.2 Asset specificity; ms:T2",
   "inference": "If the specificity measure captures effective specificity (its wording is 'how costly it would be to transfer ... to a different provider', a current switching cost), the model implies beta1 = 0 conditional on it",
   "content": "The model predicts no modularity effect once effective specificity is held fixed. Table 2 shows beta1 of 0.097 to 0.118 with specificity controlled. So either the measure captures nominal k (then say so and justify), or modularity works through a channel outside the model.",
   "entitlement": "challenged"},
  {"@id": "r-beh:cmt:27", "kind": "consequential", "locus": "ms:§4 Robustness ('state requirements for certified interfaces'); ms:§1 para 1 (DiMaggio & Powell cited)",
   "inference": "The authors' own cited typology (DiMaggio & Powell 1983) classes state mandates as coercive isomorphism",
   "content": "The manuscript's identifying variation for modularity is institutional (coercive). Modularity is, at least partly, an institutionally produced condition.",
   "entitlement": "argued (by this scorekeeper from ms:§4)"},
  {"@id": "r-beh:cmt:28", "kind": "consequential", "locus": "ms:§3.3 (year fixed effects); ms:§1 para 1; ms:Abstract sentence 1",
   "inference": "Year fixed effects absorb any change common to all hospitals in a year, including the aggregate diffusion trend",
   "content": "The estimates explain within-hospital deviations from the common year path, not the field-level diffusion named as the explanandum. Bounded by beta1 = 0.112 and m in [0,1), modularity can move a hospital's share by at most about 11 pp, against an aggregate share that 'roughly doubled'.",
   "entitlement": "argued (by this scorekeeper; magnitude asserted pending r-beh:chk:3)"}
 ],
 "incompatibilities": [
  {"@id": "r-beh:inc:1", "between": ["r-beh:cmt:3", "r-beh:cmt:5"],
   "reason": "Under A3 the cross-partial of k* is negative for all u >= 0 (cmt:21). A3 and Prop 2 cannot both hold. Asserted pending r-beh:chk:1."},
  {"@id": "r-beh:inc:2", "between": ["r-beh:cmt:16", "r-beh:cmt:7"],
   "reason": "The manuscript derives H2 from its theory and reports the result as 'contrary to H2' (ms:§4), then calls a mechanism that 'our model abstracts from' (ms:§5 para 2) 'consistent with our theory'. A result cannot be both contrary to the theory's prediction and explained consistently with the theory by a mechanism outside it."},
  {"@id": "r-beh:inc:3", "between": ["r-beh:cmt:14", "r-beh:cmt:15"],
   "reason": "cmt:14 says the practice's substance is economizing, not institutional. cmt:15 says that under high uncertainty hospitals keep functions in-house for legitimacy reasons that offset economizing. The manuscript thus invokes a legitimacy mechanism (cf. MI10) to save its interaction result while denying institutional drivers elsewhere."},
  {"@id": "r-beh:inc:4", "between": ["r-beh:cmt:10", "r-beh:cmt:25"],
   "reason": "Staffing cannot both mechanically reflect outsourcing (ms:§3.2) and serve as a pre-determined confounder whose inclusion clears modularity of capability confounding (ms:§3.3)."},
  {"@id": "r-beh:inc:5", "between": ["r-beh:cmt:2", "r-beh:cmt:6"],
   "conditionalOn": "The specificity measure capturing effective specificity (cmt:26)",
   "reason": "If m acts only through k(1-m), a modularity coefficient conditional on effective specificity should be zero; Table 2 reports it positive and significant."},
  {"@id": "r-beh:inc:6", "between": ["r-beh:cmt:20 (balanced panel, 412 hospitals, 2009-2019)", "r-beh:cmt:20 (4,712 observations)"],
   "reason": "Arithmetic: 412 x 11 = 4,532. In addition, a t-1 peer measure for 2009 requires 2008 survey data that are not described. Asserted pending r-beh:chk:2."}
 ],
 "challenges": [
  {"@id": "r-beh:chl:1", "target": "r-beh:cmt:1", "request": "What evidence shows that sourcing decisions were made by comparing make and buy costs, rather than by satisficing search, vendor approach, or the CIO-CFO coalition process?"},
  {"@id": "r-beh:chl:2", "target": "r-beh:cmt:5", "request": "Re-derive Prop 2 with H'(u) = h1 included, and state what A3 is used for."},
  {"@id": "r-beh:chl:3", "target": "r-beh:cmt:7", "request": "Give the sign of the interaction on the Phi scale. d2Phi/dm du = F''(k*) k*_m k*_u + F'(k*) k*_mu, so a distributional assumption on F is needed."},
  {"@id": "r-beh:chl:4", "target": "r-beh:cmt:8", "request": "Why are same-state sample hospitals, roughly eight per state if spread evenly over 50 states [INF], the referents of mimetic isomorphism, rather than successful, prestigious, same-system or network-tied hospitals?"},
  {"@id": "r-beh:chl:5", "target": "r-beh:cmt:9", "request": "Show that modularity is not a mediator of peer influence: does lagged peer outsourcing (or peer modularity) predict a hospital's own change in m?"},
  {"@id": "r-beh:chl:6", "target": "r-beh:cmt:11", "request": "Rule out reverse causation: do increases in m precede outsourcing at the function level, or follow vendor entry?"},
  {"@id": "r-beh:chl:7", "target": "r-beh:cmt:17", "request": "Report the first stage (mandate on m), the event-study coefficients, heterogeneity-robust staggered-adoption estimates, and an argument for the exclusion restriction."},
  {"@id": "r-beh:chl:8", "target": "r-beh:cmt:13", "request": "Provide an equivalence test for the peer coefficient against a stated smallest effect of interest; non-significance is not absence."},
  {"@id": "r-beh:chl:9", "target": "r-beh:cmt:14", "request": "What measured outcome (IT cost, hold-up incidents, switching, service quality) shows that outsourcing economized?"},
  {"@id": "r-beh:chl:10", "target": "r-beh:cmt:18", "request": "Position against prior studies of imitative and institutional influence on IT outsourcing, e.g. Loh & Venkatraman 1992 and Ang & Cummings 1997 (both to verify)."},
  {"@id": "r-beh:chl:11", "target": "r-beh:cmt:24", "request": "Does the modularity effect differ between hospitals whose operating margin is below and above historical and social aspiration levels?"},
  {"@id": "r-beh:chl:12", "target": "r-beh:cmt:26", "request": "Is the specificity rating nominal or effective specificity? If effective, why does m retain an effect conditional on it?"}
 ]
}
```

## Step 3. Assessment by dimension

### 3.1 ONT, Ontological (weight 0.7)

**[INF] Summary.** The manuscript's ontology is a unitary, cost-minimizing hospital that re-optimizes each function's governance (ms:§2.3). From the Carnegie standpoint this is the main source of over-reach. The model class is choice-theoretic (ONT.5: suspect). The admissible entities that do the work in this tradition (boundedly rational decision makers, routines and capabilities, coalitions; ONT.1) are absent. The explanandum named in the Abstract and §1 is field-level diffusion, but the estimates are within-hospital deviations net of year effects (ONT.2).

```json
[
 {"@id": "r-beh:fnd:1", "@type": "Finding", "dimension": "ONT", "parameter": ["ONT.5", "ONT.1", "ONT.3"], "severity": "damaging",
  "commitment": ["r-beh:cmt:1", "r-beh:cmt:14"],
  "problem": "missingEntitlement",
  "detail": "The choice-theoretic model (buy iff C_B < C_M) is a suspect model class here. The conclusion that the practice 'is, on closer inspection, economizing' (ms:Abstract) and 'Its substance is economizing' (ms:§6) is drawn from a directional fit of comparative statics. That step is MI9 (observed structures are optimal responses), which this perspective rejects. No outcome shows economizing: no IT cost, no hold-up event, no post-outsourcing performance.",
  "repair": "(a) Narrow the claim to 'outsourcing co-varies with modularity as TCE comparative statics predict'; or (b) add outcome evidence (cost per function before and after outsourcing, contract renegotiations, switching events) and decision-process evidence for a subsample (CIO and CFO interviews, RFP records); or (c) state the model as one of several candidate decision models and test discriminating predictions (step 5).",
  "status": "n/a (interpretive)"},
 {"@id": "r-beh:fnd:2", "@type": "Finding", "dimension": "ONT", "parameter": ["ONT.2"], "severity": "damaging",
  "commitment": ["r-beh:cmt:28", "r-beh:ctb:3", "r-beh:ctb:5"],
  "problem": "missingEntitlement (cross-level bridge absent)",
  "detail": "There are three levels: function (threshold k*), hospital (share Phi) and field (diffusion, ms:Abstract sentence 1). (i) Function to hospital requires the spending-weighted distribution F of nominal k, which is never stated. (ii) Hospital to field is not bridged at all: year fixed effects absorb the common diffusion path, which is exactly where national mimetic or fashion dynamics would sit. [INF] With beta1 = 0.112 and m in [0,1), modularity can shift a hospital's share by at most about 11 pp, while the aggregate share 'roughly doubled' (ms:§1). The design does not answer 'why so rapidly after 2009'.",
  "repair": "State F and the aggregation. Decompose the 2009-2019 rise in mean Phi into beta1 x (change in mean m) and the remainder (year effects and other terms). Rescope the title, Abstract and §6 to within-hospital variation unless the decomposition shows that modularity accounts for a large part of the aggregate rise.",
  "status": "asserted (magnitude; r-beh:chk:3)"},
 {"@id": "r-beh:fnd:3", "@type": "Finding", "dimension": "ONT", "parameter": ["ONT.4"], "severity": "damaging",
  "commitment": ["r-beh:cmt:8", "r-beh:cmt:19", "r-beh:cmt:23", "r-beh:cmt:26"],
  "problem": "missingEntitlement (construct individuation)",
  "detail": "Four constructs are loosely individuated against their theories. (a) Peer outsourcing: a same-state mean of other sample hospitals is not the referent set of mimetic theory (MI3; ms:§1 para 1 itself names peers 'they regard as successful or legitimate'). The rival is thus mis-individuated, which matters most here. (b) Modularity: certified interfaces as reported by the CIO; by MI4, certification is formal adoption and may be decoupled from functional interoperability. (c) Uncertainty: volatility of inpatient admissions is demand volatility, not the TCE construct (disturbances that require adapting the IT transaction). (d) Specificity: unclear whether nominal k or effective k(1-m) (cmt:26).",
  "repair": "(a) Re-specify peers as referents (prestige, size-similar, same system, shared vendor, CIO professional networks) and report each. (b) Validate m against an external record of certified interface use (e.g. public certification or health-IT market databases; availability to verify). (c) Justify u as a TCE disturbance or add a sourcing-relevant measure (e.g. regulatory or technology change in the function). (d) Define the specificity item precisely and say which construct it measures.",
  "status": "n/a (interpretive)"}
]
```

### 3.2 EPI, Epistemological (weight 0.7)

**[INF] Summary.** The association behind H1 is well estimated and robust across specifications (ms:T2). The epistemic failures concern the claim to have ruled out the rival, which rests on MI7 (rejected), and the causal reading of the modularity coefficient, which rests on a design that does not address reverse causation. The paper's own process evidence is nil, and process-tracing is the preferred identification standard here (EPI.3).

```json
[
 {"@id": "r-beh:fnd:4", "@type": "Finding", "dimension": "EPI", "parameter": ["EPI.2", "EPI.5", "INF.2 (MI7 rejected)"], "severity": "fatal",
  "scope": "Fatal to the claim 'rule out mimetic isomorphism' (title, ms:Abstract, ms:§5 para 1, ms:§6), which the manuscript presents as central. Not fatal to H1.",
  "commitment": ["r-beh:cmt:13", "r-beh:cmt:9", "r-beh:ctb:3"],
  "problem": "missingEntitlement",
  "detail": "The inference runs: peer coefficient non-significant after adding modularity, therefore no imitation. That is MI7. [INF] The Model 2 estimate 0.042 (SE 0.038) gives a 95% CI of about [-0.032, 0.116]; the upper bound is about 85% of the Model 1 estimate (0.137). No equivalence test is reported. Separately, attenuation after conditioning on m is predicted by the institutional account too if m carries peer influence (hospitals adopting the interfaces, or the vendors, their peers adopted). Conditioning on a mediator removes the indirect mimetic path by construction.",
  "repair": "(1) Equivalence test (TOST) against a pre-stated smallest effect of interest. (2) Test peer outsourcing and peer modularity as predictors of own change in m; report a mediation decomposition. (3) Re-estimate with referent-based peer measures (fnd:3a). (4) Replace 'rule out' with an estimate-and-interval statement.",
  "status": "asserted (CI figures; r-beh:chk:2)"},
 {"@id": "r-beh:fnd:5", "@type": "Finding", "dimension": "EPI", "parameter": ["EPI.3"], "severity": "damaging",
  "commitment": ["r-beh:cmt:11", "r-beh:cmt:17"],
  "problem": "missingEntitlement",
  "detail": "(i) Reverse causation: when a hospital hands a function to a vendor, the vendor may install or certify standard interfaces as part of the transition. [INF] This is a plausible empirical conjecture, to verify in the setting. CIO-reported m would then rise because of outsourcing, and hospital fixed effects do nothing about it. (ii) The event study is reduced form (state mandate on outsourcing). No first stage on m is shown, and the exclusion restriction is unargued: mandates can also change vendor supply, compliance burden, or coercive pressure (cmt:27). (iii) TWFE with staggered adoption (2011-2016) can be biased under heterogeneous effects (Goodman-Bacon 2021; Sun & Abraham 2021; Callaway & Sant'Anna 2021; all to verify). (iv) No coefficients, figure or pre-trend test statistics are reported.",
  "repair": "Show the first stage and a 2SLS estimate with mandates as instruments for m, with the exclusion argued. Use heterogeneity-robust event-study estimators and report the full event-time coefficients. Add timing evidence at function level (does m rise before or after a function is outsourced?).",
  "status": "n/a (design argument)"},
 {"@id": "r-beh:fnd:6", "@type": "Finding", "dimension": "EPI", "parameter": ["EPI.6"], "severity": "fixable",
  "commitment": ["r-beh:cmt:19", "r-beh:cmt:20"],
  "problem": "missingEntitlement",
  "detail": "One informant (the CIO) supplies modularity and specificity, and probably the sourcing shares (ms:§3.1-3.2), so common-method variance is possible. The CIO is also an interested party in sourcing decisions (a coalition member, in Cyert & March terms). Sample selection: inclusion requires response in all 11 years (ms:§3.1). [INF] Outsourcing may itself change or remove the responding CIO role, so attrition may be selection on the outcome. ms:§5.2 acknowledges only size and resources.",
  "repair": "Validate m and Phi against non-CIO sources (finance records, external databases). Compare included hospitals with those that dropped out, especially on outsourcing before dropout. Use an unbalanced panel or bounds as a check.",
  "status": "n/a"},
 {"@id": "r-beh:fnd:7", "@type": "Finding", "dimension": "EPI", "parameter": ["EPI.5"], "severity": "fixable",
  "commitment": ["r-beh:cmt:6"],
  "problem": "overstatement",
  "detail": "'Strongly predicts' (ms:Abstract) and 'strongly and positively associated' (ms:§4) describe 2.7 pp per SD of m, about 0.16 SD of Phi (ms:§4). Within R-squared rises from 0.08 to 0.13. These are modest effects. The arithmetic itself looks right (asserted pending r-beh:chk:2).",
  "repair": "Report standardized effects with intervals; replace 'strongly' with the magnitude.",
  "status": "asserted (r-beh:chk:2)"},
 {"@id": "r-beh:fnd:8", "@type": "Finding", "dimension": "EPI", "parameter": ["EPI.4"], "severity": "none (conditional strength)",
  "commitment": ["r-beh:cmt:21"],
  "detail": "If r-beh:chk:1 confirms cmt:21, the negative interaction the authors call 'contrary to H2' follows from assumptions stated before the data (A3), at least on the threshold scale. With medium weight on novel prediction, that would count as corroboration rather than accommodation, provided the step to the Phi scale is made (fnd:10). The paper currently converts a potential success into an anomaly and patches it post hoc (fnd:11).",
  "repair": "n/a (see fnd:9 and fnd:10).",
  "status": "asserted (r-beh:chk:1)"}
]
```

### 3.3 INF, Inferential (weight 0.7)

**[INF] Summary.** The derivation of Proposition 2 is, on this scorekeeper's re-derivation, wrong, and correcting it reverses the sign. That turns the paper's "anomaly" into a prediction of its own model. The discussion then patches that anomaly with an unlabelled abductive move that imports an institutional mechanism. Rivals are stated in weak form, and the behavioral rival is absent. The justification strategy toward institutional theory is eliminative and reductive, both suspect here.

```json
[
 {"@id": "r-beh:fnd:9", "@type": "Finding", "dimension": "INF", "parameter": ["INF.3", "TEC.2 (re-derive)"], "severity": "damaging",
  "scope": "Prop 2 and H2 fail as stated. The central H1 and rival claims are unaffected, so the severity is damaging rather than fatal.",
  "commitment": ["r-beh:cmt:5", "r-beh:cmt:3"],
  "problem": "incompatibility (r-beh:inc:1)",
  "detail": "The Appendix proof of Prop 2 differentiates (s+G(u)) / (H(u)(1-m)^2) in u as if H were constant, writing the cross-partial as g1 / (H(u)(1-m)^2). Including H'(u) = h1 gives d2k*/dm du = [g1*H(u) - h1*(s+G(u))] / [H(u)^2 (1-m)^2]. The numerator equals g1*h0 - h1*(s+g0) because the g1*h1*u terms cancel. A3 (h1/h0 > g1/(s+g0)) is equivalent to h1*(s+g0) > g1*h0, so the cross-partial is negative for every u >= 0. A3 is stated but used in no proof, which suggests it was meant to sign exactly this term. Prop 1 appears correct.",
  "repair": "Correct the Appendix and restate Prop 2 with a negative sign (or drop A3 and state the condition under which each sign holds). Then H2 predicts a negative interaction, which matches ms:T2.M3. Delete the legitimacy patch (fnd:11).",
  "status": "asserted (r-beh:chk:1)"},
 {"@id": "r-beh:fnd:10", "@type": "Finding", "dimension": "INF", "parameter": ["INF.3", "INF.4"], "severity": "fixable",
  "commitment": ["r-beh:cmt:7"],
  "problem": "missingEntitlement (sign on the tested scale)",
  "detail": "H2 is tested as a linear interaction on Phi, but Prop 2 concerns k*. Since Phi = F(k*) with F the spending-weighted CDF of nominal k, d2Phi/dm du = F''(k*) k*_m k*_u + F'(k*) k*_mu. Under A3, k*_m > 0, k*_u < 0 and k*_mu < 0. The sign on Phi is therefore negative if F is linear or convex at k*, and ambiguous if F is concave there. Corner cases (k* >= 1, all functions bought) also need handling. The same gap applies to the positive-sign version the authors state.",
  "repair": "State an assumption on F (or bound its curvature with the function-level data) and derive the sign on the Phi scale; or test at the function level, where the threshold is observed more directly.",
  "status": "asserted (r-beh:chk:1, part c)"},
 {"@id": "r-beh:fnd:11", "@type": "Finding", "dimension": "INF", "parameter": ["INF.1", "INF.6"], "severity": "damaging",
  "commitment": ["r-beh:cmt:15", "r-beh:cmt:16", "r-beh:cmt:14"],
  "problem": "incompatibility (r-beh:inc:2, r-beh:inc:3) and unlabelled abduction",
  "detail": "The legitimacy-signalling account (ms:§5 para 2) is introduced after the result, is untested, and is not labelled as conjecture. It conflicts with the paper's other commitments twice: it is called 'consistent with our theory' although the theory predicted the opposite sign (as the authors derived it), and it brings in a legitimacy mechanism while the paper claims to have set institutional drivers aside. [INF] If fnd:9 holds, the patch is also unnecessary.",
  "repair": "Delete it, or label it as an abductive conjecture with a test that discriminates it from the corrected TCE prediction and from the behavioral slack account (step 5), for example contrasts by ownership or board composition.",
  "status": "n/a"},
 {"@id": "r-beh:fnd:12", "@type": "Finding", "dimension": "INF", "parameter": ["INF.7"], "severity": "damaging",
  "commitment": ["r-beh:cmt:8", "r-beh:cmt:9", "r-beh:cmt:12"],
  "problem": "missingEntitlement (rival not in strongest form; test not discriminating)",
  "detail": "Only one institutional mechanism (mimetic) is stated, in a weak operationalization. The coercive pathway (state mandates, which the manuscript itself uses: cmt:27) and the normative pathway (CIO professional networks) are not stated. The criterion in ms:§2.4 is not discriminating, because attenuation of the peer term is predicted under mimicry-through-modularity and under coercive diffusion of standards. The manuscript's own reading ('common diffusion of standards across hospitals in the same state', ms:§4) is an institutional diffusion story. No behavioral or capability rival is considered, although Argyres 1996 (to verify) shows capabilities shaping make-or-buy beyond transaction attributes.",
  "repair": "State each rival in its strongest form and derive predictions that differ. TCE: newly outsourced functions are those whose nominal k lies between the old and new thresholds. Mimicry: hospitals outsource the same functions their referents outsourced, whatever k. Behavioral: outsourcing follows below-aspiration performance (step 5).",
  "status": "n/a"},
 {"@id": "r-beh:fnd:13", "@type": "Finding", "dimension": "INF", "parameter": ["INF.6", "INF.5"], "severity": "fixable",
  "commitment": ["r-beh:cmt:13", "r-beh:cmt:14", "r-beh:ctb:5"],
  "problem": "suspect justification strategy",
  "detail": "Toward institutional theory the paper is eliminative ('rule out', ms:Abstract) and reductive ('what spreads is not a practice but the conditions that make it efficient', ms:§6). Both strategies are suspect under this perspective. [INF] The paper's own material supports an assimilative reading: standards, produced partly by coercive mandates and field-level standard-setting, changed the opportunity set and the economics of sourcing. The two accounts are then complements at different levels, not rivals.",
  "repair": "Reframe the contribution assimilatively: institutional processes produced the interface standards, which changed the economics and search costs of sourcing. Say which part of the variance each level accounts for.",
  "status": "n/a"},
 {"@id": "r-beh:fnd:14", "@type": "Finding", "dimension": "INF", "parameter": ["INF.5 (depth)", "INF.4"], "severity": "damaging",
  "commitment": ["r-beh:cmt:2", "r-beh:cmt:6", "r-beh:cmt:26"],
  "problem": "missingEntitlement (mechanism not traced) and conditional incompatibility (r-beh:inc:5)",
  "detail": "The chain from modularity to lower effective specificity to lower hold-up exposure to outsourcing is asserted, not traced. Hold-up exposure is never observed. [INF] The one mechanism-proximate measure, specificity, does not absorb the modularity effect: modularity stays sizeable and significant with specificity controlled in every model (ms:T2.M2-M4). Also, the specificity coefficient barely moves when modularity enters (-0.094 to -0.091, ms:T2.M1-M2). If m worked through effective specificity, the two should be correlated within hospitals and that coefficient should shift. Both observations suggest modularity works through a channel the model omits. Candidates include search costs, vendor availability, or erosion of in-house capability.",
  "repair": "Test mediation through specificity, with specificity measured as nominal k and as effective switching cost. Add direct evidence on hold-up (renegotiation, price escalation, switching) by modularity level.",
  "status": "n/a"}
]
```

### 3.4 PRA, Pragmatic (weight 0.6)

**[INF] Summary.** For a generalist organization-science readership the framing has the "interesting" form in Davis's sense: what looks like fashion is shown to be economizing. That is a real strength. But it rests on a two-way contest that omits the behavioral account, and the placement claim looks unsafe.

```json
[
 {"@id": "r-beh:fnd:15", "@type": "Finding", "dimension": "PRA", "parameter": ["PRA.3"], "severity": "fixable",
  "commitment": ["r-beh:cmt:18", "r-beh:ctb:6"],
  "problem": "missingEntitlement (priority)",
  "detail": "'First study to adjudicate directly' appears to be contradicted by earlier work on the diffusion of IT outsourcing that contrasted imitative ('Kodak effect') with other influences (Loh & Venkatraman 1992, Information Systems Research; to verify) and by work on institutional influences on IS outsourcing decisions (Ang & Cummings 1997, Organization Science; to verify).",
  "repair": "Drop or qualify the priority claim and position against these studies.",
  "status": "n/a (citations to verify)"},
 {"@id": "r-beh:fnd:16", "@type": "Finding", "dimension": "PRA", "parameter": ["PRA.2"], "severity": "minor",
  "commitment": ["r-beh:ctb:4", "r-beh:ctb:5"],
  "problem": "contribution narrower than claimed",
  "detail": "Strength: the denial of an assumed institutional reading fits PRA.2. Qualification: ctb:4 ('specificity ... is partly a product of interface design') is anticipated by the works the manuscript cites (Langlois 2002; Sanchez & Mahoney 1996; Baldwin & Clark 2000). The new part is the empirical demonstration in hospitals. For this readership, the assimilative framing (fnd:13) would be more interesting than the eliminative one.",
  "repair": "Claim the empirical demonstration and the cross-level account of how standards reshape sourcing; drop the claim of conceptual novelty for ctb:4.",
  "status": "n/a"},
 {"@id": "r-beh:fnd:17", "@type": "Finding", "dimension": "PRA", "parameter": ["PRA.4"], "severity": "minor",
  "commitment": ["r-beh:ctb:7"],
  "problem": "overreach",
  "detail": "The advice that leaders 'attend first to the modularity of their systems' (ms:§5.1) presumes both a causal effect and that outsourcing is beneficial. Neither is established (fnd:1, fnd:5).",
  "repair": "Condition the advice on the causal and outcome evidence, or drop it.",
  "status": "n/a"}
]
```

### 3.5 TEC, Technical (weight 0.4)

**[INF] Summary.** Estimation is conventional, with specific problems: a bad control presented as a robustness test, clustering at the wrong level for the state-level regressors, internal numerical inconsistencies, and unreported event-study output.

```json
[
 {"@id": "r-beh:fnd:18", "@type": "Finding", "dimension": "TEC", "parameter": ["TEC.3"], "severity": "damaging",
  "commitment": ["r-beh:cmt:10", "r-beh:cmt:25"],
  "problem": "incompatibility (r-beh:inc:4); bad control",
  "detail": "In-house IT staffing is, by the manuscript's own account, reduced by outsourcing (ms:§3.2). Model 4 conditions on an outcome. The claim that the modularity effect 'cannot be attributed to capability differences' (ms:§3.3; ms:§4) is unentitled. [INF] Asset specificity (a CIO-rated switching cost) may also be post-treatment, since outsourcing changes switching costs.",
  "repair": "Measure capability before treatment (e.g. 2009 staffing, or staffing lagged several years, interacted with year), or use capability indicators unaffected by sourcing. Drop the capability claim unless such a test supports it. Show results with and without the specificity control.",
  "status": "n/a (design argument)"},
 {"@id": "r-beh:fnd:19", "@type": "Finding", "dimension": "TEC", "parameter": ["TEC.3"], "severity": "fixable",
  "commitment": ["r-beh:cmt:8", "r-beh:cmt:17"],
  "problem": "inference level",
  "detail": "Standard errors are clustered by hospital (ms:§3.3), but the peer measure and the mandates vary at state level. Peer means built from few hospitals per state are noisy, which biases the peer coefficient toward zero and so works in the authors' favour. Peer-effect identification also faces the reflection problem (Manski 1993; to verify).",
  "repair": "Cluster by state (wild cluster bootstrap if states are few); report the number of sample hospitals per state; correct for, or bound, measurement error in the peer mean.",
  "status": "n/a"},
 {"@id": "r-beh:fnd:20", "@type": "Finding", "dimension": "TEC", "parameter": ["TEC.4"], "severity": "fixable",
  "commitment": ["r-beh:cmt:20"],
  "problem": "numerical inconsistency (r-beh:inc:6)",
  "detail": "(i) N = 4,712 versus 412 x 11 = 4,532 for a balanced 2009-2019 panel; a t-1 peer measure for 2009 also needs 2008 data. (ii) Model 3 'Environmental uncertainty' 0.084 (0.051) is starred *** but t is about 1.65 (p about 0.10); the Model 4 entry 0.079 (0.050) is unstarred, which is consistent. (iii) The other stars, the 2.7 pp effect, 'about one-sixth of a standard deviation' and the 'more than two-thirds' fall in the peer coefficient (about 69%) appear consistent. All asserted pending the check.",
  "repair": "Reconcile N with the panel description and the lag structure, and correct the stars.",
  "status": "asserted (r-beh:chk:2)"},
 {"@id": "r-beh:fnd:21", "@type": "Finding", "dimension": "TEC", "parameter": ["TEC.4", "TEC.5"], "severity": "fixable",
  "commitment": ["r-beh:cmt:22"],
  "problem": "model-data tension",
  "detail": "Under A3 the model implies dPhi/du < 0 at every m (cmt:22). Table 2 shows a positive (non-significant) uncertainty main effect, and a positive implied effect at mean m (about +0.056).",
  "repair": "Report the marginal effect of u across the range of m with intervals, and discuss it against the corrected model.",
  "status": "asserted (r-beh:chk:1, r-beh:chk:2)"},
 {"@id": "r-beh:fnd:22", "@type": "Finding", "dimension": "TEC", "parameter": ["TEC.1", "TEC.2"], "severity": "fixable",
  "commitment": ["r-beh:cmt:17"],
  "problem": "reproducibility",
  "detail": "Event-study and robustness estimates are described but not shown (ms:§4 Robustness). Neither data access (a proprietary-looking survey) nor code is stated. Re-running is not possible from the manuscript.",
  "repair": "Report all robustness tables and event-time coefficients with intervals; state data access and post code.",
  "status": "n/a"}
]
```

### 3.6 Checks for the harness

None of these checks has been run. Every finding that depends on one stays `asserted`.

```json
[
 {"@id": "r-beh:chk:1", "@type": "Check", "targets": ["ms:Prop1", "ms:Prop2", "ms:A3", "r-beh:cmt:21", "r-beh:cmt:22", "r-beh:fnd:9", "r-beh:fnd:10", "r-beh:fnd:21"], "language": "python", "libraries": ["sympy", "numpy"], "status": "not-run",
  "settles": "(a) the Prop 1 expression; (b) whether the Appendix cross-partial is correct, and the sign of the true cross-partial and of dk*/du under A3; (c) the decomposition of the cross-partial on the Phi scale."},
 {"@id": "r-beh:chk:2", "@type": "Check", "targets": ["ms:T2", "ms:§3.1", "ms:§4", "r-beh:inc:6", "r-beh:fnd:4", "r-beh:fnd:7", "r-beh:fnd:20"], "language": "python", "libraries": ["numpy", "scipy"], "status": "not-run",
  "settles": "Star consistency (t with 411 df, clusters minus one), N arithmetic, effect-size arithmetic, the peer CI, and the implied effect of u at mean m. Caveat: published coefficients are rounded to 3 decimals, so near-threshold cases are indicative only."},
 {"@id": "r-beh:chk:3", "@type": "Check", "targets": ["r-beh:cmt:28", "r-beh:fnd:2"], "language": "python", "libraries": ["pandas"], "status": "not-run (requires authors' data)",
  "settles": "Share of the 2009-2019 rise in mean outsourcing share attributable to beta1 x change in mean modularity."},
 {"@id": "r-beh:chk:4", "@type": "Check", "targets": ["r-beh:cmt:24", "r-beh:chl:11", "step 5 rival"], "language": "python", "libraries": ["pandas", "statsmodels"], "status": "not-run (requires authors' data)",
  "settles": "Whether the modularity effect is moderated by performance relative to aspiration (the discriminating test in step 5)."}
]
```

**r-beh:chk:1** (derivation)

```python
import numpy as np
import sympy as sp

s, g0, g1, h0, h1, u = sp.symbols('s g0 g1 h0 h1 u', positive=True)
m = sp.symbols('m', real=True)
G = g0 + g1*u
H = h0 + h1*u
kstar = (s + G) / (H*(1 - m))            # ms:§2.3

k_m  = sp.diff(kstar, m)
k_u  = sp.diff(kstar, u)
k_mu = sp.diff(kstar, m, u)

# (a) Prop 1: Appendix expression for dk*/dm
print("(a) Prop1 expression matches:", sp.simplify(k_m - (s + G)/(H*(1 - m)**2)) == 0)

# (b) Prop 2: Appendix expression g1/(H(1-m)^2)
print("(b) Appendix Prop2 expression matches:", sp.simplify(k_mu - g1/(H*(1 - m)**2)) == 0)
num_mu = sp.simplify(k_mu * H**2 * (1 - m)**2)
num_u  = sp.simplify(k_u  * H**2 * (1 - m))
target = g1*h0 - h1*(s + g0)
print("    numerator of k_mu:", sp.expand(num_mu))
print("    k_mu numerator == g1*h0 - h1*(s+g0):", sp.simplify(num_mu - target) == 0)
print("    k_u  numerator == g1*h0 - h1*(s+g0):", sp.simplify(num_u - target) == 0)
# A3: h1/h0 > g1/(s+g0)  <=>  h1*(s+g0) > g1*h0  <=>  target < 0 (all parameters positive)

# (b') numerical spot-check on random parameter draws satisfying A3
rng = np.random.default_rng(20261023)
N = 200000
S, G0, G1, H0, H1 = (rng.uniform(0.01, 5, N) for _ in range(5))
U = rng.uniform(0, 10, N); M = rng.uniform(0, 0.99, N)
a3 = H1/H0 > G1/(S + G0)
f_kmu = sp.lambdify((s, g0, g1, h0, h1, u, m), k_mu, 'numpy')
f_ku  = sp.lambdify((s, g0, g1, h0, h1, u, m), k_u, 'numpy')
v_mu = f_kmu(S, G0, G1, H0, H1, U, M); v_u = f_ku(S, G0, G1, H0, H1, U, M)
print("(b') A3 draws:", int(a3.sum()),
      "| share k_mu<0:", float((v_mu[a3] < 0).mean()),
      "| share k_u<0:", float((v_u[a3] < 0).mean()))
print("     non-A3 draws: share k_mu>0:", float((v_mu[~a3] > 0).mean()))

# (c) Phi scale: Phi = F(k*), F = spending-weighted CDF of nominal k
x = sp.Symbol('x')
F = sp.Function('F')
Phi_mu = sp.diff(F(kstar), m, u)
decomp = (sp.diff(F(x), x, 2).subs(x, kstar) * k_m * k_u
          + sp.diff(F(x), x).subs(x, kstar) * k_mu)
print("(c) Phi_mu == F''(k*) k_m k_u + F'(k*) k_mu:", sp.simplify((Phi_mu - decomp).doit()) == 0)
# Uniform F on [0,1], interior k*: Phi = k*, so Phi_mu = k_mu (negative under A3)
```

Expected if this scorekeeper is right: (a) True; (b) False, with both numerators equal to `g1*h0 - h1*(s+g0)`; (b') shares equal to 1.0 under A3 and to 1.0 for k_mu > 0 outside A3; (c) True.

**r-beh:chk:2** (Table 2 and text arithmetic)

```python
from scipy import stats

rows = {  # (coef, se, reported stars), ms:T2
 "M1 peer": (0.137, 0.031, "***"), "M2 peer": (0.042, 0.038, ""),
 "M3 peer": (0.039, 0.037, ""),    "M4 peer": (0.036, 0.036, ""),
 "M2 mod":  (0.112, 0.024, "***"), "M3 mod":  (0.118, 0.025, "***"), "M4 mod": (0.097, 0.023, "***"),
 "M3 unc":  (0.084, 0.051, "***"), "M4 unc":  (0.079, 0.050, ""),
 "M3 mxu":  (-0.061, 0.019, "**"), "M4 mxu":  (-0.058, 0.019, "**"),
 "M1 spec": (-0.094, 0.027, "***"), "M2 spec": (-0.091, 0.027, "***"),
 "M3 spec": (-0.090, 0.026, "***"), "M4 spec": (-0.088, 0.026, "***"),
 "M4 staff": (-0.143, 0.029, "***"),
}
df = 412 - 1
def stars(p): return "***" if p < 0.001 else "**" if p < 0.01 else "*" if p < 0.05 else ""
for k, (b, se, rep) in rows.items():
    t = b/se; p = 2*stats.t.sf(abs(t), df)
    print(f"{k:9s} t={t:6.2f} p={p:.4f} implied={stars(p):3s} reported={rep:3s}",
          "OK" if stars(p) == rep else "MISMATCH")
print("Balanced N 412 x 11 =", 412*11, "| reported 4712 | 4712/412 =", round(4712/412, 3))
print("Effect 0.112*0.24 =", 0.112*0.24, "| in SD of Phi:", round(0.112*0.24/0.17, 3))
print("Peer fall M1->M2:", round((0.137 - 0.042)/0.137, 3), "(claim: > 2/3 =", round(2/3, 3), ")")
c = stats.t.ppf(0.975, df)
lo, hi = 0.042 - c*0.038, 0.042 + c*0.038
print("M2 peer 95% CI:", (round(lo, 3), round(hi, 3)), "| upper / M1 coef:", round(hi/0.137, 3))
print("Implied u effect at mean m (M3):", round(0.084 - 0.061*0.46, 3))
print("Max within-hospital shift from m (M2, m 0->1):", 0.112)
```

Expected if this scorekeeper is right: one MISMATCH (M3 unc); N 4,532 versus 4,712; effect about 0.027 (0.158 SD); fall about 0.693; CI about (-0.033, 0.117), upper bound about 0.85 of the M1 coefficient; implied u effect about +0.056.

**r-beh:chk:3** (diffusion decomposition; needs the authors' panel)

```python
import pandas as pd

def decompose(panel: pd.DataFrame, beta1: float = 0.112) -> dict:
    """panel columns: hospital, year, Phi, m (ms:§3.2 definitions)."""
    g = panel.groupby("year")[["Phi", "m"]].mean()
    dPhi = g.loc[2019, "Phi"] - g.loc[2009, "Phi"]
    dm = g.loc[2019, "m"] - g.loc[2009, "m"]
    return {"dPhi": dPhi, "dm": dm, "beta1_dm": beta1*dm, "share_explained": beta1*dm/dPhi}
# Manuscript-only bound: beta1*dm <= 0.112, since m lies in [0,1).
```

**r-beh:chk:4** (aspiration moderation; needs the authors' panel)

```python
import statsmodels.formula.api as smf

def aspiration_test(panel):
    """panel: Phi, m, u, peer_lag, spec, margin, margin_lag1, state_margin_lag1, controls, hospital, year, state.
    Aspiration form follows Greve 2003 (to verify); weights are illustrative."""
    p = panel.sort_values(["hospital", "year"]).copy()
    p["aspiration"] = 0.5*p.groupby("hospital")["margin"].shift(2) + 0.5*p["state_margin_lag1"]
    p = p.dropna(subset=["aspiration", "margin_lag1"])
    p["below"] = (p["margin_lag1"] < p["aspiration"]).astype(int)
    f = "Phi ~ m*below + u + m:u + peer_lag + spec + C(hospital) + C(year)"  # add ms:§3.2 controls by name
    return smf.ols(f, data=p).fit(cov_type="cluster", cov_kwds={"groups": p["state"]})
# Behavioral rival predicts coef on m:below > 0 and m alone near 0; TCE (cmt:24) predicts m:below about 0.
```

---

## Step 4. Contribution verdicts, with re-voicing (L1)

```json
[
 {"@id": "r-beh:vrd:1", "contribution": "r-beh:ctb:1", "verdict": "qualified",
  "narrowerForm": "A transaction-cost model in which modularity raises the outsourcing threshold (Prop 1). Under the manuscript's own A3, uncertainty WEAKENS the modularity effect on the threshold (corrected Prop 2, pending r-beh:chk:1).",
  "why": "Prop 2 as stated fails (r-beh:fnd:9). The step to the Phi scale is not made (r-beh:fnd:10).",
  "reVoiced": "Interface standards cut the cost of searching for, evaluating and switching to outside suppliers. More external alternatives come within a hospital's evoked set (March & Simon 1958), and buying becomes a 'nearby' solution in local search.",
  "lostInTranslation": "The hold-up mechanism and the optimizing threshold. In the behavioral re-voicing, modularity changes which alternatives are considered, not which one is optimal."},
 {"@id": "r-beh:vrd:2", "contribution": "r-beh:ctb:2", "verdict": "qualified",
  "narrowerForm": "A test of H1 with a lagged same-state peer control, not an adjudication between TCE and institutional theory.",
  "why": "The rival is mis-individuated and the test does not discriminate (r-beh:fnd:3, r-beh:fnd:12).",
  "reVoiced": "Evidence that within-hospital changes in interface standardization go together with changes in sourcing.",
  "lostInTranslation": "The framing as a contest won."},
 {"@id": "r-beh:vrd:3", "contribution": "r-beh:ctb:3", "verdict": "fails",
  "narrowerForm": "(What survives) Conditional on CIO-reported modularity, the lagged same-state peer coefficient is smaller (0.137 to 0.042) and imprecisely estimated (95% CI includes about 85% of the unconditional estimate).",
  "why": "'Disappear' and 'rule out' rest on MI7 (rejected) and on conditioning on a possible mediator (r-beh:fnd:4). The paper's own account of the attenuation ('common diffusion of standards' through state mandates) is institutional (r-beh:cmt:27).",
  "reVoiced": "n/a (fails as claimed)", "lostInTranslation": "n/a"},
 {"@id": "r-beh:vrd:4", "contribution": "r-beh:ctb:4", "verdict": "qualified",
  "narrowerForm": "An empirical demonstration in U.S. hospitals that sourcing co-varies with interface standardization, consistent with specificity being partly a product of interface design.",
  "why": "The conceptual point is anticipated by the cited literature (r-beh:fnd:16). Whether the effect runs through specificity is untested and doubtful (r-beh:fnd:14).",
  "reVoiced": "Field-level standards codify the interfaces between routines (cf. codification and replication of routines, Nelson & Winter 1982). Codified routines can be moved across organizational boundaries, so boundaries shift as routines are codified.",
  "lostInTranslation": "The claim that the shift is economizing. In the routines account, boundaries move because codification makes transfer feasible, whether or not it is efficient."},
 {"@id": "r-beh:vrd:5", "contribution": "r-beh:ctb:5", "verdict": "qualified",
  "narrowerForm": "Researchers should model how a practice's opportunity set and economics changed before attributing its spread to imitation.",
  "why": "The paper does not measure the economics itself (no cost or outcome data; r-beh:fnd:1). The 'efficiency-enhancing' reading depends on MI9 and MI2, both rejected.",
  "reVoiced": "Before attributing spread to imitation, trace the change in the set of available alternatives and the search that found them.",
  "lostInTranslation": "'Efficiency-enhancing'. The behavioral re-voicing claims only that feasible alternatives changed."},
 {"@id": "r-beh:vrd:6", "contribution": "r-beh:ctb:6", "verdict": "fails (provisional; citations to verify)",
  "why": "Earlier studies appear to address imitative and institutional influences on IT outsourcing (r-beh:fnd:15). If verification shows otherwise, the verdict becomes 'qualified'.",
  "reVoiced": "n/a", "lostInTranslation": "n/a"},
 {"@id": "r-beh:vrd:7", "contribution": "r-beh:ctb:7", "verdict": "qualified",
  "narrowerForm": "If modularity causally raises outsourcing, and outsourcing improves outcomes, leaders weighing outsourcing should assess interface standardization first.",
  "why": "Both conditions are unestablished (r-beh:fnd:17).",
  "reVoiced": "Interface standardization widens the set of sourcing alternatives managers will consider.",
  "lostInTranslation": "The prescriptive force."}
]
```

## Step 5. Rival explanation (L11, from the Carnegie tradition) and model re-specification (L12)

**Rival (L11): problemistic search with solution availability.** [INF throughout; not a claim about what happened.] After 2009 the federal incentive programme for electronic health records (ms:§3.3) loaded hospitals with implementation work, cost and compliance demands. Hospitals whose operating performance fell below aspiration (own history and social comparison) launched problemistic search (Cyert & March 1963; Greve 2003). That search was local: it examined alternatives near current practice. Hospitals that had already installed certified interfaces, often for the same programme, had certified vendors and vendor-ready options close at hand, so outsourcing was a nearby alternative and was the one adopted. Modularity, on this account, indexes how close the outsourcing alternative sits in search space and how much vendor attention the hospital receives, not a reduction in hold-up hazard. A capability strand reinforces it: as clinical IT grew more complex, in-house routines fell behind, and hospitals bought where they lacked capability (Argyres 1996; to verify). Same-state peers share mandates, vendors and social aspiration referents, so the peer coefficient falls once modularity enters.

The same account offers its own explanation of the negative interaction. Volatile admissions absorb managerial attention in short-term firefighting and raise the value of organizational slack (Cyert & March 1963). In-house IT staff serve as a buffer, so search for structural change, and hence outsourcing, is damped where volatility is high. This is a third explanation, distinct from the corrected TCE sign (r-beh:cmt:21) and from the authors' legitimacy patch (r-beh:cmt:15).

**Re-specification (L12, causal / boundedly rational model class).**

```json
{
 "@id": "r-beh:alt:1", "@type": "RivalModel", "modelClass": "causal (boundedly rational search)",
 "specification": [
  "Each year, hospital i reconsiders the sourcing of function j with probability pi_it = lambda0 + lambda1 * 1[margin_i,t-1 < aspiration_it] (problemistic search trigger; MI5).",
  "If triggered, it evaluates alternatives in order of proximity and adopts the first that meets aspiration (satisficing; Simon 1955).",
  "The probability that 'buy' is evoked and satisfices rises with m_it (vendor-ready interfaces), with the share of social referents that outsourced (vicarious learning), and falls with in-house capability relative to the function's demands.",
  "Volatility u_it lowers lambda1 (attention absorbed) and raises the value of in-house slack."
 ],
 "predictions": [
  "P1: the effect of m is concentrated among hospitals below aspiration; near zero above it.",
  "P2: outsourcing events cluster in the one to two years after negative performance feedback.",
  "P3: functions outsourced are those with salient recent problems (backlogs, failed go-lives), whatever their nominal specificity.",
  "P4: insourcing reversals follow below-aspiration performance of the vendor arrangement.",
  "P5: negative m x u interaction (shared with the corrected TCE model)."
 ]
}
```

**Discriminating observation.** The single most discriminating test is whether performance relative to aspiration moderates the modularity effect (r-beh:chk:4). The manuscript's account, through r-beh:cmt:24, predicts that `m x below-aspiration` is about zero, since costs drive sourcing whatever the performance feedback. The behavioral rival predicts it is positive, with the main effect of m near zero above aspiration. A second discriminator works at function level: TCE predicts that newly outsourced functions have nominal specificity between the old and the new threshold, while the behavioral rival predicts that problem salience, not specificity, selects them. A third discriminator applies to the negative interaction: the slack account predicts it is stronger where slack is low (thin margins), the legitimacy account predicts it is stronger in non-profit and community-governed hospitals, and the corrected TCE account predicts neither moderation.

## Step 6. What would change my mind

```json
[
 {"finding": "r-beh:fnd:4", "severity": "fatal", "wouldWithdrawIf": "An equivalence test excludes peer effects above a substantively meaningful bound, AND peer outsourcing and peer modularity do not predict own change in m (so m is not a mediator), AND the result holds with referent-based peer measures."},
 {"finding": "r-beh:fnd:9", "severity": "damaging", "wouldWithdrawIf": "r-beh:chk:1 shows the Appendix cross-partial is correct (part b True), or the authors show that H depends on u differently than stated in ms:§2.2. Withdrawn automatically if the harness returns refuted-by-check."},
 {"finding": "r-beh:fnd:1", "severity": "damaging", "wouldWithdrawIf": "Outcome evidence (per-function IT cost, renegotiation or hold-up events, service quality) shows that outsourcing under higher modularity lowered costs or hazards, or process evidence shows sourcing decisions were made on comparative cost."},
 {"finding": "r-beh:fnd:2", "severity": "damaging", "wouldWithdrawIf": "The r-beh:chk:3 decomposition shows that beta1 x change in mean m accounts for a large share (say, half or more) of the 2009-2019 rise in mean Phi; or the authors rescope the claims to within-hospital variation."},
 {"finding": "r-beh:fnd:3", "severity": "damaging", "wouldWithdrawIf": "Referent-based peer measures give the same pattern; m is validated against external records of interface use; the specificity item is shown to measure the intended construct."},
 {"finding": "r-beh:fnd:5", "severity": "damaging", "wouldWithdrawIf": "A strong first stage (mandate on m), a heterogeneity-robust event study with flat pre-trends, a defended exclusion restriction, and function-level timing showing that m rises before outsourcing."},
 {"finding": "r-beh:fnd:11", "severity": "damaging", "wouldWithdrawIf": "The legitimacy account is deleted, or labelled as conjecture and supported by a test that discriminates it from the corrected TCE and slack accounts."},
 {"finding": "r-beh:fnd:12", "severity": "damaging", "wouldWithdrawIf": "Rivals (mimetic, coercive, normative, behavioral) are stated in strongest form and the manuscript reports at least one prediction on which they diverge, with the result."},
 {"finding": "r-beh:fnd:14", "severity": "damaging", "wouldWithdrawIf": "Mediation shows the modularity effect runs through specificity (or through measured hold-up exposure), or the specificity item is shown to measure nominal k, which removes r-beh:inc:5."},
 {"finding": "r-beh:fnd:18", "severity": "damaging", "wouldWithdrawIf": "The modularity effect survives a pre-treatment capability control (e.g. 2009 staffing interacted with year), or the capability claim is dropped."}
]
```

## Step 7. Recommendation (simulated)

**Major revision.**

The association behind H1 is credibly estimated: positive, precise and stable across four specifications (ms:T2). The research question suits a generalist organization-science readership, and the "what looks like fashion is economizing" framing has the form that this readership finds interesting. As submitted, though, the manuscript does not earn its headline claims. The claim to have ruled out mimetic isomorphism rests on a non-significant coefficient after adding a possible mediator (r-beh:fnd:4, fatal to that claim). The claim that the practice is economizing rests on fit to comparative statics, with no outcome measured (r-beh:fnd:1). The field-level diffusion named as the explanandum is absorbed by year effects (r-beh:fnd:2). Proposition 2 is, on re-derivation pending r-beh:chk:1, wrong in sign under the paper's own A3 (r-beh:fnd:9), and the discussion patches the resulting "anomaly" with an institutional mechanism the paper elsewhere denies (r-beh:fnd:11). The robustness test for capability is a bad control (r-beh:fnd:18).

None of this calls for rejection. The repairs are specifiable, and most can be made with data the authors appear to hold: correct the proof, report equivalence and mediation tests, a first stage and robust event study, a diffusion decomposition, and a test of aspiration moderation. Correcting Prop 2 would, in fact, turn the H2 result into support for the model. Only ctb:3 and ctb:6 fail as claimed. ctb:1, ctb:2, ctb:4, ctb:5 and ctb:7 survive in narrower forms (step 4). If the authors cannot meet r-beh:fnd:4 and must keep "rule out" language, this simulated reviewer would move to reject.

## Step 8. Self-location

The parameters that most drive these verdicts, so a panel can trace disagreements to them:

1. **INF.2: MI7 rejected (with EPI.5 effect sizes).** This drives the fatal rating of the "rule out mimicry" claim (r-beh:fnd:4) and the failure of ctb:3. A scorekeeper who accepts MI7 would score H3 as refuted.
2. **ONT.5: choice-theoretic marked suspect, with MI9 and MI2 rejected.** This drives r-beh:fnd:1 and the qualification of every "economizing" claim (ctb:4, ctb:5). A TCE scorekeeper would treat buy-iff-cheaper as a default entitlement.
3. **INF.2: MI5 endorsed, with INF.7 (rivals preferred) and EPI.3 (process-tracing first).** This generates the behavioral rival, the attributed commitment r-beh:cmt:24, and the demand for the aspiration test. A scorekeeper neutral on MI5 would not attribute that commitment.

Note: the most consequential formal finding (r-beh:fnd:9) does not depend on the lens. It comes from TEC.2 (re-derive) and INF.3, and any scorekeeper who re-derives should reach it, pending r-beh:chk:1.

---

## Decisions for the reviewer

1. **Run r-beh:chk:1 and r-beh:chk:2.** Should the harness run them before any of r-beh:fnd:9, fnd:10, fnd:20 or fnd:21 enters your report? Until then they are `asserted`.
2. **Severity of r-beh:fnd:4.** Accept "fatal to the 'rule out mimetic isomorphism' claim", or downgrade to "damaging" if you read the paper's central claim as H1 rather than the rival claim.
3. **Behavioral rival.** Ask the authors for the aspiration-moderation test (r-beh:chk:4)? It reflects this lens's MI5 commitment, which you (a differing perspective) may not share.
4. **Correcting Prop 2.** Point out that corrected Prop 2 turns the H2 result into support for the model (r-beh:fnd:8, fnd:9)? Doing so helps the authors.
5. **Priority claim.** Verify Loh & Venkatraman 1992 and Ang & Cummings 1997 before raising r-beh:fnd:15; drop it if they do not bear on the claim.
6. **Reverse causation.** Whether vendors install certified interfaces on taking over functions (r-beh:fnd:5) is this scorekeeper's empirical conjecture. Keep it only if it is plausible to you in this setting.
7. **Assimilative reframing.** Suggesting an assimilative reframing (r-beh:fnd:13) is a matter of taste. Decide whether it belongs in your report or in a note to the editor.
8. **Recommendation.** Accept, modify or reject the simulated "major revision", which is conditional on fnd:4 being repairable.
