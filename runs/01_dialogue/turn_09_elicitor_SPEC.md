**Best-Self Elicitor: standards specification** (`bs:SPEC`, Reviewership v0.1)

This is a specification of the focal reviewer's standards, not a review. It contains no finding about the manuscript. The reviewer decides and signs the review.

## (a) StandardsSpecification

```json
{
  "type": "StandardsSpecification",
  "id": "bs:SPEC",
  "version": "1.0",
  "instruction_set": "Reviewership v0.1 (23 October 2026)",
  "produced_by": "Best-Self Elicitor (capability 1), Modes E and S",
  "isReview": false,
  "statement": "This is a specification of the focal reviewer's standards, elicited before the reviewer read the manuscript. It is not a review and contains no finding about the manuscript. The reviewer decides and signs the review.",
  "manuscript": {
    "title": "Modularity, Not Mimicry: Interoperability Standards and the Diffusion of IT Outsourcing in U.S. Hospitals",
    "elicitor_read_manuscript": false,
    "reviewer_read_manuscript_during_elicitation": false
  },
  "loci": {
    "inv:abs.sN": "Sentence N of the abstract in the review invitation",
    "inv:note": "Editor's note in the review invitation",
    "ed:E1..E4": "Editor's answers to bs:E0 (turn 2)",
    "rv1:": "Reviewer's reply to Round 1 (turn 4): S1.1-S1.3, S1.4.1-S1.4.5, EB.1-EB.5, depth",
    "rv2:": "Reviewer's reply to Round 2 (turn 6), by setting, inference or standard",
    "rv3:": "Reviewer's reply to Round 3 (turn 8), by section, standard, question or tension"
  },
  "elicitation": {
    "dialogue": [
      "turn 1: bs:E0, questions to the handling editor",
      "turn 2: editor's answers",
      "turn 3: bs:EB (final editor brief) and bs:S1 (Round 1 questions)",
      "turn 4: reviewer, Round 1",
      "turn 5: bs:S2 (Round 2 proposals)",
      "turn 6: reviewer, Round 2",
      "turn 7: bs:S3 (Round 3 sharpening)",
      "turn 8: reviewer, Round 3"
    ],
    "exposure_caveat": "Before elicitation the reviewer saw bs:EB, which reports manuscript details: the sign of an interaction in Table 2 (Model 3), how the peer measure is built, a legitimacy explanation in section 5, and a spending-share outcome. Standards were drawn from past reviews. Where a standard bears on a concern in the brief, its provenance says so (rv1 preamble; rv2 general note).",
    "balance_note": "The reviewer judged that the elicitor's suggested standards lean toward faults the editor already suspects. To balance the set, the reviewer widened std:12 to cover both halves of their bias and added std:15(f), on what survives. Mode C checks both (rv2 general note).",
    "reactions_kept_separate": [
      {
        "id": "bs:RX.a",
        "content": "The abstract presents the uncertainty interaction as a model prediction but does not report the result the editor describes.",
        "use": "Not used to draft standards. Overlaps std:2(a); recorded as provenance only."
      },
      {
        "id": "bs:RX.b",
        "content": "'Rule out' and 'first study to adjudicate directly' are strong claims, to be checked against the design.",
        "use": "Not used to draft standards. Overlaps std:3(e); recorded as provenance only."
      }
    ]
  },
  "perspective": {
    "type": "ReviewingPerspective",
    "id": "bs:PERSP",
    "value_conventions": "Values come from the admissible values in the perspective specification. null means the reviewer has no view. Where the reviewer's setting goes beyond the listed values, this is marked 'extension'.",
    "weights": { "ONT": 0.6, "EPI": 0.9, "INF": 0.9, "TEC": 0.7, "PRA": 0.4 },
    "dimensions": {
      "ONT": {
        "weight": 0.6,
        "weight_reason": "Matters most where measurement is itself an identification problem (rv2:weights).",
        "parameters": {
          "ONT.1": {
            "label": "admissible entities",
            "value": {
              "rational_actors": null,
              "boundedly_rational_actors": "admitted",
              "routines_and_capabilities": null,
              "networks_and_structures": null,
              "fields_logics_legitimacy": "admitted if specified so as to yield a prediction",
              "populations": null,
              "technologies_and_artifacts": null
            },
            "detail": "Actors are boundedly rational and capable of opportunism, Williamson's two behavioural assumptions.",
            "basis": ["rv1:S1.4.5", "rv2:ONT.1"]
          },
          "ONT.2": {
            "label": "level-of-analysis standard",
            "value": "cross-level with explicit bridging",
            "detail": "Built into std:1(c).",
            "basis": ["rv2:ONT.2", "rv2:std:9"],
            "standards": ["std:1"]
          },
          "ONT.3": {
            "label": "causal ontology",
            "value": {
              "individual-mechanistic": "admitted",
              "structural": null,
              "selection": "admitted; must be shown when invoked",
              "constitutive": null
            },
            "basis": ["rv1:S1.4.2", "rv2:ONT.3"],
            "standards": ["std:8"]
          },
          "ONT.4": {
            "label": "construct-individuation standard",
            "value": {
              "main_regressor": "strict",
              "outcome": "strict",
              "rival_key_construct": "strict",
              "controls_with_identifying_weight": "strict",
              "other_controls": "moderate"
            },
            "detail": "A control carries identifying weight if either of two things holds. (1) Including it changes the sign of a key coefficient, or changes its size by a margin the reviewer states before reading the results section (default: a change of a quarter or more). (2) It stands in for a rival's construct.",
            "basis": ["rv1:S1.3", "rv2:ONT.4", "rv3:Q3"],
            "standards": ["std:7"]
          },
          "ONT.5": {
            "label": "model classes",
            "value": {
              "causal": "admissible",
              "choice-theoretic": "admissible",
              "functional": "suspect",
              "selection": "admissible",
              "constitutive": null
            },
            "detail": "Selection explanations are admissible only when selection is shown. Functional explanations are rejected unless a selection or feedback mechanism is shown (std:8(b)). Constitutive explanations: no view, outside the reviewer's competence.",
            "basis": ["rv2:ONT.5", "rv3:std:8"]
          }
        }
      },
      "EPI": {
        "weight": 0.9,
        "weight_reason": "Identification is the one thing the reviewer never skips (rv2:weights).",
        "parameters": {
          "EPI.1": {
            "label": "stance",
            "value": "realism",
            "detail": "Mechanisms are real and are tested through their observable implications. No 'as if' defence is accepted for the assumption that does the work in a model (std:1(b)).",
            "basis": ["rv2:EPI.1", "rv3:std:1"]
          },
          "EPI.2": {
            "label": "logic of corroboration",
            "value": "falsificationist: sophisticated",
            "detail": "Read as Lakatos, not naive Popper. A failed derived prediction counts. An after-the-fact rescue counts against the theory (std:2).",
            "basis": ["rv1:S1.2", "rv1:S1.4.4", "rv2:EPI.2"]
          },
          "EPI.3": {
            "label": "identification standard",
            "value": {
              "design-based": "preferred",
              "model-based": "admissible if stated, argued, and tested where possible (placebos, overidentification); not a substitute where a design-based route exists",
              "process-tracing": null,
              "comparative-historical": null
            },
            "basis": ["rv1:S1.1", "rv1:S1.3", "rv2:EPI.3"],
            "standards": ["std:10", "std:11", "std:14"]
          },
          "EPI.4": {
            "label": "novelty standard",
            "value": "high",
            "basis": ["rv1:S1.2", "rv1:S1.4.4", "rv2:EPI.4"]
          },
          "EPI.5": {
            "label": "evidential standards",
            "value": {
              "effect_sizes_and_intervals_over_significance": "required",
              "equivalence_tests_or_bounds_for_absence_claims": "should; must for the leads in pre-trend checks (std:13, bs:T3)",
              "robustness": "the paper says how it chose the main specification and reports the specifications that did not work (std:10(g))",
              "pre_registration": "not expected for archival panel work; its absence is not penalised"
            },
            "basis": ["rv1:S1.3", "rv1:S1.4.5", "rv2:EPI.5", "rv3:T3"]
          },
          "EPI.6": {
            "label": "measurement standard",
            "value": {
              "factual_items": "single-informant acceptable",
              "perceptual_constructs": "validated multi-item or multi-informant"
            },
            "detail": "For perceptual constructs, a validation is an acceptable alternative to multiple informants.",
            "basis": ["rv2:EPI.6"],
            "standards": ["std:7"]
          }
        }
      },
      "INF": {
        "weight": 0.9,
        "weight_reason": "The reviewer's decisive rejection was an inference failure (rv2:weights).",
        "parameters": {
          "INF.1": {
            "label": "admitted inference modes",
            "value": {
              "deductive": "admitted",
              "inductive": "admitted",
              "abductive": "admitted; must be labelled"
            },
            "detail": "An explanation found after the results are in is labelled as such and gives no support. Inference to the best explanation between rivals needs discriminating evidence (std:3).",
            "basis": ["rv1:S1.2", "rv2:INF.1"],
            "standards": ["std:2", "std:3"]
          },
          "INF.2": {
            "label": "endorsed material inferences",
            "stance_values": "endorse | reject | neutral | argue_each_time. argue_each_time is recorded canonically as neutral: the inference carries no default entitlement, and when a manuscript relies on it the scorekeeper records a challenge (chl) that the manuscript must meet by argument.",
            "value": {
              "MI1": {
                "stance": "endorse",
                "condition": "Endorsed as theory only. In empirical use, the level of relationship-specific investment must not be assumed as given (std:11).",
                "note": "In-house governance is one safeguard among several; long-term contracts and hostages are others. This stays a setting and is not checked in Mode C."
              },
              "MI2": { "stance": "argue_each_time", "standards": ["std:8"] },
              "MI3": {
                "stance": "argue_each_time",
                "note": "Applies in both directions. Spread among peers is not evidence against imitation merely because an economizing variable also predicts it."
              },
              "MI4": {
                "stance": "argue_each_time",
                "note": "Applies to the step from adoption to use (std:7(e))."
              },
              "MI5": { "stance": "neutral" },
              "MI6": {
                "stance": "endorse",
                "condition": "Endorsed only as a conditional, and the proviso is checked every time. With staggered timing, the estimator must be robust to heterogeneous effects (std:10)."
              },
              "MI7": { "stance": "reject", "standards": ["std:4"] },
              "MI8": {
                "stance": "argue_each_time",
                "note": "This is an empirical claim about a technology, not a theoretical premise. Standard interfaces can relocate specificity rather than remove it, for example into lock-in to a vendor or platform. Causation can also run from planned outsourcing to the adoption of standards (std:11)."
              },
              "MI9": {
                "stance": "argue_each_time",
                "note": "With multiple equilibria, 'equilibrium' does not mean 'optimal' (std:8)."
              },
              "MI10": {
                "stance": "neutral",
                "note": "The second reviewer's domain. Not rejected: a legitimacy argument that predicts something an efficiency argument does not is testable, and is treated as such."
              }
            },
            "basis": ["rv1:S1.4", "rv2:MI1-MI10"]
          },
          "INF.3": {
            "label": "derivation standard",
            "value": "sketch",
            "detail": "The minimum is an explicit sketch that states every assumption fixing a sign. A proof is preferred for interactions. A verbal derivation is acceptable only for hypotheses labelled exploratory (std:1).",
            "basis": ["rv1:S1.2", "rv1:S1.4.3", "rv2:INF.3"],
            "standards": ["std:1"]
          },
          "INF.4": {
            "label": "enthymeme tolerance",
            "value": "low",
            "detail": "Applies to any premise that fixes the direction of a prediction.",
            "basis": ["rv1:S1.2", "rv2:INF.4"]
          },
          "INF.5": {
            "label": "explanatory norm",
            "value": "depth",
            "detail": "Depth means a mechanism specified closely enough to yield an implication the data could refute. Coverage is welcome, but a mechanism that covers everything predicts nothing.",
            "basis": ["rv2:INF.5"]
          },
          "INF.6": {
            "label": "justification strategies",
            "value": {
              "eliminative": "accepted, only with a discriminating test (std:3(b))",
              "assimilative": "suspect; counts only if the reinterpretation yields a prediction the rival's reading does not (std:3(f))",
              "reductive": "accepted, when the lower-level mechanism is shown to produce the pattern and not merely to be consistent with it"
            },
            "basis": ["rv1:S1.4.5", "rv2:INF.6", "rv3:std:3"]
          },
          "INF.7": {
            "label": "rival-handling standard",
            "value": "required",
            "basis": ["rv1:S1.4.5", "rv2:INF.7"],
            "standards": ["std:3", "std:12", "std:14"]
          }
        }
      },
      "TEC": {
        "weight": 0.7,
        "weight_reason": "High at the reviewer's best. A numerical slip is usually fixable unless it signals something deeper (rv2:weights). Findings are booked to the dimension where their consequence lands (bs:GR2).",
        "parameters": {
          "TEC.1": {
            "label": "reproducibility standard",
            "value": "preferred",
            "detail": "Not required at first round. For a revision, the reviewer asks for code that reproduces the main tables, plus the data where the licence allows. No code or data came with this submission (bs:EB).",
            "basis": ["rv2:TEC.1"]
          },
          "TEC.2": {
            "label": "checking depth",
            "value": {
              "formal_model": "re-derive",
              "estimates": "spot-check",
              "re-run": "not possible: no code or data supplied"
            },
            "detail": "Spot checks, not every cell. The minimum is set in std:6. In the draft, all checks are by hand; the harness runs afterwards (bs:GR3).",
            "basis": ["rv1:depth", "rv2:TEC.2", "rv3:Q1", "rv3:Q2"],
            "standards": ["std:5", "std:6"]
          },
          "TEC.3": {
            "label": "estimator discipline",
            "value": {
              "bad_controls": "mediators flagged (std:4(c)); controls that carry identifying weight are held to strict measurement (std:7)",
              "clustering": "std:9",
              "staggered_adoption_estimators": "required with a staggered discrete treatment: an estimator robust to effects that differ across adoption cohorts (std:10(e))",
              "specification_search": "the choice of main specification is disclosed and the specifications that did not work are reported (std:10(g))"
            },
            "basis": ["rv1:S1.1", "rv1:S1.3", "rv2:TEC.3", "rv3:std:10"]
          },
          "TEC.4": {
            "label": "numerical-consistency checking",
            "value": "always",
            "detail": "Covers at least the minimum set in std:6.",
            "basis": ["rv1:S1.3", "rv2:TEC.4"],
            "standards": ["std:6"]
          },
          "TEC.5": {
            "label": "formal-model standard",
            "value": "simulation acceptable with verification",
            "detail": "A closed form is preferred, and is expected for a one-page model. A simulation must report its parameter ranges and show that the claimed comparative statics hold across them, not at one chosen point.",
            "basis": ["rv2:TEC.5"]
          }
        }
      },
      "PRA": {
        "weight": 0.4,
        "weight_reason": "Governs how the reviewer writes more than what they conclude. Over-claiming is booked under INF and EPI (rv2:weights; bs:GR2).",
        "parameters": {
          "PRA.1": {
            "label": "audience",
            "value": "generalist organization-science readership: economists and sociologists of organizations",
            "detail": "The reviewer judges whether a non-economist can follow the model. On whether the rival is described recognisably, the reviewer defers to the second reviewer (std:16).",
            "basis": ["bs:EB", "rv1:EB.2"]
          },
          "PRA.2": {
            "label": "contribution standard",
            "value": [
              "extension: a derived implication, credibly tested",
              "problematization",
              "gap-spotting (counts least)"
            ],
            "detail": "Listed in order of preference. Being 'interesting' in Davis's sense (Davis 1971, to verify) is welcome but not sufficient. A higher burden of evidence attaches to the form of a claim ('rules out', 'overturns'), whichever account it targets, not to what the audience takes for granted (bs:T4).",
            "basis": ["rv2:PRA.2", "rv3:1", "rv3:T4"]
          },
          "PRA.3": {
            "label": "placement standard",
            "value": "sometimes",
            "detail": "The reviewer flags an earlier study only if they know of one; no literature search (bs:EB.N6).",
            "basis": ["rv1:S1.3", "rv2:PRA.3"]
          },
          "PRA.4": {
            "label": "relevance standard",
            "value": "none",
            "detail": "Implications for practice are not a criterion, unless the paper makes claims about practice. In that case, those claims must follow from the evidence.",
            "basis": ["rv2:PRA.4"]
          },
          "PRA.5": {
            "label": "discursive norms of the review",
            "value": ["separate fatal from fixable", "be specific", "be constructive"],
            "detail": "Operationalized in std:15 and bs:GR1.",
            "basis": ["rv1:S1.1", "rv1:S1.2"],
            "standards": ["std:15"]
          },
          "PRA.6": {
            "label": "the editor's brief",
            "value": "bs:EB",
            "detail": "Includes the reviewer's annotations bs:EB.ann1-ann6."
          }
        }
      }
    }
  },
  "general_rules": [
    {
      "id": "bs:GR1",
      "name": "When a standard counts as applied",
      "rule": "Failures go in the body of the draft: each failing condition, where it fails, and what follows. Passes go in a 'Checks run' list at the end, outside the body of about 1,000 words and under 150 words; it names the standards applied, the items they were applied to, and that they passed. If a check cannot be run because the paper does not report what it needs (descriptives, a correlation matrix, covariances), the draft asks for it, and that counts as applied. Mode C counts a standard as applied when either the body or the 'Checks run' list shows it.",
      "source": "rv3:0"
    },
    {
      "id": "bs:GR2",
      "name": "Priority, weight and booking",
      "rule": "'Must' means a standard must be applied in the draft. The dimension weight says how much a failure moves the recommendation. A TEC check is a procedure, and its finding is booked to the dimension where its consequence lands: a proposition that does not follow (std:5) is an INF finding, at 0.9; a numerical error or a mis-clustering (std:6, std:9) that would change a conclusion on which a hypothesis test rests is booked to EPI or INF; other TEC failures are minor. Over-claiming is booked to INF and EPI, so std:2(a) and std:3(e) carry the 0.9 weights. std:12 and std:15 apply to the draft, not the paper; they carry no weight, and Mode C only checks that they are applied.",
      "source": "rv3:T6"
    },
    {
      "id": "bs:GR3",
      "name": "Harness after the draft, not in it",
      "rule": "The draft is written without the workbench's other capabilities. Re-derivations and computations are done by hand, written down step by step with page or equation references, and reported as 're-derived by hand' or 'recomputed by hand', not as 'demonstrated'. After the draft, the harness runs the reviewer's steps for std:5, std:6 and std:13, on two conditions. First, the script states the parameter domain and reports where a sign holds on only part of it. Second, the script shows its transcription of the paper's model or numbers, so that the encoding can be checked. Any disagreement between the harness and the hand result is reported in the revision.",
      "source": "rv3:Q1"
    },
    {
      "id": "bs:GR4",
      "name": "Shedding order under time pressure",
      "rule": "If time runs short, shed in this order: (1) std:16; (2) std:8; (3) std:7 beyond the main regressor, the outcome and the rival's construct; (4) std:6 beyond the bs:Q2 minimum; (5) std:3(g). Never shed std:1, std:2, std:3(a)-(f), std:4, std:5, or std:9 to std:15. This is consistent with bs:EB.ann6, which never cuts N1-N3.",
      "source": "rv3:5",
      "open_issue": "bs:T7"
    },
    {
      "id": "bs:GR5",
      "name": "Facts reported in the brief",
      "rule": "What bs:EB says about the manuscript is the editor's report. Neither the elicitor nor the reviewer has checked it; the reviewer will check it on reading the paper.",
      "source": "rv3 preamble"
    },
    {
      "id": "bs:GR6",
      "name": "Citations",
      "rule": "Literature citations recalled by the elicitor or the reviewer are marked 'to verify'. Recollection is not verification.",
      "source": "rv3:1"
    }
  ],
  "standards": [
    {
      "id": "std:1",
      "title": "Hypotheses must be derived from the theory, at the level and on the scale tested",
      "dimension": "INF",
      "parameters": ["INF.3", "ONT.2", "EPI.1"],
      "priority": "must",
      "origin": "reviewer",
      "applies_to": "Each hypothesis the paper presents as a test of its theory.",
      "conditions": [
        "(a) It follows from a stated proposition, proof or explicit sketch.",
        "(b) Every assumption that fixes a predicted sign, including the sign of any interaction, is stated and defended. 'Defended' means argued to be true of the setting. For the assumption that does the work, neither convenience nor an 'as if' defence counts.",
        "(c) Where the theory's unit differs from the test's unit (for example, transactions versus organizations), the aggregation step is stated, and each predicted sign, including that of any interaction, is shown to survive it on the scale of the variable tested.",
        "(d) A hypothesis that fails (a)-(c) is labelled exploratory, and it counts neither for nor against the theory."
      ],
      "applied_when": "Per bs:GR1. A failure statement names the hypothesis, the condition that fails, where it fails, the consequence under (d), and the repair.",
      "related": ["std:2", "bs:T1"],
      "provenance": "rv1:S1.2; rv1:S1.4.3. (c) is the elicitor's suggestion (formerly std:9), which the reviewer accepted and folded in (rv2:std:1, rv2:std:9). (b) promotes the EPI.1 setting (rv3:std:1)."
    },
    {
      "id": "std:2",
      "title": "Failed predictions are results; after-the-fact rescues are costs",
      "dimension": "INF",
      "parameters": ["INF.1", "EPI.2", "EPI.4"],
      "priority": "must",
      "origin": "reviewer",
      "applies_to": "Each derived prediction that fails in the reported tests.",
      "conditions": [
        "(a) The failure is reported as a failure wherever the prediction is stated: the hypotheses, the results, the abstract and the conclusions.",
        "(b) The paper says what the failure implies for the theory, and names the assumption or step that is now in doubt.",
        "(c) An explanation offered afterwards, using a mechanism the model does not contain, is labelled as such and is not counted as support.",
        "(d) Such an explanation counts against the theory, unless the mechanism is built into the model and yields a further prediction that the data could reject and do not, tested on evidence other than the failure the mechanism was introduced to explain.",
        "(e) A prediction fails when either (i) the estimate has the opposite sign and its interval excludes zero, or (ii) the interval rules out any effect in the predicted direction large enough to matter (as in std:13). An estimate that is merely imprecise is reported as 'not supported', not as a failure, and the paper says which of the two it is. The same definition applies to the rival's predictions (std:12)."
      ],
      "scope_rule": "Resolution of bs:T1. A failure counts against the model as the paper states it, assumptions included. It does not count against the broader theory if the theory does not entail the prediction (std:1). A repaired derivation that flips the predicted sign after the result is known is a rescue, and falls under (d).",
      "applied_when": "Per bs:GR1. A failure statement names the prediction, which of (a)-(d) fails and where, and the classification under (e).",
      "booking": "(a) is over-claiming and is booked to INF/EPI at 0.9 (bs:GR2).",
      "related": ["std:1", "std:12", "std:13", "bs:T1"],
      "provenance": "rv1:S1.2; rv2:std:2. The words 'including the abstract and the conclusions' come from the elicitor's reserve PRA suggestion, which the reviewer holds in general; they overlap bs:RX.a, recorded as provenance only. rv3:std:2 adds the closing clause of (d) and all of (e)."
    },
    {
      "id": "std:3",
      "title": "Ruling out a rival needs a discriminating test",
      "dimension": "INF",
      "parameters": ["INF.7", "INF.6", "PRA.2"],
      "priority": "must; condition (g) is should",
      "origin": "reviewer",
      "applies_to": "(a)-(e): each claim that a rival account is ruled out, or words to that effect. (f): any reinterpretation of the rival's evidence. (g): the paper's own mechanism.",
      "conditions": [
        "(a) The rival's prediction is stated as its own literature usually states it, with a citation.",
        "(b) At least one test is reported on which the two accounts predict different signs or patterns, and the paper says what each account predicts.",
        "(c) The rival's key construct is measured in a way its proponents would accept, and the paper argues this. The reviewer's judgement here is provisional: the draft states which definition of the rival's construct it uses, cites that literature, and flags the point as a question for the second reviewer (bs:T2).",
        "(d) Evidence consistent with the paper's own account counts as support only where the rival predicts something different.",
        "(e) If (b) or (c) fails, the paper says only that its evidence does not require the rival. No conclusion is stated more strongly than the design supports. A claim to have ruled out or overturned either account carries the higher burden set in PRA.2 (bs:T4).",
        "(f) Reinterpreting the rival's evidence as the paper's own counts only if the reinterpretation yields a prediction the rival's reading does not.",
        "(g) [should] The same discipline applies to the paper's own mechanism, measured against the obvious non-rival explanations of the same correlation. The paper reports at least one implication specific to its mechanism, not only the reduced-form association."
      ],
      "applied_when": "Per bs:GR1. A failure statement locates the ruling-out claim and names the failing condition. Where (e) applies, it proposes weaker wording.",
      "booking": "(e) is over-claiming and is booked to INF/EPI at 0.9 (bs:GR2).",
      "related": ["std:12", "std:14", "bs:T2", "bs:T4"],
      "provenance": "rv1:S1.4.4; rv1:S1.4.5; rv1:EB.3; rv2:std:3. The closing clause of (e) comes from the elicitor's reserve PRA suggestion and overlaps bs:RX.b, recorded as provenance only. (f) promotes INF.6 (assimilative); (g) was added in rv3:std:3."
    },
    {
      "id": "std:4",
      "title": "A lost significance star is not a null result",
      "dimension": "INF",
      "parameters": ["INF.2", "EPI.5"],
      "priority": "must",
      "origin": "reviewer",
      "applies_to": "Any inference that a variable has no effect, or plays no role, drawn from a coefficient that loses significance when a correlated regressor is added.",
      "conditions": [
        "(a) Collinearity between the two regressors is addressed (for example, their correlation, or a joint test).",
        "(b) Differential measurement error, meaning which regressor is measured with more error, is addressed.",
        "(c) Mediation, meaning whether the added regressor lies on the causal path from the first, is addressed.",
        "'Addressed' means tested, or given a specific reason why it does not apply. Listing it as a limitation does not count. The paper fails if any of (a)-(c) is unaddressed."
      ],
      "applied_when": "Per bs:GR1. A failure statement locates the inference and names which of (a)-(c) the paper leaves unaddressed. If the paper does not report the needed inputs (for example, a correlation matrix), the draft asks for them.",
      "related": ["std:13", "MI7"],
      "provenance": "rv1:S1.4.5; rv2:std:4; rv3:std:4."
    },
    {
      "id": "std:5",
      "title": "Re-derive the model",
      "dimension": "TEC",
      "parameters": ["TEC.2", "TEC.5"],
      "priority": "must",
      "origin": "reviewer",
      "applies_to": "Each proposition of the formal model.",
      "conditions": [
        "(a) The reviewer re-derives the proposition from the stated assumptions, including the sign of every comparative static and interaction it claims.",
        "(b) The reviewer checks that each step of the proof uses only assumptions stated in the set-up, and lists any unstated assumption that a step relies on.",
        "(c) In the draft, the re-derivation is by hand: each step is written down with the assumptions as the reviewer reads them and with page or equation references, and the finding reads 're-derived by hand'. After the draft, the harness runs the steps under the conditions of bs:GR3."
      ],
      "applied_when": "Per bs:GR1. A failure statement names the proposition, the step that fails or the unstated assumption, and where it occurs.",
      "booking": "A proposition that does not follow is an INF finding, at 0.9 (bs:GR2).",
      "mode_c": "Reviewer's request: check that the re-derivation was done, including (b) (rv2:std:5).",
      "provenance": "rv1:S1.3; rv1:depth; rv2:std:5. (c) is the elicitor's suggestion, accepted on conditions (rv3:Q1)."
    },
    {
      "id": "std:6",
      "title": "Spot-check the numbers",
      "dimension": "TEC",
      "parameters": ["TEC.4", "TEC.2"],
      "priority": "must for the minimum set; beyond it, sheddable (bs:GR4, step 4)",
      "origin": "reviewer",
      "applies_to": "The reported results and every number quoted about them.",
      "conditions": [
        "(a) For the key coefficients, t is approximately b/se, allowing for rounding.",
        "(b) The significance stars match t (or p) under the stated thresholds.",
        "(c) N is consistent across tables and with the sample description.",
        "(d) For each reported interaction, the marginal effect of the focal variable across the observed range of the moderator matches what the text claims. If the covariances are not reported, the reviewer computes the point marginal effects across the range, says that their intervals cannot be given, and asks for the covariances.",
        "(e) The magnitudes are economically plausible given the descriptive statistics.",
        "(f) The text describes each result as the table shows it: its sign, its significance, and which model it comes from."
      ],
      "minimum_set": "(a) and (b) for every coefficient on which a hypothesis test rests, and for every number quoted in the abstract; (c) for every table; (d) for every interaction; (e) for each main effect; (f) for every result that the abstract or the conclusions mention.",
      "applied_when": "Per bs:GR1. Passes go in the 'Checks run' list. A failure statement names the cell or sentence, the check, and the discrepancy.",
      "booking": "An error that would change a conclusion on which a hypothesis test rests is booked to EPI or INF. Other errors are minor (bs:GR2).",
      "provenance": "rv1:S1.3; rv2:std:6 adds (f); rv3:Q2 sets the minimum set and the fallback in (d)."
    },
    {
      "id": "std:7",
      "title": "Measures fit their constructs, with no correlation by construction",
      "dimension": "ONT",
      "parameters": ["ONT.4", "EPI.6", "INF.2"],
      "priority": "must; the parts beyond the main regressor, the outcome and the rival's construct are sheddable (bs:GR4, step 3; see bs:T7)",
      "origin": "reviewer",
      "applies_to": "The main regressor, the outcome, the rival's key construct, and any control that carries identifying weight (defined under ONT.4).",
      "conditions": [
        "(a) The construct is defined, and the paper argues that the measure captures it.",
        "(b) No governance-relevant attribute is measured by, or inferred from, the outcome it explains.",
        "(c) Perceptual constructs have multiple informants or a validation. Single-informant factual items are acceptable.",
        "(d) The regressor and the outcome are not built from shared components, such as a common denominator or the same survey item, that would correlate them by construction.",
        "(e) Where a measure records adoption and the theory is about use, the paper argues the link between them."
      ],
      "applied_when": "Per bs:GR1. A failure statement names the variable, the failing condition, and where in the paper the measure is described.",
      "provenance": "rv1:S1.3; rv1:S1.4.4; rv2:std:7 extends the standard to controls that carry identifying weight; rv3:Q3 defines identifying weight; rv3:std:7 adds (d), and (e), which promotes MI4."
    },
    {
      "id": "std:8",
      "title": "Efficiency claims must show selection; functional claims must name their mechanism",
      "dimension": "ONT",
      "parameters": ["ONT.3", "ONT.5", "INF.2"],
      "priority": "should; must where efficiency is the paper's conclusion, meaning it is stated in the title, the abstract or the conclusions as what the results show. Sheddable (bs:GR4, step 2; see bs:T7).",
      "origin": "reviewer",
      "applies_to": "Each conclusion the paper draws about governance, and any claim that a practice exists because it serves a function.",
      "classification": "(i) A motive or alignment claim: choices track transaction attributes ('choices are made to economize'). (ii) An efficiency claim: the observed choice lowers costs or is the optimal response ('the practice does economize'). Where a sentence does not say which it means, it is classified as (ii), the stronger reading, and the authors are asked to say which they mean. Words about the rival follow the same rule (std:12(d)): 'adopted for legitimacy' is a motive claim, and 'inefficient' is an outcome claim.",
      "conditions": [
        "(a) For each claim of kind (ii), the paper shows or argues for selection pressure: competition, and the time for selection to act. Where selection is weak, as in nonprofit or regulated sectors, it cannot be assumed.",
        "(b) A claim that a practice exists because it serves a function names the selection or feedback mechanism.",
        "Claims of kind (i) need neither."
      ],
      "applied_when": "Per bs:GR1. A failure statement quotes the conclusion, gives its classification, and states what selection argument is missing.",
      "provenance": "rv1:S1.4.2; rv2:std:8; rv3:Q4 sets the classification rule; rv3:std:8 adds (b), which promotes ONT.5."
    },
    {
      "id": "std:9",
      "title": "Clustering",
      "dimension": "TEC",
      "parameters": ["TEC.3"],
      "priority": "must",
      "origin": "suggested-rewritten",
      "applies_to": "The standard errors on every key regressor. Key regressors are all regressors on which a hypothesis test rests, including the measure of the rival.",
      "conditions": [
        "(a) Standard errors are clustered at the level at which the key regressors vary, or the paper explains why not.",
        "(b) With few clusters, a small-cluster correction is used (for example, a wild cluster bootstrap). Clusters count as few when there are fewer than 50, or, whatever the count, when one or a few clusters dominate in size, or when the key regressor varies in only a few clusters.",
        "(c) Where key regressors vary at different levels, the paper clusters at the coarsest level, uses two-way clustering, or explains why not."
      ],
      "applied_when": "Per bs:GR1. The draft states the level at which the paper clusters, the level at which each key regressor varies, and whether they match.",
      "booking": "A mis-clustering that would change a conclusion on which a hypothesis test rests is booked to EPI or INF. Otherwise it is minor (bs:GR2).",
      "related": ["std:13"],
      "provenance": "The elicitor's reserve suggestion, rewritten by the reviewer (rv2:std:9). The definition of key regressors is the elicitor's, accepted (rv3:std:9). rv3:std:9 adds (c); rv3:Q5 sets the threshold for few clusters."
    },
    {
      "id": "std:10",
      "title": "Find the source of the identifying variation",
      "dimension": "EPI",
      "parameters": ["EPI.3", "TEC.3", "EPI.5"],
      "priority": "must",
      "origin": "reviewer",
      "applies_to": "The main specification and the claims that rest on it.",
      "conditions": [
        "(a) The paper shows what the fixed effects absorb and what variation remains.",
        "(b) It shows which units supply the identifying variation, and how much within-unit variation there is in the regressor.",
        "(c) It shows whether those units differed before treatment, in levels or in trends.",
        "(d) The comparison group makes sense.",
        "(e) For a discrete treatment adopted at different times: estimates in event time, with leads, against units not yet treated, using an estimator robust to effects that differ across adoption cohorts (for example Callaway and Sant'Anna 2021, or Sun and Abraham 2021; both to verify).",
        "(f) For a continuous treatment: leads of the regressor, or pre-trends by later exposure.",
        "(g) The paper says how it chose the main specification and reports the specifications that did not work."
      ],
      "pass_criterion_for_c_e_f": "Resolution of bs:T3: the leads must be 'flat and precise'. The intervals on the leads must exclude pre-trends large enough to matter relative to the estimated effect; std:13 applies here at must priority. If they do not, the paper must show that the estimate survives plausible violations of parallel trends, through a sensitivity analysis of the Rambachan and Roth (2023) kind (to verify; see also Roth 2022 on pre-testing, to verify). Under std:15(c), the reviewer states in advance what interval on the leads would persuade them.",
      "survival_selection_rule": "Resolution of bs:T5. With unit fixed effects, survival selection threatens identification only if survival is related to changes in the regressor and the outcome, not to their levels. It is first-order if, on the paper's own numbers, it could plausibly produce an estimate of the reported size. If it is first-order, it is treated under (c) and (d), and the reviewer adds a short note to the editor saying why the point goes beyond one sentence. If not, the reviewer writes one sentence. In either case, nothing is said about representativeness.",
      "applied_when": "Per bs:GR1. A failure statement names the failing condition and says what pattern would persuade the reviewer (std:15(c)).",
      "mode_c": "Check that the treatment of survival selection is one sentence, or a first-order case with a note to the editor (rv2:ann5; rv3:T5).",
      "provenance": "rv1:S1.1; rv1:S1.3; rv2:std:10 rewrites (e) and adds (f); rv3:T3 sets the pass criterion; rv3:std:10 adds (g), which promotes EPI.5."
    },
    {
      "id": "std:11",
      "title": "Direction of causation for attributes chosen together with governance",
      "dimension": "EPI",
      "parameters": ["EPI.3", "INF.2"],
      "priority": "must",
      "origin": "reviewer",
      "applies_to": "Any regression of governance on an attribute that firms may choose with governance in view. Asset specificity is the standard case; a technology choice that changes specificity is another.",
      "conditions": [
        "(a) Either the direction of causation is argued: the paper gives a reason, specific to the setting and checkable, why the attribute was not chosen in anticipation of governance. Examples are timing (the attribute was fixed before the governance option existed) and an external driver (a mandate or schedule the firm does not control, with evidence that it applied). 'Firms adopt X for other reasons' is an assertion, not an argument.",
        "(b) Or the direction is identified, by timing, an instrument or the design. Evidence that the attribute does not respond to lagged governance counts here, as identification, not under (a).",
        "(c) In either case, reverse causality is addressed, and the obvious omitted variables are named and handled."
      ],
      "applied_when": "Per bs:GR1. A failure statement names the regressor and the missing argument or identification.",
      "provenance": "rv1:S1.4.1; rv1:S1.3; rv2:MI1 and MI8 notes; rv3:Q6 defines what counts as argued under (a)."
    },
    {
      "id": "std:12",
      "title": "Symmetry (a standard for the draft)",
      "dimension": "EPI",
      "parameters": ["EPI.2", "INF.7"],
      "priority": "must",
      "origin": "reviewer",
      "applies_to": "The reviewer's draft, not the paper. It carries no weight (bs:GR2).",
      "conditions": [
        "(a) For each evidential criticism the draft makes of the rival account, the draft asks whether the paper's own account meets the same bar on the same evidence, and it gives the answer.",
        "(b) The draft does not accept the economizing account on consistency alone where the rival predicts the same thing. This is the first half of the reviewer's bias.",
        "(c) The draft does not call an institutional account unfalsifiable or untested. If the reviewer thinks the version at issue makes no testable prediction, the draft puts that to the editor as a question for the second reviewer (bs:T2). This is the second half of the bias.",
        "(d) Wording cuts both ways. Any claim strength the draft rejects in statements about the rival ('ruled out', 'fashion'), it also checks in statements about the paper's own account ('economizing', 'shows'), using the classification in std:8.",
        "The definition of failure in std:2(e) applies to the rival's predictions too."
      ],
      "applied_when": "Conditions (a)-(d) are visible in the draft. Mode C pairs each criticism of the rival with its counterpart for the paper's own account.",
      "mode_c": "Reviewer's request: check both halves, (b) and (c), and the wording symmetry in (d) (rv2 general note; rv3:std:12).",
      "provenance": "rv1:S1.4.4; rv2:std:12 widens the standard to both halves of the bias; rv3:T2 resolves (c); rv3:std:12 adds (d)."
    },
    {
      "id": "std:13",
      "title": "Claims of absence need bounds",
      "dimension": "EPI",
      "parameters": ["EPI.5"],
      "priority": "should; must for the leads in pre-trend checks (bs:T3)",
      "origin": "suggested-rewritten",
      "applies_to": "Any claim that a variable has no effect, and the leads in pre-trend checks (std:10).",
      "conditions": [
        "(a) The paper reports the estimate and its confidence interval in the specification on which the claim rests. If the reviewer judges the standard errors to be mis-clustered (std:9), the draft says the interval is probably too narrow.",
        "(b) The paper states, in substantive terms, the smallest effect that would matter.",
        "(c) The paper shows that the interval excludes that effect. An equivalence test is one way to do this; it is not required.",
        "(d) Without such bounds, the paper says only that the effect is not distinguishable from zero in this sample."
      ],
      "reviewer_proposed_threshold": "If the paper states no smallest effect that would matter, the reviewer proposes one. It is labelled as the reviewer's choice; it is justified in substantive terms, either relative to the main effect or as a share of the outcome's standard deviation; it is fixed before the reviewer looks at the interval; and the authors are invited to replace it with a value they justify.",
      "applied_when": "Per bs:GR1. A failure statement names the claim, the interval if one is reported, and the threshold used. Approximate intervals (b +/- 1.96 se) are recomputed by hand in the draft and by the harness afterwards (bs:GR3).",
      "related": ["std:4", "std:10", "std:9"],
      "provenance": "The elicitor's suggestion, rewritten by the reviewer and kept separate from std:4 so the record shows which half is the elicitor's (rv2:std:13). rv3:Q7 sets the reviewer-proposed threshold; rv3:std:13 adds the clustering clause to (a); rv3:T3 raises the standard to must for leads."
    },
    {
      "id": "std:14",
      "title": "Peer influence versus shared conditions",
      "dimension": "EPI",
      "parameters": ["EPI.3", "EPI.6"],
      "priority": "should",
      "origin": "suggested-rewritten",
      "applies_to": "Each measure of peers' earlier adoption used as evidence for or against imitation. The reviewer gives their own verdict, since this needs only the rival's minimal claim, that peers' adoption causes one's own (bs:T2).",
      "conditions": [
        "(a) The design separates imitation from peers responding alike to shared conditions, such as common shocks, common regulation or common suppliers. Lagging the peer measure does not by itself separate imitation from shared conditions that persist over time.",
        "(b) The design separates imitation from selection into peer groups.",
        "(c) Where the paper's own regressor may respond to the same shared conditions, the design addresses that too."
      ],
      "applied_when": "Per bs:GR1. A failure statement names the measure and which of (a)-(c) is not met. Condition (c) is where this standard meets std:12.",
      "provenance": "The elicitor's suggestion, prompted by bs:EB.N3, which the reviewer rewrote to cut both ways and accepted as a standard for any peer-effects paper (rv2:std:14). The sentence in (a) on lagging was added in rv3:std:14; the reviewer notes that the brief reports a lagged peer measure here and keeps the sentence as a general point. Citation: Manski 1993, reflection problem (to verify)."
    },
    {
      "id": "std:15",
      "title": "Problems to solve, not gotchas (a standard for the draft)",
      "dimension": "PRA",
      "parameters": ["PRA.5"],
      "priority": "must",
      "origin": "reviewer",
      "applies_to": "The reviewer's draft, not the paper. It carries no weight (bs:GR2).",
      "conditions": [
        "For each fatal or damaging objection: (a) the draft says where the reviewer may be wrong; (b) it proposes at least one test or analysis whose result the reviewer does not know; (c) it says in advance what result would change the reviewer's view; (d) it names the repair that would change the recommendation.",
        "For every objection: (e) the draft labels it as decisive (fatal or damaging) or as fixable or minor.",
        "Once per draft: (f) the draft says what in the paper survives the criticisms, and what would be lost if it were not published."
      ],
      "applied_when": "Conditions (a)-(e) appear for each objection they cover, and (f) appears once.",
      "mode_c": "Reviewer's request: check (f) (rv2 general note).",
      "provenance": "rv1:S1.1; rv1 excerpt; rv1:S1.2. Clause (e) is the elicitor's, accepted (rv2:std:15). rv2:std:15 adds (f); rv3:Q8 sets which objections need (a)-(d)."
    },
    {
      "id": "std:16",
      "title": "Readable by non-economists; rival recognisable",
      "dimension": "PRA",
      "parameters": ["PRA.1"],
      "priority": "should; first to shed (bs:GR4, step 1)",
      "origin": "reviewer",
      "applies_to": "The statement of the model, and the description of the rival.",
      "conditions": [
        "(a) Each assumption of the model, and what drives each prediction, is stated in words alongside the formal statement. A reader without economics training could say, from the words alone, why each prediction has its sign.",
        "(b) The rival is described in terms its proponents would recognise. The reviewer's view is provisional, and the reviewer defers to the second reviewer."
      ],
      "applied_when": "Per bs:GR1. A failure statement names any assumption or prediction that has no statement in words. The draft's view on (b) is marked as deferring.",
      "provenance": "rv1:EB.2; bs:EB.N4; rv2:std:16."
    }
  ],
  "tensions": [
    {
      "id": "bs:T1",
      "between": ["std:1", "std:2"],
      "pull": "Under std:1, a hypothesis that is not derived counts neither for nor against the theory. That can shield the theory from std:2, so that the less carefully a hypothesis is derived, the less its failure costs.",
      "resolution": "The reviewer's own rule. A failure counts against the model as the paper states it (std:2). It does not count against a broader theory that does not entail the prediction (std:1). Under-derivation is itself a must failure under std:1, so nothing is rewarded. A repaired derivation that flips the sign after the result is known is a rescue under std:2(d).",
      "ranking": "No overall ranking: std:2 governs for the model as stated, and std:1 governs for the broader theory.",
      "status": "resolved",
      "source": "rv3:T1"
    },
    {
      "id": "bs:T2",
      "between": ["std:3(c)", "std:12(c)", "std:14", "std:16(b) and the division of labour in bs:EB"],
      "pull": "Several standards require judgements about the rival, yet the reviewer defers to the second reviewer on the rival's content.",
      "resolution": "Split by standard. On std:14 the reviewer gives their own verdict, since it needs only the rival's minimal claim. On std:3(c) the reviewer judges provisionally: the draft states the definition used, cites its literature, and flags a question for the second reviewer. On std:12(c) the draft gives no verdict that an account is unfalsifiable; the point goes to the editor as a question for the second reviewer.",
      "ranking": "Deferral governs std:3(c) and std:12(c). The reviewer's own judgement governs std:14.",
      "status": "resolved",
      "source": "rv3:T2"
    },
    {
      "id": "bs:T3",
      "between": ["std:10", "std:13", "std:4"],
      "pull": "A pre-trend check is itself a claim of absence. The reviewer's past criterion ('if the leads are flat') relied on non-significance.",
      "resolution": "Option (a). The intervals on the leads must exclude pre-trends large enough to matter; otherwise a sensitivity analysis of the Rambachan and Roth kind is required. The reviewer's criterion becomes 'flat and precise'.",
      "ranking": "std:13 governs the leads and is raised to must for them.",
      "status": "resolved",
      "source": "rv3:T3"
    },
    {
      "id": "bs:T4",
      "between": ["std:12", "PRA.2 (higher burden of evidence)"],
      "pull": "Attaching a higher burden to whatever the audience takes for granted is asymmetric when the audience is dual.",
      "resolution": "Option (a). Symmetry governs the evidence. The higher burden attaches to the form of a claim ('rules out', 'overturns'), whichever account it targets. PRA.2 is restated accordingly.",
      "ranking": "std:12 governs.",
      "status": "resolved",
      "source": "rv3:T4"
    },
    {
      "id": "bs:T5",
      "between": ["bs:EB.ann5 (one sentence on survival selection)", "std:10(c),(d)"],
      "pull": "If survival selection is a first-order threat to identification, std:10 calls for more than one sentence.",
      "resolution": "Option (b), with a definition of 'first-order' (see std:10, survival_selection_rule). If the reviewer goes past one sentence, the draft includes a short note to the editor saying why. Representativeness is not discussed.",
      "ranking": "std:10 governs when the threat is first-order; otherwise the one-sentence cap governs.",
      "status": "resolved",
      "source": "rv3:T5"
    },
    {
      "id": "bs:T6",
      "between": ["priority (must)", "dimension weights"],
      "pull": "Must standards sit on lower-weight dimensions (std:15 on PRA; std:5, std:6, std:9 on TEC).",
      "resolution": "Confirmed, with corrections; now bs:GR2. 'Must' means the standard must be applied; the weight says how much a failure moves the recommendation. TEC findings are booked where their consequence lands. Standards for the draft carry no weight. Over-claiming is booked under INF and EPI.",
      "ranking": "Not a ranking; a rule of interpretation.",
      "status": "resolved",
      "source": "rv3:T6"
    },
    {
      "id": "bs:T7",
      "between": ["bs:GR4 (shedding order)", "the must clause of std:8", "std:7 for controls that carry identifying weight"],
      "pull": "The shedding order sheds std:8 second and std:7 beyond the main variables third. But std:8 is must where efficiency is the paper's conclusion, and std:7 is must for controls that carry identifying weight (ONT.4: strict). Shedding would remove must parts.",
      "resolution": null,
      "default_for_mode_c": "Until the reviewer decides, Mode C lists a shed must part under silent skips, marked 'declared shedding (bs:GR4)', so that it is visible but kept apart from undeclared skips.",
      "status": "open: reviewer to decide",
      "source": "Identified by the elicitor in assembling this specification, from rv3:5 and rv3:std:7, std:8."
    }
  ],
  "mode_c_checks_requested_by_reviewer": [
    "std:5: the re-derivation was done, including the check that proofs use only stated assumptions (rv2:std:5).",
    "std:12: both halves of the bias, (b) and (c), and the wording symmetry in (d) (rv2 general note; rv3:std:12).",
    "std:15(f): the draft says what survives (rv2 general note).",
    "bs:EB.ann5 and bs:T5: survival selection gets one sentence, or a first-order treatment with a note to the editor (rv2:ann5; rv3:T5)."
  ],
  "editorBrief": {
    "type": "EditorBrief",
    "id": "bs:EB",
    "status": "final, with reviewer annotations",
    "fills": "PRA.6",
    "precedence": "The editor's answers (ed:E1-E4) and corrections take precedence over inv:note.",
    "basis_caveat": "Statements about the manuscript's content are the editor's report. Neither the elicitor nor the reviewer has checked them (bs:GR5).",
    "contribution_ranking": [
      { "rank": 1, "ids": ["bs:C1", "bs:C2"], "question": "Does the model predict what is tested, and does the test find it?", "editor_view": "The modularity mechanism is the most interesting part of the paper and is what would make it publishable; the editor is not confident the model and the empirics connect.", "source": "ed:E1 item 1" },
      { "rank": 2, "ids": ["bs:C3", "bs:C4"], "treatment": "merged", "editor_view": "C3 is the headline and the paper's main selling point. It is the claim the editor is least sure the evidence supports.", "source": "ed:E1 preamble and item 2" },
      { "rank": 3, "ids": ["bs:C2"], "treatment": "on its own", "editor_view": "The 11-year balanced panel of 412 hospitals is unusually long. The regularity has value even if the theory and the adjudication need work.", "source": "ed:E1 item 3" },
      { "rank": 4, "ids": ["bs:C5"], "treatment": "low priority", "editor_view": "Flag an earlier study if the reviewer knows one; no literature search.", "source": "ed:E1 item 4" }
    ],
    "needs": [
      { "id": "bs:EB.N1", "need": "Re-derive the model: check that both propositions, including the uncertainty interaction, follow from the stated assumptions (editor-reported loci: sections 2.2-2.3, Appendix).", "source": "ed:E2" },
      { "id": "bs:EB.N2", "need": "Give a reasoned reading of the identification (fixed effects, controls, the event study in the robustness paragraph), with spot checks of Table 2 and the text. No re-running.", "source": "ed:E2, ed:E4" },
      { "id": "bs:EB.N3", "need": "Judge whether the empirical test of the rival (H3) is a fair one, as a question of design.", "source": "ed:E2" },
      { "id": "bs:EB.N4", "need": "Say whether a sociologist of organizations would find the model and the claims clear and fair, not only whether an economist would find them correct.", "source": "ed:E4" },
      { "id": "bs:EB.N5", "need": "On the hospital IT setting, flag anything obvious, but do not go looking.", "source": "ed:E2" },
      { "id": "bs:EB.N6", "need": "On the priority claim (bs:C5), flag an earlier study if known; no search.", "source": "ed:E1 item 4" }
    ],
    "concerns": [
      { "id": "bs:EB.K1", "concern": "Do the model and the empirics connect? (C1, C2)", "editor_reports": ["The model gives an outsourcing threshold for individual functions, but the outcome measured is a share of spending.", "H2 predicts a stronger modularity effect under high uncertainty. Table 2 (Model 3) shows a negative interaction, which the authors call 'contrary to H2'. Section 5 explains it with something outside the model."], "editor_question": "Is this a failed prediction, a problem in the model, or a problem in the test?", "source": "ed:E3 item 1" },
      { "id": "bs:EB.K2", "concern": "Is the dismissal of the institutional account fair? (C3, C4, and the 'rule out' wording in the abstract and section 5)", "editor_reports": ["Mimicry is tested with a single measure: the lagged mean outsourcing of other sample hospitals in the same state (section 3.2).", "A peer coefficient that loses significance once modularity is added is not obviously enough to rule anything out.", "Section 5 explains the H2 result with legitimacy pressures, an institutional mechanism."], "scope": "This reviewer covers the evidence side; institutional theory on its own terms goes to the second reviewer.", "source": "ed:E3 item 2" }
    ],
    "audience": { "PRA.1": "Generalist organization-science readership, both economists and sociologists of organizations.", "round": "First round, original submission.", "source": "ed:E4" },
    "process": { "code_and_data": "None supplied; reasoned reading with spot checks only.", "division_of_labour": "A second reviewer covers institutional theory.", "source": "ed:E2, ed:E4" },
    "settled": ["The question matters.", "The mechanism deserves to be taken seriously.", "The long balanced panel is an asset. The authors acknowledge in section 5.2 that requiring a response every year may skew the sample (editor-reported); no further effort is requested.", "C5 needs little effort."],
    "out_of_scope": ["Institutional theory on its own terms (second reviewer).", "A literature search for an earlier adjudicating study.", "Re-running analyses.", "Investigating the hospital IT setting beyond obvious points."],
    "reviewer_annotations": [
      { "id": "bs:EB.ann1", "note": "The reviewer accepts the scope and depth on the editor's authority. Their request to see the editor's full answers was declined under the protocol; the reviewer works from bs:EB and treats its statements about the manuscript as the editor's report, unchecked.", "source": "rv1:EB.1; rv2:ann1; rv3 preamble" },
      { "id": "bs:EB.ann2", "note": "On N4, the reviewer judges whether a non-economist can follow the model, and defers to the second reviewer on whether the rival is recognisable (std:16).", "source": "rv1:EB.2" },
      { "id": "bs:EB.ann3", "note": "On N3, the reviewer takes the rival's prediction as its literature usually states it and judges the design against it (std:3).", "source": "rv1:EB.3" },
      { "id": "bs:EB.ann4", "note": "Rank 1 is whether the model connects to the test; rank 3 is the panel regularity as a finding in its own right. Confirmed.", "source": "rv1:EB.4" },
      { "id": "bs:EB.ann5", "note": "Survival selection gets one sentence, unless it is first-order for identification; then it gets a short note to the editor (bs:T5). Representativeness is not discussed.", "source": "rv1:EB.5; rv3:T5" },
      { "id": "bs:EB.ann6", "note": "The reviewer re-derives and spot-checks. Under time pressure they cut N6, then N5, then N4, never N1-N3; this is consistent with bs:GR4.", "source": "rv1:depth; rv3:5" }
    ]
  },
  "citations_to_verify": [
    "Davis (1971), 'That's Interesting!', Philosophy of the Social Sciences (the reviewer's recollection agrees)",
    "Williamson (1985), on the transaction as the unit of analysis (the reviewer's recollection agrees)",
    "Manski (1993), the reflection problem, Review of Economic Studies (the reviewer's recollection agrees)",
    "Callaway and Sant'Anna (2021), Journal of Econometrics (the reviewer's recollection agrees)",
    "Sun and Abraham (2021), Journal of Econometrics (the reviewer's recollection agrees)",
    "Roth (2022), on pre-testing for parallel trends (from the reviewer's memory)",
    "Rambachan and Roth (2023), sensitivity to violations of parallel trends (from the reviewer's memory)"
  ],
  "decisions_for_reviewer": [
    "bs:T7: allow shedding of the must parts of std:7 and std:8, with Mode C reporting them as declared shedding; or exempt those parts from shedding.",
    "Confirm two recording choices: 'argue each time' is stored as neutral with a challenge (INF.2), and 'a derived implication, credibly tested' is stored as an extension of the PRA.2 values.",
    "Confirm the specification as final, or correct any item, before drafting."
  ]
}
```

