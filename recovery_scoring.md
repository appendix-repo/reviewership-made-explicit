# Recovery scoring of the workbench runs on `ms:TEST`

- **Scorer:** recovery scorer. This scoring knows which run each output comes from. I applied one reading of the key to every output.
- **Date:** 23 October 2026.
- **Files read in full:** `case/TEST_MANUSCRIPT.md`, `case/SEALED_DEFECT_KEY.md`, and runs 02, 03, 04, 05, 06, 08, 09 and 10. I read no other file. I did not read the probes' harness outputs (`08_checks/`, `09_checks/`, `10_checks/`), so each probe status below is the status that probe's own Part 2 reports.
- **Codes:** L = located, T = touched, M = missed. The rules are the earlier blind scorer's, applied unchanged.
- **† (referral):** the point appears only in a passage the probe marks as a referral to another probe type. These are R08 Part 1 §5 and `p08:inc:4`, and R09 §6. I scored such passages on their content, because a referral puts the point in front of the reviewer just as R10's "cross-type" findings do. R08 itself says its referrals "are not findings". The notes under the table give the counts without referrals.
- Probe outputs are scored as they stand after Part 2. A finding counts whatever its status, unless the output withdraws or refutes it.

## 1. Summary

| Run | SD1 | SD2 | SD3 | SD4 | SD5 | SD6 | SD7 | SD8 | SD9 | Located | Touched | Known-unseeded | New-substantive | Mistaken |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R02 reviewer draft | L | L | L | L | L | L | L | L | L | 9 | 0 | 4 | 13 | 0 |
| R03 sim. TCE | L | L | L | L | L | L | L | L | L | 9 | 0 | 5 | 16 | 0 |
| R04 sim. INST | L | L | L | L | L | L | L | L | L | 9 | 0 | 5 | 13 | 0 |
| R05 sim. BEH | L | L | L | L | L | L | L | L | L | 9 | 0 | 5 | 19 | 0 |
| R06 sim. DID | L | L | L | L | L | L | L | L | L | 9 | 0 | 5 | 13 | 0 |
| R08 probe P-DER/P-NUM | L | L† | T† | M | T | L | T† | L | L† | 5 | 3 | 2 | 5 | 0 |
| R09 probe P-ID/P-NUM | L† | L | L | L† | T† | L | T† | L† | M | 6 | 2 | 3 | 11 | 0 |
| R10 probe P-INF/P-MEAS/P-LIT | L | L | L | L | L | L | L | L | L | 9 | 0 | 4 | 16 | 0 |

Notes:
- **Without referrals:**
  - R08: located 3, touched 1, known-unseeded 1, new-substantive 2.
  - R09: located 3, touched 0, known-unseeded 3, new-substantive 10.
- **Unseeded counts** are one per category per output. They include the eleven new categories NS-q to NS-aa, which are defined in §4.0.
- **Mistaken:** none counted. Two questionable remarks are recorded in §3 and in the detail.

**In scope, by each probe's assigned types as its own file states them:**

| Probe (assigned types) | SD1 | SD2 | SD3 | SD4 | SD5 | SD6 | SD7 | SD8 | SD9 |
|---|---|---|---|---|---|---|---|---|---|
| R08 (P-DER main; P-NUM secondary, "arithmetic in §2 and §4 that bears on the model") | Y | N | N | N | N | Y | N | Y | N |
| R09 (P-ID; P-NUM on "every reported statistic in ms:§3 and ms:§4") | N | Y | Y | N | N | Y | N | N | N |
| R10 (P-INF, P-MEAS, P-LIT) | N | N | Y | Y | Y | N | Y | Y | Y |

R10 typed its SD1, SD2 and SD6 findings itself as "cross-type" (P-DER, P-ID, P-NUM), so I mark them N. R08 referred H3 to P-INF, which puts SD3 out of its scope.

## 2. Probe statuses for located SDs

| Probe | SD | In scope | Where | Status after Part 2 |
|---|---|---|---|---|
| R08 | SD1 | Y | `p08:fnd:1` (chk:2) | demonstrated |
| R08 | SD2 † | N | Part 1 §5, referral to P-ID | asserted (referral; R08 says it is not a finding; no check) |
| R08 | SD6 | Y | `p08:fnd:6` (stars), `p08:fnd:7` (N), chk:4 | demonstrated (both) |
| R08 | SD8 | Y | `p08:fnd:4` (chk:3) | demonstrated |
| R08 | SD9 † | N | `p08:inc:4`, "referred to P-INF" | asserted (no check; Part 2 says its premise is "weakened" by fnd:1 and fnd:2) |
| R09 | SD1 † | N | `p09:ref:1`, referral to P-DER | asserted (referral) |
| R09 | SD2 | Y | `p09:fnd:5` (chk:5) | demonstrated |
| R09 | SD3 | Y | `p09:fnd:3` (chk:3) | demonstrated |
| R09 | SD4 † | N | `p09:ref:4`, referral to P-MEAS; the point is repeated in the repair of `p09:fnd:7` | asserted (referral). fnd:7 is inconclusive, but its check tested noise, not referents |
| R09 | SD6 | Y | `p09:fnd:1` (chk:1), `p09:fnd:2` (chk:2) | demonstrated (both) |
| R09 | SD8 † | N | `p09:ref:2`, referral to P-DER/P-INF | asserted (referral) |
| R10 | SD1 | N | `p10:fnd:3`, cross-type P-DER (chk:1 A) | demonstrated |
| R10 | SD2 | N | `p10:fnd:6`, cross-type P-ID (chk:3) | demonstrated |
| R10 | SD3 | Y | `p10:fnd:1` (chk:2 e) | demonstrated |
| R10 | SD4 | Y | `p10:fnd:11` | asserted |
| R10 | SD5 | Y | `p10:fnd:4` | asserted |
| R10 | SD6 | N | `p10:fnd:21`, cross-type P-NUM (chk:2 a, b) | demonstrated |
| R10 | SD7 | Y | `p10:fnd:17` | asserted |
| R10 | SD8 | Y | `p10:fnd:10` (chk:1 B) | demonstrated (severity raised to damaging) |
| R10 | SD9 | Y | `p10:inc:2`, carried in `p10:fnd:4` | asserted |

