**Focal reviewer: reply to Mode S, Round 3 (`bs:S3`)** (Reviewership v0.1)

I still have not read the manuscript.

**The editor's own answers.** I'm told the protocol gives the reviewer the brief, not the editor's full answers, so my request is declined. Fine. I'll work from `bs:EB` and treat what it says about the manuscript as the editor's report, unchecked.

## 0. One rule for every "Applied when"

My draft is about 1,000 words, written in a sitting of about an hour. As written, the "Applied when" clauses ask for a verdict on every condition for every item. That is a 4,000-word review. My rule:
- **Failures in the body.** The body of the draft states each condition that fails, where it fails, and what follows.
- **Passes in a list.** Passes go in a short "Checks run" list at the end, outside the 1,000 words and under 150 words. It says which standards I applied, to which items, and that they passed.
- **Missing inputs.** If I can't run a check because the paper doesn't report what it needs (descriptives, a correlation matrix, the covariances for a marginal effect), the draft asks for it. That counts as applied.

Mode C should count a standard as applied when either the body or the "Checks run" list shows it.

As I understand the protocol, I draft without the workbench's other capabilities. So no harness checks appear in the draft (see `bs:Q1`).

## 1. Corrections to what you recorded

Section 1 is right, with one exception:
- **PRA.2.** Change it as I set out under `bs:T4` below. The higher burden attaches to the form of a claim ("rules out", "overturns"), whichever account the claim targets, not to what an audience takes for granted.

I agree on the citations: recollection is not verification.

## 2. The 16 standards

I confirm the checkable form of each standard except where I say otherwise.

**`std:1`. Rewrite (b).**
- (b) "Defended" means argued to be true of the setting. For the assumption that does the work, convenience doesn't count, and neither does an "as if" defence. (This promotes the EPI.1 setting.)

**`std:2`. Rewrite (d); add (e).**
- (d) Add at the end: "...tested on evidence other than the failure the mechanism was introduced to explain."
- (e) A prediction fails when either of two things holds:
  - the estimate has the opposite sign, and its interval excludes zero; or
  - the interval rules out any effect in the predicted direction that is large enough to matter (as in `std:13`).

  An estimate that is merely imprecise is reported as "not supported", not as a failure, and the paper says which it is. The same definition applies to the rival's predictions (`std:12`).

**`std:3`. Confirm (a), (b), (d) and (e); (c) as under `bs:T2`; add (f) and (g).**
- (f) Reinterpreting the rival's evidence as the paper's own counts only if the reinterpretation yields a prediction that the rival's reading does not. (This promotes INF.6, the assimilative case.)
- (g) The same discipline applies to the paper's own mechanism, measured against the obvious non-rival explanations of the same correlation. The paper reports at least one implication specific to its mechanism, not only the reduced-form association. (g) is at should priority within this must standard.

**`std:4`. Confirm; define "addressed".** "Addressed" means tested, or given a specific reason why it doesn't apply. Listing it as a limitation doesn't count.

**`std:5`. Confirm (a) and (b); (c) as under `bs:Q1`.**

**`std:6`. Confirm; the minimum check is as under `bs:Q2`.**

**`std:7`. Confirm; add (d) and (e).**
- (d) The regressor and the outcome are not built from shared components, such as a common denominator or the same survey item, that would correlate them by construction.
- (e) Where a measure records adoption and the theory is about use, the paper argues the link between them. (This promotes MI4.)

**`std:8`. Confirm; add one clause; see `bs:Q4`.**
- Added clause: a claim that a practice exists because it serves a function names the selection or feedback mechanism. (This promotes ONT.5.)

