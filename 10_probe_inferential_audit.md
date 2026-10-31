# Run 10: Adversarial Probe, inferential audit (Part 1)

- **Role:** Role 4, Adversarial Probe (capability 3). Instruction set: Reviewership v0.1 (23 October 2026).
- **Manuscript:** `ms:TEST`, "Modularity, Not Mimicry: Interoperability Standards and the Diffusion of IT Outsourcing in U.S. Hospitals".
- **Probe types assigned:** P-INF, P-MEAS, P-LIT.
- **Target:** the whole argument, Abstract to Conclusion.
- **Id prefix:** `p10:`. This is Part 1 (steps 1 to 3). No check has been run. Every finding is `asserted`.
- **Inputs used:** only the run file. No literature search was available, so every citation I add is marked "(to verify)".

## 0. Notes on scope and scorekeeping stance

1. **No reviewer perspective was supplied.** Commitments still have to be attributed by *some* scorekeeper, so I use a declared working stance and record it as a decision for the reviewer (`p10:dec:1`):
   - I attribute consequential commitments only through inferences the manuscript itself relies on: MI1 (§1, §2.2), MI8 (§1, §2.2) and MI6 (§3.3).
   - I reject MI7, which follows EPI.5 (intervals and equivalence over significance).
   - I am neutral on MI2, MI3, MI9 and MI10. Where an institutional scorekeeper who endorses MI3, plus DiMaggio and Powell's coercive/mimetic/normative typology, would attribute different consequential commitments, I mark the entry `perspective-dependent`.
2. **Findings outside my assigned types.** The audit's entitlement judgments depend on three things a P-INF probe cannot settle by argument: one derivation (Prop. 2), one estimator claim (the Model 4 staffing control) and several reported statistics. Rule 3 binds every role, so I state these as findings typed P-DER, P-ID and P-NUM. I tag each one `cross-type` and bind it to a check. The reviewer may hand them to the P-DER, P-ID and P-NUM probes instead (`p10:dec:2`).
3. **"Says" versus "infer".** In the scoreboard, `text` gives what the manuscript says, using its own wording where I quote. `basis` and `note` give my inference.

## 1. Reconstruction (L14 ArgMap)

Each step is classified as deductive (D), inductive (I) or abductive (A) with Explain(X,Y;L). Loci are in brackets.

| Step | Content | Mode | Locus |
|---|---|---|---|
| A1 | Relationship-specific assets expose the buyer to hold-up, and hierarchy economizes on that exposure (MI1). | Background (deferred) | §1 ¶2; §2.2 |
| A2 | Certified standard interfaces make functions modular, and modularity lowers effective specificity: $k \mapsto k(1-m)$ (MI8). | Assumption (deferred) | §1 ¶2; §2.2 |
| A3 | Hold-up hazards respond more to uncertainty than in-house adaptation costs do: $h_1/h_0 > g_1/(s+g_0)$. | Assumption (deferred to Williamson 1991) | §2.2, Assumption A3 |
| P1 | $\partial k^*/\partial m > 0$ | D (from A1, A2) | §2.3; Appendix |
| P2 | $\partial^2 k^*/\partial m\,\partial u > 0$ | Presented as D; the derivation is challenged (`p10:fnd:3`) | §2.3; Appendix |
| H1, H2 | Hospital-level outsourcing share $\Phi$ rises in $m$ (H1), and more steeply where $u$ is high (H2). | Presented as D from P1 and P2 via "functions with $k<k^*$ are outsourced". For H2 this is an enthymeme (`p10:fnd:10`). | §2.4 |
| H3 | Rival: $\Phi$ rises with lagged peer outsourcing. | Stated rival | §2.4 |
| DP | Discriminating prediction: economizing means the H3 association disappears once $m$ is controlled; mimicry means it survives. | Presented as D; contested (`p10:fnd:2`) | §2.4, last ¶ |
| E1 | $\hat\beta_m > 0$ in Models 2–4. | I | Table 2; §4 H1 |
| E2 | The peer coefficient falls from 0.137 to 0.042 and is non-significant. | I | Table 2 M1–M2; §4 H3 |
| C1 | "the apparent peer effect reflects the common diffusion of standards across hospitals in the same state, not imitation" | A, unlabelled | §4 H3 |
| E3 | The interaction is negative, contrary to H2. | I | Table 2 M3; §4 H2 |
| C2 | Legitimacy pressures under volatile demand offset economizing, and this is "consistent with our theory". | A, unlabelled, ad hoc | §5 ¶2 |
| E4 | The modularity effect survives the in-house-staffing control, so it is not capability. | Presented as D; challenged (`p10:fnd:6`) | §3.3 ¶2; §4 Robustness |
| E5 | The event study shows flat leads and a post-adoption rise, "consistent with a causal effect of modularity". | I, with an unstated exclusion restriction | §4 Robustness |
| C3 | "The results rule out mimetic isomorphism as a driver of IT outsourcing in this setting." | Presented as D from E2 (by MI7) | Abstract; §5 ¶1 |
| C4 | "Its substance is economizing." Standards "lowered the specificity that had kept them in-house". | Presented as D or established. The inference is A, through MI1 and MI8, with no cost evidence. | Abstract; §5; §6 |
| C5 | First study to adjudicate directly between transaction-cost economics (TCE) and institutional explanations. | Priority claim | Abstract; §1 ¶3 |

**Overall shape.** The argument runs in two lines.
- **The TCE line** (A1 → A2 → P1 → H1 → E1) is coherent as an association.
- **The adjudication line** (DP → E2 → C1 → C3 → C4) carries the title claim. It rests on three moves:
  - an unlabelled abduction (C1);
  - a significance-based null inference (MI7);
  - a discriminating prediction that does not discriminate when the institutional process runs *through* modularity.

The H2 line has two problems:
- The derivation (P2) appears to have the wrong sign under the paper's own A3.
- The authors explain the contrary result with an institutional mechanism (C2). That sits badly with C3 and C4.

## 2. Scoreboard (`p10:sb`)

Commitments as attributed by this scorekeeper, under the working stance in §0.

