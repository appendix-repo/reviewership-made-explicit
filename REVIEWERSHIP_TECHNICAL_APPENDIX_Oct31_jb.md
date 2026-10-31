# Technical Appendix: Reviewership Made Explicit

*Supplement to the Stage 1 proposal "Reviewership Made Explicit," submitted to the Organization Science Special Issue: AI-Enabled Frontiers in Organizational Science. This appendix gives the full specification of the reviewing perspective and of the suite's capabilities, the Project Lakatos components they are composed from, the instruction sets, worked transcripts of every capability run on a test manuscript (including executable checks and an end-to-end provenance trace), the draft schema and measured quantities, the governance and consent protocol, the design of the base-model dependence study with a small pilot, and the design of the two-track critical test. It supersedes the compressed descriptions in the proposal, which refer to this document.*

**Contents**

0. Reading guide and glossary
1. The reviewing perspective: five dimensions
2. Capability specifications: Best-Self reviewer (2.1), simulated reviewers (2.2), panel synthesis (2.3), adversarial probes (2.4), provenance layer (2.5), multi-LLM gateway (2.6), the workbench loop (2.7)
3. Foundations in Project Lakatos
4. Worked transcripts (Runs 01 to 14), with the verification of every citation the runs flagged
5. Schema (draft v0.1) and measured quantities
6. Governance and consent protocol
7. Base-model dependence study, with a pilot
8. The critical test: a two-track open call
9. Opening the platform, risks and how each is measured, status of components, and where each commitment of the proposal is met

References · Annex A: schema and JSON-LD context · Annex B: the test manuscript and the sealed defect key · Annex C: manifest of the transcripts and check code (the full transcripts are in the supplementary file `REVIEWERSHIP_ANNEX_C_TRANSCRIPTS.md`, which is also in the repository, and as separate files in `runs/`) · Annex D: Project Lakatos Tables 1 to 4 · Annex E: consent instruments

*The repository, at https://github.com/appendix-repo/reviewership-made-explicit, holds every file referred to here: `instruction-sets/`, `schema/`, `case/`, `runs/`, `tools/`, `governance/` and `lakatos/`.*

---

## 0. Reading guide and glossary

The suite has **three reviewer-facing capabilities**: the Best-Self reviewer, simulated reviewers (with panel synthesis), and adversarial probes. They are served through a **fourth capability, the multi-LLM gateway**, and every contribution they make is recorded by a **provenance layer**, which is infrastructure rather than an agent. The capabilities are realized as **four agent roles** (Best-Self Elicitor, Simulated Reviewer, Panel Synthesizer, Adversarial Probe), each an instruction set that composes already-specified Project Lakatos components: the thirteen cognitive operators (Lakatos Appendix A, Table 2), the discourse grammar (Table 3), the twelve routine research agents (Table 1), and the seventeen classes of scholarly-role agent (Table 4, here numbered L1 to L17). All four tables are reproduced in Annex D.

Every capability is parameterized by the **reviewing perspective**, defined on **five dimensions**: ontological, epistemological, inferential, technical and pragmatic (Section 1).

| Term | Meaning in this appendix |
|---|---|
| Reviewing perspective | The configuration of commitments a reviewer brings to a manuscript: a setting of parameters on the five dimensions, a weight for each dimension, the material inferences the reviewer endorses or rejects, and a list of checkable standards. Serialized as a `ReviewingPerspective` object (Section 5). |
| Inferential scorekeeping | Following Brandom (1994, 2000): keeping track, as reasons are given and asked for, of what each party is committed to, what they are entitled to, and which of their commitments are incompatible. The suite treats reviewing as scorekeeping on a manuscript. |
| Commitment | What a manuscript commits its authors to. *Avowed* if stated; *consequential* if it follows from avowed commitments by an inference the scorekeeper endorses. |
| Entitlement | Whether the authors have the right to a commitment: by argument, by evidence, by deference to cited work, or by default (an unchallenged background commitment of the field). |
| Unentitled commitment | A commitment that has been challenged and for which the manuscript offers nothing that would meet the challenge. The primary target of the adversarial probes. |
| Incompatibility | Two commitments that cannot both be held. |
| Material inference | An inference whose goodness depends on the content of its terms rather than on logical form (Sellars 1953; Brandom 2000, ch. 2): for example, from "this investment is specific to the relationship" to "this party is exposed to hold-up". Traditions differ in which material inferences they treat as good without argument; Section 1 catalogues ten. |
| Scoreboard | The record of commitments, entitlements, incompatibilities and challenges that one scorekeeper attributes to a manuscript. Scoreboards are perspectival: two scorekeepers endorsing different material inferences attribute different consequential commitments to the same text. |
| Standards specification | The output of the Best-Self reviewer: a reviewer's own perspective made explicit and checkable, with the editor's brief. It is not a review. |
| Lens | The configuration of a simulated reviewer: a perspective, a short canonical corpus, and its relation (resembling or differing) to the focal reviewer's perspective. |
| Probe | A targeted interrogation of a manuscript of one of six types (derivation, identification, numerical consistency, measurement, inferential audit, literature and placement). |
| Executable check | Code that settles a formal, computational or numerical claim. A finding bound to a check is `demonstrated` or `refuted-by-check` only when the harness has run the check. |
| Capability-bound / stylistic | Properties of a review that respectively do and do not improve with base-model potency once style is held fixed (Section 7 gives the pre-registered rule). |
| Human-likeness / inferential validity | Two separate axes on which reviews are scored: how far a review reads as one a human expert would write, and how far its inferential moves are correct. They are never combined into one score. |

**Counts used throughout.** Five dimensions; three reviewer-facing capabilities plus the gateway (four capabilities); four agent roles; one provenance layer; seventeen Table 4 agent classes; thirteen Table 2 operators; twelve Table 1 routine agents.

---

## 1. The reviewing perspective: five dimensions

### 1.1 Why five dimensions, and why these

A reviewer's judgment of a manuscript depends on more than the manuscript. It depends on what the reviewer takes there to be (the entities and constructs a theory may posit), on what the reviewer counts as evidence and as knowing, on which inferences the reviewer accepts as good, on how the reviewer treats code, models and estimators, and on whom the reviewer takes the manuscript to be addressing and what would count as a contribution to them. These are the five dimensions:

| Dimension | What it governs | Primary grounding |
|---|---|---|
| **Ontological (ONT)** | What there is: the entities, categories and constructs a manuscript may admit, how constructs are individuated, at what level of analysis, under which model classes | Lakatos Table 3 (ontological commitments; commitments to model classes) |
| **Epistemological (EPI)** | What counts as knowing and as evidence: stance, logic of corroboration, identification standard, novelty versus accommodation, evidential and measurement standards. This is what reviewers usually call "methodological" | Lakatos Table 3 (epistemological stances; logics of corroboration); Lakatos (1970) on novel facts |
| **Inferential (INF)** | Which transitions from reasons to claims count as good: admitted modes of inference (deductive, inductive, abductive), the material inferences a tradition treats as good, the standard of derivation, tolerance for unstated premises, explanatory and justification norms, the handling of rivals | Brandom (1994, 2000) on material inference; Lakatos Table 3 (logical and meta-logical norms; explanatory norms; justification strategies) |
| **Technical (TEC)** | The development, design and deployment of algorithms, code, estimators, simulations and formal models: reproducibility, how deep the reviewer checks (re-derive, re-run, re-simulate), estimator discipline, numerical consistency | The proposal's commitment that formal and computational claims be bound to executable checks |
| **Pragmatic (PRA)** | The pragmatics of discourse: the audience whose scorekeeping counts, the conversation the manuscript joins, what counts as a contribution to it, how contribution and priority claims are placed, and the norms governing the review itself | Brandom (1994) on scorekeeping as a social practice; Price (2011, 2013) on the functions a vocabulary performs |

Three design choices determine this list.

**Technical and pragmatic are kept apart.** Both concern practice rather than content, but different practices. The technical dimension is about the practice of computation: whether a derivation goes through, whether an estimator identifies what it is said to identify, whether reported numbers cohere. The pragmatic dimension is about the practice of discourse: to whom a claim is addressed and what it does in their conversation. A reviewer can be exacting on one and relaxed on the other, and the suite's capabilities divide along this line: adversarial probes bound to executable checks live mainly on the technical dimension, while the Best-Self reviewer's editor exchange and the placement probes live on the pragmatic one.

**Logical norms belong to the inferential dimension.** Formal validity is one standard of good inference among others. Keeping "logical" and "inferential" as separate dimensions would make them near-synonyms. The inferential dimension instead records which modes of inference a reviewer admits and where, so that a deductive proof, an inductive generalization and an abductive inference to the best explanation are each held to their own standard, and a reviewer can require that abductive moves not be dressed as deductive ones.

**Theoretical and methodological commitments are a lower layer.** A theory already brings constructs (ontological), a logic of explanation and an inferential structure (inferential), and a stance on what would corroborate it (epistemological). A methodology brings standards of identification and measurement (epistemological) and of estimation and computation (technical). These composites are what reviewers usually talk about, and the suite reports them, but it defines them from the five dimensions rather than treating them as dimensions on the same plane:

| Lower-layer notion | Composed from |
|---|---|
| Theoretical commitments | ONT (constructs, categories, level, model class) + INF (explanatory logic, inferential structure, material inferences) + EPI.4 (novel prediction versus accommodation) |
| Methodological commitments | EPI (identification, corroboration, measurement) + TEC (estimation, computation, reproducibility) |
| Logical norms | INF.1 and INF.3 |
| Data and empirical materials | EPI.6 (measurement) and TEC (reproducibility, numerical consistency) |

### 1.2 Parameters

Each dimension is set by parameters with admissible values. The parameter set is v0.1: it was written to cover the distinctions organizational reviewers draw most often and will be revised from usage data (Section 4.12 records the first revisions the runs suggest).

| Code | Parameter | Admissible values |
|---|---|---|
| ONT.1 | Admissible entities | Any of: rational or boundedly rational actors; routines and capabilities; networks and structures; fields, logics and legitimacy; populations; technologies and artifacts; coalitions; embedded actors |
| ONT.2 | Level-of-analysis standard | Same level required / cross-level with explicit bridging / indifferent |
| ONT.3 | Causal ontology | Individual-mechanistic / structural / selection / constitutive |
| ONT.4 | Construct-individuation standard | Strict / moderate / loose |
| ONT.5 | Model classes | Causal, choice-theoretic, functional, selection, constitutive: each preferred / admissible / suspect |
| EPI.1 | Stance (Table 3) | Positivism / realism / instrumentalism / constructivism / pragmatism |
| EPI.2 | Logic of corroboration (Table 3) | Inductivism (frequentist or Bayesian) / falsificationism (naive or sophisticated) |
| EPI.3 | Identification standard | Any of: design-based; model-based; process-tracing; comparative-historical |
| EPI.4 | Novelty standard | Weight on novel prediction over accommodation: high / medium / low |
| EPI.5 | Evidential standards | Any of: effect sizes; intervals and equivalence tests; robustness; pre-registration |
| EPI.6 | Measurement standard | Multi-informant or validated measures preferred / single informant acceptable |
| INF.1 | Admitted inference modes | Deductive, inductive, abductive, with where each is acceptable and whether abductive moves must be labeled (free text) |
| INF.2 | Material inferences | Endorsed, rejected or neutral on each catalogue entry (MI1 to MI10, below) |
| INF.3 | Derivation standard | Proof / sketch / verbal argument |
| INF.4 | Enthymeme tolerance | Low / medium / high |
| INF.5 | Explanatory norm (Table 3) | Depth / coverage |
| INF.6 | Justification strategies (Table 3) | Reductive, eliminative, assimilative: each accepted / suspect |
| INF.7 | Rival-handling standard | Rivals stated in their strongest form and tested on discriminating predictions: required / preferred / not required |
| TEC.1 | Reproducibility standard | Code and data required / preferred / not expected |
| TEC.2 | Checking depth | Any of: re-derive; re-run; re-simulate; spot-check; trust |
| TEC.3 | Estimator discipline | Very high / high / moderate / low |
| TEC.4 | Numerical-consistency checking | Always / sometimes / never |
| TEC.5 | Formal-model standard | Closed form required / simulation acceptable with verification |
| PRA.1 | Audience | The community whose scorekeeping counts (free text) |
| PRA.2 | Contribution standard | Gap-spotting / problematization (Alvesson & Sandberg 2011) / "interesting" (Davis 1971) |
| PRA.3 | Placement standard | Priority and positioning claims checked: always / sometimes / never |
| PRA.4 | Relevance standard | Weight on implications for practice: high / medium / low |
| PRA.5 | Discursive norms of the review | Free text (e.g., separate fatal from fixable; be specific) |
| PRA.6 | Editor's brief | What this editor needs from this reviewer (filled by the Best-Self editor exchange) |

### 1.3 The catalogue of material inferences

The inferential dimension is where perspectives differ most consequentially, because the material inferences a reviewer endorses determine which consequential commitments the reviewer attributes to a manuscript. Two reviewers reading the same sentence keep different scores on it. The v0.1 catalogue lists ten inferences that some organizational traditions treat as good without further argument and others challenge:

| Id | Material inference | Typically endorsed by |
|---|---|---|
| MI1 | Relationship-specific investment → exposure to hold-up → hierarchy economizes on that exposure | Transaction-cost economics |
| MI2 | A practice that persists under competition is approximately efficient | Some economic and evolutionary traditions |
| MI3 | Spread of a practice among peers under uncertainty → imitation of referents perceived as legitimate or successful | Institutional theory |
| MI4 | Formal adoption of a practice does not imply its implementation (decoupling) | Institutional and behavioral traditions |
| MI5 | Organizations adapt by local search triggered by performance below aspiration | Behavioral theory of the firm |
| MI6 | Within-unit variation over time, with unit and period fixed effects, identifies a causal effect absent time-varying confounders | Much applied panel work; rejected as sufficient by design-based econometrics |
| MI7 | A non-significant coefficient after adding a control means the variable has no effect | Widespread in practice; rejected by most methodologists |
| MI8 | Standardized interfaces reduce the relationship-specificity of assets | Modularity and transaction-cost research |
| MI9 | Choice-theoretic models in equilibrium imply that observed structures are optimal responses | Organizational economics |
| MI10 | Legitimacy is a resource whose loss threatens survival, independently of efficiency | Institutional theory |

A new entry is admitted when two published works in different traditions disagree about whether the inference is good, and the disagreement can be stated as a single conditional. The catalogue is therefore a map of the field's inferential fault lines, and it grows with use.

### 1.4 Perspectives as points, and their distance

A perspective is a point in the space the parameters define. This is what makes the proposal's phrase "reviewers whose commitments differ from, or resemble, the focal reviewer's" measurable. The draft perspective distance (Section 5.3) compares two perspectives parameter by parameter, averages within each dimension, and weights the dimensions by the two reviewers' mean weights. For the focal reviewer's perspective as elicited in Run 01 (`runs/configs/focal_perspective_normalized.json`) and the four simulated reviewers used in Section 4 (`runs/configs/simulated_perspectives.json`), the distances are:

| Pair | ONT | EPI | INF | TEC | PRA | Overall | Opposed inferences |
|---|---|---|---|---|---|---|---|
| FOCAL – R-TCE | 0.27 | 0.39 | 0.31 | 0.50 | 0.17 | 0.35 | none |
| FOCAL – R-INST | 0.61 | 0.65 | 0.50 | 0.33 | 0.50 | 0.53 | none |
| FOCAL – R-BEH | 0.39 | 0.42 | 0.38 | 0.43 | 0.50 | 0.42 | none |
| FOCAL – R-DID | 0.57 | 0.79 | 0.25 | 0.30 | 0.17 | 0.45 | MI6 |
| R-TCE – R-INST | 0.70 | 0.79 | 0.70 | 0.47 | 0.67 | 0.68 | MI3, MI9, MI10 |
| R-TCE – R-BEH | 0.33 | 0.69 | 0.31 | 0.40 | 0.50 | 0.45 | MI9 |
| R-TCE – R-DID | 0.34 | 0.50 | 0.11 | 0.60 | 0.00 | 0.36 | MI6 |
| R-INST – R-BEH | 0.56 | 0.31 | 0.41 | 0.20 | 0.50 | 0.42 | none |
| R-INST – R-DID | 0.80 | 0.65 | 0.61 | 0.53 | 0.67 | 0.65 | none |
| R-BEH – R-DID | 0.39 | 0.58 | 0.32 | 0.33 | 0.50 | 0.43 | none |

The computation is `tools/perspective_distance.py`. The four lenses were configured before the elicitation, from the stand-in reviewer's persona, with R-TCE meant to resemble the focal reviewer and the other three to differ. The elicited perspective bears this out: R-TCE is the nearest (0.35) and R-INST the farthest (0.53). The table also shows something the configuration did not intend. R-DID is close to the focal reviewer on the inferential dimension (0.25) and far on the epistemological (0.79). A panel built only on the overall distance would miss that, which is why distances are reported by dimension. But the dimension distances also hide something, which the panel synthesis exposed (Section 4.5): the focal reviewer endorses MI6 (fixed effects identify a causal effect) and R-DID rejects it, and the sharpest disagreement in the panel turns on exactly that inference, yet reversing one stance moves the inferential distance by less than 0.02. A single material inference can carry a disagreement that an average over parameters cannot show. The distance is therefore reported together with the list of material inferences on which two perspectives take opposite stances (Section 5.3; the last column of the table was added to the tool after Run 07, and no distance changed).

---

## 2. Capability specifications

The suite has three reviewer-facing capabilities, as the proposal says: the Best-Self reviewer (2.1), simulating other reviewers (2.2, with their synthesis into a panel, 2.3), and adversarial probes (2.4). They are recorded by the provenance layer (2.5), served through the multi-LLM gateway (2.6), and bound into a workbench (2.7); these three are infrastructure, not agents. Each capability is specified on a common template: function; grounding; inputs and outputs, typed against the schema in Section 5; composition from Project Lakatos components (detailed in Section 3); human decision points; failure modes and safeguards; and evaluation. The instruction sets are in `instruction-sets/REVIEWERSHIP_INSTRUCTION_SETS.md` (v0.1) and are reproduced in substance here. The common preamble binds every role to eight rules, of which four carry most of the weight: the human reviewer decides and signs; every claim cites its locus in the manuscript; formal, computational and numerical claims are demonstrated by a check, not asserted; and every objection names the commitment, the missing entitlement or incompatibility, and the repair, with "no material finding" an acceptable output.

### 2.1 The Best-Self reviewer

**Function.** An elicitation instrument. Before the reviewer reads the manuscript, and informed by a short exchange with the handling editor about what the paper needs, it helps the reviewer assemble their own standards across the five dimensions: the inferential standards they hold but forget under time pressure, the checks they perform on their best days, the commitments of their home tradition they would want interrogated. The output is a **standards specification**, not a review of the paper. After the reviewer has drafted their review, the same agent checks the draft against the specification.

**Grounding.** Brandom's account of scorekeeping makes the standards a scorekeeper applies part of what it is to be that scorekeeper: making them explicit is making explicit what was implicit in the reviewer's practice (Brandom 1994). The design also answers a familiar finding about expert judgment, that experts apply their own standards inconsistently across occasions, and that externalizing the standards narrows the gap.

