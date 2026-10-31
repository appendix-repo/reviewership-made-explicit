# Recovery scoring of R12, the reviewer's final review

- **Scorer:** the recovery scorer. The rules and readings are those of `recovery_scoring.md`, applied unchanged. That file is not edited.
- **Date:** 23 October 2026.
- **Files read:**
  - `runs/recovery_scoring.md`
  - `case/TEST_MANUSCRIPT.md`
  - `case/SEALED_DEFECT_KEY.md`
  - `runs/12_reviewer_dispositions_final_review.md`

  I read no other file, ran no code and did not use the web.
- **What was scored:** only the signed review, the text between `<!-- SIGNED REVIEW START -->` and `<!-- SIGNED REVIEW END -->`. That text includes the "Checks run" list and the confidential note to the editor, and I counted both, as I counted R02's checks list. I ignored the Dispositions block and the Attestation. A finding the Dispositions accept, but which does not appear in the signed text, earns no credit. For example, "while k* < 1" appears only in the Dispositions.
- **Codes:** L = located, T = touched, M = missed.

## 1. Summary row

| Run | SD1 | SD2 | SD3 | SD4 | SD5 | SD6 | SD7 | SD8 | SD9 | Located | Touched | Known-unseeded | New-substantive | Mistaken |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R12 reviewer's final review | L | L | L | L | L | L | L | L | L | 9 | 0 | 4 | 24 | 0 |
| *R02 reviewer's draft (for comparison)* | L | L | L | L | L | L | L | L | L | 9 | 0 | 4 | 13 | 0 |

Notes:
- **The new-substantive count of 24** is 23 of the existing categories plus one new category, NS-ab (§3). If NS-ab is read as an elaboration of SD1, the count is 23 (§5, item 1).
- **Known-unseeded** is out of 5. KU5 is the one not raised.

### Evidence for each seeded defect (quotes of 30 words or fewer)

| SD | Code | Evidence (quoted from the signed review) |
|---|---|---|
| SD1 | L | Major 1: "The proof treats H as constant in u." "A3 makes the numerator negative, so the cross-partial is negative at every admissible (m, u)." |
| SD2 | L | Major 3: "In-house staffing is partly the outcome ... Its survival in Model 4 therefore says nothing about capability, and 'cannot be attributed to capability differences' (§3.3, §4) does not follow." |
| SD3 | L | Major 2: "a 95% CI of about −0.03 to 0.12, which reaches 85% of the Model 1 estimate." "Equivalence fails at 0.07 (TOST p ≈ 0.24)." It also says "rule out" is not supported. |
| SD4 | L | Major 2: "§1 names peers that hospitals 'regard as successful or legitimate'. The measure is all other sample hospitals in the state, which are neither referents nor the state's hospital population." Peer × uncertainty is untested ("imitation under uncertainty, which implies a peer × uncertainty interaction"); I note this here, not as an unseeded finding. |
| SD5 | L | Major 1: "It is introduced after the result, uses a mechanism outside the model, and is called 'consistent with our theory'. So it counts against the model". It adds: "label it a conjecture and give it a test". |
| SD6 | L | Minor: "412 × 11 = 4,532, not 4,712." "Model 3 uncertainty, 0.084 (0.051), is starred *** at p ≈ 0.10." Both (a) and (b) are given. |
| SD7 | L | Minor: "Priority and novelty. If I recall correctly, Loh and Venkatraman (1992 ...) contrasted imitative and other influences on the diffusion of IT outsourcing. Ang and Cummings (1997 ...) examined institutional and efficiency influences". |
| SD8 | L | Major 1: "With Φ = F(k*) ... for H2 it does not: the interaction on Φ has the sign of [...] × [f(k*) + k*f′(k*)], so it depends on F." It asks the authors to "state its assumption on F, derive on Φ, or test at the function level." |
| SD9 | L | Major 1: the legitimacy account is "an institutional mechanism, in a paper that claims to have ruled such mechanisms out and concludes 'Its substance is economizing'." |

Points that only elaborate a seeded defect (not counted):
- **SD1:**
  - the general functional form ("A change of functional form will not rescue P2");
  - "P2 holds exactly when A3 fails";
  - "A3 ... is used in no proof";
  - the readability point on the intuition after P2, and stating A3 in words.
- **SD2:** the repair, capability measured before treatment.
- **SD3:** the request to test the change from 0.137 (the M1–M2 peer coefficient), and the smallest passable bound of 0.105.
- **SD4:** peer × uncertainty.
- **SD5:**
  - "does not say which assumption or step the failure puts in doubt (std:2(b))";
  - "The corrected sign is not a confirmation ... is a rescue". This frames the NS-l test.
- **SD6:** N = 4,120 if the lag drops 2009; "Intervals would serve better than stars".
- **SD8:**
  - the H1 step "holds ... for any F";
  - the qualification that reversal on Φ needs shares above about 0.6.

## 2. The 32 categories: R12 against R02

✓ = raised; – = not raised.

