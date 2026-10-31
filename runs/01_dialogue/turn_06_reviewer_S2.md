**Focal reviewer: reply to Mode S, Round 2 (`bs:S2`)** (Reviewership v0.1)

I still have not read the manuscript. My answers follow your order.

## A general note first

All three of your suggestions bear on the editor's concerns, and so does one reserve standard. I've accepted the ones I would hold for any paper, and I say so at each. But the result is a standard set aimed mostly at finding faults that the editor already suspects. To balance it, I've added "say what survives" to `std:15`, and I've widened `std:12` to cover both halves of my bias. Mode C should check both.

## 1. Annotations on the brief

- **ann1:** Accept. Yes, please pass on the editor's own words for E1 to E4 before I draft. I'd rather read the editor than a summary. I don't need them for the standards.
- **ann2, ann3, ann5, ann6:** Accept. That includes the Mode C check on the one sentence about survival selection.
- **ann4:** Thanks.

## 2. Settings

### INF

- **INF.1:** Accept. Inference to the best explanation between rivals needs discriminating evidence (`std:3`).
- **INF.3, INF.4, INF.7:** Accept.
- **INF.5:** Depth, meaning a mechanism specified closely enough to yield an implication the data could refute. Coverage is welcome. But a mechanism that covers everything predicts nothing.
- **INF.6:**
  - *Eliminative:* accept as proposed.
  - *Assimilative:* argue each time. Reinterpreting the rival's evidence as ours counts only if the reinterpretation yields a prediction the original reading doesn't. Otherwise it is relabelling.
  - *Reductive:* accepted when the paper shows that the lower-level mechanism produces the pattern, not merely that it is consistent with it. I have no view on reductionism as such.

### TEC

- **TEC.1:** Preferred, not required at first round. For a revision, I ask for code that reproduces the main tables, plus the data where the licence allows. This covers the code-and-data reserve standard, so it needn't be a standard.
- **TEC.2:** Accept. "Recompute" means spot checks, not every cell.
- **TEC.3:** Accept, with two additions:
  - with staggered adoption, an estimator robust to effects that differ across adoption cohorts (see `std:10`);
  - clustering (see the new `std:9`).
- **TEC.4:** Accept.
- **TEC.5:** A closed form is preferred, not required. A simulation is acceptable if the parameter ranges are reported and the claimed comparative statics hold across them, not at one chosen point. For a one-page model, I expect a closed form.

### ONT

- **ONT.1:** Accept, with one change. The actors are boundedly rational *and* capable of opportunism, since both are Williamson's behavioural assumptions. Institutional entities are admissible if they are specified so as to yield a prediction. No view on others.
- **ONT.2:** Cross-level allowed, with an explicit bridge. I've built this into `std:1` (see `std:9` below).
- **ONT.3:** Accept.
- **ONT.4:** Strict for the main regressor, the outcome and the rival's key construct. Moderate for controls, except strict for any control that carries identifying weight: one whose inclusion moves a key coefficient, or that stands in for a rival's construct.
- **ONT.5:** Accept for causal, choice-theoretic and selection explanations.
  - *Functional:* rejected unless a selection or feedback mechanism is shown. "It exists because it serves a function" is not an explanation by itself.
  - *Constitutive:* no view; outside my competence.

### EPI

- **EPI.1:** Realist. Mechanisms are real and are tested through their observable implications. I don't accept the "as if" defence for the assumption that does the work in a model.
- **EPI.2:** I accept the label, read as Lakatos rather than naive Popper (see my rewrite of `std:2`).
- **EPI.3:** Design-based preferred. Model-based assumptions are acceptable if they are stated, argued, and tested where they can be (placebos, overidentification). They are not a substitute where a design-based route is available.
- **EPI.4:** Accept.
- **EPI.5:** Accept. Pre-registration is not expected for archival panel work, and I don't penalise its absence. I do expect the paper to say how the main specification was chosen and to report the ones that didn't work.
- **EPI.6:** Accept. On informants: a single informant is fine for factual items such as spending. For perceptual constructs, I expect multiple informants or a validation.

