**Best-Self Elicitor: Mode S, Round 3 (sharpening)** (`bs:S3`, Reviewership v0.1)

Dear Reviewer,

Thank you. This is the last round before I write the standards specification. It does three things:
1. It turns each of your 16 accepted standards into a form that can be checked, against the paper and against your draft.
2. It points out the places where your accepted standards pull against each other, and asks you to rank them.
3. It asks whether anything important is missing.

After your answers, I will write the specification. It is a specification of your standards, not a review.

**Your request for the editor's own words.** I have passed on to the workbench your request for the editor's own answers to E1–E4 before you draft (`bs:EB.ann1`). Whether to share them is for the editor and the workbench to decide.

## 1. What I recorded from Round 2

Please correct anything I have recorded wrongly. I will treat silence as confirmation for this section only.

### Your general note on balance

You noted that my suggestions all bear on concerns the editor already suspects. To balance this, you widened two standards: `std:12` now covers both halves of your bias, and `std:15` now asks you to say what survives. You asked Mode C to check both.

You also asked Mode C to check three other things:
- that you checked that each proof uses only stated assumptions (`std:5`, part b);
- that your point on survival selection stays at one sentence (`bs:EB.ann5`);
- your re-derivation as a whole, since it is "exactly what I skip under pressure".

### Settings

| Dimension | Recorded setting |
|---|---|
| **INF** | **Kinds of inference:** deduction, induction and inference to the best explanation are all allowed. An explanation found after the results are in must be labelled, and it gives no support. Choosing the best explanation between rivals needs discriminating evidence.<br>**Derivation:** required. At minimum, a sketch that states every assumption fixing a sign; a formal derivation is preferred for interactions.<br>**Unstated premises:** low tolerance.<br>**What a good explanation does:** depth, meaning a mechanism specified closely enough to yield an implication the data could refute. "A mechanism that covers everything predicts nothing."<br>**Ways of justifying a claim:** eliminative, accepted when the test discriminates; assimilative, argue each time (it needs a prediction the original reading lacks); reductive, accepted when the lower-level mechanism is shown to *produce* the pattern.<br>**Rivals:** required. |
| **TEC** | **Code and data:** preferred, not required at first round. For a revision: code that reproduces the main tables, plus the data where the licence allows.<br>**Depth:** re-derive models; spot-check numbers (not every cell).<br>**Estimators:** as proposed in Round 2, plus an estimator robust to effects that differ across adoption cohorts, plus clustering (`std:9`).<br>**Numerical consistency:** always.<br>**Formal models:** a closed form is preferred. A simulation is acceptable if the parameter ranges are reported and the comparative statics hold across them. For a one-page model, a closed form is expected. |
| **ONT** | **Actors:** boundedly rational and capable of opportunism. Institutional entities are admissible if they are specified so as to yield a prediction.<br>**Level of analysis:** cross-level allowed, with an explicit bridge (now in `std:1`).<br>**Kinds of cause:** individual mechanisms and selection; selection must be shown.<br>**Constructs:** strict for the main regressor, the outcome, the rival's key construct, and any control that carries identifying weight; moderate for other controls.<br>**Model classes:** causal, choice-theoretic and selection explanations admissible. Functional explanations rejected unless a selection or feedback mechanism is shown. Constitutive: no view. |
| **EPI** | **Stance:** realist. No "as if" defence for the assumption that does the work in a model.<br>**Corroboration:** sophisticated falsificationist, read as Lakatos rather than naive Popper.<br>**Identification:** design-based preferred. Model-based assumptions are acceptable if stated, argued and tested where possible, but they are no substitute where a design-based route exists.<br>**Novel prediction:** high weight.<br>**Evidence:** effect sizes and plausibility. Pre-registration is not expected for archival panels, but the paper says how its main specification was chosen and reports the specifications that didn't work.<br>**Measurement:** fit of measure to construct argued. A single informant is fine for factual items; perceptual constructs need multiple informants or a validation. |
| **PRA** | **Audience:** generalist readers, both economists and sociologists. You defer on whether the rival is recognisable to its proponents.<br>**Contribution, in your order:** a derived implication, credibly tested; then questioning an assumption the field holds; then gap-filling, which counts least. Being "interesting" is welcome but not sufficient, and a paper that denies what its audience takes for granted carries a higher burden of evidence.<br>**Priority claims:** sometimes.<br>**Practice:** not a criterion, unless the paper makes claims about practice; then those claims must follow from the evidence.<br>**How the review is written:** `std:15`.<br>**Editor's needs:** `bs:EB` with your annotations. |

