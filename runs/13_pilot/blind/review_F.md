# Referee report: draft for the reviewer to adopt

**Manuscript:** "Modularity, Not Mimicry: Interoperability Standards and the Diffusion of IT Outsourcing in U.S. Hospitals" (`ms`)
**Task:** T5, single-pass review, style S1. No harness was available, so I could not have any check run. Every formal or numerical finding below is therefore `asserted`. The checks that would settle each one are in Annex A.
**Addressed to:** the handling editor, through the human reviewer, who decides on and signs every point.

---

## To the editor: summary assessment

This paper asks a good question. It is built on an idea worth having: asset specificity is partly a product of interface design, and therefore of standards that no single firm controls. It is not yet a sound paper.

- **The second proposition is wrong.** It is mis-derived. Solved correctly under the authors' own assumption, the model predicts the negative interaction that the paper reports as an anomaly and then explains away.
- **The "rules out" verdict is untested.** The headline claim that the evidence "rules out" mimetic isomorphism rests on a test that an institutional account would pass as easily as a transaction-cost account.
- **Cause and mechanism are not shown.** The modularity effect is not causally identified, and the claimed mechanism, which runs through specificity, is not demonstrated.
- **The design cannot see the diffusion.** The two-way fixed-effects design removes the aggregate rise in outsourcing that the paper sets out to explain.
- **The sample does not add up.** The reported observation count cannot be reconciled with the stated sample.

I recommend **major revision**. The condition is explicit: the title, abstract and conclusion must either gain a design that can tell the two accounts apart, or drop the claim to have adjudicated between them.

---

## 1. Summary of the paper and its claimed contributions

**Question.** The manuscript asks why outsourcing of IT functions spread through U.S. hospitals after 2009 (§1).

**Model.** It sets a mimetic-isomorphism account against a transaction-cost model:

- Certified interoperability standards make IT functions modular.
- Modularity reduces the effective specificity of a function from $k$ to $k(1-m)$ (§2.2).
- This raises the specificity threshold $k^*(m,u)$ below which a function is bought rather than made (§2.3).

**Propositions and hypotheses.**

- `ms:Prop1`: modularity raises the threshold.
- `ms:Prop2`: this effect increases with environmental uncertainty.
- `ms:H1` and `ms:H2` translate the two propositions into hypotheses about the share of IT spending that is outsourced.
- `ms:H3` states the institutional rival: outsourcing follows peers' prior outsourcing (§2.4).

**Data and estimates.** The data are a balanced panel of 412 general acute-care hospitals, 2009–2019, estimated with hospital and year fixed effects (§3). Table 2 (`ms:T2`) reports:

- **Modularity:** a positive coefficient in every model (0.097 to 0.118).
- **Peer outsourcing:** the coefficient on lagged same-state peer outsourcing falls from 0.137 to 0.042 and loses significance once modularity is added (`ms:T2.M1.peer`, `ms:T2.M2.peer`).
- **Interaction:** modularity × uncertainty is negative (−0.061, `ms:T2.M3.mxu`), which the authors call "contrary to H2". They explain it by legitimacy pressures (§5, ¶2).

**Claimed contributions** (§1 ¶3; §5.1):

1. A formal link between modularity and the make-or-buy decision.
2. A test of the model against an institutional rival.
3. A demonstration that apparent peer effects disappear once modularity is measured. The abstract escalates this to "The results rule out mimetic isomorphism as a driver of IT outsourcing in this setting".
4. A priority claim: "the first study to adjudicate directly" between the two explanations (abstract; §1).

## 2. Overall assessment

**Strengths, rated on their merits:**

- The question matters, and the setting is well chosen.
- The conceptual move in §5.1 is genuine and portable: specificity is "partly a product of interface design". It gives transaction-cost theory a way to make specificity a variable of technology policy rather than a fixed attribute of an activity.
- The model is transparent, and `ms:Prop1` is correctly proved.
- The decade-long hospital panel is a real asset.
- The staggered state requirements for certified interfaces (§4, Robustness) are potentially the paper's strongest source of identification. At present they are confined to one sentence.

**Weaknesses.** Against these strengths, each headline claim outruns its evidence. The concerns below are numbered, give the locus for each claim, and are graded on the workbench severity scale.

---

## 3. Major concerns

### cmt:1. Proposition 2 is false under the manuscript's own Assumption A3. [damaging; `asserted`, check K1]

**What the manuscript commits to.** `ms:Prop2` states $\partial^2 k^*/\partial m\,\partial u > 0$. The Appendix obtains $g_1/[H(u)(1-m)^2]$, reasoning that "the cross-partial is determined by how the numerator responds to uncertainty".

**The error.** The denominator also depends on $u$: $H(u) = h_0 + h_1 u$ (§2.2). The proof drops $H'(u)$.

Note that $\partial k^*/\partial m = k^*/(1-m)$, which is `ms:Prop1` and is correct. Differentiating correctly then gives