### PRA

- **PRA.1, PRA.3, PRA.5, PRA.6:** Accept.
- **PRA.2:** In my order of preference:
  1. A derived implication, credibly tested.
  2. Questioning an assumption the field holds.
  3. Gap-filling alone, which counts least.

  Being "interesting" in Davis's sense is welcome but not sufficient. A paper that denies what its audience takes for granted carries a higher burden of evidence. Your citation is right as I remember it: Davis (1971), "That's Interesting!", *Philosophy of the Social Sciences*.
- **PRA.4:** No view. Implications for practice are not a criterion for me, unless the paper makes claims about practice. Then those claims must follow from the evidence.

## 3. Weights

| Dimension | Weight | Why |
|---|---|---|
| INF | 0.9 | My decisive rejection was an inference failure. |
| EPI | 0.9 | Identification is the one thing I never skip. |
| TEC | 0.7 | High at my best. A numerical slip is usually fixable unless it signals something deeper. |
| ONT | 0.6 | Matters most where measurement is itself an identification problem. |
| PRA | 0.4 | Governs how I write more than what I conclude. Over-claiming I treat under INF and EPI. |

## 4. Field-specific inferences (MI1 to MI10)

| Id | Stance | Note |
|---|---|---|
| MI1 | Endorse as theory, with your empirical proviso (`std:11`) | One caveat: in-house is one safeguard among several. Long-term contracts and hostages are others. |
| MI2 | Argue each time | Accept. |
| MI3 | Argue each time | Accept. The reverse also holds: spread among peers is not evidence *against* imitation just because an economizing variable also predicts it. |
| MI4 | Argue each time, for the step from adoption to use | Decoupling is real. A paper that measures adoption and theorises about use must argue the link. |
| MI5 | Neutral | Not my area. |
| MI6 | Endorse only as a conditional | Accept. With staggered timing, the estimator must also be robust to heterogeneous effects. |
| MI7 | Reject | Accept. |
| MI8 | Argue each time | It's an empirical claim about a technology, not a theoretical premise. Standard interfaces can relocate specificity rather than remove it, for example into lock-in to a vendor or platform. The direction can also run the other way: firms that plan to outsource adopt standards (`std:11`). I find it plausible, which is why I want it argued. |
| MI9 | Argue each time | Accept. Where there are multiple equilibria, "equilibrium" does not mean "optimal". |
| MI10 | Neutral | The second reviewer's domain. I don't reject it: a legitimacy argument that predicts something an efficiency argument doesn't is testable, and I'll treat it so. |

## 5. Standards

### `std:1` Hypotheses must be derived from the theory

**Rewrite, must.** I've folded `std:9` in:

> A hypothesis offered as a test of the theory must follow from the theory's stated assumptions, at the level and on the scale at which it is tested. Where the theory is about transactions and the test is about organizations, the paper states the aggregation step. It also shows that each predicted sign, including the sign of any interaction, survives that step. For an interaction, the paper states and defends the assumption that fixes its sign. A hypothesis that does not follow is labelled exploratory, and it counts neither for nor against the theory.

### `std:2` Failed predictions and after-the-fact rescues

**Rewrite, must.**

> A prediction that follows from the theory and fails is reported as a result wherever the prediction is stated, including the abstract and the conclusions, and its consequence for the theory is drawn out. An explanation added afterwards, using a mechanism the theory does not contain, is labelled as such and does not count as support. It counts against the theory unless the mechanism is built into the model and yields a further prediction that the data could reject and do not.

The words "including the abstract and the conclusions" come from your reserve PRA standard, which I hold in general. Record that they overlap my reaction `bs:RX.a`.

### `std:3` Ruling out a rival needs a discriminating test

**Rewrite, must.** I've added two sentences at the end:

> The rival's prediction is taken as its own literature usually states it. Without a discriminating test, the paper may say that its evidence does not require the rival, not that the rival is ruled out, and it states its conclusions no more strongly than the design supports.

The last clause also comes from the reserve standard. Record that it overlaps `bs:RX.b`.

### `std:4` A lost significance star is not a null result

