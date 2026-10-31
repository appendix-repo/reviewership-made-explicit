# p08: Adversarial Probe, Part 1 (steps 1 to 3)

- **Role:** Role 4, Adversarial Probe (capability 3). Instruction set Reviewership v0.1 (23 October 2026).
- **Manuscript:** `ms:TEST`, "Modularity, Not Mimicry: Interoperability Standards and the Diffusion of IT Outsourcing in U.S. Hospitals".
- **Probe types:** P-DER (main): the formal model (§2.2 to §2.4) and the Appendix proofs. P-NUM (secondary): arithmetic in §2 and §4 that bears on the model.
- **Status:** Part 1. No check has been run. Every finding below is `asserted`. Step 4 (disposition) waits for the harness output (Part 2).
- **Scope discipline:** I was not assigned P-ID, P-MEAS, P-INF or P-LIT. Points I noticed under those headings are listed in §5 as *referrals*. They are not findings and carry no severity.

---

## 1. Reconstruction (L14 ArgMap)

`ms:` loci follow the manuscript's own numbering. The step type is the one the manuscript claims or implies. Where I disagree with it, I say so.

| Id | Step | Locus | Type (as presented) | Probe note |
|---|---|---|---|---|
| `p08:arg:1` | Costs: $C_B = p - s + H(u)\,k(1-m)$, $C_M = p + G(u)$ | `ms:§2.2` | stipulation | modelling premise |
| `p08:arg:2` | $H(u)=h_0+h_1u$, $G(u)=g_0+g_1u$; $s,h_0,h_1,g_0,g_1>0$; $u\ge 0$; $m\in[0,1)$; $k\in[0,1]$ | `ms:§2.1`, `ms:§2.2` | stipulation | domain premise |
| `p08:arg:3` | Assumption A3: $h_1/h_0 > g_1/(s+g_0)$, motivated by Williamson (1991) | `ms:§2.2` | stipulation (deferred) | **No Appendix proof invokes A3.** It is the only numbered assumption, and A1 and A2 do not appear. |
| `p08:arg:4` | Buy iff $k < k^* = (s+G)/(H(1-m))$ | `ms:§2.3` | deductive from arg:1, arg:2 | sound (pending `p08:chk:1`) |
| `p08:arg:5` | Prop. 1: $\partial k^*/\partial m > 0$ | `ms:Prop1`, `ms:App.P1` | deductive from arg:4 | sound (pending `p08:chk:1`) |
| `p08:arg:6` | Prop. 2: $\partial^2 k^*/\partial m\,\partial u > 0$ | `ms:Prop2`, `ms:App.P2` | presented as deductive from arg:4 | **invalid step:** the proof treats $H(u)$ as constant in $u$ (`p08:fnd:1`) |
| `p08:arg:7` | $\Phi$ = spending-weighted share with $k<k^*$; Prop. 1 gives H1 and Prop. 2 gives H2 | `ms:§2.4` | presented as deductive | hidden auxiliary about the distribution of $k$ (`p08:fnd:4`) |
| `p08:arg:8` | Rival H3, with a discriminating test: the peer coefficient conditional on $m$ | `ms:§2.4` | eliminative | out of probe scope (§5) |
| `p08:arg:9` | Table 2 → H1 supported, H3 not supported, H2 "contrary" | `ms:§4` | inductive | P-NUM on the arithmetic (`p08:fnd:6`, `p08:fnd:7`) |
| `p08:arg:10` | The negative interaction is explained by legitimacy and signalling pressures "that our model abstracts from" | `ms:§5` ¶2 | abductive, unlabelled | the corrected model predicts this sign itself (`p08:fnd:2`) |

**The derivation in brief (my inference, for `p08:chk:2` to verify).** Write $N = s+G(u)$ and $\Delta \equiv g_1h_0 - h_1(s+g_0)$. Then:

- $\partial k^*/\partial m = N/(H(1-m)^2)$
- $\partial k^*/\partial u = \Delta/(H^2(1-m))$
- $\partial^2 k^*/\partial m\,\partial u = \Delta/(H^2(1-m)^2)$

Multiplying A3 by $h_0(s+g_0)>0$ shows that A3 is equivalent to $\Delta<0$. Under the manuscript's own A3, then, the cross-partial is **negative** at every admissible $(m,u)$. Proposition 2 holds only if A3 is reversed.

---

## 2. Scoreboard

```json
{
  "Scoreboard": {
    "scorekeeper": "p08 (Adversarial Probe; P-DER, P-NUM)",
    "manuscript": "ms:TEST",
    "endorsed_material_inferences": [],
    "note": "No INF.2 catalogue entry is needed for the P-DER results. They follow from the manuscript's stipulations by calculus alone. MI8 is avowed by the authors (cmt:2) and is recorded without endorsing or challenging it.",
    "commitments": [
      {"id": "p08:cmt:1", "content": "C_B = p - s + H(u) k (1-m); C_M = p + G(u)", "locus": "ms:§2.2", "kind": "avowed", "entitlement": "default", "basis": "stipulated model; TCE framing deferred to Williamson (1975, 1985)"},
      {"id": "p08:cmt:2", "content": "Effective specificity is k(1-m): modularity scales down the relationship-specific component (MI8)", "locus": "ms:§2.2", "kind": "avowed", "entitlement": "deferred", "basis": "Baldwin & Clark (2000); Langlois (2002); Sanchez & Mahoney (1996)"},
      {"id": "p08:cmt:3", "content": "H(u) = h0 + h1 u, G(u) = g0 + g1 u; s, h0, h1, g0, g1 > 0; u >= 0; m in [0,1)", "locus": "ms:§2.2", "kind": "avowed", "entitlement": "default", "basis": "stipulated"},
      {"id": "p08:cmt:4", "content": "A3: h1/h0 > g1/(s+g0)", "locus": "ms:§2.2", "kind": "avowed", "entitlement": "deferred", "basis": "Williamson (1991); never invoked in any Appendix proof"},
      {"id": "p08:cmt:5", "content": "Buy iff k < k*(m,u) = (s+G(u))/(H(u)(1-m))", "locus": "ms:§2.3", "kind": "avowed", "entitlement": "argued", "basis": "ms:§2.3 algebra; scorekeeper concurs pending p08:chk:1"},
      {"id": "p08:cmt:6", "content": "Prop. 1: dk*/dm = (s+G)/(H(1-m)^2) > 0", "locus": "ms:Prop1; ms:App.P1", "kind": "avowed", "entitlement": "argued", "basis": "ms:App.P1; scorekeeper concurs pending p08:chk:1"},
      {"id": "p08:cmt:7", "content": "Prop. 2: d2k*/dm du = g1/(H(1-m)^2) > 0", "locus": "ms:Prop2; ms:App.P2", "kind": "avowed", "entitlement": "challenged", "basis": "the Appendix drops the term -(s+G)h1/(H^2(1-m)^2); proposed status: unentitled if p08:chk:2 confirms"},
      {"id": "p08:cmt:8", "content": "d2k*/dm du = (g1 h0 - h1(s+g0))/(H^2(1-m)^2) < 0 at every admissible (m,u)", "locus": "inferred from ms:§2.2, ms:§2.3", "kind": "consequential", "inference": "by cmt:3, cmt:4, cmt:5 and the quotient rule", "entitlement": "argued", "basis": "scorekeeper's derivation, pending p08:chk:2"},
      {"id": "p08:cmt:9", "content": "dk*/du = (g1 h0 - h1(s+g0))/(H^2(1-m)) < 0: uncertainty narrows the set of outsourced functions", "locus": "inferred from ms:§2.2, ms:§2.3", "kind": "consequential", "inference": "by cmt:3, cmt:4, cmt:5", "entitlement": "argued", "basis": "pending p08:chk:2, p08:chk:5"},
      {"id": "p08:cmt:10", "content": "dPhi/du <= 0 for any spending-weighted distribution of k", "locus": "inferred from ms:§2.4", "kind": "consequential", "inference": "by cmt:9 and the definition of Phi in ms:§2.4", "entitlement": "argued", "basis": "pending p08:chk:3, p08:chk:5; the authors neither state nor test it"},
      {"id": "p08:cmt:11", "content": "Prop. 1 implies H1 (\"Proposition 1 implies that hospitals with higher modularity outsource a larger share\")", "locus": "ms:§2.4", "kind": "avowed", "entitlement": "argued", "basis": "valid (weakly) for any distribution of k that does not move with m; pending p08:chk:3"},
      {"id": "p08:cmt:12", "content": "Prop. 2 implies H2", "locus": "ms:§2.4", "kind": "avowed", "entitlement": "challenged", "basis": "its premise is challenged (cmt:7), and on the Phi scale the sign depends on the distribution of k (pending p08:chk:3)"},
      {"id": "p08:cmt:13", "content": "\"where uncertainty is high, the hold-up hazards that modularity neutralizes are most costly, so the value of modularity is greatest\"", "locus": "ms:§2.3", "kind": "avowed", "entitlement": "challenged", "basis": "true of the per-function cost saving, false of the threshold k* (pending p08:chk:2)"},
      {"id": "p08:cmt:14", "content": "The negative interaction reflects legitimacy and signalling pressures outside the model and is \"consistent with our theory\"", "locus": "ms:§5 ¶2", "kind": "avowed", "entitlement": "challenged", "basis": "an unlabelled abductive auxiliary; unnecessary if cmt:8 holds"},
      {"id": "p08:cmt:15", "content": "Table 2 coefficients, SEs and stars; N = 4,712 from a balanced panel of 412 hospitals, 2009 to 2019", "locus": "ms:§3.1; ms:T2", "kind": "avowed", "entitlement": "challenged", "basis": "internal consistency questioned (pending p08:chk:4)"},
      {"id": "p08:cmt:16", "content": "§4 arithmetic: 1 SD of m gives 2.7 pp (\"about one-sixth\" of an SD); the peer coefficient \"falls by more than two-thirds\"", "locus": "ms:§4 H1, H3", "kind": "avowed", "entitlement": "argued", "basis": "scorekeeper concurs pending p08:chk:4"},
      {"id": "p08:cmt:17", "content": "\"Its substance is economizing\"; the results \"rule out mimetic isomorphism\"", "locus": "ms:§6; ms:Abstract; ms:§5", "kind": "avowed", "entitlement": "challenged", "basis": "outside probe scope; recorded only for inc:4 (referred to P-INF)"}
    ],
    "incompatibilities": [
      {"id": "p08:inc:1", "between": ["p08:cmt:7", "p08:cmt:8"], "reason": "Under cmt:3 to cmt:5, the sign of the cross-partial is the sign of g1 h0 - h1(s+g0), and A3 (cmt:4) makes that negative. Prop. 2 holds iff A3 is reversed.", "pending": "p08:chk:2"},
      {"id": "p08:inc:2", "between": ["p08:cmt:7", "p08:cmt:4"], "reason": "Prop. 2 is equivalent to dk*/du > 0, i.e. uncertainty favouring the market. That is the opposite of the Williamson (1991) premise the authors cite to motivate A3 (\"markets are less able than hierarchies to adapt to disturbances\").", "pending": "p08:chk:2"},
      {"id": "p08:inc:3", "between": ["p08:cmt:15", "p08:cmt:15"], "reason": "A balanced panel of 412 hospitals over 2009 to 2019 gives 4,532 hospital-years (4,120 if the t-1 peer lag drops 2009). 4,712 is not a multiple of 412.", "pending": "p08:chk:4"},
      {"id": "p08:inc:4", "between": ["p08:cmt:14", "p08:cmt:17"], "reason": "Tension, referred to P-INF. For a scorekeeper who endorses MI10, §5 brings in an institutional (legitimacy) mechanism to explain the one result the model is said to miss, while §6 says the substance is economizing. The tension dissolves if p08:fnd:1 is accepted.", "pending": null}
    ],
    "challenges": [
      {"id": "p08:chl:1", "on": "p08:cmt:7", "request": "Give a valid derivation of Prop. 2, or state the parameter restriction under which it holds. The Appendix step \"the cross-partial is determined by how the numerator responds to uncertainty\" ignores that H(u) in the denominator varies with u."},
      {"id": "p08:chl:2", "on": "p08:cmt:4", "request": "A3 is stated but no proof uses it. What work does it do? (On my derivation it signs dk*/du and the cross-partial, both negative.)"},
      {"id": "p08:chl:3", "on": "p08:cmt:12", "request": "State the assumption on the spending-weighted distribution of k under which a sign on k* carries over to Phi, the scale the hypotheses are tested on."},
      {"id": "p08:chl:4", "on": "p08:cmt:14", "request": "Why appeal to a mechanism outside the model when the model, correctly derived, predicts the observed sign?"},
      {"id": "p08:chl:5", "on": "p08:cmt:3", "request": "The model takes u >= 0 but the measure is a z-score (ms:§3.2), so H(u) can be <= 0. State how the measure maps to the model's u."},
      {"id": "p08:chl:6", "on": "p08:cmt:15", "request": "Reconcile N = 4,712 with the balanced-panel design, and correct the stars on Model 3 uncertainty."},
      {"id": "p08:chl:7", "on": "p08:cmt:10", "request": "The model under A3 predicts dPhi/du <= 0 at every m. Report and test this, which needs cov(b2, b3)."}
    ]
  }
}
```