$$\frac{\partial^2 k^*}{\partial m\,\partial u} = \frac{g_1 h_0 - h_1 (s+g_0)}{H(u)^2 (1-m)^2}.$$

The sign of this expression is the sign of $g_1 h_0 - h_1(s+g_0)$, whatever the values of $m$ and $u$. Assumption A3 ($h_1/h_0 > g_1/(s+g_0)$) is exactly the condition that makes it negative.

A3 is stated in §2.2 but used in neither proof. Its only work in the model is to fix the sign of the cross-partial, and of $\partial k^*/\partial u$, as negative. Two further oddities point the same way:

- A3 is described as a comparison of proportional responsiveness. Yet its right-hand side divides by $s+g_0$, and $s$ is a production-cost advantage, not an adaptation cost.
- A3 is the only numbered assumption; there is no A1 or A2.

**Consequences.**

- (a) `ms:H2` as stated is not implied by the model. The model, correctly solved, implies the reverse.
- (b) The negative interaction in `ms:T2.M3` (−0.061, SE 0.019) and `ms:T2.M4` (−0.058, SE 0.019) is what the model predicts. The statement "contrary to H2" (§4) is itself the error.
- (c) The legitimacy-signalling account in §5 ¶2 explains an anomaly that does not exist. It is not harmless: it brings an institutional mechanism into a paper whose verdict is that institutional mechanisms are ruled out (see cmt:2(d)).
- (d) The intuition in §2.3 conflates two different effects of modularity:
  - its effect on the cost saving for a given function, $\partial (C_M - C_B)/\partial m = H(u)k$, which does rise with $u$;
  - its effect on the threshold, which scales with $k^*$ and shrinks as uncertainty raises $H$.

  Only the second governs the range of functions outsourced.
- (e) Under A3 the model also implies a negative main effect of uncertainty. This does not sit well with the positive, if imprecise, point estimates in `ms:T2.M3.uncertainty` (0.084) and `ms:T2.M4.uncertainty` (0.079). Because $m$ is not centred, $\beta_2$ is the effect of uncertainty at $m=0$. At the sample mean $m = 0.46$, the implied effect is $0.084 - 0.061 \times 0.46 \approx 0.056$, still positive (check K5).

**Repair.**

- Correct the proof and `ms:Prop2`.
- Restate H2 with a negative sign and give the correct intuition.
- Remove the legitimacy explanation, or recast it as an untested alternative.
- Address the sign of the uncertainty main effect.
- Say plainly that the corrected H2 is being stated after the estimate was seen, while noting that it follows from an assumption the manuscript had already stated.

The correction favours the authors' model. That is a reason to make it, not a reason to pass over it.

### cmt:2. The design cannot "rule out" mimetic isomorphism. [fatal to the "Not Mimicry" claim as stated; numerical sub-points `asserted`, checks K2 and K3]

**What the manuscript commits to.** The claim appears throughout:

- the title;
- the abstract ("rule out mimetic isomorphism");
- §1, contribution 3;
- §4, on H3: the pattern is "exactly what the transaction-cost account predicts and the institutional account does not";
- §5 ¶1;
- §6: "Its substance is economizing."

**What is missing.** The evidence is that the peer coefficient falls from 0.137 (SE 0.031) to 0.042 (SE 0.038) when modularity is added. That supports "rule out" only if an institutional account predicts that peer outsourcing would survive conditioning on modularity. It does not, for four reasons.

**(a) Modularity may lie on the path of institutional diffusion, or stand in for the outcome.** By the OLS omitted-variable identity (same sample, same fixed effects, same controls), the fall in the peer coefficient equals $\beta_{m} \times \delta_{\text{peer}}$. Here $\delta_{\text{peer}}$ is the coefficient on lagged peer outsourcing in an auxiliary regression of modularity on the Model 1 regressors. Table 2 implies $\delta_{\text{peer}} \approx (0.137-0.042)/0.112 \approx 0.85$ (K3).

What Table 2 actually shows, then, is that lagged state-peer outsourcing strongly predicts a hospital's own modularity, within hospitals. That pattern is produced by at least three structures:

1. Standards diffuse across hospitals in a state for reasons common to all of them. This is the authors' reading (§4, H3). They assert it but do not show it.
2. Hospitals adopt certified interfaces because their peers have outsourced, or because the state requires it. Diffusion of the enabling technology by imitation, or by mandate, is precisely what DiMaggio and Powell (1983) call mimetic and coercive isomorphism. The state interface requirements the authors use in §4 are, on their face, coercive isomorphism.
3. A hospital's own outsourcing raises its measured modularity: a vendor that takes over a clinical application may connect it through certified interfaces. This is my inference; the manuscript is silent on it. Own outsourcing also co-moves with peers' outsourcing through common state shocks. On this structure modularity partly proxies the dependent variable, and conditioning on it mechanically absorbs any peer effect.

