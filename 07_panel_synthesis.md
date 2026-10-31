# Run 07: Panel Synthesis

**PANEL SYNTHESIS OF SIMULATED REVIEWS. This is not a review and is never sent to authors.** It organizes four simulated reviews of `ms:TEST` for the focal human reviewer, who decides and signs.

- Role: Role 3, Panel Synthesizer (capability 2). Instruction set: Reviewership v0.1 (23 October 2026). Composes L17 RadianX, L5 Deconstructor (inter), L13 PrisM, Integrate(X,Y), Corroborate(X,Y).
- Manuscript: `ms:TEST`, "Modularity, Not Mimicry: Interoperability Standards and the Diffusion of IT Outsourcing in U.S. Hospitals". **I did not read it.** Every manuscript locus or quotation below is as a simulated review or the focal draft gives it.
- Inputs read in full: `runs/03_simulated_reviewer_TCE.md`, `runs/04_simulated_reviewer_INST.md`, `runs/05_simulated_reviewer_BEH.md`, `runs/06_simulated_reviewer_DID.md`; every `*.out.txt` in `runs/03_checks/` to `runs/06_checks/` (18 files); `runs/02_reviewer_draft.md`; the perspectives and distances in the run file. No other file, no web. No code run, except listing the output files.
- Status conventions. Each simulated finding stays as its reviewer stated it; all are `asserted`. I use harness outputs only to judge whether a disagreement is resolvable (§4). The statistics I derive from the panel's verdicts (§2, §4.3) are `asserted` until `pnl:chk:1` (Annex) runs.
- Ids: `pnl:ctb:n` (aligned contributions), `pnl:srv:n` (survival rows), `pnl:agr:n` (agreements), `pnl:dis:n` (disagreements), `pnl:chk:1` (my check).

**Caveats that bear on the whole synthesis.**

1. *Correlated simulators.* The four simulated reviewers were probably produced by the same model family. The inputs do not say so; this is my inference. Their agreement is therefore weaker evidence than agreement among independent human reviewers. That matters most for recall-based claims (the literature cited "to verify") and least for claims the harness has executed.
2. *Standards.* None of the four simulated perspectives, as configured, carries a `standards` list. R-TCE lists standards "drawn from the configured parameters" (`r-tce:std:1` to `9`). R-INST derives standards and flags them as not configured (`r-inst:std:1` to `7`). R-BEH and R-DID list none. When I trace a disagreement to a parameter, I mean the parameter as that simulator applied it.
3. *Focal normalization.* `persp:FOCAL` was normalized for the distance computation, with conditional settings mapped to unconditional values (its `note`). Distances to FOCAL are therefore approximate.

## 0. Harness outputs read (provenance)

| Folder | Output file | Check | Ran | Note |
|---|---|---|---|---|
| 03_checks | `r-tce_chk_1.out.txt` | `r-tce:chk:1` | yes, exit 0 | |
| 03_checks | `r-tce_chk_1_b2.out.txt` | `r-tce:chk:2` (file headed `r-tce:chk:1`) | yes, exit 0 | **label anomaly** |
| 03_checks | `r-tce_chk_3.out.txt`, `r-tce_chk_4.out.txt` | `r-tce:chk:3`, `r-tce:chk:4` | yes, exit 0 | |
| 04_checks | `r-inst_chk_1.out.txt` to `r-inst_chk_3.out.txt` | `r-inst:chk:1` to `3` | yes, exit 0 | |
| 05_checks | `r-beh_chk_1.out.txt`, `r-beh_chk_2.out.txt` | `r-beh:chk:1`, `2` | yes, exit 0 | |
| 05_checks | `r-beh_chk_3.out.txt`, `r-beh_chk_4.out.txt` | `r-beh:chk:3`, `4` | exit 0, **empty output** | scripts only define functions that need the authors' panel |
| 06_checks | `r-did_chk_1.out.txt` to `r-did_chk_7.out.txt` | `r-did:chk:1` to `7` | yes, exit 0 | |

Two anomalies:

- `r-tce_chk_1_b2.out.txt` is headed `r-tce:chk:1`, but its content is the printout that the code of `r-tce:chk:2` produces (the sign of the interaction on the Φ scale, by spending distribution). I treat it as the output of `r-tce:chk:2`. The label should be corrected before anyone cites it.
- `r-beh:chk:3` and `r-beh:chk:4` tested nothing. Their targets stay open: the magnitude in `r-beh:fnd:2`, and the aspiration commitment `r-beh:cmt:24`.

## 1. Contribution alignment

The four reviews list seven contributions each, cut differently. The common list has eight.

| Id | Common statement | Merges | Alignment |
|---|---|---|---|
| `pnl:ctb:1` | A closed-form TCE model of modularity and make-or-buy, with Prop. 1 (∂k*/∂m > 0) and Prop. 2 (∂²k*/∂m∂u > 0) | `r-tce:ctb:1`, `r-inst:ctb:1`, `r-beh:ctb:1`, `r-did:ctb:1` | clean |
| `pnl:ctb:2` | A test of the propositions against an institutional rival on a 2009-2019 hospital panel (H1-H3) | `r-tce:ctb:2`, `r-inst:ctb:2`, `r-beh:ctb:2`, `r-did:ctb:2` | clean. R-DID moves the causal reading to `r-did:ctb:4` (see call c) |
| `pnl:ctb:3` | Once modularity is measured, the apparent peer effects "disappear" | `r-tce:ctb:3`, `r-inst:ctb:3`, `r-beh:ctb:3` (first half), `r-did:ctb:3` (first half) | **judgement call (a)** |
| `pnl:ctb:4` | The results "rule out mimetic isomorphism" in this setting | `r-tce:ctb:6` (first half), `r-inst:ctb:4` (first half), `r-beh:ctb:3` (its `alsoAvowedAs`), `r-did:ctb:3` (second half) | **judgement calls (a), (b)** |
| `pnl:ctb:5` | A practice "often read as institutional fashion is, on closer inspection, economizing"; standards, through modularity, widened outsourcing | `r-tce:ctb:6` (second half), `r-inst:ctb:4` (second half), `r-beh:ctb:5`, `r-did:ctb:4` | **judgement calls (b), (c)** |
| `pnl:ctb:6` | Specificity is partly a product of interface design, so firm boundaries respond to standards | `r-tce:ctb:5`, `r-inst:ctb:6`, `r-beh:ctb:4`, `r-did:ctb:5` | clean |
| `pnl:ctb:7` | Priority: "the first study to adjudicate directly" between TCE and institutional explanations | `r-tce:ctb:4`, `r-inst:ctb:5`, `r-beh:ctb:6`, `r-did:ctb:6` | clean |
| `pnl:ctb:8` | Practice: leaders "should attend first to the modularity of their systems" | `r-tce:ctb:7`, `r-inst:ctb:7`, `r-beh:ctb:7`, `r-did:ctb:7` | clean |

Judgement calls:

- **(a)** R-TCE and R-INST list "disappear" and "rule out" separately. R-BEH (`r-beh:ctb:3`) and R-DID (`r-did:ctb:3`) bundle them. I split them and apply R-BEH's and R-DID's single verdict to both rows.
- **(b)** R-TCE (`r-tce:ctb:6`) and R-INST (`r-inst:ctb:4`) bundle "economizing" with "rule out". I apply their single verdicts to both `pnl:ctb:4` and `pnl:ctb:5`.
- **(c)** R-BEH's `r-beh:ctb:5` leads with a weaker modal claim ("may reflect the common adoption of efficiency-enhancing technologies"). R-DID's `r-did:ctb:4` couples "economizing" with the causal claim of ms:S5. I merge both into `pnl:ctb:5`.

These calls move the scores of `pnl:ctb:3` and `pnl:ctb:5` only (§2, notes).

## 2. Survival table

Score: survives 1, qualified 0.5, fails 0, averaged over the four reviewers. **Robust**: survives or qualified for every reviewer. **Lens-dependent**: survives only for reviewers whose perspectives are close. I treat two perspectives as close when their overall distance is at most 0.40. Among the simulated reviewers, only R-TCE/R-DID (0.36) qualifies. This threshold is a judgement call; raising it to 0.45 changes no classification.

R-INST gives verdicts by contribution id without `vrd` ids, so its cells cite `r-inst:ctb:n`.

| Row | Contribution | R-TCE | R-INST | R-BEH | R-DID | Score | Classification |
|---|---|---|---|---|---|---|---|
| `pnl:srv:1` | `pnl:ctb:1` model, Props 1-2 | qualified (`r-tce:vrd:1`) | qualified (`r-inst:ctb:1`) | qualified (`r-beh:vrd:1`) | qualified (`r-did:vrd:1`) | 0.50 | **robust** |
| `pnl:srv:2` | `pnl:ctb:2` test against the rival | qualified (`r-tce:vrd:2`) | qualified (`r-inst:ctb:2`) | qualified (`r-beh:vrd:2`) | qualified (`r-did:vrd:2`) | 0.50 | **robust** |
| `pnl:srv:3` | `pnl:ctb:3` peer effects "disappear" | qualified (`r-tce:vrd:3`) | qualified (`r-inst:ctb:3`) | fails (`r-beh:vrd:3`) | fails (`r-did:vrd:3`) | 0.25 | neither |
| `pnl:srv:4` | `pnl:ctb:4` "rule out mimetic isomorphism" | fails (`r-tce:vrd:6`) | fails (`r-inst:ctb:4`) | fails (`r-beh:vrd:3`) | fails (`r-did:vrd:3`) | 0.00 | neither: **fails for every reviewer** |
| `pnl:srv:5` | `pnl:ctb:5` "economizing" | fails (`r-tce:vrd:6`) | fails (`r-inst:ctb:4`) | qualified (`r-beh:vrd:5`) | fails (`r-did:vrd:4`) | 0.125 | neither (qualified for one lens only) |
| `pnl:srv:6` | `pnl:ctb:6` specificity by design | qualified (`r-tce:vrd:5`) | **survives** (`r-inst:ctb:6`) | qualified (`r-beh:vrd:4`) | qualified (`r-did:vrd:5`) | 0.625 | **robust** |
| `pnl:srv:7` | `pnl:ctb:7` priority | fails (`r-tce:vrd:4`) | qualified, uncertain (`r-inst:ctb:5`) | fails, provisional (`r-beh:vrd:6`) | qualified (`r-did:vrd:6`) | 0.25 | neither |
| `pnl:srv:8` | `pnl:ctb:8` practice implication | qualified (`r-tce:vrd:7`) | qualified (`r-inst:ctb:7`) | qualified (`r-beh:vrd:7`) | fails (`r-did:vrd:7`) | 0.375 | neither |

Notes.

- **No contribution is lens-dependent.** Where verdicts split, the reviewers who let the contribution stand are far apart, not close. `pnl:ctb:3` stands for R-TCE and R-INST (0.68, the farthest pair). `pnl:ctb:7` stands for R-INST and R-DID (0.65). `pnl:ctb:8` stands for every reviewer except R-DID. `pnl:ctb:5` is qualified for R-BEH alone, and only in a form that drops the efficiency claim: "the behavioral re-voicing claims only that feasible alternatives changed" (`r-beh:vrd:5`).
- **What survives, in the reviewers' converging narrowed forms.** For `pnl:ctb:1`: Prop. 1 holds, and Prop. 2 holds only with its sign reversed under A3. R-INST and R-DID add that neither sign carries over to Φ without an assumption on the distribution of k. For `pnl:ctb:2`: H1 holds as a within-hospital association, and the test against the rival does not discriminate. For `pnl:ctb:6`: the idea stands, but its novelty is contested (§4, `pnl:dis:16`), and all four say its empirical premise, that m lowers measured specificity, is not shown.
- **Alignment sensitivity.** For their bundled ctb:3, R-BEH and R-DID state surviving remnants that coincide with R-TCE's and R-INST's narrowed forms: the peer coefficient is "smaller (0.137 to 0.042) and imprecisely estimated" (`r-beh:vrd:3`; `r-did:vrd:3`). I do not re-score their verdicts. `pnl:chk:1` reports the scores both ways. The `pnl:ctb:3` split is recorded as `pnl:dis:13`.

## 3. Agreement

Each row is a finding that two or more reviewers raise about the same locus for the same reason. Severity abbreviations: F = fatal, D = damaging, Fx = fixable, M = minor; "within F" means the point is part of a compound finding rated fatal. Every listed finding is `asserted`, as its reviewer stated it. The last column says whether the focal draft has it.