## (b) Your standards in brief

This is a specification of your standards, not a review. It records what you told me in Rounds 1 to 3. The JSON above is the authoritative version, and Mode C will compare your draft with it.

**Weights.** Inferential 0.9 · Epistemological 0.9 · Technical 0.7 · Ontological 0.6 · Pragmatic 0.4.

"Must" means a standard has to be applied in your draft. The weight says how much a failure moves your recommendation (`bs:GR2`). Technical findings count on the dimension where their consequence lands.

**Your perspective in brief.**
- **Inferential.** Hypotheses that test a theory must be derived from it: at least a sketch, with every assumption that fixes a sign stated. You have low tolerance for unstated premises, and you prefer depth to coverage. Rivals must be stated as their proponents would state them, and tested where the two accounts differ. Explanations found after the results are in must be labelled, and they never count as support.
- **Epistemological.** You are a realist and a sophisticated falsificationist (Lakatos). You prefer design-based identification and put high weight on novel prediction. Effect sizes and intervals count for more than significance stars. You don't expect pre-registration for archival panels, but you do expect the paper to say how it chose its main specification.
- **Technical.** You re-derive models and spot-check numbers. With staggered adoption, you expect estimators robust to differences across cohorts. Standard errors must be clustered at the level where the key regressors vary. You prefer a closed-form model. Code and data are preferred, and you ask for them at revision.
- **Ontological.** Actors are boundedly rational and capable of opportunism. Institutional entities are admitted if they yield predictions. Cross-level arguments need an explicit bridge. Measurement must be strict for the main variables, the rival's construct, and any control that carries identifying weight. Functional explanations need a mechanism.
- **Pragmatic.** The audience is both economists and sociologists. The best contribution is a derived implication, credibly tested. "Rules out" and "overturns" carry a higher burden, whichever account they target. Implications for practice are not a criterion.
- **Field-specific inferences.**
  - Endorse: MI1, hold-up and hierarchy (as theory only); MI6, fixed effects identify a causal effect (only as a conditional).
  - Reject: MI7, a lost star means no effect.
  - Argue each time: MI2, MI3, MI4, MI8 and MI9.
  - Neutral: MI5 and MI10.