```json
{
  "Scoreboard": {
    "id": "p10:sb",
    "manuscript": "ms:TEST",
    "scorekeeper_stance": "working stance p10:dec:1 (endorses MI1, MI6, MI8 as used by ms; rejects MI7; neutral MI2, MI3, MI9, MI10)",
    "commitments": [
      {"id": "p10:cmt:1", "type": "avowed", "locus": "§1 ¶2; §2.2", "text": "Certified standard interfaces make IT functions modular; effective specificity of a function is k(1-m).", "entitlement": "deferred", "basis": "Baldwin & Clark 2000; Langlois 2002; Sanchez & Mahoney 1996; MI8. Entered in the model as an assumption, not derived.", "note": "challenged by the evidence pattern; see p10:chl:4, p10:inc:4"},
      {"id": "p10:cmt:2", "type": "avowed", "locus": "§1 ¶2; §2.2", "text": "Specific assets expose the buyer to hold-up; hierarchy economizes on that exposure (MI1).", "entitlement": "default", "basis": "Williamson 1975, 1985; default in TCE"},
      {"id": "p10:cmt:3", "type": "avowed", "locus": "§2.2 Assumption A3", "text": "h1/h0 > g1/(s+g0).", "entitlement": "deferred", "basis": "'Following Williamson (1991)'"},
      {"id": "p10:cmt:4", "type": "avowed", "locus": "§2.3 Prop. 1; Appendix", "text": "dk*/dm > 0.", "entitlement": "argued", "basis": "Appendix, Proof of Prop. 1. The proof appears sound; asserted pending p10:chk:1."},
      {"id": "p10:cmt:5", "type": "avowed", "locus": "§2.3 Prop. 2; Appendix", "text": "d2k*/dm du > 0.", "entitlement": "challenged", "basis": "Appendix, Proof of Prop. 2 differentiates only the numerator's dependence on u; H(u) in the denominator also depends on u.", "note": "p10:fnd:3; p10:inc:1"},
      {"id": "p10:cmt:6", "type": "consequential", "inference": "by §2.2 cost functions, §2.3 threshold and A3 (differentiation)", "locus": "§2.2-2.3", "text": "d2k*/dm du has the sign of g1*h0 - h1*(s+g0), which is negative under A3, for every u >= 0 and m in [0,1).", "entitlement": "argued", "basis": "my derivation; asserted pending p10:chk:1"},
      {"id": "p10:cmt:7", "type": "avowed", "locus": "§2.4 H1; §4 H1", "text": "Modularity is positively associated with the outsourcing share.", "entitlement": "evidenced", "basis": "Table 2, Modularity row, M2-M4 (0.112, 0.118, 0.097; all ***). Associational only."},
      {"id": "p10:cmt:8", "type": "avowed", "locus": "§2.4 H2", "text": "The modularity-outsourcing association is stronger when uncertainty is high.", "entitlement": "unentitled", "basis": "Derived from cmt:5, which is challenged. Contradicted by Table 2 M3 (-0.061**), as §4 concedes."},
      {"id": "p10:cmt:9", "type": "avowed", "locus": "§2.4 last ¶", "text": "Economizing implies the H3 association disappears once modularity is controlled; mimicry implies peers predict 'over and above modularity'.", "entitlement": "challenged", "basis": "No argument is given that modularity is not itself on the institutional path.", "note": "p10:fnd:2; p10:chk:4"},
      {"id": "p10:cmt:10", "type": "avowed", "locus": "§4 H3", "text": "'the apparent peer effect reflects the common diffusion of standards across hospitals in the same state, not imitation'", "entitlement": "unentitled", "basis": "No reported analysis of how standards diffused within states. This is an abductive conclusion presented as a finding."},
      {"id": "p10:cmt:11", "type": "avowed", "locus": "Abstract; §5 ¶1", "text": "'The results rule out mimetic isomorphism as a driver of IT outsourcing in this setting.'", "entitlement": "unentitled", "basis": "Rests on a non-significant coefficient (MI7, rejected) and on cmt:9 (challenged)."},
      {"id": "p10:cmt:12", "type": "avowed", "locus": "Abstract; §5 ¶1; §6", "text": "'Its substance is economizing.' Standards 'lowered the specificity that had kept them in-house'.", "entitlement": "unentitled", "basis": "No cost, performance or specificity-change evidence is reported. It follows only by MI1+MI8 from cmt:7, and cmt:7 is associational.", "note": "perspective-dependent: a TCE scorekeeper endorsing MI2 would treat persistence as partial support"},
      {"id": "p10:cmt:13", "type": "avowed", "locus": "§3.3 ¶1", "text": "Hospital and year fixed effects; 'Identification therefore comes from within-hospital changes in modularity over time.'", "entitlement": "challenged", "basis": "MI6 requires no time-varying confounders and no reverse timing. §1 itself says vendors build and maintain interfaces, so outsourcing can raise m."},
      {"id": "p10:cmt:14", "type": "avowed", "locus": "§3.3 ¶2; §4 Robustness", "text": "If the modularity effect survives the in-house staffing control, 'it cannot be attributed to capability differences.'", "entitlement": "unentitled", "basis": "Incompatible with cmt:15 (p10:inc:3); p10:chk:3"},
      {"id": "p10:cmt:15", "type": "avowed", "locus": "§3.2 'In-house IT staffing'", "text": "'outsourcing a function transfers its staff to the vendor or eliminates the positions'; staffing 'also tracks the scale of the hospital's internal IT capability'.", "entitlement": "default", "basis": "plausible institutional fact"},
      {"id": "p10:cmt:16", "type": "consequential", "inference": "by cmt:15 (staffing is caused by the dependent variable)", "locus": "§3.2", "text": "In-house staffing is a post-outcome variable. Conditioning on it does not hold capability fixed.", "entitlement": "argued", "basis": "cmt:15; asserted pending p10:chk:3"},
      {"id": "p10:cmt:17", "type": "avowed", "locus": "§4 Robustness", "text": "Event study on staggered state requirements (2011-2016): flat leads, rise after adoption, 'consistent with a causal effect of modularity'.", "entitlement": "challenged", "basis": "Reduced form of mandates on outsourcing, not modularity on outsourcing. The exclusion restriction is not stated. Estimates are not shown. Two-way fixed effects (TWFE) with staggered adoption is cross-referred to P-ID."},
      {"id": "p10:cmt:18", "type": "consequential", "inference": "by DiMaggio & Powell 1983 typology (coercive isomorphism)", "locus": "§4 Robustness; §3.3 (federal incentive programme)", "text": "The identifying variation in the robustness design is state mandates, that is, coercive institutional pressure.", "entitlement": "argued", "basis": "perspective-dependent: attributed by an institutional scorekeeper; neutral under TCE"},
      {"id": "p10:cmt:19", "type": "avowed", "locus": "§5 ¶2", "text": "Under high uncertainty, 'hospitals face legitimacy pressures to retain in-house functions'. This is 'consistent with our theory'.", "entitlement": "unentitled", "basis": "No evidence. The mechanism is outside the model (§2) and is an institutional one (MI10-type)."},
      {"id": "p10:cmt:20", "type": "avowed", "locus": "§3.2 'Peer outsourcing'", "text": "The same-state lagged mean of other sample hospitals is 'the population to which mimetic isomorphism directs attention'.", "entitlement": "challenged", "basis": "p10:fnd:11"},
      {"id": "p10:cmt:21", "type": "avowed", "locus": "§3.2 'Modularity'", "text": "m = share of clinical information systems exchanging data through certified interfaces, as reported by the CIO.", "entitlement": "challenged", "basis": "Covers clinical systems only. Phi covers all IT functions. p10:fnd:12"},
      {"id": "p10:cmt:22", "type": "avowed", "locus": "Abstract; §4 H1", "text": "Modularity 'strongly predicts' the outsourcing share.", "entitlement": "challenged", "basis": "Own effect size: about 1/6 SD per SD of m. Within R2 rises from 0.08 to 0.13. p10:chk:2"},
      {"id": "p10:cmt:23", "type": "avowed", "locus": "Abstract; §1 ¶3", "text": "'the first study to adjudicate directly between transaction-cost and institutional explanations of IT outsourcing.'", "entitlement": "challenged", "basis": "p10:fnd:17"},
      {"id": "p10:cmt:24", "type": "avowed", "locus": "§5.1", "text": "TCE contribution: 'Specificity is not a fixed property of an activity; it is partly a product of interface design'.", "entitlement": "deferred", "basis": "The claim is already in the cited Langlois 2002 and Sanchez & Mahoney 1996, so its novelty is challenged (p10:fnd:18)."},
      {"id": "p10:cmt:25", "type": "avowed", "locus": "§3.1; Table 2", "text": "Balanced panel of 412 hospitals, annual 2009-2019, 4,712 hospital-years.", "entitlement": "challenged", "basis": "412 x 11 = 4,532, not 4,712. Peer(t-1) for 2009 needs 2008 data. p10:chk:2"}
    ],
    "incompatibilities": [
      {"id": "p10:inc:1", "pair": ["p10:cmt:5", "p10:cmt:6"], "reason": "Under A3 the cross-partial is negative; Prop. 2 asserts it is positive. Asserted pending p10:chk:1."},
      {"id": "p10:inc:2", "pair": ["p10:cmt:19", "p10:cmt:12"], "reason": "If legitimacy pressures materially shape sourcing under high uncertainty, the substance of the diffusion is not economizing alone. §5 ¶2 concedes an institutional mechanism that §6 denies. (Strictly compatible with cmt:11, which concerns mimetic isomorphism only.)"},
      {"id": "p10:inc:3", "pair": ["p10:cmt:14", "p10:cmt:15"], "reason": "If outsourcing removes in-house positions, staffing is partly caused by the outcome. Conditioning on it cannot hold capability fixed, so survival of beta_m under that control cannot exclude capability confounding."},
      {"id": "p10:inc:4", "pair": ["p10:cmt:1", "p10:cmt:7"], "reason": "Tension, not strict incompatibility. If m works through effective specificity, and the specificity rating (a switching-cost rating, §3.2) tracks effective specificity, then beta_m should shrink once specificity is held fixed. Adding m should also move the specificity coefficient. Table 2 shows beta_m = 0.112*** given specificity, and the specificity coefficient moves only from -0.094 to -0.091. Either the measure does not capture k(1-m) or m does not work through it. Implied auxiliary slope in p10:chk:2."},
      {"id": "p10:inc:5", "pair": ["p10:cmt:12", "p10:cmt:18"], "reason": "perspective-dependent. For a scorekeeper who classifies mandates as coercive isomorphism, the robustness design identifies an institutionally driven effect. The 'not institutional' framing of §5.1 and §6 then cannot be held together with the paper's own identifying variation. The narrower 'not mimetic' claim survives this pair."},
      {"id": "p10:inc:6", "pair": ["p10:cmt:8", "p10:cmt:19"], "reason": "The authors hold that H2 follows from the theory (§2.4) and also that its contradiction is 'consistent with our theory' (§5 ¶2). Both can stand only if the theory is amended. The amendment is not made, and §5 ¶2 defers it to 'future work'."}
    ],
    "challenges": [
      {"id": "p10:chl:1", "target": "p10:cmt:11", "request": "Show that peer effects of a substantively relevant size are excluded: equivalence bounds or a CI, not non-significance."},
      {"id": "p10:chl:2", "target": "p10:cmt:9", "request": "Give reasons why modularity is not itself diffused by imitation or mandate within states, given that the standards diffusion invoked in §4 occurs by state."},
      {"id": "p10:chl:3", "target": "p10:cmt:10", "request": "Provide evidence for within-state common diffusion of standards, and for how it occurred."},
      {"id": "p10:chl:4", "target": "p10:cmt:1", "request": "Show that modularity reduces the measured specificity, and that the specificity rating is nominal k or effective k(1-m)."},
      {"id": "p10:chl:5", "target": "p10:cmt:5", "request": "Re-derive Prop. 2 including H'(u) = h1."},
      {"id": "p10:chl:6", "target": "p10:cmt:12", "request": "Provide evidence that outsourcing lowered the hospital's governance plus production costs, or narrow the claim."},
      {"id": "p10:chl:7", "target": "p10:cmt:13", "request": "Address reverse timing (outsourcing leading to vendor-installed certified interfaces), using the timing of m relative to Phi."},
      {"id": "p10:chl:8", "target": "p10:cmt:14", "request": "Use pre-period (pre-2009) capability measures rather than contemporaneous staffing."},
      {"id": "p10:chl:9", "target": "p10:cmt:17", "request": "Report the event-study estimates. State the exclusion restriction. Use heterogeneity-robust staggered estimators."},
      {"id": "p10:chl:10", "target": "p10:cmt:19", "request": "Either drop the legitimacy account or test it. Explain how it is consistent with §6."},
      {"id": "p10:chl:11", "target": "p10:cmt:20", "request": "Justify the referent set as the one mimetic theory specifies."},
      {"id": "p10:chl:12", "target": "p10:cmt:21", "request": "Show that m bears on the specificity of the non-clinical functions included in Phi."},
      {"id": "p10:chl:13", "target": "p10:cmt:23", "request": "Engage prior IS-outsourcing studies that set economic against institutional explanations."},
      {"id": "p10:chl:14", "target": "p10:cmt:25", "request": "Reconcile 4,712 with 412 hospitals x 11 years and with the lagged peer variable."}
    ]
  }
}
```

## 3. Findings

All findings are `asserted`. Severities are provisional until Part 2.

### 3.1 P-INF: inferential audit