**Accept, must.**

### `std:5` Re-derive the model

**Rewrite, must.** Add at the end:

> and check that each proof uses only assumptions stated in the set-up.

This is exactly what I skip under pressure. Mode C should check that I did it.

### `std:6` Spot-check the numbers

**Rewrite, must.** Add a bullet:

> the text describes each result as the table shows it: its sign, its significance, and which model it comes from.

### `std:7` Measures fit their constructs

**Rewrite, must.** Extend it to controls as set in ONT.4:

> …and for any control that carries identifying weight.

### `std:8` Economizing claims must show selection

**Rewrite.** Priority: should, and must where efficiency is the paper's conclusion.

> A claim that a governance choice is efficient, meaning an optimal response and not merely a choice that responds to transaction attributes as the theory predicts, must show or argue for the selection pressure that would weed out misaligned forms: competition and time. Where selection is weak, as in nonprofit or regulated sectors, it cannot be assumed. A claim only about motive (that choices track transaction attributes) does not need this.

### `std:9` Unit of theory and unit of test [suggestion]

**Accept the substance, folded into `std:1`.** It is `std:1` applied to aggregation. I should have listed it myself, since the transaction is Williamson's unit of analysis. Your citation (Williamson 1985) is right as I remember it.

Use the freed slot for the clustering reserve, which I accept as **must**:

> Standard errors are clustered at the level at which the key regressors vary, or the paper explains why not. With few clusters, a small-cluster correction is used.

I check this whenever I check identification. I left it off my Round 1 list by oversight.

### `std:10` Find the source of the identifying variation

**Rewrite, must.** Replace the last sentence with:

> Where a discrete treatment is adopted at different times, it shows estimates in event time, with leads, against units not yet treated, using an estimator robust to effects that differ across adoption cohorts. Where the treatment is continuous, it shows the analogous check: leads of the regressor, or pre-trends by later exposure.

### `std:11` Direction of causation

**Accept, must.**

### `std:12` Symmetry

**Rewrite, must.** Replace the last sentence with:

> The reviewer checks the draft for both halves of my bias: accepting an economizing account too readily, and dismissing an institutional account as unfalsifiable without asking whether the version at issue makes a testable prediction.

### `std:13` Claims of absence need bounds [suggestion]

**Rewrite, should.** Keep it separate from `std:4`, so the record shows which half is mine.

> A claim that a variable has no effect reports the estimate and its confidence interval in the specification on which the claim rests, states in substantive terms the smallest effect that would matter, and shows that the interval excludes it. An equivalence test is one way to do this, not a requirement. Without such bounds, the paper may say only that the effect is not distinguishable from zero in this sample.

### `std:14` Peer influence versus shared conditions [suggestion]

**Rewrite, should.** You chose this one because of the brief. But I'd apply it to any peer-effects paper, so I accept it, in a form that cuts both ways:

> A measure of peers' earlier adoption counts as evidence for *or against* imitation only if the design separates imitation from two things: peers responding alike to shared conditions (common shocks, common regulation, common suppliers), and selection into peer groups. Where the paper's own regressor may respond to the same shared conditions, the design addresses that too.

Your citation is right as I remember it: Manski (1993), the reflection problem, *Review of Economic Studies*.

### `std:15` Problems to solve, not gotchas

**Rewrite, must.** I accept your addition about keeping decisive problems apart from fixable ones, and I add one more bullet:

> says what in the paper survives the criticisms, and what would be lost if it were not published.

### `std:16` Readable by non-economists; rival recognisable

**Rewrite, should.**

> The model's assumptions, and what drives each prediction, are stated in words that a reader without economics training can follow, alongside the formal statement. The rival is described in terms its proponents would recognise; on this point I defer to the second reviewer.

## 6. Reserve standards

- **Clustering:** In, in `std:9`'s slot.
- **Code and data:** Handled as the TEC.1 setting, not as a standard.
- **PRA (abstract and conclusions):** Folded into `std:2` and `std:3`, with the overlaps with `bs:RX.a` and `bs:RX.b` recorded.

The list stays at 16.