---

## 3. Findings (step 2)

All findings are `asserted` until the harness has run their checks.

```json
{
  "Findings": [
    {
      "id": "p08:fnd:1",
      "probe_type": "P-DER",
      "locus": "ms:Prop2; ms:App.P2 (\"Modularity operates on the denominator of k* only through the factor (1-m)\"); ms:§2.2 A3",
      "commitment": "p08:cmt:7",
      "incompatibility": ["p08:inc:1", "p08:inc:2"],
      "missing_entitlement": "The Appendix differentiates dk*/dm with respect to u as if H(u) were constant. The full cross-partial is [g1 H - (s+G) h1]/[H^2(1-m)^2] = [g1 h0 - h1(s+g0)]/[H^2(1-m)^2]. Its sign depends on neither m nor u, and A3 is exactly the condition that makes it negative. The printed expression g1/(H(1-m)^2) is correct only if h1 = 0, which §2.2 rules out (h1 > 0). Under the manuscript's own assumptions, Prop. 2 is false at every admissible (m,u).",
      "severity": "damaging",
      "severity_reason": "Not fatal to the central claim, because H1 and the H3 comparison do not rest on Prop. 2. But one of the two propositions, contribution 1 as stated (§1), the §2.3 intuition, H2, and the whole of §5 ¶2 do rest on it.",
      "repair": "Correct the proof. Restate Prop. 2 with a negative sign under A3, or drop A3 and state the sign condition. Revise H2, and rewrite or delete §5 ¶2. Say plainly that the corrected prediction was derived after Table 2 was seen, so it counts as accommodation, not novel prediction (EPI.4).",
      "check": "p08:chk:2",
      "status": "asserted"
    },
    {
      "id": "p08:fnd:2",
      "probe_type": "P-DER",
      "locus": "ms:§4 H2 (\"negative and significant (Model 3), contrary to H2\"); ms:§5 ¶2; ms:T2.M3.interaction",
      "commitment": "p08:cmt:14",
      "incompatibility": ["p08:inc:4"],
      "missing_entitlement": "The authors call the negative interaction (-0.061, Model 3; -0.058, Model 4) an anomaly and explain it by a mechanism the model \"abstracts from\". Correctly derived under A3, the model predicts a negative m-by-u cross-partial on k*. Nothing in the paper justifies leaving the model, and the auxiliary (legitimacy signalling) is an unlabelled abductive move.",
      "severity": "fixable",
      "severity_reason": "Follows from fnd:1, and the repair is easy. It has a cost: the corrected sign becomes accommodation. Carrying the sign from k* to Phi also needs the auxiliary in fnd:4.",
      "repair": "Drop the legitimacy auxiliary or present it as a labelled conjecture. Report the corrected model's prediction, and say that it was derived after the data were seen.",
      "check": "p08:chk:2 (sign on k*); p08:chk:3 (carry-over to Phi)",
      "status": "asserted"
    },
    {
      "id": "p08:fnd:3",
      "probe_type": "P-DER",
      "locus": "ms:§2.3 (\"where uncertainty is high, the hold-up hazards that modularity neutralizes are most costly\")",
      "commitment": "p08:cmt:13",
      "missing_entitlement": "The intuition holds for the cost saving modularity yields on a given function, d2(C_M - C_B)/dm du = h1 k > 0. It does not hold for the threshold. Higher u raises the hazard on every function, which lowers k*, and modularity's effect on the threshold, dk*/dm = k*/(1-m), is proportional to k*. The intuition runs these two together.",
      "severity": "minor",
      "repair": "Separate the per-function value of modularity from its effect on the outsourcing threshold. This is absorbed into the fnd:1 repair.",
      "check": "p08:chk:2",
      "status": "asserted"
    },
    {
      "id": "p08:fnd:4",
      "probe_type": "P-DER",
      "locus": "ms:§2.4 ¶1 (\"Since functions with k<k* are outsourced, Proposition 1 implies ...\")",
      "commitment": "p08:cmt:12",
      "missing_entitlement": "Write Phi = F(k*), with F the spending-weighted CDF of nominal k and density f, assumed fixed in m and u (§2.4 needs this but does not state it). Then dPhi/dm = f(k*) k*/(1-m) >= 0 for every F, so H1 follows weakly from Prop. 1 (strictly iff f(k*) > 0 and k* < 1). But d2Phi/dm du = Delta/(H^2(1-m)^2) * [f(k*) + k* f'(k*)]. The sign on the tested scale therefore also depends on whether k f(k) is increasing at k*, and it reverses where the density's elasticity is below -1. At the corner k* >= 1, Phi = 1 and both effects vanish.",
      "severity": "fixable",
      "repair": "State the needed assumption on F (for example d[k f(k)]/dk > 0 near k*, which a uniform F satisfies), or derive the propositions directly on Phi, the scale the linear FE model tests.",
      "check": "p08:chk:3",
      "status": "asserted"
    },
    {
      "id": "p08:fnd:5",
      "probe_type": "P-DER",
      "locus": "ms:§2.2 A3; ms:§3.3 equation; ms:T2.M3.uncertainty; ms:T2.M4.uncertainty",
      "commitment": "p08:cmt:10",
      "missing_entitlement": "Under A3, dk*/du < 0 everywhere, so dPhi/du <= 0 for any F. This prediction is distribution-free, and the manuscript neither states nor tests it. Table 2 implies dPhi/du = b2 + b3 m = 0.084 - 0.061 m (Model 3) and 0.079 - 0.058 m (Model 4). Both are positive for all m in [0,1), with the zero crossing near m = 1.37. Precision is unknown without cov(b2, b3).",
      "severity": "fixable",
      "severity_reason": "Point estimates run against the model, but on the bounds in p08:chk:5 they are probably not significant. Would become damaging if the authors' vcov shows a significantly positive effect at the sample mean of m.",
      "repair": "State the prediction. Report dPhi/du with SEs at representative m (mean and ±1 SD), or centre m so that b2 is the effect at the mean.",
      "check": "p08:chk:5",
      "status": "asserted"
    },
    {
      "id": "p08:fnd:6",
      "probe_type": "P-NUM",
      "locus": "ms:T2.M3.uncertainty (\"0.084*** (0.051)\")",
      "commitment": "p08:cmt:15",
      "missing_entitlement": "|t| = 0.084/0.051 ≈ 1.65, so p ≈ 0.10, but three stars claim p < 0.001. Model 4's 0.079 (0.050), with no stars, is consistent. The misreport bears on fnd:5.",
      "severity": "fixable",
      "repair": "Correct the stars, and check that the coefficient and SE are as estimated.",
      "check": "p08:chk:4",
      "status": "asserted"
    },
    {
      "id": "p08:fnd:7",
      "probe_type": "P-NUM",
      "locus": "ms:§3.1 (\"balanced panel of 412 ... observed annually from 2009 to 2019 ... 4,712 hospital-year observations\"); ms:T2.Observations",
      "commitment": "p08:cmt:15",
      "incompatibility": ["p08:inc:3"],
      "missing_entitlement": "412 × 11 = 4,532, or 4,120 if the t-1 peer lag drops 2009. 4,712 = 412 × 11.44 is not a multiple of 412, so the sample cannot be the balanced panel described.",
      "severity": "fixable",
      "repair": "Report the correct N, or explain the design (unbalanced panel, extra years, duplicate records). Confirm that the Table 2 estimates use the sample described.",
      "check": "p08:chk:4",
      "status": "asserted"
    },
    {
      "id": "p08:fnd:8",
      "probe_type": "P-DER",
      "locus": "ms:§2.2 (\"u >= 0\", \"m in [0,1)\"); ms:§3.2 (u \"standardized to mean zero and unit variance\"; m a share)",
      "commitment": "p08:cmt:3",
      "missing_entitlement": "The model needs H(u) > 0, but the measured u is a z-score and takes negative values. With H(u) = h0 + h1 u, H <= 0 once u <= -h0/h1, and dividing by H then reverses the buy rule. A measured share m = 1 makes k* undefined. A3 is also the only numbered assumption, with no A1 or A2.",
      "severity": "minor",
      "severity_reason": "The sign results in fnd:1 do not depend on u or m, so the corrected propositions are unaffected.",
      "repair": "State the map from the z-score to the model's u (for example u = z - z_min), or restrict the domain. Number or remove the assumption labels.",
      "check": "p08:chk:1",
      "status": "asserted"
    }
  ]
}
```