| Category | R12 | R12 locus or quote | R02 |
|---|---|---|---|
| KU1 staggered TWFE | ✓ | Major 3: "an estimator robust to effects that differ by adoption cohort, against not-yet-treated states". R12 no longer calls TWFE "biased" explicitly (§5, item 2). | ✓ |
| KU2 reverse timing | ✓ | Major 3: "Nothing argues that modularity was not chosen with outsourcing in view"; "vendors taking over a function may install them". | ✓ |
| KU3 single informant | ✓ | Minor: "One CIO reports m, the rating and, it seems, Φ ... control for CIO turnover, or validate m or Φ". Major 4: the rating is "perceptual, single-informant ... without validation". | ✓ |
| KU4 survivorship | ✓ | Minor: "Survival selection ... report the exclusions and their outcome trends before exit." | ✓ |
| KU5 corner k* ≥ 1 | – | Only "∂Φ/∂m = f(k*)·∂k*/∂m ≥ 0 for any F". The corner is never named. | – |
| NS-a year FE / decomposition | ✓ | Minor (Magnitude): "how much of the decade's doubling (§1) is accounted for by β1 times the change in mean m. Year effects absorb the rest". | – |
| NS-b modularity as channel | ✓ | Major 2: "If hospitals imitate their peers by adopting certified interfaces, modularity lies on the imitation path." | ✓ |
| NS-c state-year confounding | ✓ | Major 2: "Persistent state shocks alone yield a positive peer coefficient with no imitation"; it also cites the interface requirements and the reflection problem. | ✓ |
| NS-d noisy peer measure | ✓ | Major 2: "A mean over about eight sample hospitals per state is noisy ... it attenuates modest direct effects." | ✓ |
| NS-e clustering level | ✓ | Major 2: SEs "clustered by hospital ... please cluster by state, or two ways, with a small-cluster correction". Major 3 adds the wild bootstrap. | ✓ |
| NS-f time-varying confounders | ✓ | Major 3: the EHR incentive is absorbed by year effects "only if its effects were common across hospitals. Attestation timing varied". The request on large versus small changers' prior trends is filed here too. | ✓ |
| NS-g event study reduced form | ✓ | Major 3: "a reduced form of state requirements on outsourcing, with no first stage on m, and none of it is reported"; it names three threats to exclusion. | ✓ |
| NS-h coercive isomorphism | ✓ | Major 2: "state requirements for certified interfaces are coercive isomorphism. At most, the design speaks to mimetic isomorphism". | – |
| NS-i specificity mechanism | ✓ | Major 4: "The hold-up channel is not visible in Table 2". Also the omitted-variable inference (m moves about 0.03), the undefined referent, the rating "partly an outcome", and "either a mediator or a bad control". | ✓ |
| NS-j uncertainty proxy | ✓ | Minor: "Admissions volatility is demand volatility, whereas the model's u is disturbances that require adapting the IT transaction." | – |
| NS-k modularity scope/construct | ✓ | Major 4: "m covers clinical systems only, while Φ covers all functions, including hosting and help desk". The interoperability construct itself passes ("records use"). | – |
| NS-l ∂k*/∂u < 0 vs estimates | ✓ | Major 1: "Under A3, ∂k*/∂u < 0, so ∂Φ/∂u ≤ 0 at every m ... The point estimate ... is positive across the observed range of m". | ✓ |
| NS-m rival economizing channels | ✓ | Major 4: "certified interfaces may widen vendors' scale advantage s". Major 3: the requirements "may change vendor supply, and so ... s, directly". | – |
| NS-n economizing unevidenced | ✓ | Major 4: "need either a selection argument or direct evidence on costs ... the paper shows no cost, quality or hold-up outcome." | ✓ |
| NS-o other post-outcome controls | – | It asks only, in general, to "report the key coefficients without the controls". It names no control other than staffing (SD2) and the rating (NS-i) as post-outcome. | – |
| NS-p classification drift | – | – | – |
| NS-q H2 omitted from summary | ✓ | Major 1: "The abstract and the conclusion do not report the failure (std:2(a))." | ✓ |
| NS-r marginal effect of m | ✓ | Minor: "0.118 − 0.061u in Model 3, reaching zero near u = 1.9 SD (1.7 SD in Model 4)". | ✓ |
| NS-s rival's strongest form / dichotomy | ✓ | Major 2: "two-stage diffusion, in which later adopters are more imitative (Tolbert & Zucker 1983)". Major 4: "'Fashion' mixes motive with outcome." | ✓ |
| NS-t reproducibility/reporting | ✓ | Minor: "code that reproduces Table 2 and the event study, and the data". Major 3: "report the specifications that did not work". | ✓ |
| NS-u "strongly" | ✓ | Minor: "'Strongly predicts' (abstract) describes 2.7 points per SD of m, about 0.16 SD of Φ. Both figures use pooled SDs". | – |
| NS-v model domain | ✓ | Minor (Model domain): "u is a z-score, while the model needs u ≥ 0 ... k* is undefined at m = 1, which the data may reach." | – |
| NS-w practice implication | ✓ | Minor: "'attend first to the modularity of their systems' presupposes the causal effect and a benefit from outsourcing". | – |
| NS-x TCE novelty | ✓ | Minor: "That specificity is partly a product of interface design is already in the paper's own sources (Langlois 2002; Sanchez & Mahoney 1996)." | – |
| NS-y behavioural rival | – | Not in the signed text. | – |
| NS-z H3 stated vs tested | ✓ | Major 2: "H3 is stated as an unconditional association, which Model 1 supports. What §4 finds 'not supported' is the conditional version". | – (R02: "H3 is 'not supported', as §4 fairly says") |
| NS-aa Nickell-type peer bias | – | Not in the signed text. | – |