**`std:9`. Confirm, including your definition of key regressors (which covers the rival's measure); add (c); see `bs:Q5`.**
- (c) Where key regressors vary at different levels, the paper clusters at the coarsest level, uses two-way clustering, or explains why not.

**`std:10`. Confirm (a), (b) and (d); (c), (e) and (f) as under `bs:T3`; add (g).**
- (g) The paper says how it chose the main specification and reports the specifications that didn't work. (This promotes EPI.5.)

The two citations in (e) match my memory: Callaway and Sant'Anna (2021) and Sun and Abraham (2021), both in the *Journal of Econometrics*. Keep "to verify".

**`std:11`. Confirm; see `bs:Q6`.**

**`std:12`. Confirm; add (d).**
- (d) Wording cuts both ways. Any claim strength the draft rejects in statements about the rival ("ruled out", "fashion"), it also checks in statements about the paper's own account ("economizing", "shows"). See `bs:Q4`.

**`std:13`. Confirm; add to (a); see `bs:Q7`.**
- Added to (a): if I think the standard errors are clustered wrongly (`std:9`), I say that the interval is probably too narrow.

**`std:14`. Confirm; sharpen (a).**
- Added to (a): lagging the peer measure does not by itself separate imitation from shared conditions that persist over time.

I know the brief reports a lagged peer measure in this paper. I'd say the same of any lagged peer measure; it is a standard point in the peer-effects literature. I keep the sentence.

**`std:15`. Confirm; see `bs:Q8`.**

**`std:16`. Confirm.**

## 3. Sharpening questions

**`bs:Q1`: the harness check on the model. Yes, but after the draft, not in it.**
- **In the draft.** Under the protocol I draft without the workbench's other capabilities. So in the draft I re-derive by hand and write each step down, with the assumptions as I read them and page or equation references. A finding in the draft reads "re-derived by hand", not "demonstrated".
- **After the draft.** When I'm shown the workbench outputs, the harness runs my steps.

I accept (c) on two conditions:
- **The domain is stated.** The script states the parameter domain. If a sign holds only on part of the domain, the check says so.
- **The transcription is shown.** The harness verifies my computation, not my transcription of the paper's model. So the transcription must be shown, so that someone can see whether I encoded the model correctly.

If the harness disagrees with my hand derivation, I say so in the revision. The same applies to the approximate intervals in `std:13` and the computations in `std:6`.

**`bs:Q2`: the minimum spot check. Accept, with three additions:**
- N for every table, because it's cheap;
- check (e) for each main effect;
- check (f) for every result that the abstract or the conclusions mention.

For check (d): if the paper doesn't report the covariances, I compute the point marginal effects across the moderator's range, say that I can't give their intervals, and ask for the covariances.

**`bs:Q3`: identifying weight. Accept your rule:** a change in sign, or a change in size that I state in advance. "In advance" means before I read the results section. If I haven't stated a size, my default is a change of a quarter or more in the key coefficient.

**`bs:Q4`: efficiency claims.**
- **"Where efficiency is the conclusion".** Accept, and add the title to the abstract and the conclusions.
- **"Economizing".** My general rule:
  - "Choices are made to economize", meaning they track transaction attributes, is a motive claim: kind (i).
  - "The practice does economize", meaning it lowers costs or is the right response, is an efficiency claim: kind (ii).
  - Where the sentence doesn't say which, classify it as kind (ii), the stronger reading, and ask the authors to say which they mean. The burden of disambiguating is on the author, and `std:3` (e) already says that claims go no further than the design supports.
  - By `std:12` (d), the same rule applies to "fashion" and similar words about the rival. "Adopted for legitimacy" is a motive claim. "Inefficient" is an outcome claim.

**`bs:Q5`: few clusters.** Fewer than 50. Whatever the count, also treat the clusters as few when one or a few of them dominate in size, or when the key regressor varies in only a few of them.

**`bs:Q6`: an argued direction. Accept, with one sharpening.** The reason must be specific to the setting and checkable. Two examples:
- timing: the attribute was fixed before the governance option existed;
- an external driver: a mandate or schedule the firm doesn't control, with evidence that it applied.

"Firms adopt X for other reasons" is an assertion. Evidence that the attribute doesn't respond to lagged governance is identification under (b), not argument under (a).

**`bs:Q7`: proposing a smallest effect. Yes.** When I propose one, I:
- label it as my choice;
- justify it in substantive terms, either relative to the main effect or as a share of the outcome's standard deviation;
- fix it before I look at the interval;
- invite the authors to replace it with a value they justify.

**`bs:Q8`: which objections need (a)–(d). Accept your proposal:** (a)–(d) for fatal and damaging objections, (e) for all objections, and (f) once per draft.

## 4. Tensions

**`bs:T1` (`std:1` versus `std:2`): my own rule.** The failure counts against different things:
- **Against the model as the paper states it** (`std:2`). The paper claimed the prediction, so the paper's model, assumptions included, takes the hit.
- **Not against the broader theory,** if the theory doesn't entail the prediction (`std:1`'s logical point). The under-derivation is itself a must failure under `std:1`, so nothing is rewarded.
- **A repaired derivation is a rescue.** If a repaired derivation flips the predicted sign after the result is known, it falls under `std:2` (d). It counts against the theory unless it yields a further prediction that is tested on other evidence.