### 3.1 Strengths and claims found sound (step 5; asserted until the checks run)

- **`p08:S1`**: The threshold $k^*$ follows correctly from $C_B<C_M$, because $C_M - C_B = H(1-m)(k^*-k)$ and $H(1-m)>0$ on the stated domain (`p08:chk:1`).
- **`p08:S2`**: Proposition 1 and its Appendix proof are correct (`p08:chk:1`). H1 follows from Proposition 1 for *every* spending-weighted distribution of $k$, weakly, with no extra assumption (`p08:chk:3`). The paper's main empirical prediction is the formally robust one.
- **`p08:S3`**: The §4 arithmetic is right (`p08:chk:4`):
  - $0.112\times0.24 = 0.0269 \approx 2.7$ pp.
  - $0.0269/0.17 \approx 0.16$ SD, so "about one-sixth" is fair.
  - $(0.137-0.042)/0.137 = 0.69 > 2/3$, and this survives rounding.
  - Every other star in Table 2 matches its coefficient and SE.
- **`p08:S4`**: The model is transparent enough that the error in fnd:1 can be located in one line and repaired. Once repaired, the model's cross-partial has the sign observed in Table 2, which is good news for the authors' framework, though as accommodation.

---

## 4. Checks (step 3; not run)

Each check is self-contained and builds its premises from the manuscript's own statements, cited in comments. It prints detail lines and one or more lines beginning `VERDICT:`, each tagged with the finding or strength it settles.

```json
{
  "CheckSpecs": [
    {"id": "p08:chk:1", "finding_ids": ["p08:fnd:8", "p08:S1", "p08:S2"], "binding": "symbolic re-derivation (sympy) + numeric cross-check", "libraries": ["sympy", "numpy"], "premise_loci": ["ms:§2.2", "ms:§2.3", "ms:App.P1", "ms:§3.2"], "expected_verdict_lines": 3},
    {"id": "p08:chk:2", "finding_ids": ["p08:fnd:1", "p08:fnd:2", "p08:fnd:3"], "binding": "symbolic re-derivation (sympy) + finite differences + random parameter draws", "libraries": ["sympy", "numpy"], "premise_loci": ["ms:§2.2", "ms:§2.2 A3", "ms:§2.3", "ms:App.P2"], "expected_verdict_lines": 4},
    {"id": "p08:chk:3", "finding_ids": ["p08:fnd:4", "p08:S2"], "binding": "symbolic chain rule (sympy) + explicit distributions (scipy)", "libraries": ["sympy", "numpy", "scipy"], "premise_loci": ["ms:§2.4", "ms:§2.2", "ms:§2.3", "ms:§3.2"], "expected_verdict_lines": 2},
    {"id": "p08:chk:4", "finding_ids": ["p08:fnd:6", "p08:fnd:7", "p08:S3"], "binding": "arithmetic recomputation", "libraries": ["numpy", "scipy"], "premise_loci": ["ms:T2", "ms:§3.1", "ms:§3.2", "ms:§4"], "expected_verdict_lines": 3},
    {"id": "p08:chk:5", "finding_ids": ["p08:fnd:5"], "binding": "symbolic sign (sympy) + arithmetic on Table 2 with covariance bounds", "libraries": ["sympy", "numpy", "scipy"], "premise_loci": ["ms:§2.2 A3", "ms:§2.4", "ms:§3.3", "ms:T2.M3", "ms:T2.M4", "ms:§3.2"], "expected_verdict_lines": 1}
  ]
}
```

### p08:chk:1

```python
# CheckSpec p08:chk:1: threshold derivation, Proposition 1, model domain
# Settles: p08:S1, p08:S2 (Prop. 1 part), p08:fnd:8
# Premises, from the manuscript only:
#   ms:§2.2  C_B = p - s + H(u) k (1-m);  C_M = p + G(u)
#   ms:§2.2  H(u) = h0 + h1 u;  G(u) = g0 + g1 u;  s, h0, h1, g0, g1 > 0;  u >= 0;  m in [0,1)
#   ms:§2.3  buy iff C_B < C_M iff k < k* = (s + G(u)) / (H(u)(1-m))
#   ms:App   dk*/dm = (s + G(u)) / (H(u)(1-m)^2) > 0
#   ms:§3.2  u is "standardized to mean zero and unit variance" (negative values occur)
import sympy as sp
import numpy as np

p, s, g0, g1, h0, h1, k = sp.symbols('p s g0 g1 h0 h1 k', positive=True)
u = sp.symbols('u', nonnegative=True)
m = sp.symbols('m', real=True)
w = sp.symbols('w', positive=True)            # w = 1 - m > 0 on m in [0,1)

G = g0 + g1*u
H = h0 + h1*u
CB = p - s + H*k*(1 - m)
CM = p + G
kstar = (s + G) / (H*(1 - m))

# (a) Threshold: C_M - C_B = H(1-m)(k* - k), and H(1-m) > 0 on the domain
identity = sp.simplify((CM - CB) - H*(1 - m)*(kstar - k))
ok_threshold = (identity == 0)
factor_positive = (sp.simplify(H*w).is_positive is True)
print("C_M - C_B - H(1-m)(k*-k) simplifies to:", identity)
print("H(u)(1-m) > 0 on domain:", factor_positive)

# (b) Proposition 1: the Appendix expression and its sign
dk_dm = sp.diff(kstar, m)
appendix_P1 = (s + G) / (H*(1 - m)**2)
ok_P1_expr = (sp.simplify(dk_dm - appendix_P1) == 0)
ok_P1_sign = (sp.simplify(appendix_P1.subs(m, 1 - w)).is_positive is True)
print("dk*/dm =", sp.simplify(dk_dm), "| matches Appendix:", ok_P1_expr, "| positive on domain:", ok_P1_sign)

# numeric cross-check on random admissible draws
rng = np.random.default_rng(8)
f_k = sp.lambdify((s, g0, g1, h0, h1, u, m), kstar, 'numpy')
f_d = sp.lambdify((s, g0, g1, h0, h1, u, m), appendix_P1, 'numpy')
n = 20000
S, G0, G1, H0, H1 = (rng.uniform(0.05, 3.0, n) for _ in range(5))
U = rng.uniform(0.0, 5.0, n)
M = rng.uniform(0.0, 0.95, n)
eps = 1e-6
fd = (f_k(S, G0, G1, H0, H1, U, M + eps) - f_k(S, G0, G1, H0, H1, U, M - eps)) / (2*eps)
an = f_d(S, G0, G1, H0, H1, U, M)
num_ok = bool(np.allclose(fd, an, rtol=1e-4, atol=1e-8) and (an > 0).all())
print("numeric: finite differences match Appendix dk*/dm and all > 0:", num_ok)

# (c) Domain: the measured u is a z-score (ms:§3.2), but the model needs H(u) > 0
z = sp.symbols('z', real=True)
root = sp.solve(sp.Eq(h0 + h1*z, 0), z)[0]           # H = 0 at z = -h0/h1
example = {h0: 1, h1: sp.Rational(1, 2)}
H_at = (h0 + h1*(-3)).subs(example)                    # a hospital 3 SD below mean uncertainty
flip = bool(H_at < 0)
print("H(z) = 0 at z =", root, "| example h0=1, h1=1/2, z=-3: H =", H_at,
      "-> C_M - C_B = H(1-m)(k*-k) means buy iff k > k* (rule reverses):", flip)
print("k* at m = 1:", kstar.subs(m, 1))

print("VERDICT: p08:S1 threshold derivation", "CONFIRMED" if (ok_threshold and factor_positive) else "NOT CONFIRMED")
print("VERDICT: p08:S2 Proposition 1 (expression and sign)",
      "CONFIRMED" if (ok_P1_expr and (ok_P1_sign or num_ok) and num_ok) else "NOT CONFIRMED")
print("VERDICT: p08:fnd:8",
      "DEMONSTRATED: with u measured as a z-score, H(u) <= 0 is possible (u <= -h0/h1) and the buy rule reverses; k* undefined at m = 1"
      if flip else "NOT DEMONSTRATED")
```

