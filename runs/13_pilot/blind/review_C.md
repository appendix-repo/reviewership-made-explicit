# Referee report

**Manuscript:** "Modularity, Not Mimicry: Interoperability Standards and the Diffusion of IT Outsourcing in U.S. Hospitals"
**For:** handling editor
**Checks:** no harness was available, so every formal or numerical finding below is marked `asserted`. Section 5 gives the checks that would settle them (chk:1 to chk:3).

## 1. Summary

What the manuscript says:

1. **Question (§1).** Why IT outsourcing spread through U.S. hospitals after 2009. The outsourcing share "roughly doubled" between 2009 and 2019.
2. **Model (§2).** A function with specificity k is bought if and only if k < k*(m,u) = (s+G(u)) / (H(u)(1−m)).
   - ms:Prop1: ∂k*/∂m > 0.
   - ms:Prop2: ∂²k*/∂m∂u > 0.
   - ms:A3: h1/h0 > g1/(s+g0).
3. **Hypotheses (§2.4).**
   - ms:H1: modularity raises the outsourcing share.
   - ms:H2: this effect is stronger when uncertainty is high.
   - ms:H3 (the institutional rival): lagged state-peer outsourcing raises the outsourcing share.
4. **Data and design (§3).**
   - Balanced panel of 412 hospitals, 2009–2019, 4,712 hospital-years.
   - Data come from a CIO survey.
   - Hospital and year fixed effects (FE); standard errors (SEs) clustered by hospital.
5. **Results (ms:T2).**
   - Modularity is positive in Models 2–4 (0.097 to 0.118).
   - The peer coefficient is 0.137 in Model 1 and 0.042 (not significant) in Model 2.
   - The modularity × uncertainty interaction is negative (−0.061, Model 3), contrary to H2.
   - An event study on state interface mandates is described in the text only.
6. **Claimed contributions.**
   - C1: a formal transaction-cost (TCE) model of modularity and the make-or-buy decision.
   - C2: a test against an institutional rival.
   - C3: peer effects "disappear" once modularity is measured.
   - The results are said to "rule out mimetic isomorphism" (Abstract, §5).
   - The study claims to be the first such adjudication (Abstract, §1).

## 2. Major concerns

### cmt:1. "Rules out mimetic isomorphism" is not supported.
**Severity:** fatal for the claim as stated. **Status:** asserted (numbers in a, c).

- **Locus:** Abstract ("The results rule out mimetic isomorphism as a driver"); §5; §6; the decision rule in §2.4; ms:T2.M2.peer.
- **Commitment:** a null peer coefficient, once modularity is controlled, excludes imitation.
- **Problems:**
  - a. **Absence of evidence.** ms:T2.M2.peer = 0.042 (0.038), so the 95% CI is about [−0.032, 0.116].
    - The upper bound is close to the Model 1 estimate (0.137).
    - There is no test of the difference between Models 1 and 2, and no equivalence test.
  - b. **Modularity may carry the peer influence.**
    - §4 (H3) itself credits the peer association to "the common diffusion of standards across hospitals in the same state".
    - Why standards spread within states is not examined.
    - If peers → modularity → outsourcing, controlling for modularity removes the peer path by construction. The §2.4 decision rule ignores this case.
  - c. **Table 2 implies modularity tracks lagged peer outsourcing.**
    - Apply the omitted-variable identity to the change from Model 1 to Model 2.
    - It gives a conditional coefficient of modularity on peer of about (0.137−0.042)/0.112 ≈ 0.85 (chk:3).
  - d. **The event study rests on an institutional pressure.**
    - It uses state mandates for certified interfaces (§4, Robustness).
    - A mandate is coercive isomorphism (DiMaggio & Powell 1983).
    - If a mandate moves outsourcing through modularity, that is an institutional pathway, though not a mimetic one.
  - e. **The test is tilted against H3.**
    - Peer is a lagged leave-one-out mean of the sampled hospitals in the same state (§3.2).
    - 412 hospitals give few hospitals per state: about 8 if spread over 50 states (inferred; the distribution is not reported).
    - States with only one sampled hospital have no peer value.
    - Measurement error biases the peer coefficient toward zero.
    - Modularity, by contrast, is measured in the same year and comes from the same respondent as the outcome.
  - f. **State is a weak proxy for the peer group.**
    - The manuscript itself names the relevant peers as "peers they regard as successful or legitimate" (§1).
    - No peers are defined by system, network, vendor or status.