**`bs:T2` (judging the rival versus deferring): my own rule, split by standard.**
- **`std:14`: my own verdict.** Separating peer influence from shared conditions is an identification question. It needs only the rival's minimal claim, that peers' adoption causes one's own, not the rival's finer content.
- **`std:3` (c): I judge provisionally (your option a).** I state which definition of the rival's construct I'm using, cite its literature, and flag the point as a question for the second reviewer.
- **`std:12` (c): your option (b).** My draft does not call an institutional account unfalsifiable or untested. If I think the version at issue makes no testable prediction, I put that to the editor as a question for the second reviewer. This also removes the place where my bias would act.

**`bs:T3` (pre-trends as claims of absence): option (a). This raises `std:13` to must for leads.** The intervals on the leads must exclude pre-trends large enough to matter relative to the estimated effect. If they don't, the paper must show that the estimate survives plausible violations of parallel trends, through a sensitivity analysis of the Rambachan and Roth kind.

My past criterion, "if the leads are flat", was looser than the standard I hold now. It should read "flat and precise". Under `std:15` (c), I state in advance what interval on the leads would persuade me. The relevant literature is Roth (2022) on pre-testing, and Rambachan and Roth (2023). Both are from memory and should be marked to verify.

**`bs:T4` (symmetry versus the higher burden): option (a).** Symmetry governs the evidence. The higher burden attaches to the form of a claim, not to the audience. Any claim to have ruled out or overturned *either* account carries it, so the burden is symmetric. Restate PRA.2 accordingly. That removes the need for a rule about what a dual audience takes for granted.

**`bs:T5` (one sentence versus `std:10`): option (b), with a definition of "first-order".** With unit fixed effects, survival selection threatens identification only if survival is related to *changes* in the regressor and the outcome, not to their levels. It is first-order if, on the paper's own numbers, it could plausibly produce an estimate of the reported size. Otherwise I write one sentence. If I go past the sentence, I add a short note to the editor saying why, and I still say nothing about representativeness.

**`bs:T6` (priority versus weight): confirm, with corrections.**
- **Must versus weight.** "Must" means a standard must be applied in the draft. The weight says how much a failure moves the recommendation. Confirmed.
- **Where TEC findings are booked.** A TEC check is a procedure; its finding is booked to the dimension where its consequence lands.
  - A proposition that doesn't follow (`std:5`) is an INF finding, at 0.9.
  - A numerical error or a mis-clustering (`std:6`, `std:9`) that would change a conclusion on which a hypothesis test rests is booked to EPI or INF. That is what "signals something deeper" means.
  - Other TEC failures are minor.
- **Draft standards carry no weight.** `std:12` and `std:15` apply to my draft, not to the paper. Their weights don't move the recommendation; Mode C only checks that they are applied.
- **Over-claiming.** It falls under INF and EPI, as you say. So `std:2` (a) and `std:3` (e) carry the 0.9 weights.

## 5. Promotions and what's missing

I've merged every promotion into an existing standard, so the list stays at 16.

| Setting | Goes into |
|---|---|
| Specification choice | `std:10` (g) |
| Adoption versus use | `std:7` (e) |
| Assimilative reinterpretation | `std:3` (f) |
| Functional explanation | `std:8` |
| No "as if" defence | `std:1` (b) |
| Alternative safeguards | Stays a setting. I'll mention it where it bears; no Mode C check. |

**Missing, now added:**
- a mechanism-specific implication: `std:3` (g), at should priority within the standard;
- no mechanical correlation between regressor and outcome: `std:7` (d);
- asking for inputs a check needs when the paper doesn't report them: the general rule in section 0.

**Shedding order.** The list is now more than I'll get through in an hour on a bad day. If time runs short, I shed in this order:
1. `std:16`;
2. `std:8`;
3. `std:7` beyond the main regressor, the outcome and the rival's construct;
4. `std:6` beyond the `bs:Q2` minimum;
5. `std:3` (g).

I never shed `std:1`, `std:2`, `std:3` (a)–(f), `std:4`, `std:5` or `std:9` to `std:15`. That is consistent with `bs:EB.ann6`, which never cuts N1 to N3.
