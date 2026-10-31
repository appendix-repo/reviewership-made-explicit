**Best-Self Elicitor: Mode C consistency report** (`bs:CR`, Run 11, Reviewership v0.1)

This report compares the reviewer's draft with the standards specification `bs:SPEC` v1.0. It is not a review, it does not rewrite the review, and it does not judge the manuscript, which the elicitor has not read. Where a judgement would need the manuscript, the report says so.

**How to read this report.**
- **Line references.** `dr:Ln` means line n of `02_reviewer_draft.md`. Quotations from the draft are 25 words or fewer.
- **Ids.** Report ids use the prefixes `bs:CA`, `bs:CS`, `bs:CU`, `bs:CI`, `bs:CE`, `bs:CT`, `bs:CQ` and `bs:CH`. This avoids clashing with the contribution ids `bs:C1`–`bs:C5` in the editor brief `bs:EB`.

## 0. Report header

```json
{
  "type": "ConsistencyReport",
  "id": "bs:CR",
  "mode": "C",
  "run": "Run 11",
  "instruction_set": "Reviewership v0.1",
  "isReview": false,
  "compares": {
    "draft": "02_reviewer_draft.md (cited as dr:Ln)",
    "specification": "bs:SPEC v1.0 (turn_09_elicitor_SPEC.md)"
  },
  "elicitor_read_manuscript": false,
  "status_rule": "A standard is 'applied' if each condition is applied wherever it bites, either in the body, in the 'Checks run' list, or as a request for an input the paper does not report (bs:GR1); minor gaps are listed but do not change the status. A standard is 'partial' if at least one condition with material consequences is not shown. It is 'not applied' if no condition is shown. Each gap is graded minor or material, and 'needs_manuscript' marks judgements the elicitor cannot make without the paper.",
  "summary": {
    "applied": ["std:2", "std:3", "std:4", "std:5", "std:6", "std:8", "std:11", "std:12", "std:13", "std:14", "std:15", "std:16"],
    "partial": ["std:1", "std:7", "std:9", "std:10"],
    "not_applied": [],
    "silent_skips_of_must_parts": ["bs:CS1", "bs:CS2", "bs:CS3", "bs:CS4", "bs:CS5", "bs:CS6", "bs:CS7"],
    "undeclared_standards": ["bs:CU1", "bs:CU2", "bs:CU3", "bs:CU4"],
    "internal_consistency": ["bs:CI1", "bs:CI2", "bs:CI3", "bs:CI4", "bs:CI5", "bs:CI6"],
    "editor_brief": "Answered. N4 is answered only in part, and that part sits under the minor concerns (bs:CE1).",
    "bs:T7": "Settled in dr:L1: 'must means must'. No shedding is declared and none was found (bs:CT1)."
  },
  "harness_status": "Every formal and numerical finding in the draft is done by hand and stays 'asserted' until the harness runs it (bs:GR3). The draft correctly never uses the word 'demonstrated'. See bs:CH1."
}
```

## 1. Applied standards