### p08:chk:2

```python
# CheckSpec p08:chk:2: Proposition 2, its Appendix proof, A3, and the §2.3 intuition
# Settles: p08:fnd:1, p08:fnd:2 (sign on k*), p08:fnd:3; also p08:inc:1, p08:inc:2
# Premises, from the manuscript only:
#   ms:§2.2  H(u) = h0 + h1 u;  G(u) = g0 + g1 u;  s, h0, h1, g0, g1 > 0;  u >= 0;  m in [0,1)
#   ms:§2.2  Assumption A3: h1/h0 > g1/(s + g0)
#   ms:§2.2  C_B = p - s + H(u) k (1-m);  C_M = p + G(u)
#   ms:§2.3  k* = (s + G(u)) / (H(u)(1-m));  Prop. 2 claims d2k*/dm du > 0
#   ms:App   "d2k*/dm du = G'(u)/(H(u)(1-m)^2) = g1/(H(u)(1-m)^2) > 0"
import sympy as sp
import numpy as np

s, g0, g1, h0, h1, k = sp.symbols('s g0 g1 h0 h1 k', positive=True)
u = sp.symbols('u', nonnegative=True)
m = sp.symbols('m', real=True)
w = sp.symbols('w', positive=True)            # w = 1 - m

G = g0 + g1*u
H = h0 + h1*u
kstar = (s + G) / (H*(1 - m))

# (1) Full cross-partial vs the Appendix expression
cross = sp.diff(kstar, m, u)
appendix_P2 = g1 / (H*(1 - m)**2)
Delta = g1*h0 - h1*(s + g0)
closed = Delta / (H**2 * (1 - m)**2)
ok_closed = (sp.simplify(cross - closed) == 0)
appendix_matches = (sp.simplify(cross - appendix_P2) == 0)
omitted = sp.simplify(cross - appendix_P2)
ok_omitted = (sp.simplify(omitted - (-(s + G)*h1 / (H**2 * (1 - m)**2))) == 0)
appendix_ok_only_if_h1_zero = (sp.simplify((cross - appendix_P2).subs(h1, 0)) == 0)
print("full cross-partial      =", sp.factor(sp.simplify(cross)))
print("closed form Delta/(H^2(1-m)^2), Delta = g1*h0 - h1*(s+g0); matches:", ok_closed)
print("Appendix expression matches full cross-partial:", appendix_matches)
print("term omitted by Appendix =", sp.factor(omitted), "| equals -(s+G)h1/(H^2(1-m)^2):", ok_omitted)
print("Appendix expression correct when h1 = 0 (excluded by ms:§2.2):", appendix_ok_only_if_h1_zero)

# (2) A3 is equivalent to Delta < 0: (h1/h0 - g1/(s+g0)) * h0 (s+g0) = -Delta
ok_A3_equiv = (sp.simplify((h1/h0 - g1/(s + g0))*h0*(s + g0) + Delta) == 0)
denom_pos = ((H**2 * w**2).is_positive is True)
print("A3 <=> Delta < 0:", ok_A3_equiv, "| denominator H^2(1-m)^2 > 0:", denom_pos)

# (3) dk*/du has the same sign (Prop. 2 <=> uncertainty widens outsourcing; inc:2)
ok_dkdu = (sp.simplify(sp.diff(kstar, u) - Delta / (H**2 * (1 - m))) == 0)
print("dk*/du = Delta/(H^2(1-m)):", ok_dkdu)

# (4) Worked example satisfying A3, with finite differences independent of sympy algebra
f_k = sp.lambdify((s, g0, g1, h0, h1, u, m), kstar, 'numpy')
f_c = sp.lambdify((s, g0, g1, h0, h1, u, m), closed, 'numpy')
f_a = sp.lambdify((s, g0, g1, h0, h1, u, m), appendix_P2, 'numpy')

def fd_cross(par, U, M, e=1e-4):
    return (f_k(*par, U + e, M + e) - f_k(*par, U - e, M + e)
            - f_k(*par, U + e, M - e) + f_k(*par, U - e, M - e)) / (4*e*e)

par = (1.0, 1.0, 1.0, 1.0, 2.0)               # s, g0, g1, h0, h1
print("example A3 holds (h1/h0 = 2 > g1/(s+g0) = 0.5):", par[4]/par[3] > par[2]/(par[0] + par[1]))
ex_ok = True
for U0 in (0.0, 0.5, 1.0, 2.0, 5.0):
    for M0 in (0.0, 0.25, 0.5, 0.75):
        fdv, cv, av = fd_cross(par, U0, M0), f_c(*par, U0, M0), f_a(*par, U0, M0)
        ex_ok = ex_ok and np.isclose(fdv, cv, rtol=1e-4) and fdv < 0
        print(f"  u={U0:.2f} m={M0:.2f}  finite-diff={fdv:+.5f}  closed={cv:+.5f}  Appendix={av:+.5f}")

# (5) Random admissible draws: sign of the cross-partial with and without A3
rng = np.random.default_rng(208)
n = 100000
Sx, G0x, G1x, H0x, H1x = rng.uniform(0.2, 3.0, size=(5, n))
Ux = rng.uniform(0.0, 5.0, n)
Mx = rng.uniform(0.0, 0.9, n)
cx = f_c(Sx, G0x, G1x, H0x, H1x, Ux, Mx)
a3 = H1x/H0x > G1x/(Sx + G0x)
n_a3, n_a3_pos = int(a3.sum()), int((cx[a3] > 0).sum())
n_not, n_not_pos = int((~a3).sum()), int((cx[~a3] > 0).sum())
idx = np.arange(5000)
fdx = fd_cross((Sx[idx], G0x[idx], G1x[idx], H0x[idx], H1x[idx]), Ux[idx], Mx[idx])
fd_ok = bool(np.allclose(fdx, cx[idx], rtol=1e-3, atol=1e-3))   # atol covers round-off where Delta is near 0
print(f"draws with A3: {n_a3}, of which cross-partial > 0: {n_a3_pos}")
print(f"draws without A3: {n_not}, of which cross-partial > 0: {n_not_pos}")
print("finite differences agree with closed form on 5000 draws:", fd_ok)

# (6) §2.3 intuition: per-function cost saving vs threshold
saving = (G) - (-s + H*k*(1 - m))             # C_M - C_B, p cancels
ok_saving = (sp.simplify(sp.diff(saving, m, u) - h1*k) == 0)
ok_prop = (sp.simplify(sp.diff(kstar, m) - kstar/(1 - m)) == 0)
print("d2(C_M - C_B)/dm du = h1*k > 0:", ok_saving, "| dk*/dm = k*/(1-m):", ok_prop)

fnd1 = (ok_closed and not appendix_matches and ok_omitted and ok_A3_equiv and denom_pos
        and n_a3_pos == 0 and ex_ok and fd_ok)
print("VERDICT: p08:fnd:1",
      "DEMONSTRATED: Appendix omits -(s+G)h1/(H^2(1-m)^2); true cross-partial = (g1*h0 - h1*(s+g0))/(H^2(1-m)^2); "
      "A3 <=> numerator < 0, so Prop. 2 is false at every admissible (m,u) under A3" if fnd1 else "NOT DEMONSTRATED")
print("VERDICT: p08:inc:2",
      "DEMONSTRATED: Prop. 2 holds iff A3 fails iff dk*/du > 0 (uncertainty favours the market)"
      if (ok_dkdu and n_not_pos == n_not and n_a3_pos == 0) else "NOT DEMONSTRATED")
print("VERDICT: p08:fnd:2",
      "DEMONSTRATED (k* scale): the correctly derived model under A3 predicts a NEGATIVE m x u interaction "
      "(same sign as ms:T2.M3, -0.061) and dk*/du < 0" if (fnd1 and ok_dkdu) else "NOT DEMONSTRATED")
print("VERDICT: p08:fnd:3",
      "DEMONSTRATED: modularity's per-function cost saving rises with u (h1*k > 0), but its threshold effect is "
      "k*/(1-m), which falls with u under A3" if (ok_saving and ok_prop and fnd1) else "NOT DEMONSTRATED")
```