| Id | Locus | Shared finding | Raised by (severity) | Highest | In draft |
|---|---|---|---|---|---|
| `pnl:agr:1` | ms:Prop2; ms:Appendix; ms:A3 | The proof of Prop. 2 treats H(u) as constant in u. With H′(u) = h1, the cross-partial is [g1h0 − h1(s+g0)]/[H²(1−m)²], which is negative under A3 | `r-tce:fnd:1` D; `r-inst:fnd:8` D; `r-beh:fnd:9` D; `r-did:fnd:7` D | damaging | yes |
| `pnl:agr:2` | ms:S2.4 | There is no aggregation step from the threshold k* to the share Φ. The sign of the interaction on Φ depends on the spending distribution F, and Φ hits a ceiling at k* ≥ 1 | `r-tce:fnd:2` Fx; `r-inst:fnd:3` Fx; `r-beh:fnd:10` Fx; `r-did:fnd:8` Fx | fixable | yes |
| `pnl:agr:3` | ms:S3.2 Modularity; ms:S2.1 | m is measured over clinical systems only, but Φ covers all IT functions, including hosting and help desk | `r-tce:fnd:10` Fx; `r-inst:fnd:3` Fx | fixable | **no** |
| `pnl:agr:4` | ms:Abstract; ms:S5 para 1; ms:T2.M2.Peer | "Rule out" infers absence from non-significance (MI7, which all four reject). The 95% CI is about [−0.03, 0.12], and no equivalence test is reported | `r-tce:fnd:4` D; `r-inst:fnd:7` F (fixable if narrowed); `r-beh:fnd:4` F (to that claim); `r-did:fnd:2` F | **fatal** | yes |
| `pnl:agr:5` | ms:S2.4 last para; ms:S4 H3 | The H3 criterion does not discriminate. Modularity may carry imitation or institutional diffusion, so conditioning on it removes the peer coefficient by construction | `r-tce:fnd:5`(a) D; `r-inst:fnd:7`(b)2 within F; `r-beh:fnd:4` within F; `r-beh:fnd:12` D; `r-did:fnd:2`(ii) within F; `r-did:fnd:10` M | fatal (within compounds) | yes |
| `pnl:agr:6` | ms:S3.2 Peer outsourcing; ms:S1 | The same-state lagged mean of sample hospitals is not the referent set the rival names (peers "perceived as legitimate or successful") | `r-tce:fnd:5`(b) D; `r-inst:fnd:2` D; `r-beh:fnd:3`(a) D; `r-did:cmt:19` challenged (construct issues rated minor, r-did §8) | damaging | partial (provisional) |
| `pnl:agr:7` | ms:S3.2; ms:S3.3 | The state-year peer mean is exposed to the reflection problem (Manski 1993, to verify), to state-level correlated shocks including the mandates, and to noise from thin state cells | `r-tce:fnd:5`(c) D; `r-inst:fnd:2`(iii-iv) D; `r-beh:fnd:19` Fx; `r-did:fnd:2`(iii) within F | fatal (within compound) | partial |
| `pnl:agr:8` | ms:S2.4; ms:H3 | Only the mimetic mechanism is stated. The coercive (mandates) and normative pathways are not, and neither is imitation conditional on uncertainty or adoption stage | `r-inst:fnd:1` D; `r-inst:fnd:7`(b)3 within F; `r-beh:fnd:12` D; `r-tce:fnd:5`(a) D | damaging | partial |
| `pnl:agr:9` | ms:S3.3 | Reverse causation: vendors may install certified interfaces when they take over functions, and hospital fixed effects do not address this | `r-tce:fnd:6` D; `r-beh:fnd:5` D; `r-did:fnd:1` F | fatal | yes |
| `pnl:agr:10` | ms:S3.3 | Year fixed effects do not absorb time-varying shocks: hospital-specific timing of the EHR incentive programme, or state mandates | `r-tce:fnd:6` D; `r-inst:fnd:13` Fx; `r-did:fnd:1`(b) F | fatal | yes (minor) |
| `pnl:agr:11` | ms:S3.2 staffing; ms:S3.3; ms:T2.M4 | Outsourcing moves in-house staffing, so staffing is a bad control, and "cannot be attributed to capability" is unentitled | `r-tce:fnd:7` D; `r-inst:fnd:14` Fx; `r-beh:fnd:18` D; `r-did:fnd:3` Fx | damaging | yes |
| `pnl:agr:12` | ms:S4 Robustness | The event study uses TWFE under staggered adoption, is unreported, is a reduced form with no first stage, and leaves the exclusion restriction unargued | `r-tce:fnd:8` Fx; `r-inst:fnd:13` Fx; `r-inst:fnd:15` Fx; `r-beh:fnd:5` D; `r-did:fnd:4` D | damaging | yes |
| `pnl:agr:13` | ms:S3.3 | Standard errors are clustered by hospital although the peer measure and the mandates vary by state | `r-tce:fnd:8`(d) Fx; `r-inst:fnd:15` Fx; `r-beh:fnd:19` Fx; `r-did:fnd:11` Fx | fixable | yes |
| `pnl:agr:14` | ms:S2.2; ms:S3.2 specificity; ms:T2 | β1 stays positive with the specificity rating controlled, and that rating's coefficient barely moves (−0.094 to −0.091). If the rating measures effective specificity k(1−m), the model implies β1 ≈ 0, or the control is a mediator. That m lowers specificity is not shown | `r-tce:fnd:9` D; `r-inst:fnd:10`(ii) D; `r-beh:fnd:14` D; `r-did:fnd:12` Fx | damaging | partial |
| `pnl:agr:15` | ms:S5 para 2 | The legitimacy account is an unlabelled post hoc abduction outside the model. It clashes with "Its substance is economizing" and is unnecessary once Prop. 2 is corrected | `r-tce:fnd:3` Fx; `r-inst:fnd:9` D; `r-beh:fnd:11` D; `r-did:fnd:9` Fx | damaging | yes |
| `pnl:agr:16` | ms:Abstract; ms:S6 | "Economizing" is unentitled without cost, quality or hold-up outcomes; the step from fit to efficiency is MI9 | `r-inst:fnd:10`(i) D; `r-beh:fnd:1` D | damaging | yes (by another route) |
| `pnl:agr:17` | ms:Abstract; ms:S1 | The priority claim is unchecked. All four name Loh & Venkatraman 1992 and Ang & Cummings 1997 (both to verify) | `r-tce:fnd:15` Fx; `r-inst:fnd:4` D (for the contribution); `r-beh:fnd:15` Fx; `r-did:fnd:18` M | damaging | partial |
| `pnl:agr:18` | ms:S3.1; ms:T2 | N = 4,712, but 412 × 11 = 4,532 (and 4,120 if the lag costs 2009) | `r-tce:fnd:13` Fx; `r-inst:fnd:16` M; `r-beh:fnd:20` Fx; `r-did:fnd:5` Fx | fixable | yes |
| `pnl:agr:19` | ms:T2.M3.uncertainty | 0.084 (0.051) is marked *** at t ≈ 1.65 | `r-tce:fnd:13` Fx; `r-inst:fnd:16` M; `r-beh:fnd:20` Fx; `r-did:fnd:6` M | fixable | yes |
| `pnl:agr:20` | ms:Abstract | "Strongly predicts" describes about 0.16 SD per SD | `r-tce:fnd:14` M; `r-inst:fnd:16` M; `r-beh:fnd:7` Fx; `r-did:fnd:14` M | fixable | **no** |
| `pnl:agr:21` | ms:S3.1-3.2 | One informant, the CIO, supplies m, specificity and Φ | `r-tce:fnd:16` M; `r-inst:fnd:11` Fx; `r-beh:fnd:6` Fx; `r-did:fnd:20` M | fixable | partial |
| `pnl:agr:22` | ms:S3.2 Modularity | Reported certification may be formal adoption, decoupled from working interoperability (MI4) | `r-inst:fnd:11` Fx; `r-beh:fnd:3`(b) within D | damaging (within compound) | **no**; the draft's std:7 check takes the contrary view |
| `pnl:agr:23` | ms:S3.1 | Including only hospitals that responded in every year selects on survival and response, perhaps on the outcome | `r-tce:fnd:16` M; `r-inst:fnd:12` Fx; `r-beh:fnd:6` Fx; `r-did:fnd:15` Fx | fixable | yes |
| `pnl:agr:24` | ms:S3.2 uncertainty; ms:S2.2 | Admissions volatility is not the model's adaptation uncertainty. R-TCE adds that the standardized u takes negative values, whereas the model needs u ≥ 0 | `r-tce:fnd:11` Fx; `r-beh:fnd:3`(c) within D; `r-did:fnd:16` M | damaging (within compound) | **no** |
| `pnl:agr:25` | ms:T2.M3; ms:S2.3 | The corrected model implies that uncertainty lowers Φ at every m, but Table 2's uncertainty effect is positive (and imprecise) | `r-beh:fnd:21` Fx; `r-did:chl:6` (a challenge) | fixable | yes |
| `pnl:agr:26` | ms:S5.1 | The practice implication presupposes the causal claim | `r-tce:fnd:17` M; `r-inst:fnd:6` M; `r-beh:fnd:17` M; `r-did:fnd:19` M | minor | **no** |
| `pnl:agr:27` | (no availability statement) | No data or code availability statement | `r-inst:fnd:17` M; `r-beh:fnd:22` Fx; `r-did:fnd:13` Fx; repair in `r-tce:fnd:8` | fixable | yes |

Agreed strengths, repairs and probes (Corroborate across lenses):

| Id | Kind | Shared content | Raised by | In draft |
|---|---|---|---|---|
| `pnl:agr:28` | strength | Prop. 1 and its proof are correct | `r-tce:str:3`; `r-inst:fnd:8`; `r-beh:cmt:4`; `r-did:cmt:1` | yes |
| `pnl:agr:29` | strength | H1 is a credibly estimated within-hospital association, stable across Models 2-4 | `r-tce:cmt:7`; r-inst §7; r-beh §7; `r-did:vrd:2` | yes |
| `pnl:agr:30` | strength | Correcting Prop. 2 makes the legitimacy account unnecessary, a repair that helps the authors | `r-tce:fnd:1`; `r-inst:fnd:8`; `r-beh:fnd:9`; `r-did:fnd:7` | partial |
| `pnl:agr:31` | repair | The staggered state requirements are the paper's best route to identification: first stage, heterogeneity-robust estimator, state clustering | `r-tce:fnd:6`, `r-tce:fnd:8`; `r-inst:fnd:13`; `r-beh:fnd:5`; `r-did:fnd:1`, `r-did:fnd:4` | yes |
| `pnl:agr:32` | probe | Function-level analysis is the most discriminating test available | r-tce §5 (obs. 3, L12); r-inst §5 obs. 1; r-beh step 5; `r-did:rival:1` obs. 2 | yes (see the caveat at `pnl:dis:15`) |
| `pnl:agr:33` | probe | Timing: does m rise before or after outsourcing, or vendor contracts? | r-tce §5 obs. 1; r-inst §5 obs. 3; `r-beh:fnd:5` repair; `r-did:rival:1` obs. 1 | yes (leads of modularity) |

All four rivals have the same structure: modularity and outsourcing determined together. They are `r-tce:alt:1` (joint choice, or a production-cost channel), the r-inst §5 field-template bundle, the r-beh step 5 problemistic search, and `r-did:rival:1` (vendor-led bundling). That is why `pnl:agr:32` and `pnl:agr:33` recur across the panel.

## 4. Disagreement map

### 4.1 Summary