```json
[
  {
    "id": "bs:CA1",
    "standard": "std:1",
    "priority": "must",
    "status": "partial",
    "passages": [
      "dr:L28-29: P2's numerator 'reduces to g1h0 − h1(s+g0), which A3 makes negative'; the proof 'treats H as constant in u'; 'A3 is never used'",
      "dr:L32: 'H2 is not derived (std:1)'; 'no aggregation step from a function-level threshold to a spending-weighted share'",
      "dr:L45: repair: 'correct P2, add the aggregation step'"
    ],
    "conditions": {
      "a": "Applied for H2 (dr:L26-29). For H1, P1 is shown to follow under std:5 (dr:L23, dr:L120).",
      "b": "Partly applied. The unstated assumption is identified (dr:L29). Whether A3, the assumption that fixes the sign, is defended (argued to be true of the setting) is not assessed.",
      "c": "Applied for H2 (dr:L32). The draft does not say whether H1's sign survives aggregation to the spending-weighted share.",
      "d": "The consequence is stated through the bs:T1 rule (dr:L33-34), not as an 'exploratory' label. This is consistent with bs:T1, but see bs:CI2 on the wording."
    },
    "gaps": [
      { "gap": "Whether A3 is defended is not assessed.", "weight": "material", "reason": "The draft's 'cleaner check' (dr:L35) relies on the corrected model, which A3 signs.", "needs_manuscript": true },
      { "gap": "std:1(c) is not stated for H1.", "weight": "material", "needs_manuscript": true },
      { "gap": "Whether H3 is presented as a test of the paper's own theory, and so falls under std:1, is not settled. The draft treats H3 under std:3 (dr:L49).", "weight": "minor", "needs_manuscript": true }
    ]
  },
  {
    "id": "bs:CA2",
    "standard": "std:2",
    "priority": "must",
    "status": "applied",
    "passages": [
      "dr:L33: 'The estimate has the opposite sign and its interval excludes zero' (std:2(e)(i))",
      "dr:L34: choosing an aggregation assumption now 'would be a rescue'",
      "dr:L35: a test on other evidence (the corrected sign of the effect of u), consistent with the closing clause of (d)",
      "dr:L36: the §5 legitimacy story 'counts against the model (std:2(c)–(d))'",
      "dr:L37: 'The abstract and the conclusion leave out the H2 result (std:2(a))'",
      "dr:L56: H3 classified as 'not supported' (std:2(e))"
    ],
    "gaps": [
      { "gap": "(b), whether the paper draws out what the H2 failure implies for the theory, is not stated. dr:L36 implies it does not.", "weight": "minor", "needs_manuscript": true }
    ]
  },
  {
    "id": "bs:CA3",
    "standard": "std:3",
    "priority": "must; (g) should",
    "status": "applied",
    "passages": [
      "(a) dr:L122: 'the rival is stated with a citation'",
      "(b) dr:L49-52: the disappearance of the peer coefficient is not a discriminating test, for three stated reasons",
      "(c) dr:L58: provisional; uses the paper's own statement of the rival (§1); put to the second reviewer",
      "(d) dr:L56: 'H1 fits both accounts (std:3(d))'",
      "(e) dr:L56, dr:L68: 'rules out' is not supported; weaker wording proposed for the title, the abstract and §5–6",
      "(f) dr:L56: the reinterpretation of 'fashion' as 'economizing' is not supported",
      "(g) dr:L75: asks for the effect of modularity on specificity"
    ],
    "gaps": [
      { "gap": "(c) cites the paper's own statement of the rival, not the rival's literature directly. dr:L122 records that the paper's statement carries a citation.", "weight": "minor", "needs_manuscript": false }
    ]
  },
  {
    "id": "bs:CA4",
    "standard": "std:4",
    "priority": "must",
    "status": "applied",
    "passages": [
      "(c) dr:L50: modularity may lie on the imitation path",
      "(a)-(b) dr:L52: 'The paper reports no peer–modularity correlation'; the state mean is noisy enough to lose a horse race"
    ],
    "gaps": [
      { "gap": "The missing correlation is noted but not explicitly requested, and it does not appear in the repair (dr:L68). bs:GR1 counts a request as applied.", "weight": "minor", "needs_manuscript": false }
    ]
  },
  {
    "id": "bs:CA5",
    "standard": "std:5",
    "priority": "must",
    "status": "applied",
    "passages": [
      "dr:L22: 'I re-derived both propositions by hand (§2.2–2.3 and the Appendix)'",
      "dr:L23-28: P1 follows; the P2 cross-partial and its reduction",
      "dr:L29: the unstated assumption, and its contradiction with h1 > 0 (std:5(b))",
      "dr:L120: listed in 'Checks run'"
    ],
    "mode_c_request": "Satisfied: the re-derivation was done, including (b).",
    "gaps": [
      { "gap": "The steps are compressed. The draft never writes out k*, the functional forms of G and H, A3's content or the parameter domain. The bs:GR3 harness needs all of these (see bs:CH1).", "weight": "minor for the draft; blocking for the harness", "needs_manuscript": true }
    ]
  },
  {
    "id": "bs:CA6",
    "standard": "std:6",
    "priority": "must for the minimum set",
    "status": "applied",
    "passages": [
      "(a)-(b) dr:L35, dr:L121: t and stars for all 16 coefficients in Table 2, beyond the minimum; one discrepancy found",
      "(c) dr:L95, dr:L121",
      "(d) dr:L96: point marginal effect, its zero point, and a request for the covariances (the std:6(d) fallback)",
      "(e) dr:L121: '2.7-point magnitude', 'one-sixth of an SD', the fall in the peer coefficient",
      "(f) dr:L121: 'The text matches the table, apart from the H2 omission'"
    ],
    "gaps": [
      { "gap": "(d) does not say whether the text's claim about the modularity effect holds across the range of the moderator.", "weight": "minor", "needs_manuscript": true },
      { "gap": "(a)-(b) for numbers quoted in the abstract. The abstract in the invitation quotes none; the manuscript's abstract may differ.", "weight": "minor", "needs_manuscript": true }
    ]
  },
  {
    "id": "bs:CA7",
    "standard": "std:7",
    "priority": "must; under the bs:T7 settlement, no part can be shed (dr:L1)",
    "status": "partial",
    "passages": [
      "dr:L123: modularity and the outcome pass (c) and (d)",
      "dr:L97: asset specificity fails (b) and (c)",
      "dr:L75: results without asset specificity requested (counts as applied for that control under bs:GR1)",
      "Rival's construct, applied in substance without a std:7 label: dr:L58 (construct mismatch), dr:L52 (noise), dr:L98 (hospitals per state; single-hospital states)"
    ],
    "gaps": [
      { "gap": "(a) and (e) are not shown for modularity or the outcome.", "weight": "material", "needs_manuscript": true },
      { "gap": "The ONT.4 test for identifying weight (does the control change the sign, or the size by a quarter or more, or stand in for the rival's construct?) is applied to no control. In-house staffing (dr:L74) is treated as a bad control, not under std:7.", "weight": "material", "needs_manuscript": true }
    ]
  },
  {
    "id": "bs:CA8",
    "standard": "std:8",
    "priority": "must here, since the draft locates efficiency claims in the abstract and §6 (dr:L89)",
    "status": "applied",
    "passages": [
      "dr:L89: three phrases are classified as efficiency claims, with where each appears; 'selection is weak among non-profit and public hospitals'; repair offered",
      "dr:L91: 'fashion' classified by the same rule (std:12(d))"
    ],
    "gaps": [
      { "gap": "(b), on functional claims, is not mentioned. Whether the paper makes any needs the manuscript.", "weight": "minor", "needs_manuscript": true },
      { "gap": "The repair route 'show the cost consequences' is not a route std:8(a) provides; see bs:CU3.", "weight": "minor", "needs_manuscript": false }
    ]
  },
  {
    "id": "bs:CA9",
    "standard": "std:9",
    "priority": "must",
    "status": "partial",
    "passages": [
      "dr:L124: clustered by hospital; matches modularity (hospital-year), not the peer measure or the event-study treatment (state-year)",
      "dr:L54: 'probably makes the interval too narrow (std:9)'",
      "dr:L79: 'Cluster by state with a wild bootstrap, since there are fewer than 50 states'"
    ],
    "gaps": [
      { "gap": "The draft does not state the level at which uncertainty, and so the modularity × uncertainty interaction, varies. These are key regressors, because the H2 test rests on them.", "weight": "material", "needs_manuscript": true },
      { "gap": "(c): for the Table 2 models, which contain key regressors at both hospital-year and state-year level, the draft gives no remedy. One is given only for the event study (dr:L79).", "weight": "minor", "needs_manuscript": false }
    ]
  },
  {
    "id": "bs:CA10",
    "standard": "std:10",
    "priority": "must",
    "status": "partial",
    "passages": [
      "(a) dr:L100: year effects absorb the EHR programme only if its effects were common",
      "(b), (f), (g) dr:L81: requested",
      "(c), (e) dr:L76-78: estimator robust to cohort effects, not-yet-treated comparison, leads with a threshold stated in advance, or a sensitivity analysis",
      "(d) dr:L77: not-yet-treated states, for the event study only"
    ],
    "gaps": [
      { "gap": "(d) is not discussed for the main within-hospital, continuous-treatment specification. Whether the comparison group makes sense is on the reviewer's own never-skip list (rv1:S1.3).", "weight": "material", "needs_manuscript": true },
      { "gap": "(a) is covered only for the EHR programme; it does not say what the hospital effects absorb.", "weight": "minor", "needs_manuscript": true }
    ]
  },
  {
    "id": "bs:CA11",
    "standard": "std:11",
    "priority": "must",
    "status": "applied",
    "passages": [
      "(a) dr:L72: 'Direction is not argued'",
      "(c) dr:L72: hospitals planning to outsource, or their vendors, may install the interfaces first (reverse causality)",
      "(b) dr:L80: an instrument proposed",
      "(c) dr:L100, dr:L74: omitted variables and bad controls"
    ],
    "gaps": [],
    "note": "See bs:CI1 on the instrument."
  },
  {
    "id": "bs:CA12",
    "standard": "std:12",
    "priority": "must (a standard for the draft; no weight)",
    "status": "applied",
    "passages": [
      "(a) dr:L60: the shared-conditions criticism is turned on the paper's own regressor",
      "(b) dr:L56: 'H1 fits both accounts'; dr:L87-89: the efficiency claim is not accepted",
      "(c) No verdict that the rival is unfalsifiable; the construct question goes to the second reviewer (dr:L58)",
      "(d) dr:L56, dr:L89, dr:L91: 'rules out', 'economizing' and 'fashion' are checked by the same rule"
    ],
    "mode_c_request": "Satisfied: both halves of the bias, (b) and (c), and the wording symmetry in (d), are visible.",
    "gaps": [
      { "gap": "The draft's own phrase 'a robust within-hospital association' (dr:L107) is not checked against its own open questions (dr:L74-75, dr:L81). See bs:CI6.", "weight": "minor", "needs_manuscript": false }
    ]
  },
  {
    "id": "bs:CA13",
    "standard": "std:13",
    "priority": "should; must for leads",
    "status": "applied",
    "passages": [
      "dr:L54: interval for the peer coefficient; threshold 0.07 (half of Model 1) labelled as the reviewer's choice, fixed before computing, with the authors invited to justify another; clustering clause applied",
      "dr:L78: for leads, 'intervals that exclude pre-trends of half the post-adoption effect', or a Rambachan–Roth analysis"
    ],
    "gaps": [
      { "gap": "Whether the paper's current event study reports leads. If it does, the must-for-leads check applies to them as reported, not only to the requested re-estimation.", "weight": "minor", "needs_manuscript": true }
    ]
  },
  {
    "id": "bs:CA14",
    "standard": "std:14",
    "priority": "should",
    "status": "applied",
    "passages": [
      "(a) dr:L51: state-level conditions; 'A lag does not remove persistent conditions'",
      "(b) dr:L125: does not arise, since a hospital's state is fixed",
      "(c) dr:L60"
    ],
    "gaps": []
  },
  {
    "id": "bs:CA15",
    "standard": "std:15",
    "priority": "must (a standard for the draft; no weight)",
    "status": "applied",
    "passages": [
      "Major 1, (a)-(d): dr:L39, dr:L41, dr:L43, dr:L45",
      "Major 2, (a)-(d): dr:L62, dr:L64, dr:L66, dr:L68",
      "Major 3: (a) dr:L83; (c) dr:L85; (b) implicit in the analyses proposed in dr:L77-80; (d) via the Recommendation, dr:L113-114",
      "(e): every major concern carries a label; the minor concerns sit under their own heading",
      "(f): dr:L105-107"
    ],
    "mode_c_request": "Satisfied: (f) is present.",
    "gaps": [
      { "gap": "Major 3 has no labelled 'test whose result I can't predict' and no 'Repair' line. The content is present elsewhere.", "weight": "minor", "needs_manuscript": false },
      { "gap": "Majors 1–3 each carry two labels at once ('damaging, fixable'). See bs:CI3.", "weight": "minor", "needs_manuscript": false }
    ]
  },
  {
    "id": "bs:CA16",
    "standard": "std:16",
    "priority": "should",
    "status": "applied",
    "passages": [
      "dr:L101: the P2 intuition 'would mislead a non-economist'; 'A3 should be stated in words'; defers on whether the rival is recognisable"
    ],
    "gaps": [],
    "note": "Not shed, although it is first in the shedding order."
  }
]
```