### p08:chk:3

```python
# CheckSpec p08:chk:3: from the threshold k* to the tested outcome Phi (ms:§2.4)
# Settles: p08:fnd:4; p08:S2 (H1 part)
# Premises, from the manuscript only:
#   ms:§2.4  "Let Phi denote the share of a hospital's IT functions, weighted by spending, that are outsourced"
#            "functions with k<k* are outsourced"  =>  Phi = F(k*), F the spending-weighted CDF of nominal k
#            (the manuscript states no assumption on F; we take F fixed in m and u, as §2.4 implicitly needs)
#   ms:§2.2/§2.3  H, G linear; s, h0, h1, g0, g1 > 0; u >= 0; m in [0,1); k* = (s+G)/(H(1-m)); A3
#   ms:§3.2  mean outsourcing share 0.31, SD 0.17
import sympy as sp
import numpy as np
from scipy import stats

s, g0, g1, h0, h1 = sp.symbols('s g0 g1 h0 h1', positive=True)
u = sp.symbols('u', nonnegative=True)
m = sp.symbols('m', real=True)
f, fp = sp.symbols('f fp', real=True)          # f = F'(k*) >= 0, fp = F''(k*)

G = g0 + g1*u
H = h0 + h1*u
kstar = (s + G) / (H*(1 - m))
k_m, k_u, k_mu = sp.diff(kstar, m), sp.diff(kstar, u), sp.diff(kstar, m, u)
Delta = g1*h0 - h1*(s + g0)

# chain rule for Phi = F(k*(m,u))
dPhi_dm = f*k_m
dPhi_du = f*k_u
d2Phi = fp*k_m*k_u + f*k_mu
ok_identity = (sp.simplify(d2Phi - Delta/(H**2*(1 - m)**2)*(f + kstar*fp)) == 0)
ok_dm = (sp.simplify(dPhi_dm - f*kstar/(1 - m)) == 0)
ok_du = (sp.simplify(dPhi_du - f*Delta/(H**2*(1 - m))) == 0)
print("d2Phi/dm du = Delta/(H^2(1-m)^2) * (f(k*) + k* f'(k*)):", ok_identity)
print("dPhi/dm = f(k*) k*/(1-m) >= 0 for any F:", ok_dm)
print("dPhi/du = f(k*) Delta/(H^2(1-m)) (<= 0 under A3, any F):", ok_du)

# Explicit distributions at one admissible point satisfying A3
par = dict(s=0.2, g0=0.2, g1=0.1, h0=1.0, h1=1.0)
a3 = par['h1']/par['h0'] > par['g1']/(par['s'] + par['g0'])

def kst(U, M):
    return (par['s'] + par['g0'] + par['g1']*U) / ((par['h0'] + par['h1']*U)*(1 - M))

def cross_fd(fun, U, M, e=1e-4):
    return (fun(U + e, M + e) - fun(U - e, M + e) - fun(U + e, M - e) + fun(U - e, M - e)) / (4*e*e)

U0, M0 = 1.0, 0.375
k0 = kst(U0, M0)                                # = 0.4, interior
Dl = par['g1']*par['h0'] - par['h1']*(par['s'] + par['g0'])
base = Dl / ((par['h0'] + par['h1']*U0)**2 * (1 - M0)**2)
c_k = cross_fd(kst, U0, M0)
print(f"A3 holds: {a3}; k* = {k0:.4f}; d2k*/dm du: finite-diff {c_k:+.5f}, closed {base:+.5f}")

dists = {"uniform(0,1)": stats.uniform(0, 1), "beta(2,2)": stats.beta(2, 2), "beta(1,5)": stats.beta(1, 5)}
sign = {}
agree = True
for name, d in dists.items():
    Phi = lambda U, M, d=d: d.cdf(np.minimum(kst(U, M), 1.0))
    c_fd = cross_fd(Phi, U0, M0)
    e = 1e-5
    kf_slope = ((k0 + e)*d.pdf(k0 + e) - (k0 - e)*d.pdf(k0 - e)) / (2*e)   # f + k f' at k*
    c_formula = base*kf_slope
    agree = agree and np.isclose(c_fd, c_formula, rtol=1e-3, atol=1e-6)
    sign[name] = np.sign(c_fd)
    print(f"  {name:13s} Phi={d.cdf(k0):.3f}  f+k f'={kf_slope:+.4f}  d2Phi/dm du: finite-diff {c_fd:+.5f}, formula {c_formula:+.5f}")

# Where in the beta(1,5) family does the sign on Phi flip? f + k f' = 5(1-k)^3(1-5k) < 0 iff k > 0.2
phi_flip = 1 - 0.8**5
print(f"beta(1,5): Phi-scale sign flips for hospitals with Phi > {phi_flip:.3f} "
      f"({(phi_flip - 0.31)/0.17:.2f} SD above the ms:§3.2 mean of 0.31)")

fnd4 = (ok_identity and a3 and agree and c_k < 0
        and sign["uniform(0,1)"] < 0 and sign["beta(2,2)"] < 0 and sign["beta(1,5)"] > 0)
print("VERDICT: p08:fnd:4",
      "DEMONSTRATED: under A3 the k*-scale interaction is negative, but the Phi-scale interaction has sign "
      "sign(Delta)*sign(f + k f'), positive for beta(1,5) at k* = 0.4; the step from Prop. 2 to H2 needs an assumption on F"
      if fnd4 else "NOT DEMONSTRATED")
print("VERDICT: p08:S2 (H1 part)",
      "CONFIRMED: dPhi/dm = f(k*) k*/(1-m) >= 0 for every spending-weighted F; H1 follows from Prop. 1 without further assumption"
      if ok_dm else "NOT CONFIRMED")
```

### p08:chk:4

```python
# CheckSpec p08:chk:4: numerical consistency of ms:§3.1, ms:Table 2 and the §4 arithmetic
# Settles: p08:fnd:6, p08:fnd:7, p08:S3
# Premises, from the manuscript only:
#   ms:Table 2 coefficients, clustered SEs, stars; note "*** p < 0.001; ** p < 0.01; * p < 0.05"
#   ms:§3.1 "balanced panel of 412 ... observed annually from 2009 to 2019 ... 4,712 hospital-year observations"
#   ms:§3.2 modularity SD 0.24; outsourcing share SD 0.17
#   ms:§4  "one-standard-deviation increase in modularity (0.24) ... 2.7 percentage points ... about one-sixth of a standard deviation"
#   ms:§4  "the peer coefficient falls by more than two-thirds"
import numpy as np
from scipy import stats

rows = [
    ("T2.M1.peer", 0.137, 0.031, "***"), ("T2.M2.peer", 0.042, 0.038, ""),
    ("T2.M3.peer", 0.039, 0.037, ""), ("T2.M4.peer", 0.036, 0.036, ""),
    ("T2.M2.modularity", 0.112, 0.024, "***"), ("T2.M3.modularity", 0.118, 0.025, "***"),
    ("T2.M4.modularity", 0.097, 0.023, "***"),
    ("T2.M3.uncertainty", 0.084, 0.051, "***"), ("T2.M4.uncertainty", 0.079, 0.050, ""),
    ("T2.M3.interaction", -0.061, 0.019, "**"), ("T2.M4.interaction", -0.058, 0.019, "**"),
    ("T2.M1.specificity", -0.094, 0.027, "***"), ("T2.M2.specificity", -0.091, 0.027, "***"),
    ("T2.M3.specificity", -0.090, 0.026, "***"), ("T2.M4.specificity", -0.088, 0.026, "***"),
    ("T2.M4.staffing", -0.143, 0.029, "***"),
]
N_CLUSTERS = 412                 # ms:§3.1; Table 2 "Hospitals 412"
DF = N_CLUSTERS - 1              # usual reference df for cluster-robust t
HALF = 0.0005                    # values reported to 3 decimals
RANK = {"": 0, "*": 1, "**": 2, "***": 3}

def stars(p):
    return "***" if p < 0.001 else "**" if p < 0.01 else "*" if p < 0.05 else ""

def p_two(z, ref):
    return 2*stats.norm.sf(z) if ref == "normal" else 2*stats.t.sf(z, DF)

inconsistent = []
for name, b, se, rep in rows:
    z = abs(b)/se
    z_lo = (abs(b) - HALF)/(se + HALF)   # smallest |t| compatible with rounding
    z_hi = (abs(b) + HALF)/(se - HALF)   # largest |t| compatible with rounding
    ok_any = False
    for ref in ("t", "normal"):
        lo, hi = RANK[stars(p_two(z_lo, ref))], RANK[stars(p_two(z_hi, ref))]
        if lo <= RANK[rep] <= hi:
            ok_any = True
    pc = p_two(z, "t")
    print(f"{name:20s} b={b:+.3f} se={se:.3f} |t|={z:5.2f} p(t,{DF})={pc:.4g} implied='{stars(pc)}' "
          f"reported='{rep}' {'ok' if ok_any else 'INCONSISTENT'}")
    if not ok_any:
        inconsistent.append(name)

# §4 H1 arithmetic
eff = 0.112*0.24
frac_sd = eff/0.17
ok_27 = (round(100*eff, 1) == 2.7)
ok_sixth = abs(frac_sd - 1/6)/(1/6) < 0.10
print(f"1 SD effect = {eff:.5f} ({100*eff:.2f} pp); share of outcome SD = {frac_sd:.3f} (1/6 = {1/6:.3f})")

# §4 H3 arithmetic, including the least favourable rounding
drop = (0.137 - 0.042)/0.137
drop_min = (0.1365 - 0.0425)/0.1365
ok_twothirds = drop > 2/3 and drop_min > 2/3
print(f"peer coefficient drop = {drop:.3f} (least favourable rounding {drop_min:.3f}); 2/3 = {2/3:.3f}")

# INFO only (referred to P-INF; not a P-NUM finding): 95% CI of the Model 2 peer coefficient
tc = stats.t.ppf(0.975, DF)
lo, hi = 0.042 - tc*0.038, 0.042 + tc*0.038
print(f"INFO: Model 2 peer 95% CI = [{lo:.3f}, {hi:.3f}]; upper bound = {hi/0.137:.0%} of the Model 1 estimate")

# §3.1 sample size
years = 2019 - 2009 + 1
n_bal, n_bal_lag, N_rep = 412*years, 412*(years - 1), 4712
ok_N = N_rep in (n_bal, n_bal_lag)
print(f"412 x {years} = {n_bal}; with t-1 lag dropping 2009: {n_bal_lag}; reported {N_rep}; "
      f"4712/412 = {N_rep/412:.3f}; remainder {N_rep % 412}")

others = [x for x in inconsistent if x != "T2.M3.uncertainty"]
print("VERDICT: p08:fnd:6",
      ("DEMONSTRATED: stars inconsistent with coefficient/SE for " + ", ".join(inconsistent))
      if "T2.M3.uncertainty" in inconsistent else "REFUTED-BY-CHECK: T2.M3.uncertainty stars consistent")
print("VERDICT: p08:fnd:7",
      "DEMONSTRATED: N = 4,712 is incompatible with a balanced panel of 412 hospitals over 2009-2019 (4,532; 4,120 with lag)"
      if not ok_N else "REFUTED-BY-CHECK")
print("VERDICT: p08:S3",
      ("CONFIRMED: 2.7 pp, ~1/6 SD, >2/3 drop correct; all other stars consistent" if (ok_27 and ok_sixth and ok_twothirds and not others)
       else f"NOT CONFIRMED: ok_27={ok_27} ok_sixth={ok_sixth} ok_twothirds={ok_twothirds} other_inconsistent={others}"))
```