- **Repair:**
  - Narrow the title, Abstract, §5 and §6 to: no detectable association of lagged state-peer outsourcing once modularity is controlled.
  - Report confidence intervals (CIs) and an equivalence bound.
  - Estimate peer → modularity, with a mediation decomposition.
  - Use other peer groups and a less noisy peer measure (population-wide state data, if available).
  - Test the Tolbert & Zucker (1983) pattern, in which early adopters follow the economics and late adopters follow peers. Interact the modularity and peer effects with adoption timing.

### cmt:2. Proposition 2 is false under Assumption A3.
**Severity:** damaging. **Status:** asserted (chk:1).

- **Locus:** ms:Prop2; ms:A3; ms:App.Prop2.
- **Commitment:** ∂²k*/∂m∂u > 0, with a proof in the Appendix.
- **Problem:** the proof treats H(u) as constant ("Modularity operates on the denominator of k* only through the factor (1−m)"). But H(u) = h0 + h1·u also depends on u.
  - The correct cross-partial is ∂²k*/∂m∂u = [g1·h0 − h1·(s+g0)] / [H(u)²(1−m)²]. The u terms cancel.
  - A3 is equivalent to g1·h0 − h1·(s+g0) < 0, so under A3 the cross-partial is negative for every m and u.
  - Example: s = g0 = g1 = h0 = h1 = 1, u = 0, m = 0.5 satisfies A3 and gives −4.
- **The general reason:**
  - Since k* = A(u)/(1−m), the cross-partial ∂²k*/∂m∂u always has the same sign as ∂k*/∂u.
  - A3 encodes Williamson's (1991) premise that uncertainty favours making. Under that premise, the effect of modularity on k* falls as uncertainty rises.
  - So Prop 2 holds if and only if A3 fails.
- **The §2.3 intuition describes a different quantity.** It holds for the cost advantage of buying, not for the threshold: ∂²(C_M − C_B)/∂m∂u = h1·k > 0.
- **Consequences:**
  - H2 was derived from an error.
  - The corrected model predicts the negative interaction in ms:T2.M3.mxu (−0.061).
  - The corrected model also predicts ∂k*/∂u < 0, but ms:T2.M3.uncertainty is +0.084 (not significant; see cmt:10).
- **Repair:**
  - Correct Prop 2 and its proof, and state the sign condition for the cross-partial.
  - If H2 is reversed, say plainly that the reversal comes from correcting the derivation after the result was seen.
  - Present the interaction as consistent with the model, not as a confirmed prediction of it.
  - Remove the §5 legitimacy explanation (cmt:7).

### cmt:3. The mechanism through specificity is not shown, and Table 2 fits it poorly.
**Severity:** damaging. **Status:** asserted (chk:3; how I read the measure is my inference).

- **Locus:** §3.2 (definition of asset specificity); ms:T2.*.spec; §5 ("reduced the effective specificity of hospital–vendor relationships").
- **Commitment:** modularity raises outsourcing by lowering effective specificity, k(1−m).
- **Problems:**
  - a. **The specificity measure is the mediator.** It asks "how costly it would be to transfer the hospital's IT functions to a different provider". That matches effective specificity, k(1−m), which is the mediator (inference).
  - b. **No link is reported.** There is no estimate of the effect of modularity on specificity.
  - c. **The link Table 2 implies is near zero.**
    - Adding modularity moves the specificity coefficient only from −0.094 to −0.091.
    - The implied conditional coefficient of modularity on specificity is −0.003/0.112 ≈ −0.03 (chk:3). Within hospitals, this is close to zero.
    - The mechanism predicts a clear negative association.
  - d. **The modularity coefficient does not shrink.**
    - If modularity works through specificity, its coefficient should shrink toward zero once specificity is controlled. It stays at 0.11–0.12.
    - So either modularity acts through another channel, which the model does not allow, or the measure does not capture specificity.
  - e. **Specificity is likely a consequence of outsourcing.** Outsourced functions create vendor lock-in, which raises transfer costs.
- **Repair:**
  - Report the regression of specificity on modularity.
  - Run a mediation analysis that states when the mediator is measured.
  - Use function-level data to test the threshold structure directly: lower-k functions should be outsourced first, and the threshold should move with m. These data exist: specificity is "averaged over functions" (§3.2).

### cmt:4. The causal identification of the modularity effect is weak.
**Severity:** damaging. **Status:** asserted.