## 2. Silent skips

These are must conditions that the draft does not apply. No must standard is skipped in full. For each skip, the entry says what applying the condition would involve. The report does not apply any of them.

```json
[
  {
    "id": "bs:CS1",
    "standard": "std:1(b)",
    "skipped": "Whether each assumption that fixes a predicted sign is defended, meaning argued to be true of the setting.",
    "what_applying_involves": "For A3, and for any other assumption that signs P2, the corrected P2, or the corrected effect of u used in dr:L35, say whether the paper argues it is true of hospitals' IT sourcing. If it does not, ask for the argument. Note in the draft that the corrected-model check in dr:L35 inherits this condition.",
    "needs_manuscript": true
  },
  {
    "id": "bs:CS2",
    "standard": "std:1(c), for H1",
    "skipped": "Whether H1's predicted sign survives aggregation from the function-level threshold to the spending-weighted share.",
    "what_applying_involves": "State whether the paper shows this step for H1, or say that the general point in dr:L32 ('no aggregation step') applies to H1 as well, and whether the repair in dr:L45 is meant to cover it.",
    "needs_manuscript": true
  },
  {
    "id": "bs:CS3",
    "standard": "std:7, for controls that carry identifying weight",
    "skipped": "Identifying which controls carry identifying weight, and applying (a)-(e) to them. Under the bs:T7 settlement (dr:L1) this part cannot be shed.",
    "what_applying_involves": "For each control in Table 2, check whether including it changes the sign of a key coefficient, or its size by a quarter or more (the default, since the draft states no margin), or whether it stands in for the rival's construct. Apply (a)-(e) to each control that qualifies. Where Table 2 does not report the comparison with and without the control, ask for it (bs:GR1). The request in dr:L75 already covers asset specificity. In-house staffing and the remaining controls are not yet covered.",
    "needs_manuscript": true
  },
  {
    "id": "bs:CS4",
    "standard": "std:7(a) and (e), for the main regressor and the outcome",
    "skipped": "Whether each construct is defined and its measure argued to capture it; and, where the measure records adoption while the theory concerns use, whether the link between them is argued.",
    "what_applying_involves": "Say whether the paper defines modularity and the outsourced share, and argues that each measure captures its construct. Check whether 'connected through certified standard interfaces' records adoption or use; if it records adoption, check whether the paper argues the link to use. The entry in 'Checks run' (dr:L123) covers only (c) and (d).",
    "needs_manuscript": true
  },
  {
    "id": "bs:CS5",
    "standard": "std:9, for uncertainty and the interaction",
    "skipped": "The level at which uncertainty, and so the interaction term, varies, and whether hospital clustering matches it.",
    "what_applying_involves": "State the level at which uncertainty is measured and whether clustering by hospital matches it. For the Table 2 models that contain key regressors at both hospital-year and state-year level, say which option under (c) the paper should take: the coarsest level, two-way clustering, or an explanation.",
    "needs_manuscript": true
  },
  {
    "id": "bs:CS6",
    "standard": "std:10(d), and (a) beyond the year effects, for the main specification",
    "skipped": "Whether the comparison implicit in the main within-hospital, continuous-treatment design makes sense, and what the hospital effects absorb.",
    "what_applying_involves": "Say whether hospitals with smaller changes in modularity are a credible comparison for hospitals with larger changes, and what variation remains once hospital and year effects are in. If the paper does not report what is needed, ask for it (dr:L81 already asks for the within-hospital variation).",
    "needs_manuscript": true
  },
  {
    "id": "bs:CS7",
    "standard": "std:2(b)",
    "skipped": "Whether the paper says what the H2 failure implies for the theory and names the assumption in doubt.",
    "what_applying_involves": "One clause stating whether the paper does this. dr:L36 suggests it offers an outside mechanism instead.",
    "weight": "minor",
    "needs_manuscript": true
  }
]
```