### p08:chk:5

```python
# CheckSpec p08:chk:5: the sign of the uncertainty effect implied by A3, against Table 2
# Settles: p08:fnd:5
# Premises, from the manuscript only:
#   ms:§2.2  H, G linear; s, h0, h1, g0, g1 > 0; u >= 0; m in [0,1); A3: h1/h0 > g1/(s+g0)
#   ms:§2.3  k* = (s+G)/(H(1-m));  ms:§2.4 Phi = F(k*)  =>  dPhi/du = f(k*) dk*/du  (see p08:chk:3)
#   ms:§3.3  Phi = b1 m + b2 u + b3 (m x u) + ...  (m entered uncentred; u a z-score)  =>  dPhi/du = b2 + b3 m
#   ms:T2    Model 3: b2 = 0.084 (0.051), b3 = -0.061 (0.019); Model 4: b2 = 0.079 (0.050), b3 = -0.058 (0.019)
#   ms:§3.2  modularity mean 0.46, SD 0.24 (m in [0,1] as a share)
#   cov(b2, b3) is not reported, so SEs of b2 + b3 m are bounded using |corr| <= 1
import sympy as sp
import numpy as np
from scipy import stats

s, g0, g1, h0, h1 = sp.symbols('s g0 g1 h0 h1', positive=True)
u = sp.symbols('u', nonnegative=True)
m = sp.symbols('m', real=True)
H = h0 + h1*u
G = g0 + g1*u
kstar = (s + G) / (H*(1 - m))
num = sp.simplify(sp.diff(kstar, u)*H**2*(1 - m))      # sign of dk*/du (H^2(1-m) > 0)
ok_num = (sp.simplify(num - (g1*h0 - h1*(s + g0))) == 0)
ok_A3 = (sp.simplify((h1/h0 - g1/(s + g0))*h0*(s + g0) + num) == 0)   # A3 <=> num < 0
print("sign(dk*/du) = sign(g1*h0 - h1*(s+g0)):", ok_num, "| A3 <=> dk*/du < 0:", ok_A3)

models = {"M3": (0.084, 0.051, -0.061, 0.019), "M4": (0.079, 0.050, -0.058, 0.019)}
report_at = (0.0, 0.22, 0.46, 0.70, 1.0)               # 0, mean - 1 SD, mean, mean + 1 SD, 1
pos_all, sig_any, zmax_all = True, False, 0.0
for name, (b2, se2, b3, se3) in models.items():
    print(f"{name}: dPhi/du = {b2:+.3f} {b3:+.3f} m; zero crossing at m = {-b2/b3:.2f}")
    for mv in np.linspace(0.0, 1.0, 101):
        me = b2 + b3*mv
        se_hi = se2 + mv*se3                            # corr(b2, b3) = +1 (m >= 0)
        se_lo = abs(se2 - mv*se3)                       # corr(b2, b3) = -1
        z_min = abs(me)/se_hi
        z_max = abs(me)/se_lo if se_lo > 0 else np.inf
        pos_all = pos_all and (me > 0)
        sig_any = sig_any or (2*stats.norm.sf(z_max) < 0.05)
        zmax_all = max(zmax_all, z_max)
        if any(np.isclose(mv, x) for x in report_at):
            print(f"   m={mv:.2f}: estimate {me:+.4f}; SE in [{se_lo:.4f}, {se_hi:.4f}]; "
                  f"|z| in [{z_min:.2f}, {z_max:.2f}]; p in [{2*stats.norm.sf(z_max):.3f}, {2*stats.norm.sf(z_min):.3f}]")

if ok_num and ok_A3 and pos_all and not sig_any:
    v = ("DEMONSTRATED (tension, not refutation): under A3 the model implies dPhi/du <= 0 at every m; "
         "Table 2 point estimates of dPhi/du are positive for all m in [0,1] (M3, M4); none is significant at 5% "
         f"under any cov(b2,b3) (max |z| = {zmax_all:.2f}); the manuscript neither states nor tests the implication")
elif ok_num and ok_A3 and pos_all and sig_any:
    v = ("DEMONSTRATED (possible significant contradiction): estimates positive on [0,1] and significant at 5% "
         "for some admissible cov(b2,b3); authors' vcov needed")
else:
    v = "NOT DEMONSTRATED"
print("VERDICT: p08:fnd:5", v)
```

---

## 5. Referrals outside the assigned probe types (not findings)

Noted while reconstructing the argument and passed to the role or probe that owns each. None of them affects the P-DER or P-NUM results above.

- **P-ID: Model 4 adds a bad control.** §3.2 says "outsourcing a function transfers its staff to the vendor or eliminates the positions", so in-house IT staffing is partly a consequence of the outcome. The claim in §3.3 and §4 that the modularity effect "cannot be attributed to capability differences" needs argument.
- **P-ID / P-MEAS: the asset-specificity control may be the model's mediator.** The asset-specificity measure (§3.2: cost of transferring functions to another provider) plausibly measures *effective* specificity $k(1-m)$, the variable through which the model says modularity works (`ms:§2.2`). Conditioning on it should, under the model, absorb the modularity effect, so the link from model to estimand needs an argument.
- **P-ID: the event study (§4, Robustness).** It is a two-way FE event study under staggered state adoption (2011 to 2016), which raises staggered-adoption bias. It is also a reduced form of state requirements on outsourcing, not an estimate of the effect of modularity.
- **P-INF: H3.** The H3 inference runs from "no longer significant" to "rule out" (MI7). The Model 2 peer CI computed in `p08:chk:4` (INFO line) is for that probe. "Strongly predicts" describes an effect of about 0.16 SD. `p08:inc:4` is also referred here.
- **P-LIT:** "the first study to adjudicate directly between transaction-cost and institutional explanations of IT outsourcing" (Abstract, §1) (to verify).
- **EPI.4:** If `p08:fnd:1` is accepted, the negative interaction is an accommodated result, not a novel prediction. How much that matters is a perspective setting for the reviewer.

---

## 6. Status and hand-off to Part 2

- Bound findings: `p08:fnd:1` to `p08:fnd:8`, all `asserted`.
  - `p08:chk:1`: fnd:8
  - `p08:chk:2`: fnd:1, fnd:2, fnd:3
  - `p08:chk:3`: fnd:4
  - `p08:chk:4`: fnd:6, fnd:7
  - `p08:chk:5`: fnd:5
- Strengths `p08:S1` to `p08:S3` are bound to `p08:chk:1`, `p08:chk:3` and `p08:chk:4`. `p08:S4` depends on `p08:chk:2`.
- Unbound findings: none. Every finding is P-DER or P-NUM and has a check.
- Step 4 (disposition into `demonstrated`, `refuted-by-check` or `inconclusive`, with revised severities) waits for the harness output.

## Decisions for the reviewer