Under structures 2 and 3, an institutional account predicts the Model 2 pattern. The pattern therefore does not discriminate between the accounts. The conditional test in §2.4 ¶4 states a necessary condition for an economizing-only account and treats it as sufficient to exclude imitation.

**(b) A non-significant coefficient is not evidence of absence.**

- The 95% confidence interval for the Model 2 peer coefficient is about [−0.03, 0.12] (K2).
- Its upper end is roughly 85% of the Model 1 point estimate, so the data cannot reject a peer effect close to the one the authors set out to explain away.
- No test of the change in the peer coefficient is reported. The difference between "significant" and "not significant" is not itself significant (Gelman & Stern, 2006).

**(c) The institutional rival is operationalized weakly, in ways that favour rejecting it.**

- *Noisy proxy.* Peer outsourcing is the mean over "all other sample hospitals in the same state" (§3.2). With 412 hospitals spread across the states, that is about eight per state on average, fewer in some states. They come from a non-random subset of hospitals that answered the survey every year. This is a noisy proxy for the organizational field, and measurement error attenuates $\beta_4$ toward zero.
- *Undefined cases.* How hospitals in states with a single sample hospital are handled is not stated.
- *National field removed.* Year fixed effects absorb imitation at the level of the national field. Only state-specific deviations from the national trend are tested.
- *Sharper predictions untested.* The theories the manuscript cites have sharper implications that it does not test:
  - DiMaggio and Powell's proposition that imitation intensifies under uncertainty, which calls for a Peer × uncertainty term;
  - imitation of successful, high-status or tie-connected peers. Westphal, Gulati and Shortell (1997), cited in §1, work through network ties; see also Haveman (1993) (to verify). System peers are an obvious reference group, and system membership is already among the controls;
  - the two-stage pattern of Tolbert and Zucker (1983), also cited in §1: early adopters respond to technical attributes, late adopters to prevalence. This implies that the modularity effect should weaken, and the peer effect strengthen, as adoption proceeds.
- *Unaddressed inference problems.* Lagging the peer variable does not solve the problem of correlated effects (Manski, 1993; to verify). Errors clustered only by hospital probably understate the standard errors on this state-level regressor in every model (cmt:10).

**(d) The manuscript contradicts itself.** §5 ¶2 explains the interaction by "legitimacy pressures to retain in-house functions that would otherwise be outsourced". It then adds: "This interpretation is consistent with our theory". On any standard reading, legitimacy pressure is an institutional mechanism, and the formal model contains no such term. The manuscript cannot both rule out institutional drivers of IT sourcing (abstract; §5 ¶1) and use one to explain its own estimates. cmt:1 removes the need for that move. The fact that the authors made it shows how little their design constrains institutional explanations.

**(e) A binary contest is assumed, not argued.** The two accounts are not mutually exclusive. Treating the question as a contest with one winner is a framing choice that the manuscript never defends.

**Repair.** The authors have two options.

*Option 1: a design that tells the accounts apart.* For example:

- use the state requirements to instrument modularity, then test whether peer outsourcing predicts outsourcing given instrumented modularity;
- add the Peer × uncertainty test;
- use peer sets weighted by status, system or ties;
- test the Tolbert–Zucker staging;
- test whether peers' outsourcing predicts a hospital's own modularity before any state requirement was in force.

*Option 2: withdraw the claim.* Drop "rule out", "Not Mimicry" and the priority claim, and reframe the result: state-level peer associations do not survive the addition of measured modularity, a pattern consistent both with economizing and with institutional diffusion that runs through standards.

Without Option 1, the title cannot stand.

### cmt:3. The modularity effect is not causally identified. [damaging]

**What the manuscript commits to.**

- §3.3: "Identification therefore comes from within-hospital changes in modularity over time."
- §4: the event study is "consistent with a causal effect of modularity".
- §5 and §6 use causal language throughout ("By making IT functions modular, interoperability standards lowered the specificity…").

**What is missing.** Hospital fixed effects remove only confounders that do not change over time. Four threats remain.

**(a) Reverse causality.** Modularity and the outcome are measured in the same year ($m_{it}$, $\Phi_{it}$). Outsourcing a clinical application may itself convert its interfaces to certified ones, as in cmt:2(a), structure 3. The model treats $m$ as a parameter, but in practice hospitals choose $m$, quite possibly together with their sourcing plans.

**(b) Common source.** Modularity and outsourcing are both reported by the same CIO in the same survey (§3.1, §3.2). CIO turnover, or a change in how a CIO reports, would shift both.

**(c) Changes in internal capability.** The authors name this threat (§3.3). The Model 4 control does not address it (cmt:6).

**(d) The event study.** Four problems:

- *It is a reduced form.* The design estimates the effect of state requirements on outsourcing. To support "a causal effect of modularity", it needs a first stage (requirement → modularity) and an exclusion restriction (the requirement affects outsourcing only through modularity).
- *The exclusion restriction is doubtful.* A mandate to certify interfaces creates a compliance task. A hospital without in-house integration skills may buy that work from vendors, which would raise outsourcing through capability or production costs rather than through reduced hold-up. Concurrent state health-IT policies would also have to be ruled out.
- *It is not reported.* The manuscript gives no coefficients, no confidence intervals, and no counts of treated and never-treated states.
- *The estimator is suspect.* Two-way fixed-effects event studies with staggered adoption and heterogeneous effects are biased and can contaminate the leads (Sun & Abraham, 2021; Callaway & Sant'Anna, 2021; Goodman-Bacon, 2021; de Chaisemartin & D'Haultfœuille, 2020). Insignificant leads are weak evidence of parallel trends when pre-tests have little power (Roth, 2022; to verify).

**Repair.**

- Report the event study with an estimator robust to heterogeneous effects.
- Report the first stage and a 2SLS estimate that uses the state requirement as an instrument for modularity, with the first-stage F statistic and inference clustered by state.
- Defend the exclusion restriction, and test the compliance-capability channel. Is the outsourcing response concentrated in integration and interface services, or in functions whose nominal specificity modularity should reduce?
- Add timing tests at the function level: does certification of a function's interfaces come before its outsourcing, or after?
- Use lagged modularity, and control for changes of CIO.

### cmt:4. Year fixed effects remove the diffusion the paper sets out to explain, the estimated effects are small relative to it, and "economizing" is not evidenced. [damaging; magnitudes `asserted`, check K4]

**What the manuscript commits to.**

- The abstract opens: "Why did outsourcing … spread so rapidly…?"
- §1 says the vendor share "roughly doubled".
- §6: "The spread of IT outsourcing … has the outward form of an institutional fashion. Its substance is economizing."

**What is missing.**

**The design cannot see the diffusion.** With year fixed effects, the common movement in $\Phi$, which is the national diffusion itself, is absorbed by $\tau_t$. §3.3 concedes this for the 2009 federal incentive programme. $\beta_1$ is identified only from hospital-specific deviations from the national trend. Nothing in Table 2 says how much of the aggregate rise modularity accounts for.

**The magnitudes suggest not much.**

- Model 2 implies that a one-standard-deviation rise in modularity raises the outsourcing share by 2.7 points (§4; confirmed in K4).
- Even if mean modularity had risen from 0 to 1 over the decade, $\beta_1 = 0.112$ implies a rise of only 11 points.
- Suppose the sample tracks the national doubling described in §1. With a decade mean of 0.31 and linear growth, the share would have gone from about 0.21 to about 0.41, a rise of roughly 20 points. This is my inference; the manuscript does not report means by year.
- On that inference, modularity accounts for at most about half the rise. For any plausible rise in mean modularity (I use 0.2 to 0.5; the actual figure is not reported), it accounts for roughly 2 to 6 points, about a tenth to a quarter.

The remainder sits in the year effects. Those are compatible with any national mechanism: imitation across the national field, the federal incentive programme, vendor consolidation and marketing, or the shift to vendor-hosted software. Within R² rises only from 0.08 to 0.13 when modularity enters (`ms:T2`).

**"Economizing" has not been shown.** In transaction-cost economics, "economizing" is a claim about alignment and performance: governance matched to the attributes of the transaction saves costs (Williamson, 1991). The manuscript shows that sourcing moves with modularity. It shows nothing about costs or performance. A practice can move with a technical attribute and still be adopted for reasons that do not economize.

**Repair.**

- Report sample means of $\Phi$ and $m$ by year.
- Decompose the aggregate change into $\hat\beta_1\Delta\bar m$ and a residual.
- Plot the year-effect profiles from Models 1 and 2. If modularity explains the diffusion, the profile should flatten.
- Moderate the abstract and §6.
- If feasible, test discriminating alignment: do hospitals whose sourcing departs from the model's threshold have higher IT costs per bed?

### cmt:5. The mechanism (modularity lowers effective specificity, which raises outsourcing) is not shown, and Table 2 is in tension with it. [damaging; numerical sub-point `asserted`, check K3]

**What the manuscript commits to.** In §2.2, modularity enters the buy/make decision only through effective specificity, $k(1-m)$. §5 says that standards "reduced the effective specificity of hospital–vendor relationships".

**What is missing.**

**(a) It is unclear what the specificity measure measures.** The asset-specificity variable is the CIO's rating of "how costly it would be to transfer the hospital's IT functions to a different provider" (§3.2).