## 3. Undeclared standards

The draft uses these criteria, but the specification has no standard for them. Each may be a legitimate addition. The question for the reviewer is whether to add it.

```json
[
  {
    "id": "bs:CU1",
    "criterion": "Bad controls: a control that is partly an outcome of the treatment, or that lies on the theory's own causal channel, is dropped, or results are reported without it.",
    "passages": [
      "dr:L74: in-house staffing 'is partly the outcome'",
      "dr:L75: asset specificity 'is the theory's own channel'",
      "dr:L114: 'the bad controls removed' is one of four conditions that would change the recommendation"
    ],
    "nearest_in_spec": "The TEC.3 setting ('mediators flagged (std:4(c))'). That is a setting, not a standard, and std:4 applies only to inferences drawn from a lost significance star.",
    "weight": "material, since it is a condition of the recommendation",
    "question": "Add it as a standard (for example std:17, must), merge it into std:10, or leave it as a setting?"
  },
  {
    "id": "bs:CU2",
    "criterion": "An instrumental-variable estimate with a strong first stage.",
    "passages": [
      "dr:L80: 'Report the first stage and use the requirements as an instrument'",
      "dr:L85: 'an IV estimate with a strong first stage'",
      "dr:L113: 'identification through the state requirements'"
    ],
    "nearest_in_spec": "std:11(b) allows 'an instrument' as a way to identify direction, but no standard states what an instrument must satisfy: relevance, or exclusion.",
    "weight": "material, given bs:CI1",
    "question": "Add the conditions for an instrument (relevance and exclusion) to std:11(b) or std:10?"
  },
  {
    "id": "bs:CU3",
    "criterion": "An efficiency claim can be entitled by showing its cost consequences directly.",
    "passages": ["dr:L89: 'Show the cost consequences, or restate the claims as alignment'"],
    "nearest_in_spec": "std:8(a) requires that the paper show or argue for selection pressure. It offers no direct cost-evidence route.",
    "weight": "minor",
    "question": "Amend std:8(a) to read 'shows or argues for selection pressure, or shows directly that the practice lowers costs', or keep std:8 as it is?"
  },
  {
    "id": "bs:CU4",
    "criterion": "A paper's explanation must be compatible with its own conclusions.",
    "passages": ["dr:L36: 'It is also an institutional mechanism, in a paper claiming to have ruled such mechanisms out'"],
    "nearest_in_spec": "None as a standard. This is ordinary scorekeeping: it records an incompatibility between commitments.",
    "weight": "minor",
    "question": "Leave it to the scoreboard, or add it as a standard?"
  }
]
```