```json
[
  {
    "id": "p10:fnd:1",
    "probe_type": "P-INF",
    "locus": "Abstract ('rule out mimetic isomorphism'); §4 H3; §5 ¶1; Table 2 Peer row M1-M2",
    "commitment": "p10:cmt:11",
    "missing_entitlement": "The step from 'no longer significant' (0.042, SE 0.038) to 'rule out' is MI7, which this stance rejects (EPI.5). Read as a 95% interval, the M2 coefficient excludes neither zero nor peer effects close to the M1 estimate. The upper bound is about 0.116, against 0.137 in M1. 'Falls by more than two-thirds' is a point comparison with no test of the difference. Peer outsourcing varies at state-year level but SEs are clustered by hospital, which probably understates its SE (cross-referred to P-ID). 'Rule out' is deductive vocabulary for an inductive, underpowered null (INF.1).",
    "severity": "damaging",
    "repair": "Report the CI and a TOST equivalence test against a stated smallest effect of interest. Test the M1-M2 change in the peer coefficient (e.g., seemingly unrelated or stacked estimation). Cluster at state level or two-way. Replace 'rule out' with what the interval licenses.",
    "check": "p10:chk:2 (part e)",
    "status": "asserted"
  },
  {
    "id": "p10:fnd:2",
    "probe_type": "P-INF",
    "locus": "§2.4 last ¶; §4 H3 ('exactly what the transaction-cost account predicts and the institutional account does not'); title",
    "commitment": "p10:cmt:9, p10:cmt:10",
    "missing_entitlement": "The discriminating prediction (DP) discriminates only if modularity is not on the institutional causal path. The manuscript's own account of the pattern is 'common diffusion of standards across hospitals in the same state' (§4). How standards diffused within states is not shown. If certified interfaces were adopted by imitating peers, or under state mandates (the variation the robustness design itself uses), then controlling for m blocks the institutional path, and the peer coefficient would vanish under the institutional account too. INF.7 asks for the rival in its strongest form. The rival is stated only as a direct peer-to-outsourcing effect, the form most easily absorbed by a mediator. C1 is therefore an unlabelled abduction (INF.1).",
    "severity": "fatal",
    "severity_note": "Fatal to the adjudication claim (title, Abstract, §5, §6), not to H1. If the authors narrow their claims to the H1 association, this falls to damaging. Reviewer decision p10:dec:3.",
    "repair": "Test whether own modularity responds to lagged peer modularity or peer outsourcing, net of state mandates, and whether mandate timing explains the peer pattern. Separate coercive (mandate) from mimetic (non-mandate peer) variation. Add the rival's own discriminating predictions (p10:fnd:19), and drop 'exactly' and 'does not'.",
    "check": "p10:chk:4 (demonstration that the DP pattern arises when standards diffuse by imitation)",
    "status": "asserted"
  },
  {
    "id": "p10:fnd:4",
    "probe_type": "P-INF",
    "locus": "§5 ¶2; §6; Abstract",
    "commitment": "p10:cmt:19 vs p10:cmt:12",
    "incompatibility": "p10:inc:2 and p10:inc:6. The contrary H2 result is explained ad hoc by legitimacy pressures, an institutional mechanism (MI10-type) outside the model. It is then declared 'consistent with our theory'. The move immunizes H2 from refutation. It also concedes institutional determination of the outcome, while §6 says the substance 'is economizing'. Under §2.2-A3 the model itself may predict the negative sign (p10:fnd:3). If so, the auxiliary is unnecessary as well as unentitled.",
    "severity": "damaging",
    "repair": "If p10:chk:1 confirms the sign: correct Prop. 2 and drop the legitimacy story. H2 is then an accommodation, not a novel prediction (EPI.4), and should be labelled so. If the sign is not confirmed: either test the legitimacy account (e.g., board composition, community-board hospitals) or remove it, and stop calling it consistent with the theory.",
    "check": null,
    "status": "asserted"
  },
  {
    "id": "p10:fnd:5",
    "probe_type": "P-INF",
    "locus": "§2.2 (k(1-m)); §3.2 'Asset specificity'; Table 2 Asset specificity and Modularity rows",
    "commitment": "p10:cmt:1",
    "missing_entitlement": "p10:inc:4. The mechanism (m lowers effective specificity, and that lowers hold-up exposure) is never shown. The specificity rating ('how costly it would be to transfer... to a different provider') reads as effective, ex post specificity, which is the model's mediator. Yet beta_m stays large with it held fixed, and its coefficient barely moves when m enters. By the omitted-variable identity, the implied partial slope of m on specificity is about -0.03 per unit (p10:chk:2 part f), which is close to orthogonal. Two readings are possible, and the manuscript must choose. (a) The rating measures nominal k: then the paper never measures effective specificity, and the mechanism is assumed. (b) It measures k(1-m): then the evidence speaks against the mechanism.",
    "severity": "damaging",
    "repair": "Regress the specificity rating on m (within hospital). Show a mediation decomposition, or state that the mechanism is untested and remove the mechanism language from the Abstract and §6.",
    "check": "p10:chk:2 (part f)",
    "status": "asserted"
  },
  {
    "id": "p10:fnd:7",
    "probe_type": "P-INF",
    "locus": "Abstract; §5 ¶1 ('Interoperability standards made IT functions modular, reduced... widened'); §6; §4 Robustness (event study)",
    "commitment": "p10:cmt:13, p10:cmt:17",
    "missing_entitlement": "Extend(X,Y): causal and historical claims are drawn from within-hospital associations. MI6 needs no time-varying confounding and no reverse timing. The manuscript's own §1 says vendors build and maintain interfaces, so outsourcing can raise m (reverse timing). The event study is a reduced form of state mandates on outsourcing. To read it as 'a causal effect of modularity' requires that mandates affect outsourcing only through m. That restriction is not stated, and the mandate is itself an institutional pressure (p10:cmt:18). The estimates are not reported. TWFE with staggered timing is cross-referred to P-ID.",
    "severity": "damaging",
    "repair": "Report the event study, mandate-to-m first stage and reduced form, using heterogeneity-robust estimators. State the exclusion restriction and discuss it. Show the lead-lag timing of m relative to Phi. Otherwise use associational language.",
    "check": null,
    "status": "asserted"
  },
  {
    "id": "p10:fnd:8",
    "probe_type": "P-INF",
    "locus": "Abstract ('economizing'); §5 ¶1; §6 ('Its substance is economizing')",
    "commitment": "p10:cmt:12",
    "missing_entitlement": "Economizing is a claim about comparative costs. No costs, prices, hold-up incidents or performance outcomes are reported. The inference runs from 'outsourcing co-moves with m' through MI1 and MI8 to 'outsourcing economizes'. It is valid only for a scorekeeper who already endorses the mechanism, and the mechanism is untested (p10:fnd:5). It is an abduction presented as a finding.",
    "severity": "damaging",
    "repair": "Add cost or performance evidence (IT cost per bed, contract renegotiation, outages) by outsourcing status and m, or restate as 'consistent with an economizing account'.",
    "check": null,
    "status": "asserted"
  },
  {
    "id": "p10:fnd:9",
    "probe_type": "P-INF",
    "locus": "Abstract ('strongly predicts'); §4 H1 ('strongly and positively')",
    "commitment": "p10:cmt:22",
    "missing_entitlement": "The manuscript's own magnitude is 2.7 points per SD of m, about 1/6 SD of Phi. Within R2 rises from 0.08 to 0.13. Adding m cuts the peer coefficient's point estimate, but the variance explained stays modest. 'Strongly' conflates statistical with substantive strength. Separately, on the paper's own figures a 2.7-point gain per SD cannot account for a doubling of outsourcing (§1) unless m rose by several SDs; the paper does not report the change in m. (Inference; verify against descriptive trends.)",
    "severity": "minor",
    "repair": "Replace 'strongly'. Report the decomposition: how much of the 2009-2019 rise in Phi the observed rise in m accounts for, at beta_m.",
    "check": "p10:chk:2 (part c)",
    "status": "asserted"
  },
  {
    "id": "p10:fnd:10",
    "probe_type": "P-INF",
    "locus": "§2.4 ('Proposition 2 implies that this association is stronger where uncertainty is high')",
    "commitment": "p10:cmt:8",
    "missing_entitlement": "Enthymeme (INF.4). Phi = F(k*) for the spending-weighted distribution F of k, so d2Phi/dm du = f'(k*) k*_m k*_u + f(k*) k*_mu. The sign on the tested scale depends on the density at the threshold and on k*_u, not only on k*_mu. The paper tests a linear m x u interaction, so the derivation must give the sign on that scale. At a corner (k* >= 1), dPhi/dm = 0.",
    "severity": "fixable",
    "repair": "Derive the sign of the interaction for Phi under a stated F (or a bound on f'), or test at function level.",
    "check": "p10:chk:1 (part B)",
    "status": "asserted"
  }
]
```

Numbering note: `p10:fnd:3` and `p10:fnd:6` are cross-type findings (P-DER, P-ID) and appear in §3.4.

### 3.2 P-MEAS: measurement of constructs, the rival's included

```json
[
  {
    "id": "p10:fnd:11",
    "probe_type": "P-MEAS",
    "locus": "§3.2 'Peer outsourcing' ('the population to which mimetic isomorphism directs attention')",
    "commitment": "p10:cmt:20",
    "missing_entitlement": "The rival's key construct is under-measured on four counts. (a) Referents: mimetic isomorphism (MI3) specifies peers perceived as successful, legitimate or similar (DiMaggio & Powell 1983, as cited; Haveman 1993, ASQ 38(4), to verify), or tied through systems, boards and consultants. 'All other sample hospitals in the same state' is none of these. (b) Coverage: peers are drawn from the 412-hospital sample only, so the inferred average is about eight per state. The peer mean is therefore a noisy proxy for field prevalence. Its attenuation, and m absorbing shared state trends, could produce the M1 to M2 drop by themselves. (c) Confounding of types: the state is the unit of regulation (the mandates of §4), so a same-state peer mean mixes coercive and mimetic pressure. (d) Moderator: the rival predicts imitation is strongest under uncertainty (§1; §2.4 'Under uncertainty...'), but peer x uncertainty is never estimated.",
    "severity": "damaging",
    "repair": "Build peer measures from population data on all hospitals in the state or hospital referral region (source to verify). Add referent-specific peers (same system, similar size or teaching status, high-status hospitals). Estimate peer x uncertainty. Separate mandate states and years.",
    "check": null,
    "status": "asserted"
  },
  {
    "id": "p10:fnd:12",
    "probe_type": "P-MEAS",
    "locus": "§3.2 'Modularity' (clinical information systems) vs §2.1 functions and §3.2 'Outsourcing share' (all IT operating spending)",
    "commitment": "p10:cmt:21",
    "missing_entitlement": "Domain mismatch. In the model, m acts on the specificity of each function (§2.2). The measure counts only clinical information systems connected through certified interfaces. Phi includes functions the manuscript lists in §2.1 as infrastructure hosting, help-desk support and revenue-cycle systems. Their specificity is not obviously governed by clinical interoperability standards. A positive beta_m driven by non-clinical functions would point to a common cause, such as general IT modernization, rather than the mechanism. 'Certified to a published standard' also blurs product certification with interface use (inference).",
    "severity": "fixable",
    "severity_note": "Could rise to damaging. The repair gives a discriminating test: the mechanism predicts beta_m concentrated in clinical-application functions.",
    "repair": "Report outsourcing by function. Show beta_m for clinical versus non-clinical functions, and define the certification referent.",
    "check": null,
    "status": "asserted"
  },
  {
    "id": "p10:fnd:13",
    "probe_type": "P-MEAS",
    "locus": "§3.1 ('Data on IT spending and sourcing come from an annual survey of... CIOs'); §3.2 modularity and specificity 'as reported by the CIO'; §5.2",
    "commitment": "p10:cmt:7",
    "missing_entitlement": "EPI.6. Outcome, focal regressor and specificity all come from one informant in one instrument. Hospital fixed effects remove stable response styles, but not time-varying ones, such as a new CIO or a CIO who has just outsourced and rates interfaces more favourably. Common-source covariance can inflate beta_m. §5.2 acknowledges CIO reliance but not its consequence for the m-Phi association.",
    "severity": "fixable",
    "repair": "Validate m against an administrative source of certified-technology use (e.g., federal certification or attestation records, to verify). Validate Phi against financial filings. Report results with CIO-turnover years excluded.",
    "check": null,
    "status": "asserted"
  },
  {
    "id": "p10:fnd:14",
    "probe_type": "P-MEAS",
    "locus": "§3.2 'Environmental uncertainty' (CV of quarterly admissions, preceding three years); §2.2 H(u), G(u)",
    "commitment": "p10:cmt:8",
    "missing_entitlement": "In §2.2, u is uncertainty that raises 'the frequency of unanticipated adaptations' in the IT relationship. Volatility in inpatient demand is a different construct. It is not obviously a disturbance to IT functions. It is also not the technological or goal ambiguity that drives mimetic behaviour in the rival account. A three-year rolling window, after hospital fixed effects, leaves slow-moving within variation. The H2 test and the §5 ¶2 'resilience' story both rest on this measure.",
    "severity": "fixable",
    "repair": "Justify the construct mapping, or add IT-relevant uncertainty measures, such as standards revision events, vendor-market turnover or EHR-replacement episodes. Report within-hospital variance of u.",
    "check": null,
    "status": "asserted"
  },
  {
    "id": "p10:fnd:15",
    "probe_type": "P-MEAS",
    "locus": "§3.2 'Asset specificity' (seven-point switching-cost rating, averaged over functions); Table 2 all models",
    "commitment": "p10:cmt:1",
    "missing_entitlement": "The rating does not say whether it measures nominal k or effective k(1-m) (p10:fnd:5). For functions already outsourced, the cost of moving to 'a different provider' includes vendor lock-in created by the outsourcing itself, so the variable may be partly caused by Phi. Averaging over functions also discards the function-level threshold structure of §2.3.",
    "severity": "fixable",
    "repair": "Define the rating's referent (in-house versus outsourced functions). Treat it as mediator or as pre-determined. Show results without it.",
    "check": null,
    "status": "asserted"
  },
  {
    "id": "p10:fnd:16",
    "probe_type": "P-MEAS",
    "locus": "§2.4 (Phi as spending-weighted share of functions outsourced) vs §3.2 (share of IT operating spending paid to vendors)",
    "commitment": "p10:cmt:7",
    "missing_entitlement": "The model's Phi is the share of functions outsourced. The measure is a spending share, so it also moves with vendor prices (s) and partial outsourcing, without any change at the margin. How cloud and subscription services are classified relative to the excluded licences is not stated.",
    "severity": "minor",
    "repair": "Add a count-based or function-based share and state the treatment of subscription services.",
    "check": null,
    "status": "asserted"
  }
]
```

### 3.3 P-LIT: literature and placement

No search tool was available. Every reference below is from memory and marked "(to verify)". Bibliographic details may be wrong.