**Weights:** INF 0.9 · EPI 0.9 · TEC 0.7 · ONT 0.6 · PRA 0.4.

**Field-specific inferences (MI1–MI10):**
- **MI1** (hold-up and hierarchy): endorse as theory, with the empirical proviso in `std:11`. In-house governance is one safeguard among several; long-term contracts and hostages are others.
- **MI2** (persistence implies efficiency): argue each time.
- **MI3** (spread among peers implies imitation): argue each time, in both directions.
- **MI4** (adoption is not implementation): argue each time for the step from adoption to use.
- **MI5** (local search below aspiration): neutral.
- **MI6** (fixed effects identify a causal effect): endorse only as a conditional, and with an estimator robust to cohort differences.
- **MI7** (a lost star means no effect): reject.
- **MI8** (standard interfaces reduce specificity): argue each time. Standard interfaces can relocate specificity rather than remove it, and causation can run the other way.
- **MI9** (equilibrium implies optimality): argue each time. With multiple equilibria, "equilibrium" does not mean "optimal".
- **MI10** (legitimacy as a resource): neutral. A legitimacy argument is testable where it predicts something an efficiency argument does not.

### Changes to the list

- The substance of my suggestion `std:9` (unit of theory and unit of test) is now folded into `std:1`.
- The `std:9` slot now holds clustering. This was one of my reserve suggestions, rewritten by you.
- The reserve standard on code and data is now the TEC.1 setting.
- The reserve standard on the abstract and conclusions is folded into `std:2` and `std:3`. The overlaps with your reactions `bs:RX.a` and `bs:RX.b` are recorded as provenance.

### Citations

Your memory agrees with mine on Davis (1971), Williamson (1985) and Manski (1993). The workbench still marks them "(to verify)", because recollection, yours or mine, is not verification.

## 2. The 16 standards in checkable form

For each standard I give three things:
- **Check (paper):** the conditions that must hold for the paper to pass.
- **Applied when:** what your draft must contain for Mode C to count the standard as applied.
- **Question:** where the standard needs a decision from you to become checkable. Each question has an id, `bs:Qn`.

The wording is yours. I have only split it into conditions, and anything I added is marked [mine]. For each standard, please confirm the checkable form or rewrite it.

---

**`std:1` Hypotheses must be derived from the theory, at the tested level and scale.** INF.3, ONT.2 · must · origin: reviewer (my suggestion, formerly `std:9`, is folded in)

**Check (paper).** Take each hypothesis the paper presents as a test of its theory. All of the following must hold:
- (a) It follows from a stated proposition, proof or explicit sketch.
- (b) Every assumption that fixes a predicted sign, including the sign of any interaction, is stated and defended.
- (c) If the theory's unit differs from the test's unit (for example, transactions versus organizations), the aggregation step is stated, and each predicted sign is shown to survive it on the scale of the variable actually tested.
- (d) Any hypothesis that fails (a)–(c) is labelled exploratory, and it is not counted for or against the theory.

**Applied when.** The draft takes each hypothesis in turn and gives a verdict on (a)–(c), citing where in the paper the support lies (proposition, proof or section). Where a hypothesis fails, the draft states what follows under (d) and what repair would fix it.

**Question.** See tension `bs:T1`.

---

**`std:2` Failed predictions are results; after-the-fact rescues are costs.** INF.1, EPI.2, EPI.4 · must · origin: reviewer (wording from my reserve standard folded in; overlaps `bs:RX.a`)

**Check (paper).** Take each derived prediction that fails in the reported tests.
- (a) The failure is reported as a failure everywhere the prediction is stated: the hypotheses, the results, the abstract and the conclusions.
- (b) The paper says what the failure implies for the theory, naming which assumption or step is now in doubt.
- (c) Any explanation offered afterwards, using a mechanism the model does not contain, is labelled as such and is not counted as support.
- (d) Such an explanation counts against the theory, unless the mechanism is built into the model and yields a further prediction that the data could reject and do not.

**Applied when.** For each failed prediction, the draft checks (a)–(d), citing where each is or is not met.

---

**`std:3` Ruling out a rival needs a discriminating test.** INF.7, INF.6 · must · origin: reviewer (wording from my reserve standard folded in; overlaps `bs:RX.b`)