The draft also uses some settings as criteria. These are not undeclared standards:
- the priority flag under PRA.3 (`dr:L102`, correctly marked "to verify");
- the code request under TEC.1 (`dr:L103`). TEC.1 also asks for the data where the licence allows, and the draft does not mention data.

## 4. Internal consistency, including the weights

```json
[
  {
    "id": "bs:CI1",
    "kind": "Two passages of the draft pull against each other",
    "passages": [
      "dr:L60: 'State requirements could raise outsourcing directly, not only through modularity.'",
      "dr:L80: 'use the requirements as an instrument. This is the paper's best route to identification.'",
      "dr:L107: 'a credible route to identification in the state requirements'",
      "dr:L113: 'identification through the state requirements' (a condition of the recommendation)"
    ],
    "issue": "To serve as an instrument for modularity, the state requirements must affect outsourcing only through modularity. dr:L60 gives the draft's own reason to doubt that. The draft does not reconcile the two, and the recommendation depends on the second. The same direct channel would also enter the event-study reduced form that dr:L80 refers to.",
    "weight": "material",
    "not_a_judgement_on": "Whether the instrument is valid. That needs the manuscript, and it is the reviewer's call."
  },
  {
    "id": "bs:CI2",
    "kind": "The draft against tension bs:T1",
    "passages": ["dr:L33: 'This counts against P2 as the paper derived it, not against the model's assumptions.'"],
    "spec": "The bs:T1 resolution says a failure counts against the model as the paper states it, 'assumptions included'.",
    "issue": "The draft exempts the assumptions. The case may be one bs:T1 did not anticipate: here the prediction came from a derivation error, and on the draft's reading the assumptions, correctly derived, imply the observed sign. dr:L35 still holds the assumptions to account through a separate test, which is consistent with bs:T1 in spirit.",
    "weight": "minor",
    "question": "Amend bs:T1 so that a failure counts against whichever element produced the prediction, or align the wording of dr:L33 with bs:T1?"
  },
  {
    "id": "bs:CI3",
    "kind": "Severity labels",
    "passages": [
      "Majors 1–3 each read '(damaging, fixable)' (dr:L20, dr:L47, dr:L70)",
      "Major 4 reads '(fixable)' (dr:L87)"
    ],
    "issue": "On the workbench's scale the categories are exclusive. 'Damaging' means a main claim is materially weakened or a main conclusion overstated. 'Fixable' means the repair leaves the conclusions intact. std:15(e) asks for one label per concern. Major 4's repair, restating 'economizing' as alignment (dr:L89), would change a conclusion the draft locates in the abstract and §6, which on the scale's definition is 'damaging'. Under bs:GR2, over-claiming is booked to INF and EPI at 0.9, not to ONT at 0.6.",
    "weight": "minor",
    "question": "Choose one label per concern. For Major 4, either relabel it or say why restating the claim leaves the conclusion intact."
  },
  {
    "id": "bs:CI4",
    "kind": "Severity of Major 2 against the editor brief",
    "passages": ["dr:L56: ''rules out' (abstract, §5) is not supported'"],
    "context": "The editor identified C3, 'rule out', as the paper's headline (bs:EB, contribution rank 2). On the scale, 'fatal' means the central claim does not stand if unrepaired. The draft labels the concern damaging, and its repair keeps a weaker claim ('does not require mimicry'), which supports 'damaging'.",
    "issue": "This is not an inconsistency. It is a place where one clause would make the severity call explicit for the editor.",
    "weight": "minor"
  },
  {
    "id": "bs:CI5",
    "kind": "Weights against the recommendation",
    "finding": "Consistent. The damaging findings fall on the two dimensions weighted 0.9: INF (Major 1, std:1 and std:5; Major 2, std:3 and std:4) and EPI (Major 2; Major 3). ONT (0.6) carries Major 4 and std:7 (dr:L97). TEC (0.7) findings are booked where their consequence lands (bs:GR2): the error in the stars sits inside Major 1, and the discrepancy in N is minor (dr:L95). PRA (0.4) carries std:16, which is minor (dr:L101). There is no fatal finding, so 'Major revision' (dr:L111) is consistent with the weights. The only open point is the booking of Major 4 (bs:CI3)."
  },
  {
    "id": "bs:CI6",
    "kind": "Wording in both directions (std:12(d)) applied to the draft's own praise",
    "passages": ["dr:L107: 'a robust within-hospital association between modularity and outsourcing'"],
    "issue": "The draft calls the association robust while asking how the main specification was chosen (dr:L81) and asking for results without two bad controls (dr:L74-75). Whether 'robust' survives those requests is open.",
    "weight": "minor"
  }
]
```