```json
[
  {
    "id": "p10:fnd:17",
    "probe_type": "P-LIT",
    "locus": "Abstract; §1 ¶3 ('To our knowledge, this is the first study to adjudicate directly...')",
    "commitment": "p10:cmt:23",
    "missing_entitlement": "The priority claim is very probably false. IS-outsourcing research has set economic against institutional explanations before: Loh & Venkatraman (1992), 'Diffusion of information technology outsourcing: influence sources and the Kodak effect', Information Systems Research 3(4) (to verify), on internal versus external, imitative influence; and Ang & Cummings (1997), 'Strategic response to institutional influences on information systems outsourcing', Organization Science 8(3) (to verify). Close neighbours are Ang & Straub (1998), MIS Quarterly 22(4), on production and transaction economies in bank IS outsourcing (to verify), and Poppo & Zenger (1998), SMJ 19(9), testing TCE against alternatives for make-or-buy in information services (to verify).",
    "severity": "fixable",
    "repair": "Delete the priority claim, or narrow it (e.g., 'in hospitals' or 'with a within-hospital panel'). Position against these studies.",
    "check": null,
    "status": "asserted"
  },
  {
    "id": "p10:fnd:18",
    "probe_type": "P-LIT",
    "locus": "§1 ¶2; §5.1 TCE contribution",
    "commitment": "p10:cmt:24, p10:cmt:1",
    "missing_entitlement": "PRA.2 and PRA.3. 'Specificity is partly a product of interface design' is the thesis of works the manuscript cites (Langlois 2002; Sanchez & Mahoney 1996; Baldwin & Clark 2000). Empirical tests of modularity leading to outsourcing or disintegration exist: Schilling & Steensma (2001), AMJ 44(6) (to verify); Argyres & Bigelow (2010), Organization Science 21(4) (to verify); Tiwana (2008), SMJ 29(11), on software outsourcing (to verify). Work challenging MI8 is omitted: Brusoni, Prencipe & Pavitt (2001), ASQ 46(4), 'why do firms know more than they make?' (to verify); Hoetker (2006), SMJ 27(6), 'Do modular products lead to modular organizations?' (to verify). On uncertainty in TCE tests, a review such as David & Han (2004), SMJ 25(1) (to verify), reports mixed support. That bears directly on H2 and A3.",
    "severity": "fixable",
    "severity_note": "This reduces the stated TCE contribution to setting plus adjudication. Reviewer decision p10:dec:4 on whether it is damaging to contribution.",
    "repair": "Recast the TCE contribution as evidence in a new setting, engage the challenges to MI8, and justify A3 against the mixed evidence on uncertainty.",
    "check": null,
    "status": "asserted"
  },
  {
    "id": "p10:fnd:19",
    "probe_type": "P-LIT",
    "locus": "§1 ¶1 (Tolbert & Zucker 1983; Westphal, Gulati & Shortell 1997 cited); §2.4 H3",
    "commitment": "p10:cmt:9",
    "missing_entitlement": "INF.7: the rival is not in its strongest form. The paper's own citations carry a stage-dependent prediction. Early adopters adopt for technical reasons, later adopters for legitimacy (Tolbert & Zucker 1983), and early adopters customize where later ones conform (Westphal et al. 1997). That predicts the m-Phi association weakening, and peer effects strengthening, as adoption spreads. It is not tested. The efficiency-versus-imitation dichotomy is itself contested. Kennedy & Fiss (2009), AMJ 52(5), on TQM in U.S. hospitals (to verify), argue that both early and late adopters have economic motives under different framings. Lieberman & Asaba (2006), AMR 31(2) (to verify), and Strang & Macy (2001), AJS 107(1) (to verify), treat imitation as potentially information-based and adaptive. Peer effects therefore do not imply mimicry, and their absence does not imply economizing. That cuts against the H3 framing in both directions.",
    "severity": "damaging",
    "severity_note": "Overlaps p10:fnd:2. Reviewer may consolidate (p10:dec:3).",
    "repair": "Test the stage-dependent prediction: interact m and peer with adopter cohort or with time since the state's first adoption. Engage the information-based imitation literature, and restate H3 accordingly.",
    "check": null,
    "status": "asserted"
  },
  {
    "id": "p10:fnd:20",
    "probe_type": "P-LIT",
    "locus": "§3.3; §4 Robustness (TWFE event study); §4 H3",
    "commitment": "p10:cmt:17, p10:cmt:11",
    "missing_entitlement": "Methodological literature is omitted where the design depends on it. Staggered-adoption TWFE: Goodman-Bacon (2021), Sun & Abraham (2021), Callaway & Sant'Anna (2021), all J. Econometrics, and de Chaisemartin & D'Haultfoeuille (2020), AER (all to verify). Identification of peer effects (the reflection problem): Manski (1993), Review of Economic Studies (to verify). Equivalence testing for null claims: Lakens (2017), Social Psychological and Personality Science (to verify). Bad controls: Angrist & Pischke (2009), Mostly Harmless Econometrics (to verify). Cross-referred to P-ID for substance.",
    "severity": "fixable",
    "repair": "Cite and apply these.",
    "check": null,
    "status": "asserted"
  }
]
```

### 3.4 Cross-type findings (P-DER, P-ID, P-NUM), bound to checks under rule 3

Each of these decides an entitlement on the scoreboard. They lie outside the assigned probe types, so they are tagged `cross-type`.

```json
[
  {
    "id": "p10:fnd:3",
    "probe_type": "P-DER",
    "cross_type": true,
    "locus": "§2.3 Prop. 2; Appendix, Proof of Prop. 2 ('Modularity operates on the denominator of k* only through the factor (1-m), so the cross-partial is determined by how the numerator responds to uncertainty')",
    "commitment": "p10:cmt:5",
    "incompatibility": "p10:inc:1. The proof treats H(u) as constant in u. But §2.2 sets H(u) = h0 + h1 u with h1 > 0. Including H'(u), the cross-partial is [g1 H(u) - (s+G(u)) h1] / [H(u)^2 (1-m)^2]. The u-terms cancel in the numerator, leaving g1 h0 - h1 (s+g0). That is negative exactly when A3 holds. Under the paper's own assumption, then, the model predicts a negative m x u interaction, and that is what Table 2 M3 reports. The quoted sentence is a non sequitur: that m enters only through (1-m) says nothing about whether u enters the denominator.",
    "severity": "damaging",
    "severity_note": "Damaging to the theory section and to a stated contribution (§1 ¶3, 'the effect is amplified by environmental uncertainty'). Not fatal to H1. If confirmed, it removes the need for §5 ¶2 (p10:fnd:4), and the correct sign becomes an accommodation (EPI.4).",
    "repair": "Correct Prop. 2's sign and proof. Restate H2 as a negative interaction derived from A3, and report that it was derived after the estimate was seen. Alternatively, drop A3, but then the sign of Prop. 2 is undetermined.",
    "check": "p10:chk:1 (part A)",
    "status": "asserted"
  },
  {
    "id": "p10:fnd:6",
    "probe_type": "P-ID",
    "cross_type": true,
    "locus": "§3.3 ¶2 ('If the modularity effect survives this control, it cannot be attributed to capability differences'); §3.2 'In-house IT staffing'; Table 2 M4; §4 Robustness",
    "commitment": "p10:cmt:14",
    "incompatibility": "p10:inc:3. By the manuscript's own §3.2, staffing falls when functions are outsourced, so it is partly an outcome of Phi. It also tracks unobserved capability. Conditioning on a variable caused by the dependent variable neither holds capability fixed nor leaves beta_m interpretable. Survival of beta_m therefore cannot license 'cannot be attributed'. Operating margin (a control) may raise the same issue (inference).",
    "severity": "fixable",
    "repair": "Drop the claim, or use pre-period (2008) capability measures interacted with year, or an instrument for capability. Report M4 as a sensitivity analysis only.",
    "check": "p10:chk:3",
    "status": "asserted"
  },
  {
    "id": "p10:fnd:21",
    "probe_type": "P-NUM",
    "cross_type": true,
    "locus": "§3.1 ('balanced panel of 412... 2009 to 2019... 4,712 hospital-year observations'); Table 2 Observations row; Table 2 M3 Environmental uncertainty '0.084*** (0.051)'",
    "commitment": "p10:cmt:25, p10:cmt:7",
    "incompatibility": "(i) 412 x 11 = 4,532 observations, not 4,712, for a balanced 2009-2019 annual panel. Also, a peer variable lagged to t-1 for 2009 needs 2008 data, which §3.1 does not mention. Without it, N would be 412 x 10 = 4,120. (ii) 0.084/0.051 gives |t| of about 1.65, which does not reach p < 0.05, yet *** is reported. Other stars, the 2.7-point and one-sixth-SD magnitudes, and the 'more than two-thirds' fall look consistent (asserted).",
    "severity": "fixable",
    "severity_note": "The N discrepancy may indicate an unbalanced panel or a data-construction problem. If it does, upgrade to damaging.",
    "repair": "Reconcile N and the panel definition. Correct the stars.",
    "check": "p10:chk:2 (parts a, b)",
    "status": "asserted"
  }
]
```

## 4. Checks (CheckSpecs). Not run; for the harness

Each check is self-contained and uses only `numpy`, `scipy`, `sympy`, `statsmodels` and `pandas`. Each one prints lines beginning `VERDICT:`. Premises are taken from the manuscript and cited in comments.

### p10:chk:1

```json
{
  "CheckSpec": {
    "id": "p10:chk:1",
    "binds": ["p10:fnd:3", "p10:fnd:10", "p10:cmt:4", "p10:cmt:5", "p10:cmt:6"],
    "probe_type": "P-DER",
    "method": "Symbolic re-derivation (sympy) of Prop. 1 and Prop. 2, with a numerical sign sweep under A3. Part B checks the sign of the m x u interaction on the Phi scale under illustrative Beta specificity densities.",
    "premises": ["§2.2 C_B, C_M, H(u)=h0+h1u, G(u)=g0+g1u, s,h0,h1,g0,g1>0, u>=0, m in [0,1)", "§2.2 Assumption A3", "§2.3 k*", "Appendix proofs", "§2.4 'functions with k<k* are outsourced'"],
    "expected_output": "VERDICT lines for Prop. 1, Prop. 2 and the H2 scale",
    "libraries": ["sympy", "numpy", "scipy"]
  }
}
```