**Inputs.** The invitation (title, abstract, editor's note); the editor's answers; the reviewer's answers. In Mode C, the reviewer's draft review.
**Outputs.** `EditorBrief`; `StandardsSpecification` (five dimension settings, weights, 10 to 16 standards each with dimension, parameter, checkable statement, priority and origin, the tensions between standards and the reviewer's ranking of them); in Mode C, a `ConsistencyReport`.

**Procedure.** *Mode E*: at most four questions to the editor, in one message (main contribution, why this reviewer, the editor's concerns, journal and process), summarized as the editor brief. *Mode S*: three rounds with the reviewer: recall (the review they are proudest of, a decisive rejection, the checks they skip under pressure); a dimension-by-dimension proposal of settings and standards, including at most two standards per dimension that a demanding reviewer in the field would hold and the reviewer did not mention, marked as suggestions; and sharpening, where each accepted standard is made checkable and tensions between standards are ranked. *Mode C*: for each standard, applied, partial or not applied, with the passage; `must` standards silently skipped; standards the draft uses but did not declare; internal inconsistencies; whether the editor's brief is answered.

**Composition.** L4 Deconstructor (intra), applied to the reviewer's own statements, extracts the warrants presupposed by what they say they value; L2 Challenger (intra) proposes the standards a demanding reviewer in the field would hold; L17 RadianX records the elicitation as a dialogue tree; Justify(X,Y) ties each standard to the reason the reviewer gives for it; the Table 3 grammar supplies the vocabulary for ONT, EPI and INF settings.

**Human decision points.** The editor's answers; every proposed standard (accept, reject, rewrite); the five weights; the ranking of tensions; in Mode C, whether to apply skipped standards and whether to adopt undeclared ones. All are provenance events.

**Failure modes and safeguards.** *Substitution by elicitation*: the agent writes the reviewer's standards for them. Safeguard: suggested standards are labeled with their origin, capped at two per dimension, and must be explicitly accepted; the specification records the share of standards of each origin. *Leakage*: the elicitor reads the manuscript and smuggles findings into the standards. Safeguard: the elicitor never receives the manuscript. The editor brief is a second channel for leakage, because the editor has read the manuscript; Section 4.0 shows this happening in the demonstration. *Mode C as ghost-writing*: the consistency check rewrites the review. Safeguard: it reports, it does not draft.

**Evaluation.** (i) Reviewer recognition: whether reviewers judge the specification a sharper statement of their own standards (a rating, collected in the open-call study, Section 8); (ii) the standards coverage of the final review against the specification; (iii) whether reviews written with a specification are rated higher on inferential validity than the same reviewers' reviews without one, in the base-model and critical-test designs.

### 2.2 Simulated reviewers

**Function.** Instantiates reviewers whose perspectives differ from, or resemble, the focal reviewer's, so that the reviewer (or editor) can see how the same manuscript reads through configurations of commitments other than their own. Which contributions survive across perspectives, and which are artifacts of one school, becomes visible.

**Grounding.** Scorekeeping is perspectival (Brandom 1994, ch. 8): a scorekeeper attributes to others the consequential commitments that follow by the inferences *the scorekeeper* endorses. Simulated reviewers with different material-inference settings (INF.2) therefore keep different scores on the same text, and their disagreements should trace to those settings. That is the empirical content of the claim that simulated disagreements "track real theoretical fault lines".

**Configuration.** A `ReviewingPerspective` (five settings, weights, material inferences), a lens label, a short canonical corpus, and the relation to the focal reviewer (resembling or differing, with the perspective distance). Each simulated review is labeled `simulated` in the schema and is never sent to authors as a review.

**Outputs.** `SimulatedReview`: claimed contributions; a scoreboard; findings by dimension, in order of weight, each with severity, commitment, missing entitlement or incompatibility, and repair; a verdict on each contribution (survives, qualified, fails) with a restatement in the lens's own terms; the strongest rival explanation and the observation that would discriminate it; what would change the simulated reviewer's mind; a recommendation; and the two or three parameters that drive its verdicts.

**Composition.** L2 and L3 Challengers (intra and inter); L16 ArgDef (cross-field defeaters); L6 Arbiter (claims checked against the tradition's canonical findings); L5 Deconstructor (inter: what would have to hold for the manuscript to persuade this tradition); L1 Translator/Re-Voicer (restating each contribution in the tradition's terms); L10 AltGen and L11 AltGenX (rival explanations); L12 AltGenM (the manuscript's model re-specified in the tradition's model class); the Summarizer/Conclusion Builder routine agent (the claimed contributions); Represent, Challenge, Refute, Corroborate, and Reduce, Assimilate or Eliminate where the tradition would treat the result as a special case, absorb it, or explain it away.

**Human decision points.** Which lenses to instantiate (the workbench proposes a default set covering the dimensions with the largest distances from the focal perspective, always including one resembling and one maximally differing lens); which simulated findings, if any, the reviewer adopts.

**Failure modes and safeguards.** *Caricature*: a simulated tradition is a stereotype of itself. Safeguard: lens corpora are curated by members of the tradition, and lenses are validated against the published critical record before release. *Spurious disagreement*: perspectives differ for the sake of differing. Safeguard: the panel synthesis classifies every disagreement and reports the share traceable to named parameters. *Homogenization of judgment*: the opposite risk, that every reviewer's simulated panel is the same. Safeguard: lenses are pluggable (Section 2.6) and the platform measures the diversity of assisted reviews (Section 5.3).

**Evaluation.** (i) The fault-line share: the proportion of disagreements between simulated reviewers that coders, blind to the perspectives, trace to a named parameter difference; (ii) expert judgment of whether each simulated review is recognizably of its tradition; (iii) agreement between simulated and real reviewers of the same tradition on the same manuscript, in the open-call study.

### 2.3 Panel synthesis

**Function.** Composes the simulated reviews (and optionally the focal reviewer's draft) into a panel: a composed board of alternative selves the reviewer can confront before finalizing.

**Outputs.** `PanelSynthesis`: a survival table with each contribution's cross-perspective survival score (survives 1, qualified 0.5, fails 0, averaged over reviewers) and a classification as **robust** (survives or is qualified for every reviewer) or **lens-dependent** (survives only for reviewers close to each other); the agreements; a disagreement map classifying each disagreement as a **fault line** (traceable to a named parameter difference; neither side in error), **resolvable** (one side is wrong in a way a check or closer reading would settle; a probe is recommended) or **idiosyncratic**; the spread of recommendations; and, if a draft is supplied, what the focal reviewer faces.

**Rule.** The synthesis never averages the recommendations and never tells the reviewer which side of a fault line to take. Minority findings rated fatal or damaging are preserved.

**Composition.** L17 RadianX (the panel as a structured dialogue); L5 Deconstructor (inter: whether a disagreement reflects incommensurable standards or a resolvable error); L13 PrisM (questions a reader from another tradition would ask); Integrate(X,Y) applied to evaluations; Corroborate(X,Y).

**Human decision points.** Which resolvable disagreements to send to a probe; which fault-line objections to anticipate in the review.

**Failure modes and safeguards.** *Consensus by stealth*: the synthesis drifts toward a single verdict. Safeguard: the recommendation spread is reported, not summarized. *Mislabeling a resolvable error as a fault line*, which would excuse a mistake as a difference of perspective. Safeguard: every fault line must cite the parameters on which the reviewers differ; a disagreement with no such parameter is not a fault line.

**Evaluation.** Coder agreement with the synthesis's classification of disagreements; whether contributions classified robust are rated more favorably by real reviewers from all traditions in the open-call study.

### 2.4 Adversarial probes

**Function.** Targeted interrogations of a manuscript's models, data and arguments, hunting for commitments incurred without entitlement and for inferential transitions a competent scorekeeper would challenge. Where claims are formal or computational, probes are bound to executable checks, so that "this derivation does not go through" or "this estimate is not identified under the stated assumptions" is demonstrated, not asserted.

**Probe types.**

| Code | Probe | Hunts for | Binding |
|---|---|---|---|
| P-DER | Derivation | Propositions that do not follow from the stated assumptions; dropped terms; signs; hidden auxiliaries | Symbolic re-derivation |
| P-ID | Identification | Estimates that do not identify the stated quantity under the stated assumptions: bad controls, colliders, reverse timing, staggered-adoption bias | Simulation from a data-generating process built from the manuscript's **own** stated relations |
| P-NUM | Numerical consistency | Reported statistics inconsistent with each other: estimates, standard errors, significance marks, sample sizes | Arithmetic recomputation |
| P-MEAS | Measurement | Measures that do not capture the construct as the theory, or its rival, defines it | Argued |
| P-INF | Inferential audit | Unentitled commitments, non-sequiturs, abductive moves dressed as deductive, incompatible commitments, conclusions broader than their evidence | Scoreboard |
| P-LIT | Literature and placement | Priority and positioning claims; omitted prior or rival work | Literature search where available; otherwise flagged |

**The check harness.** The probe writes each check as a self-contained `CheckSpec`; it does not run it. The harness (a sandboxed Python environment with `sympy`, `numpy`, `scipy`, `statsmodels`, `pandas`) runs the check and returns a `CheckResult`; the probe then disposes of the finding as `demonstrated`, `refuted-by-check` or `inconclusive`. A check must build its premises from the manuscript's own statements and cite them: the point of binding is that the authors' own commitments, not the probe's preferred theory, entail the failure. This is the inferentialist reading of a demonstration: the authors are shown to be committed to something incompatible with what they assert.

**Grounding.** Brandom's scorekeeping (unentitled commitments and incompatibilities); Toulmin's (1958) argument structure for the audit; Lakatos (1970) for accommodation dressed as prediction; for executable binding, the general principle that a language model's assent to a derivation is not evidence that the derivation holds.

**Composition.** L14 ArgMap and L15 ArgDef; L6 Arbiter; L8 Model Expander/Contractor (which results survive removing or adding an assumption); L9 Meta-Analyzer (plausibility of reported magnitudes); L7 Referee (the observation that would discriminate the claim from its rival); routine agents Proof Verifier, Proof Synthesizer, Data Specifier: Causal, Data Interpreter (Descriptive, Inferential and Causal), Modeling Assistant: Refiner, Targeted Literature Review; operators Challenge, Refute, Explain(X,Y;L), Measure(X,Y;M), Extend(X,Y).

**Human decision points.** Which probes to run and on what; acceptance, rejection or modification of every finding before anything enters a review.

**Failure modes and safeguards.** *Objection theater*: fluent, generic, empty critique. Safeguard: the rubric requires commitment, missing entitlement and repair for every finding; generic findings fail validation. *Sycophancy*: softening real failures. Safeguard: the severity scale is fixed, and bound findings take their status from the harness, not the probe. *False demonstration*: a check that encodes the probe's own assumptions rather than the manuscript's. Safeguard: each check cites the manuscript passages its premises come from, and the reviewer sees the code.

**Evaluation.** Seeded-defect recovery and demonstration rate on manuscripts with sealed defect keys (Section 5.3); false-alarm rate; expert rating of unseeded findings as substantive, minor or mistaken; incremental validity over unassisted human review (Section 8).

### 2.5 The provenance layer

**Function.** Records every agent contribution and every human decision as an append-only, hash-chained sequence of `ProvenanceEvent`s, so that the human and machine division of labor in any assisted review is a matter of inspectable record rather than a disclosure statement.

**Record.** Each event carries a timestamp and whether it is actual or reconstructed; the actor (human, agent, harness, or, in demonstrations, a stand-in), with base model, gateway route and instruction-set version for agents; the action (ingest, seal, elicit, specify, simulate, synthesize, probe, check, consistency-check, draft, accept, reject, modify, include, sign, score, annotate, delete); input and output ids; the event it responds to; a rationale; the SHA-256 hash of any content it registers; the previous event's hash; and its own hash over its canonical JSON.

**Views.** The *reviewer view* is the full trace. The *editor view*, attached to a signed review, lists which agent outputs were consulted, which findings the reviewer accepted, rejected or modified, and which passages of the signed review originated in agent output (by string overlap above a threshold), with the share of the review so originating. The *author view* is a one-paragraph statement of the capabilities used and the reviewer's attestation (Section 6.7). The *research view* is the de-identified trace, available only under the study protocol.

**Composition.** L17 RadianX is the precursor: it records dialogues as trees of assertions, questions and responses. The provenance layer generalizes this to every transformation and human decision, and adds hash-chaining.

**Evaluation.** Completeness (every agent output and human decision in a session is an event); and whether editors who see the editor view judge the human contribution to a review more accurately than editors who see only a disclosure statement (Section 8, secondary outcome).

### 2.6 The multi-LLM gateway

**Function.** Serves the suite across base models of differing potency, so that the same reviewing task can be run on different models and base-model potency becomes an experimental variable (Section 7).

**Architecture (Stage 1 build).** Hosted at [institution]. Components: (i) a router exposing one interface to all roles, with the base model a per-call parameter; (ii) a model roster of open-weight models served on institution-controlled hardware and closed models reached only through enterprise endpoints whose terms exclude retention and training (Section 6.4); (iii) a manuscript store, encrypted, holding manuscript text only for consented manuscripts and only for the retention window; (iv) the check harness, sandboxed, without network access; (v) the provenance layer; (vi) a lens registry holding versioned perspectives and corpora. Every call logs the model's exact version string, the instruction-set version, the prompt hash and the output hash; manuscript text is never written to logs.

**Pluggable lenses.** A new lens enters the registry by supplying a perspective in the schema, a curated corpus of at least ten works, and passing a validation check against the tradition's published critical record. The lens set is a contested, extensible commons, which is the architectural answer to the homogenization risk.

**Evaluation.** Reproducibility: the same task, model version and inputs return outputs whose findings agree above a pre-registered threshold across repeated calls (reported per model in Section 7).

### 2.7 The workbench loop

The capabilities are bound into a loop under the reviewer's direction. The default order is shown; the reviewer can invoke any capability at any point, and every arrow is a provenance event.

```
 invitation ──► [Best-Self, Mode E] ◄──► EDITOR answers ──► editor brief
                         │
                         ▼
               [Best-Self, Mode S] ◄──► REVIEWER answers ──► standards specification
                         │
                         ▼
          REVIEWER reads the manuscript and drafts (unassisted)
                         │
        ┌────────────────┼──────────────────────────────┐
        ▼                ▼                              ▼
 [Simulated reviewers]  [Adversarial probes] ──► [check harness]
        │                │   findings: asserted / demonstrated / refuted
        ▼                │
 [Panel synthesis] ──────┤  (resolvable disagreements → probes)
        │                │
        ▼                ▼
 [Best-Self, Mode C: consistency check of the draft]
                         │
                         ▼
 REVIEWER accepts / rejects / modifies each finding, revises, signs
                         │
                         ▼
 [Provenance: full trace; editor view attached to the signed review]
```

**Gates.** Four points require an explicit human decision: the editor's answers; the reviewer's acceptance of the standards specification; the disposition of every finding before it can enter the review; and the signature. The reviewer drafts before seeing any agent's view of the manuscript, so that the draft records the reviewer's own reading; this ordering is also what makes the Mode C check meaningful.

**Status.** The roles are specified as instruction sets and exercised individually and in sequence (Section 4). The orchestration software that binds them, routes objects between them and writes the provenance record is Stage 1 work.

---

## 3. Foundations in Project Lakatos

The four roles are not built from scratch. Each composes components of Project Lakatos, a program of agent design for the social and behavioral sciences whose components are documented in four tables, reproduced in full in Annex D (and in `lakatos/LAKATOS_TABLES_1-4.md`):

- **Table 1:** twelve routine research agents (literature review, data interpretation and specification, modeling assistance, proof verification and synthesis, summarization);
- **Table 2:** thirteen typed cognitive operators (Represent, Explain, Justify, Extend, Corroborate, Measure, Integrate, Augment, Challenge, Refute, Reduce, Assimilate, Eliminate);
- **Table 3:** a discourse grammar for epistemological stances, logics of corroboration, ontological and modeling norms, explanatory norms, justification strategies, and logical norms of inference;
- **Table 4:** seventeen classes of scholarly-role agent, intra- and inter-disciplinary, numbered here L1 to L17.

Table 4 already contains a reviewer: **L2, the Challenger/Interrogator (intra)**, "emulates the critical stance of peer reviewers within the same field" and "helps researchers anticipate critiques likely to arise during the review process." The suite generalizes L2 in three directions: from one implicit stance to an explicit, parameterized perspective (Section 1); from one reviewer to a panel of differing perspectives; and from critique on the model's authority to findings bound to executable checks.

The Table 3 grammar supplies most of the vocabulary of the ontological, epistemological and inferential dimensions (Section 1.2 marks which parameters come from it). The technical and pragmatic dimensions extend the grammar: Table 3 has no category for the practice of computation or for the pragmatics of addressing a community, and the suite needs both.

### 3.1 Role-by-role mapping

| Role | Scholarly-role agents (Table 4) | Operators (Table 2) | Routine agents (Table 1) | What the composition contributes |
|---|---|---|---|---|
| **Best-Self Elicitor** (capability 1) | L4 Deconstructor (intra), applied to the reviewer's own statements; L2 Challenger (intra); L17 RadianX | Justify | (none) | L4 recovers the warrants presupposed by what the reviewer says they value, which become candidate standards; L2 proposes the standards a demanding reviewer in the field would hold; Justify ties each standard to the reviewer's reason; L17 records the elicitation as a dialogue tree |
| **Simulated Reviewer** (capability 2) | L2 and L3 Challengers; L16 ArgDef (cross-field); L6 Arbiter; L5 Deconstructor (inter); L1 Translator/Re-Voicer; L10 AltGen; L11 AltGenX; L12 AltGenM; L7 Referee | Represent; Challenge; Refute; Corroborate; Reduce; Assimilate; Eliminate | Summarizer/Conclusion Builder (claimed contributions); Synthetic Literature Review (lens corpus synopsis); Modeling Assistant: Exploratory (with L12) | L2/L3/L16 give the tradition's objections and defeaters; L6 checks claims against its canonical findings; L1 restates contributions in its terms, which is how survival is judged; L10–L12 give rival explanations and model re-specifications; L7 names the discriminating observation; Reduce, Assimilate and Eliminate name what the tradition would do with the result |
| **Panel Synthesizer** (capability 2) | L17 RadianX; L5 Deconstructor (inter); L13 PrisM | Integrate; Corroborate | (none) | L17 structures the panel as a dialogue; L5 decides whether a disagreement is incommensurable (a fault line) or resolvable; L13 anticipates cross-tradition questions; Integrate composes evaluations without averaging them |
| **Adversarial Probe** (capability 3) | L14 ArgMap; L15 ArgDef (intra); L6 Arbiter; L8 Model Expander/Contractor; L9 Meta-Analyzer; L7 Referee; L4 Deconstructor (intra) | Explain (inferential logic L); Challenge; Refute; Measure; Extend; Augment | Proof Verifier; Proof Synthesizer; Modeling Assistant: Refiner; Data Specifier: Causal; Data Interpreter: Descriptive, Inferential and Causal; Targeted Literature Review | L14/L15 map the argument and generate defeaters; Explain(X,Y;L) classifies each step as deductive, inductive or abductive, which catches abductive moves dressed as deductive; L8 and Augment test which results survive adding or removing an assumption; the proof agents re-derive (P-DER); Data Specifier: Causal builds the causal graph implied by the manuscript's own statements, which the identification checks simulate (P-ID); Data Interpreter: Descriptive recomputes reported statistics (P-NUM); Measure tests construct–measure fit (P-MEAS); Targeted Literature Review tests priority claims (P-LIT) |
| **Provenance layer** (not an agent) | L17 RadianX | (none) | (none) | RadianX's dialogue tree generalized to every transformation and human decision, with hash-chaining |
| **Gateway** (not an agent) | (none) | (none) | Exploratory Literature Review (assembling lens corpora for the registry) | Lens corpora are assembled with the routine agent and curated by members of each tradition |

### 3.2 Coverage audit

Every Table 4 class, every Table 2 operator and every Table 1 routine agent is used by at least one role.

| Lakatos component | Used by |
|---|---|
| L1 Translator/Re-Voicer | Simulated Reviewer |
| L2 Challenger (intra) | Best-Self Elicitor, Simulated Reviewer |
| L3 Challenger (inter) | Simulated Reviewer |
| L4 Deconstructor (intra) | Best-Self Elicitor, Adversarial Probe |
| L5 Deconstructor (inter) | Simulated Reviewer, Panel Synthesizer |
| L6 Arbiter | Simulated Reviewer, Adversarial Probe |
| L7 Referee | Simulated Reviewer, Adversarial Probe |
| L8 Model Expander/Contractor | Adversarial Probe |
| L9 Meta-Analyzer | Adversarial Probe |
| L10 AltGen, L11 AltGenX, L12 AltGenM | Simulated Reviewer |
| L13 PrisM | Panel Synthesizer |
| L14 ArgMap, L15 ArgDef (intra) | Adversarial Probe |
| L16 ArgDef (cross-field) | Simulated Reviewer |
| L17 RadianX | Best-Self Elicitor, Panel Synthesizer, provenance layer |
| Represent | Simulated Reviewer (the scoreboard) |
| Explain | Adversarial Probe |
| Justify | Best-Self Elicitor |
| Extend | Adversarial Probe (conclusions extended beyond their evidence) |
| Corroborate | Simulated Reviewer, Panel Synthesizer |
| Measure | Adversarial Probe (P-MEAS) |
| Integrate | Panel Synthesizer |
| Augment | Adversarial Probe (with L8) |
| Challenge, Refute | Simulated Reviewer, Adversarial Probe |
| Reduce, Assimilate, Eliminate | Simulated Reviewer |
| Literature review agents (3) | Gateway (Exploratory), Simulated Reviewer (Synthetic), Adversarial Probe (Targeted) |
| Data Interpreter (3), Data Specifier: Causal | Adversarial Probe |
| Modeling Assistant: Exploratory | Simulated Reviewer (with L12) |
| Modeling Assistant: Refiner, Proof Verifier, Proof Synthesizer | Adversarial Probe |
| Summarizer/Conclusion Builder | Simulated Reviewer (the claimed-contributions list with which every review begins) |

---

## 4. Worked transcripts (Runs 01 to 14)

This section runs every capability on one test manuscript, in the order of the workbench loop (Section 2.7), and reports what each produced. The transcripts are in `runs/`, unedited, and are summarized here with their key passages. The section answers the proposal's statement that "the current instruction sets and worked transcripts are in the accompanying repository", and it is the first test of the instruction sets, the schema and the check harness.

| Run | Capability | Role or actor | Output |
|---|---|---|---|
| 01 | Best-Self reviewer, Modes E and S | Elicitor; editor and reviewer stand-ins | `runs/01_dialogue/` (9 turns, 3 stand-in notes); standards specification |
| 02 | (unassisted) | Reviewer stand-in | `runs/02_reviewer_draft.md`, with a stand-in note |
| 03–06 | Simulated reviewers | Four lenses: transaction-cost (resembling), institutional, behavioral, design-based (differing) | `runs/03_…` to `06_…`; harness outputs in `runs/03_checks/` to `06_checks/` |
| 07 | Panel synthesis | Panel Synthesizer | `runs/07_panel_synthesis.md` |
| 08–10 | Adversarial probes | P-DER; P-ID and P-NUM; P-INF, P-MEAS and P-LIT | `runs/08_…` to `10_…`, each in two parts (before and after the harness); harness outputs in `runs/08_checks/` to `10_checks/` |
| 11 | Best-Self reviewer, Mode C | Elicitor | `runs/11_consistency_check.md` |
| 12 | Dispositions and signed review | Reviewer stand-in | `runs/12_reviewer_dispositions_final_review.md`, with a stand-in note |
| 13 | Base-model pilot (Section 7.9) | Three model tiers × two styles; blind scorer | `runs/13_pilot/` |
| 14 | Provenance trace and editor view | Provenance layer (file-based stand-in) | `runs/provenance_events.json`; `runs/14_machine_origin.json`; `runs/14_editor_view.md` |

### 4.0 How the runs were produced, and what they can and cannot show

**No human took part.** The proposal's workbench has two human participants, the handling editor and the reviewer. In these runs **both were played by Claude**, each as a separate agent instance given a persona (`instruction-sets/REVIEWERSHIP_INSTRUCTION_SETS.md`, Section S): a handling editor who has read the manuscript once, quickly; and an associate professor of strategy who works in transaction-cost economics with an econometric bent, reviews in about an hour, and re-derives models "on good days". Wherever this section says "the editor" or "the reviewer", it means these stand-ins. Each stand-in returned an out-of-role note with each turn, saying where it thought it departed from what a human in the role would do; the notes are published verbatim beside the turns. What the runs show is that the roles produce outputs of the intended kind, that the objects pass between them, and that the checks run. They do not show how human editors and reviewers respond to the workbench. That is what the critical test (Section 8) is for, and whether human reviewers find their elicited standards "sharper and more checkable than a reviewer's first statement of them", as the proposal claims, is tested there, not here.

**Who did what.** One orchestrating Claude session wrote the test manuscript and its sealed defect key, configured the four simulated perspectives, built each role's prompt from the instruction set (`instruction-sets/REVIEWERSHIP_INSTRUCTION_SETS.md`, v0.1), relayed messages between the elicitor and the stand-ins, ran the check harness, and logged every step. Every role ran as a separate Claude agent instance (model family Claude, Anthropic, as served on 23 October 2026) that read only its own prompt and the files named in it. The elicitor never saw the manuscript. Only two agents ever saw the sealed key: the blind scorer of the base-model pilot and the scorer of seeded-defect recovery (Section 4.10).

**Checks.** No role ran its own code. Every role that made a formal, computational or numerical claim wrote a self-contained Python check; the harness (`tools/harness.py`) extracted the checks, ran each in an isolated interpreter with an empty environment, no network and a 120-second limit, and returned the output; the probe then disposed of each finding in a second part. Checks written by the simulated reviewers were run the same way, but simulated reviews have no second part, so their findings stay as written.

**Single, unedited runs.** Each run was made once. The transcripts are as the agents wrote them, with one exception: the elicitor's perspective block in its specification did not follow the schema (it used `type` and `id` for `@type` and `@id` and nested the values differently), and the orchestrator normalized it into `runs/configs/focal_perspective_normalized.json` without changing any setting, recorded as provenance event `ev:29`.

**Departures and leaks, all disclosed.**
1. **The editor brief leaked findings into the elicitation.** The editor stand-in, asked for its concerns, named the spending-share outcome against a function-level model, the "wrong-way" uncertainty interaction, the single same-state peer measure, the gap between losing significance and "ruling out", and the legitimacy explanation in a paper that rules out institutional accounts (`turn_02_editor.md`). These touch six of the nine seeded defects (SD1, SD3, SD4, SD5, SD8, SD9). The elicitor passed them into the brief, and three of the standards it suggested (clustering, bounds on claims of absence, peer influence against shared conditions) bear on them. The reviewer stand-in noticed this itself ("I can't unread those … please don't fit my standards to those specifics", `turn_04_reviewer_S1.md`). Section 4.12 discusses what this means for the design.
2. **The editor stand-in found the main seeded defect and withheld it in role.** Its out-of-role note says it re-derived Proposition 2 and found the sign error, and kept it out of its answers because the persona had read the paper only quickly (`turn_02_editor_standin_note.md`).
3. **The invitation's editor's note** ("I would value your reading of the transaction-cost model and the empirical design. The paper makes strong claims against the institutional account.") was written by the orchestrator.
4. **The reviewer's request to see the editor's own answers** was declined, as the protocol provides (`turn_07_elicitor_S3.md`).
5. **The orchestrator wrote both the key and the lens configurations.** To limit contamination, standards in the lens configurations that mirrored seeded defects were removed before any run. Two traces remain: the design-based lens's corpus includes work on bad controls (Cinelli, Forney and Pearl), and no lens corpus includes the three prior studies named under SD7.
6. **The reviewer stand-in is not a realistic one-hour reviewer.** Its own note on the draft says that the volume of checks in the draft "is at or past what a human can do in an hour" (`runs/02_reviewer_draft_standin_note.md`). Section 4.12 discusses the consequence: the unassisted draft already locates all nine seeded defects (Section 4.10).
7. **Timestamps.** Events were logged as they happened. Where an event was logged after the fact (agent completions that arrived later), its time is reconstructed from the output file's save time and marked `reconstructed` in the trace. The trace is in append order, so a few reconstructed events appear after events that happened later.
8. **Citations.** No agent had a search tool. Every work an agent was unsure of is marked "(to verify)" in the transcripts, and every such work is checked in Section 4.11.

### 4.1 The test case

The manuscript (`case/TEST_MANUSCRIPT.md`, 2,744 words; Annex B) is synthetic, written for this demonstration in the format of an organization-science submission: "Modularity, Not Mimicry: Interoperability Standards and the Diffusion of IT Outsourcing in U.S. Hospitals". It develops a transaction-cost model in which interoperability standards make hospital IT functions modular and so lower effective asset specificity. A function of nominal asset specificity $k$ is outsourced when $k$ is below the threshold $k^* = (s+G(u))/\big(H(u)(1-m)\big)$, where $s$ is the vendor's production-cost advantage, $m$ is modularity (effective specificity is $k(1-m)$), $H(u) = h_0 + h_1 u$ is the hold-up hazard per unit of effective specificity, $G(u) = g_0 + g_1 u$ is the cost of in-house adaptation, and $u$ is environmental uncertainty. Proposition 1 (modularity raises the threshold) follows. Proposition 2 (uncertainty amplifies the modularity effect) is asserted under Assumption A3, $h_1/h_0 > g_1/(s+g_0)$. The empirical part is a fixed-effects panel of 412 hospitals, 2009–2019, with four models in Table 2: modularity predicts the outsourced share of IT spending (H1); the modularity × uncertainty interaction is negative, which the paper calls "contrary to H2" and explains by legitimacy pressures; and a same-state peer-outsourcing coefficient loses significance once modularity is added (H3), from which the paper concludes that the results "rule out mimetic isomorphism". It claims to be "the first study to adjudicate directly between transaction-cost and institutional explanations of IT outsourcing". No data exist; the numbers in Table 2 were written to be internally consistent except where a defect is seeded.

The **sealed defect key** (`case/SEALED_DEFECT_KEY.md`; Annex B) lists nine seeded defects, spread across the five dimensions, each with its locus, what is wrong, what a reviewer must say for it to count as *located*, and whether a check can demonstrate it:

| Id | Dimension | Defect | Demonstrable by a check |
|---|---|---|---|
| SD1 | TEC, INF | The proof of Proposition 2 holds $H$ constant in $u$; the correct cross-partial is negative under the paper's own A3 | Yes |
| SD2 | EPI, TEC | Model 4 controls for in-house IT staffing, which the paper says outsourcing reduces: a bad control | Yes |
| SD3 | INF, EPI | A non-significant peer coefficient, 0.042 (0.038), is read as refuting the rival; its interval reaches 0.116 | Yes |
| SD4 | ONT, PRA | A same-state peer mean does not capture mimetic isomorphism's referents (chosen by status, success, similarity or ties); the rival's uncertainty contingency is untested | No |
| SD5 | EPI | The legitimacy explanation of the H2 result is introduced after the fact and called "consistent with our theory" | No |
| SD6 | TEC | (a) 0.084 (0.051) is starred \*\*\* at p ≈ 0.10; (b) 412 hospitals × 11 years is 4,532 observations, not 4,712 | Yes |
| SD7 | PRA | The priority claim ignores prior work (Loh & Venkatraman 1992; Ang & Cummings 1997; Roberts & Greenwood 1997) | Partly (literature) |
| SD8 | ONT | The model is about functions; the test is on hospital spending shares, with no bridging assumptions | Partly |
| SD9 | INF | The paper rules out institutional pressures and then explains its interaction by legitimacy pressures | No |

The key also lists five known weaknesses that were not seeded (two-way fixed effects with staggered adoption; reverse timing between modularity and outsourcing; single-informant measures; survivorship in a balanced panel; the corner where $k^* \geq 1$). Both files were hashed with SHA-256 and the hashes recorded (`case/HASHES.txt`; provenance `ev:1`, `ev:2`) before any role ran: manuscript `a8ab4709…52d0`, key `970e0574…809d`. Both hashes still match.

### 4.2 Run 01: the Best-Self elicitation (Modes E and S)

**Inputs.** The elicitor had the invitation only: the title, the abstract and the editor's note. The editor stand-in had the manuscript. The reviewer stand-in had the invitation, and later the elicitor's messages.

| Turn | From → to | Content | Words | Event |
|---|---|---|---|---|
| 01 | Elicitor → editor | Mode E: four questions (main contribution, ranking five candidate claims quoted from the abstract; why this reviewer; the editor's concerns; journal and process) and a draft brief | 863 | `ev:3` |
| 02 | Editor → elicitor | Answers: rank the model–test link first and the case against the rival second; re-derive the model; reasoned reading of identification with spot checks; two concerns; generalist readership | 816 | `ev:4` |
| 03 | Elicitor → reviewer | The editor brief and Mode S Round 1 (recall) | 1,751 | `ev:5` |
| 04 | Reviewer → elicitor | Proudest review (an Ashenfelter dip found by asking where the identifying variation came from); a rejection (moderation hypotheses that did not follow from the theory); the checks skipped under pressure | 1,751 | `ev:6` |
| 05 | Elicitor → reviewer | Round 2: settings for the five dimensions, 16 candidate standards with the reviewer's words that suggested each, suggested standards marked, weights requested | 3,978 | `ev:7` |
| 06 | Reviewer → elicitor | Accepts, rejects and rewrites each; sets weights ONT 0.6, EPI 0.9, INF 0.9, TEC 0.7, PRA 0.4 | 2,246 | `ev:8` |
| 07 | Elicitor → reviewer | Round 3: each standard made checkable; seven tensions to rank | 4,886 | `ev:11` |
| 08 | Reviewer → elicitor | Rankings, sharpening, a shedding order for when time runs short | 2,399 | `ev:19` |
| 09 | Elicitor | The standards specification | 9,509 | `ev:28` |

**From recollection to checkable standard.** Round 1 asks for episodes, not principles. The reviewer's decisive rejection was of a transaction-cost paper whose moderation hypotheses rested on an unstated assumption: "A hypothesis that does not follow from the theory cannot test it." By Round 3 this had become `std:1`, a must standard with four conditions: the hypothesis follows from a stated proposition or proof; every assumption that fixes a predicted sign, including an interaction's, is stated and defended, with no "as if" defense for the assumption that does the work; where the theory's unit differs from the test's, the aggregation step is stated and each sign shown to survive it on the scale tested; and a hypothesis that fails these is labeled exploratory and counts neither for nor against the theory. Condition (c) was the elicitor's suggestion, which the reviewer folded in. Similarly, the reviewer's list of checks skipped under time pressure ("Re-deriving proofs. Under pressure I check only that each proposition's sign makes intuitive sense") became two must standards, `std:5` (re-derive each proposition by hand) and `std:6` (a stated minimum set of numerical spot checks), and the reviewer's own diagnosis ("The checks I skip are the ones that catch an internally inconsistent paper") became the reason for their weight.

**The specification** (`turn_09_elicitor_SPEC.md`; summarized in `runs/configs/focal_perspective_normalized.json` for the perspective). It is labeled a specification, not a review (`isReview: false`), and it contains no finding about the manuscript.

| | Count |
|---|---|
| Standards | 16: INF 4, EPI 5, TEC 3, ONT 2, PRA 2 |
| Priority | 9 must; 3 must in part (std:3, std:6, std:7); 2 should but must in stated conditions (std:8, std:13); 2 should (std:14, std:16) |
| Origin | 13 the reviewer's own; 3 suggested by the elicitor and rewritten by the reviewer (std:9 clustering, std:13 bounds on claims of absence, std:14 peer influence against shared conditions); none accepted unchanged |
| Tensions | 7, ranked by the reviewer (e.g. `bs:T1`: a failed prediction counts against the model as stated, not against a broader theory that does not entail it; a repaired derivation that flips the sign after the fact counts as a rescue). One, `bs:T7`, was left open and settled by the reviewer in the first line of the draft: "must means must" |
| Material inferences | Endorses MI1 (hold-up) and MI6 (fixed-effects identification); rejects MI7 (non-significance means no effect) |
| Working rules | Failures go in the body; passes go in a "Checks run" list of under 150 words; derivations are done by hand in the draft and checked by the harness afterwards; a shedding order if time runs short |

**What Run 01 shows.** The elicitation turns recollected practice into checkable standards, records the origin of each, and leaves the reviewer in charge of every standard. It also shows the leak the protocol must close: the brief carried the editor's reading of this manuscript into standards that are supposed to be the reviewer's own (Section 4.12).

### 4.3 Run 02: the reviewer's unassisted draft

The reviewer stand-in read the manuscript and the specification only, with no code and no other capability, and wrote a review in the persona's single sitting (`runs/02_reviewer_draft.md`; 1,567 words with headings and the checks list; the stand-in estimates about 1,200 in the body). It recommends **major revision** on four major concerns:

1. "P2 does not follow; under the paper's own A3 its sign is reversed": a correct hand derivation of the cross-partial, $\partial^2 k^*/\partial m\,\partial u = [g_1 H - h_1(s+G)]/[H^2(1-m)^2]$, negative under A3; the missing aggregation step; the legitimacy explanation as an after-the-fact mechanism that is also institutional.
2. "The test of the rival does not discriminate": mediation, shared state conditions, a noisy peer measure; an interval for the peer coefficient that includes a smallest effect of interest fixed in advance at half the Model 1 estimate; the unweighted state mean does not match the paper's own statement of the rival.
3. Identification of the modularity effect: direction, two bad controls (in-house staffing; and asset specificity, which is the theory's own channel), the event study under staggered adoption, and the state requirements as an instrument.
4. "Economizing" as an efficiency claim without a selection argument.

Minor concerns include the N arithmetic, the marginal effect of modularity crossing zero near u = 1.9 SD, and the priority claim (Ang and Cummings 1997, "to verify"). A "Checks run" list records the passes: Proposition 1 re-derived, 16 t-ratios and stars checked (one discrepancy), N checked, magnitudes confirmed.

The stand-in's note lists what it noticed but left out for length or because the persona would plausibly not have found it in an hour (a peer × uncertainty test, the fit of the uncertainty measure, spending weights that move with sourcing, the corner case, the within-R² jump when staffing enters), and what it included that such a reviewer might well have missed (the follow-up check that the corrected model implies a negative uncertainty main effect; the specificity control as the theory's own mechanism; the volume of checks). That note is the main evidence that the stand-in outperforms the persona it plays.

### 4.4 Runs 03–06: four simulated reviewers

Each simulated reviewer was configured with a perspective (`runs/configs/simulated_perspectives.json`), a lens label, a canonical corpus and its relation to the focal reviewer, and it read the manuscript. The perspectives were written before the elicitation, from the reviewer's persona; the distances in Section 1.4 show that the configuration achieved its aim (R-TCE nearest the elicited focal perspective, R-INST farthest).

| | R-TCE (resembling) | R-INST (differing) | R-BEH (differing) | R-DID (differing) |
|---|---|---|---|---|
| Lens | Transaction-cost economist (strategy) | Institutional theorist (organizational sociology) | Behavioral theorist (Carnegie tradition) | Design-based empirical economist |
| Highest weights | EPI 0.9, INF 0.9 | ONT 0.9, PRA 0.8 | ONT, EPI, INF 0.7 | EPI 1.0, TEC 1.0 |
| Material inferences | Endorses MI1, MI6, MI8, MI9; rejects MI3, MI7, MI10 | Endorses MI3, MI4, MI10; rejects MI2, MI7, MI9 | Endorses MI4, MI5; rejects MI2, MI7, MI9 | Rejects MI6, MI7 |
| Words | 8,266 | 8,939 | 8,855 | 9,585 |
| Contributions: survives / qualified / fails | 0 / 5 / 2 | 1 / 5 / 1 | 0 / 5 / 2 | 0 / 4 / 3 |
| Fatal findings | none | "rule out" (MI7) | "rule out" (MI7) | the causal claim (no design); "rule out" (MI7) |
| Recommendation | Major revision | Major revision | Major revision | Major revision, "at the boundary with reject" |
| Parameters it names as driving its verdicts | INF.3 proof with TEC.2 re-derive; MI7 rejected; TEC.3 high | ONT.3 constitutive with fields and legitimacy admitted; MI7, MI9 rejected and MI3, MI4 endorsed; INF.7 rivals required | MI7 rejected; ONT.5 choice-theoretic suspect with MI2, MI9 rejected; MI5 endorsed | EPI.3 design-based with MI6 rejected; MI7 rejected; TEC.3 very high |

**How the lenses read the same paper differently.** The resembling lens re-voices the model as "a shift parameter in Williamson's (1991) reduced-form comparison of governance costs" and finds its strongest rival inside its own tradition: hospitals decided to buy because vendors' production costs fell, then installed certified interfaces as a contractual safeguard, so that technology and governance were chosen together. It names the sharpest discriminating observation, a function-level pattern: the hold-up account predicts the modularity effect concentrated in high-specificity clinical applications, the production-cost variant in commodity functions such as hosting. The institutional lens treats standards and mandates as institutions, so that "the manuscript's own explanans has coercive institutional origins", and it is the only lens for which one contribution survives unqualified: the idea that standards produce asset specificity, which "an organizational-sociology readership would value". The behavioral lens asks whether outsourcing was triggered by performance below aspiration, proposes the test (a modularity effect concentrated in hospitals below aspiration), and notes that year effects absorb the field-level diffusion the paper sets out to explain. The design-based lens accepts nothing as causal without a design: the fixed-effects estimates become "evidence of an association", and the state requirements become the only route to identification.

**Where they agree, and why.** All four found the Proposition 2 sign error, wrote a symbolic check for it, and saw that the corrected model predicts the interaction the authors report as anomalous. All four reject MI7 and so reject "rule out". The behavioral lens says why the first agreement is not a fact about perspectives: "the most consequential formal finding does not depend on the lens. It comes from TEC.2 (re-derive) and INF.3, and any scorekeeper who re-derives should reach it." Section 4.12 takes up the uncomfortable corollary, that the institutional lens re-derived the model although its configuration says it spot-checks.

### 4.5 Run 07: the panel synthesis

The Panel Synthesizer read the four simulated reviews, their 18 harness outputs and the reviewer's unassisted draft. It did not read the manuscript (`runs/07_panel_synthesis.md`). It aligns the four reviews' contributions into one list, scores their survival, maps agreement and disagreement, reports the spread of recommendations without forming a consensus, and ends with what the focal reviewer faces. Its own statistics were marked asserted until its one check, `pnl:chk:1`, ran. The harness ran that check after the synthesis was written (`runs/07_checks/`, event `ev:34`), and every number matched what the synthesizer had asserted.

**Survival across lenses.** Survives = 1, qualified = 0.5, fails = 0, averaged over the four reviewers.

| Contribution (as aligned by the panel) | R-TCE | R-INST | R-BEH | R-DID | Score | Classification |
|---|---|---|---|---|---|---|
| `pnl:ctb:1` The model, Props. 1–2 | qualified | qualified | qualified | qualified | 0.50 | robust |
| `pnl:ctb:2` The test against the institutional rival | qualified | qualified | qualified | qualified | 0.50 | robust |
| `pnl:ctb:3` Peer effects "disappear" once modularity is measured | qualified | qualified | fails | fails | 0.25 | neither |
| `pnl:ctb:4` The results "rule out mimetic isomorphism" | fails | fails | fails | fails | 0.00 | fails for every lens |
| `pnl:ctb:5` A practice read as fashion is "economizing" | fails | fails | qualified | fails | 0.125 | neither |
| `pnl:ctb:6` Specificity is partly a product of interface design | qualified | **survives** | qualified | qualified | 0.625 | robust |
| `pnl:ctb:7` "The first study to adjudicate directly" | fails | qualified | fails | qualified | 0.25 | neither |
| `pnl:ctb:8` The practice implication | qualified | qualified | qualified | fails | 0.375 | neither |

The counts in Section 4.4 are each lens's verdicts on its own list of seven contributions. The panel aligned the four lists into the eight contributions above, so the columns here do not reproduce those counts.

What survives, survives narrowed, and the four narrowings converge: Proposition 1 holds and Proposition 2 holds only with its sign reversed; H1 holds as a within-hospital association, but the test against the rival does not discriminate; and the idea that standards make specificity a design variable stands, but its novelty is contested and its empirical premise (that modularity lowers measured specificity) is untested. The headline claim of the title fails under every lens. **No contribution is lens-dependent**: where verdicts split, the reviewers who let a contribution stand are far apart, not close (for example, `pnl:ctb:3` stands for R-TCE and R-INST, the farthest pair).

**Agreement.** Twenty-seven findings are raised by two or more lenses about the same locus for the same reason (`pnl:agr:1` to `27`), with six agreed strengths, repairs and probes. The synthesizer noticed that all four lenses' rival accounts share one structure, modularity and outsourcing chosen together, which is why the same two probes (function-level analysis, and the timing of modularity against outsourcing) recur across the panel.

**Disagreement: fault lines, resolvable errors and noise.** The map has 18 entries. Ten are **fault lines**, each traced to the parameters on which the reviewers differ. Four are **resolvable**: a misreading of signs, a literature check, an inconsistency among the reviewers' own rival predictions, and a decomposition that needs the authors' data. Four are **idiosyncratic**, such as how a contribution was cut. Six of the ten fault lines run through material inferences from the catalogue (Section 1.3): MI3 (imitation of legitimate referents) on how grave the unentitled "rule out" is; MI6 (fixed effects identify a causal effect) on how grave the causal reading is, and on the event study; MI9 with MI2 (equilibrium fit implies efficiency) on "economizing"; MI10 (legitimacy as a resource) on the legitimacy account; MI8 (standards reduce specificity) on whether standards are a technology or an institution. Most fault lines concern gravity, not existence: in six of them every side accepts that the defect is there, and they differ on whether it is fatal, damaging or fixable.

**Disagreement did not track perspective distance.** Across the eight contributions, verdict divergence did not rise with the overall distance between the two reviewers (Pearson r = −0.42, p = 0.40; Spearman ρ = −0.65, p = 0.16; n = 6 pairs, which supports no inference either way). The sharpest split on a shared finding, fatal against damaging on identification, fell between the *closest* pair (R-TCE and R-DID, 0.36 apart), and it turns on MI6 alone. The synthesizer inferred that the distance tool must weight the material inferences lightly. It is right. In `tools/perspective_distance.py` the ten inferences together are one of six compared INF parameters, so reversing R-DID's stance on MI6 from rejected to endorsed moves the INF distance between the two from 0.114 to 0.097 and the overall distance from 0.365 to 0.361. A distance that averages over all the parameters washes out the one commitment that does the work. Section 4.12 records the consequence for the design.

**Recommendation spread.** All four simulated reviewers, and the draft, recommend major revision. The synthesizer reports no consensus (as the instruction set requires) and shows what the common label hides: R-INST and R-BEH would accept narrowed wording and further tests, R-DID wants an identification strategy and sits "at the boundary with reject", and R-TCE sets neither condition. Every fatal rating in the panel is scoped to a headline claim ("Not Mimicry", the causal "Modularity"), none to the H1 association or the corrected model, which is why the labels converge despite four fatal ratings. Twelve minority findings are preserved regardless of the majority, among them the behavioral lens's point that year fixed effects absorb the field-level diffusion the paper sets out to explain.

**What the focal reviewer faces.** Section 6 of the synthesis is addressed to the reviewer:
- The draft already has 16 of the 27 agreed findings and five of the six agreed strengths, repairs and probes; the draft's "test whose result I can't predict" is the function-level test every lens proposes.
- Three findings raised by three or four lenses are missing from the draft: "strongly predicts" for an effect of about 0.16 SD per SD, the practice implication, and whether admissions volatility is the model's uncertainty (which bears on the draft's own "cleaner check"). Six more agreed findings, and the robust contribution on specificity, are in the draft only in part.
- Six findings are the draft's alone, including that the abstract and conclusion leave out the failed H2 and that efficiency needs a selection argument, which reaches the panel's conclusion on "economizing" without MI9.
- For eleven points of perspectival difference (nine of the mapped fault lines, plus MI4 and INF.6), the synthesis states where the draft stands, the focal perspective's own setting, and the objection the draft will meet from the other side. One example: on whether standards are an institution, the draft takes no position, although the reviewer's own ONT.1 admits fields and legitimacy; the institutional objection is "If certification was mandated, in what sense is the explanation 'not institutional'?"
- Two resolvable points correct the draft. The draft's conditional "If the stars are right, the corrected model fails this check" has a false antecedent, since every star check in the panel finds Model 3's three stars inconsistent with t ≈ 1.65. And the draft's smallest peer effect of interest (0.07) is the most lenient in the panel, although the estimate fails equivalence under all of them.

**What the synthesizer caught that the orchestrator had missed.** It found that one harness output file was mislabeled: `r-tce_chk_1_b2.out.txt` carries the id `r-tce:chk:1` but is the output of `r-tce:chk:2`. The cause is in the harness, which prefers an id found in the first lines of a code block, and the code of `r-tce:chk:2` begins with a comment naming `r-tce:chk:1`, whose closed form it reuses. It also found that two of the behavioral lens's checks (`r-beh:chk:3`, `r-beh:chk:4`) only define functions that need the authors' data, so they tested nothing. And it warned that the four simulated reviewers were "probably produced by the same model family", so their agreement on recalled literature is "not four independent recalls".

**What it did not notice.** It records that all four lenses reject MI7, but not that this leaves the panel without anyone who reads the manuscript's central inference as its authors do (Section 4.12, item 4). Nor did it notice that the institutional lens re-derived the model despite being configured to spot-check (item 3). Both are facts about the panel's configuration, which the synthesizer was given only as data.

**The proposal's claim.** The proposal says that prior work produced "simulated reviews whose disagreements track real theoretical fault lines". This run supports that claim in a specific form. Ten of the 18 disagreements were classified as fault lines, each traced to named parameters, and six of them to material inferences that divide real traditions (MI6 divides design-based from model-based identification; MI9 divides organizational economics from its critics). Two qualifications apply. The disagreements track individual commitments, not overall perspective distance. And the classification is the synthesizer's own, not yet checked against human coders blind to the perspectives, which the evaluation in Sections 2.2 and 2.3 provides for (the fault-line share).


### 4.6 Runs 08–10: adversarial probes and the check harness

Three probes interrogated the manuscript: P-DER on the formal model (Run 08); P-ID and P-NUM on the estimation, Table 2 and every reported statistic (Run 09); and P-INF, P-MEAS and P-LIT on the whole argument (Run 10). Each wrote Part 1 (scoreboard, findings, checks), the harness ran the checks, and each wrote Part 2 (dispositions).

| | Run 08 (P-DER) | Run 09 (P-ID, P-NUM) | Run 10 (P-INF, P-MEAS, P-LIT) |
|---|---|---|---|
| Findings | 8 | 11, plus one new finding from the harness output | 21 |
| Checks written and run | 5 | 9 | 4 (for findings of other types, cross-referred) |
| After the harness | 8 demonstrated (one only in part) | 8 demonstrated; 1 refuted-by-check; 2 inconclusive; the new finding asserted | 7 demonstrated; 1 inconclusive; 13 asserted (argued or literature) |
| Severity changes | 1 lowered | 2 lowered (one from fatal); 1 repair withdrawn | 1 raised |
| Most severe after the harness | Prop. 2 false under A3 (damaging) | Peer null not evidence of absence; peer coefficient does not identify imitation (damaging) | The discriminating prediction does not discriminate (fatal to the adjudication claim, conditional on accepting the check's premise) |

**A derivation failure demonstrated.** `p08:chk:2` re-derives Proposition 2 symbolically from the manuscript's own §2.2 and compares it with the Appendix expression. The harness output: "Appendix expression matches full cross-partial: False"; the omitted term is "-h1\*(g0 + g1\*u + s)/((h0 + h1\*u)\*\*2\*(m - 1)\*\*2)"; "A3 <=> Delta < 0: True"; "draws with A3: 74343, of which cross-partial > 0: 0". The probe disposed of the finding as **demonstrated** and added that "Prop. 2 holds exactly when A3 fails", and that the negative interaction in Table 2 is what the correctly derived model predicts, which makes the legitimacy explanation idle but also turns the sign into accommodation, since it was derived after Table 2 was seen.

**An identification failure demonstrated.** `p09:chk:5` builds a data-generating process from the manuscript's own statement that outsourcing "transfers or eliminates" in-house IT positions (§3.2) and asks whether surviving the staffing control (Model 4) excludes capability confounding. Output: with a true modularity effect of zero, Model 4 gives a coefficient of 0.146, "positive, p<.05 in 100% of replications"; with a true effect of 0.11 and no confounding, the control biases it by −18%. **Demonstrated**: Model 4 is uninformative in either direction. `p10:chk:3` reached the same verdict independently. `p09:chk:7` showed that same-year feedback from outsourcing to reported modularity, with no causal effect at all, reproduces Table 2's modularity estimate (0.107 against 0.112), significant in every replication; it also showed that lagging modularity, a repair the probe had itself proposed in Part 1, does not fix this, and the probe withdrew it.

**The harness corrects the probe as well as the paper.** Three things happened that an unbound probe could not have done:
- `p09:chk:4` **refuted** the probe's own suspicion that the paper's effect-size arithmetic was wrong ("2.69 pp; 0.158 against one-sixth; fall 0.693 > 0.667"), and the probe recorded the arithmetic as a strength.
- `p09:chk:6` was **too weak to decide** its question: the economizing-only benchmark reproduced the Table 2 pattern in only 28% of replications, so the probe downgraded its only fatal finding to "damaging (provisional)" and said plainly that the fault was its own calibration. Run 10's `p10:chk:4` tested a closely related claim with a different calibration and found it demonstrated, conditional on the reviewer accepting its data-generating process as a fair statement of the rival. Two checks of nearly the same claim reached different statuses, which is why the instruction set makes the premise of every simulation a decision for the reviewer.
- `p09:chk:9` turned up a result nobody had anticipated, a downward bias of −0.063 in the peer coefficient under a true null with serially independent state shocks. The probe recorded it as a new **asserted** finding (`p09:fnd:12`) rather than a demonstrated one, because no check had been designed to test it.

**Numerical consistency.** `p08:chk:4` and `p09:chk:1–2` recompute every t-ratio, star and sample size in Table 2 and the text: 15 of 16 cells consistent; Model 3's uncertainty coefficient starred \*\*\* at p = 0.1003; N = 4,712 not 412 × 11 = 4,532 (nor 4,120 with the lagged peer measure). P-DER also found a weakness that is not in the key: with uncertainty measured as a z-score, $H(u) \le 0$ is possible, which reverses the buy rule (`p08:fnd:8`).

**What the probes did not do.** Measurement, inference and literature findings cannot be bound to code (P-MEAS, P-INF, P-LIT); 13 of Run 10's 21 findings stay asserted, and the literature findings are marked "(to verify)" because no search tool was available (Section 4.11).

### 4.7 Run 11: the consistency check on the reviewer's draft (Mode C)

The elicitor, still without the manuscript, compared the reviewer's draft with the reviewer's own specification (`runs/11_consistency_check.md`, 35,792 bytes). It is labeled a report, not a review (`isReview: false`), and wherever a judgment would need the manuscript it says so (`needs_manuscript: true`). It cites the draft by line (`dr:L60`) and keeps its quotations under 25 words.

| What Mode C checks | Result |
|---|---|
| Standards applied | 12 of 16 applied; 4 partial (`std:1`, `std:7`, `std:9`, `std:10`); none unapplied |
| Silent skips of must conditions | 7 (`bs:CS1`–`bs:CS7`), each with what applying it would involve, none applied by the report |
| Undeclared standards | 4 criteria the draft uses but the specification lacks (`bs:CU1`–`bs:CU4`), each with the question whether to add it |
| Internal consistency | 6 items (`bs:CI1`–`bs:CI6`): one material inconsistency, two on severity labels, one on wording, and two confirmations |
| The editor's brief | Every need and concern answered; one need (fairness to sociologists) only in part and only among the minor concerns |
| The tension left open at specification (`bs:T7`) | Settled in the draft's first line, "must means must"; no shedding declared, none found |
| Formal and numerical findings | 7 hand computations listed for the harness, with the inputs each needs and which the draft supplies |

**The material inconsistency.** The draft says, as a threat to identification, "State requirements could raise outsourcing directly, not only through modularity" (`dr:L60`), and twenty lines later recommends the same requirements as an instrument for modularity, "the paper's best route to identification" (`dr:L80`), and makes that route a condition of its recommendation (`dr:L113`). An instrument must affect the outcome only through the instrumented variable; the draft's own sentence gives the reason to doubt it. Mode C did not judge whether the instrument is valid ("That needs the manuscript, and it is the reviewer's call"); it put the two passages side by side (`bs:CI1`). Probe P-ID had raised the same threat to the instrument from the manuscript side (`p09:ref:3`) without knowing the draft relied on it.

**Standards the reviewer uses but never stated.** The draft's most consequential criterion has no standard behind it: bad controls, a control that is partly an outcome of the treatment or lies on the theory's own causal channel (`bs:CU1`). The draft applies it to two controls (`dr:L74–75`) and makes it one of the four conditions on which the recommendation turns (`dr:L114`), yet the specification records it only as a setting (TEC.3). The draft also uses, without a standard, what an instrument must satisfy (`bs:CU2`), a direct cost-evidence route for efficiency claims (`bs:CU3`), and the requirement that a paper's explanation be compatible with its own conclusions (`bs:CU4`). Each is put to the reviewer as a question: add it, merge it, or leave it.

**Where the reviewer applied less than the reviewer asked for.** The seven silent skips are conditions the reviewer made must standards in Run 01 and then did not apply: whether the assumption that signs the corrected model is defended (`bs:CS1`); whether H1's sign survives aggregation (`bs:CS2`); which controls carry identifying weight (`bs:CS3`, which the reviewer's own `bs:T7` settlement says cannot be shed); construct definition for the main regressor and the outcome (`bs:CS4`); the level at which uncertainty varies, against the clustering (`bs:CS5`); the comparison implicit in the within-hospital design (`bs:CS6`); and what the failed H2 implies for the theory (`bs:CS7`). These are exactly what time pressure removes from a review, and they are what the reviewer said, in Round 1, that time pressure removes ("The checks I skip are the ones that catch an internally inconsistent paper").

**Smaller points, which a reviewer can settle in a minute each.** The draft gives Majors 1–3 the label "(damaging, fixable)", which the workbench's severity scale treats as exclusive (`bs:CI3`); one sentence of the draft exempts the model's assumptions from a failed prediction although the reviewer's own resolution of `bs:T1` says the assumptions are included (`bs:CI2`, which Mode C notes may be a case `bs:T1` did not anticipate, since here the failure came from a derivation error); the draft calls the association "robust" while asking for results without two controls it calls bad (`bs:CI6`); and the body runs to about 1,475 words against the reviewer's rule of about 1,000.

**What this run shows about the capability.** Mode C found what no other role could have found, because it is about the review, not the paper. None of its findings needed the manuscript to state, and none of them is a finding about the manuscript: each is a relation between two of the reviewer's own commitments, or between a commitment and its application. That is the Best-Self capability as the proposal describes it: "a specification of the reviewer's own reviewing self, against which their eventual review can be checked". It is also a check on the elicitation itself: four undeclared standards against a sixteen-standard specification measure how much of the reviewer's practice the elicitation missed, which is why the standards-coverage measure counts undeclared standards separately (Section 5.3).

### 4.8 Run 12: the reviewer's dispositions and the signed review

The reviewer stand-in, still in persona, read the consistency check on its draft, the panel synthesis, the three probes, the simulated reviews as needed and the harness outputs. It wrote no code. It was required to decide on every finding rated fatal or damaging, every probe finding that the harness had demonstrated, refuted or left inconclusive, every item in the panel's "What the focal reviewer faces", every question Mode C put to it, and every probe's decisions for the reviewer; other findings it could decide in groups. Each decision is accept, reject or modify, with a one-line reason and the place in the signed review where it lands. A rejected finding lands nowhere. The output is one file: a machine-readable `Dispositions` block, the signed review between fixed markers, and an attestation (`runs/12_reviewer_dispositions_final_review.md`). The stand-in's out-of-role note is beside it (`runs/12_reviewer_standin_note.md`).

**117 decisions: 74 accept, 35 modify, 8 reject.** Many entries cover a finding raised by several roles, so the entries carry several hundred role-level ids between them.

| Source of the item | Decisions | Of which modified | Of which rejected |
|---|---|---|---|
| Consistency check on the draft (Run 11) | 24 | 3 | 1 |
| Panel synthesis (Run 07), its own items | 22 | 6 | 1 |
| Findings raised by several roles, decided together | 28 | 12 | 0 |
| Probes (Runs 08–10), single-role items and decisions | 38 | 13 | 3 |
| Simulated reviewers, single-role items | 5 | 1 | 3 |

*Counts by the `source` field of each entry; the five rows sum to 117.*

**What the reviewer changed, and why.**
- **The instrument.** The draft recommended the state requirements as an instrument while saying they may raise outsourcing directly (Section 4.7). The signed review keeps the requirements as "the paper's best route to identification, but only if two conditions hold", states relevance and exclusion, and names three threats to exclusion, including the one the draft itself had raised (`bs:CI1`, accepted). The reviewer also added relevance and exclusion to its own specification (`bs:CU2`).
- **The silent skips.** All seven must conditions the draft had skipped are applied in the signed review; none was declined. Bad controls, the most consequential undeclared standard, became a must condition of the reviewer's identification standard rather than a new standard (`bs:CU1`, modified).
- **Severity.** The draft labeled three concerns "(damaging, fixable)". The signed review gives one label each. The test of the rival is now "fatal to 'Not Mimicry' and 'rule out' as worded", scoped to the headline claim and closed by narrowing it; the reviewer made this call explicit, as Mode C suggested, and took the scoped form from the probes and the panel (`pnl:dis:1`, modified). The causal reading stays damaging under the reviewer's conditional endorsement of MI6, and the design-based objection that would make it fatal is answered in the review and in the note to the editor (`pnl:dis:2`, modified). The recommendation is still major revision, now with a stated condition: "If the title claim is kept without a discriminating test, I would recommend rejection."
- **A corrected premise.** The draft's "If the stars are right, the corrected model fails this check" rested on a star the harness had shown to be wrong. The signed review restates the point as a wrong-signed, imprecise estimate and asks for the covariance needed to settle it (`pnl:dis:4`, modified).
- **New content.** The panel's three robust findings the draft lacked are all accepted (the overstated "strongly", the practice implication, the uncertainty construct), as is the consequence of the mechanism test the draft had only half drawn: Major 4 is rewritten from an efficiency concern into "The mechanism and the efficiency conclusion are not shown", with the omitted-variable reasoning on the specificity rating and the production-cost channel that the panel preserved as a minority finding.
- **What the reviewer held to.** The reviewer did not credit the corrected interaction as corroboration, because a sign repaired after the result is a rescue under its own standard (`r-beh:fnd:8`, rejected; `pnl:dis:3`, modified). It declined to raise the share-scale reversal to damaging after reading the check script and seeing that the probe's grid kept the threshold high (`p10:fnd:10`, modified). It rejected the behavioral rival as outside the paper's own contest (`r-beh:fnd:12`), an asserted finding no check had tested (`p09:fnd:12`), and the panel's distance check as something it did not rely on.

**The signed review.** 3,758 words by the measure used for the draft in Section 4.3 (the draft: 1,567), of which 3,334 are the body, with a checks list and a confidential note to the editor. Its style barely moved: Flesch reading ease 48.6 against the draft's 47.1, hedges 7.2 per 1,000 words against 6.4. The note to the editor explains the growth (points missed that bear on the main claims, standards the draft had not applied, and one inconsistency that "needed an argument rather than a sentence"), reports that "the formal and numerical points were checked by machine as well as by hand", and says that no simulated magnitude is cited to the authors. The citations that the reviewer could not check stay "to verify", and the editor is asked to verify or strike them.

**The stand-in's own account.** The note says where a human would probably have decided differently: a human anchored on the draft, or close to the resembling lens, "might well have kept 'damaging'" for the rival test, and the move to fatal "also tracks three simulated lenses and two probes that point the same way", although the panel itself warned that its simulators are correlated. It says that reading the workbench's outputs and writing 117 dispositions "is several hours of reading for a human", and it lists the accepted findings it could not have assessed without the harness (for example, that the staffing control can bias the coefficient in either direction under the manuscript's own relations). Its list of what made deciding harder than it needed to be (no cross-walk of ids across roles, overlapping decision lists, severity conventions that differ between roles, and a disposition vocabulary that fits findings but not choices between options) is the most useful design feedback the runs produced, and Section 4.12 takes it up.

### 4.9 Run 14: the provenance trace and the editor view

Every step of Runs 01 to 14 is an event in `runs/provenance_events.json`: 42 events, each hash-linked to its predecessor, each validating against `ProvenanceEvent` in the schema, 21 with actual times and 21 reconstructed from file save times and marked so (Section 4.0, item 7). One event records a correction before publication: a stand-in event had been logged with an actor kind the schema does not allow, and the orchestrator corrected it and recomputed the chain from that event onward (`ev:35`). Two tools turn the trace into what an editor sees.

**Machine-origin share** (`tools/machine_origin.py`; definition in Section 5.3). A sentence of the signed review counts as of machine origin when at least 60% of its word 5-grams occur in some agent output of the session, after removing 5-grams that occur in the manuscript or in the reviewer's own unassisted draft.

| Threshold | Machine origin | Mixed | Carried from the draft | New |
|---|---|---|---|---|
| 0.6 (the definition) | **1.9%** | 0.0% | 14.2% | 83.9% |
| 0.4 | 6.0% | 0.4% | 17.2% | 76.4% |
| 0.3 | 9.4% | 1.1% | 22.1% | 67.4% |
| 0.2 | 15.7% | 1.1% | 26.6% | 56.6% |

*267 sentences scored. At the defined threshold, five sentences are of machine origin; the longest is "The rating's coefficient barely moves when m enters (−0.094 to −0.091)."*

**The measure and the record disagree, and the record is right.** The reviewer made 109 accept or modify decisions on workbench findings, and the review more than doubled in length, yet under 2% of its sentences are of machine origin by wording. The reviewer rewrote what it accepted. That is what the protocol asks of a reviewer, but it is also what a reviewer who wanted to hide reliance on the workbench would do, so text overlap cannot be the measure of what the workbench contributed. The dispositions are: they say, finding by finding, what entered the review and where. The editor view therefore leads with the dispositions and reports the text measure second, with a warning that it compares wording, not content. Section 4.12 records the consequence for the measure.

**The editor view** (`tools/editor_view.py`; `runs/14_editor_view.md`), generated from the trace as it stood when the review was signed (39 events), the dispositions and the machine-origin analysis, reports:
- record integrity (the hash chain verified; the pilot and scoring events, which belong to the research record rather than to this review, listed and excluded);
- the capabilities used, each with its events, and the models and instruction-set version;
- the participants, here named as Claude stand-ins;
- every disposition in a table (finding, source, decision, reason, where it lands);
- where the accepted and modified findings land (Major 2 and the minor concerns most, 26 each; seven decisions concern process only and land in no text);
- the composition table above, with the passages of machine origin and the agent output each most overlaps;
- the author view: a paragraph for the decision letter naming the capabilities used and restating the reviewer's attestation.

What the editor view cannot show is whether the reviewer's decisions were good ones. It shows that every finding that entered the review passed a recorded human decision, and which ones did. That is the proposal's claim for the provenance layer, that it makes "any assisted review's composition inspectable by editors", and in this run it holds, with the qualification that the composition it makes inspectable is the composition of decisions, not of sentences.

### 4.10 Seeded-defect recovery across the runs

A separate Claude instance scored every output that makes findings against the sealed key, with the same rules as the pilot's blind scorer (`runs/13_pilot/scoring.md`), and counted the other substantive findings by category (`runs/recovery_scoring.md`). Unlike the pilot, this scoring knew which run each output came from. The authors spot-checked the scoring against the outputs and the sealed key before submission. Because one model family wrote the test manuscript and its key, played every role and scored the outputs, that spot-check is the only check on the scoring made outside that family. L = located (right locus and reason), T = touched, M = missed; † = only in a passage the probe marks as a referral to another probe type.

| Output | SD1 | SD2 | SD3 | SD4 | SD5 | SD6 | SD7 | SD8 | SD9 | Located | Known-unseeded (of 5) | New-substantive categories | Mistaken |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 02 Reviewer's draft (no workbench) | L | L | L | L | L | L | L | L | L | 9 | 4 | 13 | 0 |
| 03 Simulated, transaction-cost | L | L | L | L | L | L | L | L | L | 9 | 5 | 16 | 0 |
| 04 Simulated, institutional | L | L | L | L | L | L | L | L | L | 9 | 5 | 13 | 0 |
| 05 Simulated, behavioral | L | L | L | L | L | L | L | L | L | 9 | 5 | 19 | 0 |
| 06 Simulated, design-based | L | L | L | L | L | L | L | L | L | 9 | 5 | 13 | 0 |
| 08 Probe, P-DER (P-NUM) | L | L† | T† | M | T | L | T† | L | L† | 5 (3 without referrals) | 2 | 5 | 0 |
| 09 Probe, P-ID and P-NUM | L† | L | L | L† | T† | L | T† | L† | M | 6 (3 without referrals) | 3 | 11 | 0 |
| 10 Probe, P-INF, P-MEAS, P-LIT | L | L | L | L | L | L | L | L | L | 9 | 4 | 16 | 0 |
| **12 Reviewer's final review (after the workbench)** | L | L | L | L | L | L | L | L | L | 9 | 4 | 24 | 0 |

**The headline is a ceiling.** The reviewer stand-in's unassisted draft located all nine seeded defects, and so did each simulated reviewer and the inferential audit. On this manuscript, with this stand-in, the workbench added **no seeded-defect recovery** over the reviewer's own draft. This is the clearest consequence of the two limits in Section 4.0: the manuscript is too easy for the model family, and the stand-in is not a one-hour human reviewer. It is reported as it fell.

**What the workbench did add.**
- **Demonstration.** Four seeded defects are demonstrable by a check (SD1, SD2, SD3, SD6) and one partly (SD8). Each was demonstrated by the harness in at least one probe: SD1 by `p08:chk:2` and `p10:chk:1`; SD2 by `p09:chk:5` and `p10:chk:3`; SD3 by `p09:chk:3` and `p10:chk:2`; SD6 by `p08:chk:4`, `p09:chk:1–2` and `p10:chk:2`; SD8 by `p08:chk:3` and `p10:chk:1`. The demonstration rate is 4 of 4 (5 of 5 with SD8). The draft's findings on the same defects rest on the reviewer's hand derivations and mental arithmetic, which its own "Checks run" list asks the harness to confirm.
- **Unseeded findings.** Across the 32 categories of substantive weakness the scorers identified, the draft raised 17. The workbench roles together raised 31, including 15 the draft did not: the corner solution (KU5); year effects absorbing the diffusion the paper sets out to explain; coercive isomorphism; the uncertainty proxy; the scope of the modularity measure; rival economizing channels; other post-outcome controls; classification drift in the outcome; "strongly" overstating a modest association; the model's domain against its measures; the practice implication; the novelty of the transaction-cost contribution; a behavioral rival; H3 as stated against H3 as tested; and the downward bias in the peer coefficient. One category, the abstract's silence about the contrary H2 result, was raised by the draft and by no role.
- **Incremental recall.** On seeded defects, 0 of 9 (the draft found all nine). On unseeded categories, 15 of the 31 the workbench raised (48%), with no finding judged mistaken in any output.
- **A check on the reviewer.** The consistency check found an inconsistency in the draft itself (Section 4.7), which no seeded defect or simulated reviewer could have found, because it is about the review, not the paper.

**The reviewer's final review.** Scored by the same rules (`runs/recovery_scoring_R12.md`; only the signed text counts, not the dispositions), the signed review locates all nine seeded defects, as the draft did, and raises 28 categories of unseeded weakness against the draft's 17: all 17 of the draft's, 10 of the 15 that only the workbench roles had raised, and one the scorer had not defined before, that assumption A3 is never defended for the setting although every corrected sign depends on it. That one came from the consistency check (`bs:CS1`, a must condition the draft had skipped), which the recovery scoring of the roles could not credit because Mode C makes no findings about the manuscript. Of the five workbench-only categories the review does not raise, it rejected two explicitly (the behavioral rival, and the downward bias in the peer coefficient, which was asserted and never checked) and did not take up three (the corner solution, other post-outcome controls, and classification drift in the outcome). No finding in it was judged mistaken; the scorer noted one imprecise phrase in the readability point. Within the located defects, the final review is firmer than the draft on five (the equivalence test on the peer coefficient, the rival's construct, the legitimacy account, the priority claim and the share-scale algebra).

So, on this manuscript, the assisted review improves on the same reviewer's unassisted draft by 0 of 9 seeded defects and **11 categories** of unseeded weakness (17 to 28), with no mistaken finding in either. This is a within-reviewer analogue of incremental validity. Section 5.3 defines the review-level quantity against a conventional review of the same manuscript by another reviewer, which the demonstration does not have; the critical test measures it at scale (H2, H3), with human reviewers on both tracks.

**Probes are scoped.** The two technical probes miss what lies outside their types (P-DER does not hunt for the misrepresented rival, SD4; P-ID does not hunt for the incompatible commitments, SD9) and pass some of it on as referrals; the inferential audit covers the rest. Recovery is therefore reported per probe, and the union is what a reviewer receives.

**The scorer's doubts** are listed in `runs/recovery_scoring.md` §3 and `runs/recovery_scoring_R12.md` §5. The one it was least sure of for the roles (whether Run 08's referral on SD3 counts as touched or located) changes nothing above. For the final review, two calls could each lower a count by one: the new A3 category could be read as part of SD1 (24 new-substantive categories would become 23), and a request for a heterogeneity-robust estimator could be read as not raising the staggered-adoption weakness (4 known-unseeded would become 3). Together they would reduce the gain over the draft from 11 categories to 9.


### 4.11 Verification of the citations flagged in the runs

No agent in the runs had a search tool. Each was told to mark any work it could not vouch for from memory as "(to verify)", and the transcripts are left as written. The table below checks every flagged work against the published record (journal, volume, issue, pages) and against the use the run makes of it. The checks were made by Claude: for the six items marked †, against an online record of the article (the publisher's page or an indexing service); for the rest, from its knowledge of the published record. The authors spot-checked these verdicts against the original publications before submission. Runs: 01 dialogue (turn numbers), 02 reviewer's unassisted draft, 03 R-TCE, 04 R-INST, 05 R-BEH, 06 R-DID, 08 P-DER, 09 P-ID/P-NUM, 07 panel synthesis, 10 P-INF/P-MEAS/P-LIT, 11 consistency check (which only repeats the draft's flag), 13 pilot reports A to F.

| Work as verified | Flagged in | Use in the run | Verdict |
|---|---|---|---|
| Angrist, J. D., & Pischke, J.-S. (2009). *Mostly Harmless Econometrics*. Princeton University Press | 10 | Bad controls | Supported |
| Ang, S., & Cummings, L. L. (1997). Strategic response to institutional influences on information systems outsourcing. *Organization Science*, 8(3), 235–256 † | 02, 03, 04, 05, 06, 07, 10, 11; B, C, E, F | Prior work weighing institutional against economic drivers of IS outsourcing; contradicts the priority claim | Supported (sealed key, SD7) |
| Ang, S., & Straub, D. W. (1998). Production and transaction economies and IS outsourcing: A study of the U.S. banking industry. *MIS Quarterly*, 22(4), 535–552 | 04, 10; A, C | A close neighbor that tests economic accounts of IS outsourcing | **Partly.** It weighs production against transaction economies; it does not test institutional influence, so it supports "close neighbor" but not "weighed institutional against economic drivers" (04) |
| Argyres, N. S. (1996). Evidence on the role of firm capabilities in vertical integration decisions. *Strategic Management Journal*, 17(2), 129–150 | 05 | Capabilities shape make-or-buy beyond transaction attributes | Supported |
| Argyres, N. S., & Bigelow, L. (2010). Innovation, modularity, and vertical deintegration: Evidence from the early U.S. auto industry. *Organization Science*, 21(4), 842–853 | 10 | Empirical test of modularity and disintegration | Supported |
| Baldwin, C. Y., & Clark, K. B. (2000). *Design Rules, Vol. 1: The Power of Modularity*. MIT Press | 03, 10 | Modularity cited by the manuscript | Supported |
| Bertrand, M., Duflo, E., & Mullainathan, S. (2004). How much should we trust differences-in-differences estimates? *Quarterly Journal of Economics*, 119(1), 249–275 | B | Hospital clustering understates standard errors of state-level regressors | **Partly.** The paper's subject is serial correlation in difference-in-differences; it does recommend clustering at the level of the policy variable. Moulton (1990), cited in run 09, is the canonical source for aggregate regressors |
| Bramoullé, Y., Djebbari, H., & Fortin, B. (2009). Identification of peer effects through social networks. *Journal of Econometrics*, 150(1), 41–55 | 09 | Identification from partially overlapping peer groups | Supported |
| Brusoni, S., Prencipe, A., & Pavitt, K. (2001). Knowledge specialization, organizational coupling, and the boundaries of the firm: Why do firms know more than they make? *Administrative Science Quarterly*, 46(4), 597–621 | 10 | Work challenging the step from modular products to modular organizations | Supported |
| Callaway, B., & Sant'Anna, P. H. C. (2021). Difference-in-differences with multiple time periods. *Journal of Econometrics*, 225(2), 200–230 | 01 (turns 7–9), 02, 03, 04, 05, 06, 09, 10; B, D, E, F | Staggered adoption with heterogeneous effects | Supported |
| Cameron, A. C., & Miller, D. L. (2015). A practitioner's guide to cluster-robust inference. *Journal of Human Resources*, 50(2), 317–372 | 09 | Clustering for state-level regressors | Supported |
| Cameron, A. C., Gelbach, J. B., & Miller, D. L. (2008). Bootstrap-based improvements for inference with clustered errors. *Review of Economics and Statistics*, 90(3), 414–427 | 09 (as "wild-bootstrap") | Small-cluster correction | Supported (the run names the method, not the paper) |
| Cinelli, C., Forney, A., & Pearl, J. (2024). A crash course in good and bad controls. *Sociological Methods & Research*, 53(3), 1071–1104 | 06 | Conditioning on a mediator removes the peer coefficient | Supported |
| Cinelli, C., & Hazlett, C. (2020). Making sense of sensitivity: Extending omitted variable bias. *Journal of the Royal Statistical Society: Series B*, 82(1), 39–67 | 06, 09 | Sensitivity analysis for unobserved confounding | Supported |
| Cyert, R. M., & March, J. G. (1963). *A Behavioral Theory of the Firm*. Prentice-Hall | 05 | The CIO as a coalition member | Supported |
| David, R. J., & Han, S.-K. (2004). A systematic assessment of the empirical support for transaction cost economics. *Strategic Management Journal*, 25(1), 39–58 | 10 | Mixed support for transaction-cost predictions, notably on uncertainty | Supported |
| Davis, M. S. (1971). That's interesting! Towards a phenomenology of sociology and a sociology of phenomenology. *Philosophy of the Social Sciences*, 1(4), 309–344 | 01 (turns 5–9) | A contribution is "interesting" when it denies what the audience took for granted | Supported |
| de Chaisemartin, C., & D'Haultfœuille, X. (2020). Two-way fixed effects estimators with heterogeneous treatment effects. *American Economic Review*, 110(9), 2964–2996 | 03, 06, 09, 10 | Two-way fixed effects under heterogeneous effects | Supported |
| Dibbern, J., Goles, T., Hirschheim, R., & Jayatilaka, B. (2004). Information systems outsourcing: A survey and analysis of the literature. *ACM SIGMIS Database*, 35(4), 6–102 | D | The IS outsourcing literature the priority claim ignores | Supported |
| DiMaggio, P. J., & Powell, W. W. (1983). The iron cage revisited. *American Sociological Review*, 48(2), 147–160 | 10 | Mimetic isomorphism under uncertainty; imitation of perceived successful or legitimate peers | Supported |
| Fligstein, N. (1985). The spread of the multidivisional form among large firms, 1919–1979. *American Sociological Review*, 50(3), 377–391 | 04 | Weighs efficiency against institutional explanations of diffusion | Supported |
| Gelman, A., & Stern, H. (2006). The difference between "significant" and "not significant" is not itself statistically significant. *The American Statistician*, 60(4), 328–331 | E | The fall from Model 1 to Model 2 is not itself tested | Supported |
| Giesselmann, M., & Schmidt-Catran, A. W. (2022). Interactions in fixed effects regression models. *Sociological Methods & Research*, 51(3), 1100–1127 † | 09 | An interaction under fixed effects can carry between-unit variation | Supported |
| Goodman-Bacon, A. (2021). Difference-in-differences with variation in treatment timing. *Journal of Econometrics*, 225(2), 254–277 | 03, 04, 05, 06, 09, 10; B, D, E, F | Staggered adoption | Supported |
| Greve, H. R. (2003). *Organizational Learning from Performance Feedback*. Cambridge University Press | 05 | Aspiration as a weighted combination of historical and social reference points | Supported |
| Haveman, H. A. (1993). Follow the leader: Mimetic isomorphism and entry into new markets. *Administrative Science Quarterly*, 38(4), 593–627 | 10; F | Imitation targets large and successful referents | Supported |
| Hoetker, G. (2006). Do modular products lead to modular organizations? *Strategic Management Journal*, 27(6), 501–518 † | 03, 10; C | A test of the step from modularity to disintegration (03); work challenging that step (10) | **Supported, with a nuance the runs leave out.** Hoetker finds that product modularity increases organizational reconfigurability more than it moves activities out of the firm, which is itself evidence relevant to the manuscript's H1 |
| Jacobides, M. G., & Winter, S. G. (2005). The co-evolution of capabilities and transaction costs. *Strategic Management Journal*, 26(5), 395–413 | A | Modularity and boundary literature | Supported |
| Kennedy, M. T., & Fiss, P. C. (2009). Institutionalization, framing, and diffusion: The logic of TQM adoption and implementation decisions among U.S. hospitals. *Academy of Management Journal*, 52(5), 897–918 † | 10 | Early and late adopters both pursue economic gains and legitimacy, under different framings | Supported |
| Klein, B., Crawford, R. G., & Alchian, A. A. (1978). Vertical integration, appropriable rents, and the competitive contracting process. *Journal of Law and Economics*, 21(2), 297–326 | 03 | Appropriable quasi-rents | Supported |
| Lakens, D. (2017). Equivalence tests: A practical primer for t tests, correlations, and meta-analyses. *Social Psychological and Personality Science*, 8(4), 355–362 | 10 | Equivalence testing for null claims | Supported |
| Langlois, R. N. (2002). Modularity in technology and organization. *Journal of Economic Behavior & Organization*, 49(1), 19–37 | 03, 10; A | Modularity cited by the manuscript | Supported |
| Langlois, R. N., & Robertson, P. L. (1992). Networks and innovation in a modular system. *Research Policy*, 21(4), 297–313 | A | Modularity and boundary literature | Supported |
| Lee, D. S. (2009). Training, wages, and sample selection: Estimating sharp bounds on treatment effects. *Review of Economic Studies*, 76(3), 1071–1102 | 06 (as "Lee bounds") | Bounds under selective attrition | Supported (the run names the method, not the paper) |
| Lieberman, M. B., & Asaba, S. (2006). Why do firms imitate each other? *Academy of Management Review*, 31(2), 366–385 | 10 | Imitation can be information-based | Supported |
| Loh, L., & Venkatraman, N. (1992). Diffusion of information technology outsourcing: Influence sources and the Kodak effect. *Information Systems Research*, 3(4), 334–358 † | 03, 04, 05, 06, 07, 10; A, B, C, E, F | Prior study of imitative diffusion of IT outsourcing; contradicts the priority claim | Supported (sealed key, SD7) |
| Manski, C. F. (1993). Identification of endogenous social effects: The reflection problem. *Review of Economic Studies*, 60(3), 531–542 | 01 (turns 5–9), 03, 05, 06, 07, 09, 10; F | The reflection problem for same-group peer means | Supported |
| Moulton, B. R. (1990). An illustration of a pitfall in estimating the effects of aggregate variables on micro units. *Review of Economics and Statistics*, 72(2), 334–338 | 09 | Standard errors for aggregate regressors | Supported |
| Nickell, S. (1981). Biases in dynamic models with fixed effects. *Econometrica*, 49(6), 1417–1426 | 09 (new finding `p09:fnd:12`) | Within-transformation bias of a lagged state-mean regressor | **Partly.** Nickell derives the bias for a lagged dependent variable; the same mechanism applies to any predetermined regressor, which the lagged peer mean is when it shares state-year shocks with the outcome. The analogy is apt; the citation alone does not establish the sign or size found in the simulation |
| Oster, E. (2019). Unobservable selection and coefficient stability: Theory and evidence. *Journal of Business & Economic Statistics*, 37(2), 187–204 | 09; F | Sensitivity to omitted confounding | Supported |
| Palmer, D. A., Jennings, P. D., & Zhou, X. (1993). Late adoption of the multidivisional form by large U.S. corporations: Institutional, political, and economic accounts. *Administrative Science Quarterly*, 38(1), 100–131 | 04 | Weighs efficiency against institutional explanations of diffusion | Supported |
| Papke, L. E., & Wooldridge, J. M. (1996). Econometric methods for fractional response variables with an application to 401(k) plan participation rates. *Journal of Applied Econometrics*, 11(6), 619–632 | A | Fractional-response robustness for a share outcome | Supported |
| Pearl, J. (2009). *Causality* (2nd ed.). Cambridge University Press | 09 | Causal graphs | Supported |
| Poppo, L., & Zenger, T. (1998). Testing alternative theories of the firm: Transaction cost, knowledge-based, and measurement explanations for make-or-buy decisions in information services. *Strategic Management Journal*, 19(9), 853–877 | 03, 10; B, E | Transaction-cost make-or-buy tested in information services | Supported |
| Rambachan, A., & Roth, J. (2023). A more credible approach to parallel trends. *Review of Economic Studies*, 90(5), 2555–2591 | 01 (turns 8–9), 02, 06 | Sensitivity of event-study estimates to violations of parallel trends | Supported |
| Roth, J. (2022). Pretest with caution: Event-study estimates after testing for parallel trends. *American Economic Review: Insights*, 4(3), 305–322 | 01 (turns 8–9), 09; F | Pre-trend tests have low power | Supported |
| Sanchez, R., & Mahoney, J. T. (1996). Modularity, flexibility, and knowledge management in product and organization design. *Strategic Management Journal*, 17(S2), 63–76 | 03, 10; A | Modularity cited by the manuscript | Supported |
| Schilling, M. A., & Steensma, H. K. (2001). The use of modular organizational forms: An industry-level analysis. *Academy of Management Journal*, 44(6), 1149–1168 | 10 | Empirical test of modularity and modular organizational forms | Supported |
| Strang, D., & Macy, M. W. (2001). In search of excellence: Fads, success stories, and adaptive emulation. *American Journal of Sociology*, 107(1), 147–182 | 10 | Imitation can be adaptive | Supported |
| Sun, L., & Abraham, S. (2021). Estimating dynamic treatment effects in event studies with heterogeneous treatment effects. *Journal of Econometrics*, 225(2), 175–199 | 01 (turns 7–9), 02, 03, 04, 05, 06, 09, 10; B, E, F | Event studies under heterogeneous effects | Supported |
| Tiwana, A. (2008). Does technological modularity substitute for control? A study of alliance performance in software outsourcing. *Strategic Management Journal*, 29(7), 769–780 † | 10 | Modularity in software outsourcing | **Supported, with a wrong issue number.** Run 10 gives 29(11); the paper is in 29(7) |
| Tolbert, P. S., & Zucker, L. G. (1983). Institutional sources of change in the formal structure of organizations: The diffusion of civil service reform, 1880–1935. *Administrative Science Quarterly*, 28(1), 22–39 | 10 | Two-stage diffusion, technical then legitimacy-driven | Supported |
| Westphal, J. D., Gulati, R., & Shortell, S. M. (1997). Customization or conformity? An institutional and network perspective on the content and consequences of TQM adoption. *Administrative Science Quarterly*, 42(2), 366–394 | 04, 10; F | Separates technical customization from conformity among hospitals | Supported |
| Williamson, O. E. (1985). *The Economic Institutions of Capitalism*. Free Press | 01 (turns 5–7), 03 | Technology and governance chosen together (the contracting schema) | Supported |

**Result.** 54 works (two of them named in the runs by method rather than by paper: the wild cluster bootstrap and Lee bounds). 49 are supported as used. Three are partly supported, as the table explains: Ang and Straub (1998), Bertrand, Duflo and Mullainathan (2004), and Nickell (1981). Hoetker (2006) is supported, but its finding cuts more sharply against the manuscript than the runs say. Tiwana (2008) carries a wrong issue number. None is misattributed, and none is invented. Three flags concern empirical premises, not works: that the 2009 federal incentive program required certified EHR technology, which hospitals reached at different times (06; correct: the HITECH Act's incentive programs required certified technology and were attested in stages); that federal certification or attestation records could validate the modularity measure (06, 09; the public list of certified health-IT products and the incentive programs' attestation records exist, but whether they can be linked to the manuscript's hospitals is not established); and that hospital cost reports record contracted IT spending (06; not checked, left open).

### 4.12 What the runs exposed about the suite

The runs were the first test of the instruction sets, the schema and the harness, and they exposed problems in all three. Each is listed with what it implies and the change it motivates (recorded for v0.2 in `instruction-sets/ERRATA_AND_v0.2_CHANGES.md`).

1. **The editor brief is a channel for findings.** The protocol keeps the manuscript from the elicitor so that the standards are the reviewer's own. But the editor has read the manuscript, and the editor stand-in's concerns carried six seeded defects into the brief and from there into the elicitation (Section 4.0, item 1). Real editors write such notes too, and the consent language already asks them not to (Annex E.4). The run shows that asking is not enough. *Change:* Mode E records the editor's needs and audience separately from the editor's concerns about this manuscript; only the first goes to Mode S, and the second goes to Mode C, which checks whether the draft answers it.

2. **A model stand-in is not a one-hour human reviewer.** The reviewer stand-in's unassisted draft located all nine seeded defects (Section 4.10) and, by its own account, ran more checks than a human could in an hour. This makes the demonstration a weak test of what the workbench adds: it compares the workbench with a reviewer who already does much of what the workbench does. The incremental recall of the workbench over the draft (Section 4.10) is therefore a lower bound on what it could add for a human reviewer under time pressure, and an unknown quantity for a human reviewer with different strengths. The base-model study's human benchmark (Section 7.8) and the critical test (Section 8) measure the real quantity.

3. **The simulated reviewers did not hold their technical settings.** The institutional lens is configured to spot-check (TEC.2) and to accept verbal derivations (INF.3), yet it re-derived Proposition 2 symbolically and wrote a check for it. The reason is in the instruction set: the common preamble tells every role to demonstrate formal claims with a check, and that rule overrode the lens's configuration. The four lenses' agreement on the Proposition 2 error is therefore partly an artifact of the preamble, not evidence that all four traditions would catch it. *Change:* a simulated reviewer writes checks only where its TEC.2 setting says its tradition would; formal checking beyond that is the probes' work.

4. **The panel lacked a sympathetic lens.** All four lenses reject MI7 (a non-significant coefficient means no effect), so none of them read the manuscript's central inference as its authors do, and the panel could not show that fault line. The lenses were configured to span traditions, not to span the manuscript's own inferences, and the panel synthesizer, given the configurations only as data, did not notice the gap (Section 4.5). *Change:* the default panel includes, for each material inference the manuscript's central claim relies on (read off the scoreboard), at least one lens that endorses it.

5. **"Demonstrated" is relative to a data-generating process.** Two probes tested nearly the same claim, that the Model 1 to Model 2 pattern does not discriminate between the accounts, with different simulations. One check was too weakly calibrated to decide (`p09:chk:6`, inconclusive); the other found the claim demonstrated, conditional on the reviewer accepting its process as a fair statement of the rival (`p10:chk:4`). Binding to code makes a finding inspectable, not unconditional. *Change:* every simulation check lists its premises, and a "demonstrated" verdict names the premises it depends on, each of which is a decision for the reviewer.

6. **The harness corrected the probes.** It refuted one probe's suspicion (the effect-size arithmetic is right), forced a probe to downgrade its only fatal finding, led a probe to withdraw a repair it had proposed (lagging modularity), and produced an unanticipated result that the probe correctly recorded as asserted, not demonstrated. Without the harness, all of these would have reached the reviewer as confident assertions. This is the strongest evidence in the runs for the proposal's insistence that formal claims be demonstrated, not asserted.

7. **The sealed key captures only part of what the runs found.** Real weaknesses outside the key include: a domain problem that reverses the buy rule when uncertainty is measured as a z-score (`p08:fnd:8`); the asset-specificity control as a control for the theory's own mechanism (Run 02); a downward bias in the peer coefficient under serially independent state shocks (`p09:fnd:12`, asserted); and an inconsistency in the reviewer's own draft, which recommends the state requirements as an instrument after saying they may raise outsourcing directly (Mode C, `bs:CI1`). A probe had raised the same threat to the instrument independently (`p09:ref:3`). Recovery against a key is a floor; unseeded yield, judged by experts, is a separate measure for this reason.

8. **The test manuscript is too easy for the models.** The middle and top tiers of the pilot located all nine seeded defects in a single pass (Section 7.9), and so did the reviewer stand-in's draft and several roles (Section 4.10). Set A of the base-model study must be harder: defects that need a derivation or a simulation to find, defects spread across long arguments, and passages that look defective but are not.

9. **The outputs are long.** The four simulated reviews run to between 8,266 and 9,585 words each, and the three probes, the panel synthesis and the consistency check add several times that. A human reviewer could not read all of it in the time the assisted track promises. The ranked lists the probes ended with, and the panel synthesis, are what a reviewer can use. *Change:* every role ends with a ranked digest, deduplicated across roles, which the reviewer reads before the full outputs.

10. **Agents do not follow the schema unaided.** The elicitor's perspective block used other key names and nesting, and the orchestrator had to normalize it. *Change:* validation at every hand-off, with one request to the agent to correct its output and any remaining coercion logged.

11. **A closed model's safeguards can refuse a reviewing task.** Two of the six pilot runs were first refused by an automated safeguard of the provider's interface and succeeded only after the wrapper was reworded (Section 7.9). In production, such refusals would silently drop roles from a review. *Change:* the gateway logs every refusal as a provenance event, and the editor view reports any role that did not run.

12. **Literature needs a tool.** No agent could search, so every uncertain citation was flagged, and Section 4.11 had to check them afterwards. None was invented, and one carried a wrong issue number. P-LIT needs a literature search bound to its findings, as P-DER is bound to symbolic algebra.

13. **The perspective distance hides the commitments that drive disagreement.** Verdict divergence did not rise with distance, and the sharpest split in the panel fell between the closest pair, on one material inference (MI6) whose reversal moves their distance by less than 0.02 (Section 4.5). The distance is still useful for its intended purpose (the lenses it calls resembling and differing behaved as such), but it is the wrong quantity for predicting where reviewers will disagree. *Change:* the distance is always reported with the opposed inferences (Sections 1.4 and 5.3; the tool now prints them), and the default panel is composed from the inferences the manuscript's central claim relies on (item 4), not from distance alone.

14. **The harness mislabeled a check, and a role caught it.** The panel synthesizer found that one output file carried the wrong check id, because the harness took the id from a comment in the code that referred to an earlier check; it also found two checks that only defined functions and printed nothing (Section 4.5). The files are kept as they were produced, and the synthesis records the correct reading. *Change:* each check declares its id in a fixed first line, the harness refuses a block without one, and a check that prints nothing is logged as not run.

15. **Text overlap does not measure what the workbench contributed.** The signed review's machine-origin share is 1.9% by its definition, yet the reviewer made 109 accept or modify decisions on workbench findings and the review more than doubled in length (Section 4.9). The reviewer rewrote what it accepted. A reviewer hiding reliance on the workbench would do the same. *Change:* the decision composition, computed from the dispositions, is the primary measure of contribution, and the machine-origin share is kept as a secondary measure of wording (Section 5.3); validating both against expert judgments of where a review's content came from is listed as open work in Section 9.3.

16. **Deciding was harder than it needed to be.** The reviewer stand-in reported that one defect carried up to seven ids across the roles with different severities, that the probes' decision lists overlapped and were numbered differently, that severity conventions differed between the probes (scoped labels) and Mode C (one label per concern), and that accept, reject and modify fit findings but not choices between options or decisions about process (Section 4.8). It needed 117 decisions. *Change:* the panel synthesis deduplicates across all roles, probes included, and gives each defect one id that the dispositions use; decision lists use one numbering; the scoped severity label becomes the convention for every role; and the disposition vocabulary adds *choose* (between named options) and *note* (process, no review text).

---

## 5. Schema (draft v0.1) and measured quantities

> **Status: draft v0.1, 23 October 2026. Not yet implemented.** The schema is the current specification of the objects the workbench passes between roles and records. It was used as the output format of the runs in Section 4, which is its first test; field names and enumerations will change in Stage 1. The full JSON Schema (draft 2020-12) and JSON-LD context are in Annex A and in the repository as `schema/review-objects.v0.schema.json` and `schema/context.v0.jsonld`.

### 5.1 Design principles

1. **The perspective is an object.** `ReviewingPerspective` must set all five dimensions, each with a weight; perspectives can be stored, compared (Section 5.3), composed into panels and versioned. This is the schema-level form of the proposal's central move.
2. **A standards specification is never a review.** `StandardsSpecification.isReview` is fixed to `false`; the object has no field for findings about the manuscript.
3. **Scores are perspectival.** A `Scoreboard` names its scorekeeper (a perspective id). Consequential commitments must name the inference (`via`) by which they were attributed.
4. **Findings have a status, and only the harness can promote it.** `Finding.status` is `asserted`, `demonstrated`, `refuted-by-check` or `inconclusive`; the last three require a linked `CheckResult`.
5. **Simulated reviews say so.** `SimulatedReview.simulated` is fixed to `true`.
6. **The manuscript is referenced, not copied.** Objects refer to a `ManuscriptRef` (id and SHA-256 hash); manuscript text lives only in the gateway's manuscript store, under the retention rules of Section 6.
7. **Everything is addressable and traced.** Every node has an `@id`; every creation and every human decision is a `ProvenanceEvent`, whose timestamp is marked `actual` or `reconstructed`.
8. **Consent is data.** `ConsentRecord` lists the scopes each party has granted, so that the gateway can refuse any use outside them.

### 5.2 Node types

| Node | Required fields | Purpose |
|---|---|---|
| `ReviewingPerspective` | id, label, owner, five `DimensionSetting`s | A reviewer's (or a lens's) perspective: parameters, weights, material inferences, standards, corpus |
| `Standard` | id, dimension, statement, priority | One checkable standard, with its parameter and origin |
| `EditorBrief` | id, manuscript, needs | What the editor needs from this reviewer, concerns, audience |
| `StandardsSpecification` | id, reviewer, perspective, editorBrief | The Best-Self output, with tensions and their ranking |
| `ManuscriptRef` | id, sha256 | The manuscript, by hash |
| `Scoreboard` | id, manuscript, scorekeeper, commitments | `Commitment`s (avowed or consequential, with entitlement status), `Incompatibility`s, `Challenge`s |
| `SimulatedReview` | id, perspective, contributions, verdicts, findings, recommendation | One simulated reviewer's output |
| `Finding` | id, locus, problem, severity, status | One objection or probe finding |
| `PanelSynthesis` | id, reviews, survival, disagreements | Survival table, agreements, disagreement map, recommendation spread |
| `CheckSpec` | id, finding, language, code | An executable check written by a probe |
| `CheckResult` | id, check, ranAt, stdout, verdict | The harness's result |
| `ConsistencyReport` | id, specification, review, applied | Best-Self Mode C output |
| `ProvenanceEvent` | id, timestamp, timestampKind, actor, action, prevHash, hash | One hash-chained provenance entry |
| `ConsentRecord` | id, party, role, scope, grantedAt, instrumentVersion | What a party has consented to |

### 5.3 The measured quantities

The proposal says that once the reviewing perspective is an object, properties of scientific judgment that have never been observable become measurable. The draft operational definitions are below. All are computable from the schema; their reliability and validity are themselves Stage 1 objects of study.

| Quantity | Draft definition | Range |
|---|---|---|
| **Perspective distance** $d(P,Q)$ | Per parameter: Jaccard distance for sets; normalized rank difference for ordinal scales; 0/1 for other categories; mean rating difference for model-class and strategy ratings; material inferences scored +1/0/−1 and compared by mean absolute difference. Averaged within each dimension; dimensions weighted by the two perspectives' mean weights. Always reported with the *opposed inferences*, the catalogue entries one perspective endorses and the other rejects, because an average over parameters can hide the single inference on which a disagreement turns (Section 4.5). Free-text parameters are not compared. | 0 to 1 |
| **Cross-perspective survival** $S(c)$ | For contribution $c$, the mean over a panel of 1 (survives), 0.5 (qualified), 0 (fails). $c$ is *robust* if no reviewer rates it "fails"; *lens-dependent* if it survives only for reviewers whose pairwise distances are below the panel median. | 0 to 1 |
| **Fault-line share** | Of the disagreements between simulated reviewers, the share that blind coders trace to a named parameter difference. The proposal's claim that simulated disagreements "track real theoretical fault lines" is the claim that this share is high and that the parameters named are those on which the perspectives in fact differ. | 0 to 1 |
| **Scorekeeping accuracy** | Precision and recall of the commitments a role attributes, against a reference scoreboard compiled by two expert coders; Cohen's (1960) κ on entitlement status; recall of reference incompatibilities. | 0 to 1 each |
| **Seeded-defect recovery** | On manuscripts with a sealed defect key: the share of seeded defects *located* (right locus and right reason), with *touched* (right locus, wrong or generic reason) reported separately. Reported per dimension. | 0 to 1 |
| **Demonstration rate** | Of located defects that are demonstrable by a check, the share actually demonstrated by the harness. | 0 to 1 |
| **False-alarm rate** | The share of a role's findings judged *mistaken* by expert adjudication (the manuscript does not commit the authors to what the finding says, or the finding's reasoning is wrong). | 0 to 1 |
| **Unseeded yield** | The number of findings not on the sealed key judged *substantive* by expert adjudication. | ≥ 0 |
| **Standards coverage** | Of the `must` standards in a reviewer's specification, the share the signed review applies; undeclared standards counted separately. | 0 to 1 |
| **Machine-origin share** | The share of sentences in a signed review whose token overlap with some agent output in the session exceeds a threshold (draft: 0.6 on 5-gram overlap, after removing 5-grams in the manuscript and in the reviewer's unassisted draft). It measures wording, not content: a reviewer who rewrites accepted findings scores low (Section 4.9), so it is always reported with the decision composition. | 0 to 1 |
| **Decision composition** | From the dispositions: the number of workbench findings accepted, modified and rejected, the share of the signed review's concerns that contain at least one accepted or modified finding, and the share of findings adopted without modification. The primary record of what the workbench contributed to a review. | counts; 0 to 1 |
| **Human-likeness** | The area under the curve (AUC) of blind raters' judgments of whether a review was written with or without agent assistance; 0.5 means indistinguishable. Reported with a stylistic profile: length, hedging density, nominalization rate, Flesch Reading Ease (Flesch 1948). | 0.5 to 1 |
| **Inferential validity** | Reported as its components (scorekeeping accuracy, recovery, false alarms, placement accuracy) and as a pre-registered index: the mean of their standardized values. **Never combined with human-likeness.** | standardized |
| **Incremental validity** | For a review: the paired difference, on the same manuscript, between the inferential-validity index of the assisted and of the conventional review. For a role: incremental recall, the share of the reference audit's unentitled commitments the role locates that the reviewer's unassisted draft did not, reported beside the role's false alarms (Section 9.2). | standardized; 0 to 1 |
| **Review diversity** | For the reviews of one manuscript, the mean pairwise Jaccard distance between their sets of coded findings (locus × reason), and their evaluative range (the number of distinct finding categories, e.g. theory, data, method, placement). Compared between assisted and unassisted reviews to test the homogenization risk. | 0 to 1; count |

Two of these quantities answer findings the special issue's own editorial reports. Gartenberg, Hasan, Murray and Pierce (2026) find that reviews written with AI at this journal "are harder to read, with more complex word choice, more nominalization, and more jargon", are biased "toward a 'theory' focus and away from a 'data' focus", and "cover a narrower evaluative range", so that "review diversity systematically decreases". The stylistic profile and the review-diversity measure make these properties outcomes in the base-model study (Section 7) and the critical test (Section 8), where the question is whether a *structured* workbench (explicit standards, a panel of differing perspectives, probes bound to checks) reverses or deepens them relative to unstructured use.

---

## 6. Governance and consent protocol

Manuscripts under review are privileged. This section sets out how the gateway and the studies handle them: what is hosted where, who consents to what and in what words, what is stored, for how long and how it is deleted, who can see the provenance record, how the commitment not to train on submitted manuscripts is enforced, and what ethics review and oversight apply. It is written to be adopted, with local changes, by any venue that partners with the project, and it is developed in the open because, as the proposal argues, the field needs a workable model for this whether or not it uses this suite.

### 6.1 The policy landscape this protocol answers

Existing policies on generative AI in peer review rest mainly on **confidentiality**. The U.S. National Institutes of Health prohibits its peer reviewers from using generative AI, on the ground that "AI tools have no guarantee of where data are being sent, saved, viewed, or used in the future" (NIH 2023, NOT-OD-23-149). The Academy of Management states that "AI should never substitute for the reviewer’s personal assessment of the quality, contribution, or integrity of a submission" and prohibits reviewers from "upload[ing] any portion of a manuscript, including text, figures, or data, into any AI tool or platform" in order to "preserve confidentiality and intellectual integrity" (Academy of Management n.d.). Elsevier's policy tells reviewers not to "upload the material/manuscript or any part thereof into a generative AI tool" and not to use AI "to assist in the review", while noting that the publisher's own "identity protected AI-assisted technologies ... respect confidentiality" (Elsevier n.d.). INFORMS journal guidelines tell members of the review team not to upload any part of a manuscript "into a generative AI tool such that it might compromise confidentiality and/or copyright" (INFORMS n.d.). The special issue's own editorial argues that the field's "response cannot be purely technical approaches or consist solely of disclosure policies or AI 'bans'" (Gartenberg et al. 2026).

The protocol takes these policies at their word. It does not ask any reviewer to do what their journal forbids: assisted review takes place only at a venue that has adopted the protocol for the study, under the venue's explicit authorization, inside an environment controlled by [institution], with the authors' consent. The protocol is designed to remove the confidentiality ground for prohibition (data leaving a controlled environment for unknown use), so that what remains of the question is the one the proposal wants studied: what machine assistance contributes to review, and what it only performs.

### 6.2 Principles

1. **No use without consent.** No manuscript enters the gateway unless the venue has authorized the study and the authors have consented to the specific use.
2. **Controlled hosting.** Manuscript text is processed only in an environment controlled by [institution], or by model providers bound by the terms in Section 6.4.
3. **Minimization.** Only the manuscript text needed for the review enters the gateway; logs hold hashes and ids, never text.
4. **No training.** No submitted manuscript, review, standards specification or provenance record is used to train or fine-tune any model, by the project or by any provider.
5. **Human accountability.** The reviewer remains the author of the review and signs it; the provenance record makes the composition of every assisted review inspectable by the editor.
6. **Open governance.** The protocol, its revisions, and summaries of its audits are public.

### 6.3 Data flow

```
 Journal submission system
   │  (author consents to the study at submission; Section 6.5)
   ▼
 Venue exports consented manuscript ──► Gateway manuscript store at [institution]
                                         (encrypted at rest; key held by [institution]; access-logged)
   │
   ├─► Agent roles (via router) ──► open-weight models on [institution] hardware
   │                            └─► closed models only via enterprise endpoints meeting §6.4
   ├─► Check harness (sandboxed; no network)
   └─► Provenance layer (ids, hashes, actions, decisions; never manuscript text)
   │
   ▼
 Reviewer's workbench session (authenticated; reviewer sees the full trace)
   │
   ▼
 Signed review + editor view of provenance ──► Journal system (normal confidentiality)
   │
   ▼
 After the decision: research extraction (de-identified scores and coded findings only)
                     manuscript text and manuscript-derived outputs deleted (§6.6)
```

### 6.4 Hosting and model access

- **Open-weight models** (the lower and middle tiers of the base-model study, and the default for confidential material) run on hardware controlled by [institution].
- **Closed models** are used on confidential manuscripts only through enterprise or API agreements that (i) exclude the use of inputs and outputs for training, (ii) set retention of inputs and outputs to zero or to a fixed short window for abuse monitoring, after which they are deleted, (iii) bind the provider to confidentiality, and (iv) fix the processing region. The exact terms of each provider are checked, recorded in the registry, and reviewed at each contract renewal. A model whose provider cannot meet these terms is used only on the non-confidential sets (synthetic manuscripts and published papers; Section 7.3).
- **Separation.** The manuscript store has no read path to any training or fine-tuning pipeline. Lens corpora and instruction-set development use only published, synthetic or explicitly released material.

### 6.5 Consent

Consent is collected from three parties, separately for each scope, and recorded as `ConsentRecord`s that the gateway checks before every use. Consent to one scope never implies another. Declining any research scope has no effect on the editorial process.

| Scope | Editor / venue | Author | Reviewer |
|---|---|---|---|
| `workbench-use`: the reviewer may use the workbench on this manuscript | Venue authorizes | Consents | Consents to use, and to provenance logging of their session |
| `ai-assisted-track`: the author chooses the assisted track (Section 8) | Venue offers | Chooses | (n/a) |
| `pairing`: the manuscript is also reviewed in the other mode, for research | Venue authorizes | Consents | Consents to their review being paired |
| `research-use`: de-identified scores and coded findings enter the study dataset | Venue authorizes | Consents | Consents |
| `blind-evaluation`: after the decision, the author and editor rate reviews of this manuscript blind to their source | Editor agrees | Consents | Consents to their review being rated |
| `deidentified-release`: the de-identified research dataset may be released publicly | Venue authorizes | Consents | Consents |
| `base-model-study`: the manuscript may be among those on which base models are compared (Section 7) | Venue authorizes | Consents | (n/a) |

**Timing.** Authors consent at submission and may withdraw any research scope until the decision on the round; withdrawal triggers deletion within seven days. Reviewers consent when accepting the invitation. The venue's authorization is a written agreement, approved by the venue's editorial board and the publisher, specifying the scopes it offers.

**Instruments.** The consent language for authors, reviewers and editors is in Annex E (`governance/CONSENT_INSTRUMENTS.md`). It states in plain words what the workbench is, that a human reviewer remains responsible, where the manuscript is processed, the no-training commitment, the retention periods, who sees the provenance record, and how to withdraw.

### 6.6 Retention and deletion

| Data | Where | Retention | Deletion |
|---|---|---|---|
| Manuscript text | Gateway manuscript store | Until 30 days after the decision on the round (to allow the reviewer to complete the report and the editor to query it); on withdrawal, 7 days | Cryptographic erasure of the manuscript's key; a `ProvenanceEvent` records the deletion and its time |
| Agent outputs (which quote the manuscript) | Gateway, linked to the session | As manuscript text | As manuscript text |
| Signed review and editor view | Journal system | The journal's normal retention for review records | The journal's procedures |
| Provenance metadata (ids, hashes, actions, decisions, model versions; no text) | Gateway | Seven years, for audit | Then deleted |
| Research dataset (de-identified scores, coded findings, stylistic metrics; no manuscript text, no review text) | Study repository at [institution] | As approved by the ethics board; released publicly only under `deidentified-release` | As approved |
| Provider-side copies (closed models) | Provider | Zero, or the fixed window in the agreement | By contract; verified at audit |

### 6.7 Who can see the provenance record

| View | Who | Contents |
|---|---|---|
| Reviewer view | The reviewer, during and after the session | The full trace of their session |
| Editor view | The handling editor and the editor-in-chief, attached to the signed review | Which capabilities were used; every finding consulted, with the reviewer's decision on it; where the accepted and modified findings land in the review; passages of the review originating in agent output, and the machine-origin share, marked as a measure of wording; model and instruction-set versions |
| Author view | The authors, with the decision letter | A short statement that the review was written with the workbench, which capabilities were used, and the reviewer's attestation that they read the manuscript in full and take responsibility for every statement in the review |
| Research view | The study team, after the decision, under the ethics protocol | De-identified trace: actions, decisions, timings and coded findings, without text |
| Audit view | The external auditor | Access logs, deletion events, provider terms |

### 6.8 Enforcing the no-training commitment

The commitment is enforced at three levels. **Contractual:** provider agreements exclude training on inputs and outputs (Section 6.4), and the project's own data-use agreements with venues forbid it. **Technical:** the manuscript store is isolated from every model-development environment, egress from the gateway is restricted to the approved endpoints, and every access to manuscript text is logged. **Audit:** an annual external audit checks the access logs, the deletion events and the provider terms, and its summary is published.

### 6.9 Ethics review and oversight

Every component that involves people (the open call, the paired reviews, the blind evaluations, the internal fallback study) is submitted to the research ethics board of [institution] before it begins, and to the partner venue's own review where it has one. A **governance board** oversees the platform: a representative of the partner venue's editors, an author representative, a reviewer representative, [institution]'s data-protection officer, and an external research ethicist. It approves changes to the protocol, receives audit reports, and holds a **stop rule**: any breach of confidentiality, any use outside consented scopes, or evidence that assisted reviews harm authors (for example, decisions systematically driven by unverified agent findings) suspends the study pending review. Breaches are reported to the venue and the affected parties within 72 hours.

### 6.10 Reproducibility under confidentiality

The special issue's call asks for projects that can share enough data to be reproduced. Confidential manuscripts and reviews cannot be shared. The project therefore releases everything else: instruction sets, schema, gateway configuration, lens registry, check harness, the synthetic manuscripts with their sealed keys, all runs on synthetic and published manuscripts (Section 7.3), and the de-identified research dataset where consented. Every quantitative result in the studies is computed on data that are either fully shareable or released in de-identified form.

---

## 7. Base-model dependence study

### 7.1 Question

Hold the reviewing task and the manuscript fixed, vary the potency of the base model, and measure which properties of the resulting review scale with capability and which do not. The proposal expects a decomposition of the reviewing act into **capability-bound** components (catching a computational error, checking an identification claim, tracking an unentitled commitment across a long argument, recovering a missed literature) and **stylistic** components (fluency, hedging, the mimicry of a reviewer's voice). In inferentialist terms: at what point does a model become a competent scorekeeper in the discourse rather than a fluent impersonator of one?

### 7.2 Models

The gateway serves models in four tiers:

| Tier | Description | Examples of families (exact versions fixed at pre-registration) |
|---|---|---|
| T1 Frontier closed | The most capable tier of each major closed family | Claude (Anthropic), GPT (OpenAI), Gemini (Google) |
| T2 Mid closed | Smaller, faster tiers of the same families | The same families' mid-sized tiers |
| T3 Large open-weight | Open-weight models of roughly 70 billion parameters or more | Families such as Llama, Qwen, Mistral, DeepSeek |
| T4 Small open-weight | Open-weight models of roughly 7 to 14 billion parameters | Small members of the same families |

Model versions change quickly, so the exact roster (at least ten models, at least two per tier, with at least two families represented within the closed and the open tiers) is fixed in the pre-registration and every call logs the exact version string. **Potency** is measured in two ways, fixed in advance: (i) a *potency index*, the first principal component of the models' published scores on a pre-registered set of public reasoning and knowledge benchmarks, standardized; and (ii) *within-family rank*, the cleanest contrast, because models of one family share training lineage and differ mainly in capability. Results are reported on both; a property is classified only if the two agree.

### 7.3 Manuscripts held fixed

| Set | Content | Why |
|---|---|---|
| **A. Seeded synthetic** | 24 manuscripts written for the study, in the format of organization-science submissions, 12 in organizational economics and strategy and 12 in organizational sociology and behavior. Each has 8 to 10 seeded defects spanning all five dimensions, recorded in a sealed key hashed before any run (as for the test manuscript in Section 4). Written by team members who take no part in scoring. | A ground truth for recovery, immune to training-data contamination because neither the manuscripts nor their defects exist anywhere a model could have read them |
| **B. Published with documented critiques** | 20 published organization-science papers that later received published comments, corrections or retractions with identifiable points. Where possible, papers whose critiques appeared after the training cutoffs of the models compared. | Realism: defects that real reviewers missed. Contamination is possible; Set B results are reported separately and compared with Set A |
| **C. Consented submissions** | Up to 40 real submissions from the critical test whose authors consent to `base-model-study` (Section 6.5), run only on T3/T4 models and on closed models meeting Section 6.4 | External validity on real, unpublished work |

### 7.4 Tasks held fixed

T1 scoreboard construction; T2 each probe type (P-DER, P-ID and P-NUM with the harness; P-INF, P-MEAS and P-LIT without); T3 a simulated review under a fixed perspective (the same four lenses as Section 4); T4 panel synthesis from fixed simulated reviews; T5 a single-pass review with no workbench (the condition closest to unstructured use, as measured in the special issue's editorial); T6 the Best-Self consistency check, given a fixed specification and a fixed human draft. Best-Self elicitation itself requires a human respondent and is studied in Section 8, not here.

### 7.5 Design

A factorial design: model (≥ 10) × style condition (3) × manuscript (Sets A and B; C where consented) × task, with three replicate calls per cell at fixed sampling settings, so that within-cell variability can be estimated. The three **style conditions** manipulate voice while holding the task fixed: **S0** neutral instructions; **S1** "write in the voice of a senior, authoritative reviewer for a leading journal"; **S2** "terse numbered findings, no rhetoric". A manipulation check confirms that the style conditions move the stylistic profile.

### 7.6 Measures

*Candidates for capability-bound properties*: seeded-defect recovery (overall and per dimension), demonstration rate, false-alarm rate, scorekeeping precision and recall, incompatibility recall, literature-placement accuracy, unseeded yield, reproducibility across replicate calls. *Candidates for stylistic properties*: length; hedging density; nominalization rate; Flesch Reading Ease; conformity to the conventional review format; politeness; and **human-likeness** as rated by blind expert raters. All are defined in Section 5.3. Scoring of recovery, false alarms and unseeded yield is done by two expert coders, blind to model and style condition, with disagreements adjudicated and Cohen's κ reported.

### 7.7 Pre-registered classification rule

For each property $Y$, fit a mixed model with fixed effects for potency, style condition and their interaction, and random effects for manuscript and model family. With equivalence bound $\Delta = 0.2$ SD of $Y$ (two one-sided tests, α = 0.05, Schuirmann 1987, Lakens 2017; Holm 1979 correction within each family of properties):

- **Capability-bound:** the potency effect is in the expected direction with its 95% CI excluding zero, **and** every style contrast is equivalent to zero within ±Δ.
- **Stylistic:** at least one style contrast lies outside ±Δ, **and** the potency effect is equivalent to zero within ±Δ, or saturates (the difference between the T4 and T1 means is within ±Δ).
- **Mixed:** both potency and style effects lie outside ±Δ.
- **Undetermined:** none of the above.

The rule is applied to each property separately, so the result is a map of the reviewing act: which of its components a more capable model does better, which any model can be prompted to perform, and which are both.

### 7.8 The competent-scorekeeper threshold

A human benchmark is collected on Set A: 12 expert reviewers (paid, consented), each reviewing 4 Set A manuscripts unassisted, scored by the same blind coders. For scorekeeping accuracy and seeded-defect recovery, a segmented regression on the potency index estimates the potency at which models reach the **median expert human** score, with a bootstrap CI. A model is classed a **fluent impersonator** on a task if its human-likeness is within the human range while its inferential validity is below the human median. The proportion of models in that class, by tier, is the direct measure of capability laundering.

### 7.9 Pilot: one manuscript, three model tiers, two styles

To test the pipeline end to end before Stage 1, the single-pass review task (T5) was run on the test manuscript of Section 4 with three tiers of one model family (Claude Haiku, Sonnet and Opus, as served on 23 October 2026) under two style conditions (S1 reviewerly; S2 terse), six runs in all. The six outputs were shuffled and given letter labels, and scored against the sealed key by a separate Claude instance that was told neither the model nor the style of any output. Stylistic metrics were computed by `tools/style_metrics.py`. **This is a single manuscript, a single run per cell and a model scorer, so it supports no inference; it shows that the measures can be computed and how they will be reported.**

| Tier | Style | Report | Seeded located (of 9) | Touched | Missed | Known-unseeded (of 5) | New substantive (categories) | Mistaken | Words | Hedges per 1,000 words | Nominalizations per 100 words | Flesch Reading Ease | Recommendation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Haiku | S1 reviewerly | A | 8 | 1 (SD4) | 0 | 4 | 10 | 1 | 3,586 | 2.8 | 7.3 | 42.6 | Reject, with encouragement to resubmit |
| Haiku | S2 terse | D | 5 | 3 (SD4, SD5, SD7) | 1 (SD9) | 4 | 8 | 0 | 2,067 | 3.4 | 4.7 | 56.7 | Major revision |
| Sonnet | S1 reviewerly | E | 9 | 0 | 0 | 4 | 13 | 0 | 4,493 | 3.6 | 7.2 | 33.9 | Reject (in present form) |
| Sonnet | S2 terse | B | 9 | 0 | 0 | 4 | 12 | 0 | 2,359 | 3.4 | 7.2 | 43.6 | Major revision |
| Opus | S1 reviewerly | F | 9 | 0 | 0 | 4 | 13 | 0 | 4,927 | 3.5 | 7.2 | 40.8 | Major revision |
| Opus | S2 terse | C | 9 | 0 | 0 | 4 | 11 | 0 | 2,831 | 3.5 | 7.3 | 47.2 | Major revision |

Sources: `runs/13_pilot/scoring.md` (the blind scorer's codes, quotations and seven calls it was unsure of), `runs/13_pilot/UNBLINDING_MAP.json` (its SHA-256 was logged at `ev:9`, before scoring, and matched at unblinding, `ev:25`), `runs/13_pilot/style_metrics.txt`. Every report found the four known unseeded weaknesses KU1 to KU4; none noted the corner solution KU5.

**What the pilot shows about the design, not about the models.**

1. **Ceiling.** The middle and top tiers located all nine seeded defects in a single pass, in both styles. The test manuscript was written to exercise the workbench, not to discriminate between models, and it is too easy for that purpose. Set A must be harder: more defects that need a derivation or a computation to find, defects spread across longer arguments, and decoy passages that look defective but are not. Without that, recovery cannot show capability-bound scaling above the lowest tier.
2. **A first sign of a mixed property.** The lowest tier lost recovery under the terse style (8 located to 5), while the other tiers did not. If it held up, recovery would be capability-bound above some potency and style-sensitive below it, which is the "mixed" class of Section 7.7. One run per cell cannot distinguish this from noise.
3. **The style manipulation was weak.** The terse condition shortened reviews by 42 to 47 percent but left them at 2,000 to 2,800 words, and moved hedging and nominalization little except in the lowest tier. The manipulation check of Section 7.5 would have flagged this. The S2 instruction needs a length cap.
4. **Recommendation follows style as much as content.** The two reviewerly reports from the lower and middle tiers recommended rejection; the other four recommended major revision, on very similar findings. Recommendation is therefore a candidate stylistic property, to be measured, not assumed to track inferential validity.
5. **Unseeded yield is large.** Each report raised 8 to 13 substantive points not on the sealed key, judged real by the scorer. A sealed key measures recall against the defects the authors of the test planted, not the whole of what a good review finds, which is why expert adjudication of unseeded findings is part of the design.

**Departures to disclose.** The two Sonnet runs were first refused by an automated safeguard of the model provider's interface (an error naming "reasoning extraction"); both were rerun with a reworded wrapper ("write a referee report on the academic manuscript") and the same task text, and the reruns are the ones scored. The Haiku S1 run wrote its report but returned no completion message. The scorer is a model, and its seven uncertain calls are listed in `scoring.md`. Under the stricter readings it names, reports A and D (Haiku) would lose SD2 and reports C and F (Opus) would lose SD5; under the more lenient ones, A and D would gain SD4 and D would gain SD7. None of these changes the ceiling.

---

## 8. The critical test: a two-track open call

### 8.1 Design

In cooperation with a partner venue (a journal, or a dedicated submission venue set up for the study), the project issues an open call for papers in which authors **choose their review track** at submission:

- **Assisted track.** Each manuscript is reviewed by human reviewers using the workbench (Section 2.7), under the governance protocol (Section 6), with a target turnaround agreed with the venue that is a small fraction of its usual time to first decision.
- **Conventional track.** Reviews at the venue's usual pace, without the workbench.

Reviewers in both tracks are recruited, briefed and paid on the same terms. Editors handle both tracks and alone make the decisions. Authors who consent to `pairing` receive, in addition, one review from the other track, so that the same manuscript has both an assisted and a conventional review. After the decision, authors and editors who consent to `blind-evaluation` rate every review of the manuscript without being told how it was written. A reference audit, compiled by two expert adjudicators blind to source from all reviews of the manuscript and from harness checks run on its formal and numerical claims, provides the reference scoreboard and the validated set of unentitled commitments against which reviews are scored.

### 8.2 Hypotheses (to be registered before launch)

| | Hypothesis | Measure | Test |
|---|---|---|---|
| H1 | **Revealed trust.** A substantial share of authors choose the assisted track under a real speed–assurance tradeoff; the share varies with career stage and paper type as pre-specified (more junior authors and empirical papers more likely to choose it) | Track choice | Share with 95% CI; logistic regression on pre-registered predictors |
| H2 | **Parity on inferential auditing.** On commitment fidelity and on unentitled commitments located, assisted reviews are non-inferior to the **best** conventional review of the same manuscript | Reference-audit scores; blind ratings on the four criteria | Paired non-inferiority, margin 0.3 points on a 7-point scale (about 0.25 SD of the difference) |
| H3 | **Superiority on identifiable sub-tasks.** Assisted reviews exceed conventional ones on (a) derivation and numerical consistency, (b) incompatibilities located across long arguments, (c) placement of the contribution among its rivals | Recall against the reference audit, per sub-task | Paired tests, Holm-corrected across the three |
| H4 | **Separate axes.** Human-likeness and inferential validity are weakly related across reviews, and fluency measures do not predict inferential validity once source is controlled | AUC of source judgments; correlation of human-likeness with the validity index | Correlation with CI; regression |
| H5 | **Usefulness.** Authors and editors rate assisted reviews at least as useful | Blind usefulness ratings | Paired non-inferiority |
| H6 | **Diversity.** Assisted reviews of a manuscript are at least as diverse as conventional ones | Review diversity (Section 5.3) | Paired comparison |
| H7 | **Speed.** Assisted reviews arrive faster | Days from invitation to submission of review | Comparison of medians |

**The four evaluation criteria** are those named in the proposal: (1) did the review correctly identify what the paper commits its authors to; (2) did it locate real unentitled commitments; (3) did it place the contribution accurately in the landscape of ideas; (4) was it useful. Criteria (1) and (2) are scored objectively against the reference audit and also rated by editors and authors; (3) and (4) are rated. **Human-likeness and inferential validity are reported as separate axes** throughout: the rating instrument asks raters to judge how a review was written (the human-likeness measure, which doubles as a check on blinding) separately from the four criteria, and no composite of the two is ever computed.

H2 and H3 together are the incremental-validity benchmark that the proposal names as its defense against objection theater (Section 9.2).

"Best conventional review" is defined in advance as the conventional review of the manuscript with the highest reference-audit score; H2 is also reported against the mean conventional review.

### 8.3 Blinding

Reviews are put into a common format before rating (headers, salutations and formatting normalized; review length is not altered). Raters are not told the source and rate only after the decision, so that ratings cannot affect decisions. Each rater also guesses the source of each review; the accuracy of those guesses (as AUC) is reported both as the human-likeness measure and as the degree to which blinding held.

### 8.4 Sample size

The calculations are in `tools/power_critical_test.py`; inputs marked as assumptions there will be replaced by estimates from the first two months of the call before the sample size is locked.

| Requirement | Paired manuscripts needed |
|---|---|
| H2 non-inferiority, SD of paired difference 1.2, margin 0.3, one-sided α = 0.025, power 0.80 | 126 |
| … power 0.90 | 169 |
| H3 superiority on a sub-task, recall difference 0.10, SD 0.25, power 0.80, Holm's smallest threshold | 66 |
| H4 human-likeness: with 150 reviews per source, SE(AUC) ≈ 0.033, so an AUC of 0.60 is distinguishable from 0.50 (z ≈ 3.1) | 150 |

The target is **150 paired manuscripts**. If about half of submitting authors choose the assisted track and about half of all authors consent to pairing, this needs roughly 300 to 400 submissions, which sets the length of the call (planned at twelve months).

### 8.5 Selection into track

Authors choose their track, so the tracks receive different manuscripts. The quality comparisons (H2, H3, H5, H6) are **within manuscript**, between the assisted and conventional reviews of the same paper, so selection into track does not bias them; it limits their generalization to manuscripts whose authors consent to pairing, whose characteristics are compared with those of non-consenting authors and reported. Track choice itself (H1) is the object of the revealed-trust analysis. To separate trust from impatience, the venue may randomize, at submission, the information authors receive about expected turnaround in the two tracks; if adopted, this is registered as a secondary design.

### 8.6 The fallback

If a venue partnership is not secured in time, the paired comparison is run internally at smaller scale: 30 to 40 working papers and pre-submission drafts from the investigators' networks, with their authors' consent, each reviewed once with the workbench and once without by reviewers recruited for the study, under the same consent, blinding, reference-audit and rating protocol. With 30 pairs the minimum detectable difference in mean rating is about 0.61 points (0.51 SD); with 40, about 0.53 points (0.44 SD). The fallback can therefore detect only moderate or larger differences, and its results will be reported as such. H1 cannot be tested in the fallback, because there is no real speed–assurance choice.

### 8.7 Registration and reporting

The hypotheses, measures, margins, analysis models, sample-size rule and stopping rule are registered on a public registry before the call opens. Deviations are reported. Results on every hypothesis are published whatever their direction, together with the de-identified dataset where consented (Section 6.10).

---

## 9. Opening the platform, risks, and status

### 9.1 Opening the platform

The proposal's last commitment is to release the suite through the gateway "as shared infrastructure, instrumented so that its use generates data on the perspective-dependence of evaluation across the field". The release has three parts, each governed by Section 6.

**What is released.** The instruction sets; the schema and its JSON-LD context; the check harness; the lens registry, with the rule for admitting a lens (a perspective in the schema, a curated corpus of at least ten works, and validation against the tradition's published critical record; Section 2.6); the material-inference catalogue, with the rule for admitting an inference (Section 1.3); the synthetic manuscripts with their sealed keys (Section 7.3); and the gateway configuration. All are versioned, and every output names the versions it used.

**Who can use what.** Any registered scholar can run the suite on published or synthetic manuscripts, and on their own drafts, through the gateway. Use on a confidential manuscript is possible only through a venue that has adopted the protocol of Section 6, with the consents recorded as `ConsentRecord`s. No route exists for an individual reviewer to upload a manuscript under review on their own initiative, which keeps the platform compatible with the journal policies in Section 6.1.

**What the instrumentation records, and what it is for.** With `research-use` consent, each session contributes de-identified records: the perspective objects used (the reviewer's elicited perspective and the lenses instantiated), the panel's survival table and disagreement map, the dispositions of findings, the machine-origin share of the signed review, and the coded findings of the review. From these the project computes, by subfield and over time:

| Field-level quantity | Computed from | Question it answers |
|---|---|---|
| Distribution of perspective distances among reviewers of the same manuscript | Elicited perspectives | How different are the reviewers editors actually assemble? |
| Fault-line share by subfield, and the parameters most often named | Panel disagreement maps | Which material inferences and settings divide the field's evaluations? |
| Robust versus lens-dependent contributions | Survival tables | How much of what papers claim survives across the field's perspectives? |
| Review diversity and evaluative range, assisted and unassisted | Coded findings | Does assisted review converge or diversify? (the homogenization risk) |
| Machine-origin share and finding acceptance rates | Provenance records | Where does augmentation shade into substitution in practice? |

**Monitoring rule for homogenization.** If, over any six-month window, the review diversity of assisted reviews falls below that of unassisted reviews at the same venues by more than a pre-registered margin, the governance board (Section 6.9) reviews the default lens sets and the elicitation defaults, and the result is published. The platform is built to multiply perspectives; this rule makes it answerable when it does not.

### 9.2 The risks of Section 5 of the proposal, and how each is measured

The proposal treats each risk as something to be measured, not only mitigated. The table gives, for each, the architectural safeguard, the measure, and where it is tested.

| Risk | Safeguard in the architecture | Measure (Section 5.3) | Where tested |
|---|---|---|---|
| **Substitution**: a reviewer signs machine output | The Best-Self agent produces a specification, never a review (`isReview: false`); the reviewer drafts before seeing any agent's view of the manuscript; every finding needs an explicit disposition before it can enter the review; the editor view shows the composition of the review | Decision composition and machine-origin share; share of findings adopted without modification; standards coverage | Run 14 (one review); the open platform (field level); the critical test, where the relation between machine-origin share and blind-rated quality is a registered secondary analysis. This relation is how the boundary between augmentation and substitution becomes a first-order object of study |
| **Confidentiality and consent** | Section 6 in full | Audit findings; deletion events; consent coverage of every use | Annual external audit (Section 6.8) |
| **Homogenization of judgment** | Several lenses per panel, always including a resembling and a maximally differing one; a pluggable, contested lens registry; the synthesis never averages | Review diversity and evaluative range | Critical test, H6; the platform's monitoring rule (Section 9.1) |
| **Sycophancy and objection theater** | Every objection must name the commitment, the missing entitlement and the repair; "no material finding" is acceptable; a fixed severity scale; formal claims take their status from the harness, not the agent | False-alarm rate; demonstration rate; the share of findings refuted by check; unseeded yield; the incremental-validity benchmark | Base-model study (Section 7); critical test, H2 and H3; Section 4.6 shows a probe's own suspicion refuted by its check |
| **Capability laundering**: authoritative-sounding but invalid reviews | Human-likeness and inferential validity are separate measures and are never combined | Human-likeness (AUC) beside the inferential-validity index; the share of models classed "fluent impersonator" | Base-model study (Section 7.8); critical test, H4 |

**The incremental-validity benchmark.** The proposal names it as the defense against objection theater. It is defined at two levels. *For a review*: the paired difference, on the same manuscript, between the inferential-validity index of the assisted review and that of the conventional review (the quantity H2 and H3 test, Section 8.2). *For a role*: incremental recall, the share of the reference audit's unentitled commitments that the role locates and the reviewer's unassisted draft did not, reported beside the role's false alarms. A role that adds findings only by adding false alarms has no incremental validity. Section 4.10 computes the role-level version for the demonstration, and a within-reviewer analogue of the review-level version (the signed review against the same reviewer's unassisted draft).

### 9.3 Status of components

| Component | Status on 23 October 2026 | Evidence | Stage 1 work |
|---|---|---|---|
| Reviewing perspective: five dimensions, 29 parameters | Specified (v0.1); one perspective elicited, four configured | Section 1; Runs 01, 03–06 | Reliability of elicited settings across occasions; validation with human reviewers |
| Material-inference catalogue | Specified (v0.1), ten entries | Section 1.3 | Growth by the admission rule; review by members of each tradition |
| Instruction sets (four roles) | Written (v0.1) and exercised once each on one manuscript | `instruction-sets/`; Section 4 | Revisions from Section 4.12; human-participant pilots |
| Schema and JSON-LD context | Draft (v0.1); `ProvenanceEvent` validated on every event of the trace; agents' other objects only partly conform | `schema/`; Section 5; Section 4.12 | Validation and coercion at every hand-off; version 1.0 |
| Check harness | Prototype: isolated subprocess, empty environment, no network, time limit; one labeling fault found in the runs (Section 4.12) | `tools/harness.py`; 37 checks run in Section 4 (18 by the simulated reviewers, 18 by the probes, 1 by the panel synthesis) | Hardened sandbox on [institution] hardware; resource limits; audit log |
| Provenance layer | File-based stand-in: hash-chained events, actual and reconstructed times | `tools/prov.py`; `runs/provenance_events.json` | The layer itself: access control, views, retention and deletion events |
| Editor view; machine-origin share | Prototype tools, run once | `runs/14_editor_view.md`; `tools/machine_origin.py`; `tools/editor_view.py` | Interface for editors; validation of the overlap threshold against human judgments; a content-level origin measure (Section 4.9) |
| Perspective distance | Prototype tool; reports opposed inferences since Run 07 | `tools/perspective_distance.py`; Sections 1.4 and 4.5 | Reliability; sensitivity to parameter coding; whether opposed inferences predict disagreement better than distance |
| Orchestration (the workbench) | Not built; in the runs, a Claude session moved objects between roles by hand | Section 4.0 | The workbench software |
| Multi-LLM gateway and lens registry | Not built; one model family used, lenses in one file | Section 2.6 | Build at [institution] |
| Governance protocol and consent instruments | Drafted | Section 6; Annex E | Ethics review; venue agreement |
| Base-model dependence study | Designed and pre-registrable; pipeline piloted on one manuscript | Section 7; Run 13 | Set A of 24 harder manuscripts; the full study |
| Critical test | Designed; sample size computed | Section 8; `tools/power_critical_test.py` | Venue partnership or fallback; registration; the study |
| Open platform | Planned | Section 9.1 | Release after the critical test begins |

### 9.4 Where each commitment of the proposal is met

| The proposal says | Section of the proposal | Where this appendix delivers it |
|---|---|---|
| The reviewing perspective, a configuration of ontological, epistemological, inferential, technical and pragmatic commitments, becomes an explicit, inspectable and manipulable object | §1 | Section 1 (dimensions, parameters, the catalogue of material inferences, distance); `ReviewingPerspective` in Section 5; elicited and configured perspectives in Section 4 |
| Agents keep deontic score on commitments and entitlements and make the right inferential moves | §1, §6 | The `Scoreboard` shared by every role (Sections 2 and 5); scorekeeping accuracy (Section 5.3); scoreboards in Runs 03–06 and 08–10 |
| The Best-Self reviewer: an exchange with the editor, then a specification of the reviewer's standards, not a review, against which the review is checked | §2, §5 | Section 2.1; Run 01 (exchange and specification); Run 11 (the check of the draft against the specification) |
| Simulated reviewers whose commitments differ from or resemble the focal reviewer's; which contributions survive across lenses | §2, §6 | Section 2.2; Runs 03–06; perspective distances (Section 1.4); survival table (Run 07) |
| A composed board of alternative selves | §2 | Section 2.3; Run 07 |
| Probes bound to executable checks, so failures are demonstrated, not asserted | §2 | Section 2.4; Runs 08–10, including a derivation failure and an identification failure demonstrated by the harness (Section 4.6) |
| A multi-LLM gateway at [institution], serving base models of differing potency | §2, §4 | Section 2.6; Section 7.2 |
| Instruction sets and worked transcripts in the repository | §3 | `instruction-sets/`; `runs/`; Section 4 |
| Roles exercised end to end on a synthetic test manuscript with seeded defects, with model stand-ins in the editor and reviewer roles | §3 | Section 4 (Runs 01–14, all on one synthetic manuscript with a sealed key, with model stand-ins in the editor and reviewer roles; Section 4.0). The interactive runs on published manuscripts and the authors' drafts that §3 also mentions are not reported in this appendix |
| Elicited standards sharper and more checkable than a reviewer's first statement of them | §3 | Section 4.2 (from recollection to checkable standard); Section 4.7 (the draft checked against them); reviewer recognition is tested in the open call (Section 8), not here |
| Simulated reviews whose disagreements track real theoretical fault lines | §3 | Section 4.5: 10 of 18 disagreements classified as fault lines traced to named parameters, six through material inferences; they track individual commitments, not overall distance; coder validation by the fault-line share (Section 5.3) |
| Probes that locate genuine soft points, demonstrated by executed checks, rather than generic complaints | §3 | Sections 4.6 and 4.10: every seeded defect that a check can demonstrate was demonstrated; unseeded findings beyond the reviewer's draft; no finding judged mistaken |
| The provenance layer, with every agent contribution and human decision on inspectable record | §4, §5 | Sections 2.5 and 5; Run 14 (trace and editor view) |
| The base-model dependence study: capability-bound against stylistic components; competent scorekeeper against fluent impersonator | §4 | Section 7, with a pre-registered classification rule, a threshold analysis and a pilot (Run 13) |
| The two-track open call: revealed trust, paired reviews rated blind on four criteria, registered hypotheses, human-likeness and validity as separate axes, an internal fallback | §4 | Section 8 |
| Open the platform, instrumented | §4 | Section 9.1 |
| Each risk mitigated architecturally and measured | §5 | Section 9.2; governance in Section 6 |
| Peer review becomes an object of measurement | §6 | Section 5.3 (measured quantities); Section 9.1 (field-level quantities) |

---

## References

Works checked from the runs' "(to verify)" flags are referenced in full in the table of Section 4.11 and are not repeated here, except where this appendix cites them in its own text.

Academy of Management. (n.d.). AOM artificial intelligence (AI) policy: AI policy for reviewers. https://www.aom.org/publications/journals/publishing-with-aom/aom-artificial-intelligence-policy/. Retrieved 27 October 2026.

Alvesson, M., & Sandberg, J. (2011). Generating research questions through problematization. *Academy of Management Review*, 36(2), 247–271.

Ang, S., & Cummings, L. L. (1997). Strategic response to institutional influences on information systems outsourcing. *Organization Science*, 8(3), 235–256.

Brandom, R. B. (1994). *Making It Explicit: Reasoning, Representing, and Discursive Commitment*. Harvard University Press.

Brandom, R. B. (2000). *Articulating Reasons: An Introduction to Inferentialism*. Harvard University Press.

Cohen, J. (1960). A coefficient of agreement for nominal scales. *Educational and Psychological Measurement*, 20(1), 37–46.

Davis, M. S. (1971). That's interesting! Towards a phenomenology of sociology and a sociology of phenomenology. *Philosophy of the Social Sciences*, 1(4), 309–344.

Elsevier. (n.d.). The use of generative AI and AI-assisted technologies in the review process. Elsevier policy for reviewers. Retrieved 23 October 2026.

Flesch, R. (1948). A new readability yardstick. *Journal of Applied Psychology*, 32(3), 221–233.

Gartenberg, C., Hasan, S., Murray, A., & Pierce, L. (2026). More versus better: Artificial intelligence, incentives, and the emerging crisis in peer review. *Organization Science*, 37(3), 795–812. https://doi.org/10.1287/orsc.2026.ed.v37.n3

Holm, S. (1979). A simple sequentially rejective multiple test procedure. *Scandinavian Journal of Statistics*, 6(2), 65–70.

INFORMS. (n.d.). Policy on the use of generative AI (journal guidelines for authors and the review team; e.g., *Service Science*). Retrieved 23 October 2026.

Lakatos, I. (1970). Falsification and the methodology of scientific research programmes. In I. Lakatos & A. Musgrave (Eds.), *Criticism and the Growth of Knowledge* (pp. 91–196). Cambridge University Press.

Lakens, D. (2017). Equivalence tests: A practical primer for t tests, correlations, and meta-analyses. *Social Psychological and Personality Science*, 8(4), 355–362.

Loh, L., & Venkatraman, N. (1992). Diffusion of information technology outsourcing: Influence sources and the Kodak effect. *Information Systems Research*, 3(4), 334–358.

National Institutes of Health. (2023). *The use of generative artificial intelligence technologies is prohibited for the NIH peer review process* (Notice NOT-OD-23-149, 23 June 2023).

Price, H. (2011). *Naturalism Without Mirrors*. Oxford University Press.

Price, H. (with Blackburn, S., Brandom, R., Horwich, P., & Williams, M.) (2013). *Expressivism, Pragmatism and Representationalism*. Cambridge University Press.

Roberts, P. W., & Greenwood, R. (1997). Integrating transaction cost and institutional theories: Toward a constrained-efficiency framework for understanding organizational design adoption. *Academy of Management Review*, 22(2), 346–373.

Schuirmann, D. J. (1987). A comparison of the two one-sided tests procedure and the power approach for assessing the equivalence of average bioavailability. *Journal of Pharmacokinetics and Biopharmaceutics*, 15(6), 657–680.

Sellars, W. (1953). Inference and meaning. *Mind*, 62(247), 313–338.

Toulmin, S. E. (1958). *The Uses of Argument*. Cambridge University Press.

Williamson, O. E. (1991). Comparative economic organization: The analysis of discrete structural alternatives. *Administrative Science Quarterly*, 36(2), 269–296.

*Project Lakatos components.* The routine agents, cognitive operators, discourse grammar and scholarly-role agents (L1 to L17) are those of the Project Lakatos outline (July 2026), whose Tables 1 to 4 are reproduced in Annex D and in `lakatos/LAKATOS_TABLES_1-4.md`.

---

## Annex A. Schema (draft v0.1) and JSON-LD context

*Status: draft v0.1, 23 October 2026; not yet implemented. Generated file: `schema/review-objects.v0.schema.json` (JSON Schema draft 2020-12). Every event in `runs/provenance_events.json` validates against `ProvenanceEvent`.*

### A.1 `schema/review-objects.v0.schema.json`

```json
{
 "$schema": "https://json-schema.org/draft/2020-12/schema",
 "$id": "https://reviewership.lakatos.example/schema/review-objects.v0.schema.json",
 "title": "Reviewership review objects (DRAFT v0.1)",
 "description": "Draft v0.1, 23 October 2026. Objects for the reviewing perspective, standards specification, scoreboard, simulated review, panel synthesis, probes and checks, consistency report, provenance events and consent records. Not yet implemented; used as the output format of the worked runs.",
 "$defs": {
  "Id": {
   "type": "string",
   "pattern": "^[A-Za-z][A-Za-z0-9_-]*:[A-Za-z0-9_.:-]+$"
  },
  "Locus": {
   "type": "string",
   "description": "Section, equation, table cell or short quotation in the manuscript"
  },
  "DimensionSetting": {
   "type": "object",
   "required": [
    "weight",
    "parameters"
   ],
   "properties": {
    "weight": {
     "type": "number",
     "minimum": 0,
     "maximum": 1
    },
    "parameters": {
     "type": "object",
     "description": "Parameter code (e.g. ONT.3) to value: a string, an array of strings, or an object mapping options to preferred/admissible/suspect",
     "propertyNames": {
      "pattern": "^(ONT|EPI|INF|TEC|PRA)\\.[1-9]$"
     }
    }
   }
  },
  "Standard": {
   "type": "object",
   "required": [
    "@id",
    "dimension",
    "statement",
    "priority"
   ],
   "properties": {
    "@id": {
     "type": "string",
     "pattern": "^[A-Za-z][A-Za-z0-9_-]*:[A-Za-z0-9_.:-]+$"
    },
    "dimension": {
     "enum": [
      "ONT",
      "EPI",
      "INF",
      "TEC",
      "PRA"
     ]
    },
    "parameter": {
     "type": "string"
    },
    "statement": {
     "type": "string"
    },
    "priority": {
     "enum": [
      "must",
      "should",
      "could"
     ]
    },
    "origin": {
     "enum": [
      "reviewer",
      "suggested-accepted",
      "suggested-rewritten",
      "configured"
     ]
    },
    "reason": {
     "type": "string"
    }
   }
  },
  "ReviewingPerspective": {
   "type": "object",
   "required": [
    "@id",
    "@type",
    "label",
    "owner",
    "dimensions"
   ],
   "properties": {
    "@id": {
     "type": "string",
     "pattern": "^[A-Za-z][A-Za-z0-9_-]*:[A-Za-z0-9_.:-]+$"
    },
    "@type": {
     "const": "ReviewingPerspective"
    },
    "label": {
     "type": "string"
    },
    "owner": {
     "type": "object",
     "required": [
      "kind"
     ],
     "properties": {
      "kind": {
       "enum": [
        "human",
        "simulated",
        "stand-in"
       ]
      },
      "name": {
       "type": "string"
      }
     }
    },
    "dimensions": {
     "type": "object",
     "required": [
      "ONT",
      "EPI",
      "INF",
      "TEC",
      "PRA"
     ],
     "properties": {
      "ONT": {
       "$ref": "#/$defs/DimensionSetting"
      },
      "EPI": {
       "$ref": "#/$defs/DimensionSetting"
      },
      "INF": {
       "$ref": "#/$defs/DimensionSetting"
      },
      "TEC": {
       "$ref": "#/$defs/DimensionSetting"
      },
      "PRA": {
       "$ref": "#/$defs/DimensionSetting"
      }
     },
     "additionalProperties": false
    },
    "materialInferences": {
     "type": "object",
     "properties": {
      "endorsed": {
       "type": "array",
       "items": {
        "type": "string"
       }
      },
      "rejected": {
       "type": "array",
       "items": {
        "type": "string"
       }
      }
     }
    },
    "standards": {
     "type": "array",
     "items": {
      "$ref": "#/$defs/Standard"
     }
    },
    "corpus": {
     "type": "array",
     "items": {
      "type": "string"
     }
    },
    "relationToFocal": {
     "enum": [
      "focal",
      "resembling",
      "differing"
     ]
    }
   }
  },
  "EditorBrief": {
   "type": "object",
   "required": [
    "@id",
    "@type",
    "manuscript",
    "needs"
   ],
   "properties": {
    "@id": {
     "type": "string",
     "pattern": "^[A-Za-z][A-Za-z0-9_-]*:[A-Za-z0-9_.:-]+$"
    },
    "@type": {
     "const": "EditorBrief"
    },
    "manuscript": {
     "type": "string",
     "pattern": "^[A-Za-z][A-Za-z0-9_-]*:[A-Za-z0-9_.:-]+$"
    },
    "needs": {
     "type": "array",
     "items": {
      "type": "string"
     }
    },
    "concerns": {
     "type": "array",
     "items": {
      "type": "string"
     }
    },
    "audience": {
     "type": "string"
    },
    "round": {
     "type": "string"
    }
   }
  },
  "Tension": {
   "type": "object",
   "required": [
    "between"
   ],
   "properties": {
    "between": {
     "type": "array",
     "items": {
      "type": "string",
      "pattern": "^[A-Za-z][A-Za-z0-9_-]*:[A-Za-z0-9_.:-]+$"
     }
    },
    "ranking": {
     "type": "array",
     "items": {
      "type": "string",
      "pattern": "^[A-Za-z][A-Za-z0-9_-]*:[A-Za-z0-9_.:-]+$"
     }
    },
    "note": {
     "type": "string"
    }
   }
  },
  "StandardsSpecification": {
   "type": "object",
   "required": [
    "@id",
    "@type",
    "reviewer",
    "perspective",
    "editorBrief"
   ],
   "properties": {
    "@id": {
     "type": "string",
     "pattern": "^[A-Za-z][A-Za-z0-9_-]*:[A-Za-z0-9_.:-]+$"
    },
    "@type": {
     "const": "StandardsSpecification"
    },
    "reviewer": {
     "type": "string"
    },
    "perspective": {
     "$ref": "#/$defs/ReviewingPerspective"
    },
    "editorBrief": {
     "oneOf": [
      {
       "type": "string",
       "pattern": "^[A-Za-z][A-Za-z0-9_-]*:[A-Za-z0-9_.:-]+$"
      },
      {
       "$ref": "#/$defs/EditorBrief"
      }
     ]
    },
    "tensions": {
     "type": "array",
     "items": {
      "$ref": "#/$defs/Tension"
     }
    },
    "isReview": {
     "const": false,
     "description": "A standards specification is never a review of the manuscript"
    }
   }
  },
  "ManuscriptRef": {
   "type": "object",
   "required": [
    "@id",
    "@type",
    "sha256"
   ],
   "properties": {
    "@id": {
     "type": "string",
     "pattern": "^[A-Za-z][A-Za-z0-9_-]*:[A-Za-z0-9_.:-]+$"
    },
    "@type": {
     "const": "ManuscriptRef"
    },
    "title": {
     "type": "string"
    },
    "sha256": {
     "type": "string",
     "pattern": "^[0-9a-f]{64}$"
    },
    "version": {
     "type": "string"
    }
   },
   "description": "The manuscript is registered by hash; its text is held only in the gateway's manuscript store"
  },
  "Commitment": {
   "type": "object",
   "required": [
    "@id",
    "statement",
    "kind",
    "entitlement"
   ],
   "properties": {
    "@id": {
     "type": "string",
     "pattern": "^[A-Za-z][A-Za-z0-9_-]*:[A-Za-z0-9_.:-]+$"
    },
    "statement": {
     "type": "string"
    },
    "locus": {
     "$ref": "#/$defs/Locus"
    },
    "kind": {
     "enum": [
      "avowed",
      "consequential"
     ]
    },
    "via": {
     "type": "string",
     "description": "For consequential commitments: the inference used (e.g. MI6, or 'Prop. 1 and \u00a72.4')"
    },
    "entitlement": {
     "enum": [
      "argued",
      "evidenced",
      "deferred",
      "default",
      "challenged",
      "unentitled"
     ]
    },
    "entitlementBasis": {
     "type": "string"
    }
   }
  },
  "Incompatibility": {
   "type": "object",
   "required": [
    "@id",
    "between",
    "reason"
   ],
   "properties": {
    "@id": {
     "type": "string",
     "pattern": "^[A-Za-z][A-Za-z0-9_-]*:[A-Za-z0-9_.:-]+$"
    },
    "between": {
     "type": "array",
     "items": {
      "type": "string",
      "pattern": "^[A-Za-z][A-Za-z0-9_-]*:[A-Za-z0-9_.:-]+$"
     },
     "minItems": 2,
     "maxItems": 2
    },
    "reason": {
     "type": "string"
    }
   }
  },
  "Challenge": {
   "type": "object",
   "required": [
    "@id",
    "target",
    "question"
   ],
   "properties": {
    "@id": {
     "type": "string",
     "pattern": "^[A-Za-z][A-Za-z0-9_-]*:[A-Za-z0-9_.:-]+$"
    },
    "target": {
     "type": "string",
     "pattern": "^[A-Za-z][A-Za-z0-9_-]*:[A-Za-z0-9_.:-]+$"
    },
    "question": {
     "type": "string"
    }
   }
  },
  "Scoreboard": {
   "type": "object",
   "required": [
    "@id",
    "@type",
    "manuscript",
    "scorekeeper",
    "commitments"
   ],
   "properties": {
    "@id": {
     "type": "string",
     "pattern": "^[A-Za-z][A-Za-z0-9_-]*:[A-Za-z0-9_.:-]+$"
    },
    "@type": {
     "const": "Scoreboard"
    },
    "manuscript": {
     "type": "string",
     "pattern": "^[A-Za-z][A-Za-z0-9_-]*:[A-Za-z0-9_.:-]+$"
    },
    "scorekeeper": {
     "type": "string",
     "pattern": "^[A-Za-z][A-Za-z0-9_-]*:[A-Za-z0-9_.:-]+$"
    },
    "commitments": {
     "type": "array",
     "items": {
      "$ref": "#/$defs/Commitment"
     }
    },
    "incompatibilities": {
     "type": "array",
     "items": {
      "$ref": "#/$defs/Incompatibility"
     }
    },
    "challenges": {
     "type": "array",
     "items": {
      "$ref": "#/$defs/Challenge"
     }
    }
   }
  },
  "ClaimedContribution": {
   "type": "object",
   "required": [
    "@id",
    "statement"
   ],
   "properties": {
    "@id": {
     "type": "string",
     "pattern": "^[A-Za-z][A-Za-z0-9_-]*:[A-Za-z0-9_.:-]+$"
    },
    "statement": {
     "type": "string"
    },
    "locus": {
     "$ref": "#/$defs/Locus"
    }
   }
  },
  "Finding": {
   "type": "object",
   "required": [
    "@id",
    "locus",
    "problem",
    "severity",
    "status"
   ],
   "properties": {
    "@id": {
     "type": "string",
     "pattern": "^[A-Za-z][A-Za-z0-9_-]*:[A-Za-z0-9_.:-]+$"
    },
    "dimension": {
     "enum": [
      "ONT",
      "EPI",
      "INF",
      "TEC",
      "PRA"
     ]
    },
    "probeType": {
     "enum": [
      "P-DER",
      "P-ID",
      "P-NUM",
      "P-MEAS",
      "P-INF",
      "P-LIT"
     ]
    },
    "locus": {
     "$ref": "#/$defs/Locus"
    },
    "commitment": {
     "type": "string"
    },
    "problem": {
     "type": "string"
    },
    "severity": {
     "enum": [
      "fatal",
      "damaging",
      "fixable",
      "minor"
     ]
    },
    "repair": {
     "type": "string"
    },
    "status": {
     "enum": [
      "asserted",
      "demonstrated",
      "refuted-by-check",
      "inconclusive"
     ]
    },
    "check": {
     "type": "string",
     "pattern": "^[A-Za-z][A-Za-z0-9_-]*:[A-Za-z0-9_.:-]+$"
    }
   }
  },
  "ContributionVerdict": {
   "type": "object",
   "required": [
    "contribution",
    "verdict"
   ],
   "properties": {
    "contribution": {
     "type": "string",
     "pattern": "^[A-Za-z][A-Za-z0-9_-]*:[A-Za-z0-9_.:-]+$"
    },
    "verdict": {
     "enum": [
      "survives",
      "qualified",
      "fails"
     ]
    },
    "qualifiedForm": {
     "type": "string"
    },
    "restatement": {
     "type": "string"
    }
   }
  },
  "SimulatedReview": {
   "type": "object",
   "required": [
    "@id",
    "@type",
    "perspective",
    "contributions",
    "verdicts",
    "findings",
    "recommendation"
   ],
   "properties": {
    "@id": {
     "type": "string",
     "pattern": "^[A-Za-z][A-Za-z0-9_-]*:[A-Za-z0-9_.:-]+$"
    },
    "@type": {
     "const": "SimulatedReview"
    },
    "perspective": {
     "type": "string",
     "pattern": "^[A-Za-z][A-Za-z0-9_-]*:[A-Za-z0-9_.:-]+$"
    },
    "relationToFocal": {
     "enum": [
      "resembling",
      "differing"
     ]
    },
    "contributions": {
     "type": "array",
     "items": {
      "$ref": "#/$defs/ClaimedContribution"
     }
    },
    "verdicts": {
     "type": "array",
     "items": {
      "$ref": "#/$defs/ContributionVerdict"
     }
    },
    "findings": {
     "type": "array",
     "items": {
      "$ref": "#/$defs/Finding"
     }
    },
    "rival": {
     "type": "string"
    },
    "discriminatingObservation": {
     "type": "string"
    },
    "mindChangers": {
     "type": "array",
     "items": {
      "type": "string"
     }
    },
    "recommendation": {
     "enum": [
      "accept",
      "minor revision",
      "major revision",
      "reject"
     ]
    },
    "drivers": {
     "type": "array",
     "items": {
      "type": "string"
     }
    },
    "simulated": {
     "const": true
    }
   }
  },
  "Disagreement": {
   "type": "object",
   "required": [
    "between",
    "about",
    "kind"
   ],
   "properties": {
    "between": {
     "type": "array",
     "items": {
      "type": "string",
      "pattern": "^[A-Za-z][A-Za-z0-9_-]*:[A-Za-z0-9_.:-]+$"
     }
    },
    "about": {
     "type": "string"
    },
    "kind": {
     "enum": [
      "fault-line",
      "resolvable",
      "idiosyncratic"
     ]
    },
    "parameters": {
     "type": "array",
     "items": {
      "type": "string"
     }
    },
    "settleBy": {
     "type": "string"
    }
   }
  },
  "SurvivalRow": {
   "type": "object",
   "required": [
    "contribution",
    "verdicts",
    "score"
   ],
   "properties": {
    "contribution": {
     "type": "string",
     "pattern": "^[A-Za-z][A-Za-z0-9_-]*:[A-Za-z0-9_.:-]+$"
    },
    "verdicts": {
     "type": "object"
    },
    "score": {
     "type": "number",
     "minimum": 0,
     "maximum": 1
    },
    "robust": {
     "type": "boolean"
    },
    "lensDependent": {
     "type": "boolean"
    }
   }
  },
  "PanelSynthesis": {
   "type": "object",
   "required": [
    "@id",
    "@type",
    "reviews",
    "survival",
    "disagreements"
   ],
   "properties": {
    "@id": {
     "type": "string",
     "pattern": "^[A-Za-z][A-Za-z0-9_-]*:[A-Za-z0-9_.:-]+$"
    },
    "@type": {
     "const": "PanelSynthesis"
    },
    "reviews": {
     "type": "array",
     "items": {
      "type": "string",
      "pattern": "^[A-Za-z][A-Za-z0-9_-]*:[A-Za-z0-9_.:-]+$"
     }
    },
    "survival": {
     "type": "array",
     "items": {
      "$ref": "#/$defs/SurvivalRow"
     }
    },
    "agreements": {
     "type": "array",
     "items": {
      "type": "object"
     }
    },
    "disagreements": {
     "type": "array",
     "items": {
      "$ref": "#/$defs/Disagreement"
     }
    },
    "recommendationSpread": {
     "type": "object"
    }
   }
  },
  "CheckSpec": {
   "type": "object",
   "required": [
    "@id",
    "@type",
    "finding",
    "language",
    "code"
   ],
   "properties": {
    "@id": {
     "type": "string",
     "pattern": "^[A-Za-z][A-Za-z0-9_-]*:[A-Za-z0-9_.:-]+$"
    },
    "@type": {
     "const": "CheckSpec"
    },
    "finding": {
     "type": "string",
     "pattern": "^[A-Za-z][A-Za-z0-9_-]*:[A-Za-z0-9_.:-]+$"
    },
    "language": {
     "const": "python"
    },
    "code": {
     "type": "string"
    },
    "premises": {
     "type": "array",
     "items": {
      "$ref": "#/$defs/Locus"
     }
    }
   }
  },
  "CheckResult": {
   "type": "object",
   "required": [
    "@id",
    "@type",
    "check",
    "ranAt",
    "stdout",
    "verdict"
   ],
   "properties": {
    "@id": {
     "type": "string",
     "pattern": "^[A-Za-z][A-Za-z0-9_-]*:[A-Za-z0-9_.:-]+$"
    },
    "@type": {
     "const": "CheckResult"
    },
    "check": {
     "type": "string",
     "pattern": "^[A-Za-z][A-Za-z0-9_-]*:[A-Za-z0-9_.:-]+$"
    },
    "harness": {
     "type": "string"
    },
    "ranAt": {
     "type": "string",
     "format": "date-time"
    },
    "stdout": {
     "type": "string"
    },
    "verdict": {
     "enum": [
      "demonstrated",
      "refuted-by-check",
      "inconclusive"
     ]
    }
   }
  },
  "ConsistencyReport": {
   "type": "object",
   "required": [
    "@id",
    "@type",
    "specification",
    "review",
    "applied"
   ],
   "properties": {
    "@id": {
     "type": "string",
     "pattern": "^[A-Za-z][A-Za-z0-9_-]*:[A-Za-z0-9_.:-]+$"
    },
    "@type": {
     "const": "ConsistencyReport"
    },
    "specification": {
     "type": "string",
     "pattern": "^[A-Za-z][A-Za-z0-9_-]*:[A-Za-z0-9_.:-]+$"
    },
    "review": {
     "type": "string",
     "pattern": "^[A-Za-z][A-Za-z0-9_-]*:[A-Za-z0-9_.:-]+$"
    },
    "applied": {
     "type": "array",
     "items": {
      "type": "object",
      "required": [
       "standard",
       "status"
      ],
      "properties": {
       "standard": {
        "type": "string",
        "pattern": "^[A-Za-z][A-Za-z0-9_-]*:[A-Za-z0-9_.:-]+$"
       },
       "status": {
        "enum": [
         "applied",
         "partial",
         "not-applied"
        ]
       },
       "locus": {
        "type": "string"
       }
      }
     }
    },
    "silentSkips": {
     "type": "array",
     "items": {
      "type": "string",
      "pattern": "^[A-Za-z][A-Za-z0-9_-]*:[A-Za-z0-9_.:-]+$"
     }
    },
    "undeclared": {
     "type": "array",
     "items": {
      "type": "string"
     }
    },
    "inconsistencies": {
     "type": "array",
     "items": {
      "type": "string"
     }
    },
    "briefAnswered": {
     "type": "string"
    }
   }
  },
  "Actor": {
   "type": "object",
   "required": [
    "kind",
    "name"
   ],
   "properties": {
    "kind": {
     "enum": [
      "human",
      "agent",
      "harness",
      "stand-in",
      "orchestrator"
     ]
    },
    "name": {
     "type": "string"
    },
    "model": {
     "type": "string"
    },
    "gatewayRoute": {
     "type": "string"
    },
    "instructionSetVersion": {
     "type": "string"
    }
   }
  },
  "ProvenanceEvent": {
   "type": "object",
   "required": [
    "@id",
    "@type",
    "timestamp",
    "timestampKind",
    "actor",
    "action",
    "prevHash",
    "hash"
   ],
   "properties": {
    "@id": {
     "type": "string",
     "pattern": "^[A-Za-z][A-Za-z0-9_-]*:[A-Za-z0-9_.:-]+$"
    },
    "@type": {
     "const": "ProvenanceEvent"
    },
    "timestamp": {
     "type": "string",
     "format": "date-time"
    },
    "timestampKind": {
     "enum": [
      "actual",
      "reconstructed"
     ]
    },
    "actor": {
     "$ref": "#/$defs/Actor"
    },
    "action": {
     "enum": [
      "ingest",
      "seal",
      "elicit",
      "specify",
      "simulate",
      "synthesize",
      "probe",
      "check",
      "consistency-check",
      "draft",
      "accept",
      "reject",
      "modify",
      "include",
      "sign",
      "score",
      "annotate",
      "delete"
     ]
    },
    "inputs": {
     "type": "array",
     "items": {
      "type": "string",
      "pattern": "^[A-Za-z][A-Za-z0-9_-]*:[A-Za-z0-9_.:-]+$"
     }
    },
    "outputs": {
     "type": "array",
     "items": {
      "type": "string",
      "pattern": "^[A-Za-z][A-Za-z0-9_-]*:[A-Za-z0-9_.:-]+$"
     }
    },
    "respondsTo": {
     "type": "string",
     "pattern": "^[A-Za-z][A-Za-z0-9_-]*:[A-Za-z0-9_.:-]+$"
    },
    "rationale": {
     "type": "string"
    },
    "contentHash": {
     "type": "string",
     "pattern": "^[0-9a-f]{64}$"
    },
    "prevHash": {
     "type": "string",
     "pattern": "^[0-9a-f]{64}$"
    },
    "hash": {
     "type": "string",
     "pattern": "^[0-9a-f]{64}$"
    }
   }
  },
  "ConsentRecord": {
   "type": "object",
   "required": [
    "@id",
    "@type",
    "party",
    "role",
    "scope",
    "grantedAt",
    "instrumentVersion"
   ],
   "properties": {
    "@id": {
     "type": "string",
     "pattern": "^[A-Za-z][A-Za-z0-9_-]*:[A-Za-z0-9_.:-]+$"
    },
    "@type": {
     "const": "ConsentRecord"
    },
    "party": {
     "type": "string",
     "description": "Pseudonymous id"
    },
    "role": {
     "enum": [
      "editor",
      "author",
      "reviewer"
     ]
    },
    "scope": {
     "type": "array",
     "items": {
      "enum": [
       "workbench-use",
       "ai-assisted-track",
       "pairing",
       "research-use",
       "blind-evaluation",
       "deidentified-release",
       "base-model-study"
      ]
     }
    },
    "grantedAt": {
     "type": "string",
     "format": "date-time"
    },
    "withdrawnAt": {
     "type": [
      "string",
      "null"
     ],
     "format": "date-time"
    },
    "instrumentVersion": {
     "type": "string"
    }
   }
  }
 },
 "oneOf": [
  {
   "$ref": "#/$defs/ReviewingPerspective"
  },
  {
   "$ref": "#/$defs/StandardsSpecification"
  },
  {
   "$ref": "#/$defs/EditorBrief"
  },
  {
   "$ref": "#/$defs/ManuscriptRef"
  },
  {
   "$ref": "#/$defs/Scoreboard"
  },
  {
   "$ref": "#/$defs/SimulatedReview"
  },
  {
   "$ref": "#/$defs/PanelSynthesis"
  },
  {
   "$ref": "#/$defs/CheckSpec"
  },
  {
   "$ref": "#/$defs/CheckResult"
  },
  {
   "$ref": "#/$defs/ConsistencyReport"
  },
  {
   "$ref": "#/$defs/ProvenanceEvent"
  },
  {
   "$ref": "#/$defs/ConsentRecord"
  }
 ]
}
```

### A.2 `schema/context.v0.jsonld`

```json
{
 "@context": {
  "@version": 1.1,
  "@vocab": "https://reviewership.lakatos.example/vocab/v0#",
  "rvw": "https://reviewership.lakatos.example/vocab/v0#",
  "prov": "http://www.w3.org/ns/prov#",
  "xsd": "http://www.w3.org/2001/XMLSchema#",
  "perspective": {
   "@id": "rvw:perspective",
   "@type": "@id"
  },
  "scorekeeper": {
   "@id": "rvw:scorekeeper",
   "@type": "@id"
  },
  "manuscript": {
   "@id": "rvw:manuscript",
   "@type": "@id"
  },
  "between": {
   "@id": "rvw:between",
   "@type": "@id",
   "@container": "@set"
  },
  "target": {
   "@id": "rvw:target",
   "@type": "@id"
  },
  "contribution": {
   "@id": "rvw:contribution",
   "@type": "@id"
  },
  "reviews": {
   "@id": "rvw:reviews",
   "@type": "@id",
   "@container": "@set"
  },
  "finding": {
   "@id": "rvw:finding",
   "@type": "@id"
  },
  "check": {
   "@id": "rvw:check",
   "@type": "@id"
  },
  "specification": {
   "@id": "rvw:specification",
   "@type": "@id"
  },
  "review": {
   "@id": "rvw:review",
   "@type": "@id"
  },
  "standard": {
   "@id": "rvw:standard",
   "@type": "@id"
  },
  "silentSkips": {
   "@id": "rvw:silentSkip",
   "@type": "@id",
   "@container": "@set"
  },
  "inputs": {
   "@id": "prov:used",
   "@type": "@id",
   "@container": "@set"
  },
  "outputs": {
   "@id": "prov:generated",
   "@type": "@id",
   "@container": "@set"
  },
  "respondsTo": {
   "@id": "prov:wasInformedBy",
   "@type": "@id"
  },
  "timestamp": {
   "@id": "prov:atTime",
   "@type": "xsd:dateTime"
  },
  "ranAt": {
   "@id": "prov:atTime",
   "@type": "xsd:dateTime"
  },
  "actor": {
   "@id": "prov:wasAssociatedWith"
  }
 }
}
```

---

## Annex B. The test manuscript and the sealed defect key

*Synthetic; written for the demonstration. No data exist. SHA-256 hashes, recorded before any run (`case/HASHES.txt`):*

```
970e0574092c8e9dd0c97200980c804f0431153f256b0e9f34260b405034809d  SEALED_DEFECT_KEY.md
a8ab4709ef157d6e5467077a6e54eb4f0ee9f35bac2b241be91fe80a950852d0  TEST_MANUSCRIPT.md
```

### B.1 The test manuscript (`case/TEST_MANUSCRIPT.md`)

#### Modularity, Not Mimicry: Interoperability Standards and the Diffusion of IT Outsourcing in U.S. Hospitals

*Manuscript submitted for review. Author names removed.*

##### Abstract

Why did outsourcing of information-technology (IT) functions spread so rapidly through U.S. hospitals after 2009? Institutional accounts attribute the diffusion to mimetic imitation of peers under uncertainty. We develop a transaction-cost model in which interoperability standards make IT functions modular, lowering the effective asset specificity of the hospital–vendor relationship and widening the range of functions that can be outsourced without exposure to hold-up. The model predicts that modularity increases outsourcing, and that this effect is stronger where environmental uncertainty is high. Using a balanced panel of 412 general acute-care hospitals observed from 2009 to 2019, we find that a hospital's modularity, measured as the share of its clinical systems connected through certified standard interfaces, strongly predicts the share of its IT spending that is outsourced. Once modularity is accounted for, prior adoption by peer hospitals no longer predicts outsourcing. The results rule out mimetic isomorphism as a driver of IT outsourcing in this setting and show that a sourcing practice often read as institutional fashion is, on closer inspection, economizing. To our knowledge, this is the first study to adjudicate directly between transaction-cost and institutional explanations of IT outsourcing.

##### 1. Introduction

Between 2009 and 2019 the share of U.S. hospital IT spending paid to outside vendors roughly doubled. Hospitals that had run their own data centres, help desks and clinical-application teams handed these functions to specialized providers. The pace and breadth of the change invite an institutional reading. Organizations facing technological uncertainty imitate peers they regard as successful or legitimate (DiMaggio & Powell, 1983), and practices diffuse through organizational fields long after their technical merits have been established, or in their absence (Tolbert & Zucker, 1983). Hospitals are a canonical setting for such arguments: they are embedded in dense professional and regulatory fields, and their adoption of managerial practices has been shown to reflect conformity as well as customization (Westphal, Gulati & Shortell, 1997).

We offer a different account. Transaction-cost economics holds that activities are kept inside the firm when the assets they require are specific to the relationship, because specificity exposes the parties to hold-up and markets govern such exposure poorly (Williamson, 1975, 1985). Our argument is that interoperability standards changed the specificity of hospital IT. Before standardization, a vendor running a hospital's laboratory-information system had to build and maintain bespoke interfaces to the hospital's other clinical systems; that investment was worth little outside the relationship, and the hospital, once dependent on it, was exposed. Certified standard interfaces made IT functions *modular* in the sense of Baldwin and Clark (2000): components that interact through published rules rather than through idiosyncratic knowledge. Modularity lowers the effective specificity of the relationship, and with it the hazard that kept functions in-house (Langlois, 2002; Sanchez & Mahoney, 1996).

We make three contributions. First, we formalize the link between modularity and the make-or-buy decision in a simple transaction-cost model, deriving two propositions: modularity widens the range of outsourced functions, and the effect is amplified by environmental uncertainty. Second, we test these propositions against an institutional rival using a decade-long panel of hospitals. Third, we show that once modularity is measured, the apparent peer effects that have motivated institutional accounts disappear. To our knowledge, this is the first study to adjudicate directly between transaction-cost and institutional explanations of IT outsourcing.

##### 2. Theory and model

###### 2.1 Setting

A hospital performs a set of IT functions (for example, infrastructure hosting, help-desk support, revenue-cycle systems, laboratory and pharmacy applications). Each function can be performed in-house ("make") or by a specialized vendor ("buy"). Functions differ in the specificity of the assets they require, which we index by $k \in [0,1]$: a function with high $k$ requires investments (interfaces, configuration, tacit knowledge of the hospital's workflows) that are worth little outside the relationship.

###### 2.2 Costs of make and buy

Vendors enjoy production-cost advantages from scale and specialization, which we denote $s > 0$. Buying a function, however, exposes the hospital to hold-up in proportion to the specificity of the relationship. Let $m \in [0,1)$ denote the hospital's degree of modularity, the extent to which its systems interact through certified standard interfaces. Modularity reduces the relationship-specific component of a function's assets, so that the effective specificity of a function with nominal specificity $k$ is $k(1-m)$.

Environmental uncertainty $u \geq 0$ raises the costs of both governance modes. Under market governance, uncertainty increases the frequency of unanticipated adaptations, each of which is an occasion for hold-up; we write the hazard rate per unit of effective specificity as $H(u) = h_0 + h_1 u$, with $h_0, h_1 > 0$. Under hierarchy, uncertainty raises the bureaucratic costs of in-house adaptation, which we write as $G(u) = g_0 + g_1 u$, with $g_0, g_1 > 0$. Following Williamson (1991), we assume that markets are less able than hierarchies to adapt to disturbances, so that hold-up hazards respond more strongly to uncertainty than in-house adaptation costs do, in proportional terms:

**Assumption A3.** $\dfrac{h_1}{h_0} > \dfrac{g_1}{s + g_0}$.

Normalizing the common production cost to $p$, the cost of buying a function is $C_B = p - s + H(u)\,k(1-m)$ and the cost of making it is $C_M = p + G(u)$.

###### 2.3 Propositions

The hospital buys a function if and only if $C_B < C_M$, that is, if
$$ k < k^*(m,u) \equiv \frac{s + G(u)}{H(u)\,(1-m)}. $$
Functions with specificity below the threshold $k^*$ are outsourced; those above it are kept in-house.

**Proposition 1 (modularity widens outsourcing).** The outsourcing threshold rises with modularity: $\partial k^*/\partial m > 0$.

**Proposition 2 (uncertainty amplifies the modularity effect).** The effect of modularity on the outsourcing threshold is increasing in environmental uncertainty: $\partial^2 k^*/\partial m\,\partial u > 0$.

Proofs are in the Appendix. Proposition 2 has an intuitive reading: where uncertainty is high, the hold-up hazards that modularity neutralizes are most costly, so the value of modularity is greatest.

###### 2.4 Hypotheses

Let $\Phi$ denote the share of a hospital's IT functions, weighted by spending, that are outsourced. Since functions with $k<k^*$ are outsourced, Proposition 1 implies that hospitals with higher modularity outsource a larger share of their IT spending, and Proposition 2 implies that this association is stronger where uncertainty is high.

**H1.** A hospital's modularity is positively associated with the share of its IT spending that is outsourced.

**H2.** The positive association between modularity and outsourcing is stronger when environmental uncertainty is high.

The institutional account predicts instead that hospitals outsource because their peers do. Under uncertainty about the merits of a practice, organizations model themselves on others in their field (DiMaggio & Powell, 1983). We therefore state the rival hypothesis:

**H3 (institutional rival).** A hospital's outsourcing share is positively associated with the prior outsourcing of peer hospitals.

If outsourcing reflects economizing, H1 should hold and the association predicted by H3 should disappear once modularity is controlled; if it reflects mimicry, peer outsourcing should predict outsourcing over and above modularity.

##### 3. Data and methods

###### 3.1 Sample

Our sample is a balanced panel of 412 U.S. general acute-care hospitals observed annually from 2009 to 2019. Data on IT spending and sourcing come from an annual survey of hospital chief information officers (CIOs), the Hospital IT Sourcing Survey, linked to hospital characteristics from administrative sources. Hospitals were included if they responded to the survey in every year, yielding 4,712 hospital-year observations.

###### 3.2 Measures

*Outsourcing share* ($\Phi_{it}$) is the share of hospital $i$'s IT operating spending in year $t$ paid to external vendors for the performance of IT functions (excluding hardware and software licence purchases). Mean 0.31, SD 0.17.

*Modularity* ($m_{it}$) is the share of the hospital's clinical information systems that exchange data with its other systems through interfaces certified to a published standard, as reported by the CIO. Mean 0.46, SD 0.24.

*Environmental uncertainty* ($u_{it}$) is the coefficient of variation of the hospital's quarterly inpatient admissions over the preceding three years, standardized to mean zero and unit variance.

*Peer outsourcing* is the mean outsourcing share of all other sample hospitals in the same state in year $t-1$. This captures the prevalence of the practice in the hospital's immediate field, the population to which mimetic isomorphism directs attention.

*Asset specificity* is the CIO's rating, on a seven-point scale, of how costly it would be to transfer the hospital's IT functions to a different provider, averaged over functions and rescaled to $[0,1]$.

*Controls* include beds (log), system membership, teaching status, ownership (for-profit, non-profit, public), operating margin, and case-mix index.

*In-house IT staffing* is the number of full-time-equivalent IT employees per staffed bed (log). Because outsourcing a function transfers its staff to the vendor or eliminates the positions, in-house staffing also tracks the scale of the hospital's internal IT capability.

###### 3.3 Estimation

We estimate linear models of the outsourcing share with hospital and year fixed effects:
$$ \Phi_{it} = \beta_1 m_{it} + \beta_2 u_{it} + \beta_3 (m_{it} \times u_{it}) + \beta_4 \text{Peer}_{s,t-1} + \gamma' X_{it} + \alpha_i + \tau_t + \varepsilon_{it}, $$
with standard errors clustered by hospital. Hospital fixed effects absorb stable differences in capability, culture and governance; year fixed effects absorb national shocks, including the federal incentive programme for electronic health records introduced in 2009. Identification therefore comes from within-hospital changes in modularity over time.

To address the concern that unobserved, time-varying differences in internal IT capability drive both modularity and outsourcing, Model 4 adds in-house IT staffing as a control. If the modularity effect survives this control, it cannot be attributed to capability differences.

##### 4. Results

Table 2 reports the estimates.

**Table 2. Fixed-effects estimates of the IT outsourcing share** (standard errors clustered by hospital in parentheses)

| | Model 1 | Model 2 | Model 3 | Model 4 |
|---|---|---|---|---|
| Peer outsourcing (t−1) | 0.137*** (0.031) | 0.042 (0.038) | 0.039 (0.037) | 0.036 (0.036) |
| Modularity | | 0.112*** (0.024) | 0.118*** (0.025) | 0.097*** (0.023) |
| Environmental uncertainty | | | 0.084*** (0.051) | 0.079 (0.050) |
| Modularity × uncertainty | | | −0.061** (0.019) | −0.058** (0.019) |
| Asset specificity | −0.094*** (0.027) | −0.091*** (0.027) | −0.090*** (0.026) | −0.088*** (0.026) |
| In-house IT staffing (log) | | | | −0.143*** (0.029) |
| Controls | Yes | Yes | Yes | Yes |
| Hospital and year fixed effects | Yes | Yes | Yes | Yes |
| Observations | 4,712 | 4,712 | 4,712 | 4,712 |
| Hospitals | 412 | 412 | 412 | 412 |
| Within R² | 0.08 | 0.13 | 0.14 | 0.19 |

*** p < 0.001; ** p < 0.01; * p < 0.05.

**H1.** Modularity is strongly and positively associated with the outsourcing share in every specification. In Model 2, a one-standard-deviation increase in modularity (0.24) is associated with an increase of 2.7 percentage points in the outsourcing share, about one-sixth of a standard deviation. H1 is supported.

**H3.** Peer outsourcing is positively and significantly associated with the outsourcing share when modularity is omitted (Model 1). Once modularity enters (Model 2), the peer coefficient falls by more than two-thirds and is no longer significant. This pattern is exactly what the transaction-cost account predicts and the institutional account does not: the apparent peer effect reflects the common diffusion of standards across hospitals in the same state, not imitation. H3 is not supported.

**H2.** The interaction between modularity and uncertainty is negative and significant (Model 3), contrary to H2. We return to this result in the discussion.

**Robustness.** The modularity effect survives the addition of in-house IT staffing (Model 4), so it cannot be attributed to differences in internal IT capability. In an event-study specification exploiting the staggered timing of state requirements for certified interfaces (2011 to 2016), estimated by two-way fixed effects with leads and lags of the year in which the hospital's state adopted a requirement, the leads are small and insignificant and outsourcing rises in the years after adoption, consistent with a causal effect of modularity. Results are similar when the outsourcing share is computed over all IT spending including licences, and when the sample is restricted to non-system hospitals.

##### 5. Discussion

Our findings support a transaction-cost account of the diffusion of IT outsourcing among hospitals. Interoperability standards made IT functions modular, reduced the effective specificity of hospital–vendor relationships, and widened the range of functions hospitals could outsource without exposure to hold-up. Once modularity is measured, peer outsourcing no longer predicts a hospital's own outsourcing. These results rule out mimetic isomorphism as a driver of IT outsourcing in this setting. A practice that appears to spread by imitation spreads, on closer inspection, because its economics changed.

The negative interaction between modularity and uncertainty calls for comment. We believe it reflects a feature of the hospital setting that our model abstracts from. When demand is volatile, hospital boards and community stakeholders are especially attentive to the hospital's resilience, and visible in-house IT capacity serves as a signal of that resilience. Under high uncertainty, then, hospitals face legitimacy pressures to retain in-house functions that would otherwise be outsourced, offsetting the economizing effect of modularity. This interpretation is consistent with our theory: the economizing logic operates, but is tempered by the hospital's need to be seen as prepared. Incorporating such signalling considerations into the model is a promising direction for future work.

###### 5.1 Contributions

For transaction-cost theory, we show that the boundaries of the firm respond not only to the attributes of transactions but to the technological standards that shape those attributes. Specificity is not a fixed property of an activity; it is partly a product of interface design, and therefore of standards that firms do not individually control. For institutional theory, our results counsel caution: diffusion patterns that look mimetic may reflect the common adoption of efficiency-enhancing technologies, and researchers should measure the economics of a practice before attributing its spread to imitation. For practice, the results suggest that hospital leaders considering outsourcing should attend first to the modularity of their systems.

###### 5.2 Limitations

Our measures of modularity and specificity rely on CIO reports. The sample is restricted to hospitals that responded in every year, which may over-represent larger and better-resourced hospitals. We study one industry in one country over one decade, and the generalizability of the modularity mechanism to other settings remains to be established.

##### 6. Conclusion

The spread of IT outsourcing through U.S. hospitals has the outward form of an institutional fashion. Its substance is economizing. By making IT functions modular, interoperability standards lowered the specificity that had kept them in-house. Theories of organizational diffusion should take seriously the possibility that what spreads is not a practice but the conditions that make it efficient.

##### Appendix. Proofs

**Proof of Proposition 1.** Differentiating $k^* = \dfrac{s + G(u)}{H(u)(1-m)}$ with respect to $m$ gives
$$ \frac{\partial k^*}{\partial m} = \frac{s + G(u)}{H(u)(1-m)^2} > 0, $$
since $s$, $G(u)$ and $H(u)$ are positive. $\blacksquare$

**Proof of Proposition 2.** Modularity operates on the denominator of $k^*$ only through the factor $(1-m)$, so the cross-partial is determined by how the numerator responds to uncertainty. Differentiating the expression in the proof of Proposition 1 with respect to $u$,
$$ \frac{\partial^2 k^*}{\partial m\,\partial u} = \frac{G'(u)}{H(u)(1-m)^2} = \frac{g_1}{H(u)(1-m)^2} > 0. \qquad \blacksquare $$

##### References

Baldwin, C. Y., & Clark, K. B. (2000). *Design Rules, Volume 1: The Power of Modularity*. MIT Press.

DiMaggio, P. J., & Powell, W. W. (1983). The iron cage revisited: Institutional isomorphism and collective rationality in organizational fields. *American Sociological Review*, 48(2), 147–160.

Langlois, R. N. (2002). Modularity in technology and organization. *Journal of Economic Behavior & Organization*, 49(1), 19–37.

Sanchez, R., & Mahoney, J. T. (1996). Modularity, flexibility, and knowledge management in product and organization design. *Strategic Management Journal*, 17(S2), 63–76.

Tolbert, P. S., & Zucker, L. G. (1983). Institutional sources of change in the formal structure of organizations: The diffusion of civil service reform, 1880–1935. *Administrative Science Quarterly*, 28(1), 22–39.

Westphal, J. D., Gulati, R., & Shortell, S. M. (1997). Customization or conformity? An institutional and network perspective on the content and consequences of TQM adoption. *Administrative Science Quarterly*, 42(2), 366–394.

Williamson, O. E. (1975). *Markets and Hierarchies: Analysis and Antitrust Implications*. Free Press.

Williamson, O. E. (1985). *The Economic Institutions of Capitalism*. Free Press.

Williamson, O. E. (1991). Comparative economic organization: The analysis of discrete structural alternatives. *Administrative Science Quarterly*, 36(2), 269–296.

### B.2 The sealed defect key (`case/SEALED_DEFECT_KEY.md`)

#### Sealed defect key for the test manuscript

*Written on 23 October 2026 together with `TEST_MANUSCRIPT.md`, before any run. Its SHA-256 hash was recorded as the first event of the provenance trace (ev:2) before any agent saw the manuscript. No agent was given this file. It is used only to score runs after the fact.*

The manuscript was written for the demonstration. Its data, results and survey are fictitious; its citations to the published literature are real. Nine defects were seeded, at least one on each of the five dimensions of the reviewing perspective. Everything else in the manuscript was written to be competent, so weaknesses an agent finds that are not on this list are scored separately as *unseeded findings*.

**Recovery rule.** A defect counts as *located* if a run identifies the right locus **and** the right reason (the paraphrase in the "Located if" column, in any words). Naming the locus with a wrong or generic reason counts as *touched*, not located. A defect counts as *demonstrated* if an executable check, run by the harness, establishes it.

| Id | Dimension(s) | Locus | Defect | Located if the run says, in substance | Demonstrable by an executable check? |
|---|---|---|---|---|---|
| SD1 | Technical; inferential | Appendix, proof of Prop. 2; §2.3 | The proof holds $H(u)$ constant when differentiating with respect to $u$. The correct cross-partial is $\big(g_1 h_0 - h_1(s+g_0)\big)/\big(H(u)^2(1-m)^2\big)$, whose sign is ambiguous in general and **negative under the paper's own Assumption A3**. Prop. 2 is reversed under the paper's assumptions. | The derivation of Prop. 2 is wrong because the dependence of $H$ on $u$ is ignored; the sign is ambiguous or negative (full credit if it notes A3 implies negative) | Yes (symbolic differentiation) |
| SD2 | Epistemological; technical | §3.3 Model 4 and the robustness claim in §4 | In-house IT staffing is a *consequence of the outcome* (the paper says outsourcing transfers or eliminates IT positions). Controlling for it conditions on a descendant of the dependent variable, which biases the modularity coefficient. It cannot "rule out" capability explanations. | Model 4 conditions on a post-outcome variable (bad control, collider or descendant of the outcome), so its estimate is biased and the robustness claim does not follow | Yes (simulation under the paper's stated relations) |
| SD3 | Inferential; epistemological | §4 (H3) and §5 ("rule out mimetic isomorphism") | A non-significant coefficient (0.042, SE 0.038) is treated as evidence of absence. The 95% CI is about [−0.032, 0.116]; its upper end is about the size of the modularity coefficient (0.112). No power or equivalence analysis is offered. | The null on peer outsourcing is taken as refuting the rival; the CI does not exclude a substantial peer effect (equivalence or power missing) | Yes (CI from reported estimates) |
| SD4 | Ontological; pragmatic | §3.2 "Peer outsourcing" and §2.4 H3 | The rival's construct is misrepresented. Mimetic isomorphism concerns imitation of organizations perceived as legitimate or successful, under uncertainty; same-state prevalence measures geographic co-location, not referent selection. The test is of a straw version of the institutional account, and the uncertainty contingency the rival predicts is not tested. | The peer measure does not capture the institutional construct (referents chosen by status, success, similarity or network ties, not state), so H3 does not test the rival theory as its proponents state it | No (conceptual) |
| SD5 | Epistemological | §4 (H2) and §5 second paragraph | A result contrary to H2 is accommodated by an auxiliary (legitimacy pressure under uncertainty) introduced after the fact, and the result is then called "consistent with our theory". A Lakatosian degenerating move: the theory is protected, not tested. | The explanation of the negative interaction is post hoc or ad hoc, untested, and the claim of consistency with the theory is unwarranted | No (but see SD1: the correct derivation predicts the negative sign, which makes the rescue idle) |
| SD6 | Technical | Table 2 and §3.1 | (a) Environmental uncertainty in Model 3: 0.084 (SE 0.051) is starred *** (p < 0.001); z ≈ 1.65, two-sided p ≈ 0.10. (b) A balanced panel of 412 hospitals over 2009–2019 (11 years) has 4,532 observations, not the 4,712 reported. | Either (a) or (b), with the arithmetic; full credit for both | Yes (arithmetic) |
| SD7 | Pragmatic | Abstract, §1 ("first study to adjudicate") | The contribution claim ignores directly relevant prior work: Loh & Venkatraman (1992) on imitative diffusion of IT outsourcing (the "Kodak effect"); Ang & Cummings (1997) on institutional influences on IS outsourcing; Roberts & Greenwood (1997) on integrating transaction-cost and institutional theories. | The "first study" claim is false or overstated, naming at least one of these (or other genuinely prior work on TCE and institutional explanations of IT outsourcing) | Partly (literature search, not code) |
| SD8 | Ontological | §2.4 (from Props. to H1 and H2), §3.2 measures | Level-of-analysis mismatch. The model's threshold is defined over functions; the data are hospital-level spending shares and an average CIO rating. Moving from $k^*$ to the hospital's share $\Phi$ requires assumptions about the distribution of $k$ across functions (and its invariance to $m$) that are not stated. | The propositions are about functions (transactions) but are tested on hospital-level aggregates without the bridging assumptions, so the test does not follow from the model | Partly (a simulation can show the share need not move with $k^*$ when the distribution of $k$ shifts) |
| SD9 | Inferential | §5: "rule out mimetic isomorphism" versus the legitimacy explanation of the interaction | Incompatible commitments. The paper commits to institutional pressures playing no role (rule out mimetic isomorphism) and, two paragraphs later, explains its interaction result by legitimacy pressures, an institutional mechanism. | The paper both rules out institutional pressures and relies on legitimacy pressure to explain the interaction; the two commitments are in tension | No (a scorekeeping finding) |

**Known unseeded weaknesses** (written down before the runs, so that they are not counted as discoveries of the seeding): the two-way fixed-effects event study with staggered adoption is vulnerable to bias under heterogeneous treatment effects; modularity adoption may be chosen in anticipation of outsourcing (reverse timing); the CIO-rated specificity measure is a single-informant perception; survivorship in a balanced panel of survey responders is mentioned but not addressed; the corner where $k^* \geq 1$ is ignored. These are realistic weaknesses that a competent reviewer may raise; they are scored as unseeded findings.

---

## Annex C. Manifest of the transcripts, check code and harness outputs

The full transcripts, in run order, with each check's code and the harness output, are in the supplementary file `REVIEWERSHIP_ANNEX_C_TRANSCRIPTS.md`, which is also at the root of the repository, and as separate files in `runs/`. The table lists every file with its size and the first 16 hex digits of its SHA-256 hash, so that a reader can confirm that the files are those this appendix describes.

| File | Bytes | SHA-256 (prefix) |
|---|---|---|
| `runs/01_dialogue/turn_01_elicitor_E0.md` | 5,551 | `81f0c7a6ce851d65…` |
| `runs/01_dialogue/turn_02_editor.md` | 4,901 | `44ae4b3f642f9dcf…` |
| `runs/01_dialogue/turn_02_editor_standin_note.md` | 1,010 | `e6e1b77ec23082f0…` |
| `runs/01_dialogue/turn_03_elicitor_EB_S1.md` | 12,942 | `f463636cdda2e6cf…` |
| `runs/01_dialogue/turn_04_reviewer_S1.md` | 10,390 | `d1023525ef3a6e49…` |
| `runs/01_dialogue/turn_04_reviewer_standin_note.md` | 923 | `97c9cb895f4c2ba4…` |
| `runs/01_dialogue/turn_05_elicitor_S2.md` | 24,977 | `7459a6d02bcf7573…` |
| `runs/01_dialogue/turn_06_reviewer_S2.md` | 13,746 | `77cd49e275e69440…` |
| `runs/01_dialogue/turn_06_reviewer_standin_note.md` | 902 | `f13283fcb7d9e9d3…` |
| `runs/01_dialogue/turn_07_elicitor_S3.md` | 30,871 | `f4b2fd95c68e011f…` |
| `runs/01_dialogue/turn_08_reviewer_S3.md` | 14,502 | `200aec92029c9f66…` |
| `runs/01_dialogue/turn_08_reviewer_standin_note.md` | 1,385 | `ae162e15f3495e14…` |
| `runs/01_dialogue/turn_09_elicitor_SPEC.md` | 71,102 | `148f7c33a4dfef62…` |
| `runs/02_reviewer_draft.md` | 10,801 | `4702005efea83b50…` |
| `runs/02_reviewer_draft_standin_note.md` | 5,900 | `da5e3e04c4776957…` |
| `runs/03_checks/r-tce_chk_1.out.txt` | 434 | `6c3c040448632193…` |
| `runs/03_checks/r-tce_chk_1.py` | 1,579 | `9291cd48945fe163…` |
| `runs/03_checks/r-tce_chk_1_b2.out.txt` | 1,000 | `0b206aa98c9b6b99…` |
| `runs/03_checks/r-tce_chk_1_b2.py` | 1,228 | `ba87d046731502aa…` |
| `runs/03_checks/r-tce_chk_3.out.txt` | 1,716 | `0df9d6889c2298ed…` |
| `runs/03_checks/r-tce_chk_3.py` | 1,786 | `b6feeaf7b5fff9b8…` |
| `runs/03_checks/r-tce_chk_4.out.txt` | 310 | `9af127b719c0570f…` |
| `runs/03_checks/r-tce_chk_4.py` | 1,530 | `e53d58ed06229029…` |
| `runs/03_checks/results.json` | 845 | `613a6a6dfb96f930…` |
| `runs/03_simulated_reviewer_TCE.md` | 59,886 | `3189b06a27efc8ba…` |
| `runs/04_checks/r-inst_chk_1.out.txt` | 441 | `e999992eed8949ca…` |
| `runs/04_checks/r-inst_chk_1.py` | 1,015 | `05f0ea58f13d2f12…` |
| `runs/04_checks/r-inst_chk_2.out.txt` | 1,549 | `ad61eb8f5c43cac1…` |
| `runs/04_checks/r-inst_chk_2.py` | 1,738 | `4054e0a6743b2c89…` |
| `runs/04_checks/r-inst_chk_3.out.txt` | 707 | `fc42ca6c5cb92b3d…` |
| `runs/04_checks/r-inst_chk_3.py` | 689 | `3ac9755c864dbe62…` |
| `runs/04_checks/results.json` | 638 | `6e53fa4fcdc5dec5…` |
| `runs/04_simulated_reviewer_INST.md` | 67,943 | `0ba73ceeda35c57d…` |
| `runs/05_checks/r-beh_chk_1.out.txt` | 435 | `24674e7180d3f78e…` |
| `runs/05_checks/r-beh_chk_1.py` | 2,114 | `09f2f12bf79b8c65…` |
| `runs/05_checks/r-beh_chk_2.out.txt` | 1,306 | `e5bb8dc499ab8244…` |
| `runs/05_checks/r-beh_chk_2.py` | 1,516 | `998ca8f35b134171…` |
| `runs/05_checks/r-beh_chk_3.out.txt` | 70 | `926fa5c64a331d9b…` |
| `runs/05_checks/r-beh_chk_3.py` | 465 | `d2a581449e06acdd…` |
| `runs/05_checks/r-beh_chk_4.out.txt` | 70 | `dd4b9fd8954cce92…` |
| `runs/05_checks/r-beh_chk_4.py` | 837 | `4d72b8a9ece8492d…` |
| `runs/05_checks/results.json` | 842 | `588f09a96484fc6d…` |
| `runs/05_simulated_reviewer_BEH.md` | 66,863 | `9f8e91debce33d48…` |
| `runs/06_checks/r-did_chk_1.out.txt` | 448 | `d16b5bd8a4b62677…` |
| `runs/06_checks/r-did_chk_1.py` | 1,832 | `5aa0de22eaddaac6…` |
| `runs/06_checks/r-did_chk_2.out.txt` | 1,962 | `877ed189fdb2b99a…` |
| `runs/06_checks/r-did_chk_2.py` | 1,811 | `4dabcc75264012de…` |
| `runs/06_checks/r-did_chk_3.out.txt` | 279 | `cbabde48567afa30…` |
| `runs/06_checks/r-did_chk_3.py` | 465 | `85454c7bc4babcc8…` |
| `runs/06_checks/r-did_chk_4.out.txt` | 535 | `85ea072289b8900e…` |
| `runs/06_checks/r-did_chk_4.py` | 1,061 | `be7b42b0421b1732…` |
| `runs/06_checks/r-did_chk_5.out.txt` | 703 | `599a7ba0b11a2d28…` |
| `runs/06_checks/r-did_chk_5.py` | 995 | `73d8101747f50642…` |
| `runs/06_checks/r-did_chk_6.out.txt` | 411 | `ec0359f5f4ce5b61…` |
| `runs/06_checks/r-did_chk_6.py` | 2,815 | `9c728731d3ea0855…` |
| `runs/06_checks/r-did_chk_7.out.txt` | 188 | `44dd63a100a00189…` |
| `runs/06_checks/r-did_chk_7.py` | 1,104 | `7ad5dfa876acdf49…` |
| `runs/06_checks/results.json` | 1,472 | `4f406e50207456cb…` |
| `runs/06_simulated_reviewer_DID.md` | 71,936 | `938d9fc3010a87f3…` |
| `runs/07_checks/pnl_chk_1.out.txt` | 1,686 | `728e37c203a7942f…` |
| `runs/07_checks/pnl_chk_1.py` | 2,235 | `9668ffb3c865fca4…` |
| `runs/07_checks/results.json` | 208 | `aee114eb40f667b8…` |
| `runs/07_panel_synthesis.md` | 99,354 | `451aaadb1e0c9086…` |
| `runs/08_checks/p08_chk_1.out.txt` | 717 | `0602300f7573df26…` |
| `runs/08_checks/p08_chk_1.py` | 3,230 | `c9729c9510572db9…` |
| `runs/08_checks/p08_chk_2.out.txt` | 2,959 | `bff897196e18cd60…` |
| `runs/08_checks/p08_chk_2.py` | 5,534 | `7422a03eebd7e7d8…` |
| `runs/08_checks/p08_chk_3.out.txt` | 1,091 | `7a8b510cee50cd53…` |
| `runs/08_checks/p08_chk_3.py` | 3,875 | `5458dd2435f60fe4…` |
| `runs/08_checks/p08_chk_4.out.txt` | 2,289 | `704bdf58fc53ee7d…` |
| `runs/08_checks/p08_chk_4.py` | 4,369 | `e3748b4808e655db…` |
| `runs/08_checks/p08_chk_5.out.txt` | 1,502 | `a49eb23d99b6654e…` |
| `runs/08_checks/p08_chk_5.py` | 3,047 | `fcd408352bd5097f…` |
| `runs/08_checks/results.json` | 3,031 | `a76d3d1548a2ee09…` |
| `runs/08_probe_derivation.md` | 61,476 | `27a4acfc3ae1a669…` |
| `runs/09_checks/p09_chk_1.out.txt` | 452 | `62adffb4d363db17…` |
| `runs/09_checks/p09_chk_1.py` | 1,443 | `f7896a4b8d0ffd25…` |
| `runs/09_checks/p09_chk_2.out.txt` | 1,724 | `36f2ae908b587886…` |
| `runs/09_checks/p09_chk_2.py` | 2,426 | `2d9e5526ac64a658…` |
| `runs/09_checks/p09_chk_3.out.txt` | 788 | `9c8d1e9698f68c40…` |
| `runs/09_checks/p09_chk_3.py` | 1,649 | `8e5f639da7bee53e…` |
| `runs/09_checks/p09_chk_4.out.txt` | 703 | `6f38c3ce669a2080…` |
| `runs/09_checks/p09_chk_4.py` | 1,395 | `55f63a629cc073f3…` |
| `runs/09_checks/p09_chk_5.out.txt` | 937 | `0fb1394951e5cf51…` |
| `runs/09_checks/p09_chk_5.py` | 4,160 | `6ded55b98c053248…` |
| `runs/09_checks/p09_chk_6.out.txt` | 1,929 | `f976f1a5ca037245…` |
| `runs/09_checks/p09_chk_6.py` | 6,675 | `8b802b4a3417ab3f…` |
| `runs/09_checks/p09_chk_7.out.txt` | 1,013 | `67f5324df060efb2…` |
| `runs/09_checks/p09_chk_7.py` | 3,956 | `fc8516b79dc6d19f…` |
| `runs/09_checks/p09_chk_8.out.txt` | 2,443 | `14a68b3e88557021…` |
| `runs/09_checks/p09_chk_8.py` | 4,248 | `cf63a163e9b50a98…` |
| `runs/09_checks/p09_chk_9.out.txt` | 701 | `8ba1923166a7adf5…` |
| `runs/09_checks/p09_chk_9.py` | 3,251 | `280fbf5afe481350…` |
| `runs/09_checks/results.json` | 4,615 | `2be75db17d40807c…` |
| `runs/09_probe_identification_numerical.md` | 89,381 | `9005de186aa98af7…` |
| `runs/10_checks/p10_chk_1.out.txt` | 1,299 | `76dd878204bf93e6…` |
| `runs/10_checks/p10_chk_1.py` | 5,307 | `31566af031342a14…` |
| `runs/10_checks/p10_chk_2.out.txt` | 2,439 | `4fc6763bcdc88176…` |
| `runs/10_checks/p10_chk_2.py` | 5,024 | `55e21886adc186ef…` |
| `runs/10_checks/p10_chk_3.out.txt` | 687 | `85059c42926f7543…` |
| `runs/10_checks/p10_chk_3.py` | 2,774 | `18b8fa7eb232bc77…` |
| `runs/10_checks/p10_chk_4.out.txt` | 592 | `143e490fde020cb3…` |
| `runs/10_checks/p10_chk_4.py` | 3,827 | `788db90f94226c4b…` |
| `runs/10_checks/results.json` | 2,543 | `29e27ff42b8303a9…` |
| `runs/10_probe_inferential_audit.md` | 84,521 | `e32f7d882e80d975…` |
| `runs/11_consistency_check.md` | 35,792 | `da09b5cc496b6d21…` |
| `runs/12_reviewer_dispositions_final_review.md` | 57,645 | `f58e6bf143becaad…` |
| `runs/12_reviewer_standin_note.md` | 6,097 | `44a1f264766ed3e0…` |
| `runs/13_pilot/UNBLINDING_MAP.json` | 110 | `b5ad0406379fdcba…` |
| `runs/13_pilot/blind/review_A.md` | 25,068 | `006699536c2a49ef…` |
| `runs/13_pilot/blind/review_B.md` | 15,990 | `2aba7507913826c2…` |
| `runs/13_pilot/blind/review_C.md` | 22,609 | `330c746084ce441c…` |
| `runs/13_pilot/blind/review_D.md` | 12,965 | `a7f99d5b4d9d1001…` |
| `runs/13_pilot/blind/review_E.md` | 30,815 | `9ad27f68114c3f13…` |
| `runs/13_pilot/blind/review_F.md` | 40,087 | `ede5276d77629ac6…` |
| `runs/13_pilot/scoring.md` | 30,493 | `573b330a17e63b18…` |
| `runs/13_pilot/style_metrics.txt` | 720 | `79094435a7409cd5…` |
| `runs/14_editor_view.md` | 29,026 | `91fd60740d69ecc6…` |
| `runs/14_machine_origin.json` | 58,416 | `3228e3265fb6a1ed…` |
| `runs/configs/focal_perspective_normalized.json` | 2,599 | `1850e78c07088e3e…` |
| `runs/configs/simulated_perspectives.json` | 9,023 | `bf7377317f86511b…` |
| `runs/provenance_events.json` | 31,486 | `7ce80b25748762fc…` |
| `runs/recovery_scoring.md` | 42,314 | `552f66207f12aecf…` |
| `runs/recovery_scoring_R12.md` | 14,621 | `8f6629ae737b82d1…` |

---

## Annex D. Project Lakatos Tables 1 to 4

#### Project Lakatos component tables (Appendix A, Tables 1 to 4)

###### D.1 Table 1. ‘Routine’ Agents for the Cocreation of Research Contributions

| Agent                           | Function / Description                                                                                                                                            |
|:--------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Exploratory Literature Review   | Assists in the creation of an exploratory review in a specific domain or literature field.                                                                        |
| Targeted Literature Review      | Assists in the creation of a targeted literature review that aims to provide corroborating or refuting empirical arguments for a specific idea.                   |
| Synthetic Literature Review     | Assists in the creation of a synthetic synopsis of a field, based on targeted instructions.                                                                       |
| Data Interpreter: Descriptive   | Assists in the descriptive interpretation of a data set, based on specific instructions.                                                                          |
| Data Interpreter: Inferential   | Assists in performing inferential tests of one or more hypotheses based on a formatted data set.                                                                  |
| Data Interpreter: Causal        | Assists in performing tests of causal links and relationships in RCT or natural experiment data, based on a specification of one or more causal model topologies. |
| Data Specifier: Causal          | Assists in the formulation of causal models based on specific inputs that specify variable sets and available data sources.                                       |
| Modeling Assistant: Exploratory | Assists in the formulation of a model of a phenomenon or of a data set.                                                                                             |
| Modeling Assistant: Refiner     | Assists in the refinement of a model of a phenomenon or of a data set.                                                                                            |
| Proof Verifier                  | Assists in the verification of a formal proof.                                                                                                                    |
| Proof Synthesizer               | Assists in the construction of a proof or a counterexample.                                                                                                       |
| Summarizer/Conclusion Builder   | Assists in the summarization of main findings of a completed paper, or in the creation [entry incomplete in the source]                                                                          |


###### D.2 Table 2. Cognitive Operators for Advanced Research Assistant/Production Agents

| Operator            | Function / Description                                                                                                                                                                                                                                                                                                                                                                |
|:--------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Represent (X,Y)     | Represents natural language description X of a phenomenon in terms of a set of entities Y (concepts, variables—independent, dependent, control, moderators—and inferential links between them), where the representations (Y) include relational models (spatial, temporal, social), structural models, and dynamical models (including causal, teleological, and functional models). |
| Explain (X,Y; L)    | Constructs explanations of a natural language description X of a phenomenon in terms of a model (or representation) Y, using an inferential logic L (deductive, inductive, abductive; formal, informal).                                                                                                                                                                              |
| Justify (X,Y)       | Justifies a set of principles, injunctions, prescriptions or proscriptions (X) in terms of another set Y comprising normative and/or descriptive statements that are either general or particular, and may include empirical examples, counterexamples, competing theories, or alternative representations.                                                                           |
| Extend (X,Y)        | Extends the explanatory coverage of a set of concepts or models X into a domain of empirical support Y to which X had not previously been applied.                                                                                                                                                                                                                                    |
| Corroborate (X,Y)   | Provides corroborations for theory or model X from domain of applicability Y.                                                                                                                                                                                                                                                                                                         |
| Measure (X,Y; M)    | Derives a measure and associated measurement method M reflecting current technological capabilities for some quantity of interest X that renders it measurable via M within the variable space of some model or theory Y.                                                                                                                                                             |
| Integrate (X,Y)     | Produces an integration (logical, ontological, epistemological) of two representational entities (theories, models) X and Y.                                                                                                                                                                                                                                                          |
| Augment (X,Y)       | Augments a theory or model X by some or all of the base assumptions of another theory or model Y.                                                                                                                                                                                                                                                                                     |
| Challenge (X,Y)     | Produces a challenge to the empirical validity, coverage, coherence, or explanatory logic of theory/model X that is logically and semantically consistent with the substantive claims of theory/model Y.                                                                                                                                                                              |
| Refute (X,Y)        | Produces one or more refutations of the substantive, empirically testable claims of theory/model X from a relevant domain.                                                                                                                                                                                                                                                            |
| Reduce (X,Y; Φ)     | Produces a reduction of the explanatory apparatus of theory/model Y for phenomenon Φ to the terms (entities, variables, inferential links) of theory/model X.                                                                                                                                                                                                                         |
| Assimilate (X,Y; Φ) | Produces an assimilation (“unification”) of the empirical base associated with phenomena Φ of theory/model Y into the apparatus (entities, variables, inferential links) of theory/model X.                                                                                                                                                                                           |
| Eliminate (X,Y; Φ)  | Produces an elimination (as “epi-phenomenal”) of the theoretical apparatus of theory/model Y for the empirical base associated with phenomena Φ to the theoretical apparatus of theory/model X.                                                                                                                                                                                       |


###### D.3 Table 3. Reconstructing Epistemological/Inferential Discourse: A Grammar for Patterning Agents

| Category                                    | Subcategory / Type           | Description                                                                                                                                                                                                                                                                                                                   |
|:--------------------------------------------|------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Epistemological Stances (Commitments)       | Positivism                   | In strict form, only statements referring to observable/sensible quantities “make sense” (Mach); propositions about electrons are nonsense. In “layman” form (common among social scientists), theories/models must be testable against empirical data.                                                                       |
|                                             | Realism                      | In metaphysical form: we can speak about events/objects as they are and independently of our minds because the terms of a theory correspond to the right states of affairs. In language-dependent form: multiple ways of describing the same state of affairs exist, and “truth” is always “truth-in-a-description-language.” |
|                                             | Instrumentalism              | Theories/models are instruments for making predictions; they need not be “true,” “valid,” or “representative.” Advanced by Friedman (1953) and others in quantum mechanics.                                                                                                                                                   |
|                                             | Constructivism               | Multiple forms: the “picture of reality” emerging from science results from interactions between minds/bodies and phenomena; contributions of agencies and essences are inseparable and relevant to how objects and events are constituted and labelled (cf. participatory realism in Fuchs).                                 |
|                                             | Pragmatism                   | Amplified instrumentalism: the success of a theory/model depends on the useful effects it produces (including prediction/control).                                                                                                                                                                                            |
| Logics of Corroboration (Testing)           | Inductivism                  | Theories/models receive inductive support (confirmation) from observation statements (data) consistent with them. Includes Bayesian and frequentist approaches.                                                                                                                                                               |
|                                             | Falsificationism             | Theories/models can only be refuted by observation statements, never confirmed. Variants: dogmatic, methodological, naïve, and sophisticated falsificationism (Popper, Peirce).                                                                                                                                               |
| Ontological and Modeling Norms              | Ontological Commitments      | E.g., rational expected utility-maximizing agents in economics; “waves”/“particles” in QM; networks (of interactions, information flows, trust, epistemic states) in social network science.                                                                                                                                  |
|                                             | Commitments to Model Classes | E.g., teleological models in economics; causal models in physics; functional models in sociology and anthropology.                                                                                                                                                                                                            |
| Explanatory Norms                           | Explanatory Depth            | Some disciplines value explanations with high logical depth (e.g., mathematics, theoretical physics).                                                                                                                                                                                                                         |
|                                             | Explanatory Coverage         | Some disciplines value parsimony – explaining much by little (Ockham’s Razor).                                                                                                                                                                                                                                                |
| Justification Norms and Strategies          | Reductive Approaches         | Reduce a set of facts/theories/models to a more basic core (e.g., game theory in human/animal behavior).                                                                                                                                                                                                                      |
|                                             | Eliminative Approaches       | Eliminate phenomena as epi-phenomenal (e.g., eliminativist theories of consciousness).                                                                                                                                                                                                                                        |
|                                             | Assimilative Approaches      | Assimilate facts or models from other paradigms to support one’s own approach (e.g., transaction cost economics).                                                                                                                                                                                                             |
| Logical and Meta-Logical Norms of Inference | **—**                        | Heuristics and norms constraining scientific reasoning; commitments to deductive, inductive, or abductive inference; positions on replication, reproduction, generalization, and application, ranging from “we’re done” to “we don’t know what you are referring to.”                                                         |


###### D.4 Table 4. Types of Agents – A Preliminary Synopsis

| Id | Type (Intra- / Inter-Disciplinary) | Use Case / Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|:---|:-----------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| L1 | INTER / INTRA                      | Translator / Re-Voicer: Re-voices or reformulates an argument, derivation, or empirical result using the terminology, inferential logic, and rhetorical conventions of another disciplinary community. For example, translating a result in transaction-cost economics into neoclassical economics, or reframing an economic coordination model in the discourse of social psychology to expose hidden assumptions.                                                                   |
| L2 | INTRA                              | Challenger / Interrogator: Emulates the critical stance of peer reviewers within the same field. It raises discipline-typical questions about inferential validity, effect-size reliability, replicability, generalizability, relevance, and informativeness, helping researchers anticipate critiques likely to arise during the review process.                                                                                                                                     |
| L3 | INTER                              | Challenger / Interrogator: Operates across disciplinary boundaries, posing challenges concerning ontological choices (e.g., individual vs. systemic causation), modeling conventions (causal vs. functional explanations), or inferential schemes (frequentist vs. Bayesian reasoning). Serves as an epistemic bridge exposing implicit disciplinary biases.                                                                                                                          |
| L4 | INTRA                              | Deconstructor: Analyzes scholarly text to extract the normative and descriptive statements presupposed by its arguments, i.e., the background axioms and warrants that must hold for the claims to be accepted within the field. Reveals hidden epistemic commitments and disciplinary norms.                                                                                                                                                                                         |
| L5 | INTER                              | Deconstructor: Performs the same function across disciplines, reconstructing what norms, empirical regularities, or theoretical premises would have to hold for a claim in one field to be persuasive in another. Useful for mapping commensurability between paradigms.                                                                                                                                                                                                              |
| L6 | INTRA                              | Arbiter: Evaluates descriptive, methodological, and normative claims within a discipline, comparing them against canonical findings or accepted background results. Acts as an internal auditor of epistemic coherence and methodological rigor.                                                                                                                                                                                                                                      |
| L7 | INTER                              | Referee: Designs or identifies “crucial experiments” capable of arbitrating between competing theories from different disciplines, i.e., experiments whose results would be regarded as binding by both sides (for example, testing cognitive-economics versus behavioral-sociology explanations of cooperation).                                                                                                                                                                     |
| L8 | INTRA                              | Model Expander / Contractor: For a given axiomatic system, explores consequences of adding or removing assumptions, e.g., introducing risk aversion into the Modigliani–Miller theorem or bounded rationality into Nash bargaining. Derives empirical predictions of the modified theory, functioning both as generator and critic of extensions.                                                                                                                                     |
| L9 | INTRA                              | Meta-Analyzer: Conducts meta-analyses by aggregating and weighting existing studies according to effect size, reliability, reproducibility, and generalizability. Helps identify empirical regularities, contradictions, and potential boundary conditions.                                                                                                                                                                                                                           |
| L10 | INTRA                              | AltGen (Alternative Explanation Generator): For a given empirical result, generates one or more competing explanations from within the same field that yield identical predictions but rest on different assumptions or mechanisms—for instance, behavioral-economics findings interpreted via “irrationality” versus “contextual adaptive rationality,” or cognitive-neuroscience data explained by distinct architectural models.                                                   |
| L11 | INTER                              | AltGenX: Produces alternative explanations drawn from other disciplines that predict the same empirical regularities but imply different theoretical or practical conclusions, e.g., framing an organizational behavior result in terms of evolutionary game theory or sociotechnical systems design.                                                                                                                                                                                 |
| L12 | INTER                              | AltGenM: Generates explanations from other fields that rely on different model ontologies, for example, replacing a causal model with a teleological or functional one, or re-describing a psychological process using network or dynamical-systems language.                                                                                                                                                                                                                         |
| L13 | INTRA                              | PrisM (Predictive / Reflective Implication Synthesizer): For a given model or theory, derives implications for related theories of the same phenomenon in adjacent disciplines (e.g., computational-vision models vs. neurophysiological models of vision). It also anticipates the kinds of questions a researcher from another field would ask to reach convergent understanding.                                                                                                   |
| L14 | INTRA                              | ArgMap (Argument Mapper): Reconstructs informal arguments within a discipline using the claim–warrant–backing schema (approximately 82 canonical forms). Reveals the argumentative patterns regarded as valid or “warrantedly assertible” without further justification.                                                                                                                                                                                                              |
| L15 | INTRA                              | ArgDef (Argument Defeater): Generates prima facie defeaters – counterarguments that undermine or qualify claims identified by *ArgMap* – using norms that are themselves warranted within the same field. Provides internal dialectical testing.                                                                                                                                                                                                                                      |
| L16 | INTER                              | ArgDef (Cross-Field Defeater): Constructs defeaters or counterarguments warranted in another discipline that studies similar phenomena, illuminating how a claim valid in one field might fail under another’s epistemic criteria.                                                                                                                                                                                                                                                    |
| L17 | INTER / INTRA                      | RadianX (Reasoning and Dialogue Network): Builds structured, tree-like representations of dialogues on a shared empirical or theoretical problem, tracking each assertion, clarification, question, answer, and response. Evaluates conversational moves according to discursive norms – validity, relevance, informativeness, coherence, semantic consistency, and responsiveness – common to one or more fields. Enables transparent mapping of reasoning paths across disciplines. |

---

## Annex E. Consent instruments

#### Consent instruments (draft v0.1, 23 October 2026)

*Annex E of the Reviewership technical appendix. Draft language for the partner venue's submission and reviewer systems. To be adapted to the venue's systems and approved by the research ethics board of [institution] and by the venue before use. Bracketed items are filled at deployment.*

---

##### E.1 Author information and consent (shown at submission)

**About this study.** [Journal] is taking part in a study of machine-assisted peer review run by researchers at [institution]. In the study, some reviewers use a *reviewing workbench*: software that helps a human reviewer state their own standards before reading, see how a manuscript might read to scholars from other traditions, and check formal and numerical claims with code. **A human reviewer always reads your manuscript in full, writes the review and is responsible for every statement in it.** The workbench does not make or recommend editorial decisions.

**Where your manuscript would be processed.** Only inside a secure environment controlled by [institution], using AI models that run on [institution]'s own hardware or that are provided under agreements that forbid the provider from keeping your manuscript beyond [retention window] or using it to train any model. Your manuscript is never uploaded to a public AI service.

**What we will never do.** We will never use your manuscript, the reviews of it, or any record of the review to train or fine-tune an AI model. We will never share your manuscript outside the review process.

**How long we keep it.** Your manuscript text is deleted from the secure environment 30 days after the decision on this round (or within 7 days if you withdraw from the study). Records of *what was done* in the review (which tools were used, which findings the reviewer accepted or rejected), without any text from your manuscript, are kept for 7 years for audit.

**Your choices.** Please choose each item separately. Saying no to any item does not affect how your manuscript is handled or the editorial decision.

1. **Review track.** ☐ Assisted track: reviewers use the workbench; we aim to return reviews within [N] days. ☐ Conventional track: reviews at the journal's usual pace, without the workbench. ☐ I do not want my manuscript in the study (conventional review, no study use).
2. ☐ My manuscript may be reviewed in both ways (one assisted and one conventional review), so that the reviews can be compared. Both reviews will be sent to the editor and to me.
3. ☐ After the decision, I am willing to rate the reviews of my manuscript without being told how each was written (about 15 minutes).
4. ☐ De-identified data from the review of my manuscript (scores and coded categories of findings, never text) may be used in the study.
5. ☐ That de-identified data may be released publicly for other researchers.
6. ☐ My manuscript may be one of those on which different AI models are compared, inside the same secure environment and under the same rules.

**What you will see.** With the decision letter you will receive, for each assisted review, a short statement of which workbench capabilities the reviewer used and the reviewer's attestation that they read your manuscript in full and take responsibility for the review.

**Withdrawal.** You can withdraw from any research item until the decision on this round by writing to [contact]. Your manuscript text will then be deleted within 7 days.

**Questions and concerns.** [Study contact]; [ethics board contact and protocol number].

---

##### E.2 Reviewer information and consent (shown with the invitation)

**About this study.** As E.1, first paragraph.

**What you would do.** If you accept an assisted-track review, you will (1) have a short structured exchange with the workbench, informed by the editor's brief, to set out your own reviewing standards before reading (about 20 minutes); (2) read the manuscript and draft your review in the usual way; (3) optionally consult simulated reviewers from other traditions, adversarial probes that check formal and numerical claims with code, and a check of your draft against your own standards; (4) decide which, if any, of the workbench's findings to use; and (5) sign the review. You remain the author of the review and responsible for every statement in it.

**What is recorded.** The workbench records which capabilities you used, which findings you saw and what you decided about each, and which passages of your signed review originated in workbench output. The **editor** sees this record. The **authors** see a short statement of which capabilities you used and your attestation. Researchers see a de-identified version, without text, after the decision.

**Rules you agree to.** Use the workbench only through [institution]'s secure environment; do not copy the manuscript or any workbench output into any other AI tool; read the manuscript in full before consulting any agent's view of it.

**Your choices.** ☐ I agree to review in the assisted track under these rules. ☐ My review may be paired with a conventional review of the same manuscript. ☐ My review may be rated, without my name, by the editor and the authors after the decision. ☐ De-identified data from my review session (no text) may be used in the study. ☐ … and may be released publicly.

**Withdrawal and questions.** As E.1.

---

##### E.3 Venue authorization (summary of the written agreement)

The partner venue's editorial board and publisher authorize, for a fixed study period: (i) the offer of the assisted track to authors; (ii) export of consented manuscripts to the gateway; (iii) the scopes in Section 6.5 of the appendix that the venue elects to offer; (iv) attachment of the editor view to assisted reviews; (v) the retention and deletion schedule of Section 6.6; (vi) the governance board and stop rule of Section 6.9. The venue retains the right to suspend the study at any time. Editorial decisions remain the editors' alone; no editor is required to use any workbench output.

---

##### E.4 Editor information (for handling editors)

The workbench may ask you up to four short questions before a reviewer begins: what you take the manuscript's main contribution to be, why you chose this reviewer, any concerns of your own, and anything about the journal's standards or process the reviewer should weigh. Your answers become the reviewer's *editor brief*. Please do not include findings you would prefer the reviewer to reach independently. You will receive, with each assisted review, the editor view of its provenance record.
