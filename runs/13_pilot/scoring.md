# Run 13 pilot: blind scoring of reports A to F

Scorer: blind scorer. Files read: `case/TEST_MANUSCRIPT.md`, `case/SEALED_DEFECT_KEY.md`, `runs/13_pilot/blind/review_A.md` to `review_F.md`. Nothing else was read, and the web was not used.

**Codes.** L = located (right locus and the reason in the key's "Located if" column). T = touched (right locus, but a wrong, generic or partial reason). M = missed.

**Rules used for all six reports**
- SD2: L requires that the report says staffing is a consequence of the outcome *and* that the Model 4 robustness inference does not follow. An explicit statement of bias is not required when the "bad control" or descendant reasoning is given.
- SD4: L requires that the report says the same-state peer measure does not capture the rival's construct *because* mimicry targets referents chosen by status, success, similarity or ties. Two things alone give only T: saying the state "may be the wrong field" with alternative groupings, and noting that Peer × uncertainty is untested. The untested uncertainty contingency is part of the SD4 defect in the key, so I note it under SD4 and do not count it as an unseeded finding.
- SD5: L requires that the report says the legitimacy account is ad hoc (post hoc, or outside the model), untested or unformalized, and that the "consistent with our theory" claim is unwarranted. Each may be said in substance rather than in those words.
- SD6: every report gave both (a) and (b) with the arithmetic, so every SD6 score is full credit.
- SD7: L requires that the report says the priority claim is false or overstated *and* names prior adjudicating or combining work (one of the key's three papers, or equivalent).
- Unseeded findings are counted by distinct category (see the legend), so a report gets one count per category however many sub-points it makes. Some points only elaborate a seeded defect: a test of the change in the Model 1 to Model 2 peer coefficient supports SD3, the §2.3-intuition analysis supports SD1, and the intensive-margin or share-mapping points support SD8. These are noted under that defect and not counted.

## Summary table

| Report | SD1 | SD2 | SD3 | SD4 | SD5 | SD6 | SD7 | SD8 | SD9 | Located | Touched | New-substantive | Mistaken | Recommendation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A | L | L | L | T | L | L | L | L | L | 8 | 1 | 10 | 1 | Reject in current form, with encouragement to resubmit |
| B | L | L | L | L | L | L | L | L | L | 9 | 0 | 12 | 0 | Major revision |
| C | L | L | L | L | L | L | L | L | L | 9 | 0 | 11 | 0 | Major revision |
| D | L | L | L | T | T | L | T | L | M | 5 | 3 | 8 | 0 | Major revision (reject and resubmit if rv:M5 or rv:M7 unresolved) |
| E | L | L | L | L | L | L | L | L | L | 9 | 0 | 13 | 0 | Reject (in present form) |
| F | L | L | L | L | L | L | L | L | L | 9 | 0 | 13 | 0 | Major revision (otherwise reject with encouragement to resubmit) |

**Calls I am unsure of**
1. **SD4, reports A and D (T).** Both say the state may be the wrong field and both note that Peer × uncertainty is untested. Neither ties referent choice to status, success, similarity or ties: the alternatives they offer are referral region, system and nearby hospitals. A more lenient reading would give L.
2. **SD5, reports C and F (L).** Neither uses "post hoc" or "ad hoc". I credited both because each says the account is outside the model and untested (F only implies "untested" in its repair) and rebuts the consistency claim. A stricter reading would give T.
3. **SD7, report D (T).** D names Dibbern et al. (2004), a review of the IS outsourcing literature, and asks the authors to "narrow or support" the claim. It neither says the claim is false nor names prior adjudicating work. A more lenient reading would give L.
4. **SD2, reports A and D (L).** Neither says in so many words that the modularity coefficient is biased. Both say staffing is partly caused by the outcome and that the robustness inference fails.
5. **Report A's one "mistaken" item (m10(d))** is a small misreading, and I hold it with moderate confidence.
6. **NS-l** (the corrected model also implies a negative uncertainty main effect, against positive estimates) is borderline between new-substantive and minor. It extends SD1, and the estimates it contrasts with are not significant.
7. **The m × specificity test (B, D, E).** At the function level the gain from modularity does scale with k. The reports' hospital-level prediction of an m × average-specificity interaction is not derived from the model, because its sign at the share level depends on the distribution of k. I did not score it as mistaken. It is counted within NS-i.

## Legend: unseeded finding categories

**Known-unseeded** (from the key's list)
- **KU1.** The two-way fixed-effects event study with staggered adoption is biased under heterogeneous effects.
- **KU2.** Reverse timing or causality between modularity and outsourcing.
- **KU3.** Single-informant CIO measures. I include common-source bias across m, Φ and specificity, and requests to validate CIO-reported m.
- **KU4.** Survivorship or selection among the balanced-panel responders.
- **KU5.** The corner where k* ≥ 1 is ignored.

**New-substantive** (real weaknesses not on the key)
- **NS-a.** Year fixed effects absorb the aggregate diffusion, so the design cannot explain the 2009–2019 rise. There is no decomposition or magnitude check.
- **NS-b.** Modularity may be the channel of peer influence, or a proxy for the outcome, so conditioning on it absorbs the peer effect. The "common diffusion of standards" reading is asserted but not tested.
- **NS-c.** State-year common shocks or correlated effects confound the peer variable: supply, policy, mandates, same-system ties.
- **NS-d.** The peer measure is noisy: few sampled hospitals per state, undefined for single-hospital states, so its coefficient is attenuated.
- **NS-e.** Standard errors are clustered by hospital although the peer variable and the mandates vary by state.
- **NS-f.** Time-varying confounders of modularity and outsourcing: EHR replacement, platform migration, CIO change, system acquisition, or EHR-incentive effects that differ across hospitals.
- **NS-g.** The event study is a reduced form only: no first stage, a doubtful exclusion restriction, and no results reported.
- **NS-h.** Coercive isomorphism: the mandates, certification and federal incentive are institutional pressures, and only the mimetic strand of institutional theory is tested.
- **NS-i.** The specificity mechanism is untested or contradicted. No link from m to specificity is shown. The measure is ambiguous (effective or nominal, ex post, possibly caused by outsourcing). There is no m × specificity test.
- **NS-j.** The uncertainty proxy (coefficient of variation of admissions) measures demand volatility, not the model's uncertainty or the rival's.
- **NS-k.** The modularity measure's scope and construct are off. It covers clinical systems only, but the outcome covers all functions, including hosting and help desk. Interoperability is not Baldwin–Clark modularity, and k(1−m) is a strong assumption.
- **NS-l.** Under A3 the corrected model also implies ∂k*/∂u < 0, which is at odds with the positive uncertainty estimates.
- **NS-m.** Rival economizing channels are not excluded: standards may lower G, raise s or increase vendor availability. Prop 1 depends on m entering only the hold-up term.
- **NS-n.** "Economizing" is asserted without cost or performance evidence of alignment.
- **NS-o.** Other controls may be post-outcome: operating margin, system membership.
- **NS-p.** Classification drift: a shift from licences (excluded) to hosted or subscription spending could raise measured Φ.

---

## Report A

### Seeded defects

| SD | Score | Quote (at most 30 words) | Note |
|---|---|---|---|
| SD1 | L | "does not license dropping $H'(u)$, because $H(u)$ is also in the denominator. ... Under A3 it is negative for every $u$." (M1) | Gives the full corrected bracket and a numerical instance; both are correct. |
| SD2 | L | "Staffing is therefore partly determined by the dependent variable. ... A surviving modularity coefficient therefore does not show that capability is not a confounder." (M6) | Bias is implied ("removes part of the outcome's variation"), not stated. Recommends a bad-control analysis. |
| SD3 | L | "Absence of significance is not evidence of absence. ... Its approximate 95% interval is $-0.03$ to $0.12$, which includes effects of 0.10 or more" (M4(i)) | Requires an equivalence test. |
| SD4 | T | "The peer group is 'the same state' (§3.2). The field relevant to imitation need not be the state, and the paper does not justify the choice." (M4(v)) | Also M4(iii): Peer × u is untested. No argument about referent selection. Unsure (see calls). |
| SD5 | L | "The moderation result is misreported, its interpretation is post hoc ... It is not in the model and it is not tested." (M9) | |
| SD6 | L (a+b) | "A balanced panel of 412 hospitals over the eleven years 2009–2019 has $412\times11=4{,}532$ observations" (M8); "The t-statistic is about 1.65 (p ≈ 0.10), so the three-star flag is wrong." (M9(i)) | |
| SD7 | L | "'The first study to adjudicate directly' is not supportable without engaging the literature" (m1); "prior work on diffusion and influence in IT outsourcing (for example, Loh and Venkatraman, 1992 (to verify))" (m2) | |
| SD8 | L | "The propositions concern a per-function threshold, but the hypotheses concern spending shares, and the text moves between the two without a mapping. ... The model never specifies $F$." (M2) | The derivation of the share-level cross-partial is correct. |
| SD9 | L | "The legitimacy account in §5 is an institutional mechanism ... offered to explain the paper's own main moderation result, while the Abstract and §6 state that institutional explanations are ruled out." (M9(iii)) | |

### Other findings
- **Known-unseeded**
  - KU1: M5(iii), TWFE with staggered adoption.
  - KU2: M5, outsourcing may force the hospital to expose certified interfaces, which would raise measured modularity.
  - KU3: M7(iv)–(v), m, Φ and specificity come from the same CIO survey; the measures need validation.
  - KU4: m8, selection by the balanced design.
- **New-substantive (10)**
  - NS-a: M3, year fixed effects absorb the rise, no decomposition. Also m5, a static model under a title about diffusion.
  - NS-b: M4(ii), modularity may mediate the peer effect, and "common diffusion of standards" is asserted.
  - NS-c: M4(iv), state-level supply shocks such as vendor entry.
  - NS-e: M8, peer is state-year but clustering is by hospital.
  - NS-f: M5, a common time-varying cause such as EHR replacement, platform migration or a new CIO.
  - NS-g: M5(i), (ii), (iv), (v): no first stage, nothing reported, doubtful exclusion restriction, requirement not described.
  - NS-i: M6, the specificity rating comes after contracting and "is not the ex ante $k$ of the model".
  - NS-j: M7(iii), the uncertainty measure is demand volatility.
  - NS-k: M7(i), the clinical-systems measure omits hosting and help desk.
  - NS-o: M6, operating margin and system membership may be affected by outsourcing.
- **Minor**
  - M7(ii): how m = 1 is handled.
  - M9(ii): the modularity effect reaches zero at u ≈ 1.9 SD (1.7 SD in Model 4); arithmetic correct.
  - m1: "strongly predicts" overstates; "prior adoption" does not match the variable.
  - m2: the modularity and firm-boundaries literature is not engaged.
  - m3: A1 and A2 are missing; the distribution of k is unspecified.
  - m4: Prop 1 is built into the functional form.
  - m6: robustness results not reported.
  - m7: unclear whether the SDs are total or within-hospital.
  - m9: no fractional-response check.
  - m10(a): "in every specification" although Model 1 omits modularity.
  - m10(b): the index s is undefined.
  - m10(c) restates SD1.
- **Mistaken (1)**
  - m10(d) says §3.3 "describes 'culture and governance' as stable". The manuscript says only that hospital fixed effects absorb "stable differences in capability, culture and governance". It does not claim governance is time-invariant, and system membership is controlled separately as time-varying. Minor; moderate confidence.

### Recommendation
Reject in the current form, with encouragement to resubmit a substantially revised manuscript.

---

## Report B

### Seeded defects

| SD | Score | Quote (at most 30 words) | Note |
|---|---|---|---|
| SD1 | L | "The proof differentiates only the numerator, s + G(u), and treats H(u) as constant. H'(u) = h1 > 0 is dropped. ... So under A3 the cross-partial is negative" (Concern 1) | Also correctly separates the cost saving H·k·m from the threshold. |
| SD2 | L | "a bad control, and the inference drawn from it does not follow ... Conditioning on it biases the modularity coefficient in an unknown direction." (Concern 5) | |
| SD3 | L | "Absence of significance is not absence of effect. ... Its 95% CI is about (-0.03, 0.12), which includes 85% of the Model 1 estimate" (3(a)) | Also notes that the Model 1 to Model 2 difference is untested. |
| SD4 | L | "State is an arbitrary definition of the 'field'. Mimicry is usually directed at similar or prestigious organizations, such as system peers, local competitors, large teaching hospitals, or vendors' reference sites" (3(c)) | Also Peer × u. |
| SD5 | L | "The discussion of the negative interaction is ad hoc ... 'This interpretation is consistent with our theory.' The signalling and legitimacy story is outside the model and untested." (Concern 2) | |
| SD6 | L (a+b) | "412 hospitals x 11 years (2009-2019) = 4,532, not 4,712"; "ms:T2.M3.uncertainty reads 0.084*** (0.051). The t-ratio is 1.65 (p about 0.10), which fits no star." (Concern 10) | |
| SD7 | L | "The novelty claim is unsupported. ... Prior work I recall tests institutional and TCE accounts of IT outsourcing: Loh & Venkatraman (1992), Ang & Cummings (1997)" (Concern 11) | |
| SD8 | L | "The share of functions outsourced depends on the distribution of k ... Prop 1 gives a threshold, not a share. ... State what the mapping from k* to Φ is." (minor 16) | Raised only as a minor point, framed on Prop 1; it still meets the criterion. |
| SD9 | L | "The paper uses an institutional mechanism to rescue the transaction-cost account while claiming to rule institutional accounts out." (Concern 2) | |

### Other findings
- **Known-unseeded**
  - KU1: Concern 6.
  - KU2: Concern 4, vendor platforms ship certified interfaces.
  - KU3: Concern 4, common-method bias.
  - KU4: Concern 10, selection of responders.
  - KU5: minor 16, "k* may exceed 1".
- **New-substantive (12)**
  - NS-a: Concern 9.
  - NS-b: 3(d).
  - NS-c: Concern 6, the state requirement also moves the state-level peer variable and so confounds H3.
  - NS-d: 3(b) and minor 17.
  - NS-e: Concern 7.
  - NS-f: Concern 4, EHR vendor migration, joining a system, CIO turnover, timing of the incentive programme.
  - NS-g: Concern 6.
  - NS-h: 3(e).
  - NS-i: Concern 8, no regression of specificity on m, specificity coefficient stable, no m × k term. See call 7.
  - NS-j: minor 15.
  - NS-k: Concern 8, interoperability is not modularity; k(1−m) is strong given configuration and tacit knowledge.
  - NS-l: Concern 1.
- **Minor**
  - Concern 2: the abstract omits the H2 failure.
  - Concern 1: why s appears in A3.
  - Concern 10: the survey is not identified.
  - 12: "strongly" overstates.
  - 13: "in every specification".
  - 14: the u main effect is the effect at m = 0, and the modularity effect is about zero at u = +2 SD; arithmetic correct.
  - 18: no descriptive statistics.
  - 19: practice advice goes beyond the evidence.
  - 20: the limitations section is thin.
  - 21: p cancels.
  - 22: the two accounts are not mutually exclusive.
- **Mistaken:** none. One slip: Concern 1 points to "see 6" for the uncertainty-star issue, which is in Concern 10. It is not a substantive finding.

### Recommendation
Major revision.

---

## Report C

### Seeded defects

| SD | Score | Quote (at most 30 words) | Note |
|---|---|---|---|
| SD1 | L | "the proof treats H(u) as constant ... But H(u) = h0 + h1·u also depends on u. ... under A3 the cross-partial is negative for every m and u." (cmt:2) | Numerical example (−4) and the sign identity with ∂k*/∂u are both correct. |
| SD2 | L | "staffing is a consequence of the outcome. Controlling for it neither removes capability confounding nor leaves β1 unbiased." (cmt:6) | |
| SD3 | L | "Absence of evidence. ... the 95% CI is about [−0.032, 0.116]. The upper bound is close to the Model 1 estimate (0.137). ... no equivalence test." (cmt:1a) | |
| SD4 | L | "State is a weak proxy for the peer group. ... 'peers they regard as successful or legitimate' (§1). No peers are defined by system, network, vendor or status." (cmt:1f) | Also proposes a test of the Tolbert–Zucker staging. |
| SD5 | L | "'This interpretation is consistent with our theory' ... Legitimacy pressure is an institutional mechanism, and it is not in the model. ... It is untested and, given cmt:2, unnecessary." (cmt:7) | No explicit "post hoc". Unsure (see calls). |
| SD6 | L (a+b) | "412 × 11 = 4,532, not 4,712, and 4,712/412 is not a whole number." (cmt:8); "0.084 (0.051) gives t ≈ 1.65 and p ≈ 0.10, but it is reported with ***." (cmt:10) | |
| SD7 | L | "The IS outsourcing literature has already tested imitation against economic explanations: Loh & Venkatraman (1992) ... Ang & Cummings (1997)" (cmt:13) | |
| SD8 | L | "H2 does not follow from Prop 2 alone. ... Φ = F(k*), where F is the spending-weighted distribution of k across functions. ... State an assumption about the distribution of k" (cmt:11) | |
| SD9 | L | "Using it to explain a main result contradicts the claim in the Abstract and §6 that the practice is economizing rather than institutional fashion." ... "withdraw the 'rule out' language" (cmt:7) | |

### Other findings
- **Known-unseeded**
  - KU1: cmt:4c.
  - KU2: cmt:4a.
  - KU3: cmt:4b.
  - KU4: cmt:18.
  - KU5: cmt:11, "Φ = 1 once k* ≥ 1".
- **New-substantive (11)**
  - NS-a: cmt:5, including a magnitude comparison flagged as inferred.
  - NS-b: cmt:1b–c. The omitted-variable identity gives δ ≈ 0.85; the arithmetic is correct.
  - NS-d: cmt:1e.
  - NS-e: cmt:17.
  - NS-f: cmt:4d, year fixed effects do not absorb EHR-incentive effects that differ across hospitals.
  - NS-g: cmt:4c.
  - NS-h: cmt:1d.
  - NS-i: cmt:3, including δ_spec ≈ −0.03; arithmetic correct.
  - NS-j: cmt:12.
  - NS-k: cmt:9.
  - NS-l: cmt:2.
- **Minor**
  - cmt:14: the abstract omits the H2 failure.
  - cmt:15: "strongly"; within-hospital SD.
  - cmt:16: unreported robustness.
  - cmt:18: survey documentation.
  - cmt:19: the leave-one-out peer mean conflicts with the Peer_{s,t−1} notation; measured m can equal 1; A3 is phrased as "proportional".
  - cmt:20: practice advice.
  - cmt:8 adds that the 2009 uncertainty measure needs 2006–2008 admissions.
- **Mistaken:** none. Note: cmt:3(d) says the modularity coefficient "stays at 0.11–0.12" once specificity is controlled. Table 2 has no specification with modularity but without specificity, so the wording implies a comparison that cannot be made. The underlying point, a large coefficient conditional on effective specificity, stands, so I did not score it as mistaken.

### Recommendation
Major revision.

---

## Report D

### Seeded defects

| SD | Score | Quote (at most 30 words) | Note |
|---|---|---|---|
| SD1 | L | "It then differentiates only the numerator in u and drops H'(u) = h1. ... Under ms:A3 ... the bracket is negative for all u >= 0. The cross-partial is therefore negative." (rv:M1) | |
| SD2 | L | "In-house staffing is therefore partly caused by the outcome. A coefficient that survives a control set by the outcome does not rule out capability confounding." (rv:M9) | Headed "bad control". Bias not stated explicitly (see calls). |
| SD3 | L | "Non-significance is read as absence of mimicry. ... Its 95% CI is about [-0.035, 0.107]. That range contains the modularity coefficient (0.097)." (rv:M4) | Uses Model 4. Its difference-test z ≈ 1.9 is also correct. |
| SD4 | T | "the state may be the wrong 'field'. Other definitions (referral region, system, nearby hospitals) are not tested." (rv:M8); "The peer x uncertainty term, the institutional account's own moderator, is absent." (rv:M4) | No argument about referent selection. Unsure (see calls). |
| SD5 | T | "The signalling account (ms:S5, para 2) is not needed to explain the sign. Calling it 'consistent with our theory' is incorrect." (rv:M1) | Does not call it post hoc, ad hoc or untested. The reason given is the corrected sign from SD1. |
| SD6 | L (a+b) | "412 x 11 = 4,532. 4,712 is not a multiple of 11 or of 412." (rv:M5); "t of about 1.65, p of about 0.10 ... The star is wrong." (rv:m1) | |
| SD7 | T | "'first study to adjudicate directly' ... The paper cites no prior empirical IT-outsourcing study. Address the IS outsourcing literature (e.g., Dibbern et al., 2004 ...). Narrow or support the claim." (rv:m9) | Names only a literature review and does not call the claim false. Unsure (see calls). |
| SD8 | L | "the step from threshold to hospital share (ms:S2.4) needs a distribution of k and spending weights that do not depend on m or u. None is stated." (rv:M10) | |
| SD9 | M | none | No passage sets "rule out" against the legitimacy explanation. |

### Other findings
- **Known-unseeded**
  - KU1: rv:M7.
  - KU2: rv:M6.
  - KU3: rv:M6.
  - KU4: rv:m7.
  - KU5: rv:M10, "the linear share model fails when k* > 1".
- **New-substantive (8)**
  - NS-b: rv:M4, in a weak form. The standards-diffusion reading is untested, and D proposes adding peer modularity, but it does not give the mediation argument.
  - NS-c: rv:M8.
  - NS-e: rv:M7.
  - NS-f: rv:M6.
  - NS-g: rv:M7.
  - NS-i: rv:M2. See call 7.
  - NS-j: rv:m5.
  - NS-m: rv:M10 and rv:m11.
- **Minor**
  - rv:M3: the modularity effect is zero at u ≈ 1.9 SD (1.7 SD in Model 4). The arithmetic is correct. I score it minor because it reads directly off the reported interaction, although D rates it damaging.
  - rv:M10: the m = 1 domain.
  - rv:m2: missing constant, cluster count and descriptive statistics; within-hospital SD.
  - rv:m3: asks whether specificity varies within hospital.
  - rv:m4: controls absorbed by the fixed effects.
  - rv:m6: no standard is named; the denominator may change.
  - rv:m8: unreported robustness.
  - rv:m10: "prior adoption" wording.
  - rv:m11: "strongly predicts".
  - rv:m12: check the Williamson (1991) attribution.
- **Mistaken:** none.

### Recommendation
Major revision. D would move to reject and resubmit if rv:M5 or rv:M7 cannot be resolved.

---

## Report E

### Seeded defects

| SD | Score | Quote (at most 30 words) | Note |
|---|---|---|---|
| SD1 | L | "The proof ... differentiates ∂k*/∂m ... with respect to u while treating H(u) as if it did not vary. ... So under A3 the cross-partial is negative for all m and u" (M1) | |
| SD2 | L | "It is thus an outcome of the dependent variable ... a bad control that can induce bias in either direction. ... Survival of the modularity coefficient therefore says nothing about confounding by capability." (M4) | |
| SD3 | L | "Absence of significance is not evidence of absence. ... Its 95% interval is roughly (−0.03, 0.12) ... The data do not exclude a substantial peer effect." (M2.1) | Also gives the Gelman–Stern difference point. |
| SD4 | L | "The reference group is asserted, not justified. Mimetic theory points to salient peers: similar size, system affiliation, the same referral region, or high-status organizations." (M3.1) | Also M2.4, Peer × u. |
| SD5 | L | "The signalling account in ms:S5 is introduced after the fact, is not formalized, and is not tested ... The statement that it is 'consistent with our theory' is not available" (M7) | M1.1 also calls it an "ad hoc patch". |
| SD6 | L (a+b) | "has 412 × 11 = 4,532 observations, not 4,712 ... 'Environmental uncertainty 0.084*** (0.051)' gives t ≈ 1.65 and p ≈ 0.10, which is not significant at conventional levels" (M8.1–2) | |
| SD7 | L | "is, I believe, not accurate. ... the 'Kodak effect' (Loh & Venkatraman, 1992, to verify), on institutional influences on IS outsourcing (Ang & Cummings, 1997" (m1) | |
| SD8 | L | "Even a correct cross-partial of k* does not map into the sign of an interaction in the spending share Φ. ... The step from ms:Prop2 to ms:H2 ... is therefore not licensed" (M1.4) | Asks for Φ to be derived from a distribution of k with spending weights. |
| SD9 | L | "A paper that has just argued that institutional forces are ruled out cannot also rely on them to rescue its model." (M2, closing paragraph) | |

### Other findings
- **Known-unseeded**
  - KU1: M6.5.
  - KU2: M6.2 and M6.4 (the hospital chooses its own modularity).
  - KU3: M6.3.
  - KU4: M8.5.
  - KU5: M1.4, the "corner at k* ≥ 1".
- **New-substantive (13)**
  - NS-a: M2.3.
  - NS-b: M2.2.
  - NS-c: M3.3 (Manski), M3.5 (same-system peers) and M6.5 (state timing confounded with the peer variable).
  - NS-d: M3.2.
  - NS-e: M3.4.
  - NS-f: M6.1.
  - NS-g: M6.5.
  - NS-h: M2.2.
  - NS-i: M5.1–2. See call 7.
  - NS-j: m2.
  - NS-k: the construct-validity paragraph in M5.
  - NS-m: M5.3.
  - NS-n: M5.4.
- **Minor**
  - M1.3: Williamson (1991) separates autonomous adaptation, where markets excel, from cooperative adaptation, which favours hierarchy. This is an accurate nuance, flagged "to verify". A1 and A2 are missing.
  - M2.5: the accounts are not mutually exclusive.
  - M3.6: S-curve functional form.
  - M7: the abstract omits the H2 failure; the marginal effect is zero at +1.9 SD.
  - M8.3: no Table 1.
  - M8.4: "strongly predicts".
  - m3: Prop 1 holds by construction; m treated as exogenous.
  - m4: fractional response; marginal effects; controls; state counts.
  - m5: survey documentation.
  - m6: unit of decision.
  - m7: language calibration and practice advice.
  - m8: thin limitations section.
  - NS-l is not counted for E: M1.1 notes that A3 implies a negative uncertainty main effect but does not compare it with the estimates.
- **Mistaken:** none. One slip: M1.1 labels the interaction estimate (−0.061) as `ms:T2.M3.uncertainty`. It is not a substantive finding.

### Recommendation
Reject (in its present form). E would review a fundamentally reworked paper, and it lists minimum conditions in case the editor prefers major revision.

---

## Report F

### Seeded defects

| SD | Score | Quote (at most 30 words) | Note |
|---|---|---|---|
| SD1 | L | "The denominator also depends on u: H(u) = h_0 + h_1 u (§2.2). The proof drops H'(u). ... Assumption A3 ... is exactly the condition that makes it negative." (cmt:1) | |
| SD2 | L | "In-house IT staffing (Model 4) is a post-treatment control, and the conclusion drawn from it does not follow. ... partly a mechanical outcome of Φ" (cmt:6) | Calls it a bad control (citing Angrist & Pischke) and notes the 18% fall in the coefficient. |
| SD3 | L | "A non-significant coefficient is not evidence of absence. ... [−0.03, 0.12] ... Its upper end is roughly 85% of the Model 1 point estimate" (cmt:2(b)) | Also gives the Gelman–Stern difference point. |
| SD4 | L | "The institutional rival is operationalized weakly, in ways that favour rejecting it. ... imitation of successful, high-status or tie-connected peers. ... System peers are an obvious reference group" (cmt:2(c)) | Also Peer × u and the Tolbert–Zucker staging. |
| SD5 | L | "'This interpretation is consistent with our theory'. On any standard reading, legitimacy pressure is an institutional mechanism, and the formal model contains no such term." (cmt:2(d)); "recast it as an untested alternative" (cmt:1) | No explicit "post hoc". Unsure (see calls). |
| SD6 | L (a+b) | "2009–2019 inclusive is 11 years, and 412 × 11 = 4,532." (cmt:7); "reported as 0.084 (SE 0.051) and marked ***. That gives t ≈ 1.65 and a two-sided p ≈ 0.10" (cmt:8) | |
| SD7 | L | "The information-systems literature has studied the diffusion of IT outsourcing as imitation ... Loh and Venkatraman's 'Kodak effect' (1992 ...). It has also combined institutional and economic accounts ... Ang and Cummings" (cmt:15) | |
| SD8 | L | "H1 and H2 are stated for Φ, a spending-weighted share (§2.4). The propositions concern k*. ... State the needed assumptions (for example, a uniform distribution of k)" (cmt:11) | Adds an intensive-margin point, which elaborates SD8. |
| SD9 | L | "The manuscript cannot both rule out institutional drivers of IT sourcing (abstract; §5 ¶1) and use one to explain its own estimates." (cmt:2(d)) | |

### Other findings
- **Known-unseeded**
  - KU1: cmt:3(d), including the low power of pre-trend tests.
  - KU2: cmt:2(a) structure 3 and cmt:3(a).
  - KU3: cmt:3(b).
  - KU4: cmt:14.
  - KU5: cmt:11, "requires ... k* < 1".
- **New-substantive (13)**
  - NS-a: cmt:4. Also cmt:2(c): year fixed effects absorb imitation at the level of the national field.
  - NS-b: cmt:2(a). The omitted-variable identity gives δ ≈ 0.85; the arithmetic is correct.
  - NS-c: cmt:2(a) common state shocks; cmt:2(c) Manski.
  - NS-d: cmt:2(c).
  - NS-e: cmt:10.
  - NS-g: cmt:3(d), including the compliance-capability exclusion problem.
  - NS-h: cmt:2(a) structure 2.
  - NS-i: cmt:5(a)–(b); δ_spec arithmetic correct.
  - NS-j: cmt:12.
  - NS-k: cmt:5(c).
  - NS-l: cmt:1(e). The effect at mean m is 0.056; correct.
  - NS-n: cmt:4.
  - NS-p: cmt:16.
- **Not counted:** time-varying confounders appear only as CIO turnover inside the common-source point (cmt:3(b)). I counted that under KU3, not NS-f.
- **Minor**
  - cmt:1: A3 oddities (s on the right-hand side; the only numbered assumption).
  - cmt:2(e): the contest is assumed to be binary.
  - cmt:9: marginal effects; k* is convex in m but the estimating equation is linear.
  - cmt:11: m = 1.
  - cmt:13: language of magnitude.
  - cmt:16: unreported analyses.
  - cmt:17: presentation, controls absorbed by the fixed effects, practice advice.
  - The confidential note to the editor requests code and a log of how the sample was built.
- **Mistaken:** none.

### Recommendation
Major revision. If the editor keeps major revision for papers whose central claim should survive intact, F's recommendation becomes reject with encouragement to resubmit.