- The most natural reading is *effective* specificity, the very quantity modularity is supposed to reduce. On that reading, controlling for it controls for the mechanism. In the model, once effective specificity is fixed, $m$ has no further effect. A large and stable modularity coefficient conditional on the measure (Models 2–4) would then be evidence that modularity works through some other channel.
- If the measure is meant to capture *nominal* $k$, the manuscript must say so. It must also explain why nominal specificity varies within a hospital over time, since within-hospital variation is the only variation used.
- The question also measures different things for different functions. For a function already outsourced it asks about switching vendors; for one kept in-house it asks about outsourcing. The measure may therefore be endogenous to $\Phi$.

**(b) The auxiliary association is weak.**

- The specificity coefficient barely moves when modularity enters, from −0.094 to −0.091. By the identity used in cmt:2(a), $\delta_{\text{spec}} \approx -0.003/0.112 \approx -0.03$; allowing for rounding, the range is about −0.04 to −0.02 (K3).
- Conditional on fixed effects, controls and peer outsourcing, moving across the entire specificity scale is therefore associated with a change in modularity of about 0.03, roughly an eighth of modularity's pooled standard deviation (0.24).
- Without within-hospital standard deviations this cannot be converted into a correlation. Even so, it is hard to reconcile with a mechanism in which modularity is what drives specificity down.

**(c) Modularity and outsourcing are measured over different scopes.**

- Modularity covers *clinical* information systems (§3.2).
- The outsourcing share covers all IT functions, including infrastructure hosting and help-desk support (§2.1). Clinical interface standards plausibly do not touch the specificity of those functions.
- The model works function by function, and the survey appears to collect function-level data: specificity is "averaged over functions" (§3.2).

The natural test, which doubles as a falsification test, is therefore at the function level. Modularity should raise outsourcing of clinical-application functions and of functions with intermediate nominal $k$. It should leave hosting and help desk essentially unaffected.

**Repair.**

- State clearly what the specificity measure captures.
- Report the within-hospital regression of specificity on modularity.
- Estimate mediation explicitly, with the usual caveats.
- Add the function-level analysis, using hosting and help desk as placebo functions.

### cmt:6. In-house IT staffing (Model 4) is a post-treatment control, and the conclusion drawn from it does not follow. [fixable]

**What the manuscript commits to.** §3.3: "If the modularity effect survives this control, it cannot be attributed to capability differences." The robustness paragraph in §4 repeats the claim.

**Where it contradicts itself.** §3.2 states that "outsourcing a function transfers its staff to the vendor or eliminates the positions". In-house staffing is therefore partly a mechanical outcome of $\Phi$, and conditioning on it is a bad control (Angrist & Pischke, 2009). Its coefficient (−0.143) and the jump in within R² (0.14 to 0.19) are what that mechanical link would produce.

The inference also fails on its own terms: a coefficient that survives one imperfect proxy cannot show that a confounder is absent. In fact the modularity coefficient falls by about 18% (0.118 to 0.097) when staffing is added.

**Repair.**

- Replace the control with pre-determined measures of capability, such as baseline staffing interacted with year.
- Drop "cannot be attributed".
- Add a sensitivity analysis for unobserved confounding, for example Oster (2019) (to verify).

### cmt:7. The observation count is inconsistent with the stated design. [fixable, but must be resolved before the estimates can be assessed; `asserted`, check K2]

**What the manuscript commits to.** §3.1 describes a balanced panel of 412 hospitals observed annually from 2009 to 2019, giving 4,712 hospital-years. `ms:T2` reports 4,712 observations in all four models.

**Where it contradicts itself.**

- 2009–2019 inclusive is 11 years, and $412 \times 11 = 4{,}532$.
- $4{,}712/412 \approx 11.44$. A balanced panel requires a whole number.
- $\text{Peer}_{s,t-1}$ for 2009 requires survey data from 2008, which §3.1 does not mention. If none exist, every model containing the peer variable should have $412 \times 10 = 4{,}120$ observations.
- The uncertainty measure needs quarterly admissions for the three preceding years (2006–2008 for the 2009 observations). Administrative sources plausibly supply these, but the manuscript should say so.

**Repair.**

- Reconcile the counts.
- Give the sample-construction flow: survey respondents → hospitals that responded every year → analytic sample.
- Document the 2008 data.
- Report how many states are represented and the distribution of sample hospitals per state.

---

## 4. Minor concerns

**cmt:8. Significance marker.** [minor; `asserted`, K2] `ms:T2.M3.uncertainty` is reported as 0.084 (SE 0.051) and marked ***. That gives $t \approx 1.65$ and a two-sided $p \approx 0.10$: not significant at any conventional level. The Model 4 estimate, 0.079 (SE 0.050), is correctly unstarred. The other stars in Table 2 are consistent with their standard errors (K2).

**cmt:9. Presentation of the interaction.** [fixable; K5]