```python
# p10:chk:1 — re-derive Prop. 1 and Prop. 2 of ms:TEST from its own §2.2-2.3 (Part A);
#              sign of the m x u interaction on the Phi scale of §2.4 (Part B). Not run by the probe.
import numpy as np
import sympy as sp
from scipy import stats

# §2.2: s > 0; h0, h1, g0, g1 > 0; u >= 0; m in [0,1)
s, h0, h1, g0, g1 = sp.symbols('s h0 h1 g0 g1', positive=True)
u = sp.symbols('u', nonnegative=True)
m = sp.symbols('m', nonnegative=True)
H = h0 + h1*u                    # §2.2 H(u) = h0 + h1 u
G = g0 + g1*u                    # §2.2 G(u) = g0 + g1 u
kstar = (s + G) / (H*(1 - m))    # §2.3 k*(m,u) = (s + G(u)) / (H(u)(1 - m)), from C_B < C_M

# ---------- Part A1: Prop. 1 ----------
d_m = sp.diff(kstar, m)
appendix_d_m = (s + G) / (H*(1 - m)**2)            # Appendix, Proof of Prop. 1
p1_match = sp.simplify(d_m - appendix_d_m) == 0

# ---------- Part A2: Prop. 2 ----------
d_mu = sp.simplify(sp.diff(kstar, m, u))
appendix_d_mu = g1 / (H*(1 - m)**2)                # Appendix, Proof of Prop. 2
p2_appendix_match = sp.simplify(d_mu - appendix_d_mu) == 0
numer_claim = g1*h0 - h1*(s + g0)                  # probe's claimed sign-bearing numerator
numer_ok = sp.simplify(d_mu*H**2*(1 - m)**2 - numer_claim) == 0
e = sp.symbols('e', positive=True)                 # A3 slack: h1/h0 = (1+e) g1/(s+g0), e > 0
numer_A3 = sp.simplify(numer_claim.subs(h1, g1*h0*(1 + e)/(s + g0)))
print("Prop 1: Appendix derivative equals re-derivation:", p1_match)
print("Prop 2: re-derived cross-partial:", sp.factor(d_mu))
print("Prop 2: Appendix expression equals re-derivation:", p2_appendix_match)
print("Prop 2: numerator equals g1*h0 - h1*(s+g0):", numer_ok, "| under A3 it is", numer_A3,
      "| symbolically negative:", numer_A3.is_negative)

# Numerical sweep over parameters satisfying A3 (and, for contrast, violating it)
args = (s, h0, h1, g0, g1, u, m)
f_dm = sp.lambdify(args, d_m, 'numpy')
f_dmu = sp.lambdify(args, d_mu, 'numpy')
rng = np.random.default_rng(1)
n = 200_000
S_ = rng.uniform(0.01, 2, n); H0 = rng.uniform(0.01, 2, n)
G0 = rng.uniform(0.01, 2, n); G1 = rng.uniform(0.01, 2, n)
U = rng.uniform(0, 5, n); M = rng.uniform(0, 0.99, n)
ratio = G1/(S_ + G0)
H1 = H0*ratio*rng.uniform(1.0001, 5, n)            # enforces A3: h1/h0 > g1/(s+g0)
H1r = H0*ratio*rng.uniform(0.01, 0.9999, n)        # A3 violated
share_dm_pos = np.mean(f_dm(S_, H0, H1, G0, G1, U, M) > 0)
share_dmu_neg = np.mean(f_dmu(S_, H0, H1, G0, G1, U, M) < 0)
share_dmu_pos_noA3 = np.mean(f_dmu(S_, H0, H1r, G0, G1, U, M) > 0)
print(f"Sweep: dk*/dm > 0 in {share_dm_pos:.4f} of A3 draws; d2k*/dmdu < 0 in {share_dmu_neg:.4f} of A3 draws;"
      f" d2k*/dmdu > 0 in {share_dmu_pos_noA3:.4f} of draws violating A3")

p1_ok = p1_match and share_dm_pos == 1.0
print("VERDICT: Prop. 1 —", "UPHELD (Appendix derivative correct; positive on the whole domain)" if p1_ok
      else "NOT UPHELD (see lines above)")
if (not p2_appendix_match) and numer_ok and share_dmu_neg == 1.0:
    print("VERDICT: Prop. 2 — REFUTED under the manuscript's own A3: the Appendix omits H'(u)=h1; "
          "the cross-partial has the sign of g1*h0 - h1*(s+g0), which A3 makes negative for all u>=0, m in [0,1).")
elif p2_appendix_match:
    print("VERDICT: Prop. 2 — Appendix expression matches the re-derivation; probe finding p10:fnd:3 not supported.")
else:
    print("VERDICT: Prop. 2 — INCONCLUSIVE (Appendix mismatch but sign under A3 not uniformly negative; inspect output).")

# ---------- Part B: H2 on the Phi scale (§2.4) ----------
# Phi(m,u) = F(k*(m,u)), F = CDF of spending-weighted specificity on [0,1]. Beta shapes are illustrative only:
# the manuscript does not state F, which is the point of p10:fnd:10.
par = dict(s=0.2, g0=0.3, g1=0.1, h0=1.0, h1=0.5)   # A3: 0.5 > 0.1/0.5 = 0.2
assert par['h1']/par['h0'] > par['g1']/(par['s'] + par['g0'])
def kst(mm, uu, p=par):
    return (p['s'] + p['g0'] + p['g1']*uu) / ((p['h0'] + p['h1']*uu)*(1 - mm))
def Phi(mm, uu, a, b):
    return stats.beta.cdf(np.minimum(kst(mm, uu), 1.0), a, b)
def mixed(f, mm, uu, h=1e-4):
    return (f(mm+h, uu+h) - f(mm+h, uu-h) - f(mm-h, uu+h) + f(mm-h, uu-h)) / (4*h*h)
rows = []
for (a, b) in [(1, 1), (2, 5), (5, 2), (2, 2), (0.5, 0.5)]:
    for mm in np.linspace(0.05, 0.5, 10):
        for uu in np.linspace(0.01, 3.0, 10):
            if kst(mm, uu) >= 1 - 1e-3:
                continue                                   # corner: all functions outsourced
            kmu = float(f_dmu(par['s'], par['h0'], par['h1'], par['g0'], par['g1'], uu, mm))
            phimu = mixed(lambda x, y: Phi(x, y, a, b), mm, uu)
            rows.append((a, b, np.sign(kmu), np.sign(phimu)))
rows = np.array(rows)
for (a, b) in sorted(set(map(tuple, rows[:, :2]))):
    sel = (rows[:, 0] == a) & (rows[:, 1] == b)
    print(f"Part B Beta({a},{b}): sign disagreement in {np.mean(rows[sel, 2] != rows[sel, 3]):.2f} of {sel.sum()} interior points")
dis = np.mean(rows[:, 2] != rows[:, 3])
print("VERDICT: H2 scale —", (f"sign of the Phi-scale interaction differs from sign of d2k*/dmdu at {dis:.0%} of interior points; "
      "Prop. 2 alone does not fix the sign on the tested scale") if dis > 0 else
      "sign of the Phi-scale interaction matched sign of d2k*/dmdu at every interior point tried; p10:fnd:10 not supported for these densities")
```

### p10:chk:2

```json
{
  "CheckSpec": {
    "id": "p10:chk:2",
    "binds": ["p10:fnd:21", "p10:fnd:1", "p10:fnd:5", "p10:fnd:9", "p10:cmt:25", "p10:cmt:22"],
    "probe_type": "P-NUM",
    "method": "Arithmetic recomputation from the manuscript's reported numbers, with rounding bounds.",
    "premises": ["§3.1 panel definition", "Table 2 coefficients, SEs, stars, N", "§3.2 SDs", "§4 H1 and H3 text"],
    "expected_output": "VERDICT lines (a) to (f)",
    "libraries": ["numpy", "scipy"]
  }
}
```

```python
# p10:chk:2 — arithmetic recomputation of reported statistics in ms:TEST (§3.1, §3.2, Table 2, §4). Not run by the probe.
import numpy as np
from scipy import stats

R = 0.0005                    # half-unit rounding for 3-decimal entries in Table 2
G = 412                       # clusters (hospitals): Table 2 'Hospitals'
ORDER = {"": 0, "*": 1, "**": 2, "***": 3}
def stars_of(p): return "***" if p < 0.001 else "**" if p < 0.01 else "*" if p < 0.05 else ""
def p_of(t): return 2*stats.t.sf(abs(t), df=G - 1)

# (a) N — §3.1: balanced panel, 412 hospitals, annual 2009-2019, 4,712 hospital-years
years = 2019 - 2009 + 1
print(f"(a) 412 x {years} = {412*years}; reported 4712; 4712/412 = {4712/412:.3f}; "
      f"if 2009 is lost to Peer(t-1): {412*(years-1)}")
print("VERDICT: (a) N", "CONSISTENT" if 412*years == 4712 else "INCONSISTENT",
      "with a balanced 412-hospital annual 2009-2019 panel")

# (b) stars vs coef/SE — Table 2; legend '*** p<0.001; ** p<0.01; * p<0.05'
cells = [("M1 Peer", 0.137, 0.031, "***"), ("M2 Peer", 0.042, 0.038, ""), ("M3 Peer", 0.039, 0.037, ""),
         ("M4 Peer", 0.036, 0.036, ""), ("M2 Modularity", 0.112, 0.024, "***"), ("M3 Modularity", 0.118, 0.025, "***"),
         ("M4 Modularity", 0.097, 0.023, "***"), ("M3 Uncertainty", 0.084, 0.051, "***"), ("M4 Uncertainty", 0.079, 0.050, ""),
         ("M3 Mod x Unc", -0.061, 0.019, "**"), ("M4 Mod x Unc", -0.058, 0.019, "**"), ("M1 Specificity", -0.094, 0.027, "***"),
         ("M2 Specificity", -0.091, 0.027, "***"), ("M3 Specificity", -0.090, 0.026, "***"),
         ("M4 Specificity", -0.088, 0.026, "***"), ("M4 Staffing", -0.143, 0.029, "***")]
bad = []
for name, b, se, st in cells:
    tmin = max(abs(b) - R, 0)/(se + R); tmax = (abs(b) + R)/(se - R)
    lo, hi = ORDER[stars_of(p_of(tmin))], ORDER[stars_of(p_of(tmax))]
    ok = lo <= ORDER[st] <= hi
    print(f"(b) {name}: |t|={abs(b)/se:.2f}, p={p_of(b/se):.4f}, reported '{st}' -> {'ok' if ok else 'MISMATCH'}")
    if not ok:
        bad.append(name)
print("VERDICT: (b) stars", "CONSISTENT in all cells" if not bad else "INCONSISTENT in: " + ", ".join(bad))

# (c) magnitudes — §4 H1: 'one-standard-deviation increase in modularity (0.24) ... 2.7 percentage points ... about one-sixth of a SD'
b_m, sd_m, sd_phi = 0.112, 0.24, 0.17          # Table 2 M2; §3.2 SDs
eff = b_m*sd_m; frac = eff/sd_phi
c_ok = round(eff*100, 1) == 2.7 and 0.14 <= frac <= 0.19
print(f"(c) effect = {eff*100:.2f} pp; = {frac:.3f} SD of Phi (1/6 = 0.167); within R2 gain M1->M2 = {0.13-0.08:.2f}")
print("VERDICT: (c) H1 magnitudes", "CONSISTENT" if c_ok else "INCONSISTENT",
      f"with text; size is {frac:.2f} SD per SD of m (bears on 'strongly', p10:fnd:9)")

# (d) §4 H3: 'falls by more than two-thirds'
drop = (0.137 - 0.042)/0.137
drop_min = ((0.137 - R) - (0.042 + R))/(0.137 - R)
print(f"(d) fall = {drop:.3f} (min under rounding {drop_min:.3f})")
print("VERDICT: (d) 'more than two-thirds'", "CONSISTENT" if drop_min > 2/3 else "NOT ROBUST TO ROUNDING")

# (e) what the M2 peer estimate licenses (EPI.5; bears on 'rule out', p10:fnd:1)
b1, se1, b2, se2 = 0.137, 0.031, 0.042, 0.038
z = stats.norm.ppf(0.975)
ci = (b2 - z*se2, b2 + z*se2)
delta_min = abs(b2) + stats.norm.ppf(0.95)*se2   # smallest symmetric TOST bound giving equivalence at alpha = .05
print(f"(e) M2 peer 95% CI = [{ci[0]:.3f}, {ci[1]:.3f}]; TOST equivalence needs bounds >= ±{delta_min:.3f} "
      f"(= {delta_min/b1:.0%} of the M1 estimate)")
for rho in (0.0, 0.5, 0.8, 0.9):                 # covariance of M1 and M2 estimates is not reported
    sed = np.sqrt(se1**2 + se2**2 - 2*rho*se1*se2)
    zz = (b1 - b2)/sed
    print(f"(e) M1-M2 difference, assumed corr {rho}: z = {zz:.2f}, p = {2*stats.norm.sf(abs(zz)):.4f}")
print("VERDICT: (e) a null peer effect is", "NOT ESTABLISHED" if ci[1] > 0.5*b1 else "SUPPORTED",
      f"by M2: the 95% CI reaches {ci[1]:.3f}, i.e. {ci[1]/b1:.0%} of the M1 peer estimate")

# (f) implied auxiliary slope (omitted-variable / FWL identity; M1 and M2 share sample, FE and controls, Table 2):
#     b_spec(M1) = b_spec(M2) + b_m(M2) * pi,  pi = coefficient on specificity in the regression of m on M1's regressors
bs1, bs2 = -0.094, -0.091
pi = (bs1 - bs2)/b_m
pis = [((bs1 + d1) - (bs2 + d2))/(b_m + d3) for d1 in (-R, R) for d2 in (-R, R) for d3 in (-R, R)]
corr_bound = max(abs(min(pis)), abs(max(pis)))*0.5/sd_m   # specificity in [0,1] => SD <= 0.5 (raw SDs; within SDs unreported)
print(f"(f) implied pi = {pi:.4f} (rounding range {min(pis):.4f} to {max(pis):.4f}); "
      f"full-range change in specificity <-> {pi/sd_m:.2f} SD of m; |implied corr| <= {corr_bound:.3f} on raw-SD basis")
print("VERDICT: (f) INDICATIVE — conditional on controls and FE, modularity is nearly unrelated to measured specificity "
      f"(pi in [{min(pis):.3f}, {max(pis):.3f}]); if the rating measures effective specificity k(1-m), this does not fit the "
      "§2.2 mechanism (p10:fnd:5). Within-hospital SDs are unreported, so the bound is indicative only.")
```