## 3. Calls I was unsure of

1. **R08 SD3, scored T† (the call I was least sure of).**
   - What R08 says: the referral names the MI7 step ("from 'no longer significant' to 'rule out'"), and Part 2 gives the interval [−0.033, 0.117].
   - What it does not say: that the interval admits a substantial peer effect, or that an equivalence or power analysis is missing. I took this as a partial reason.
   - If the interval, quoted in that context, is read as the reason, the code becomes L†.
2. **Counting referrals (R08, R09).** I scored them on content and marked them †, although R08 says its referrals are not findings. Without them, R08 drops from 5 L to 3 L and R09 from 6 L to 3 L.
3. **R06 SD4, scored L.**
   - The right reason appears only in the scoreboard entry `r-did:cmt:19` ("referents ... are perceived-successful or legitimate peers, not a state mean") and in §8.
   - R06 deliberately does not make the construct point a numbered finding.
   - I scored scoreboard text the same way in every output.
4. **R02 SD4, scored L.** The point is "Provisional" and deferred to "the second reviewer". It still gives the right reason (referents "regarded as successful or legitimate").
5. **SD9 for R03, R06 and R10, all scored L (likewise R08 †).**
   - Each puts the clash between the legitimacy account and "economizing" or "institutional fashion".
   - Each says the clash with "rule out mimetic isomorphism" is weaker or "not a strict contradiction".
   - I took this as the key's tension, stated more finely.
6. **R08 SD5, scored T.**
   - R08 calls the legitimacy story an "unlabelled abductive" auxiliary outside the model that is not needed once Prop. 2 is corrected.
   - It never says the story is untested, or that "consistent with our theory" is unwarranted. Instead it says the story "may still be true but is not needed".
7. **SD7 hedging.**
   - R02 ("If I recall correctly") and R04 ("unchecked ... I believe, but am not certain") are scored L, because each names Ang & Cummings (and R04 Loh & Venkatraman) as prior work.
   - R08 and R09 are scored T†. They flag the claim for checking but name no prior work.