- Because $m$ is not centred, $\beta_1$ in Models 3–4 is the modularity effect at mean uncertainty. $\beta_2$ is the uncertainty effect at $m = 0$, about 1.9 standard deviations below mean modularity.
- Report the marginal effect of modularity across the observed range of $u$, with confidence intervals. The implied effect is $0.118 - 0.061u$: 0.057 at $u = +1$ SD, and zero near $u \approx +1.9$ SD.
- The model's threshold is convex in $m$ (through $1/(1-m)$), whereas the estimating equation is linear. Show that the interaction is not an artefact of functional form.

**cmt:10. Clustering.** [fixable] The peer variable and the state requirements vary at the state level. Standard errors should be clustered by state. With few clusters, use a wild-cluster bootstrap. This applies to Models 1–4 and to the event study, and it affects how much weight Model 1's "significant" peer effect can bear.

**cmt:11. From threshold to share.** [fixable; `asserted`] H1 and H2 are stated for $\Phi$, a spending-weighted share (§2.4). The propositions concern $k^*$.

- For H1: $\partial\Phi/\partial m = f(k^*)\,\partial k^*/\partial m$, which requires positive spending-weighted density at $k^*$ and $k^* < 1$.
- For H2: $\partial^2\Phi/\partial m\,\partial u = f'(k^*)\,\partial k^*/\partial m\,\partial k^*/\partial u + f(k^*)\,\partial^2 k^*/\partial m\,\partial u$, which requires an assumption about $f'$.
- Because $\Phi$ is a share of *spending* paid to vendors (§3.2), modularity also lowers $C_B$ for functions already outsourced. Whether that raises or lowers $\Phi$ depends on whether hold-up costs are payments to vendors. Left unaddressed, this intensive-margin effect could offset the extensive-margin effect.
- The model restricts $m$ to $[0,1)$, but the measured share can equal 1.

State the needed assumptions (for example, a uniform distribution of $k$), or derive the predictions directly for $\Phi$.

**cmt:12. Construct validity of uncertainty.** [minor] Volatility of admissions (§3.2) measures demand uncertainty. The transaction-cost construct is uncertainty about the disturbances that require adapting the IT relationship. The institutional construct, uncertainty about the link between means and ends, is different again. Justify the measure, or supplement it.

**cmt:13. Language of magnitude.** [minor] The abstract says modularity "strongly predicts" outsourcing. The effect is one-sixth of a pooled standard deviation per pooled standard deviation of modularity (K4). The within-hospital standard deviation of modularity, which is the variation actually used, is presumably smaller. Report within-hospital standard deviations and describe magnitudes in measured terms.

**cmt:14. Selection.** [fixable] The sample is restricted to hospitals that responded every year (§3.1), and §5.2 acknowledges the risk. Report how many hospitals were dropped. Re-estimate on the unbalanced panel, with weights for response and attrition.

**cmt:15. Priority and literature.** [fixable] The claim to be "the first study to adjudicate directly between transaction-cost and institutional explanations of IT outsourcing" (abstract; §1) needs support. The information-systems literature has studied the diffusion of IT outsourcing as imitation, for example Loh and Venkatraman's "Kodak effect" (1992; to verify). It has also combined institutional and economic accounts of IS outsourcing, for example Ang and Cummings (1997; to verify). Engage this literature, or remove the claim.

**cmt:16. Unreported analyses and measurement drift.** [fixable]

- The event study, the measure that includes licences, and the non-system subsample are all described as giving "similar" results but none is shown. Report them in an appendix.
- During the decade, spending moved from licensed to vendor-hosted software. Explain where hosted and subscription spending is classified: with the excluded licences, or with the included services. A reclassification would raise measured $\Phi$ at the same time as certified interfaces spread.

**cmt:17. Presentation.** [minor]

- Number the assumptions consistently (cmt:1).
- Say which controls actually vary within hospitals. Teaching status and ownership are largely absorbed by the hospital fixed effects.
- Report the number of clusters and the mean of the dependent variable in Table 2.
- The practical advice in §5.1, that leaders should "attend first to the modularity of their systems", has no support without evidence on performance (cmt:4).

---

## 5. Recommendation

**Major revision.**

**Rationale.** The core finding may well survive a proper design: within a hospital, rising modularity goes with rising outsourcing. The conceptual contribution, specificity as a product of interface standards, deserves a hearing. As submitted, however:

- the second proposition is mis-derived (cmt:1);
- the headline adjudication is not supported, and that is fatal to the claim as stated (cmt:2);
- the causal language is not earned (cmt:3, cmt:6);
- the design cannot speak to the aggregate diffusion that frames the paper (cmt:4);
- the mechanism is not shown (cmt:5);
- the sample counts do not reconcile (cmt:7).

Each repair is feasible with data the authors appear to hold, namely the function-level survey items and the staggered state requirements. I would not support publishing any version that keeps "rule out" or "Not Mimicry" without a design that can tell the accounts apart.

If the editor reserves major revision for papers whose central claim is expected to survive substantially intact, this paper should instead be read as **reject, with encouragement to resubmit** as a reframed paper.