**Length.** By whitespace tokens, the body of the draft runs to about 1,475 words, including the title and formulae, against the "about 1,000" of `bs:GR1`. The "Checks run" list is about 127 words, within the 150 limit. Body length is a working rule, not a standard.

## 5. The editor brief

```json
{
  "id": "bs:CE1",
  "needs": {
    "bs:EB.N1": "Answered: dr:L22-29, dr:L120.",
    "bs:EB.N2": "Answered: dr:L70-85 (controls, event study, fixed effects, within-hospital variation); spot checks in dr:L95-96 and dr:L121.",
    "bs:EB.N3": "Answered: dr:L47-68.",
    "bs:EB.N4": "Answered in part, under the minor concerns. dr:L101 covers whether the model is readable for a non-economist and defers on whether the rival is recognisable. Whether the claims are fair to sociologists is addressed only indirectly, through dr:L56 and dr:L91.",
    "bs:EB.N5": "Answered: dr:L100 (the EHR programme) and dr:L89 (non-profit and public hospitals).",
    "bs:EB.N6": "Answered: dr:L102, marked 'to verify'."
  },
  "concerns": {
    "bs:EB.K1": "Answered, including the editor's question (failed prediction, a problem in the model, or a problem in the test?): a derivation error plus a missing aggregation step; H2 failed as stated; the observed sign is not a confirmation (dr:L28-37).",
    "bs:EB.K2": "Answered on the evidence side (dr:L47-68), including the legitimacy incompatibility (dr:L36). Institutional theory is left to the second reviewer (dr:L58)."
  },
  "settled_items_respected": "Yes. The question, the mechanism and the panel are acknowledged (dr:L16, dr:L107). Representativeness is not discussed. Survival selection: see bs:CQ4.",
  "out_of_scope_respected": "Yes. No institutional theory on its own terms, no literature search ('If I recall correctly', dr:L102), no re-running, and only obvious points about the setting.",
  "audience": "Both economists and sociologists. See N4."
}
```