**The 16 standards**

| | Standard | Priority |
|---|---|---|
| `std:1` | Hypotheses are derived at the level and on the scale tested; no "as if" defence for the assumption that does the work | must |
| `std:2` | Failed predictions are reported as results everywhere, including the abstract; rescues after the fact are costs; "fails" is defined by sign and interval | must |
| `std:3` | Ruling out a rival needs a discriminating test, with the rival measured in a way its proponents would accept; a reinterpretation of the rival's evidence needs a new prediction; (g) the paper's own mechanism gets a specific implication | must; (g) should |
| `std:4` | A lost significance star is not a null result: collinearity, measurement error and mediation are tested or specifically ruled out | must |
| `std:5` | Re-derive each proposition by hand; check that proofs use only stated assumptions; the harness runs after the draft | must |
| `std:6` | Spot-check the numbers, with at least the minimum set from `bs:Q2` | must (minimum set) |
| `std:7` | Measures fit their constructs; no correlation by construction; the link from adoption to use is argued | must |
| `std:8` | Efficiency claims show selection; functional claims name their mechanism; an ambiguous "economizing" is read as an efficiency claim | should; must where efficiency is the conclusion |
| `std:9` | Clustering at the level of variation; a small-cluster correction below 50 clusters, or when clusters are lopsided | must |
| `std:10` | Find the source of identifying variation; an event study robust to cohort differences; leads that are "flat and precise", or a sensitivity analysis; the choice of main specification disclosed | must |
| `std:11` | The direction of causation is argued, with a reason specific to the setting that can be checked, or it is identified | must |
| `std:12` | Symmetry in your draft: the same bar for both accounts; no verdict that an account is unfalsifiable (put it to the editor instead); wording checked both ways | must (draft) |
| `std:13` | Claims of absence need bounds; you may propose the smallest effect that matters, fixed in advance | should; must for leads |
| `std:14` | Peer influence is separated from shared conditions and from selection into peer groups; a lag alone does not do this | should |
| `std:15` | Problems to solve: say where you may be wrong, propose a test whose result you don't know, say in advance what would persuade you, name the repair, label each problem; say what survives | must (draft) |
| `std:16` | The model can be followed in words by a non-economist; the rival is recognisable (you defer on this) | should |