1. **`p08:fnd:1` severity.** Treat the Prop. 2 derivation error as *damaging* (my rating: the central H1/H3 claim survives) or as *fatal to the formal-model contribution* (contribution 1 in §1 rests on two propositions, and one is false under the paper's own A3).
2. **Credit for the corrected model.** Count the corrected model's agreement with the negative interaction in Table 2 in the authors' favour, or discount it as post hoc accommodation (your EPI.4 setting).
3. **Fixing the step to H2 (`p08:fnd:4`).** Ask the authors to derive their propositions directly on $\Phi$, or accept an explicitly stated assumption on the spending-weighted distribution of $k$.
4. **Raising `p08:fnd:5`.** Decide whether to raise the unstated implication $\partial\Phi/\partial u \le 0$ and request the variance-covariance matrix for $b_2 + b_3 m$.
5. **The numerical errors (`p08:fnd:6`, `p08:fnd:7`).** Raise them as routine fixable queries, or treat the N discrepancy as a reason to request data and code (TEC.1).
6. **Referred probes (§5).** Decide whether to commission P-ID (Model 4 control, asset-specificity control, event study), P-INF (H3) and P-LIT (priority claim).
7. **Acceptance of each finding.** Accept, reject or modify each finding once the Part 2 dispositions arrive. Nothing here is to be copied into the review unedited.

---

# Part 2: disposition after the harness

**Harness run.** All five checks ran on 2026-10-23, between 20:31:57Z and 20:32:01Z, each in a fresh isolated interpreter. Every check exited 0 with empty stderr. The outputs are in `/mnt/project-files/reviewership-appendix/runs/08_checks/p08_chk_1.out.txt` to `p08_chk_5.out.txt`. Each disposition below rests on the harness line cited, not on my Part 1 expectation. No check was refuted, and no check failed to run.

## 7. Disposition of bound findings (step 4)

| Finding | Check | Harness evidence | Disposition | Severity (Part 1 → Part 2) |
|---|---|---|---|---|
| `p08:fnd:1` | chk:2 | "Appendix expression matches full cross-partial: False"; the omitted term is "-h1\*(g0 + g1\*u + s)/((h0 + h1\*u)\*\*2\*(m - 1)\*\*2)"; "A3 <=> Delta < 0: True"; "draws with A3: 74343, of which cross-partial > 0: 0"; at every grid point the true value is negative and the Appendix value positive (e.g. u=1, m=0.5: finite-diff −1.33333, Appendix +1.33333) | **demonstrated** | damaging → **damaging** |
| `p08:fnd:2` | chk:2, chk:3 | chk:2: "the correctly derived model under A3 predicts a NEGATIVE m x u interaction (same sign as ms:T2.M3, -0.061)". chk:3: on the $\Phi$ scale the sign also depends on the distribution of $k$ (see fnd:4) | **demonstrated** on the $k^*$ scale; on $\Phi$ it holds only given an assumption on $F$ | fixable → **fixable** |
| `p08:fnd:3` | chk:2 | "d2(C_M - C_B)/dm du = h1\*k > 0: True \| dk\*/dm = k\*/(1-m): True" | **demonstrated** | minor → **minor** |
| `p08:fnd:4` | chk:3 | Chain-rule identity "True". $\partial^2\Phi/\partial m\,\partial u$: uniform −0.19200, beta(2,2) −0.36864, beta(1,5) **+0.20736** (at $\Phi$ = 0.922). In the beta(1,5) family the sign flips only for "Phi > 0.672 (2.13 SD above the ms:§3.2 mean of 0.31)" | **demonstrated** | fixable → **fixable** (little practical effect in the families tested) |
| `p08:fnd:5` | chk:5 | "A3 <=> dk\*/du < 0: True". Point estimates of $\partial\Phi/\partial u$ are positive on all of [0,1] in M3 and M4 (zero crossings at m = 1.38 and 1.36). "max \|z\| = 1.65"; p ≥ 0.100 at every m under any cov($b_2,b_3$) | **demonstrated** for the unstated implication and the sign of the point estimates. **Inconclusive** as evidence against the model, since nothing is significant under any covariance | fixable → **fixable** |
| `p08:fnd:6` | chk:4 | "T2.M3.uncertainty b=+0.084 se=0.051 \|t\|= 1.65 p(t,411)=0.1003 implied='' reported='\*\*\*' INCONSISTENT" | **demonstrated** | fixable → **minor** |
| `p08:fnd:7` | chk:4 | "412 x 11 = 4532; with t-1 lag dropping 2009: 4120; reported 4712; 4712/412 = 11.437; remainder 180" | **demonstrated** | fixable → **fixable** |
| `p08:fnd:8` | chk:1 | "H(z) = 0 at z = -h0/h1 \| example h0=1, h1=1/2, z=-3: H = -1/2 -> ... (rule reverses): True"; "k\* at m = 1: zoo" | **demonstrated** | minor → **minor** |

### 7.1 Severity revisions and the reasons for them

- **`p08:fnd:6`, fixable → minor.** The harness confines the inconsistency to one cell, 1 of 16 checked. The same coefficient in Model 4, 0.079 (0.050), carries no stars, which is consistent, and the text never relies on the uncertainty main effect. A typo is likely, but only the authors can confirm that (asserted).
- **`p08:fnd:4`, kept at fixable.** The reversal is real, but in the families tested it appears only far above the sample mean of $\Phi$. The repair is still needed because §2.4 presents the step from $k^*$ to $\Phi$ as automatic, and the standard requires the sign on the tested scale.
- **`p08:fnd:1`, kept at damaging.** The harness shows Prop. 2 false at every admissible point under A3. All 25,657 draws without A3 give a positive cross-partial, so Prop. 2 holds exactly when A3 fails. I keep it short of fatal because the central H1/H3 claim does not depend on Prop. 2. Decision 1 puts this rating to the reviewer.
- No other severity changes.

### 7.2 Strengths (step 5), after the harness

- **`p08:S1` confirmed** (chk:1: "threshold derivation CONFIRMED").
- **`p08:S2` confirmed.** chk:1 confirms Proposition 1 in expression and sign. chk:3 confirms "H1 follows from Prop. 1 without further assumption" for every spending-weighted $F$.
- **`p08:S3` confirmed** (chk:4):
  - the 1 SD effect is 0.02688 (2.69 pp);
  - that is 0.158 of an outcome SD;
  - the peer coefficient drops by 0.693, and by 0.689 under the least favourable rounding;
  - 15 of 16 star markings are consistent.
- **`p08:S4` confirmed** (chk:2). The correctly derived model predicts a negative $m\times u$ interaction on $k^*$, the sign reported in T2.M3 and T2.M4.

### 7.3 Incompatibilities, after the harness

- **`p08:inc:1` demonstrated** (chk:2).
- **`p08:inc:2` demonstrated.** chk:2 prints "VERDICT: p08:inc:2 DEMONSTRATED: Prop. 2 holds iff A3 fails iff dk\*/du > 0".
- **`p08:inc:3` demonstrated** (chk:4).
- **`p08:inc:4` unchanged.** It has no check and stays referred to P-INF. Its premise, that the negative interaction is something the model fails to explain, is removed by fnd:1 and fnd:2.

### 7.4 Scorekeeper's remark (asserted; not checked)

I believe fnd:1 does not depend on the linear forms of §2.2. For any differentiable $H, G > 0$, $\partial^2 k^*/\partial m\,\partial u = [G'H - (s+G)H']/[H^2(1-m)^2]$. This is negative exactly when $H'/H > G'/(s+G)$, which is the proportional-response reading of the Williamson premise that A3 encodes. If so, a change of functional form cannot rescue Prop. 2 while keeping the authors' motivation. This is my inference and has not been run. A one-line `sympy` check could settle it if the reviewer wants to use it (decision 7).

## 8. Scoreboard after the harness (changed entries only)

```json
{
  "ScoreboardUpdate": {
    "scorekeeper": "p08 (Adversarial Probe; P-DER, P-NUM)",
    "manuscript": "ms:TEST",
    "basis": "harness outputs p08_chk_1 to p08_chk_5, 2026-10-23",
    "commitments": [
      {"id": "p08:cmt:5", "entitlement": "argued", "check": "p08:chk:1", "note": "confirmed: C_M - C_B = H(1-m)(k*-k), H(1-m) > 0"},
      {"id": "p08:cmt:6", "entitlement": "argued", "check": "p08:chk:1", "note": "Prop. 1 expression and sign confirmed"},
      {"id": "p08:cmt:7", "entitlement": "unentitled", "check": "p08:chk:2", "note": "the Appendix proof omits -(s+G)h1/(H^2(1-m)^2); Prop. 2 is false at every admissible (m,u) under A3"},
      {"id": "p08:cmt:8", "entitlement": "argued", "check": "p08:chk:2", "note": "demonstrated: cross-partial = (g1 h0 - h1(s+g0))/(H^2(1-m)^2) < 0 under A3"},
      {"id": "p08:cmt:9", "entitlement": "argued", "check": "p08:chk:2; p08:chk:5", "note": "demonstrated: dk*/du < 0 under A3"},
      {"id": "p08:cmt:10", "entitlement": "argued", "check": "p08:chk:3; p08:chk:5", "note": "demonstrated formally; Table 2 point estimates run the other way but are not significant (max |z| = 1.65)"},
      {"id": "p08:cmt:11", "entitlement": "argued", "check": "p08:chk:3", "note": "H1 follows from Prop. 1 for every spending-weighted F"},
      {"id": "p08:cmt:12", "entitlement": "unentitled", "check": "p08:chk:2; p08:chk:3", "note": "the premise (Prop. 2) is false under A3, and the step to Phi needs an unstated assumption on F"},
      {"id": "p08:cmt:13", "entitlement": "unentitled", "check": "p08:chk:2", "note": "as an account of the threshold; it holds only for the per-function cost saving (h1 k > 0)"},
      {"id": "p08:cmt:14", "entitlement": "challenged", "check": "p08:chk:2", "note": "its premise, that the negative interaction is an anomaly for the model, is removed: the corrected model predicts it. The legitimacy story may still be true but is not needed."},
      {"id": "p08:cmt:15", "entitlement": "challenged", "check": "p08:chk:4", "note": "two internal inconsistencies demonstrated: T2.M3.uncertainty stars, and N = 4,712"},
      {"id": "p08:cmt:16", "entitlement": "argued", "check": "p08:chk:4", "note": "§4 arithmetic confirmed"}
    ],
    "incompatibilities": [
      {"id": "p08:inc:1", "status": "demonstrated", "check": "p08:chk:2"},
      {"id": "p08:inc:2", "status": "demonstrated", "check": "p08:chk:2"},
      {"id": "p08:inc:3", "status": "demonstrated", "check": "p08:chk:4"},
      {"id": "p08:inc:4", "status": "asserted", "check": null, "note": "referred to P-INF; its premise is weakened by fnd:1 and fnd:2"}
    ],
    "challenges": [
      {"id": "p08:chl:1", "status": "stands", "note": "cannot be met as written; Prop. 2 must be re-signed or A3 dropped"},
      {"id": "p08:chl:2", "status": "answered by the scorekeeper", "note": "A3 makes dk*/du and the cross-partial negative (chk:2, chk:5)"},
      {"id": "p08:chl:3", "status": "stands", "check": "p08:chk:3"},
      {"id": "p08:chl:4", "status": "stands", "check": "p08:chk:2"},
      {"id": "p08:chl:5", "status": "stands", "check": "p08:chk:1"},
      {"id": "p08:chl:6", "status": "stands", "check": "p08:chk:4"},
      {"id": "p08:chl:7", "status": "stands", "check": "p08:chk:5", "note": "needs cov(b2, b3) from the authors"}
    ]
  }
}
```

## 9. Final findings list

Ordered by severity. The repairs are those of Part 1 §3, with the additions noted.

```json
{
  "Findings": [
    {"id": "p08:fnd:1", "probe_type": "P-DER", "locus": "ms:Prop2; ms:App.P2; ms:§2.2 A3", "severity": "damaging", "status": "demonstrated", "check": "p08:chk:2",
     "summary": "The Appendix proof of Prop. 2 drops the term -(s+G)h1/(H^2(1-m)^2). The true cross-partial is (g1 h0 - h1(s+g0))/(H^2(1-m)^2), negative at every admissible (m,u) under A3. Prop. 2 holds iff A3 fails, i.e. iff uncertainty favours the market (inc:2).",
     "repair": "Correct the proof. Re-sign Prop. 2 under A3, or drop A3 and state the sign condition. Revise H2 and §1 contribution 1, rewrite §5 ¶2, and say the corrected prediction was derived after Table 2 was seen (EPI.4)."},
    {"id": "p08:fnd:2", "probe_type": "P-DER", "locus": "ms:§4 H2; ms:§5 ¶2; ms:T2.M3.interaction", "severity": "fixable", "status": "demonstrated (k* scale); conditional on F for Phi", "check": "p08:chk:2; p08:chk:3",
     "summary": "The negative interaction the authors treat as an anomaly is what the correctly derived model predicts on k*, so the legitimacy auxiliary in §5 is not needed.",
     "repair": "Drop the legitimacy auxiliary or label it as a conjecture. Report the corrected prediction as accommodation."},
    {"id": "p08:fnd:4", "probe_type": "P-DER", "locus": "ms:§2.4 ¶1", "severity": "fixable", "status": "demonstrated", "check": "p08:chk:3",
     "summary": "On the tested scale, sign(d2Phi/dm du) = sign(Delta) * sign(f(k*) + k* f'(k*)). A worked case under A3 (beta(1,5), k* = 0.4) gives +0.20736 against -0.19200 on k*. In that family the flip occurs only for Phi > 0.672.",
     "repair": "State the assumption on F (e.g. d[k f(k)]/dk > 0 near k*), or derive the propositions on Phi."},
    {"id": "p08:fnd:5", "probe_type": "P-DER", "locus": "ms:§2.2 A3; ms:§3.3; ms:T2.M3, ms:T2.M4 uncertainty", "severity": "fixable", "status": "demonstrated (implication and sign of point estimates); inconclusive as evidence against the model", "check": "p08:chk:5",
     "summary": "Under A3 the model implies dPhi/du <= 0 for any F. The manuscript neither states nor tests this. Table 2 point estimates of dPhi/du are positive across m in [0,1] but not significant under any covariance (max |z| = 1.65).",
     "repair": "State the prediction. Report dPhi/du with SEs at representative m (needs cov(b2,b3)), or centre m."},
    {"id": "p08:fnd:7", "probe_type": "P-NUM", "locus": "ms:§3.1; ms:T2.Observations", "severity": "fixable", "status": "demonstrated", "check": "p08:chk:4",
     "summary": "N = 4,712 does not fit a balanced panel of 412 hospitals over 2009 to 2019 (4,532, or 4,120 with the t-1 lag). It is 412 x 11.437, remainder 180.",
     "repair": "Correct N or explain the design, and confirm the estimation sample."},
    {"id": "p08:fnd:3", "probe_type": "P-DER", "locus": "ms:§2.3 intuitive reading", "severity": "minor", "status": "demonstrated", "check": "p08:chk:2",
     "summary": "The intuition holds for the per-function cost saving (h1 k > 0), not for the threshold effect k*/(1-m), which falls with u under A3.",
     "repair": "Separate the two; absorbed into the fnd:1 repair."},
    {"id": "p08:fnd:6", "probe_type": "P-NUM", "locus": "ms:T2.M3.uncertainty", "severity": "minor", "severity_revised_from": "fixable", "status": "demonstrated", "check": "p08:chk:4",
     "summary": "0.084 (0.051) gives |t| = 1.65, p = 0.100, yet three stars are shown. The other 15 cells are consistent.",
     "repair": "Correct the stars."},
    {"id": "p08:fnd:8", "probe_type": "P-DER", "locus": "ms:§2.2 domain; ms:§3.2 measures", "severity": "minor", "status": "demonstrated", "check": "p08:chk:1",
     "summary": "With u measured as a z-score, H(u) <= 0 is possible (u <= -h0/h1) and the buy rule reverses. k* is undefined at m = 1. A3 is the only numbered assumption.",
     "repair": "Map the z-score to the model's u or restrict the domain. Fix the assumption labels."}
  ],
  "Strengths": [
    {"id": "p08:S1", "status": "confirmed", "check": "p08:chk:1"},
    {"id": "p08:S2", "status": "confirmed", "check": "p08:chk:1; p08:chk:3"},
    {"id": "p08:S3", "status": "confirmed", "check": "p08:chk:4"},
    {"id": "p08:S4", "status": "confirmed", "check": "p08:chk:2"}
  ],
  "Counts": {"demonstrated": 8, "refuted_by_check": 0, "inconclusive": 0, "partly_inconclusive": ["p08:fnd:5 (evidential part)"], "asserted_unbound": 0}
}
```

**Overall reading (P-DER and P-NUM only).**

- **What holds.** Proposition 1, the threshold, and the step from Proposition 1 to H1 are sound. The §4 effect-size arithmetic is correct.
- **What fails.** Proposition 2 is false under the paper's own A3. Correctly derived, the model predicts the negative interaction the authors report as anomalous. This removes the need for §5 ¶2 but turns that sign into accommodation.
- **Numerical errors.** There are two:
  - the N reported does not fit the stated panel design;
  - one cell's stars are wrong.
- **Out of scope.** Nothing here bears on the identification of the modularity effect or on the H3 inference. Those are referred (Part 1 §5).

## Decisions for the reviewer (Part 2)

1. **`p08:fnd:1` severity.** Accept *damaging* (my rating: the formal error is demonstrated, but the central H1/H3 claim does not depend on Prop. 2), or treat it as *fatal to the formal-model contribution* (contribution 1 in §1).
2. **Credit for the corrected model.** Credit its fit to the negative interaction, or discount it as post hoc accommodation (your EPI.4 setting). The harness shows the sign matches. It cannot show the prediction was made in advance.
3. **`p08:fnd:4`.** Ask the authors to derive their propositions on $\Phi$, or accept a stated distributional assumption. The harness shows the reversal is possible but, in the families tested, confined to hospitals far above the mean outsourcing share.
4. **`p08:fnd:5`.** Decide whether to raise it. If you do, request cov($b_2,b_3$) or a centred specification. The harness shows the contrary point estimates are not significant under any covariance.
5. **`p08:fnd:7` and `p08:fnd:6`.** Raise the N discrepancy as a query, or as grounds to request data and code (TEC.1). Raise the star error (now *minor*) as a correction.
6. **Referred probes.** Commission the probes referred in Part 1 §5 (P-ID on the Model 4 and asset-specificity controls and the event study; P-INF on H3, using the chk:4 INFO line, a Model 2 peer CI of [−0.033, 0.117]; P-LIT on the priority claim), or leave them.
7. **The §7.4 remark.** Have the general-functional-form claim checked before you rely on it in the review. It is currently `asserted`.
8. **Each finding.** Accept, reject or modify each finding above. None is to be copied into the review unedited.