## 6. How the draft settled `bs:T7`, and whether anything was shed

```json
{
  "id": "bs:CT1",
  "settlement": "dr:L1: 'must means must'. The must parts of std:7 (controls that carry identifying weight) and std:8 (efficiency as the paper's conclusion) cannot be shed; only their should parts can.",
  "option_chosen": "Exempt the must parts from shedding.",
  "effect_on_mode_c": "The provisional 'declared shedding' marker in bs:SPEC (bs:T7.default_for_mode_c) is withdrawn. Any must part of std:7 or std:8 that goes unapplied is a plain silent skip.",
  "consequences_for_the_specification": [
    "Record bs:T7 as resolved: must parts cannot be shed.",
    "Amend bs:GR4. Step 3 is now empty, because bs:SPEC gives std:7 no should part. Step 2 now sheds only std:8's should part, that is, efficiency claims made outside the title, the abstract and the conclusions."
  ],
  "shedding_declared": "None.",
  "shedding_found": "None. std:16 was applied (dr:L101). std:8 was applied, as a must (dr:L87-89). std:6 was applied beyond the minimum (all 16 coefficients, dr:L121). std:3(g) was applied (dr:L75). The controls clause of std:7 is partly unapplied, but this is not declared shedding, and under the settlement it could not be shed. It is reported as silent skip bs:CS3.",
  "presentation": "dr:L1 is a workbench note at the top of the review file. Decide whether it stays in the version sent to the editor."
}
```

## 7. The Mode C checks the reviewer requested