| Id | Topic | Split | Classification | Parameters, or what settles it |
|---|---|---|---|---|
| `pnl:dis:1` | How grave is the unentitled "rule out mimetic isomorphism"? | R-TCE damaging; R-INST, R-BEH, R-DID fatal | fault line | INF.2 MI3; PRA.1; PRA.2 |
| `pnl:dis:2` | How grave is the unentitled causal reading of β1? | R-DID fatal; R-TCE, R-BEH damaging; R-INST fixable | fault line | INF.2 MI6; EPI.3; EPI weight |
| `pnl:dis:3` | Does the corrected Prop. 2 make the negative interaction corroboration? | R-BEH yes (conditional); R-TCE moderate; R-DID accommodation | fault line (resolvable part settled) | EPI.4; EPI.5 (pre-registration); EPI.2 |
| `pnl:dis:4` | Do model and data agree on every sign once Prop. 2 is corrected? | R-TCE yes; R-BEH, R-DID no | **resolvable** | harness on k*_u, plus Table 2 |
| `pnl:dis:5` | Are standards a technological shift parameter or a field-level institution? | R-INST (and R-BEH via the manuscript's typology) vs R-TCE, R-DID | fault line | ONT.3; ONT.1; INF.6; INF.2 MI8 |
| `pnl:dis:6` | Does fit to comparative statics entitle "economizing"? | R-TCE yes (MI9); R-INST, R-BEH no | fault line | INF.2 MI9, MI2; ONT.5 choice-theoretic |
| `pnl:dis:7` | How much does the peer measure's construct validity matter? | R-TCE, R-INST, R-BEH damaging; R-DID minor | fault line | ONT.4; ONT weight |
| `pnl:dis:8` | How grave is the staffing bad control? | R-TCE, R-BEH damaging; R-INST, R-DID fixable | idiosyncratic | allocation of one defect between findings |
| `pnl:dis:9` | How grave are the event-study defects? | R-DID, R-BEH damaging; R-TCE, R-INST fixable | fault line | EPI.3; INF.2 MI6; TEC weight |
| `pnl:dis:10` | Is the specificity control a failed mechanism or an estimator bias? | R-TCE, R-INST, R-BEH damaging; R-DID fixable | fault line | ONT weight; EPI.3 (total effect as estimand) |
| `pnl:dis:11` | How grave is the legitimacy account? | R-INST, R-BEH damaging; R-TCE, R-DID fixable | fault line (with an idiosyncratic residue) | INF.2 MI10; ONT.1 |
| `pnl:dis:12` | Does the priority claim fail or qualify? | R-TCE, R-BEH fail; R-INST, R-DID qualified | **resolvable** (verdict); fault line (severity) | literature verification; PRA.3; PRA weight |
| `pnl:dis:13` | Verdict on `pnl:ctb:3` | R-TCE, R-INST qualified; R-BEH, R-DID fail | idiosyncratic | how the contribution was cut |
| `pnl:dis:14` | Verdict on `pnl:ctb:8` | R-DID fails; the others qualified; all rate the finding minor | idiosyncratic | verdict convention |
| `pnl:dis:15` | What can a function-level test discriminate? | R-TCE and R-DID "placebo"; R-INST "sharpest test"; R-TCE's own production-cost variant | **resolvable** | closer reading of the reviewers' own predictions |
| `pnl:dis:16` | How novel is "specificity is partly a product of interface design"? | R-INST survives; R-TCE, R-BEH anticipated; R-DID untested | fault line | PRA.2; ONT.3 |
| `pnl:dis:17` | Does the design explain the field-level diffusion it names? | R-BEH damaging; R-TCE minor; others silent | **resolvable** with the authors' data | decomposition (`r-beh:chk:3`, not yet run on data) |
| `pnl:dis:18` | What is the smallest peer effect of interest? | R-TCE ≈ 0.068; R-INST ≈ 0.046; R-DID ≈ ±0.03; R-BEH unstated | idiosyncratic | no parameter sets the bound |

### 4.2 Entries

Each entry records the moves (L17 RadianX) and the classification (L5 Deconstructor, inter). Where a harness output bears on the question, I cite it only to judge whether the disagreement is resolvable.

**`pnl:dis:1`. Gravity of "rule out mimetic isomorphism". Fault line.**
- The moves: R-TCE rates it damaging (`r-tce:fnd:4`, `r-tce:fnd:5`). R-INST rates it fatal for the central claim, falling to fixable if the claim is narrowed (`r-inst:fnd:7`). R-BEH rates it fatal to that claim but not to H1 (`r-beh:fnd:4`). R-DID rates it fatal, becoming a fixable presentation matter if the claim is narrowed (`r-did:fnd:2`; r-did §6).
- What all four share: they reject MI7, and they cite the same interval and the same mediation concern (`pnl:agr:4`, `pnl:agr:5`).
- The parameters: INF.2 MI3. R-TCE rejects MI3, so for it "the Model 1 peer correlation was never evidence of imitation in the first place" (`r-tce:fnd:5`, repair). R-INST endorses MI3 and puts the burden on the authors (`r-inst:cmt:21`). PRA.1 and PRA.2 also differ. R-TCE addresses strategy and organizational economics in a gap-spotting mode, where the model and H1 are the contribution. R-INST addresses organizational sociology in a problematizing mode, where "Not Mimicry" is the claim addressed to it.
- Residue: the severity scale ties `fatal` to "the central claim", and the manuscript offers two candidates for that role. Which one is central is a reading the reviewer must make (R-BEH's decision 2 says so).
- Harness: the interval and equivalence outputs (`r-tce:chk:3`, `r-inst:chk:2`, `r-beh:chk:2`, `r-did:chk:4`) agree. The 95% CI is about [−0.033, 0.117]. The smallest equivalence bound passable at 5% is about 0.104, 0.76 of the Model 1 estimate. They contradict no reviewer's numbers, so no check resolves this disagreement.

**`pnl:dis:2`. Gravity of the causal reading. Fault line.**
- The moves: R-DID rates it fatal (`r-did:fnd:1`), R-TCE damaging (`r-tce:fnd:6`), R-BEH damaging (`r-beh:fnd:5`), R-INST fixable (`r-inst:fnd:13`).
- The parameters: INF.2 MI6. R-TCE endorses it, conditional on an argument against time-varying confounding (`r-tce:std:7`); R-DID rejects it; R-INST and R-BEH are neutral. EPI.3: R-DID admits design-based identification only, while R-TCE also admits model-based. EPI weight: R-DID 1.0, R-INST 0.6. R-DID's self-location names this parameter as decisive.
- R-TCE and R-DID are the closest pair in the panel (0.36), and this is their largest severity gap. No check bears on it.

**`pnl:dis:3`. Corroboration or accommodation? Fault line, with a resolvable component now settled.**
- The moves: R-TCE gives the corrected sign corroborating weight that is "real but moderate" (`r-tce:fnd:1`), and says that, corrected, "model and data agree on all signs" (`r-tce:str:4`). R-BEH says it "would count as corroboration rather than accommodation, provided the step to the Phi scale is made" (`r-beh:fnd:8`). R-DID says "a design-based reader will treat the interaction result as accommodation" (`r-did:fnd:7`). R-INST calls the legitimacy story "redundant, not vindicated" and takes no position on corroboration (`r-inst:fnd:8`).
- *Resolvable component:* does the corrected model predict a negative interaction on Φ, the scale tested? The harness outputs say: not without an assumption on F. Under A3, the Φ-scale cross-partial is negative for uniform and Beta(5,2) spending distributions and positive for Beta(2,5) and Beta(1,3); Beta(2,2) is mixed (`r-tce:chk:2` output, in `r-tce_chk_1_b2.out.txt`; `r-inst:chk:3`; `r-did:chk:5`; decomposition confirmed by `r-beh:chk:1`(c)). This fits the curvature condition in `r-beh:fnd:10`.
- So R-BEH's claim stands as stated, a conditional whose antecedent the manuscript does not supply. R-TCE's "agree on all signs" (`r-tce:str:4`) goes beyond R-TCE's own `r-tce:fnd:2` on this point.
- *Fault-line residue:* grant such an assumption. Does a sign implied by a stated assumption (A3), but derived only after the results were seen, count as a novel prediction? The parameters involved are EPI.4 (R-TCE high, R-BEH medium, R-DID low), EPI.5 pre-registration (R-DID only) and EPI.2 (R-TCE sophisticated falsificationism; R-BEH and R-DID inductivism).
- The positions do not order by EPI.4 alone. What separates them is the conception of novelty: logical implication by a prior assumption, or temporal priority. The schema does not encode that as a parameter (my inference).

**`pnl:dis:4`. Do all signs agree once Prop. 2 is corrected? Resolvable.**
- The moves: R-TCE says yes (`r-tce:str:4`; `r-tce:cmt:20`). R-BEH says no: the corrected model implies dΦ/du ≤ 0 at every m, while Table 2 implies about +0.056 at mean m (`r-beh:cmt:22`; `r-beh:fnd:21`, fixable). R-DID asks the authors to reconcile the sign (`r-did:chl:6`; `r-did:cmt:5`). R-INST is silent.
- Harness, on the model side: `r-beh:chk:1` finds k*_u < 0 in every A3 draw, and `r-did:chk:1` shows the numerator of k*_u is g1h0 − h1(s+g0). With Φ = F(k*) and F non-decreasing, dΦ/du = F′(k*)k*_u ≤ 0 whatever F is. That last step is argued (`r-beh:cmt:22`), not run.
- Harness, on the data side: `r-beh:chk:2` reproduces the implied +0.056 at mean m. The reported point estimates therefore do not agree with the corrected model on the sign of the uncertainty effect, and `r-tce:str:4` is wrong on this point.
- What stays open: whether the uncertainty effect differs from zero. Its main-effect t is about 1.65. All four star checks find the *** marker inconsistent with that t, and `r-did:chk:2` finds it inconsistent under every admissible rounding. The precision of the effect at mean m needs the covariance of the two coefficients. The u measure is also standardized, while the model needs u ≥ 0 (`r-tce:chl:11`).
- Probe: ask the authors for the marginal effect of u across the range of m, with intervals, on a non-negative u.

**`pnl:dis:5`. Standards: a technological shift parameter, or an institution? Fault line.**
- The moves: R-INST says standards, certification and mandates are institutions. The explanans is then partly institutional, so the contrast holds only against mimetic isomorphism (`r-inst:fnd:1`, damaging; `r-inst:inc:3`). R-BEH reaches the coercive classification from the manuscript's own citation of DiMaggio & Powell (`r-beh:cmt:27`) and proposes an assimilative reframing (`r-beh:fnd:13`, fixable).
- R-TCE assimilates the idea as "a special case of the TCE claim that standardization reduces asset specificity" (`r-tce:vrd:5`), and treats mandates as a mediation problem in the test (`r-tce:fnd:5`(a)). R-DID treats mandates as correlated shocks and as a candidate instrument (`r-did:fnd:2`(iii); `r-did:fnd:1`, repair), and is neutral on MI8 (`r-did:vrd:5`).
- The parameters: ONT.3 (R-INST constitutive; the others individual-mechanistic), ONT.1 (R-INST admits fields, logics and legitimacy; R-TCE admits technologies and artifacts), INF.6 (R-TCE accepts assimilation; R-INST marks its own assimilative move suspect) and INF.2 MI8 (R-TCE endorses). R-INST's self-location predicts this split.
- R-BEH's route needs no constitutive ontology. That part is a reading the reviewer can check against ms:S1 and ms:S4.
- Consequence: the narrowed claims diverge. R-TCE: "diffusion that looks mimetic can be accounted for by economizing on changed transaction attributes" (`r-tce:vrd:6`). R-INST and R-BEH: complementarity, in which field-level rules reconstitute specificity and organizations then economize.

**`pnl:dis:6`. "Economizing". Fault line.**
- The moves: R-TCE holds that, once Prop. 2 is corrected, observed shares are optimal responses by MI9 (`r-tce:cmt:20`, argued), though the hold-up channel is still unshown (`r-tce:cmt:19`, challenged). R-INST rejects MI9 and asks for outcome evidence (`r-inst:fnd:10`, damaging). R-BEH rejects MI9 and MI2 and marks the choice-theoretic model class suspect (`r-beh:fnd:1`, damaging). R-DID, neutral on MI9, fails the claim on design grounds (`r-did:vrd:4`).
- The parameters: INF.2 MI9 and MI2, and ONT.5 for choice-theoretic models (R-TCE preferred; R-INST and R-BEH suspect; R-DID admissible).

**`pnl:dis:7`. Construct validity of the peer measure. Fault line.**
- The moves: R-TCE, R-INST and R-BEH rate it damaging (`r-tce:fnd:5`(b); `r-inst:fnd:2`; `r-beh:fnd:3`(a)). R-DID rates construct issues minor (`r-did:cmt:19`; r-did §8).
- The parameters: ONT.4 (strict and moderate, against R-DID's loose) and ONT weight (0.6 to 0.9, against 0.3). R-DID's self-location predicts this.
- R-DID raises the identification side of the same measure, reflection and correlated effects, inside a fatal finding (`r-did:fnd:2`(iii)). The split is over which property of the measure matters, not over whether the measure is adequate.

**`pnl:dis:8`. The staffing bad control. Idiosyncratic.**
- The moves: R-TCE (`r-tce:fnd:7`) and R-BEH (`r-beh:fnd:18`) rate it damaging. R-INST (`r-inst:fnd:14`) and R-DID (`r-did:fnd:3`) rate it fixable.
- The premise is shared. The harness outputs on it agree with all four: with no true effect, the coefficient stays clearly non-zero after the staffing control. It moves to 0.166 in `r-tce:chk:4` and to 0.065 in `r-did:chk:6`, scenario A, in opposite directions, as "unknown direction" predicts. No check settles the severity.
- The difference is one of allocation. R-TCE and R-BEH treat Model 4 as the paper's only answer to capability confounding. R-DID folds that question into `r-did:fnd:1`. R-INST notes that "Models 2 and 3 do not depend on it".
- It does not trace to TEC.3: R-DID holds the strictest TEC.3 and rates it lowest.

**`pnl:dis:9`. Event-study defects. Fault line.**
- The moves: R-DID rates them damaging (`r-did:fnd:4`). R-BEH rates them damaging inside `r-beh:fnd:5`, together with reverse causation. R-TCE (`r-tce:fnd:8`) and R-INST (`r-inst:fnd:13`, `r-inst:fnd:15`) rate them fixable.
- The parameters: EPI.3 and MI6. For R-DID the mandate event study is the only candidate design; for R-TCE, which endorses MI6, it is supplementary. TEC weight also differs (1.0 against 0.7 and 0.3).
- `r-did:chk:7` bears on the shared premise, not on severity: static TWFE recovers about a fifth of the true ATT (0.031 against 0.165).

**`pnl:dis:10`. The specificity control: a failed mechanism, or an estimator bias? Fault line.**
- The moves: R-TCE, R-INST and R-BEH rate it damaging. If the rating measures effective specificity, the model implies β1 ≈ 0 conditional on it, and β1 is not zero, so the hold-up channel is not evidenced (`r-tce:inc:5`, `r-inst:inc:5`, `r-beh:inc:5`). R-DID rates it fixable: the control is a mediator that biases β1 toward the direct effect, so the models should be reported without it (`r-did:fnd:12`).
- The parameters: R-DID's ONT weight (0.3) and EPI.3. R-DID's estimand is the total effect, and for its test "only the signs matter" (`r-did:vrd:1`). The others are committed to the mechanism (ONT.3 individual-mechanistic; INF.5 depth for R-TCE and R-BEH).
- All four make the point conditional on what the rating measures. Reading the item wording (ms:S3.2) settles that condition, not the severity.

**`pnl:dis:11`. The legitimacy account. Fault line, with an idiosyncratic residue.**
- The moves: R-INST rates it damaging. By MI10, the account commits the authors to an institutional mechanism (`r-inst:fnd:9`; `r-inst:cmt:26`). R-BEH rates it damaging (`r-beh:fnd:11`). R-TCE rates it fixable: delete it, since R-TCE rejects MI10 and does not admit legitimacy under its ONT.1 (`r-tce:fnd:3`). R-DID rates it fixable (`r-did:fnd:9`), and minor as to its functional form (`r-did:fnd:17`).
- The parameters: INF.2 MI10 and ONT.1. Residue: R-BEH is neutral on MI10 yet rates it damaging, which the parameters do not explain.

**`pnl:dis:12`. Priority. Resolvable as to verdict; a fault line as to severity.**
- The moves: R-TCE fails it on two grounds (`r-tce:vrd:4`). R-BEH fails it provisionally (`r-beh:vrd:6`). R-INST qualifies it, uncertain, and would fail it if the studies are confirmed (`r-inst:ctb:5`). R-DID qualifies it (`r-did:vrd:6`).
- All four rest on the same unverified citations. R-TCE's second ground is that the design makes no discriminating predictions (`r-tce:fnd:5`). All four accept that point in substance (`pnl:agr:5`), but only R-TCE applied it to "adjudicate directly".
- Probe: verify Loh & Venkatraman 1992 and Ang & Cummings 1997 (and R-INST's further candidates; all to verify), and apply `pnl:agr:5` to the priority claim.
- Severity residue: R-INST rates it damaging for the contribution, R-TCE and R-BEH fixable, R-DID minor. That traces to PRA.3 (R-INST always) and PRA weight (0.8 against 0.3).
- Caution: four simulations recalling the same two citations are not four independent recalls (caveat 1).

**`pnl:dis:13`. Verdict on `pnl:ctb:3`. Idiosyncratic.** R-BEH and R-DID scored a bundled contribution that includes "rule out". Their stated remnants match the narrowed forms of R-TCE and R-INST (§2, notes). The split traces to how the contribution was cut, not to a parameter or an error.

**`pnl:dis:14`. Verdict on `pnl:ctb:8`. Idiosyncratic.** All four rate the underlying finding minor. R-DID fails a prescription that holds only conditionally; the others count the conditional version as qualified. The split is downstream of the `pnl:dis:2` fault line.

**`pnl:dis:15`. What a function-level test can discriminate. Resolvable by closer reading.**
- The moves: R-TCE and R-DID propose non-clinical functions as a placebo, on which "TCE predicts no m effect" (`r-tce:fnd:10`; `r-did:fnd:1`, repair). R-INST calls function-level incidence "the sharpest test", because its bundle rival predicts equal effects in hosting and help desk (r-inst §5 obs. 1). R-TCE's own production-cost variant predicts "the largest effects in low-k commodity functions (hosting, help desk)" (`r-tce:alt:1`, obs. 3).
- A modularity effect in commodity functions is therefore predicted both by the institutional bundle and by an economizing (production-cost) account. The placebo is a placebo for the hold-up channel only. The "sharpest test" separates hold-up from both rivals, but not the two rivals from each other.
- Probe: pair the function-level test with a test on which those two rivals differ. Candidates are cost consequences by adoption timing (r-inst §5 obs. 5), certified-but-unused interfaces (r-inst §5 obs. 2, MI4), and whether m rises only in the functions that were outsourced (`r-did:rival:1`, obs. 2).

**`pnl:dis:16`. Novelty of specificity-by-design. Fault line.**
- The moves: R-INST says it survives, calling it "the manuscript's strongest idea", undersold (`r-inst:ctb:6`; `r-inst:fnd:5`). R-TCE qualifies it, novelty lost: "already in Langlois (2002) and Baldwin & Clark (2000)" (`r-tce:vrd:5`). R-BEH qualifies it as anticipated by the works cited (`r-beh:fnd:16`). R-DID qualifies it as an untested conjecture with no first stage of m on measured specificity (`r-did:vrd:5`).
- The parameters: PRA.2. For R-INST (problematization), the idea problematizes TCE's assumption that transaction attributes are given. R-TCE and R-DID are gap-spotting, and R-BEH looks for the "interesting". ONT.3 also matters: the constitutive reading gives the idea content beyond MI8.
- Common ground: all four say the idea's empirical premise is not shown.

**`pnl:dis:17`. Within-hospital estimates against a field-level explanandum. Resolvable with the authors' data.**
- The moves: R-BEH rates it damaging. Year fixed effects absorb the field-level diffusion the paper names as its explanandum, and β1 bounds modularity's within-hospital contribution at about 11 points, against an aggregate share that doubled (`r-beh:fnd:2`; `r-beh:cmt:28`). R-TCE rates a related point minor: benchmark the magnitude against the decade's doubling (`r-tce:fnd:14`).
- The decomposition in `r-beh:chk:3` would settle it. The harness ran that check without data, and it produced no output. `r-beh:fnd:2` is preserved as a minority damaging finding (§5).

**`pnl:dis:18`. The smallest peer effect of interest. Idiosyncratic.**
- The moves: R-TCE proposes half the Model 1 estimate (≈ 0.068; r-tce §6). R-INST proposes an upper bound below a third of it (≈ 0.046; r-inst §6). R-DID proposes an interval of about ±0.03 (r-did §6). R-BEH says "substantively meaningful" without a number.
- EPI.5 names equivalence tests, but no parameter sets the bound. `r-did:chk:4` reports that the smallest bound the current Model 2 estimate passes at 5% is about 0.104. Every proposed bound therefore fails now. The disagreement sets the bar for a revision, not the verdict on the submission.

### 4.3 What the map shows (L5 Deconstructor, inter)

- **Eighteen disagreements: ten fault lines, four resolvable, four idiosyncratic.** No disagreement turns on a formal or numerical error left standing. Wherever a check bears, its output agrees with every reviewer's numbers. The four resolvable disagreements are:
  - a misreading of signs (`pnl:dis:4`, against `r-tce:str:4`);
  - a literature check (`pnl:dis:12`);
  - an inconsistency among the reviewers' own rival predictions (`pnl:dis:15`);
  - a decomposition that needs the authors' data (`pnl:dis:17`).
  
  The resolvable part of `pnl:dis:3` is settled against any unconditional claim of corroboration.
- **Six of the ten fault lines run through a material inference.** These are MI3 (`pnl:dis:1`), MI6 (`pnl:dis:2`, `pnl:dis:9`), MI9 with MI2 (`pnl:dis:6`), MI10 (`pnl:dis:11`) and MI8 (`pnl:dis:5`). The other four run through ONT.3 and ONT.1, ONT.4, ONT weight, PRA.2, and EPI.4 with EPI.5.
- **Most fault lines are about gravity, not existence.** In `pnl:dis:1`, `2`, `7`, `9`, `10` and `11`, every side accepts that the defect is there. The substance is shared across lenses, and the severity is perspectival.
- **Divergence does not track overall distance** (asserted, pending `pnl:chk:1`). Across the eight contributions, verdict divergence does not rise with perspective distance: Pearson r ≈ −0.42 and Spearman ρ ≈ −0.65, over n = 6 pairs, which supports no inference either way. The farthest pair (R-TCE/R-INST, 0.68) gives the same verdict on 6 of 8 contributions; R-INST/R-BEH (0.42) gives the same verdict on 4 of 8.
- **The sharpest split falls between the closest pair, on a single material inference.** The sharpest split on a shared finding is fatal against damaging on identification (`pnl:dis:2`). It falls between the closest pair (R-TCE/R-DID, 0.36), and it turns on MI6. Their INF distance is 0.11 although they take opposite stances on MI6. That suggests the distance tool weights INF.2 lightly or not at all. This is my inference; the tool was not among my inputs.

## 5. Recommendation spread (no consensus)

No consensus recommendation is produced (Role 3, instruction 4).

| Reviewer | Recommendation (simulated) | Would move toward reject if | Main driver |
|---|---|---|---|
| R-TCE | major revision | names no such condition (no fatal finding) | six damaging findings, each with a concrete repair (r-tce §7) |
| R-INST | major revision | "the authors keep the headline claims without these analyses" (r-inst §7) | `r-inst:fnd:7` (fatal, fixable if narrowed); MI7 and MI9 rejected |
| R-BEH | major revision | "rule out" is kept and `r-beh:fnd:4` cannot be met (r-beh step 7) | `r-beh:fnd:4` (fatal to that claim) |
| R-DID | major revision, "at the boundary with reject" | the editor treats building an identification strategy as beyond a revision (r-did §7) | `r-did:fnd:1` (fatal; MI6 rejected; EPI.3) |
| *Focal draft* | *major revision* | *not stated* | |

What drives the spread:

1. **Identical labels hide different conditions.** R-INST and R-BEH make a wording-and-tests condition: narrow the rule-out claim and run the tests (`pnl:dis:1`). R-DID makes a design condition: build an identification strategy (`pnl:dis:2`). R-TCE makes neither.
2. **R-DID's boundary depends on the editor's brief.** That brief is PRA.6, which no perspective sets.
3. **All four fatal ratings are scoped to headline claims.** The four are `r-inst:fnd:7`, `r-beh:fnd:4`, `r-did:fnd:1` and `r-did:fnd:2`. They concern "Not Mimicry" and the causal "Modularity". No reviewer rates any finding fatal to the H1 association or to the corrected model. This is why the labels converge despite the fatal ratings.

**Preserved findings.** These are findings rated fatal or damaging by a minority of reviewers, at most two of four at that level, or rated fatal by any reviewer. They are kept regardless of the panel majority.

| Finding(s) | Rating | What others say |
|---|---|---|
| `r-inst:fnd:7`, `r-beh:fnd:4`, `r-did:fnd:2` | fatal (rule-out claim) | R-TCE: damaging (`pnl:dis:1`) |
| `r-did:fnd:1` | fatal (causal claim) | R-TCE, R-BEH damaging; R-INST fixable (`pnl:dis:2`) |
| `r-inst:fnd:1` | damaging: standards are institutions, so the explanans is partly institutional | raised in this form by R-INST only; R-BEH in part (`pnl:dis:5`) |
| `r-inst:fnd:4` | damaging (priority, for the contribution) | others fixable or minor |
| `r-beh:fnd:2` | damaging: year fixed effects absorb the field-level explanandum | R-TCE minor; others silent (`pnl:dis:17`) |
| `r-inst:fnd:10`, `r-beh:fnd:1` | damaging: "economizing" unentitled (MI9) | R-TCE accepts by MI9 (`pnl:dis:6`) |
| `r-beh:fnd:3` | damaging: the constructs (uncertainty, certification, specificity) are loosely individuated | others fixable or minor on those parts |
| `r-beh:fnd:12` (part) | damaging: no behavioral or capability rival is considered (aspiration test, `r-beh:chk:4`) | raised by R-BEH only |
| `r-tce:fnd:9` (part) | damaging: a production-cost channel through vendor scale economies may carry the m effect | raised by R-TCE only |
| `r-inst:fnd:9`, `r-beh:fnd:11` | damaging (legitimacy account) | R-TCE, R-DID fixable (`pnl:dis:11`) |
| `r-tce:fnd:7`, `r-beh:fnd:18` | damaging (staffing bad control) | R-INST, R-DID fixable (`pnl:dis:8`) |
| `r-did:fnd:4`, `r-beh:fnd:5` | damaging (event study) | R-TCE, R-INST fixable (`pnl:dis:9`) |

## 6. What the focal reviewer faces

The focal draft (`runs/02_reviewer_draft.md`) recommends major revision. It has four major concerns:

1. P2 is mis-derived (damaging, fixable).
2. The test of the rival does not discriminate (damaging, fixable).
3. The identification of the modularity effect needs work (damaging, fixable).
4. "Economizing" claims efficiency without showing selection (fixable).

### 6.1 Where the draft already matches the panel

The draft has the following panel findings: `pnl:agr:1`, `2`, `4`, `5`, `9`, `10`, `11`, `12`, `13`, `15`, `16`, `18`, `19`, `23`, `25` and `27`. It also has the agreed strengths and probes `pnl:agr:28`, `29`, `31`, `32` and `33`. The draft's "test whose result I can't predict" for concern 1 is the function-level test that every lens proposes. Its "best route to identification" is the panel's agreed repair.

### 6.2 Robust findings the draft lacks

Here, robust means raised by three or four of the four lenses.

- **`pnl:agr:20`, "strongly predicts" (all four lenses).** The draft confirms the 2.7-point and one-sixth-SD arithmetic but does not question the word "strongly".
- **`pnl:agr:26`, the practice implication (all four; minor).** The draft does not mention it.
- **`pnl:agr:24`, the uncertainty construct (three lenses; inside a damaging finding for R-BEH).** The draft asks for the distribution of u. It does not ask whether admissions volatility is the model's u, or address that standardized u can be negative while the model needs u ≥ 0 (`r-tce:chl:11`). This bears on the draft's own "cleaner check" (∂k*/∂u < 0), which reads the sign of the u coefficient.

The draft has the following robust findings only in part:

- **`pnl:agr:14`, mechanism.** The draft states the premise ("Asset specificity ... is the theory's own channel") and asks for the effect of m on specificity. It does not draw the consequence that three lenses rate damaging. If the rating measures effective specificity, a non-zero β1 conditional on it means modularity works through a channel the model lacks, or else the rating measures nominal k (`r-tce:inc:5`, `r-inst:inc:5`, `r-beh:inc:5`). R-TCE names one such channel, production costs, which is economizing but not transaction-cost economizing (`r-tce:fnd:9`).
- **`pnl:agr:7`, the peer measure's exposure.** The draft names shared state conditions and noise. Three lenses also name the reflection problem (Manski 1993, to verify).
- **`pnl:agr:8`, the incomplete rival.** The draft does not list the rival's untested forms: imitation conditional on uncertainty, two-stage diffusion (Tolbert & Zucker 1983), and the coercive and normative pathways.
- **`pnl:agr:6`, the rival's construct.** The draft raises it "provisionally" and puts it "to the second reviewer". Three lenses rate it damaging.
- **`pnl:agr:17`, priority.** All four lenses name Loh & Venkatraman 1992 alongside Ang & Cummings 1997 (both to verify). Caveat 1 applies.
- **`pnl:agr:21`, single informant.** The draft's std:7 check passes m and the outcome as factual single-informant items. All four lenses note that one CIO supplies m, specificity and Φ.
- **Robust contribution `pnl:ctb:6`, the panel's highest survival score (0.625).** The draft's closing sentence comes near it ("how standards shape the boundaries of the firm"). The draft does not address the idea's novelty (`r-tce:vrd:5`; `r-beh:fnd:16`), or the panel's shared point that its premise, that m lowers measured specificity, is untested.

There is also a two-lens finding the draft lacks. **`pnl:agr:3`, measurement scope**: m covers clinical systems only, while Φ covers all functions. This bears directly on the draft's proposed function-level test.

### 6.3 Findings only the draft has

No simulated reviewer raises these. The panel neither supports nor contests them.

- The abstract and conclusion omit the H2 result (concern 1, std:2(a)).
- "Fashion" mixes motive with outcome (concern 4).
- Efficiency needs a selection argument, and selection is weak among non-profit and public hospitals (concern 4, std:8). This route reaches the conclusion of `pnl:agr:16` without using MI9.
- The marginal effect of modularity reaches zero near u ≈ 1.9 SD (minor).
- Selection into peer groups does not arise, because a hospital's state is fixed (std:14(b)).
- A lag does not remove persistent conditions (concern 2).

### 6.4 Fault lines to anticipate, and where the draft stands

The middle column gives the focal perspective's own setting, to show whether draft and perspective align. The last column states the question each fault line will put to the draft from the other side (L13 PrisM). Which side to take is the reviewer's decision.

| Fault line | Where the draft stands | `persp:FOCAL` setting | The objection from the other side |
|---|---|---|---|
| `pnl:dis:1`, gravity of "rule out" | Damaging: "rules out" is not supported; repair the title. Same as R-TCE | MI3 neutral; PRA.1 includes economists and sociologists; PRA.2 problematization and gap-spotting | R-INST, R-BEH, R-DID: fatal to the central claim. "If the title claim does not stand, which central claim does?" |
| `pnl:dis:2`, causal reading | Damaging; identify through the requirements. Same as R-TCE and R-BEH | MI6 endorsed; EPI.3 design-based and model-based | R-DID: fatal. "What design makes within-hospital changes in m as good as random?" |
| `pnl:dis:3`, corroboration | "Not a confirmation either ... choosing an aggregation assumption now would be a rescue". Close to R-DID | EPI.4 high; EPI.2 sophisticated falsificationism | R-BEH, and more weakly R-TCE: the sign follows from A3, which was stated before the data. "Why does a consequence of a stated assumption count for nothing?" |
| `pnl:dis:5`, standards as institutions | No position taken. Mandates appear as shared conditions and an exclusion problem; recognisability is deferred to "the second reviewer" | ONT.1 includes fields, logics and legitimacy; ONT.5 constitutive admissible; ONT.3 individual-mechanistic and selection | R-INST: "If certification was mandated, in what sense is the explanation 'not institutional'?" |
| `pnl:dis:6`, economizing | Unentitled, by a selection argument (std:8, a "must" in the draft's first line), rated fixable. In substance with R-INST and R-BEH | MI9 neutral; ONT.5 choice-theoretic admissible; ONT.3 includes selection | R-TCE: "Observed shares are optimal responses (MI9). Why demand outcome evidence for a comparative-statics fit?" |
| `pnl:dis:7`, peer construct | Provisional; deferred to the second reviewer | ONT.4 strict | R-DID: construct validity is minor; the real problem is identifying peer effects |
| `pnl:dis:10`, specificity control | Estimator framing (bad control; report results without it). Same framing as R-DID | INF.5 depth; ONT weight 0.6 | R-TCE, R-INST, R-BEH: "What does β1 > 0 conditional on specificity say about the hold-up mechanism?" |
| `pnl:dis:11`, legitimacy account | It "counts against the model" and is an institutional mechanism in a paper claiming to have ruled such mechanisms out. Uses R-INST's and R-BEH's incompatibility, inside a damaging concern | MI10 neutral; ONT.1 admits legitimacy | R-TCE, R-DID: an unlicensed auxiliary to delete; fixable |
| `pnl:dis:16`, novelty of specificity-by-design | Not addressed | PRA.2 problematization and gap-spotting | R-INST: the paper's strongest idea, undersold. R-TCE, R-BEH: anticipated by Langlois 2002 and Baldwin & Clark 2000 |
| MI4 (`pnl:agr:22`) | The std:7 check passes m and Φ as "factual items" | MI4 neutral | R-INST, R-BEH: certified is not implemented; validate against actual use |
| INF.6 | The draft's repair is eliminative: an interval that "excludes 0.07 ... would justify 'no evidence of imitation through this channel'" | Eliminative accepted, assimilative suspect. FOCAL is the only perspective in the panel that accepts eliminative justification | R-BEH and R-INST propose an assimilative reframing (`r-beh:fnd:13`; `r-inst:fnd:1`), which FOCAL's INF.6 marks suspect |

On `pnl:dis:6` and `pnl:dis:11`, the draft parts company with the resembling reviewer (R-TCE). R-TCE endorses MI9 and rejects MI10; FOCAL is neutral on both.

### 6.5 Resolvable items that bear on the draft

- **`pnl:dis:4`.** The draft says: "If the stars are right, the corrected model fails this check." All four star checks find the *** on Model 3 uncertainty inconsistent with t ≈ 1.65 (p ≈ 0.10), and `r-did:chk:2` finds it inconsistent under every admissible rounding. The antecedent of the draft's conditional is therefore false. What remains is a point estimate with the wrong sign (about +0.056 at mean m, `r-beh:chk:2`), whose precision needs the coefficient covariance the draft already requests.
- **`pnl:dis:3`.** The draft's statement that, on the share scale, the interaction's sign "also depends on how spending is distributed near k*" is the resolvable component of `pnl:dis:3`. The harness outputs used there bear it out.
- **H3 as stated versus as tested.** R-DID holds that H3 as stated, an unconditional positive association, is supported by Model 1, and that "not supported" tests a conditional reformulation (`r-did:inc:7`; `r-did:fnd:10`, minor). The draft writes: H3 is "not supported", "as §4 fairly says". Reading ms:H3 against ms:S2.4 settles which is right.
- **`pnl:dis:15`.** The draft's function-level test, on k, m and u, separates the hold-up channel from both the production-cost variant and the institutional bundle. It does not separate those two from each other.
- **`pnl:dis:18`.** The draft's bound of 0.07 is the most lenient one in the panel: R-TCE ≈ 0.068, R-INST ≈ 0.046, R-DID ≈ ±0.03. Under every one of them, the current estimate fails equivalence (smallest passable bound ≈ 0.104, `r-did:chk:4`). The choice of bound sets the bar for a revision, not the current verdict.

### 6.6 Presentation

The draft file opens with a line that is not review text: "bs:T7 settled: must means must ...". It reads as a workbench note on the reviewer's standards std:7 and std:8, and should be removed before the review is submitted.

## 7. The PanelSynthesis object

```json
{
 "@id": "pnl:synthesis:1",
 "@type": "PanelSynthesis",
 "manuscript": "ms:TEST",
 "instructionSet": "Reviewership v0.1 (23 October 2026), Role 3 (Panel Synthesizer)",
 "simulated": true,
 "statusConvention": "Simulated findings stay as stated (asserted). Harness outputs are used only to judge whether a disagreement is resolvable. Derived statistics are asserted pending pnl:chk:1.",
 "reviews": [
  {"@id": "pnl:rev:1", "file": "runs/03_simulated_reviewer_TCE.md", "perspective": "persp:R-TCE", "relationToFocal": "resembling", "distanceToFocal": 0.35, "recommendation": "major revision",
   "severityCounts": {"fatal": 0, "damaging": 6, "fixable": 7, "minor": 3},
   "standards": "listed (r-tce:std:1-9), drawn from configured parameters",
   "checkOutputs": ["03_checks/r-tce_chk_1.out.txt", "03_checks/r-tce_chk_1_b2.out.txt (content of r-tce:chk:2; header mislabelled r-tce:chk:1)", "03_checks/r-tce_chk_3.out.txt", "03_checks/r-tce_chk_4.out.txt"]},
  {"@id": "pnl:rev:2", "file": "runs/04_simulated_reviewer_INST.md", "perspective": "persp:R-INST", "relationToFocal": "differing", "distanceToFocal": 0.53, "recommendation": "major revision (reject if headline claims kept without the analyses)",
   "severityCounts": {"fatal": 1, "damaging": 6, "fixable": 7, "minor": 3},
   "standards": "derived by the simulator (r-inst:std:1-7) and flagged as not configured",
   "checkOutputs": ["04_checks/r-inst_chk_1.out.txt", "04_checks/r-inst_chk_2.out.txt", "04_checks/r-inst_chk_3.out.txt"]},
  {"@id": "pnl:rev:3", "file": "runs/05_simulated_reviewer_BEH.md", "perspective": "persp:R-BEH", "relationToFocal": "differing", "distanceToFocal": 0.42, "recommendation": "major revision (reject if 'rule out' kept and r-beh:fnd:4 unmet)",
   "severityCounts": {"fatal": 1, "damaging": 9, "fixable": 9, "minor": 2, "none": 1},
   "standards": "none listed",
   "checkOutputs": ["05_checks/r-beh_chk_1.out.txt", "05_checks/r-beh_chk_2.out.txt", "05_checks/r-beh_chk_3.out.txt (empty: needs authors' data)", "05_checks/r-beh_chk_4.out.txt (empty: needs authors' data)"]},
  {"@id": "pnl:rev:4", "file": "runs/06_simulated_reviewer_DID.md", "perspective": "persp:R-DID", "relationToFocal": "differing", "distanceToFocal": 0.45, "recommendation": "major revision, at the boundary with reject and resubmit",
   "severityCounts": {"fatal": 2, "damaging": 2, "fixable": 8, "minor": 8},
   "standards": "none listed",
   "checkOutputs": ["06_checks/r-did_chk_1.out.txt to r-did_chk_7.out.txt"]}
 ],
 "survival": [
  {"@id": "pnl:srv:1", "contribution": {"@id": "pnl:ctb:1", "statement": "Closed-form TCE model of modularity and make-or-buy; Prop. 1 and Prop. 2", "merges": ["r-tce:ctb:1", "r-inst:ctb:1", "r-beh:ctb:1", "r-did:ctb:1"], "alignment": "clean"},
   "verdicts": [{"perspective": "persp:R-TCE", "verdict": "qualified", "ref": "r-tce:vrd:1"}, {"perspective": "persp:R-INST", "verdict": "qualified", "ref": "r-inst:ctb:1"}, {"perspective": "persp:R-BEH", "verdict": "qualified", "ref": "r-beh:vrd:1"}, {"perspective": "persp:R-DID", "verdict": "qualified", "ref": "r-did:vrd:1"}],
   "survivalScore": 0.5, "classification": "robust",
   "note": "All four: Prop. 1 holds; Prop. 2 holds only with its sign reversed under A3. R-INST and R-DID add that neither sign transfers to Phi without an assumption on F."},
  {"@id": "pnl:srv:2", "contribution": {"@id": "pnl:ctb:2", "statement": "Test of the propositions against an institutional rival on a 2009-2019 hospital panel", "merges": ["r-tce:ctb:2", "r-inst:ctb:2", "r-beh:ctb:2", "r-did:ctb:2"], "alignment": "clean; R-DID moves the causal reading to r-did:ctb:4"},
   "verdicts": [{"perspective": "persp:R-TCE", "verdict": "qualified", "ref": "r-tce:vrd:2"}, {"perspective": "persp:R-INST", "verdict": "qualified", "ref": "r-inst:ctb:2"}, {"perspective": "persp:R-BEH", "verdict": "qualified", "ref": "r-beh:vrd:2"}, {"perspective": "persp:R-DID", "verdict": "qualified", "ref": "r-did:vrd:2"}],
   "survivalScore": 0.5, "classification": "robust",
   "note": "All four: H1 as a within-hospital association; the test does not discriminate between the accounts."},
  {"@id": "pnl:srv:3", "contribution": {"@id": "pnl:ctb:3", "statement": "Once modularity is measured, apparent peer effects 'disappear'", "merges": ["r-tce:ctb:3", "r-inst:ctb:3", "r-beh:ctb:3 (first half)", "r-did:ctb:3 (first half)"], "alignment": "judgement call (a): R-BEH and R-DID bundle this with 'rule out'"},
   "verdicts": [{"perspective": "persp:R-TCE", "verdict": "qualified", "ref": "r-tce:vrd:3"}, {"perspective": "persp:R-INST", "verdict": "qualified", "ref": "r-inst:ctb:3"}, {"perspective": "persp:R-BEH", "verdict": "fails", "ref": "r-beh:vrd:3"}, {"perspective": "persp:R-DID", "verdict": "fails", "ref": "r-did:vrd:3"}],
   "survivalScore": 0.25, "classification": "neither",
   "note": "Survives for the farthest pair (0.68). R-BEH's and R-DID's stated remnants match the R-TCE and R-INST narrowed forms (pnl:dis:13)."},
  {"@id": "pnl:srv:4", "contribution": {"@id": "pnl:ctb:4", "statement": "The results 'rule out mimetic isomorphism' in this setting", "merges": ["r-tce:ctb:6 (first half)", "r-inst:ctb:4 (first half)", "r-beh:ctb:3 (alsoAvowedAs)", "r-did:ctb:3 (second half)"], "alignment": "judgement calls (a), (b)"},
   "verdicts": [{"perspective": "persp:R-TCE", "verdict": "fails", "ref": "r-tce:vrd:6"}, {"perspective": "persp:R-INST", "verdict": "fails", "ref": "r-inst:ctb:4"}, {"perspective": "persp:R-BEH", "verdict": "fails", "ref": "r-beh:vrd:3"}, {"perspective": "persp:R-DID", "verdict": "fails", "ref": "r-did:vrd:3"}],
   "survivalScore": 0.0, "classification": "neither (fails for every reviewer)"},
  {"@id": "pnl:srv:5", "contribution": {"@id": "pnl:ctb:5", "statement": "The practice is economizing; standards, through modularity, widened outsourcing", "merges": ["r-tce:ctb:6 (second half)", "r-inst:ctb:4 (second half)", "r-beh:ctb:5", "r-did:ctb:4"], "alignment": "judgement calls (b), (c): R-BEH's statement is a weaker modal claim; R-DID's adds the causal claim of ms:S5"},
   "verdicts": [{"perspective": "persp:R-TCE", "verdict": "fails", "ref": "r-tce:vrd:6"}, {"perspective": "persp:R-INST", "verdict": "fails", "ref": "r-inst:ctb:4"}, {"perspective": "persp:R-BEH", "verdict": "qualified", "ref": "r-beh:vrd:5"}, {"perspective": "persp:R-DID", "verdict": "fails", "ref": "r-did:vrd:4"}],
   "survivalScore": 0.125, "classification": "neither (qualified for one lens only)",
   "note": "R-BEH's qualified form drops the efficiency claim: only feasible alternatives changed."},
  {"@id": "pnl:srv:6", "contribution": {"@id": "pnl:ctb:6", "statement": "Specificity is partly a product of interface design; boundaries respond to standards", "merges": ["r-tce:ctb:5", "r-inst:ctb:6", "r-beh:ctb:4", "r-did:ctb:5"], "alignment": "clean"},
   "verdicts": [{"perspective": "persp:R-TCE", "verdict": "qualified", "ref": "r-tce:vrd:5"}, {"perspective": "persp:R-INST", "verdict": "survives", "ref": "r-inst:ctb:6"}, {"perspective": "persp:R-BEH", "verdict": "qualified", "ref": "r-beh:vrd:4"}, {"perspective": "persp:R-DID", "verdict": "qualified", "ref": "r-did:vrd:5"}],
   "survivalScore": 0.625, "classification": "robust",
   "note": "Highest score. Novelty is contested (pnl:dis:16); all four say its empirical premise (m lowers measured specificity) is not shown."},
  {"@id": "pnl:srv:7", "contribution": {"@id": "pnl:ctb:7", "statement": "Priority: first study to adjudicate directly", "merges": ["r-tce:ctb:4", "r-inst:ctb:5", "r-beh:ctb:6", "r-did:ctb:6"], "alignment": "clean"},
   "verdicts": [{"perspective": "persp:R-TCE", "verdict": "fails", "ref": "r-tce:vrd:4"}, {"perspective": "persp:R-INST", "verdict": "qualified (uncertain)", "ref": "r-inst:ctb:5"}, {"perspective": "persp:R-BEH", "verdict": "fails (provisional)", "ref": "r-beh:vrd:6"}, {"perspective": "persp:R-DID", "verdict": "qualified", "ref": "r-did:vrd:6"}],
   "survivalScore": 0.25, "classification": "neither",
   "note": "Survivors R-INST and R-DID are 0.65 apart; all rest on citations to verify (pnl:dis:12)."},
  {"@id": "pnl:srv:8", "contribution": {"@id": "pnl:ctb:8", "statement": "Practice: attend first to modularity", "merges": ["r-tce:ctb:7", "r-inst:ctb:7", "r-beh:ctb:7", "r-did:ctb:7"], "alignment": "clean"},
   "verdicts": [{"perspective": "persp:R-TCE", "verdict": "qualified", "ref": "r-tce:vrd:7"}, {"perspective": "persp:R-INST", "verdict": "qualified", "ref": "r-inst:ctb:7"}, {"perspective": "persp:R-BEH", "verdict": "qualified", "ref": "r-beh:vrd:7"}, {"perspective": "persp:R-DID", "verdict": "fails", "ref": "r-did:vrd:7"}],
   "survivalScore": 0.375, "classification": "neither",
   "note": "Underlying finding rated minor by all four (pnl:dis:14)."}
 ],
 "agreements": [
  {"@id": "pnl:agr:1", "kind": "problem", "locus": ["ms:Prop2", "ms:Appendix", "ms:A3"], "finding": "Prop. 2's proof treats H(u) as constant in u; the true cross-partial is negative under A3", "raisedBy": [{"ref": "r-tce:fnd:1", "severity": "damaging"}, {"ref": "r-inst:fnd:8", "severity": "damaging"}, {"ref": "r-beh:fnd:9", "severity": "damaging"}, {"ref": "r-did:fnd:7", "severity": "damaging"}], "highestSeverity": "damaging", "inFocalDraft": "yes"},
  {"@id": "pnl:agr:2", "kind": "problem", "locus": ["ms:S2.4"], "finding": "No aggregation from k* to Phi; the interaction's sign on Phi depends on F; ceiling at k* >= 1", "raisedBy": [{"ref": "r-tce:fnd:2", "severity": "fixable"}, {"ref": "r-inst:fnd:3", "severity": "fixable"}, {"ref": "r-beh:fnd:10", "severity": "fixable"}, {"ref": "r-did:fnd:8", "severity": "fixable"}], "highestSeverity": "fixable", "inFocalDraft": "yes"},
  {"@id": "pnl:agr:3", "kind": "problem", "locus": ["ms:S3.2 Modularity", "ms:S2.1"], "finding": "m covers clinical systems only; Phi covers all IT functions", "raisedBy": [{"ref": "r-tce:fnd:10", "severity": "fixable"}, {"ref": "r-inst:fnd:3", "severity": "fixable"}], "highestSeverity": "fixable", "inFocalDraft": "no"},
  {"@id": "pnl:agr:4", "kind": "problem", "locus": ["ms:Abstract", "ms:S5 para 1", "ms:T2.M2.Peer"], "finding": "'Rule out' infers absence from non-significance (MI7); 95% CI about [-0.03, 0.12]; no equivalence test", "raisedBy": [{"ref": "r-tce:fnd:4", "severity": "damaging"}, {"ref": "r-inst:fnd:7", "severity": "fatal (fixable if narrowed)"}, {"ref": "r-beh:fnd:4", "severity": "fatal (to that claim)"}, {"ref": "r-did:fnd:2", "severity": "fatal"}], "highestSeverity": "fatal", "inFocalDraft": "yes"},
  {"@id": "pnl:agr:5", "kind": "problem", "locus": ["ms:S2.4 last para", "ms:S4 H3"], "finding": "The H3 criterion does not discriminate: modularity may carry imitation, so conditioning on it removes the peer coefficient by construction", "raisedBy": [{"ref": "r-tce:fnd:5", "severity": "damaging"}, {"ref": "r-inst:fnd:7", "severity": "within fatal"}, {"ref": "r-beh:fnd:4", "severity": "within fatal"}, {"ref": "r-beh:fnd:12", "severity": "damaging"}, {"ref": "r-did:fnd:2", "severity": "within fatal"}, {"ref": "r-did:fnd:10", "severity": "minor"}], "highestSeverity": "fatal (within compound findings)", "inFocalDraft": "yes"},
  {"@id": "pnl:agr:6", "kind": "problem", "locus": ["ms:S3.2 Peer outsourcing", "ms:S1"], "finding": "The same-state lagged mean of sample hospitals is not the rival's referent set", "raisedBy": [{"ref": "r-tce:fnd:5", "severity": "damaging"}, {"ref": "r-inst:fnd:2", "severity": "damaging"}, {"ref": "r-beh:fnd:3", "severity": "damaging"}, {"ref": "r-did:cmt:19", "severity": "challenged (construct issues minor)"}], "highestSeverity": "damaging", "inFocalDraft": "partial (provisional)"},
  {"@id": "pnl:agr:7", "kind": "problem", "locus": ["ms:S3.2", "ms:S3.3"], "finding": "The state-year peer mean is exposed to reflection, state-level correlated shocks and thin-cell noise", "raisedBy": [{"ref": "r-tce:fnd:5", "severity": "damaging"}, {"ref": "r-inst:fnd:2", "severity": "damaging"}, {"ref": "r-beh:fnd:19", "severity": "fixable"}, {"ref": "r-did:fnd:2", "severity": "within fatal"}], "highestSeverity": "fatal (within compound)", "inFocalDraft": "partial"},
  {"@id": "pnl:agr:8", "kind": "problem", "locus": ["ms:S2.4", "ms:H3"], "finding": "Only the mimetic mechanism is stated; coercive and normative pathways and conditional forms of imitation are untested", "raisedBy": [{"ref": "r-inst:fnd:1", "severity": "damaging"}, {"ref": "r-inst:fnd:7", "severity": "within fatal"}, {"ref": "r-beh:fnd:12", "severity": "damaging"}, {"ref": "r-tce:fnd:5", "severity": "damaging"}], "highestSeverity": "damaging", "inFocalDraft": "partial"},
  {"@id": "pnl:agr:9", "kind": "problem", "locus": ["ms:S3.3"], "finding": "Reverse causation: vendors may install certified interfaces on taking over functions", "raisedBy": [{"ref": "r-tce:fnd:6", "severity": "damaging"}, {"ref": "r-beh:fnd:5", "severity": "damaging"}, {"ref": "r-did:fnd:1", "severity": "fatal"}], "highestSeverity": "fatal", "inFocalDraft": "yes"},
  {"@id": "pnl:agr:10", "kind": "problem", "locus": ["ms:S3.3"], "finding": "Year FE do not absorb hospital-specific EHR timing or state mandates", "raisedBy": [{"ref": "r-tce:fnd:6", "severity": "damaging"}, {"ref": "r-inst:fnd:13", "severity": "fixable"}, {"ref": "r-did:fnd:1", "severity": "fatal"}], "highestSeverity": "fatal", "inFocalDraft": "yes (minor)"},
  {"@id": "pnl:agr:11", "kind": "problem", "locus": ["ms:S3.2 staffing", "ms:S3.3", "ms:T2.M4"], "finding": "In-house staffing is a bad control; the capability claim is unentitled", "raisedBy": [{"ref": "r-tce:fnd:7", "severity": "damaging"}, {"ref": "r-inst:fnd:14", "severity": "fixable"}, {"ref": "r-beh:fnd:18", "severity": "damaging"}, {"ref": "r-did:fnd:3", "severity": "fixable"}], "highestSeverity": "damaging", "inFocalDraft": "yes"},
  {"@id": "pnl:agr:12", "kind": "problem", "locus": ["ms:S4 Robustness"], "finding": "Event study: staggered TWFE, unreported, no first stage, exclusion unargued", "raisedBy": [{"ref": "r-tce:fnd:8", "severity": "fixable"}, {"ref": "r-inst:fnd:13", "severity": "fixable"}, {"ref": "r-inst:fnd:15", "severity": "fixable"}, {"ref": "r-beh:fnd:5", "severity": "damaging"}, {"ref": "r-did:fnd:4", "severity": "damaging"}], "highestSeverity": "damaging", "inFocalDraft": "yes"},
  {"@id": "pnl:agr:13", "kind": "problem", "locus": ["ms:S3.3"], "finding": "Hospital clustering for state-level regressors", "raisedBy": [{"ref": "r-tce:fnd:8", "severity": "fixable"}, {"ref": "r-inst:fnd:15", "severity": "fixable"}, {"ref": "r-beh:fnd:19", "severity": "fixable"}, {"ref": "r-did:fnd:11", "severity": "fixable"}], "highestSeverity": "fixable", "inFocalDraft": "yes"},
  {"@id": "pnl:agr:14", "kind": "problem", "locus": ["ms:S2.2", "ms:S3.2 specificity", "ms:T2"], "finding": "Beta1 survives the specificity control; if the rating is effective specificity, the model implies beta1 near 0 or the control is a mediator; m lowering specificity is not shown", "raisedBy": [{"ref": "r-tce:fnd:9", "severity": "damaging"}, {"ref": "r-inst:fnd:10", "severity": "damaging"}, {"ref": "r-beh:fnd:14", "severity": "damaging"}, {"ref": "r-did:fnd:12", "severity": "fixable"}], "highestSeverity": "damaging", "inFocalDraft": "partial"},
  {"@id": "pnl:agr:15", "kind": "problem", "locus": ["ms:S5 para 2"], "finding": "Legitimacy account: post hoc, unlabelled, outside the model, clashes with 'Its substance is economizing', unnecessary once Prop. 2 is corrected", "raisedBy": [{"ref": "r-tce:fnd:3", "severity": "fixable"}, {"ref": "r-inst:fnd:9", "severity": "damaging"}, {"ref": "r-beh:fnd:11", "severity": "damaging"}, {"ref": "r-did:fnd:9", "severity": "fixable"}], "highestSeverity": "damaging", "inFocalDraft": "yes"},
  {"@id": "pnl:agr:16", "kind": "problem", "locus": ["ms:Abstract", "ms:S6"], "finding": "'Economizing' unentitled without outcome evidence; the step is MI9", "raisedBy": [{"ref": "r-inst:fnd:10", "severity": "damaging"}, {"ref": "r-beh:fnd:1", "severity": "damaging"}], "highestSeverity": "damaging", "inFocalDraft": "yes (by a selection argument, not MI9)"},
  {"@id": "pnl:agr:17", "kind": "problem", "locus": ["ms:Abstract", "ms:S1"], "finding": "Priority unchecked; Loh & Venkatraman 1992 and Ang & Cummings 1997 named by all four (to verify)", "raisedBy": [{"ref": "r-tce:fnd:15", "severity": "fixable"}, {"ref": "r-inst:fnd:4", "severity": "damaging (for the contribution)"}, {"ref": "r-beh:fnd:15", "severity": "fixable"}, {"ref": "r-did:fnd:18", "severity": "minor"}], "highestSeverity": "damaging", "inFocalDraft": "partial", "caveat": "recall-based; simulators likely correlated"},
  {"@id": "pnl:agr:18", "kind": "problem", "locus": ["ms:S3.1", "ms:T2"], "finding": "N = 4,712 versus 412 x 11 = 4,532", "raisedBy": [{"ref": "r-tce:fnd:13", "severity": "fixable"}, {"ref": "r-inst:fnd:16", "severity": "minor"}, {"ref": "r-beh:fnd:20", "severity": "fixable"}, {"ref": "r-did:fnd:5", "severity": "fixable"}], "highestSeverity": "fixable", "inFocalDraft": "yes"},
  {"@id": "pnl:agr:19", "kind": "problem", "locus": ["ms:T2.M3.uncertainty"], "finding": "0.084 (0.051) marked *** at t of about 1.65", "raisedBy": [{"ref": "r-tce:fnd:13", "severity": "fixable"}, {"ref": "r-inst:fnd:16", "severity": "minor"}, {"ref": "r-beh:fnd:20", "severity": "fixable"}, {"ref": "r-did:fnd:6", "severity": "minor"}], "highestSeverity": "fixable", "inFocalDraft": "yes"},
  {"@id": "pnl:agr:20", "kind": "problem", "locus": ["ms:Abstract"], "finding": "'Strongly predicts' for about 0.16 SD", "raisedBy": [{"ref": "r-tce:fnd:14", "severity": "minor"}, {"ref": "r-inst:fnd:16", "severity": "minor"}, {"ref": "r-beh:fnd:7", "severity": "fixable"}, {"ref": "r-did:fnd:14", "severity": "minor"}], "highestSeverity": "fixable", "inFocalDraft": "no"},
  {"@id": "pnl:agr:21", "kind": "problem", "locus": ["ms:S3.1", "ms:S3.2"], "finding": "One CIO supplies m, specificity and Phi", "raisedBy": [{"ref": "r-tce:fnd:16", "severity": "minor"}, {"ref": "r-inst:fnd:11", "severity": "fixable"}, {"ref": "r-beh:fnd:6", "severity": "fixable"}, {"ref": "r-did:fnd:20", "severity": "minor"}], "highestSeverity": "fixable", "inFocalDraft": "partial"},
  {"@id": "pnl:agr:22", "kind": "problem", "locus": ["ms:S3.2 Modularity"], "finding": "Certification may be decoupled from working interoperability (MI4)", "raisedBy": [{"ref": "r-inst:fnd:11", "severity": "fixable"}, {"ref": "r-beh:fnd:3", "severity": "within damaging"}], "highestSeverity": "damaging (within compound)", "inFocalDraft": "no (std:7 check takes the contrary view)"},
  {"@id": "pnl:agr:23", "kind": "problem", "locus": ["ms:S3.1"], "finding": "All-years-responder inclusion selects on survival and response", "raisedBy": [{"ref": "r-tce:fnd:16", "severity": "minor"}, {"ref": "r-inst:fnd:12", "severity": "fixable"}, {"ref": "r-beh:fnd:6", "severity": "fixable"}, {"ref": "r-did:fnd:15", "severity": "fixable"}], "highestSeverity": "fixable", "inFocalDraft": "yes"},
  {"@id": "pnl:agr:24", "kind": "problem", "locus": ["ms:S3.2 uncertainty", "ms:S2.2"], "finding": "Admissions volatility is not the model's adaptation uncertainty; standardized u is negative where the model needs u >= 0", "raisedBy": [{"ref": "r-tce:fnd:11", "severity": "fixable"}, {"ref": "r-beh:fnd:3", "severity": "within damaging"}, {"ref": "r-did:fnd:16", "severity": "minor"}], "highestSeverity": "damaging (within compound)", "inFocalDraft": "no"},
  {"@id": "pnl:agr:25", "kind": "problem", "locus": ["ms:T2.M3", "ms:S2.3"], "finding": "The corrected model implies uncertainty lowers Phi at every m; Table 2's uncertainty effect is positive and imprecise", "raisedBy": [{"ref": "r-beh:fnd:21", "severity": "fixable"}, {"ref": "r-did:chl:6", "severity": "challenge"}], "highestSeverity": "fixable", "inFocalDraft": "yes"},
  {"@id": "pnl:agr:26", "kind": "problem", "locus": ["ms:S5.1"], "finding": "Practice implication presupposes the causal claim", "raisedBy": [{"ref": "r-tce:fnd:17", "severity": "minor"}, {"ref": "r-inst:fnd:6", "severity": "minor"}, {"ref": "r-beh:fnd:17", "severity": "minor"}, {"ref": "r-did:fnd:19", "severity": "minor"}], "highestSeverity": "minor", "inFocalDraft": "no"},
  {"@id": "pnl:agr:27", "kind": "problem", "locus": ["no availability statement"], "finding": "No data or code availability", "raisedBy": [{"ref": "r-inst:fnd:17", "severity": "minor"}, {"ref": "r-beh:fnd:22", "severity": "fixable"}, {"ref": "r-did:fnd:13", "severity": "fixable"}], "highestSeverity": "fixable", "inFocalDraft": "yes"},
  {"@id": "pnl:agr:28", "kind": "strength", "finding": "Prop. 1 and its proof are correct", "raisedBy": [{"ref": "r-tce:str:3"}, {"ref": "r-inst:fnd:8"}, {"ref": "r-beh:cmt:4"}, {"ref": "r-did:cmt:1"}], "inFocalDraft": "yes"},
  {"@id": "pnl:agr:29", "kind": "strength", "finding": "H1 is a credibly estimated, stable within-hospital association", "raisedBy": [{"ref": "r-tce:cmt:7"}, {"ref": "r-inst §7"}, {"ref": "r-beh step 7"}, {"ref": "r-did:vrd:2"}], "inFocalDraft": "yes"},
  {"@id": "pnl:agr:30", "kind": "strength", "finding": "Correcting Prop. 2 makes the legitimacy account unnecessary", "raisedBy": [{"ref": "r-tce:fnd:1"}, {"ref": "r-inst:fnd:8"}, {"ref": "r-beh:fnd:9"}, {"ref": "r-did:fnd:7"}], "inFocalDraft": "partial"},
  {"@id": "pnl:agr:31", "kind": "repair", "finding": "The staggered state requirements are the best route to identification", "raisedBy": [{"ref": "r-tce:fnd:6"}, {"ref": "r-inst:fnd:13"}, {"ref": "r-beh:fnd:5"}, {"ref": "r-did:fnd:1"}], "inFocalDraft": "yes"},
  {"@id": "pnl:agr:32", "kind": "probe", "finding": "Function-level analysis is the most discriminating test available", "raisedBy": [{"ref": "r-tce:alt:1"}, {"ref": "r-inst §5 obs. 1"}, {"ref": "r-beh step 5"}, {"ref": "r-did:rival:1"}], "inFocalDraft": "yes", "caveat": "pnl:dis:15"},
  {"@id": "pnl:agr:33", "kind": "probe", "finding": "Timing of m relative to outsourcing and vendor contracts", "raisedBy": [{"ref": "r-tce:alt:1"}, {"ref": "r-inst §5 obs. 3"}, {"ref": "r-beh:fnd:5"}, {"ref": "r-did:rival:1"}], "inFocalDraft": "yes"}
 ],
 "disagreements": [
  {"@id": "pnl:dis:1", "topic": "Gravity of the unentitled 'rule out mimetic isomorphism'", "positions": [{"perspective": "persp:R-TCE", "refs": ["r-tce:fnd:4", "r-tce:fnd:5"], "severity": "damaging"}, {"perspective": "persp:R-INST", "refs": ["r-inst:fnd:7"], "severity": "fatal (fixable if narrowed)"}, {"perspective": "persp:R-BEH", "refs": ["r-beh:fnd:4"], "severity": "fatal (to that claim)"}, {"perspective": "persp:R-DID", "refs": ["r-did:fnd:2"], "severity": "fatal"}],
   "classification": "fault line", "parameters": ["INF.2 MI3", "PRA.1", "PRA.2"], "harness": "Interval and TOST outputs agree across r-tce:chk:3, r-inst:chk:2, r-beh:chk:2, r-did:chk:4; no reviewer's numbers contradicted; not resolvable by check.", "residue": "Which claim is 'central' is a reading the reviewer must make."},
  {"@id": "pnl:dis:2", "topic": "Gravity of the unentitled causal reading of beta1", "positions": [{"perspective": "persp:R-DID", "refs": ["r-did:fnd:1"], "severity": "fatal"}, {"perspective": "persp:R-TCE", "refs": ["r-tce:fnd:6"], "severity": "damaging"}, {"perspective": "persp:R-BEH", "refs": ["r-beh:fnd:5"], "severity": "damaging"}, {"perspective": "persp:R-INST", "refs": ["r-inst:fnd:13"], "severity": "fixable"}],
   "classification": "fault line", "parameters": ["INF.2 MI6", "EPI.3", "EPI weight"], "harness": "No check bears.", "note": "Closest pair (R-TCE/R-DID, 0.36); their INF distance is 0.11 despite opposite MI6 stances."},
  {"@id": "pnl:dis:3", "topic": "Is the corrected negative interaction corroboration or accommodation?", "positions": [{"perspective": "persp:R-TCE", "refs": ["r-tce:fnd:1", "r-tce:str:4"], "position": "real but moderate corroboration; all signs agree"}, {"perspective": "persp:R-BEH", "refs": ["r-beh:fnd:8"], "position": "corroboration, provided the Phi step is made"}, {"perspective": "persp:R-DID", "refs": ["r-did:fnd:7"], "position": "accommodation"}, {"perspective": "persp:R-INST", "refs": ["r-inst:fnd:8"], "position": "legitimacy story redundant, not vindicated; no position on corroboration"}],
   "classification": "fault line", "resolvedComponent": "The Phi-scale sign depends on F: negative for uniform and Beta(5,2), positive for Beta(2,5) and Beta(1,3), mixed for Beta(2,2) (r-tce:chk:2 output, r-inst:chk:3, r-did:chk:5; decomposition r-beh:chk:1(c)). R-BEH's conditional stands; r-tce:str:4 overreaches r-tce:fnd:2.", "parameters": ["EPI.4", "EPI.5 (pre-registration)", "EPI.2"], "note": "The operative difference is the conception of novelty, which the schema does not encode (inference)."},
  {"@id": "pnl:dis:4", "topic": "Do model and data agree on every sign once Prop. 2 is corrected?", "positions": [{"perspective": "persp:R-TCE", "refs": ["r-tce:str:4", "r-tce:cmt:20"], "position": "yes"}, {"perspective": "persp:R-BEH", "refs": ["r-beh:cmt:22", "r-beh:fnd:21"], "position": "no: implied u effect about +0.056 at mean m", "severity": "fixable"}, {"perspective": "persp:R-DID", "refs": ["r-did:chl:6", "r-did:cmt:5"], "position": "asks authors to reconcile"}],
   "classification": "resolvable", "harness": "k*_u < 0 in every A3 draw (r-beh:chk:1); k*_u numerator = g1h0 - h1(s+g0) (r-did:chk:1); implied +0.056 reproduced (r-beh:chk:2); M3 uncertainty stars inconsistent in all four star checks.", "settledBy": "Signs: r-tce:str:4 is wrong on the uncertainty effect. Open: whether that effect differs from zero.", "probe": "Marginal effect of u across m with intervals, on a non-negative u (r-tce:chl:11)."},
  {"@id": "pnl:dis:5", "topic": "Standards: technological shift parameter or field-level institution?", "positions": [{"perspective": "persp:R-INST", "refs": ["r-inst:fnd:1", "r-inst:inc:3"], "severity": "damaging"}, {"perspective": "persp:R-BEH", "refs": ["r-beh:cmt:27", "r-beh:fnd:13"], "severity": "fixable"}, {"perspective": "persp:R-TCE", "refs": ["r-tce:vrd:5", "r-tce:fnd:5"], "position": "special case of TCE; mandates are a mediation problem"}, {"perspective": "persp:R-DID", "refs": ["r-did:fnd:2", "r-did:vrd:5"], "position": "correlated shocks; instrument; neutral on MI8"}],
   "classification": "fault line", "parameters": ["ONT.3", "ONT.1", "INF.6", "INF.2 MI8"], "note": "R-BEH's route (the manuscript's own cited typology) is checkable against ms:S1 and ms:S4. Narrowed claims diverge (r-tce:vrd:6 vs complementarity)."},
  {"@id": "pnl:dis:6", "topic": "Does fit to comparative statics entitle 'economizing'?", "positions": [{"perspective": "persp:R-TCE", "refs": ["r-tce:cmt:20", "r-tce:cmt:19"], "position": "yes by MI9, hold-up channel unshown"}, {"perspective": "persp:R-INST", "refs": ["r-inst:fnd:10"], "severity": "damaging"}, {"perspective": "persp:R-BEH", "refs": ["r-beh:fnd:1"], "severity": "damaging"}, {"perspective": "persp:R-DID", "refs": ["r-did:vrd:4"], "position": "fails on design grounds"}],
   "classification": "fault line", "parameters": ["INF.2 MI9", "INF.2 MI2", "ONT.5 choice-theoretic"]},
  {"@id": "pnl:dis:7", "topic": "Weight of the peer measure's construct validity", "positions": [{"perspective": "persp:R-TCE", "refs": ["r-tce:fnd:5"], "severity": "damaging"}, {"perspective": "persp:R-INST", "refs": ["r-inst:fnd:2"], "severity": "damaging"}, {"perspective": "persp:R-BEH", "refs": ["r-beh:fnd:3"], "severity": "damaging"}, {"perspective": "persp:R-DID", "refs": ["r-did:cmt:19", "r-did:fnd:10"], "severity": "minor"}],
   "classification": "fault line", "parameters": ["ONT.4", "ONT weight"], "note": "R-DID raises the identification side inside a fatal finding (r-did:fnd:2)."},
  {"@id": "pnl:dis:8", "topic": "Gravity of the staffing bad control", "positions": [{"perspective": "persp:R-TCE", "refs": ["r-tce:fnd:7"], "severity": "damaging"}, {"perspective": "persp:R-BEH", "refs": ["r-beh:fnd:18"], "severity": "damaging"}, {"perspective": "persp:R-INST", "refs": ["r-inst:fnd:14"], "severity": "fixable"}, {"perspective": "persp:R-DID", "refs": ["r-did:fnd:3"], "severity": "fixable"}],
   "classification": "idiosyncratic", "harness": "Premise shared: r-tce:chk:4 and r-did:chk:6 (scenario A) both show the coefficient surviving the control with no true effect; severity not settleable.", "note": "Allocation of one defect between findings; R-DID has the strictest TEC.3 and rates it lowest."},
  {"@id": "pnl:dis:9", "topic": "Gravity of the event-study defects", "positions": [{"perspective": "persp:R-DID", "refs": ["r-did:fnd:4"], "severity": "damaging"}, {"perspective": "persp:R-BEH", "refs": ["r-beh:fnd:5"], "severity": "damaging (with reverse causation)"}, {"perspective": "persp:R-TCE", "refs": ["r-tce:fnd:8"], "severity": "fixable"}, {"perspective": "persp:R-INST", "refs": ["r-inst:fnd:13", "r-inst:fnd:15"], "severity": "fixable"}],
   "classification": "fault line", "parameters": ["EPI.3", "INF.2 MI6", "TEC weight"], "harness": "r-did:chk:7 (static TWFE 0.031 vs ATT 0.165) bears on the shared premise only."},
  {"@id": "pnl:dis:10", "topic": "Specificity control: failed mechanism or estimator bias?", "positions": [{"perspective": "persp:R-TCE", "refs": ["r-tce:fnd:9", "r-tce:inc:5"], "severity": "damaging"}, {"perspective": "persp:R-INST", "refs": ["r-inst:fnd:10", "r-inst:inc:5"], "severity": "damaging"}, {"perspective": "persp:R-BEH", "refs": ["r-beh:fnd:14", "r-beh:inc:5"], "severity": "damaging"}, {"perspective": "persp:R-DID", "refs": ["r-did:fnd:12", "r-did:vrd:1"], "severity": "fixable"}],
   "classification": "fault line", "parameters": ["ONT weight", "EPI.3 (total effect as estimand)", "ONT.3 with INF.5 depth"], "note": "The condition (what the item measures) is settled by reading ms:S3.2; the severity is not."},
  {"@id": "pnl:dis:11", "topic": "Gravity of the legitimacy account", "positions": [{"perspective": "persp:R-INST", "refs": ["r-inst:fnd:9", "r-inst:cmt:26"], "severity": "damaging"}, {"perspective": "persp:R-BEH", "refs": ["r-beh:fnd:11"], "severity": "damaging"}, {"perspective": "persp:R-TCE", "refs": ["r-tce:fnd:3"], "severity": "fixable"}, {"perspective": "persp:R-DID", "refs": ["r-did:fnd:9", "r-did:fnd:17"], "severity": "fixable"}],
   "classification": "fault line", "parameters": ["INF.2 MI10", "ONT.1"], "residue": "R-BEH is neutral on MI10 yet rates it damaging (idiosyncratic component)."},
  {"@id": "pnl:dis:12", "topic": "Priority: fails or qualified?", "positions": [{"perspective": "persp:R-TCE", "refs": ["r-tce:vrd:4", "r-tce:fnd:15"], "verdict": "fails", "severity": "fixable"}, {"perspective": "persp:R-BEH", "refs": ["r-beh:vrd:6", "r-beh:fnd:15"], "verdict": "fails (provisional)", "severity": "fixable"}, {"perspective": "persp:R-INST", "refs": ["r-inst:ctb:5", "r-inst:fnd:4"], "verdict": "qualified (uncertain)", "severity": "damaging for the contribution"}, {"perspective": "persp:R-DID", "refs": ["r-did:vrd:6", "r-did:fnd:18"], "verdict": "qualified", "severity": "minor"}],
   "classification": "resolvable", "settledBy": "Verify the cited prior studies (to verify); apply pnl:agr:5 to 'adjudicate directly'.", "residue": "Severity: fault line on PRA.3 and PRA weight."},
  {"@id": "pnl:dis:13", "topic": "Verdict on pnl:ctb:3", "positions": [{"perspective": "persp:R-TCE", "refs": ["r-tce:vrd:3"], "verdict": "qualified"}, {"perspective": "persp:R-INST", "refs": ["r-inst:ctb:3"], "verdict": "qualified"}, {"perspective": "persp:R-BEH", "refs": ["r-beh:vrd:3"], "verdict": "fails"}, {"perspective": "persp:R-DID", "refs": ["r-did:vrd:3"], "verdict": "fails"}],
   "classification": "idiosyncratic", "note": "Individuation of the contribution; stated remnants coincide."},
  {"@id": "pnl:dis:14", "topic": "Verdict on pnl:ctb:8", "positions": [{"perspective": "persp:R-DID", "refs": ["r-did:vrd:7"], "verdict": "fails"}, {"perspective": "persp:R-TCE", "refs": ["r-tce:vrd:7"], "verdict": "qualified"}, {"perspective": "persp:R-INST", "refs": ["r-inst:ctb:7"], "verdict": "qualified"}, {"perspective": "persp:R-BEH", "refs": ["r-beh:vrd:7"], "verdict": "qualified"}],
   "classification": "idiosyncratic", "note": "Verdict convention for conditional claims; downstream of pnl:dis:2; finding minor for all."},
  {"@id": "pnl:dis:15", "topic": "What a function-level test discriminates", "positions": [{"perspective": "persp:R-TCE", "refs": ["r-tce:fnd:10", "r-tce:alt:1"], "position": "placebo in non-clinical functions, yet its production-cost variant predicts the largest effects there"}, {"perspective": "persp:R-DID", "refs": ["r-did:fnd:1"], "position": "placebo"}, {"perspective": "persp:R-INST", "refs": ["r-inst §5 obs. 1"], "position": "sharpest test against the bundle rival"}],
   "classification": "resolvable", "settledBy": "Closer reading: the test separates hold-up from both rivals but not the production-cost variant from the bundle.", "probe": "Pair it with cost consequences by adoption timing, certified-but-unused interfaces, or whether m rises only in outsourced functions."},
  {"@id": "pnl:dis:16", "topic": "Novelty of specificity-by-design", "positions": [{"perspective": "persp:R-INST", "refs": ["r-inst:ctb:6", "r-inst:fnd:5"], "verdict": "survives"}, {"perspective": "persp:R-TCE", "refs": ["r-tce:vrd:5"], "verdict": "qualified (anticipated)"}, {"perspective": "persp:R-BEH", "refs": ["r-beh:fnd:16", "r-beh:vrd:4"], "verdict": "qualified (anticipated)"}, {"perspective": "persp:R-DID", "refs": ["r-did:vrd:5"], "verdict": "qualified (untested)"}],
   "classification": "fault line", "parameters": ["PRA.2", "ONT.3"]},
  {"@id": "pnl:dis:17", "topic": "Within-hospital estimates against a field-level explanandum", "positions": [{"perspective": "persp:R-BEH", "refs": ["r-beh:fnd:2", "r-beh:cmt:28"], "severity": "damaging"}, {"perspective": "persp:R-TCE", "refs": ["r-tce:fnd:14"], "severity": "minor"}],
   "classification": "resolvable", "settledBy": "Decomposition with the authors' data (r-beh:chk:3; produced no output without data)."},
  {"@id": "pnl:dis:18", "topic": "Smallest peer effect of interest", "positions": [{"perspective": "persp:R-TCE", "refs": ["r-tce §6"], "position": "about 0.068"}, {"perspective": "persp:R-INST", "refs": ["r-inst §6"], "position": "about 0.046"}, {"perspective": "persp:R-DID", "refs": ["r-did §6"], "position": "about +/-0.03"}, {"perspective": "persp:R-BEH", "refs": ["r-beh step 6"], "position": "unstated"}],
   "classification": "idiosyncratic", "harness": "Smallest passable bound now about 0.104 (r-did:chk:4); every proposal fails now, so the dispute concerns the revision bar.", "note": "EPI.5 names equivalence tests but no parameter sets the bound."}
 ],
 "recommendationSpread": {
  "consensus": null,
  "note": "No consensus recommendation is produced (Role 3, instruction 4).",
  "spread": [
   {"perspective": "persp:R-TCE", "recommendation": "major revision", "movesToRejectIf": null},
   {"perspective": "persp:R-INST", "recommendation": "major revision", "movesToRejectIf": "headline claims kept without the analyses"},
   {"perspective": "persp:R-BEH", "recommendation": "major revision", "movesToRejectIf": "'rule out' kept and r-beh:fnd:4 unmet"},
   {"perspective": "persp:R-DID", "recommendation": "major revision, at the boundary with reject and resubmit", "movesToRejectIf": "editor treats building an identification strategy as beyond a revision"}
  ],
  "drivers": [
   "Identical labels, different conditions: wording plus tests (R-INST, R-BEH; pnl:dis:1) versus a new design (R-DID; pnl:dis:2).",
   "R-DID's boundary depends on PRA.6 (editor's brief), which no perspective sets.",
   "All fatal ratings are scoped to headline claims; none is fatal to H1 or to the corrected model."
  ],
  "fatalRatings": ["r-inst:fnd:7", "r-beh:fnd:4", "r-did:fnd:1", "r-did:fnd:2"],
  "preservedFindings": ["r-inst:fnd:7", "r-beh:fnd:4", "r-did:fnd:2", "r-did:fnd:1", "r-inst:fnd:1", "r-inst:fnd:4", "r-beh:fnd:2", "r-inst:fnd:10", "r-beh:fnd:1", "r-beh:fnd:3", "r-beh:fnd:12 (behavioral rival)", "r-tce:fnd:9 (production-cost channel)", "r-inst:fnd:9", "r-beh:fnd:11", "r-tce:fnd:7", "r-beh:fnd:18", "r-did:fnd:4", "r-beh:fnd:5"]
 },
 "focalReviewer": {
  "draft": "runs/02_reviewer_draft.md",
  "perspective": "persp:FOCAL",
  "draftRecommendation": "major revision",
  "matches": ["pnl:agr:1", "pnl:agr:2", "pnl:agr:4", "pnl:agr:5", "pnl:agr:9", "pnl:agr:10", "pnl:agr:11", "pnl:agr:12", "pnl:agr:13", "pnl:agr:15", "pnl:agr:16", "pnl:agr:18", "pnl:agr:19", "pnl:agr:23", "pnl:agr:25", "pnl:agr:27", "pnl:agr:28", "pnl:agr:29", "pnl:agr:31", "pnl:agr:32", "pnl:agr:33"],
  "robustFindingsLacking": ["pnl:agr:20", "pnl:agr:26", "pnl:agr:24"],
  "robustFindingsPartial": ["pnl:agr:14", "pnl:agr:7", "pnl:agr:8", "pnl:agr:6", "pnl:agr:17", "pnl:agr:21", "pnl:ctb:6 (robust contribution, not addressed as such)"],
  "otherLacking": ["pnl:agr:3"],
  "draftOnlyFindings": ["Abstract and conclusion omit the H2 result", "'Fashion' mixes motive with outcome", "Efficiency needs a selection argument (std:8)", "Marginal effect of m reaches zero near u of about 1.9 SD", "Peer-group selection does not arise", "A lag does not remove persistent conditions"],
  "faultLines": [
   {"disagreement": "pnl:dis:1", "draftPosition": "damaging (with R-TCE)", "focalSetting": "MI3 neutral; PRA.1 economists and sociologists"},
   {"disagreement": "pnl:dis:2", "draftPosition": "damaging (with R-TCE, R-BEH)", "focalSetting": "MI6 endorsed; EPI.3 design- and model-based"},
   {"disagreement": "pnl:dis:3", "draftPosition": "not a confirmation; a rescue (close to R-DID)", "focalSetting": "EPI.4 high; EPI.2 sophisticated falsificationism"},
   {"disagreement": "pnl:dis:5", "draftPosition": "not taken; deferred", "focalSetting": "ONT.1 includes fields, logics and legitimacy; ONT.5 constitutive admissible"},
   {"disagreement": "pnl:dis:6", "draftPosition": "unentitled via selection, fixable (with R-INST, R-BEH in substance)", "focalSetting": "MI9 neutral; ONT.3 includes selection"},
   {"disagreement": "pnl:dis:7", "draftPosition": "provisional; deferred", "focalSetting": "ONT.4 strict"},
   {"disagreement": "pnl:dis:10", "draftPosition": "estimator framing (with R-DID)", "focalSetting": "INF.5 depth; ONT weight 0.6"},
   {"disagreement": "pnl:dis:11", "draftPosition": "incompatibility argument, inside a damaging concern (with R-INST, R-BEH)", "focalSetting": "MI10 neutral"},
   {"disagreement": "pnl:dis:16", "draftPosition": "not addressed", "focalSetting": "PRA.2 problematization and gap-spotting"},
   {"disagreement": "pnl:agr:22 (MI4)", "draftPosition": "std:7 passes m and Phi as factual", "focalSetting": "MI4 neutral"},
   {"disagreement": "INF.6", "draftPosition": "eliminative repair (interval excluding 0.07)", "focalSetting": "eliminative accepted, assimilative suspect; unique in the panel"}
  ],
  "resolvableItems": [
   {"ref": "pnl:dis:4", "item": "The draft's 'if the stars are right' has a false antecedent per all four star checks; what remains is a wrong-signed, imprecise estimate."},
   {"ref": "pnl:dis:3", "item": "The draft's Phi-scale dependence on F is borne out."},
   {"ref": "r-did:inc:7", "item": "H3 as stated vs as tested; read ms:H3 against ms:S2.4."},
   {"ref": "pnl:dis:15", "item": "The draft's function-level test does not separate the production-cost variant from the institutional bundle."},
   {"ref": "pnl:dis:18", "item": "The draft's 0.07 bound is the most lenient in the panel; all bounds fail now."}
  ],
  "presentation": ["Remove the draft's first line ('bs:T7 settled: ...'), a workbench note."]
 }
}
```

## Annex. `pnl:chk:1`: survival scores and verdict divergence against distance

Not run. It recomputes §2 and the statistics in §4.3, using only `numpy`, `pandas` and `scipy`. Until the harness reports, the correlations in §4.3 are `asserted`.

Expected output, if this synthesis is right:
- Scores 0.5, 0.5, 0.25, 0.0, 0.125, 0.625, 0.25, 0.375.
- Robust: `pnl:ctb:1`, `2` and `6`. Fails for all: `pnl:ctb:4`.
- Same-verdict counts: R-TCE/R-INST 6, R-TCE/R-BEH 6, R-TCE/R-DID 5, R-INST/R-BEH 4, R-INST/R-DID 5, R-BEH/R-DID 5.
- As stated: Pearson r ≈ −0.42 (p ≈ 0.4) and Spearman ρ ≈ −0.65 (p ≈ 0.16).
- Sensitivity run: Pearson r ≈ −0.20.
- Lens-dependent: none, at both thresholds.

```python
import pandas as pd
from scipy import stats

SCORE = {"s": 1.0, "q": 0.5, "f": 0.0}
rows = [f"pnl:ctb:{i}" for i in range(1, 9)]
V = pd.DataFrame({
    "R-TCE":  ["q", "q", "q", "f", "f", "q", "f", "q"],
    "R-INST": ["q", "q", "q", "f", "f", "s", "q", "q"],
    "R-BEH":  ["q", "q", "f", "f", "q", "q", "f", "q"],
    "R-DID":  ["q", "q", "f", "f", "f", "q", "q", "f"],
}, index=rows)
S = V.apply(lambda col: col.map(SCORE))

table = pd.DataFrame({
    "score": S.mean(axis=1),
    "robust": (S >= 0.5).all(axis=1),
    "fails_for_all": (S == 0.0).all(axis=1),
    "survivors": S.apply(lambda r: ",".join(r.index[r.values >= 0.5]), axis=1),
})
print(table.to_string())

dist = {("R-TCE", "R-INST"): 0.68, ("R-TCE", "R-BEH"): 0.45, ("R-TCE", "R-DID"): 0.36,
        ("R-INST", "R-BEH"): 0.42, ("R-INST", "R-DID"): 0.65, ("R-BEH", "R-DID"): 0.43}

def divergence(scores):
    out = [{"pair": f"{a}/{b}", "distance": d,
            "same_verdict": int((scores[a] == scores[b]).sum()),
            "mean_abs_diff": float((scores[a] - scores[b]).abs().mean())}
           for (a, b), d in dist.items()]
    return pd.DataFrame(out).sort_values("distance")

S_alt = S.copy()
S_alt.loc["pnl:ctb:3", ["R-BEH", "R-DID"]] = 0.5   # score pnl:ctb:3 by the remnants R-BEH and R-DID state
for label, scores in [("as stated", S), ("sensitivity: pnl:ctb:3 scored by stated remnants", S_alt)]:
    P = divergence(scores)
    r, p = stats.pearsonr(P["distance"], P["mean_abs_diff"])
    rho, p_s = stats.spearmanr(P["distance"], P["mean_abs_diff"])
    print(f"\n[{label}]\n{P.to_string(index=False)}")
    print(f"Pearson r = {r:+.3f} (p = {p:.2f}); Spearman rho = {rho:+.3f} (p = {p_s:.2f}); n = {len(P)} pairs")

# Lens-dependent: stands (>= 0.5) for two or more reviewers but not all, with every survivor pair within the threshold
for thr in (0.40, 0.45):
    flagged = []
    for c in rows:
        surv = [k for k in S.columns if S.loc[c, k] >= 0.5]
        if 2 <= len(surv) < S.shape[1]:
            pairs = [dist.get((a, b), dist.get((b, a))) for i, a in enumerate(surv) for b in surv[i + 1:]]
            if all(d <= thr for d in pairs):
                flagged.append(c)
    print(f"threshold {thr}: lens-dependent ->", flagged or "none")
```

## Decisions for the reviewer

1. **Alignment.** Accept or modify the three judgement calls in §1. They move only the scores of `pnl:ctb:3` and `pnl:ctb:5`; `pnl:chk:1` reports both ways.
2. **`pnl:dis:1`.** Decide whether the rule-out problem is fatal or damaging in your review. Three of four simulated lenses rate it fatal, scoped to the title claim; the resembling lens and your draft rate it damaging. Decide also which claim you read as central.
3. **`pnl:dis:2`.** Your MI6 endorsement places you with R-TCE. Decide whether to anticipate R-DID's fatal rating in the review or in the note to the editor.
4. **`pnl:dis:3` and `pnl:dis:4`.** Decide how to describe the corrected interaction. Then restate your "if the stars are right" point: the star is wrong in all four star checks, so the remaining tension is a wrong-signed, imprecise estimate.
5. **`pnl:dis:5`.** Decide whether to engage R-INST's objection that standards are institutions, or to leave it to an institutional co-reviewer. Your perspective admits fields, logics and legitimacy (ONT.1).
6. **MI4 (`pnl:agr:22`).** Decide whether your std:7 pass for m holds against the decoupling reading.
7. **Robust findings the draft lacks** (§6.2): `pnl:agr:20`, `pnl:agr:26` and `pnl:agr:24`, plus the consequence in `pnl:agr:14`. Accept or reject each.
8. **Literature.** Verify Loh & Venkatraman 1992 and Ang & Cummings 1997, and the other candidates marked "to verify", before citing any. Four simulations naming the same works are not four independent recalls.
9. **Preserved minority findings** (§5). Decide which to raise. Candidates: `r-beh:fnd:2` (field-level explanandum), the production-cost channel in `r-tce:fnd:9`, and the behavioral rival in `r-beh:fnd:12`.
10. **Provenance.** Have `r-tce_chk_1_b2.out.txt` relabelled as the output of `r-tce:chk:2` before citing it. Treat `r-beh:chk:3` and `r-beh:chk:4` as not run.
11. **`pnl:chk:1`.** Have the harness run it before anyone relies on the distance observations in §4.3.
12. **Presentation.** Remove the first line of your draft ("bs:T7 settled: ...").
13. **Recommendation.** The panel offers no consensus. All four labels are "major revision", under different conditions (§5). The recommendation is yours.