**Check (paper).** Take each claim that a rival account is ruled out, or words to that effect.
- (a) The rival's prediction is stated as its own literature usually states it, with a citation.
- (b) At least one test is reported on which the two accounts predict different signs or patterns, and the paper says what each account predicts.
- (c) The rival's key construct is measured in a way its proponents would accept, and the paper argues this.
- (d) Evidence consistent with the paper's own account is counted as support only where the rival predicts something different.
- (e) If (b) or (c) fails, the paper says only that its evidence does not require the rival. Throughout, no conclusion is stated more strongly than the design supports.

**Applied when.** The draft locates each ruling-out claim, checks (a)–(e), and proposes weaker wording where (e) applies.

**Question.** Your judgement on (c) depends on the rival's content. See tension `bs:T2`.

---

**`std:4` A lost significance star is not a null result.** INF.2 (rejects MI7), EPI.5 · must · origin: reviewer

**Check (paper).** The paper may infer that a variable has no effect, or plays no role, from a coefficient that loses significance once a correlated regressor is added. Wherever it does, it addresses all three of the following:
- (a) collinearity between the two regressors (for example, their correlation, or a joint test) [the examples are mine];
- (b) differential measurement error, that is, which regressor is measured with more error;
- (c) mediation, that is, whether the added regressor lies on the causal path from the first.

The paper fails if any of the three is left unaddressed.

**Applied when.** The draft locates each such inference and names which of (a)–(c) the paper leaves unaddressed.

---

**`std:5` Re-derive the model.** TEC.2, TEC.5 · must · origin: reviewer · Mode C to check, at your request

**Check (by you).** For each proposition:
- (a) Re-derive it from the stated assumptions, including the sign of every comparative static and interaction it claims.
- (b) Check that each step of the proof uses only assumptions stated in the set-up, and list any unstated assumption that a step relies on.
- (c) [mine] Record the re-derivation as a check that the workbench harness can run, for example a `sympy` script for the signs of the derivatives and cross-partials. A finding about the model then reads "demonstrated" or "refuted-by-check", not "asserted".

**Applied when.** For each proposition, the draft says whether it follows and names any unstated assumption, with its location. If you accept (c), it also gives the id of the check and its result.

**Question `bs:Q1`.** Do you accept (c)? It is the workbench's rule for formal claims. You can do the re-derivation by hand and have the harness check it.

---

**`std:6` Spot-check the numbers.** TEC.4 · must · origin: reviewer

**Check (by you).** Check the following:
- (a) For the key coefficients, t is approximately b/se, allowing for rounding.
- (b) The significance stars match t (or p) under the stated thresholds.
- (c) N is consistent across tables and with the sample description.
- (d) For each reported interaction, the marginal effect of the focal variable across the observed range of the moderator matches what the text claims.
- (e) The magnitudes are economically plausible given the descriptive statistics, for example the implied change in the outcome for a one-standard-deviation change in the regressor.
- (f) The text describes each result as the table shows it: its sign, its significance, and which model it comes from.

**Applied when.** The draft lists which checks were run, on which cells, and with what result. If you accept `bs:Q1`, the computational checks are recorded as harness checks.

**Question `bs:Q2`.** What is the minimum spot check? My proposal: every coefficient on which a hypothesis test rests, every number quoted in the abstract, and every interaction for check (d). Do you accept this, or do you want to set your own minimum?

---

**`std:7` Measures fit their constructs.** ONT.4, EPI.6 · must · origin: reviewer

**Check (paper).** This standard covers the main regressor, the outcome, the rival's key construct, and any control that carries identifying weight. For each of these:
- (a) The construct is defined, and the paper argues that the measure captures it.
- (b) No governance-relevant attribute is measured by, or inferred from, the outcome it explains.
- (c) Perceptual constructs have multiple informants or a validation. Single-informant factual items are acceptable.

**Applied when.** The draft names each such variable and gives a verdict on (a)–(c), citing where in the paper each is addressed.

**Question `bs:Q3`.** A control "carries identifying weight" if its inclusion moves a key coefficient, or if it stands in for a rival's construct. To make this checkable, how much movement counts? My proposal: a change in sign, or a change in size that you state in advance as substantively meaningful. I have avoided a significance-based threshold because of `std:4`.

---

**`std:8` Efficiency claims must show selection.** ONT.3, INF.2 (MI2, MI9) · should, and must where efficiency is the paper's conclusion · origin: reviewer

**Check (paper).** Classify each of the paper's conclusions about governance as one of two kinds:
- (i) a claim about motive or alignment: choices track transaction attributes as the theory predicts;
- (ii) a claim about efficiency: the observed choice is an optimal response.