- **Locus:** §3.3 ("Identification therefore comes from within-hospital changes in modularity over time"); §4, Robustness (event study).
- **Commitment:** changes in modularity within a hospital cause changes in outsourcing. The event study is "consistent with a causal effect of modularity".
- **Problems:**
  - a. **Reverse causality.** Vendors that take over functions may install certified interfaces. m is measured in the same year as Φ.
  - b. **Common-method variance.** Φ, m and specificity all come from the same CIO survey (§3.1, §3.2).
  - c. **The event study is incomplete:**
    - No estimates, figure or table are reported.
    - It is only a reduced form of mandates on Φ. There is no first stage (mandate → m).
    - The exclusion restriction is not argued. Hospitals may contract out the compliance work itself.
    - Two-way FE with leads and lags under staggered adoption is biased when effects differ by timing (Goodman-Bacon 2021; Sun & Abraham 2021; Callaway & Sant'Anna 2021).
    - The control group (never treated or not yet treated) is not stated.
    - The sources and dates of the mandates are not documented.
  - d. **Year FE may not absorb the EHR incentive programme.** Year FE absorb the 2009 federal EHR incentive only if its effect is the same for all hospitals (§3.3). The effect plausibly varies with how far a hospital had already adopted EHRs.
- **Repair:**
  - Use lagged m.
  - Estimate a first stage and two-stage least squares with the mandates.
  - Use an event-study estimator robust to timing heterogeneity, and plot all coefficients.
  - Cluster SEs by state for the state-level treatment.
  - Take the outcome from a source other than the CIO, e.g. hospital cost reports, if they record contracted IT spending (to verify).
  - Control for baseline EHR status × year.

### cmt:5. The design does not answer the stated question.
**Severity:** damaging. **Status:** asserted.

- **Locus:** §1 ("Why did outsourcing ... spread so rapidly"); Abstract; year FE in §3.3; §6 ("Its substance is economizing").
- **Commitment:** modularity explains the decade-long spread of outsourcing.
- **Problem:** year FE absorb the common national rise, so β1 is estimated only from deviations around that rise.
- **Magnitude:**
  - β1 = 0.112, so even a full 0→1 change in modularity raises Φ by only 11.2 percentage points.
  - A doubling consistent with a mean Φ of 0.31 is about 20 points (inferred: a linear rise from about 0.21 to about 0.41; the actual series is not reported).
  - No yearly series of Φ or m is shown.
- **Repair:**
  - Report the yearly means of Φ and m.
  - Compare the actual aggregate change in Φ with the change predicted by Δm × β1.
  - Compare the path of the year effects with and without m.
  - Restate the conclusions as the share of the spread that modularity accounts for.

### cmt:6. Model 4 controls for an outcome of outsourcing.
**Severity:** fixable. **Status:** asserted.

- **Locus:** §3.2 ("Because outsourcing a function transfers its staff to the vendor or eliminates the positions"); §3.3 ("it cannot be attributed to capability differences"); ms:T2.M4.
- **Commitment:** because β1 survives a control for staffing, capability differences cannot explain it.
- **Problem:**
  - By the manuscript's own statement, outsourcing mechanically reduces staffing, so staffing is a consequence of the outcome.
  - Controlling for it neither removes capability confounding nor leaves β1 unbiased.
  - The staffing coefficient (−0.143) and the rise in within R² (0.14 → 0.19) are what that mechanical link predicts.
- **Repair:**
  - Drop the claim.
  - Use pre-period staffing (baseline × year), or capability measures that outsourcing does not determine.

### cmt:7. The Discussion explains the H2 result with an institutional mechanism.
**Severity:** fixable. **Status:** n/a (textual).

- **Locus:** §5, paragraph 2 ("hospitals face legitimacy pressures to retain in-house functions"; "This interpretation is consistent with our theory").
- **Incompatibility:**
  - Legitimacy pressure is an institutional mechanism, and it is not in the model.
  - Using it to explain a main result contradicts the claim in the Abstract and §6 that the practice is economizing rather than institutional fashion.
  - It is untested and, given cmt:2, unnecessary.
- **Repair:** delete it. Alternatively, test it (e.g. by ownership or board composition) and withdraw the "rule out" language.

### cmt:8. The reported N does not match the stated design.
**Severity:** fixable. **Status:** asserted (chk:2).

- **Locus:** §3.1 ("balanced panel of 412 ... from 2009 to 2019"; "4,712 hospital-year observations"); Observations row of ms:T2.
- **Problems:**
  - 412 × 11 = 4,532, not 4,712, and 4,712/412 is not a whole number.
  - Peer(t−1) for 2009 needs 2008 survey data. If the survey starts in 2009, the estimation sample is at most 412 × 10 = 4,120.
  - The 2009 uncertainty measure needs admissions data for 2006–2008.
- **Repair:** state how the sample was actually built and which years it covers, and reconcile the counts in every model.

### cmt:9. The modularity measure does not cover the same functions as the outcome.
**Severity:** fixable. **Status:** n/a.

- **Locus:** §3.2 (m is the share of "clinical information systems" on certified interfaces); §2.1 (the functions include "infrastructure hosting, help-desk support, revenue-cycle systems").
- **Problem:** clinical interface standards bear on clinical-application functions. They do not obviously bear on hosting or help desk, yet Φ pools all of these.
- **Repair:**
  - Split Φ by function type.
  - Use non-clinical functions as a placebo: m should not predict their outsourcing, unless the authors explain why it should.

## 3. Minor concerns

- **cmt:10. Wrong significance stars.** Fixable; asserted.
  - ms:T2.M3.uncertainty = 0.084 (0.051) gives t ≈ 1.65 and p ≈ 0.10, but it is reported with ***.
  - Model 4's 0.079 (0.050) is correctly left unstarred. All other stars match (chk:2).
- **cmt:11. H2 does not follow from Prop 2 alone.** Fixable; asserted.
  - Φ = F(k*), where F is the spending-weighted distribution of k across functions.
  - ∂²Φ/∂m∂u = f(k*)·∂²k*/∂m∂u + f′(k*)·(∂k*/∂m)(∂k*/∂u), so the sign depends on f′.
  - Φ = 1 once k* ≥ 1, and k* is unbounded as m → 1.
  - State an assumption about the distribution of k, or test at the function level.
- **cmt:12. The uncertainty measure does not match the theory.** Fixable.
  - The coefficient of variation of quarterly admissions (§3.2) measures demand volatility.
  - In the model, u is the frequency of unanticipated adaptations in the IT relationship (§2.2).
  - For the institutional rival, uncertainty concerns the merits of a practice (§2.4).
  - Justify the measure or add IT-specific measures.
- **cmt:13. Priority claim and missing literature.** Fixable.
  - The manuscript claims to be the "first study to adjudicate directly" (Abstract, §1).
  - The IS outsourcing literature has already tested imitation against economic explanations:
    - Loh & Venkatraman (1992), *Information Systems Research*, "Kodak effect" (to verify).
    - Ang & Cummings (1997), *Organization Science* (to verify).
    - Ang & Straub (1998), *MIS Quarterly* (to verify).
  - On modularity and firm boundaries: Hoetker (2006), *Strategic Management Journal* (to verify).
  - Engage with this work or drop the priority claim.
- **cmt:14. H2's failure is not reported up front.** Minor. The Abstract and Conclusion state the model's H2 prediction but not that H2 failed. Report it.
- **cmt:15. "Strongly predicts" overstates the effect.** Minor.
  - The effect is one-sixth of an SD: 2.7 percentage points per SD of modularity. The arithmetic is correct (chk:2).
  - The SD used (0.24) is pooled, but identification is within hospitals.
  - Report the within-hospital SD of m and the effect per within-hospital SD.
- **cmt:16. Robustness results are given without numbers (§4).** Fixable. This covers the licence-inclusive Φ, the non-system subsample and the event study. Report them.
- **cmt:17. Clustering by hospital is likely too narrow.** Fixable.
  - Peer varies at the state-year level, and mandates at the state level. Hospitals in the same system may share IT decisions.
  - Clustering by hospital alone likely understates the SEs of these regressors.
  - Cluster by state, and check clustering by system.
- **cmt:18. Survey and sample.** Fixable.
  - Name the survey's sponsor, sampling frame and response rates. Validate the CIO-reported spending shares.
  - Requiring a response in every year selects hospitals that survived and kept responding. §5.2 notes only the bias toward larger hospitals.
  - Compare included and excluded hospitals on observables, and check sensitivity with an unbalanced panel.
- **cmt:19. Notation and model details.** Minor.
  - The equation writes Peer_{s,t−1}, but the text defines a leave-one-out mean, which varies by hospital.
  - The model restricts m to [0,1), but measured m can equal 1.
  - A3 is described as a comparison "in proportional terms", yet its right side divides g1 by s+g0. State that A3 is equivalent to ∂k*/∂u < 0.
- **cmt:20. Practice advice goes beyond the evidence.** Minor. §5.1 advises leaders to "attend first to the modularity of their systems", but this rests on observational estimates. Qualify it.

## 4. Recommendation

**Major revision.**

Rationale:

1. The setting, the panel and the H1 association are of interest. The H1 coefficient is stable across Models 2–4.
2. The title claim and "rule out mimetic isomorphism" (cmt:1) do not stand on this evidence. The authors must either narrow the claim or run new analyses (mediation, other peer groups, more precision).
3. Prop 2 is wrong (cmt:2). The corrected version fits the data, but it turns H2 into a revision made after the result, which must be disclosed.
4. The mechanism (cmt:3) and identification (cmt:4, cmt:5) need analyses that the authors appear able to run with their existing data (function-level records, state mandates).
5. If the revision supports only "no detectable state-peer association once modularity is controlled", the contribution may fall below the bar. In that case, reject at that stage.

## 5. Checks (not run; for the harness)

**chk:1. Prop 2 (cmt:2).**
```python
import sympy as sp
s,g0,g1,h0,h1,u,k = sp.symbols('s g0 g1 h0 h1 u k', positive=True)
m = sp.symbols('m')
G, H = g0+g1*u, h0+h1*u
kstar = (s+G)/(H*(1-m))
cross = sp.diff(kstar, m, u)
print(sp.simplify(cross*H**2*(1-m)**2 - (g1*h0 - h1*(s+g0))))        # expect 0
print(sp.simplify(cross - sp.diff(kstar, u)/(1-m)))                   # expect 0: sign = sign of dk*/du
print(sp.simplify(cross - g1/(H*(1-m)**2)))                           # manuscript's expression; expect nonzero
print(cross.subs({s:1,g0:1,g1:1,h0:1,h1:1,u:0,m:sp.Rational(1,2)}))   # A3 holds (1 > 1/2); expect -4
adv = (s+G) - H*k*(1-m)                                               # C_M - C_B
print(sp.diff(adv, m, u))                                             # expect h1*k (> 0)
```

**chk:2. Table 2 arithmetic (cmt:1a, cmt:5, cmt:8, cmt:10, cmt:15).**
```python
from scipy import stats
T = {'M1.peer':(.137,.031,3),'M2.peer':(.042,.038,0),'M3.peer':(.039,.037,0),'M4.peer':(.036,.036,0),
     'M2.mod':(.112,.024,3),'M3.mod':(.118,.025,3),'M4.mod':(.097,.023,3),
     'M3.unc':(.084,.051,3),'M4.unc':(.079,.050,0),'M3.mxu':(-.061,.019,2),'M4.mxu':(-.058,.019,2),
     'M1.spec':(-.094,.027,3),'M2.spec':(-.091,.027,3),'M3.spec':(-.090,.026,3),'M4.spec':(-.088,.026,3),
     'M4.staff':(-.143,.029,3)}
for key,(b,se,st) in T.items():
    p = 2*stats.t.sf(abs(b/se), df=411)
    imp = 3 if p<.001 else 2 if p<.01 else 1 if p<.05 else 0
    print(key, round(b/se,2), round(p,4), 'reported', st, 'implied', imp, '' if st==imp else 'MISMATCH')
print(412*11, 412*10, 4712/412)          # expect 4532, 4120, non-integer
print(.112*.24, .112*.24/.17)            # expect ~0.027, ~0.16
print(.042-1.96*.038, .042+1.96*.038)    # expect ~(-0.032, 0.116)
print((.137-.042)/.137)                  # expect ~0.69
print(.112*1.0)                          # max contribution of m, 0 -> 1
```
Expected result: the only mismatch is M3.unc.

**chk:3. Omitted-variable identity on Table 2 (cmt:1c, cmt:3c).** For OLS on the same sample, b_short = b_long + β_m·δ, where δ is the coefficient from regressing m on the included regressors (including FE and controls). This assumes Models 1 and 2 share the sample and controls; the reported N is the same.
```python
b_m = .112
print((.137 - .042)/b_m)                 # d_peer, expect ~0.85
print((-.094 - -.091)/b_m)               # d_spec, expect ~-0.027
print(-.004/.1115, -.002/.1125)          # bounds on d_spec under 3-decimal rounding: ~[-0.036, -0.018]
```
A definitive check needs the authors' data: regress m_it on Peer, specificity, the controls and both sets of FE.

## 6. Decisions for the reviewer

1. **cmt:1 severity.** Keep `fatal` (the claim as worded), or downgrade to `damaging` (the claim can be narrowed).
2. **cmt:2.** Allow H2 to be reversed in the revision with disclosure, or require it to be reported as an unpredicted result.
3. **cmt:1c and cmt:3c.** These rely on Table 2's rounded coefficients and on my reading of the specificity item as effective specificity. Include them, soften them, or drop them.
4. **cmt:13.** Verify the four citations marked (to verify) before sending.
5. **Recommendation.** Major revision (mine) or reject.
6. **Data and code.** Decide whether to request them, so that chk:1 to chk:3 can be run and the findings moved beyond `asserted`.
7. **cmt:8.** Send it to the authors as a reporting question, or flag it to the editor as a possible data-integrity issue.