**How the tensions were resolved**
- **`bs:T1`, derivation versus failed predictions.** A failure counts against the model as stated, not against a broader theory that doesn't entail the prediction. Under-derivation is itself a must failure. A repaired derivation that flips the sign after the fact counts as a rescue.
- **`bs:T2`, judging the rival versus deferring.**
  - On peer-effects identification (`std:14`), you give your own verdict.
  - On the rival's construct (`std:3` c), you give a provisional judgement, with its source cited, and flag it for the second reviewer.
  - On whether an institutional account is unfalsifiable (`std:12` c), you give no verdict; you put the question to the editor.
- **`bs:T3`, pre-trends.** The intervals on the leads must exclude pre-trends large enough to matter; otherwise the paper needs a sensitivity analysis. `std:13` is must for leads.
- **`bs:T4`, symmetry versus the higher burden.** The higher burden attaches to the form of the claim, for either account.
- **`bs:T5`, survival selection.** One sentence, unless it is first-order: that is, survival is linked to changes (not levels) in the regressor and outcome, and could produce an estimate of the reported size. If it is first-order, you add a short note to the editor.
- **`bs:T6`, priority versus weight.** Confirmed, together with the rule on where findings count (`bs:GR2`).

**Working rules**
- Failures go in the body of the draft. Passes go in a "Checks run" list of under 150 words. If the paper lacks an input a check needs, you ask for it (`bs:GR1`).
- Derivations and computations in the draft are done by hand. The harness runs afterwards, with the parameter domain and your transcription of the paper's model shown (`bs:GR3`).
- If time runs short, you shed standards in the order set in `bs:GR4`.

**One point still open: `bs:T7`.**
- **The conflict.** Your shedding order sheds `std:8` second, and `std:7`'s controls clause third. But `std:8` is must where efficiency is the paper's conclusion, and `std:7`'s must covers controls that carry identifying weight. Shedding them would drop must parts.
- **Why it may matter here.** The invitation's abstract uses "economizing" in a concluding sentence (sentence 7). Under your `bs:Q4` rule, an ambiguous use is read as an efficiency claim, which would make `std:8` must. I make no judgement on how that sentence reads.
- **Until you decide.** Mode C will list a shed must part under silent skips, marked "declared shedding".

**Decisions for the reviewer**
- **`bs:T7`.** Either allow shedding of the must parts of `std:7` and `std:8`, with Mode C reporting them as declared shedding, or exempt those parts from shedding.
- **Two recording choices.** Please confirm both:
  - "argue each time" is stored as neutral with a challenge, in the stances on field-specific inferences;
  - "a derived implication, credibly tested" is stored as an extension of the listed contribution values.
- **The specification as a whole.** Confirm it as final, or correct any item before you draft.