**Totals:**

| | KU raised | NS raised (of the 27) | NS-ab |
|---|---|---|---|
| R12 | 4 | 23 | yes |
| R02 | 4 | 13 | no |

- **Raised by R12 and not by R02 (10):** NS-a, NS-h, NS-j, NS-k, NS-m, NS-u, NS-v, NS-w, NS-x, NS-z.
- **Raised by R02 and not by R12:** none. Every one of R02's 17 categories reappears in R12.
- **Raised by neither:** KU5, NS-o, NS-p, NS-y, NS-aa.

## 3. New category, and mistaken findings

**New category**
- **NS-ab.** A3 is unmotivated for the setting.
  - It rests on a citation to Williamson (1991), not on an argument that hold-up hazards in hospital IT respond proportionally more to uncertainty than in-house costs do.
  - Once Prop. 2 is corrected, every derived sign depends on it.
  - R12, Major 1: "A3 needs a defence (std:1(b)). It rests on a citation, not on an argument that it holds for hospital IT. Every corrected sign below depends on it."
  - R02 does not raise it. R02's "then A3 is empty" is a different point. I did not check the other outputs for NS-ab, because I was scoring only R12.

**Mistaken:** none.

I checked the following against the manuscript, and each holds:
- the cross-partial, and its general form G′H − (s+G)H′;
- the sign of the interaction on Φ, [g1h0 − h1(s+g0)]·[f + k*f′];
- +0.056 at mean m;
- the CI for the interaction, −0.098 to −0.024;
- 85% of Model 1;
- TOST p ≈ 0.24, at a bound of half of 0.137, that is 0.0685;
- the smallest passable bound of about 0.105;
- the omitted-variable step: −0.094 = −0.091 + 0.112·δ gives δ ≈ −0.027;
- 15 of the 16 cells consistent;
- N = 4,120 under the lag;
- the zero crossings at 1.93 and 1.67;
- 2.7 points and 0.16 SD;
- all quotations from the manuscript.

I spot-checked the "about 0.6" Beta threshold at Beta(1,2) and Beta(2,5). The share at the reversal point is about 0.75 and 0.65, which is consistent with the claim. One imprecision is not counted as mistaken: in the readability point, "(h1k, which rises with u)". The saving H(u)k rises with u at rate h1k; h1k itself is constant in u.

## 4. SD codes that differ between R02 and R12

None: all nine are L in both. Within L, R12 is firmer in five places:
- **SD3:** R12 adds the TOST result and the smallest passable bound.
- **SD4:** R12 is no longer deferred. It is still "provisional" and flagged to the second reviewer, but it now places the mismatch against the paper's own §1 definition and adds peer × uncertainty.
- **SD5:** R12 adds "label it a conjecture and give it a test".
- **SD7:** R12 adds Loh & Venkatraman (1992) to Ang & Cummings (1997). It is still hedged with "If I recall correctly ... to verify".
- **SD8:** R12 gives the Φ = F(k*) algebra, and qualifies how likely a reversal is (shares above about 0.6).

## 5. Calls I was unsure of

1. **NS-ab counted as new-substantive.** It could be read as part of SD1, since the corrected sign depends on A3. I counted it because it questions whether the assumption holds in this setting, not the derivation. Without it, the row reads 23 new-substantive.
2. **KU1 credited.** R02 said TWFE "is biased when effects vary by cohort". R12 only asks for "an estimator robust to effects that differ by adoption cohort". I read the request as raising the weakness in substance. Without it, known-unseeded would be 3.
3. **KU5 not credited.** R12 writes "≥ 0 for any F" and "k* is undefined at m = 1" (NS-v), but never names the corner k* ≥ 1. The Dispositions' "while k* < 1" is outside the scored text.
4. **NS-o not credited.** "Report the key coefficients without the controls" is generic. It names no post-outcome control other than staffing and the rating.
5. **SD7 scored L.** As with R02, R12 never says in so many words that the "first study" claim is false. It names prior work under the heading "Priority and novelty", hedges it as "to verify", and asks the editor to "verify or strike" it. I read it the same way as R02.
6. **Requests filed under existing categories, without changing any count:**
   - the request on large versus small changers' prior trends (std:10) is filed under NS-f;
   - the request to report the specifications that did not work is filed under NS-t.

   This matches R02, whose similar std:10 requests were not counted as separate categories.