```json
[
  { "id": "bs:CQ1", "check": "std:5: the re-derivation was done, including (b)", "result": "Satisfied: dr:L22-29, dr:L120." },
  { "id": "bs:CQ2", "check": "std:12: both halves of the bias, (b) and (c), and (d)", "result": "Satisfied: dr:L56, dr:L58, dr:L60, dr:L87-91. One minor point is noted in bs:CI6." },
  { "id": "bs:CQ3", "check": "std:15(f): the draft says what survives", "result": "Satisfied: dr:L105-107." },
  {
    "id": "bs:CQ4",
    "check": "Survival selection gets one sentence, or a first-order treatment with a note to the editor (bs:EB.ann5, bs:T5)",
    "result": "Close, but not exact. dr:L99 has two sentences: a statement of when survival selection matters, and a request for exclusions and trends before exit. It makes no first-order determination, adds no note to the editor, and says nothing about representativeness. Whether a data request (bs:GR1) counts within the one-sentence cap is for the reviewer to decide."
  }
]
```

## 8. Harness checks pending (`bs:GR3`)

Each formal or numerical finding below is "asserted (by hand)" until the harness runs it. This report does not check any of them. Each entry lists the inputs the harness will need, and whether the draft supplies them.

```json
{
  "id": "bs:CH1",
  "items": [
    { "finding": "P1: ∂k*/∂m = k*/(1−m) > 0", "locus": "dr:L23", "inputs_in_draft": "the result only", "missing": "the transcription of k*; the parameter domain" },
    { "finding": "P2: the cross-partial and its reduction to g1h0 − h1(s+g0)", "locus": "dr:L26-28", "inputs_in_draft": "G′ = g1, H′ = h1", "missing": "k*; the forms of G and H; A3's content; the parameter domain" },
    { "finding": "t ≈ 1.65 for uncertainty in Model 3", "locus": "dr:L35", "inputs_in_draft": "0.084 (0.051)", "missing": "none" },
    { "finding": "412 × 11 = 4,532, against the reported 4,712", "locus": "dr:L95", "inputs_in_draft": "all", "missing": "none" },
    { "finding": "The marginal effect 0.118 − 0.061u reaches zero near u = 1.9 SD", "locus": "dr:L96", "inputs_in_draft": "both coefficients", "missing": "confirmation that u is standardized" },
    { "finding": "Interaction 95% CI of about −0.10 to −0.02", "locus": "dr:L33", "inputs_in_draft": "the coefficient (−0.061, from dr:L96)", "missing": "its standard error" },
    { "finding": "Peer 95% CI of about −0.03 to 0.12; threshold 0.07 = half of Model 1", "locus": "dr:L54", "inputs_in_draft": "0.042 (0.038)", "missing": "the Model 1 estimate behind the threshold" }
  ],
  "labelling": "The derivations are labelled 're-derived by hand' (dr:L22, dr:L120). The computations are not labelled 'recomputed by hand', as bs:GR3 asks. This is minor."
}
```

## Decisions for the reviewer

1. **Silent skips.** For each of `bs:CS1`–`bs:CS7`, decide whether to apply it or decline it, and give a reason if you decline. Under your own `bs:T7` settlement, `bs:CS3` (controls that carry identifying weight) cannot be shed.
2. **The instrument (`bs:CI1`).** Reconcile your point that state requirements may raise outsourcing directly (`dr:L60`) with your recommendation to use them as an instrument (`dr:L80`, `dr:L107`, `dr:L113`). Decide whether to add the conditions an instrument must meet to the specification (`bs:CU2`).
3. **Undeclared standards.**
   - Bad controls (`bs:CU1`): add as a standard, merge into `std:10`, or leave as a setting?
   - The cost-evidence route for efficiency claims (`bs:CU3`): amend `std:8`, or keep it as it is?
   - Incompatibility between a paper's explanation and its conclusions (`bs:CU4`): add as a standard, or leave it to the scoreboard?
4. **`bs:T1` wording (`bs:CI2`).** Amend `bs:T1` so that a failure counts against whichever element produced the prediction, or align `dr:L33` with `bs:T1` as it stands.
5. **Severity labels (`bs:CI3`, `bs:CI4`).** Give each major concern one label. Settle Major 4's label, which depends on whether restating "economizing" as alignment leaves the conclusion intact.
6. **Survival selection (`bs:CQ4`).** Does the data request count within your one-sentence cap?
7. **Consequences of `bs:T7` (`bs:CT1`).** Confirm the amendment to `bs:GR4`: step 3 becomes empty, and step 2 sheds only `std:8`'s should part. Decide whether `dr:L1` stays in the version sent to the editor.
8. **Smaller points.**
   - Whether N4 should be more visible than a minor concern (`bs:CE1`).
   - Whether to bring the body nearer your 1,000-word rule.
   - Whether to confirm the two recording choices still open from `bs:SPEC`: "argue each time" stored as neutral with a challenge, and "a derived implication, credibly tested" stored as an extension of the PRA.2 values.