### p10:chk:3

```json
{
  "CheckSpec": {
    "id": "p10:chk:3",
    "binds": ["p10:fnd:6", "p10:cmt:14", "p10:cmt:16"],
    "probe_type": "P-ID",
    "method": "Simulation from a data-generating process built from the manuscript's own statements. Unobserved time-varying capability drives m and Phi (§3.3 ¶2). Staffing tracks capability and falls with outsourcing (§3.2). True beta_m = 0. Two-way FE with SEs clustered by hospital, as in §3.3.",
    "premises": ["§3.3 ¶2 confounding concern", "§3.2 staffing definition", "§3.1 N=412, T=11", "§3.3 estimator"],
    "expected_output": "VERDICT on whether beta_m 'survives' the staffing control under the null",
    "libraries": ["numpy", "pandas", "statsmodels"]
  }
}
```

```python
# p10:chk:3 — does surviving the in-house-staffing control exclude capability confounding? (ms:TEST §3.3 ¶2; §3.2; Table 2 M4)
# Not run by the probe. Signs and sizes of the capability paths are not given in ms:TEST; several are tried.
import numpy as np
import pandas as pd
import statsmodels.api as sm

rng = np.random.default_rng(3)
N, T = 412, 11                                   # §3.1: 412 hospitals, 2009-2019

def fe_ols(df, y, xs):
    d = df[[y] + xs + ['i', 't']].copy()
    for v in [y] + xs:                           # two-way within transformation, balanced panel (hospital + year FE, §3.3)
        d[v] = d[v] - d.groupby('i')[v].transform('mean') - d.groupby('t')[v].transform('mean') + d[v].mean()
    r = sm.OLS(d[y], d[xs]).fit(cov_type='cluster', cov_kwds={'groups': d['i'].values})   # clustered by hospital (§3.3)
    return r.params, r.tvalues

def one_draw(c_m, c_phi, c_s=1.0, d=0.5, beta_m=0.0):
    i = np.repeat(np.arange(N), T); t = np.tile(np.arange(T), N)
    C = np.cumsum(rng.normal(0, 0.1, (N, T)), axis=1).ravel()   # §3.3: unobserved, time-varying internal IT capability
    m = 0.46 + c_m*C + np.repeat(rng.normal(0, 0.1, N), T) + rng.normal(0, 0.05, N*T)    # capability -> modularity (§3.3)
    phi = (0.31 + beta_m*m + c_phi*C + np.repeat(rng.normal(0, 0.1, N), T)
           + 0.01*t + rng.normal(0, 0.05, N*T))                  # capability -> outsourcing (§3.3); true beta_m = 0
    S = c_s*C - d*phi + rng.normal(0, 0.05, N*T)                 # §3.2: staffing tracks capability; outsourcing removes positions
    df = pd.DataFrame(dict(i=i, t=t, phi=phi, m=m, S=S))
    b2, t2 = fe_ols(df, 'phi', ['m'])                            # Model-2-like (controls omitted)
    b4, t4 = fe_ols(df, 'phi', ['m', 'S'])                       # Model-4-like (adds staffing)
    return b2['m'], t2['m'], b4['m'], t4['m']

refuted = []
for c_m, c_phi in [(0.5, 0.5), (0.5, -0.5), (1.0, 0.3)]:
    out = np.array([one_draw(c_m, c_phi) for _ in range(40)])
    rej2, rej4 = np.mean(np.abs(out[:, 1]) > 1.96), np.mean(np.abs(out[:, 3]) > 1.96)
    print(f"C->m {c_m:+}, C->Phi {c_phi:+}: Model-2-like mean b_m = {out[:, 0].mean():.3f} (reject 0 in {rej2:.0%}); "
          f"Model-4-like mean b_m = {out[:, 2].mean():.3f} (reject 0 in {rej4:.0%}); true b_m = 0")
    if rej4 > 0.5:
        refuted.append((c_m, c_phi))
print("VERDICT:", ("§3.3 ¶2 claim REFUTED for DGP(s) " + str(refuted) + ": with true beta_m = 0 and capability confounding, "
      "beta_m 'survives' the staffing control, so survival cannot exclude capability differences") if refuted else
      "in these DGPs the staffing control removed the capability bias; p10:fnd:6 NOT DEMONSTRATED by simulation "
      "(the claim is still not entailed; see p10:inc:3)")
```

### p10:chk:4

```json
{
  "CheckSpec": {
    "id": "p10:chk:4",
    "binds": ["p10:fnd:2", "p10:cmt:9", "p10:cmt:10"],
    "probe_type": "P-ID (demonstration supporting a P-INF finding)",
    "method": "Two data-generating processes, each with no direct peer term in Phi. (T) Standards diffuse by state, without imitation: the manuscript's §4 reading. (I) Standards diffuse by imitation of peers' interface adoption: the §1 institutional mechanism applied to standards. Each DGP is estimated with the Table 2 M1 and M2 specifications.",
    "premises": ["§2.4 last ¶ (discriminating prediction)", "§4 H3 ('common diffusion of standards across hospitals in the same state')", "§1 ¶1 (imitation of peers under uncertainty)", "§3.2 peer definition", "§3.3 estimator", "§4 Robustness (staggered state timing)"],
    "premise_caveat": "DGP (I) adds one premise not in ms:TEST: that interface adoption, rather than outsourcing directly, is imitated. That is the probe's construction of the rival's strongest form. Parameter values are illustrative.",
    "expected_output": "VERDICT on whether the M1-M2 pattern arises under both DGPs",
    "libraries": ["numpy", "pandas", "statsmodels"]
  }
}
```

```python
# p10:chk:4 — does the §2.4 discriminating prediction discriminate? (ms:TEST §2.4 last ¶; §4 H3; §3.2 Peer; Table 2 M1-M2)
# Not run by the probe.
import numpy as np
import pandas as pd
import statsmodels.api as sm

rng = np.random.default_rng(4)
S, n, T = 50, 8, 12   # ~8 sample hospitals per state (412/50, inferred from §3.1); 12 waves so Peer(t-1) exists for 11 years

def fe_ols(df, y, xs):
    d = df[[y] + xs + ['i', 't']].copy()
    for v in [y] + xs:                            # hospital + year FE (§3.3), balanced panel
        d[v] = d[v] - d.groupby('i')[v].transform('mean') - d.groupby('t')[v].transform('mean') + d[v].mean()
    r = sm.OLS(d[y], d[xs]).fit(cov_type='cluster', cov_kwds={'groups': d['i'].values})   # clustered by hospital (§3.3)
    return r.params, r.tvalues

def simulate(kind, beta=0.11, kappa=0.8):
    N = S*n; st = np.repeat(np.arange(S), n)
    a = rng.normal(0.31, 0.1, N)
    m = np.clip(rng.normal(0.2, 0.05, N), 0, 1)
    L = rng.integers(2, 9, S)                     # staggered state timing (cf. §4 Robustness, requirements 2011-2016)
    is_leader = (np.arange(N) % n) < 2            # DGP I: two early adopters per state
    recs, phi_prev = [], None
    for t in range(T):
        if t > 0:
            if kind == 'T':
                # §4 H3 reading: standards diffuse by state; no imitation anywhere
                m = m + 0.02 + 0.15*(t == L[st]) + rng.normal(0, 0.02, N)
            else:
                # §1 institutional mechanism (imitate peers under uncertainty) applied to adopting standard interfaces
                peer_m = (np.bincount(st, weights=m, minlength=S)[st] - m)/(n - 1)
                jump = 0.5*(t == L[st])*is_leader
                m = m + 0.02 + kappa*np.clip(peer_m - m, 0, None) + jump + rng.normal(0, 0.02, N)
            m = np.clip(m, 0, 1)
        phi = a + beta*m + rng.normal(0, 0.02, N)  # §2.2-2.4: Phi responds to m; NO direct peer term in either DGP
        if phi_prev is not None:
            peer = (np.bincount(st, weights=phi_prev, minlength=S)[st] - phi_prev)/(n - 1)   # §3.2: other same-state hospitals, t-1
            recs.append(pd.DataFrame(dict(i=np.arange(N), t=t, phi=phi, m=m, peer=peer)))
        phi_prev = phi
    return pd.concat(recs, ignore_index=True)

summary = {}
for kind in ('T', 'I'):
    res = []
    for _ in range(20):
        df = simulate(kind)
        b1, t1 = fe_ols(df, 'phi', ['peer'])          # Table 2 M1 analogue
        b2, t2 = fe_ols(df, 'phi', ['peer', 'm'])     # Table 2 M2 analogue
        res.append((b1['peer'], t1['peer'], b2['peer'], t2['peer'], b2['m']))
    res = np.array(res)
    sig1, sig2 = np.mean(np.abs(res[:, 1]) > 1.96), np.mean(np.abs(res[:, 3]) > 1.96)
    summary[kind] = (sig1, sig2)
    label = 'standards diffuse by state, no imitation' if kind == 'T' else 'standards diffuse by imitation'
    print(f"DGP {kind} ({label}): M1 peer mean {res[:, 0].mean():.3f}, significant in {sig1:.0%}; "
          f"M2 peer mean {res[:, 2].mean():.3f}, significant in {sig2:.0%}; M2 b_m mean {res[:, 4].mean():.3f}")
pattern = {k: (v[0] > 0.5 and v[1] <= 0.2) for k, v in summary.items()}
if pattern['T'] and pattern['I']:
    print("VERDICT: the M1-M2 pattern (peer significant without m, not with m) arises BOTH without imitation and under "
          "imitative diffusion of standards; the §2.4 prediction does NOT discriminate economizing from mimicry routed through modularity.")
elif pattern['T']:
    print("VERDICT: pattern arises without imitation but NOT under imitative diffusion in this DGP; demonstration for p10:fnd:2 FAILS here "
          "(the finding then rests on argument alone).")
else:
    print(f"VERDICT: INCONCLUSIVE — the simulated DGPs did not reproduce the manuscript's M1-M2 pattern ({pattern}); adjust the DGP before concluding.")
```

