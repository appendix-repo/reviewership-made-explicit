bs:T7 settled: must means must. The must parts of std:7 (controls that carry identifying weight) and std:8 (where efficiency is the paper's conclusion) cannot be shed; only their should parts can.

# Review: "Modularity, Not Mimicry: Interoperability Standards and the Diffusion of IT Outsourcing in U.S. Hospitals"

## Summary

The paper argues that certified interoperability standards made hospital IT modular, which lowered effective asset specificity and widened outsourcing. A threshold model yields two propositions. P1: modularity raises the outsourcing threshold. P2: uncertainty amplifies that effect.

A fixed-effects panel of 412 hospitals (2009–2019) finds three things:
- a positive within-hospital association between modularity and the outsourced share of IT spending (H1);
- a negative modularity × uncertainty interaction, which the authors report as contrary to H2;
- a peer-outsourcing coefficient that loses significance once modularity enters (H3).

The paper concludes that mimicry is "ruled out" and that outsourcing is "economizing".

The question matters, the mechanism deserves attention, and the panel is valuable. But P2 is mis-derived, the test of the rival does not discriminate, and the identification of the modularity effect needs work.

## Major concerns

### 1. P2 does not follow; under the paper's own A3 its sign is reversed (damaging, fixable)

I re-derived both propositions by hand (§2.2–2.3 and the Appendix).
- **P1 follows:** ∂k*/∂m = k*/(1−m) > 0.
- **P2 does not.** With G′ = g1 and H′ = h1:

  ∂²k*/∂m∂u = [g1H − h1(s+G)] / [H²(1−m)²]

  The numerator reduces to g1h0 − h1(s+g0), which A3 makes negative.
- **The proof's error.** The proof treats H as constant in u. That is an unstated assumption, and it contradicts h1 > 0. A3 is never used.

What follows:
- **H2 is not derived (std:1).** There is also no aggregation step from a function-level threshold to a spending-weighted share. On the share scale, the interaction's sign also depends on how spending is distributed near k*.
- **H2 failed as stated.** The estimate has the opposite sign and its interval excludes zero (95% CI about −0.10 to −0.02; std:2(e)). This counts against P2 as the paper derived it, not against the model's assumptions.
- **The estimate is not a confirmation either.** Nobody predicted it, and choosing an aggregation assumption now would be a rescue.
- **A cleaner check exists.** The corrected model implies ∂k*/∂u < 0, a sign that survives aggregation. Yet the uncertainty coefficient in Model 3 is positive: 0.084 (0.051), starred *** although t ≈ 1.65. If the stars are right, the corrected model fails this check.
- **The §5 legitimacy story.** It is an after-the-fact mechanism outside the model, so it counts against the model (std:2(c)–(d)). It is also an institutional mechanism, in a paper claiming to have ruled such mechanisms out.
- **Omission.** The abstract and the conclusion leave out the H2 result (std:2(a)).

**Where I may be wrong:** H may be meant not to vary with u. But then A3 is empty.

**A test whose result I can't predict:** model function-level outsourcing on k, m and u, using the survey's function-level ratings.

**What would persuade me:** a smaller modularity effect at high u in that model, together with a negative effect of u.

**Repair:** correct P2, add the aggregation step, fix the stars, and drop the explanation in §5.

### 2. The test of the rival does not discriminate (damaging, fixable)

§2.4 treats the disappearance of the peer coefficient as a discriminating test (std:3(b)). It is not, for three reasons:
- **Mediation (std:4(c)).** If hospitals imitate peers by adopting standards, modularity lies on the imitation path.
- **Shared conditions (std:14(a)).** A lagged state mean confounds imitation with state-level conditions, including the interface requirements that §4 uses. The authors' own reading of Model 2 ("the common diffusion of standards across hospitals in the same state") concedes this. A lag does not remove persistent conditions.
- **Collinearity and noise (std:4(a)–(b)).** The paper reports no peer–modularity correlation. A state mean over about eight sample hospitals is noisy enough to lose a horse race on its own.

**Bounds (std:13).** The Model 2 peer coefficient, 0.042 (0.038), has a 95% CI of about −0.03 to 0.12. Before computing it, I set the smallest effect that matters at half the Model 1 estimate, 0.07. That is my choice, and the authors may justify another. The interval includes 0.07. Clustering a state-year regressor by hospital probably makes the interval too narrow (std:9).

So H3 is "not supported", as §4 fairly says (std:2(e)). But "rules out" (abstract, §5) is not supported, and neither is the reinterpretation of "fashion" as "economizing" (std:3(e)–(f)). H1 fits both accounts (std:3(d)).

**The rival's construct (std:3(c)).** Provisionally, an unweighted state mean does not match the paper's own statement of the rival: peers "regarded as successful or legitimate" (§1). I put this to the second reviewer.

**The same bar for the paper's own account (std:12, std:14(c)).** State requirements could raise outsourcing directly, not only through modularity.

**Where I may be wrong:** the second reviewer may accept the state peer set.

**A test whose result I can't predict:** a non-geographic peer group (similar hospitals in other states), estimated with state-by-year fixed effects.

**What would persuade me:** an interval in that test that excludes 0.07. That would justify "no evidence of imitation through this channel".

**Repair:** the title, the abstract and §5–6 should say that the evidence does not require mimicry.

### 3. Identification of the modularity effect (damaging, fixable)

- **Direction (std:11).** Direction is not argued. Hospitals planning to outsource, or their vendors, may install certified interfaces first.
- **Two bad controls.**
  - In-house staffing is partly the outcome (§3.2 says outsourcing removes it), so Model 4 says nothing about capability.
  - Asset specificity, controlled throughout, is the theory's own channel (effective specificity is k(1−m)). The models therefore estimate the effect of modularity other than through specificity. Report the results without this control, and the effect of modularity on specificity (std:3(g)).
- **The event study (std:10(e), std:13).** It uses two-way fixed effects with staggered adoption, which is biased when effects vary by cohort.
  - Use a robust estimator against not-yet-treated states (Callaway & Sant'Anna 2021; Sun & Abraham 2021; to verify).
  - Show leads with intervals that exclude pre-trends of half the post-adoption effect, or report a Rambachan–Roth sensitivity analysis (to verify).
  - Cluster by state with a wild bootstrap, since there are fewer than 50 states.
- **First stage.** As it stands, the event study is a reduced form. Report the first stage and use the requirements as an instrument. This is the paper's best route to identification.
- **Also report (std:10(b), (f), (g)):** the within-hospital variation in modularity, leads of modularity, and how the main specification was chosen.

**Where I may be wrong:** some of this may have been done but not reported.

**What would persuade me:** an IV estimate with a strong first stage, and leads that are flat and precise.

### 4. "Economizing" claims efficiency without showing selection (fixable)

Three phrases are efficiency claims: "economizing" (abstract, §6), "efficiency-enhancing" (§5.1) and "the conditions that make it efficient" (§6). Efficiency claims need a selection argument, and selection is weak among non-profit and public hospitals (std:8). Show the cost consequences, or restate the claims as alignment.

Likewise, "fashion" mixes motive with outcome. Mimetic isomorphism, as cited, is about motive (std:12(d)).

## Minor concerns

- **N (std:6(c)).** 412 × 11 = 4,532, not 4,712, and the lagged peer measure should also drop 2009. Please explain.
- **Marginal effect of modularity (std:6(d)).** It is 0.118 − 0.061u, which reaches zero near u = 1.9 SD. Please report the distribution of u and the covariances.
- **Asset specificity (std:7(b)–(c)).** It is a perceptual, single-informant rating, unvalidated, and it depends on current sourcing.
- **Peer measure.** Please report the number of sample hospitals per state, and explain how states with a single sample hospital are handled.
- **Survival selection.** Under fixed effects, it matters only if attrition tracks changes in modularity or outsourcing. Please report the exclusions and their trends before exit.
- **EHR incentive programme.** Year effects absorb it only if its effects were common across hospitals, and attestation timing varied.
- **P2 intuition (std:16).** The intuition in §2.3 describes the cost saving, not the threshold, and would mislead a non-economist. A3 should be stated in words. On whether the rival is recognisable, I defer to the second reviewer.
- **Priority.** If I recall correctly, Ang and Cummings (1997, *Organization Science*) examined institutional and efficiency influences on IS outsourcing (to verify).
- **Code.** At revision, please supply code that reproduces Table 2.

## What survives

Three things survive: a robust within-hospital association between modularity and outsourcing, in an unusually long panel; a model that, once corrected, may explain the interaction rather than contradict it; and a credible route to identification in the state requirements. Without this paper, we would lose a clear transaction-cost account of how standards shape the boundaries of the firm.

## Recommendation

Major revision. These changes would change my view:
- P2 corrected, with the aggregation step added;
- identification through the state requirements;
- the bad controls removed;
- the claims about the rival reduced to what the design supports, title included.

---

**Checks run** (outside the word count)
- **std:5:** I re-derived P1 by hand (it follows) and P2 by hand (it does not).
- **std:6:** t and stars for all 16 coefficients in Table 2: one discrepancy (Model 3, uncertainty). N checked. Confirmed: the 2.7-point magnitude, "one-sixth of an SD", and the peer coefficient's fall of more than two-thirds. The text matches the table, apart from the H2 omission.
- **std:3(a):** the rival is stated with a citation.
- **std:7:** modularity and the outcome pass: both are factual items from a single informant, with no shared components.
- **std:9:** standard errors are clustered by hospital. That matches modularity (hospital-year) but not the peer measure or the event-study treatment (state-year).
- **std:14(b):** selection into peer groups does not arise, since a hospital's state is fixed.