For each claim of kind (ii), the paper must show or argue for selection pressure, meaning competition and the time for selection to act. Where selection is weak, as in nonprofit or regulated sectors, it cannot be assumed. Claims of kind (i) do not need this.

**Applied when.** The draft classifies each governance conclusion, citing where it appears. For each kind-(ii) claim, it checks the argument for selection.

**Question `bs:Q4`.**
- **"Where efficiency is the conclusion":** my proposal is that this means stated in the abstract or the conclusions as what the results show. Do you accept that?
- **"Economizing":** how should a conclusion stated as "X is economizing" be classified: as an efficiency claim, as a motive claim, or by context? The word is common in transaction-cost work, and it appears in this invitation's abstract (sentence 7), so the answer matters here. I am asking for your general rule, not for a verdict on this paper.

---

**`std:9` Clustering.** TEC.3 · must · origin: my reserve suggestion, rewritten by you

**Check (paper).**
- (a) Standard errors are clustered at the level at which the key regressors vary, or the paper explains why not. "Key regressors" means every regressor on which a hypothesis test rests, including the measure of the rival [this definition is mine].
- (b) With few clusters, a small-cluster correction is used, for example a wild cluster bootstrap [the example is mine].

**Applied when.** The draft states three things: the level at which the paper clusters, the level at which each key regressor varies, and whether the two match.

**Question `bs:Q5`.** What counts as "few clusters"? Please set a number. I will not propose one with confidence.

---

**`std:10` Find the source of the identifying variation.** EPI.3, TEC.3 · must · origin: reviewer