## Confidential note to the editor

Two problems are of the kind careful internal checking would have caught: the proof error in `ms:Prop2`, and the observation count (cmt:7). I suggest nothing beyond error. Still, before a revised version goes back to referees, the editor may wish to require the analysis code and a log of how the sample was constructed.

---

## Annex A. Checks that would settle the formal and numerical findings (not run; all findings `asserted`)

**K1 (cmt:1): the cross-partial of $k^*$ and its sign under A3.**

```python
import numpy as np
import sympy as sp

s, g0, g1, h0, h1, u = sp.symbols('s g0 g1 h0 h1 u', positive=True)
m = sp.symbols('m', nonnegative=True)
G, H = g0 + g1*u, h0 + h1*u
kstar = (s + G) / (H*(1 - m))

prop1   = sp.diff(kstar, m)
cross   = sp.diff(kstar, m, u)
claimed = g1 / (H*(1 - m)**2)                                  # Appendix, proof of Prop. 2
correct = (g1*h0 - h1*(s + g0)) / (H**2*(1 - m)**2)

print(sp.simplify(prop1 - (s + G)/(H*(1 - m)**2)))              # expect 0: Prop. 1 as printed
print(sp.simplify(cross - correct))                             # expect 0: correct cross-partial
print(sp.factor(sp.simplify(claimed - cross)))                  # expect nonzero: omitted H'(u) term
print(sp.simplify(sp.diff(kstar, u) - (g1*h0 - h1*(s + g0))/(H**2*(1 - m))))  # expect 0

f = sp.lambdify((s, g0, g1, h0, h1, u, m), cross, 'numpy')
rng = np.random.default_rng(0)
n = 200_000
sv, g0v, g1v, h0v, h1v = rng.uniform(0.01, 5, (5, n))
uv, mv = rng.uniform(0, 5, n), rng.uniform(0, 0.99, n)
a3 = h1v/h0v > g1v/(sv + g0v)                                   # Assumption A3
vals = f(sv, g0v, g1v, h0v, h1v, uv, mv)
print(a3.sum(), int((vals[a3] >= 0).sum()), (vals[~a3] > 0).mean())
# expect: no draw satisfying A3 has a non-negative cross-partial; draws violating A3 are positive
```

**K2 (cmt:7, cmt:8, cmt:2(b)): observation count; t statistics, p-values and 95% CIs from Table 2.**

```python
from scipy import stats

print(412*11, 412*10, 4712/412)            # expect 4532, 4120, 11.437 (not an integer)

dfree = 412 - 1                            # hospital clusters minus one
T2 = {'M1 peer': (0.137, 0.031), 'M2 peer': (0.042, 0.038), 'M3 peer': (0.039, 0.037),
      'M4 peer': (0.036, 0.036), 'M2 mod': (0.112, 0.024), 'M3 mod': (0.118, 0.025),
      'M4 mod': (0.097, 0.023), 'M3 unc': (0.084, 0.051), 'M4 unc': (0.079, 0.050),
      'M3 mxu': (-0.061, 0.019), 'M4 mxu': (-0.058, 0.019), 'M1 spec': (-0.094, 0.027),
      'M2 spec': (-0.091, 0.027), 'M3 spec': (-0.090, 0.026), 'M4 spec': (-0.088, 0.026),
      'M4 staff': (-0.143, 0.029)}
q = stats.t.ppf(0.975, dfree)
for k, (b, se) in T2.items():
    t = b/se
    print(f'{k:9s} t={t:6.2f} p={2*stats.t.sf(abs(t), dfree):.4f} '
          f'CI=({b - q*se:.3f}, {b + q*se:.3f})')
# expect: M3 unc t~1.65, p~0.10 (not ***); M2 peer CI ~(-0.03, 0.12); other stars consistent
```

**K3 (cmt:2(a), cmt:5): implied auxiliary coefficients, and a demonstration that the identity holds exactly.**