## 5. Summary of findings (provisional, pending Part 2)

| Id | Type | Locus | Severity | Check | Status |
|---|---|---|---|---|---|
| p10:fnd:2 | P-INF | §2.4 last ¶; §4 H3; title | fatal (to the adjudication claim) | p10:chk:4 | asserted |
| p10:fnd:1 | P-INF | Abstract; §4 H3; §5 | damaging | p10:chk:2(e) | asserted |
| p10:fnd:3 | P-DER (cross-type) | Prop. 2; Appendix | damaging | p10:chk:1(A) | asserted |
| p10:fnd:4 | P-INF | §5 ¶2 vs §6 | damaging | none | asserted |
| p10:fnd:5 | P-INF | §2.2; §3.2 specificity; Table 2 | damaging | p10:chk:2(f) | asserted |
| p10:fnd:7 | P-INF | Abstract; §5; §6; event study | damaging | none | asserted |
| p10:fnd:8 | P-INF | Abstract; §6 'economizing' | damaging | none | asserted |
| p10:fnd:11 | P-MEAS | §3.2 peer measure | damaging | none | asserted |
| p10:fnd:19 | P-LIT | §1 ¶1; H3 (rival's strongest form) | damaging (overlaps fnd:2) | none | asserted |
| p10:fnd:6 | P-ID (cross-type) | §3.3 ¶2; Table 2 M4 | fixable | p10:chk:3 | asserted |
| p10:fnd:10 | P-INF | §2.4 H2 derivation | fixable | p10:chk:1(B) | asserted |
| p10:fnd:12 | P-MEAS | §3.2 modularity domain | fixable (may rise) | none | asserted |
| p10:fnd:13 | P-MEAS | §3.1–3.2 single informant | fixable | none | asserted |
| p10:fnd:14 | P-MEAS | §3.2 uncertainty | fixable | none | asserted |
| p10:fnd:15 | P-MEAS | §3.2 specificity rating | fixable | none | asserted |
| p10:fnd:17 | P-LIT | priority claim | fixable | none | asserted |
| p10:fnd:18 | P-LIT | §5.1 TCE contribution | fixable | none | asserted |
| p10:fnd:20 | P-LIT | methods literature | fixable | none | asserted |
| p10:fnd:21 | P-NUM (cross-type) | §3.1 N; Table 2 M3 stars | fixable | p10:chk:2(a,b) | asserted |
| p10:fnd:9 | P-INF | 'strongly' | minor | p10:chk:2(c) | asserted |
| p10:fnd:16 | P-MEAS | Phi as spending share | minor | none | asserted |

**What stands and what does not, if the findings hold.**
- **H1 survives** as a within-hospital association of moderate size (`p10:cmt:7`, `evidenced`).
- **The title's adjudication does not survive.** "Not mimicry" and "rule out mimetic isomorphism" (`p10:cmt:9`, `p10:cmt:11`) need a discriminating design that the paper does not have.
- **The economizing conclusion** (`p10:cmt:12`) and the **mechanism** (`p10:cmt:1`) are unentitled or in tension with the paper's own table.
- **Prop. 2 is probably mis-signed.** If `p10:chk:1` confirms this, the H2 "anomaly" is the model's own prediction under A3, and the legitimacy story in §5 should go.

## 6. Strengths found (step 5)

- **Prop. 1 appears sound.** The Appendix derivative is correct as written. It is asserted pending `p10:chk:1`, part A1.
- **Explicit rival and test criterion.** The manuscript states a rival hypothesis and a discriminating criterion in advance (§2.4 last ¶). That is better practice than is common, even though the criterion fails (`p10:fnd:2`).
- **Contrary result reported.** The negative interaction is reported openly and labelled "contrary to H2" (§4 H2), not buried. The problem lies in the §5 ¶2 rescue, not in the reporting.
- **Formal derivation.** Hypotheses are derived from a formal model, not asserted verbally. That makes the sign error (`p10:fnd:3`) detectable at all.
- **Design.** The panel has hospital and year fixed effects and SEs clustered by hospital. The staggered state requirements are a potentially valuable source of exogenous variation in m, if the estimates are reported and the exclusion restriction is argued.
- **Reported arithmetic.** These look internally consistent, asserted pending `p10:chk:2`:
  - the 2.7-point / one-sixth-SD magnitude;
  - the "more than two-thirds" fall;
  - most of the stars.
- **Limitations.** §5.2 honestly acknowledges CIO reliance and selection into the balanced panel.

## 7. Decisions for the reviewer

1. **`p10:dec:1` Perspective.** No perspective was supplied. Do you accept the working stance (endorse MI1, MI6 and MI8 as used by the manuscript; reject MI7; neutral on MI2, MI3, MI9 and MI10)? If you endorse MI3 and the coercive/mimetic typology, `p10:inc:5` becomes a firm incompatibility rather than perspective-dependent.
2. **`p10:dec:2` Routing.** Keep the cross-type findings `p10:fnd:3`, `p10:fnd:6` and `p10:fnd:21` here, or hand them to the P-DER, P-ID and P-NUM probes.
3. **`p10:dec:3` Severity of the adjudication finding.** Rate `p10:fnd:2` fatal (as proposed), or damaging on the view that the authors can narrow to H1? Also decide whether to consolidate `p10:fnd:2` with `p10:fnd:19`.
4. **`p10:dec:4` Contribution.** Is the overlap with Langlois, Sanchez and Mahoney, and the empirical modularity-outsourcing work (`p10:fnd:18`), damaging to the contribution, or a positioning fix?
5. **`p10:dec:5` Literature.** Every added citation in §3.3 is from memory and "(to verify)". Verify the priority-claim references (`p10:fnd:17`) before anything goes to the authors.
6. **`p10:dec:6` Simulation premise.** `p10:chk:4` adds one premise not in the manuscript: imitative diffusion of interface adoption. Accept it as a fair statement of the rival's strongest form, or treat `p10:fnd:2` as argued only.
7. **`p10:dec:7` Requests to the authors.** Choose which repairs to request. The highest-value ones look to be:
   - correct Prop. 2 (`p10:fnd:3`);
   - CI and equivalence for the peer effect (`p10:fnd:1`);
   - test whether modularity diffuses through peers or mandates (`p10:fnd:2`);
   - function-level outsourcing (`p10:fnd:12`);
   - report the event study (`p10:fnd:7`).

---

# Part 2: disposition after the harness

**Harness outputs read:** `10_checks/p10_chk_1.out.txt` to `p10_chk_4.out.txt`, run 2026-10-23T20:34:26Z to 20:34:30Z. All four exited 0 with empty stderr. Dispositions below rest only on those outputs. Findings with no check stay `asserted`. Part 1 above is unchanged.

**Result in brief.**
- Bound findings: **7 demonstrated, 1 inconclusive, 0 refuted-by-check**. No check showed the manuscript right on a point I had challenged.
- Manuscript claims the checks confirmed:
  - Prop. 1;
  - the H1 magnitudes;
  - the "more than two-thirds" fall;
  - 15 of 16 significance-star cells.
- These are recorded as demonstrated strengths.

## 8. Disposition of bound findings (step 4)

### p10:fnd:3, Prop. 2 sign (P-DER, cross-type): **demonstrated**
- **Harness output (`p10:chk:1`, Part A):**
  - "Appendix expression equals re-derivation: False".
  - The re-derived cross-partial is `-(g0*h1 - g1*h0 + h1*s)/((h0 + h1*u)**2*(m - 1)**2)`.
  - Its numerator equals `g1*h0 - h1*(s+g0)`, which "under A3 ... is -e*g1*h0 | symbolically negative: True".
  - In the sweep, the cross-partial is negative in 1.0000 of A3 draws and positive in 1.0000 of draws violating A3.
  - VERDICT: "Prop. 2 — REFUTED under the manuscript's own A3".
- **Disposition:** under the manuscript's own A3, Prop. 2 as stated is false. `p10:inc:1` is demonstrated.
- **Severity:** damaging (unchanged). The second proposition, and the stated contribution "the effect is amplified by environmental uncertainty" (§1 ¶3), are reversed. H1 is untouched.

### p10:fnd:10, H2 sign on the tested scale (P-INF): **demonstrated; severity raised from fixable to damaging**
- **Harness output (`p10:chk:1`, Part B):** the sign of the interaction on the outsourcing-share (Φ) scale differs from the sign of the cross-partial ∂²k*/∂m∂u at "25% of interior points" overall. By density:

  | Specificity density F | Sign disagreement (of 100 points) |
  |---|---|
  | Beta(0.5,0.5) | 0.00 |
  | Beta(1,1) | 0.00 |
  | Beta(2,2) | 0.19 |
  | Beta(5,2) | 0.04 |
  | Beta(2,5) | 1.00 |

  VERDICT: "Prop. 2 alone does not fix the sign on the tested scale".
- **Disposition:** demonstrated. Take a right-skewed specificity distribution, Beta(2,5), where most spending sits in low-specificity functions. There, the correctly signed (negative) cross-partial gives a **positive** interaction on the Φ scale at every interior point tried. So even the corrected model makes no sign prediction for the estimated m × u coefficient until F is stated.
- **Why the severity rises:**
  - H2 is a main hypothesis.
  - Neither the original H2 nor its corrected version is a test of the model as run.
  - The Table 2 M3 estimate therefore neither confirms nor disconfirms the model without an assumption about F.
- **Caveats:**
  - The Beta shapes are illustrative, and I chose them.
  - Only one parameter set satisfying A3 was used.
  - The finite-difference step was not varied.
- **Repair (sharpened):** state F, or bound f′ at k*, and derive the sign of ∂²Φ/∂m∂u. Alternatively, test at function level.

### p10:fnd:21, reported-statistics inconsistencies (P-NUM, cross-type): **demonstrated**
- **Harness output (`p10:chk:2` a, b):**
  - (a) "412 x 11 = 4532; reported 4712; 4712/412 = 11.437; if 2009 is lost to Peer(t-1): 4120". VERDICT: "N INCONSISTENT with a balanced 412-hospital annual 2009-2019 panel".
  - (b) "M3 Uncertainty: |t|=1.65, p=0.1003, reported '***' -> MISMATCH". The other 15 cells are "ok".
- **Disposition:** both inconsistencies are demonstrated.
  - 4,712 matches neither 412 × 11 nor 412 × 10.
  - The M3 uncertainty coefficient is not significant at 5%, let alone at 0.1%. Because the model includes m × u, that coefficient is the effect of u at m = 0, which lies outside most of the data (mean m = 0.46). It does not bear directly on H1 to H3.
- **Severity:** fixable (unchanged). It rises to damaging if the authors' reconciliation shows the panel is not as §3.1 describes.

### p10:fnd:1, "rule out" from a non-significant coefficient (P-INF): **demonstrated**
- **Harness output (`p10:chk:2` e):**
  - "M2 peer 95% CI = [-0.032, 0.116]; TOST equivalence needs bounds >= ±0.105 (= 76% of the M1 estimate)".
  - VERDICT: "a null peer effect is NOT ESTABLISHED by M2: the 95% CI reaches 0.116, i.e. 85% of the M1 peer estimate".
- **Disposition:** demonstrated. The data cannot exclude a peer effect 85% as large as the one the authors call "apparent".
- **Additional result, partly in the authors' favour:** the M1 to M2 *fall* in the peer coefficient is significant if the two estimates are positively correlated ("corr 0.5: z = 2.71, p = 0.0067"), but not at zero correlation ("z = 1.94, p = 0.0527"). Estimates from nested models on the same sample are typically positively correlated (inference), so "falls" is plausibly supported. "Falls to zero" is not.
- **Severity:** damaging (unchanged).

### p10:fnd:6, staffing control (P-ID, cross-type): **demonstrated**
- **Harness output (`p10:chk:3`):** true b_m = 0 in every DGP.

  | Capability paths | Model-2-like b_m (reject 0) | Model-4-like b_m (reject 0) |
  |---|---|---|
  | C→m +0.5, C→Φ +0.5 | 0.668 (100%) | 0.489 (100%) |
  | C→m +0.5, C→Φ −0.5 | −0.669 (100%) | 0.004 (0%) |
  | C→m +1.0, C→Φ +0.3 | 0.267 (100%) | 0.379 (100%) |

  VERDICT: "§3.3 ¶2 claim REFUTED for DGP(s) [(0.5, 0.5), (1.0, 0.3)]".
- **Disposition:** demonstrated. §3.3 ¶2's universal claim ("cannot be attributed") is refuted by two counterexamples built from §3.2–3.3.
  - In one DGP the control *amplified* the spurious coefficient (0.267 to 0.379).
  - In another it removed the bias. So the control can work, but its success is not entailed (`p10:inc:3` demonstrated).
- **Severity:** fixable (unchanged).

### p10:fnd:2, the discriminating prediction does not discriminate (P-INF): **demonstrated, conditional on `p10:dec:6`**
- **Harness output (`p10:chk:4`):**
  - DGP T: "M1 peer mean 0.117, significant in 85%; M2 peer mean -0.004, significant in 0%".
  - DGP I: "M1 peer mean 0.235, significant in 100%; M2 peer mean 0.015, significant in 10%".
  - VERDICT: "the §2.4 prediction does NOT discriminate economizing from mimicry routed through modularity".
- **Disposition:** demonstrated, given the one added premise flagged in Part 1: interface adoption is what is imitated. The M1 to M2 pattern, which §4 calls "exactly what the transaction-cost account predicts and the institutional account does not", arises under both processes. It is slightly weaker under imitation: the M2 peer coefficient is significant in 10% of replications there.
- **Severity:** fatal to the adjudication claim (title, Abstract, §5 ¶1, §6); not to H1. Unchanged. If the reviewer rejects the added premise, the finding reverts to `asserted` and should be rated damaging.

### p10:fnd:5, mechanism versus the specificity coefficient (P-INF): **inconclusive** (numerical leg)
- **Harness output (`p10:chk:2` f):**
  - "implied pi = -0.0268 (rounding range -0.0359 to -0.0178) ... |implied corr| <= 0.075 on raw-SD basis".
  - VERDICT: "INDICATIVE ... Within-hospital SDs are unreported, so the bound is indicative only".
- **Disposition:** inconclusive, as the check itself states. The small slope is robust to rounding, but near-orthogonality within hospitals cannot be established from the published table.
- **What remains standing:** the argued legs, which stay `asserted`. The mechanism is untested, and the specificity rating's referent is undefined.
- **Severity:** damaging (unchanged).

### p10:fnd:9, "strongly" (P-INF): **demonstrated** (arithmetic leg)
- **Harness output (`p10:chk:2` c):**
  - "effect = 2.69 pp; = 0.158 SD of Phi ... within R2 gain M1->M2 = 0.05".
  - VERDICT: "H1 magnitudes CONSISTENT with text".
- **Disposition:** the manuscript's own magnitudes are confirmed. The size, 0.16 SD per SD of m, is demonstrated. Whether that is "strong" is a judgment, not a check result.
- **Severity:** minor (unchanged).

## 9. Strengths confirmed by the harness (step 5)

- **`ms:Prop1` is demonstrated sound.**
  - "Prop 1: Appendix derivative equals re-derivation: True".
  - "dk*/dm > 0 in 1.0000 of A3 draws".
  - VERDICT: "Prop. 1 — UPHELD".
  - `p10:cmt:4` moves from `argued` to `argued` + demonstrated.
- **H1 reporting is accurate.** The 2.7-point / one-sixth-SD statement (`p10:chk:2` c) and "falls by more than two-thirds" (d, minimum 0.689 under rounding) are both CONSISTENT.
- **Significance stars are correct in 15 of 16 cells.** That includes every cell that bears on H1, H2 and H3 (`p10:chk:2` b).

## 10. Scoreboard updates (`p10:sb`, delta only)

```json
{
  "Scoreboard_delta": {
    "id": "p10:sb",
    "after_harness": true,
    "commitments": [
      {"id": "p10:cmt:4", "entitlement": "argued", "check_result": "demonstrated (p10:chk:1 A1)"},
      {"id": "p10:cmt:5", "entitlement": "unentitled", "check_result": "refuted under A3 (p10:chk:1 A2)"},
      {"id": "p10:cmt:6", "entitlement": "argued", "check_result": "demonstrated (p10:chk:1 A2)"},
      {"id": "p10:cmt:8", "entitlement": "unentitled", "check_result": "derivation refuted; on the Phi scale the sign depends on F (p10:chk:1 B)"},
      {"id": "p10:cmt:9", "entitlement": "unentitled", "check_result": "demonstrated non-discriminating, given p10:dec:6 (p10:chk:4)"},
      {"id": "p10:cmt:11", "entitlement": "unentitled", "check_result": "null not established; CI reaches 85% of M1 estimate (p10:chk:2 e)"},
      {"id": "p10:cmt:14", "entitlement": "unentitled", "check_result": "refuted by counterexample (p10:chk:3)"},
      {"id": "p10:cmt:16", "entitlement": "argued", "check_result": "demonstrated (p10:chk:3)"},
      {"id": "p10:cmt:22", "entitlement": "challenged", "check_result": "size 0.16 SD per SD confirmed (p10:chk:2 c)"},
      {"id": "p10:cmt:25", "entitlement": "unentitled", "check_result": "N inconsistent (p10:chk:2 a)"}
    ],
    "incompatibilities": [
      {"id": "p10:inc:1", "check_result": "demonstrated (p10:chk:1)"},
      {"id": "p10:inc:3", "check_result": "demonstrated (p10:chk:3)"},
      {"id": "p10:inc:4", "check_result": "inconclusive (p10:chk:2 f, indicative only)"}
    ]
  }
}
```

**Knock-on effect on an unbound finding.** `p10:fnd:4` (the legitimacy rescue in §5 ¶2) stays `asserted` and damaging, but its premise has changed.
- **Part 1 said** the corrected model might itself predict the observed negative interaction.
- **The harness now shows two things:**
  - the negative sign holds for ∂²k*/∂m∂u (`p10:chk:1` A);
  - on the Φ scale it holds only for some specificity distributions (B).
- **So the legitimacy story is still unentitled,** and §5 ¶2 still conflicts with §6. But the honest repair is no longer "the model predicts the result". It is to derive the Φ-scale sign under a stated F and to label any such derivation as accommodation (EPI.4).

## 11. Final findings list

| Id | Type | Severity (final) | Status | Basis |
|---|---|---|---|---|
| p10:fnd:2 | P-INF | **fatal** to the adjudication claim (not to H1) | demonstrated, conditional on p10:dec:6 | p10:chk:4 |
| p10:fnd:1 | P-INF | damaging | demonstrated | p10:chk:2 e |
| p10:fnd:3 | P-DER (cross-type) | damaging | demonstrated | p10:chk:1 A |
| p10:fnd:10 | P-INF | **damaging** (raised from fixable) | demonstrated | p10:chk:1 B |
| p10:fnd:5 | P-INF | damaging | inconclusive (numerical leg); argued legs asserted | p10:chk:2 f |
| p10:fnd:4 | P-INF | damaging | asserted | argument; premise revised above |
| p10:fnd:7 | P-INF | damaging | asserted | argument |
| p10:fnd:8 | P-INF | damaging | asserted | argument |
| p10:fnd:11 | P-MEAS | damaging | asserted | argument |
| p10:fnd:19 | P-LIT | damaging (overlaps fnd:2) | asserted | literature, to verify |
| p10:fnd:6 | P-ID (cross-type) | fixable | demonstrated | p10:chk:3 |
| p10:fnd:21 | P-NUM (cross-type) | fixable (damaging if N reflects a data problem) | demonstrated | p10:chk:2 a, b |
| p10:fnd:12 | P-MEAS | fixable (may rise) | asserted | argument |
| p10:fnd:13 | P-MEAS | fixable | asserted | argument |
| p10:fnd:14 | P-MEAS | fixable | asserted | argument |
| p10:fnd:15 | P-MEAS | fixable | asserted | argument |
| p10:fnd:17 | P-LIT | fixable | asserted | literature, to verify |
| p10:fnd:18 | P-LIT | fixable | asserted | literature, to verify |
| p10:fnd:20 | P-LIT | fixable | asserted | literature, to verify |
| p10:fnd:9 | P-INF | minor | demonstrated (arithmetic leg) | p10:chk:2 c |
| p10:fnd:16 | P-MEAS | minor | asserted | argument |

**Overall reading after the harness.**
- **H1 stands** as a correctly reported within-hospital association of about 0.16 SD per SD of modularity.
- **The adjudication does not stand.** "Modularity, not mimicry" and "rule out mimetic isomorphism" fail:
  - the null peer effect is not established (`p10:fnd:1`, demonstrated);
  - the paper's discriminating pattern is reproduced by imitative diffusion of standards (`p10:fnd:2`, demonstrated given p10:dec:6).
- **The theory section has a demonstrated sign error** (`p10:fnd:3`). H2 has no determinate sign on the scale tested (`p10:fnd:10`).
- **The capability robustness claim is refuted by counterexample** (`p10:fnd:6`). The panel size is inconsistent with its description (`p10:fnd:21`).
- **Unchecked by design:** the economizing conclusion, the mechanism and the literature placement are untouched by the harness and remain `asserted`.

## 12. Decisions for the reviewer (final)

1. **`p10:dec:6` Simulation premise** (decide this first; it sets the top severity). Do you accept DGP I in `p10:chk:4` (imitative adoption of interfaces) as a fair statement of the rival's strongest form? If yes, `p10:fnd:2` is demonstrated and fatal to the adjudication claim. If no, it reverts to asserted and damaging.
2. **`p10:dec:3` Framing for the editor.** If the authors would accept narrowing to H1 (dropping "not mimicry", "rule out" and "economizing"), is the fatal rating better conveyed as "fatal unless claims are narrowed"? Consolidate `p10:fnd:2` with `p10:fnd:19`?
3. **`p10:dec:8` Prop. 2.** Accept the demonstrated sign reversal (`p10:fnd:3`) and the raised severity of `p10:fnd:10` (illustrative Beta densities, one parameter set)? Ask the authors to restate H2 with F specified and to label it accommodation?
4. **`p10:dec:9` Numerical requests.** Ask the authors to:
   - reconcile N = 4,712 with 412 hospitals × 2009–2019 and the lagged peer variable;
   - correct the M3 uncertainty stars;
   - report the M1–M2 covariance, or a direct test of the fall in the peer coefficient;
   - run the within-hospital regression of the specificity rating on m that `p10:fnd:5` needs.
5. **`p10:dec:1` Perspective.** Confirm the working stance: MI7 rejected; MI3 and the coercive typology neutral, which leaves `p10:inc:5` perspective-dependent.
6. **`p10:dec:2` Routing.** Keep the three cross-type findings here, or merge them with the P-DER, P-ID and P-NUM probes' outputs, if those probes ran.
7. **`p10:dec:5` Literature.** All P-LIT references remain "(to verify)". Verify `p10:fnd:17` (priority claim) before it goes to the authors.
8. **`p10:dec:4` Contribution.** Is `p10:fnd:18` damaging to the stated contribution, or a positioning fix?