8. **Borderline unseeded calls:**
   - KU2 for R04 (the bundle rival's "order of events" test).
   - NS-c for R03 and R05 (a reflection-problem mention, plus shared mandates in R05).
   - NS-k for R05 (decoupling of certification from working interoperability).
   - NS-t for R02 and R03 (a request for code, and a repair clause).
   - NS-a not credited to R03, whose fnd:14 only asks to "benchmark it against the decade's doubling".
9. **Not counted as mistaken:**
   - R03 `str:4` says "Once Prop. 2 is corrected, model and data agree on all signs". That overlooks the positive uncertainty point estimates (the corrected model implies ∂Φ/∂u ≤ 0) and R03's own fnd:2. It is a strength claim, not a finding.
   - R08 `inc:4` says "The tension dissolves if p08:fnd:1 is accepted". Accepting fnd:1 removes the need for the legitimacy auxiliary, not the authors' commitment to it. The finding itself states the tension correctly.

## 4. Per-output detail

### 4.0 New unseeded categories, and which outputs raise each category

New categories, used consistently across outputs:

- **NS-q.** The Abstract and Conclusion leave out the contrary H2 result (a selective summary).
- **NS-r.** The marginal effect of modularity, β1 + β3·u, reaches zero at about u = 1.7 to 1.9 SD. "In every specification" therefore holds only near mean uncertainty.
- **NS-s.** The rival is weakened in ways that go beyond the peer measure:
  - the two-stage diffusion prediction in the paper's own citations (technical reasons first, legitimacy later) is untested;
  - the opposition of fashion to economizing is a false dichotomy, since imitation can be efficient or informational, and efficiency can itself be an institutional logic.
- **NS-t.** Reproducibility and reporting:
  - there is no data or code availability statement; or
  - robustness results (licences included, non-system subsample) are asserted but not shown.
  The event study not being reported is NS-g, not NS-t.
- **NS-u.** "Strongly predicts" overstates a modest association (about 0.16 SD per SD of m; within R² rises by 0.05), or magnitudes use pooled rather than within-hospital SDs.
- **NS-v.** The model's domain does not match the measures:
  - u is a z-score and takes negative values, so H(u) can be ≤ 0 and the buy rule reverses; or
  - the share m can equal 1, which leaves k* undefined.
- **NS-w.** The practice implication ("attend first to the modularity of their systems") presupposes a causal and beneficial effect that the paper has not shown.
- **NS-x.** The novelty of the TCE contribution is overstated. "Specificity is partly a product of interface design", and the link from modularity to outsourcing, are already in the cited modularity literature and in uncited empirical work.
- **NS-y.** A behavioural or capability rival (problemistic search below aspiration, capability gaps) is neither considered nor tested.
- **NS-z.** H3 as stated, an unconditional association, is supported by Model 1. "H3 is not supported" judges a different, conditional proposition.
- **NS-aa.** With hospital fixed effects, a lagged state-mean peer regressor is subject to Nickell-type bias, downward when state-year shocks are serially independent. The Model 2 peer coefficient can therefore be biased in either direction.

Which outputs raise each category (✓ = raised; † = only in a referral; – = not raised):

| Category | R02 | R03 | R04 | R05 | R06 | R08 | R09 | R10 |
|---|---|---|---|---|---|---|---|---|
| KU1 staggered TWFE | ✓ | ✓ | ✓ | ✓ | ✓ | † | ✓ | ✓ |
| KU2 reverse timing | ✓ | ✓ | ✓ | ✓ | ✓ | – | ✓ | ✓ |
| KU3 single informant | ✓ | ✓ | ✓ | ✓ | ✓ | – | ✓ | ✓ |
| KU4 survivorship | ✓ | ✓ | ✓ | ✓ | ✓ | – | – | – |
| KU5 corner k* ≥ 1 | – | ✓ | ✓ | ✓ | ✓ | ✓ | – | ✓ |
| NS-a year FE / decomposition | – | – | – | ✓ | – | – | – | ✓ |
| NS-b modularity as channel | ✓ | ✓ | ✓ | ✓ | ✓ | – | ✓ | ✓ |
| NS-c state-year confounding | ✓ | ✓ | ✓ | ✓ | ✓ | – | ✓ | ✓ |
| NS-d noisy peer measure | ✓ | ✓ | ✓ | ✓ | – | – | ✓ | ✓ |
| NS-e clustering level | ✓ | ✓ | ✓ | ✓ | ✓ | – | ✓ | ✓ |
| NS-f time-varying confounders | ✓ | ✓ | – | – | ✓ | – | ✓ | – |
| NS-g event study reduced form | ✓ | ✓ | ✓ | ✓ | ✓ | † | ✓ | ✓ |
| NS-h coercive isomorphism | – | ✓ | ✓ | ✓ | – | – | † | ✓ |
| NS-i specificity mechanism | ✓ | ✓ | ✓ | ✓ | ✓ | † | – | ✓ |
| NS-j uncertainty proxy | – | ✓ | – | ✓ | ✓ | – | – | ✓ |
| NS-k modularity scope/construct | – | ✓ | ✓ | ✓ | – | – | – | ✓ |
| NS-l ∂k*/∂u < 0 vs estimates | ✓ | – | – | ✓ | ✓ | ✓ | – | – |
| NS-m rival economizing channels | – | ✓ | – | ✓ | – | – | – | – |
| NS-n economizing unevidenced | ✓ | – | ✓ | ✓ | – | – | – | ✓ |
| NS-o other post-outcome controls | – | – | – | – | – | – | – | ✓ |
| NS-p classification drift | – | – | – | – | – | – | – | ✓ |
| NS-q H2 omitted from summary | ✓ | – | – | – | – | – | – | – |
| NS-r marginal effect of m | ✓ | – | – | – | – | – | ✓ | – |
| NS-s rival's strongest form / dichotomy | ✓ | – | ✓ | ✓ | – | – | – | ✓ |
| NS-t reproducibility/reporting | ✓ | ✓ | ✓ | ✓ | ✓ | – | ✓ | – |
| NS-u "strongly" | – | ✓ | ✓ | ✓ | ✓ | † | ✓ | ✓ |
| NS-v model domain | – | ✓ | – | – | ✓ | ✓ | – | – |
| NS-w practice implication | – | ✓ | ✓ | ✓ | ✓ | – | – | – |
| NS-x TCE novelty | – | ✓ | – | ✓ | – | – | – | ✓ |
| NS-y behavioural rival | – | – | – | ✓ | – | – | – | – |
| NS-z H3 stated vs tested | – | – | – | – | ✓ | – | – | – |
| NS-aa Nickell-type peer bias | – | – | – | – | – | – | ✓ | – |

### 4.1 R02, the reviewer's draft (written without the workbench)

| SD | Code | Evidence (quoted) |
|---|---|---|
| SD1 | L | "The proof treats H as constant in u." "The numerator reduces to g1h0 − h1(s+g0), which A3 makes negative." |
| SD2 | L | "In-house staffing is partly the outcome (§3.2 says outsourcing removes it), so Model 4 says nothing about capability." |
| SD3 | L | "has a 95% CI of about −0.03 to 0.12 ... The interval includes 0.07." "'rules out' (abstract, §5) is not supported" |
| SD4 | L | "Provisionally, an unweighted state mean does not match the paper's own statement of the rival: peers 'regarded as successful or legitimate' (§1)." It is deferred to the second reviewer. There is no point on peer × uncertainty. |
| SD5 | L | "It is an after-the-fact mechanism outside the model, so it counts against the model" |
| SD6 | L | "412 × 11 = 4,532, not 4,712"; "starred *** although t ≈ 1.65". Both (a) and (b). |
| SD7 | L | "Priority. If I recall correctly, Ang and Cummings (1997, Organization Science) examined institutional and efficiency influences on IS outsourcing (to verify)." |
| SD8 | L | "There is also no aggregation step from a function-level threshold to a spending-weighted share. On the share scale, the interaction's sign also depends on how spending is distributed near k*." |
| SD9 | L | "It is also an institutional mechanism, in a paper claiming to have ruled such mechanisms out." |

Unseeded findings (4 known-unseeded, 13 new-substantive):
- **KU1.** Major 3: two-way FE "with staggered adoption, which is biased when effects vary by cohort".
- **KU2.** Major 3: "Hospitals planning to outsource, or their vendors, may install certified interfaces first."
- **KU3.** Minor: specificity is "a perceptual, single-informant rating, unvalidated".
- **KU4.** Minor: "Survival selection ... report the exclusions and their trends before exit."
- **NS-b.** Major 2: "If hospitals imitate peers by adopting standards, modularity lies on the imitation path."
- **NS-c.** Major 2: "A lagged state mean confounds imitation with state-level conditions, including the interface requirements".
- **NS-d.** Major 2: a state mean "over about eight sample hospitals is noisy enough to lose a horse race". Minor: asks how single-hospital states are handled.
- **NS-e.** Major 2: hospital clustering of a state-year regressor makes the interval too narrow. Major 3: cluster by state, with a wild bootstrap.
- **NS-f.** Minor: the EHR programme is absorbed by year effects "only if its effects were common across hospitals".
- **NS-g.** Major 3: "the event study is a reduced form. Report the first stage". Major 2: "State requirements could raise outsourcing directly".
- **NS-i.** Major 3: specificity "is the theory's own channel"; asks for the effect of modularity on specificity. Minor: specificity "depends on current sourcing".
- **NS-l.** Major 1: "The corrected model implies ∂k*/∂u < 0 ... Yet the uncertainty coefficient in Model 3 is positive".
- **NS-n.** Major 4: "Efficiency claims need a selection argument ... Show the cost consequences".
- **NS-q.** Major 1: "The abstract and the conclusion leave out the H2 result".
- **NS-r.** Minor: "0.118 − 0.061u, which reaches zero near u = 1.9 SD".
- **NS-s.** Major 4: "'fashion' mixes motive with outcome. Mimetic isomorphism, as cited, is about motive".
- **NS-t.** Minor: "please supply code that reproduces Table 2".

Points that only elaborate a seeded defect (not counted):
- the §2.3 intuition point (SD1);
- the smallest effect of interest set at 0.07 (SD3);
- the lag also dropping 2009 (SD6).

Mistaken: none.

### 4.2 R03, simulated reviewer TCE (resembling)

| SD | Code | Evidence (quoted) |
|---|---|---|
| SD1 | L | fnd:1: "H(u) = h0 + h1u also sits in the denominator ... A3 says exactly that h1(s+g0) > g1 h0, so the cross-partial is negative." |
| SD2 | L | fnd:7: "Staffing is therefore partly an outcome of Φ ... Conditioning on it is post-treatment conditioning. The coefficient's survival ... is compatible with confounding by capability" |
| SD3 | L | fnd:4: "The inference from 'no longer significant' ... to 'no effect' is MI7. The approximate 95% interval [-0.032, 0.116] includes economically meaningful peer effects." |
| SD4 | L | fnd:5(b): "It is not the set of referents 'perceived as legitimate or successful' that the rival names, so the rival is not stated in its strongest form." |
| SD5 | L | fnd:3: "an unlabelled abduction ('We believe it reflects...') with no test"; inc:2: "explained by a mechanism the model 'abstracts from' is not consistent with that theory." |
| SD6 | L | fnd:13: "N = 4,712 is not equal to 412 × 11 = 4,532"; "0.084 (0.051) is marked *** but t ≈ 1.65 (p ≈ 0.10)". |
| SD7 | L | fnd:15: "Prior work may already set economic against institutional influences on IT outsourcing. Candidates are Loh & Venkatraman 1992 ... Ang & Cummings 1997". vrd:4 adds: "likely contradicted". |
| SD8 | L | fnd:2: "There is no aggregation step. With Φ = F(k*) ... its sign depends on F." |
| SD9 | L | inc:3: "Invoking legitimacy pressures ... concedes that a non-economizing, institutional force shapes sourcing ... That clashes with 'Its substance is economizing'". It calls the clash with "rule out mimetic isomorphism" weaker (see §3, item 5). |

Unseeded findings (5 known-unseeded, 16 new-substantive):
- **KU1.** fnd:8(a): TWFE under staggered timing.
- **KU2.** fnd:6 and chl:5: vendors install interfaces when they take over functions. alt:1: joint choice of governance and safeguard.
- **KU3.** fnd:16: "m, specificity and Φ all come from the same CIO survey".
- **KU4.** fnd:16: "Selection on response and on survival".
- **KU5.** fnd:2: "k* can exceed 1 (Φ saturates at 1)"; chl:2.
- **NS-b.** fnd:5(a): "Controlling for m then blocks the institutional pathway". cmt:16: the "common diffusion of standards" reading is untested.
- **NS-c.** fnd:5(c): the reflection problem. chl:4: state-by-year effects.
- **NS-d.** fnd:5(c): "thin state cells add measurement error".
- **NS-e.** fnd:8(d): the peer measure and the treatment vary by state, but SEs are clustered by hospital.
- **NS-f.** fnd:6: "Differential exposure to the 2009 federal incentive programme ... is not absorbed by year effects".
- **NS-g.** fnd:8(b)–(c): reduced form, no first stage, exclusion broken via vendor entry, not reported.
- **NS-h.** fnd:5(a): state requirements "are what institutional theory calls coercive isomorphism".
- **NS-i.** fnd:9, inc:5 and chl:8: the mechanism is not evidenced, and specificity is conditioned on as the mediator.
- **NS-j.** fnd:11: "Demand volatility is a distal proxy".
- **NS-k.** fnd:10: m covers clinical systems only, while Φ includes hosting and help desk.
- **NS-m.** fnd:9: m may work by "raising vendors' production-cost advantage s". alt:1 gives a production-cost variant.
- **NS-t.** fnd:8 repair: "State whether code and survey data are available".
- **NS-u.** fnd:14: "The arithmetic is right (asserted); 'strongly' is not."
- **NS-v.** fnd:11 and chl:11: "Standardization gives negative u, whereas the model requires u ≥ 0".
- **NS-w.** fnd:17: the practice advice "rests on the causal reading".
- **NS-x.** fnd:15: the modularity-to-disintegration link "is established in the paper's own sources ... and tested in Hoetker 2006". vrd:5 makes the same point.

Points that only elaborate a seeded defect (not counted):
- chl:3, the test of the M1–M2 change (SD3);
- vrd:1 on the §2.3 intuition (SD1).

Mistaken: none counted. `str:4` ("model and data agree on all signs") overstates; see §3, item 9.

### 4.3 R04, simulated reviewer INST (differing)

| SD | Code | Evidence (quoted) |
|---|---|---|
| SD1 | L | fnd:8: "It does not differentiate H(u) in the denominator ... So under the manuscript's own assumption, Proposition 2 is false and the sign is reversed" |
| SD2 | L | fnd:14: "Staffing is therefore partly an outcome of Phi, and conditioning on it can bias the modularity coefficient in either direction. The Model 4 robustness claim is unentitled." |
| SD3 | L | fnd:7(b)1: "95% interval is about [-0.032, 0.116]. Its upper end is about 85% of the Model 1 point estimate ... 'Not significant' is not 'ruled out'" |
| SD4 | L | fnd:2: "referents *perceived as legitimate or successful* ... no referent structure: no prestige, size, system ties or shared vendors". fnd:7(b)3 also notes that no peer × uncertainty term is estimated. |
| SD5 | L | cmt:13: "Post hoc. Untested." fnd:9: "The TCE model ... has no legitimacy term, so the interpretation is not 'consistent with' the theory" |
| SD6 | L | fnd:16: "0.084*** with SE 0.051. The z-ratio is about 1.65"; "412 x 11 years ... = 4,532, not 4,712". |
| SD7 | L | fnd:4: "earlier studies modelled IT outsourcing diffusion as internal (imitative) versus external influence, or weighed institutional against economic drivers of IS outsourcing: Loh & Venkatraman 1992 ...; Ang & Cummings 1997". The ctb:5 verdict narrows the claim to "among the studies". |
| SD8 | L | fnd:3: "The propositions concern the threshold k* for single functions. The test concerns Phi, a spending-weighted aggregate ... the sign depends on f'" |
| SD9 | L | inc:2: "cannot hold that the practice's 'substance is economizing' ... while also explaining a main result by legitimacy pressures that retain functions independently of efficiency" |

Unseeded findings (5 known-unseeded, 13 new-substantive):
- **KU1.** fnd:15: staggered TWFE.
- **KU2.** §5, observation 3: "Order of events ... the two co-occur in adoption episodes" (borderline; see §3, item 8).
- **KU3.** fnd:11: one informant, common-method variance. chl:12: validate certification.
- **KU4.** fnd:12: "selects on continued survival and survey compliance".
- **KU5.** fnd:3: "There is also a ceiling once k* >= 1."
- **NS-b.** fnd:7(b)2: "modularity is the channel through which imitation operates". chl:6.
- **NS-c.** fnd:2(iv): the peer measure carries "the same variation carried by the state certification mandates". fnd:13: state-specific timing.
- **NS-d.** fnd:2(iii): "state peer groups may be small, which plausibly attenuates the coefficient".
- **NS-e.** fnd:15: cluster by state.
- **NS-g.** fnd:13: reduced form, exclusion not argued, no first stage, no coefficients.
- **NS-h.** fnd:1: "coercive isomorphism ... The opposition in the title holds only against *mimetic* isomorphism."
- **NS-i.** fnd:10(ii) and inc:5: specificity does not absorb m.
- **NS-k.** fnd:3: m covers clinical systems only, while Φ includes hosting and help desk. fnd:11: certification may be decoupled from working interoperability.
- **NS-n.** fnd:10(i): "No cost, quality or performance consequences are measured."
- **NS-s.** fnd:5: the paper argues against "a weaker institutional theory than the one in the cited corpus". fnd:7(b)3: the two-stage prediction is untested.
- **NS-t.** fnd:17: no code or data statement.
- **NS-u.** fnd:16: "'strongly predicts' ... for an effect of about one-sixth of an SD".
- **NS-w.** fnd:6: the practice implication is not entitled.

Points that only elaborate a seeded defect (not counted):
- peer × uncertainty (SD4);
- the §2.3 intuition in fnd:8 (SD1).

Mistaken: none.

### 4.4 R05, simulated reviewer BEH (differing)

| SD | Code | Evidence (quoted) |
|---|---|---|
| SD1 | L | fnd:9: "differentiates ... in u as if H were constant ... A3 ... is equivalent to h1*(s+g0) > g1*h0, so the cross-partial is negative for every u >= 0." |
| SD2 | L | fnd:18: "In-house IT staffing is, by the manuscript's own account, reduced by outsourcing ... Model 4 conditions on an outcome. The claim ... is unentitled." |
| SD3 | L | fnd:4: "That is MI7 ... 95% CI of about [-0.032, 0.116]; the upper bound is about 85% of the Model 1 estimate ... No equivalence test is reported." |
| SD4 | L | fnd:3(a): "a same-state mean of other sample hospitals is not the referent set of mimetic theory (MI3; ms:§1 para 1 itself names peers 'they regard as successful or legitimate')" |
| SD5 | L | fnd:11: "introduced after the result, is untested, and is not labelled as conjecture ... called 'consistent with our theory' although the theory predicted the opposite sign" |
| SD6 | L | fnd:20: "N = 4,712 versus 412 x 11 = 4,532"; "0.084 (0.051) is starred *** but t is about 1.65". |
| SD7 | L | fnd:15: "'First study to adjudicate directly' appears to be contradicted by earlier work". Names Loh & Venkatraman (1992) and Ang & Cummings (1997). |
| SD8 | L | fnd:2(i): "Function to hospital requires the spending-weighted distribution F of nominal k, which is never stated." fnd:10: "Prop 2 concerns k*." |
| SD9 | L | inc:3: "invokes a legitimacy mechanism (cf. MI10) to save its interaction result while denying institutional drivers elsewhere." |

Unseeded findings (5 known-unseeded, 19 new-substantive):
- **KU1.** fnd:5(iii): staggered TWFE.
- **KU2.** fnd:5(i): the vendor may install or certify interfaces as part of the transition.
- **KU3.** fnd:6: one informant, common-method variance; validate m and Φ.
- **KU4.** fnd:6: "attrition may be selection on the outcome".
- **KU5.** fnd:10: "Corner cases (k* >= 1, all functions bought)".
- **NS-a.** fnd:2(ii): "year fixed effects absorb the common diffusion path"; asks for a decomposition of the 2009–2019 rise.
- **NS-b.** fnd:4: "Conditioning on a mediator removes the indirect mimetic path".
- **NS-c.** fnd:19: the reflection problem. Step 5: same-state peers "share mandates, vendors and social aspiration referents".
- **NS-d.** fnd:19: "Peer means built from few hospitals per state are noisy".
- **NS-e.** fnd:19: cluster by state.
- **NS-g.** fnd:5(ii) and (iv): reduced form, no first stage, exclusion unargued, nothing reported.
- **NS-h.** cmt:27: the identifying variation is "institutional (coercive)". fnd:12: coercive and normative pathways are not stated.
- **NS-i.** fnd:14: the mechanism is not traced. fnd:3(d): nominal or effective specificity. fnd:18: specificity may be post-treatment.
- **NS-j.** fnd:3(c): "volatility of inpatient admissions is demand volatility, not the TCE construct".
- **NS-k.** fnd:3(b): "certification is formal adoption and may be decoupled from functional interoperability" (borderline; see §3, item 8).
- **NS-l.** fnd:21: "Under A3 the model implies dPhi/du < 0 at every m ... Table 2 shows a positive (non-significant) uncertainty main effect".
- **NS-m.** fnd:14: other channels, namely "search costs, vendor availability, or erosion of in-house capability".
- **NS-n.** fnd:1: "No outcome shows economizing".
- **NS-s.** fnd:13: the paper is eliminative and reductive towards institutional theory; the two accounts are "complements at different levels, not rivals".
- **NS-t.** fnd:22: estimates described but not shown; no data or code statement.
- **NS-u.** fnd:7: "'Strongly predicts' ... describe 2.7 pp per SD".
- **NS-w.** fnd:17: the advice "presumes both a causal effect and that outsourcing is beneficial".
- **NS-x.** fnd:16: ctb:4 "is anticipated by the works the manuscript cites".
- **NS-y.** fnd:12: "No behavioral or capability rival is considered". chl:11 and step 5 propose an aspiration test.

Points that only elaborate a seeded defect, or are not weaknesses (not counted):
- fnd:10 (SD8);
- fnd:8, a conditional strength rather than a weakness.

Mistaken: none.

### 4.5 R06, simulated reviewer DID (differing)

| SD | Code | Evidence (quoted) |
|---|---|---|
| SD1 | L | fnd:7: "H(u) = h0 + h1 u sits in the denominator of k* ... Assumption A3 is exactly the condition that makes this numerator negative." |
| SD2 | L | fnd:3: "It is a descendant of the outcome, a bad control ... The claim that the effect 'cannot be attributed to differences in internal IT capability' ... is unentitled." |
| SD3 | L | fnd:2: "This is MI7. (i) The 95% interval is about [-0.03, 0.12]; it excludes little, and an equivalence test at conventional bounds cannot be passed" |
| SD4 | L | cmt:19: "referents in the institutional account are perceived-successful or legitimate peers, not a state mean". This appears in the scoreboard only (see §3, item 3). |
| SD5 | L | fnd:9: "a legitimacy-signalling explanation that is untested, sits outside the model, is called 'consistent with our theory'". §3.1: "the explanation offered was constructed after the result". |
| SD6 | L | fnd:5: "412 hospitals x 11 years = 4,532, not the 4,712 reported". fnd:6: "0.084 (0.051) with ***; \|t\| = 1.65, p about 0.10". |
| SD7 | L | fnd:18: "this one is checkable and I doubt it. Earlier work tested economic versus institutional or imitation accounts of IS outsourcing". Names Loh & Venkatraman (1992) and Ang & Cummings (1997). |
| SD8 | L | fnd:8: "Propositions concern the threshold k*; hypotheses are tested on Phi ... Its sign depends on f' ... The step from proposition to hypothesis is an enthymeme." |
| SD9 | L | inc:5: "not a strict contradiction with 'rule out mimetic isomorphism', but it is incompatible with the stronger closing claim that the substance is economizing." See §3, item 5. |

Unseeded findings (5 known-unseeded, 13 new-substantive):
- **KU1.** fnd:4: TWFE under staggered adoption.
- **KU2.** fnd:1(a): "Phi can cause m within hospital". rival:1.
- **KU3.** fnd:20: correlated single-informant reporting; use certification records.
- **KU4.** fnd:15: "Continuous response may correlate with sourcing".
- **KU5.** fnd:8 and chl:5: the step needs "k* interior to [0,1]".
- **NS-b.** fnd:2(ii): "modularity is a mediator of imitation".
- **NS-c.** fnd:2(iii): "state-level correlated shocks"; chl:4.
- **NS-e.** fnd:11: hospital clustering of a state-year regressor.
- **NS-f.** fnd:1(b): "Hospital-specific timing of certified-EHR adoption ... year FE remove only its national average".
- **NS-g.** fnd:4: reduced form, no first stage, exclusion, not reported.
- **NS-i.** fnd:12: the specificity control may be a mediator; "use it as an outcome in a mechanism test".
- **NS-j.** fnd:16: "Demand volatility is a loose proxy".
- **NS-l.** chl:6: "The corrected model implies a negative main effect of uncertainty ... Table 2 reports a positive (imprecise) one."
- **NS-t.** fnd:13: no replication package.
- **NS-u.** fnd:14: "'strongly predicts' ... overstates a one-sixth-SD association".
- **NS-v.** fnd:8: "m is a share that can reach 1 in the data ... while the model requires m < 1".
- **NS-w.** fnd:19: the practice implication presupposes causality.
- **NS-z.** inc:7 and fnd:10: "H3 is stated unconditionally ... Model 1 supports it".

Points that only elaborate a seeded defect (not counted):
- fnd:17, that the legitimacy account is "functional in form" (SD5).

Mistaken: none.

### 4.6 R08, probe of the derivation (P-DER main, P-NUM secondary)

| SD | Code | In scope | Status after Part 2 | Evidence (quoted) |
|---|---|---|---|---|
| SD1 | L | Y | demonstrated (chk:2) | fnd:1: "The Appendix differentiates dk*/dm with respect to u as if H(u) were constant ... A3 is exactly the condition that makes it negative." |
| SD2 | L† | N | asserted (referral) | §5: "in-house IT staffing is partly a consequence of the outcome. The claim ... that the modularity effect 'cannot be attributed to capability differences' needs argument." Heading: "Model 4 adds a bad control." |
| SD3 | T† | N | asserted (referral) | §5: "The H3 inference runs from 'no longer significant' to 'rule out' (MI7)." Part 2: "a Model 2 peer CI of [−0.033, 0.117]". The interval is not interpreted. |
| SD4 | M | N | – | – |
| SD5 | T | N | fnd:2 demonstrated, but only on the k* sign | fnd:2: "a mechanism the model 'abstracts from' ... the auxiliary (legitimacy signalling) is an unlabelled abductive move." Part 2: the story "may still be true but is not needed". |
| SD6 | L | Y | demonstrated (chk:4) | fnd:6: "\|t\| = 0.084/0.051 ≈ 1.65, so p ≈ 0.10, but three stars". fnd:7: "4,712 = 412 × 11.44 is not a multiple of 412". |
| SD7 | T† | N | asserted (referral) | §5: "P-LIT: 'the first study to adjudicate directly ...' (Abstract, §1) (to verify)." No prior work is named. |
| SD8 | L | Y | demonstrated (chk:3) | fnd:4: "F the spending-weighted CDF of nominal k ... assumed fixed in m and u (§2.4 needs this but does not state it)". |
| SD9 | L† | N | asserted (referred to P-INF) | inc:4: "§5 brings in an institutional (legitimacy) mechanism to explain the one result the model is said to miss, while §6 says the substance is economizing." |

Unseeded findings (2 known-unseeded, 5 new-substantive; 1 and 2 without referrals):
- **KU1 †.** §5: "a two-way FE event study under staggered state adoption".
- **KU5.** fnd:4: "At the corner k* >= 1, Phi = 1 and both effects vanish." Demonstrated.
- **NS-g †.** §5: "a reduced form of state requirements on outsourcing, not an estimate of the effect of modularity".
- **NS-i †.** §5: "the asset-specificity control may be the model's mediator".
- **NS-l.** fnd:5: under A3, dΦ/du ≤ 0, while the point estimates are positive for every m in [0,1]. The implication is demonstrated; as evidence against the model it is inconclusive (max \|z\| = 1.65).
- **NS-u †.** §5: "'Strongly predicts' describes an effect of about 0.16 SD."
- **NS-v.** fnd:8: "H(u) <= 0 is possible ... the buy rule reverses. k* is undefined at m = 1." Demonstrated.

Points that only elaborate a seeded defect (not counted):
- fnd:3, the §2.3 intuition (SD1);
- inc:2, Prop. 2 holds iff A3 fails (SD1);
- the §7.4 remark on general functional forms (SD1).

Mistaken: none counted. The remark in inc:4 that the tension "dissolves" is noted in §3, item 9.

### 4.7 R09, probe of identification and numerical consistency (P-ID, P-NUM)

| SD | Code | In scope | Status after Part 2 | Evidence (quoted) |
|---|---|---|---|---|
| SD1 | L† | N | asserted (referral) | ref:1: "The numerator reduces to g1·h0 − h1·(s + g0), which does not depend on u and is negative under Assumption A3." "The Appendix proof drops the H′(u) term" |
| SD2 | L | Y | demonstrated (chk:5) | fnd:5: "staffing is a descendant of Phi and of the confounder ... survival of the coefficient (0.118 -> 0.097) is uninformative about confounding" |
| SD3 | L | Y | demonstrated (chk:3) | fnd:3: "95% CI ... is about [-0.033, 0.117]; its upper end is 85% of the Model 1 association (0.137). A TOST equivalence test ... fails" |
| SD4 | L† | N | asserted (referral) | ref:4: "Peer is a state mean of respondent hospitals. MI3's construct is referents perceived as legitimate or successful." The fnd:7 repair says: "Use the referents that MI3 names". |
| SD5 | T† | N | asserted (referral) | arg:8: "a legitimacy-signalling rescue" (classed as abductive). ref:1: "'contrary to H2' ... and the legitimacy rescue (`ms:§5`) rest on a derivation error." |
| SD6 | L | Y | demonstrated (chk:1, chk:2) | fnd:1: "412 x 11 = 4,532; 4,712/412 = 11.44 is not an integer". fnd:2: "t = 0.084/0.051 = 1.65; two-sided p about 0.10". |
| SD7 | T† | N | asserted (referral) | ref:5: "'First study to adjudicate directly' (Abstract, `ms:§1`) is not checked here." |
| SD8 | L† | N | asserted (referral) | ref:2: "H2 is tested on Φ, a spending-weighted share, while Proposition 2 concerns the threshold k*. Carrying the sign from k* to Φ needs the distribution of k" |
| SD9 | M | N | – | ref:3 raises coercive isomorphism, not the tension between legitimacy and "rule out". |

Unseeded findings (3 known-unseeded, 11 new-substantive; 3 and 10 without referrals):
- **KU1.** fnd:9(a): demonstrated, but Part 2 says it has limited bearing on the flat leads the authors report.
- **KU2.** fnd:8: same-year feedback from Φ to m. Demonstrated, conditional on an inferred edge.
- **KU3.** fnd:8 repair: "verify modularity from certification records rather than the same informant".
- **NS-b.** fnd:6: Model 2 conditions on a possible mediator of mimicry. Inconclusive; severity cut to damaging (provisional).
- **NS-c.** fnd:11: persistent state shocks produce a peer coefficient with no imitation. Demonstrated.
- **NS-d.** fnd:7: a noisy sample-based peer measure. Inconclusive, and partly undercut in Part 2. fnd:1: single-hospital states have no Peer.
- **NS-e.** fnd:10: hospital clustering over-rejects. Demonstrated, with a caveat.
- **NS-f.** chl:1: "differential exposure to EHR incentives".
- **NS-g.** fnd:9(b)–(c): the estimand is the effect of mandates; no first stage, no exclusion argument, nothing reported. Asserted.
- **NS-h †.** ref:3: "Diffusion driven by mandates is itself an institutional mechanism".
- **NS-r.** fnd:4(b): the modularity effect is zero at u = 1.93 SD (Model 3) and 1.67 SD (Model 4). Asserted, as a residual remark.
- **NS-t.** chl:8 and cmt:17: the robustness results (licences, non-system subsample) are "not reported".
- **NS-u.** fnd:4(a): pooled rather than within SDs; "'strongly' is then generous". Asserted, as a residual remark.
- **NS-aa.** fnd:12: the FE and lagged-Peer construction can bias β4 downward. New from the harness, asserted.

Not counted:
- §5 "Considered and not raised" (selection on response, the interaction under FE);
- fnd:4's arithmetic, which was refuted by the check and so stands as a strength of the manuscript;
- the "m at t−1" repair, which R09 withdrew.

Mistaken: none.

### 4.8 R10, probe for the inferential audit (P-INF, P-MEAS, P-LIT)

| SD | Code | In scope | Status after Part 2 | Evidence (quoted) |
|---|---|---|---|---|
| SD1 | L | N | demonstrated (chk:1 A) | fnd:3: "The proof treats H(u) as constant in u ... leaving g1 h0 - h1 (s+g0). That is negative exactly when A3 holds." |
| SD2 | L | N | demonstrated (chk:3) | fnd:6: "staffing falls when functions are outsourced, so it is partly an outcome of Phi ... Survival of beta_m therefore cannot license 'cannot be attributed'." |
| SD3 | L | Y | demonstrated (chk:2 e) | fnd:1: "The step from 'no longer significant' ... to 'rule out' is MI7 ... the M2 coefficient excludes neither zero nor peer effects close to the M1 estimate." |
| SD4 | L | Y | asserted | fnd:11: "mimetic isomorphism (MI3) specifies peers perceived as successful, legitimate or similar ..., or tied through systems, boards and consultants. 'All other sample hospitals in the same state' is none of these." Point (d) adds peer × uncertainty. |
| SD5 | L | Y | asserted | fnd:4: "explained ad hoc by legitimacy pressures, an institutional mechanism (MI10-type) outside the model. It is then declared 'consistent with our theory'. The move immunizes H2 from refutation." |
| SD6 | L | N | demonstrated (chk:2 a, b) | fnd:21: "412 x 11 = 4,532 observations, not 4,712"; "0.084/0.051 gives \|t\| of about 1.65 ... yet *** is reported." |
| SD7 | L | Y | asserted | fnd:17: "The priority claim is very probably false." Names Loh & Venkatraman (1992) and Ang & Cummings (1997). |
| SD8 | L | Y | demonstrated (chk:1 B) | fnd:10: "Phi = F(k*) for the spending-weighted distribution F of k ... The sign on the tested scale depends on the density at the threshold". |
| SD9 | L | Y | asserted | inc:2: "§5 ¶2 concedes an institutional mechanism that §6 denies. (Strictly compatible with cmt:11, which concerns mimetic isomorphism only.)" See §3, item 5. |

Unseeded findings (4 known-unseeded, 16 new-substantive):
- **KU1.** fnd:20: the staggered-adoption TWFE literature is omitted. fnd:7 cross-refers the same point.
- **KU2.** fnd:7: "outsourcing can raise m (reverse timing)". chl:7.
- **KU3.** fnd:13: "Outcome, focal regressor and specificity all come from one informant". Asks for validation.
- **KU5.** fnd:10: "At a corner (k* >= 1), dPhi/dm = 0."
- **NS-a.** fnd:9: the effect cannot account for a doubling "unless m rose by several SDs". Asks for a decomposition.
- **NS-b.** fnd:2: the discriminating prediction does not discriminate. Demonstrated, given `p10:dec:6`.
- **NS-c.** fnd:11(c): "a same-state peer mean mixes coercive and mimetic pressure". fnd:20: the reflection problem.
- **NS-d.** fnd:11(b): "The peer mean is therefore a noisy proxy for field prevalence."
- **NS-e.** fnd:1: hospital clustering "probably understates its SE".
- **NS-g.** fnd:7: reduced form, exclusion not stated, estimates not reported.
- **NS-h.** cmt:18, inc:5 and fnd:7: "the mandate is itself an institutional pressure".
- **NS-i.** fnd:5: the mechanism is untested (its numerical leg is inconclusive). fnd:15: the rating's referent is undefined and the rating may be caused by Φ.
- **NS-j.** fnd:14: "Volatility in inpatient demand is a different construct".
- **NS-k.** fnd:12: domain mismatch between clinical systems and all IT functions; "product certification with interface use".
- **NS-n.** fnd:8: "No costs, prices, hold-up incidents or performance outcomes are reported."
- **NS-o.** fnd:6: "Operating margin (a control) may raise the same issue".
- **NS-p.** fnd:16: "How cloud and subscription services are classified relative to the excluded licences is not stated."
- **NS-s.** fnd:19: the stage-dependent prediction is untested, and the efficiency-versus-imitation dichotomy is contested.
- **NS-u.** fnd:9: "'Strongly' conflates statistical with substantive strength."
- **NS-x.** fnd:18: "'Specificity is partly a product of interface design' is the thesis of works the manuscript cites".

Points that only elaborate a seeded defect (not counted):
- fnd:16's share mapping (SD8);
- fnd:11(d), peer × uncertainty (SD4);
- fnd:1's test of the M1–M2 change (SD3).

Mistaken: none.