```python
import itertools
import numpy as np, pandas as pd, statsmodels.api as sm

bm, e = 0.112, 0.0005
print((0.137 - 0.042)/bm, (-0.094 + 0.091)/bm)                  # expect ~0.85 and ~-0.027
dp = [(0.137+a - (0.042+b))/(bm+c) for a, b, c in itertools.product([-e, e], repeat=3)]
ds = [(-0.094+a - (-0.091+b))/(bm+c) for a, b, c in itertools.product([-e, e], repeat=3)]
print(min(dp), max(dp), min(ds), max(ds))                       # rounding bounds

# Identity b_short = b_long + b_mod * delta under two-way FE on a balanced panel
rng = np.random.default_rng(1)
N, T = 412, 11
i, t = np.repeat(np.arange(N), T), np.tile(np.arange(T), N)
peer = rng.normal(size=N*T) + 0.1*t
spec = rng.normal(size=N*T)
mod = 0.8*peer - 0.03*spec + rng.normal(size=N*T)
y = 0.11*mod + 0.04*peer - 0.09*spec + rng.normal(size=N*T)
d = pd.DataFrame(dict(i=i, t=t, y=y, mod=mod, peer=peer, spec=spec))
def within(c):                                                  # exact two-way demeaning (balanced)
    return (d[c] - d.groupby('i')[c].transform('mean')
                 - d.groupby('t')[c].transform('mean') + d[c].mean())
W = pd.DataFrame({c: within(c) for c in ['y', 'mod', 'peer', 'spec']})
short = sm.OLS(W.y, W[['peer', 'spec']]).fit().params
long_ = sm.OLS(W.y, W[['mod', 'peer', 'spec']]).fit().params
aux   = sm.OLS(W['mod'], W[['peer', 'spec']]).fit().params
print(short - (long_[['peer', 'spec']] + long_['mod']*aux))     # expect ~0 (machine precision)
```

**K4 (cmt:4, cmt:13): magnitudes.**

```python
b2, sd_m, sd_phi = 0.112, 0.24, 0.17
print(b2*sd_m, b2*sd_m/sd_phi)                                  # expect 0.027 and ~0.16
print(b2*1.0, [round(b2*dm, 3) for dm in (0.2, 0.3, 0.4, 0.5)]) # upper bound; illustrative rises
x = 0.31/1.5
print(x, 2*x, x)   # if the share doubled linearly with decade mean 0.31: ~0.21 -> ~0.41, rise ~0.21
```

**K5 (cmt:9, cmt:1(e)): marginal effects in Model 3.**

```python
b_m, b_u, b_mu, mbar = 0.118, 0.084, -0.061, 0.46
for uu in (-2, -1, 0, 1, 2):
    print(uu, round(b_m + b_mu*uu, 3))                          # modularity effect at u (SD units)
print(-b_m/b_mu)                                                # expect ~1.93: effect reaches zero
print(b_u + b_mu*mbar)                                          # expect ~0.056: u effect at mean m
```

## Annex B. Findings ledger

| id | locus | severity | status |
|---|---|---|---|
| cmt:1 | `ms:Prop2`, Appendix, `ms:A3`, `ms:H2`, §5 ¶2 | damaging | asserted (K1) |
| cmt:2 | title, abstract, `ms:H3`, `ms:T2.M1/M2.peer`, §5, §6 | fatal (to the "Not Mimicry" claim as stated) | asserted (K2, K3); conceptual parts are argument |
| cmt:3 | §3.3, §4 Robustness, §5 | damaging | argument |
| cmt:4 | abstract, §1, §3.3, §6 | damaging | asserted (K4) |
| cmt:5 | §2.2, §3.2, `ms:T2.*.spec`, §5 | damaging | asserted (K3) |
| cmt:6 | §3.2, §3.3, `ms:T2.M4` | fixable | argument |
| cmt:7 | §3.1, `ms:T2` observations | fixable | asserted (K2) |
| cmt:8 | `ms:T2.M3.uncertainty` | minor | asserted (K2) |
| cmt:9 | `ms:T2.M3`, `ms:T2.M4` | fixable | asserted (K5) |
| cmt:10 | §3.3 | fixable | argument |
| cmt:11 | §2.4, §3.2 | fixable | asserted |
| cmt:12–17 | as cited | minor/fixable | argument |

---

## Decisions for the reviewer

1. **cmt:1.** Accept the corrected cross-partial, after running K1 or checking it by hand. It changes the report's account of H2 and of §5 ¶2.
2. **cmt:2 severity.** Choose between *fatal* (to the "Not Mimicry" claim as stated) and *damaging*. Downgrade if you read the paper's central claim as the link between modularity and outsourcing rather than the adjudication.
3. **Reverse-causality conjecture.** Decide whether to keep it (cmt:2(a) structure 3; cmt:3(a)). It rests on domain plausibility, not on anything in the manuscript.
4. **Implied auxiliary coefficients.** Decide whether to keep $\delta_{\text{peer}}$ and $\delta_{\text{spec}}$ (cmt:2(a), cmt:5(b)). They depend on the OVB identity and on rounding, and $\delta_{\text{spec}}$ cannot be turned into a correlation without within-hospital standard deviations.
5. **Magnitude bound in cmt:4.** Decide whether to keep it. It assumes the sample tracks the national doubling described in §1.
6. **Citations marked "(to verify)".** Check them before sending: Haveman 1993; Manski 1993; Roth 2022; Oster 2019; Loh & Venkatraman 1992; Ang & Cummings 1997.
7. **Recommendation.** Choose between major revision and reject with encouragement to resubmit, and decide whether to keep the confidential note asking for code and the sample-construction log.
8. **Raising cmt:7 early.** Decide whether to send the observation-count discrepancy to the editor as a query ahead of the full report.