**Check (paper).** The paper shows:
- (a) what the fixed effects absorb, and what variation remains;
- (b) which units supply the identifying variation, and how much within-unit variation there is in the regressor;
- (c) whether those units differed before treatment, in levels or in trends;
- (d) that the comparison group makes sense;
- (e) for a discrete treatment adopted at different times: estimates in event time, with leads, against units not yet treated, using an estimator robust to effects that differ across adoption cohorts (for example Callaway and Sant'Anna 2021, or Sun and Abraham 2021; both to verify);
- (f) for a continuous treatment: leads of the regressor, or pre-trends by later exposure.

**Applied when.** The draft answers (a)–(d) for the main specification, and says which of (e) or (f) applies and whether the paper has done it. Under `std:15`, it also says in advance what pattern would persuade you.

**Question.** What counts as passing (c), (e) and (f)? See tension `bs:T3`.

---

**`std:11` Direction of causation for attributes chosen together with governance.** EPI.3, INF.2 (proviso to MI1) · must · origin: reviewer

**Check (paper).** This applies wherever governance is regressed on an attribute that firms may choose with governance in view. Asset specificity is the standard case; a technology choice that changes specificity is another, per your note on MI8. The paper must do at least one of the following:
- (a) argue the direction of causation, giving a reason why the attribute was not chosen in anticipation of governance; or
- (b) identify the direction, by timing, an instrument or the design.

In either case it must also:
- (c) address reverse causality, and name the obvious omitted variables and say how they are handled.

**Applied when.** The draft identifies each such regressor and gives a verdict on (a) or (b), and on (c).

**Question `bs:Q6`.** What makes a direction "argued" under (a) rather than merely asserted? My proposal: the paper gives a reason why anticipation is implausible, for example that the attribute was fixed before the governance option existed. Do you accept this?

---

**`std:12` Symmetry.** EPI.2 · must · origin: reviewer · this applies to your draft, not to the paper; Mode C to check both halves, at your request

**Check (your draft).**
- (a) For each evidential criticism the draft makes of the rival account, the draft asks whether the paper's own account meets the same bar on the same evidence, and it gives the answer.
- (b) The draft does not accept the economizing account on consistency alone where the rival predicts the same thing. This is the first half of your bias.
- (c) Before calling an institutional account unfalsifiable or untested, the draft asks whether the version at issue makes a testable prediction, and it gives the answer. This is the second half.

**Applied when.** Points (a)–(c) are visible in the draft. Mode C will pair each criticism of the rival with its counterpart for the paper's own account.

---

**`std:13` Claims of absence need bounds.** EPI.5 · should · origin: my suggestion, rewritten by you (kept separate from `std:4` so the record shows which half is mine)

**Check (paper).** Where the paper claims that a variable has no effect:
- (a) It reports the estimate and its confidence interval, in the specification on which the claim rests.
- (b) It states, in substantive terms, the smallest effect that would matter.
- (c) It shows that the interval excludes that effect. An equivalence test is one way to do this, but it is not required.
- (d) If it cannot do (a)–(c), it says only that the effect is not distinguishable from zero in this sample.

**Applied when.** The draft checks (a)–(d) for each claim of absence. [mine] An approximate interval, b ± 1.96·se, can be recomputed as a harness check.

**Question `bs:Q7`.** If the paper does not state a smallest effect that would matter, should you propose one yourself (under `std:15`), labelled as your choice, and check the interval against it?

---

**`std:14` Peer influence versus shared conditions.** EPI.3, EPI.6 · should · origin: my suggestion, rewritten by you so that it cuts both ways

**Check (paper).** Take each measure of peers' earlier adoption used as evidence for or against imitation. The design must separate imitation from:
- (a) peers responding alike to shared conditions, such as common shocks, common regulation or common suppliers;
- (b) selection into peer groups.

In addition:
- (c) where the paper's own regressor may respond to the same shared conditions, the design addresses that too.

**Applied when.** The draft checks (a) and (b) for the peer measure, and (c) for the paper's own regressor. Point (c) is where this standard meets `std:12`.

---

**`std:15` Problems to solve, not gotchas.** PRA.5 · must · origin: reviewer (with my clause on decisive versus fixable problems, accepted by you) · Mode C to check (f), at your request

**Check (your draft).** For each objection, the draft:
- (a) says where you may be wrong;
- (b) proposes at least one test or analysis whose result you do not know;
- (c) says in advance what result would change your view;
- (d) names the repair that would change the recommendation;
- (e) labels the problem as decisive (fatal or damaging) or as fixable or minor.

For the draft as a whole:
- (f) it says what in the paper survives the criticisms, and what would be lost if the paper were not published.

**Applied when.** Points (a)–(e) appear for each objection they cover (see `bs:Q8`), and (f) appears once.

**Question `bs:Q8`.** Does every objection need (a)–(d), or only the fatal and damaging ones? My proposal: (a)–(d) for fatal and damaging objections, (e) for all objections, and (f) once per draft.

---

**`std:16` Readable by non-economists; rival recognisable.** PRA.1 · should · origin: reviewer (from the editor's need N4)

**Check (paper).**
- (a) Each assumption of the model, and what drives each prediction, is stated in words alongside the formal statement. A reader without economics training could say, from the words alone, why each prediction has its sign.
- (b) The rival is described in terms its proponents would recognise. You give a provisional view and defer to the second reviewer.

**Applied when.** The draft gives a verdict on (a), naming any assumption or prediction that lacks a statement in words, and gives (b), marked as deferring.

## 3. Tensions: please rank

Each tension below is a pair of your accepted standards that pull against each other. For each, please choose an option, or say which standard governs when the two conflict.

**`bs:T1`: `std:1` (derivation) versus `std:2` (failed predictions).**
- **The pull.** Under `std:1`, a hypothesis that does not follow from the theory counts neither for nor against it. Under `std:2`, a failed prediction counts against the theory. So the less carefully a hypothesis is derived, the less its failure costs the theory: `std:1` can shield a theory from `std:2`.
- **Option (a): `std:1` first.** A failed hypothesis that is not properly derived does not count against the theory. The paper's presentation of it as derived is a separate `std:1` failure, rated as a must on a dimension weighted 0.9. This respects the logical point that a prediction the theory does not entail cannot refute it.
- **Option (b): `std:2` governs where the paper presented the hypothesis as derived.** The failure counts against the theory as the paper states it, and `std:1` adds the derivation fault. This avoids rewarding under-derivation.
- **Option (c):** your own rule.

**`bs:T2`: Your judgements about the rival (`std:3` part c, `std:12` part c, `std:14`) versus your deferral on the rival's content (`std:16` part b, and the division of labour in `bs:EB`).**
- **The pull.** Three of your standards, two of them must, require judgements about institutional theory:
  - whether the rival's construct is measured in a way its proponents would accept (`std:3` c);
  - whether the version at issue makes a testable prediction (`std:12` c);
  - what imitation predicts, as opposed to shared conditions (`std:14`).
  But you defer to the second reviewer on the rival's content.
- **Option (a): judge provisionally.** Make each judgement, mark it as provisional, and defer if the second reviewer disagrees. This extends what you already do under `std:16` (b).
- **Option (b): split the work.** Keep your own verdicts to design and econometrics (`std:3` b and e, `std:14`). Put `std:3` (c) and `std:12` (c) to the editor as questions for the second reviewer, not as your verdicts.
- **Option (c):** your own rule.

**`bs:T3`: `std:10` (pre-trend checks) versus `std:13` and `std:4` (claims of absence).**
- **The pull.** A pre-trend check is itself a claim of absence: no difference before treatment. Your own past criterion was "If the leads are flat, I'd be persuaded". `std:4` and `std:13` say that non-significance alone does not establish absence. The ranking matters because `std:10` is must and `std:13` is should.
- **Option (a): `std:13` applies to leads.** The intervals on the leads must exclude pre-trends large enough to matter relative to the estimated effect.
- **Option (b): leads are diagnostic.** `std:13` applies only to the paper's substantive claims. For leads, it is enough that they are jointly insignificant and small in point estimate.
- **Option (c):** your own rule.

**`bs:T4`: `std:12` (symmetry) versus your contribution setting (a paper that denies what its audience takes for granted carries a higher burden of evidence).**
- **The pull.** The readership is dual. Economists and sociologists take different accounts for granted. A higher burden on denial makes the burden depend on which account the audience favours, and that is asymmetric between the accounts.
- **Option (a): symmetry governs the evidence.** The higher burden applies only to how strongly the paper may word its claims, which is already in `std:3` (e).
- **Option (b): the higher burden governs.** Then I need your rule for deciding what a dual audience takes for granted.
- **Option (c):** your own rule.

**`bs:T5`: `bs:EB.ann5` (one sentence on survival selection) versus `std:10` (comparison group, and differences before treatment; must).**
- **The pull.** If survival selection turns out to be a first-order threat to identification, `std:10` (c) and (d) would call for more than your self-imposed single sentence.
- **Option (a): the cap holds.** One sentence, in deference to the editor's settled item.
- **Option (b): `std:10` governs if the threat is first-order.** You add a short note to the editor explaining why you went past the cap. Mode C would check that the note is there.

**`bs:T6`: A clarification rather than a tension (priority versus weight).**
- Several must standards sit on dimensions with lower weights: `std:15` on PRA (0.4), and `std:5`, `std:6` and `std:9` on TEC (0.7).
- My reading: "must" means the standard must be applied in the draft, and the weight says how much a failure on that dimension moves the recommendation.
- On that reading, a failed TEC check would move the recommendation only when you say it "signals something deeper", as in your note on the TEC weight.
- You also said that over-claiming falls under INF and EPI. So the wording clauses in `std:2` (a) and `std:3` (e) carry the 0.9 weights, not PRA's 0.4.
- Please confirm or correct this reading. Mode C's consistency check depends on it.

## 4. Is anything important missing?

The list stands at 16. Several of your Round 2 settings are themselves checkable, but Mode C checks standards, not settings. If you want any of the following checked in your draft, promote it to a standard and say which standard to merge or drop to make room. Or tell me you want the list to grow past 16.
- **Specification choice** (from EPI.5): the paper says how its main specification was chosen and reports the specifications that didn't work.
- **Adoption versus use** (from MI4): a paper that measures adoption and theorises about use argues for the link.
- **Assimilative reinterpretation** (from INF.6): reinterpreting the rival's evidence as the paper's own counts only if it yields a prediction the original reading does not.
- **Functional explanation** (from ONT.5): "it exists because it serves a function" needs a selection or feedback mechanism.
- **No "as if" defence** (from EPI.1): none for the assumption that does the work in a model.
- **Alternative safeguards** (from MI1): where a paper treats in-house governance as the remedy for hold-up, it considers the other safeguards, such as long-term contracts and hostages.

Beyond these: is there a check you perform that none of the 16 standards or the settings captures?

## 5. How to reply

Short answers are fine. For example: "std:1–16 confirmed except std:6 (see Q2) · Q1 yes · T1 b · T2 a · … · promote: specification choice, merge into std:13".

**Decisions for the reviewer**
- Confirm or rewrite the checkable form of each of `std:1` to `std:16`.
- Answer the sharpening questions `bs:Q1` to `bs:Q8`.
- Rank or resolve tensions `bs:T1` to `bs:T5`, and confirm or correct the reading in `bs:T6`.
- Decide whether to promote any setting to a standard, and if so, what to merge or drop.
- Say whether anything important is missing.
- Correct anything in section 1 that I have recorded wrongly.
