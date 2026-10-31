**Best-Self Elicitor: final editor brief (`bs:EB`) and Mode S, Round 1** (Reviewership v0.1)

## (a) Editor brief `bs:EB`

How the sources are cited:
- `inv:note` is the editor's note in the invitation.
- `ed:E1`–`ed:E4` are the editor's answers to `bs:E0` (turn 2). The editor says these answers take precedence over the note.

The elicitor has not read the manuscript. Every statement in the brief about the manuscript's content is the editor's, cited to `ed:…`, and has not been checked. The `parameters_at_stake` and `catalogue_entries_at_stake` fields are the elicitor's mapping onto the perspective dimensions. They are not findings.

```json
{
  "type": "EditorBrief",
  "id": "bs:EB",
  "status": "final",
  "instruction_set": "Reviewership v0.1",
  "fills": "PRA.6",
  "sources": {
    "inv:note": "Editor's note in the review invitation",
    "ed:E1": "Editor's answer on main contribution",
    "ed:E2": "Editor's answer on why this reviewer and how deep to go",
    "ed:E3": "Editor's answer on own concerns, including what is settled",
    "ed:E4": "Editor's answer on journal and process",
    "ed:EB-corr": "Editor's corrections to the draft bs:EB"
  },
  "precedence": "ed:E1-E4 and ed:EB-corr take precedence over inv:note (editor's statement, ed preamble).",
  "basis_caveat": "Statements about the manuscript's content are reported by the editor and have not been checked by the elicitor, who has not read the manuscript.",
  "contribution_ranking": [
    {
      "rank": 1,
      "ids": ["bs:C1", "bs:C2"],
      "treatment": "merged into one question",
      "question": "Does the model predict what is tested, and does the test find it?",
      "editor_view": "The modularity mechanism is the most interesting thing in the paper and is what would make it publishable; the editor is not confident the model and the empirics connect.",
      "source": "ed:E1 item 1"
    },
    {
      "rank": 2,
      "ids": ["bs:C3", "bs:C4"],
      "treatment": "merged (C4 is the broader version of C3)",
      "editor_view": "C3 is the paper's main selling point and its headline, as the title shows; it is the claim the editor is least sure the evidence supports.",
      "source": "ed:E1 preamble and item 2"
    },
    {
      "rank": 3,
      "ids": ["bs:C2"],
      "treatment": "on its own",
      "editor_view": "The balanced panel (412 hospitals, 11 years) is unusually long; the regularity has value even if the theory and the adjudication need work.",
      "source": "ed:E1 item 3"
    },
    {
      "rank": 4,
      "ids": ["bs:C5"],
      "treatment": "low priority",
      "editor_view": "Flag an earlier study that does this if the reviewer knows of one; do not search the literature.",
      "source": "ed:E1 item 4"
    }
  ],
  "needs": [
    {
      "id": "bs:EB.N1",
      "need": "Re-derive the model: check that both propositions, including the uncertainty interaction, follow from the stated assumptions.",
      "depth": "re-derive",
      "editor_reported_loci": ["§2.2-2.3 (model, about one page)", "Appendix (short proofs)"],
      "parameters_at_stake": ["TEC.2", "TEC.5", "INF.3"],
      "source": "ed:E2 (Model), ed:EB-corr"
    },
    {
      "id": "bs:EB.N2",
      "need": "Give a reasoned reading of the identification (fixed effects, controls, and the event study described in the robustness paragraph), and spot-check the numbers in Table 2 and the text.",
      "depth": "reasoned reading plus spot checks; no re-running (no code or data supplied)",
      "editor_reported_loci": ["Table 2", "robustness paragraph (event study)"],
      "parameters_at_stake": ["EPI.3", "TEC.3", "TEC.4", "TEC.2"],
      "source": "ed:E2 (Empirics), ed:E4, ed:EB-corr"
    },
    {
      "id": "bs:EB.N3",
      "need": "Judge whether the empirical test of the rival (H3) is a fair one, as a question of design.",
      "parameters_at_stake": ["INF.7", "EPI.3", "EPI.6", "ONT.4"],
      "source": "ed:E2, ed:EB-corr"
    },
    {
      "id": "bs:EB.N4",
      "need": "Say whether a sociologist of organizations would find the model and the claims clear and fair, not only whether an economist would find them correct.",
      "parameters_at_stake": ["PRA.1", "PRA.5"],
      "source": "ed:E4"
    },
    {
      "id": "bs:EB.N5",
      "need": "Hospital IT setting: flag anything obvious, but do not go looking (no one is specifically covering it).",
      "depth": "flag only",
      "source": "ed:E2 (Hospital IT setting)"
    },
    {
      "id": "bs:EB.N6",
      "need": "Priority claim (bs:C5): flag an earlier study that adjudicates the same question if the reviewer knows of one; no literature search.",
      "depth": "flag only",
      "parameters_at_stake": ["PRA.3"],
      "source": "ed:E1 item 4"
    }
  ],
  "concerns": [
    {
      "id": "bs:EB.K1",
      "concern": "Do the model and the empirics connect? (bs:C1, bs:C2)",
      "scope": "theory and evidence together",
      "editor_reports": [
        "The model gives an outsourcing threshold for individual functions, but the outcome measured is a share of spending.",
        "H2 predicts a stronger modularity effect when uncertainty is high; Table 2 (Model 3) shows a negative interaction, which the authors call 'contrary to H2'.",
        "§5 explains the H2 result with something outside the model."
      ],
      "editor_question": "Is the H2 result a failed prediction, a problem in the model, or a problem in the test?",
      "parameters_at_stake": ["ONT.2", "ONT.4", "INF.3", "TEC.5", "EPI.2", "EPI.4", "INF.1"],
      "catalogue_entries_at_stake": ["MI1", "MI8"],
      "source": "ed:E3 item 1"
    },
    {
      "id": "bs:EB.K2",
      "concern": "Is the dismissal of the institutional account fair? (bs:C3, bs:C4, and the 'rule out' wording in the abstract and §5)",
      "scope": "evidence side for this reviewer; institutional theory on its own terms goes to the second reviewer",
      "facets": [
        {
          "facet": "representation of the rival",
          "editor_reports": "Mimicry is tested with a single measure: the lagged mean outsourcing of other sample hospitals in the same state (§3.2).",
          "parameters_at_stake": ["INF.7", "EPI.6", "ONT.4"]
        },
        {
          "facet": "evidence",
          "editor_reports": "A peer coefficient that loses significance once modularity is added is not obviously enough to rule anything out.",
          "parameters_at_stake": ["EPI.2", "EPI.5"],
          "catalogue_entries_at_stake": ["MI7", "MI3"]
        },
        {
          "facet": "wording",
          "editor_reports": "'Rule out' wording in the abstract and §5.",
          "parameters_at_stake": ["PRA.5"]
        },
        {
          "facet": "internal tension",
          "editor_reports": "§5 explains the H2 result with legitimacy pressures, an institutional mechanism, in a paper that claims to have ruled that account out.",
          "parameters_at_stake": ["INF.1", "EPI.4"],
          "catalogue_entries_at_stake": ["MI10"]
        }
      ],
      "source": "ed:E3 item 2"
    }
  ],
  "audience": {
    "PRA.1": "Generalist organization-science readership; the paper must speak to both the economics and the sociology of organizations.",
    "round": "First round, original submission",
    "source": "ed:E4, ed:EB-corr"
  },
  "process": {
    "round": "First round; no earlier reports or response letter.",
    "code_and_data": "None supplied with the manuscript as the editor has it; reasoned reading with spot checks only. (This states what materials exist; the reviewer's own TEC.1 standard is still theirs to set.)",
    "recommendation_format_deadline": "Nothing beyond the invitation.",
    "division_of_labour": "A second reviewer covers institutional theory; this reviewer covers transaction-cost theory and panel econometrics, and the design of the test of the rival (H3).",
    "source": "ed:E2, ed:E4"
  },
  "settled": [
    {"item": "The question matters.", "source": "ed:E3 (Settled)"},
    {"item": "The mechanism deserves to be taken seriously.", "source": "ed:E3 (Settled)"},
    {"item": "The long, balanced panel is a real asset; the authors acknowledge in §5.2 that requiring a response in every year may skew the sample (editor-reported). The editor asks for no further effort here.", "source": "ed:E3 (Settled)"},
    {"item": "bs:C5 needs little effort.", "source": "ed:E3 (Settled), ed:E1 item 4"}
  ],
  "out_of_scope": [
    {"item": "Critique or defence of institutional theory on its own terms", "reason": "second reviewer", "source": "ed:E2"},
    {"item": "Literature search for an earlier adjudicating study", "source": "ed:E1 item 4"},
    {"item": "Re-running analyses", "reason": "no code or data supplied", "source": "ed:E2, ed:E4"},
    {"item": "Investigating the hospital IT setting beyond obvious points", "source": "ed:E2"}
  ],
  "elicitation_order": [
    {
      "step": 1,
      "serves": ["bs:C1+C2", "bs:EB.N1", "bs:EB.K1"],
      "dimensions": ["INF", "TEC", "ONT"],
      "parameters": ["INF.3", "TEC.2", "TEC.5", "TEC.4", "ONT.2", "ONT.4", "EPI.4", "INF.2 (MI1, MI8)"]
    },
    {
      "step": 2,
      "serves": ["bs:C3+C4", "bs:EB.N3", "bs:EB.K2"],
      "dimensions": ["EPI", "INF"],
      "parameters": ["EPI.2", "EPI.5", "EPI.6", "INF.7", "INF.1", "INF.2 (MI3, MI7, MI10)"]
    },
    {
      "step": 3,
      "serves": ["bs:C2", "bs:EB.N2"],
      "dimensions": ["EPI", "TEC"],
      "parameters": ["EPI.3", "TEC.3", "TEC.1", "INF.2 (MI6)"]
    },
    {
      "step": 4,
      "serves": ["bs:EB.N4", "bs:EB.N6", "bs:C5"],
      "dimensions": ["PRA"],
      "parameters": ["PRA.1", "PRA.2", "PRA.5", "PRA.3 (low)"]
    }
  ],
  "note": "The brief tells the reviewer what the editor needs. It does not set the reviewer's standards or weights, which are elicited in Mode S."
}
```

## (b) Mode S, Round 1 (recall): questions to the reviewer (`bs:S1`)

Dear Reviewer,

**The editor brief in short.** The full brief (`bs:EB`) is above. The editor chose you for transaction-cost theory and panel econometrics, and would like you to do four things:
- re-derive the model;
- give a reasoned reading of the identification, with spot checks of the reported numbers (no code or data were supplied);
- judge whether the empirical test of the institutional rival (H3) is a fair one;
- say whether a sociologist of organizations would find the model and the claims clear and fair.

A second reviewer covers institutional theory. If anything in `bs:EB` does not match your reading of the invitation, please say so.

**Before we draft your standards, four recall questions.**
- **Answer from past reviews, not this manuscript.** The aim is to record the standards you hold at your best before you read this paper, so that they are not fitted to it. If you have already read the manuscript, please tell me, and I will keep your reactions to it separate.
- **A few sentences each is enough.**
- **Do not identify any paper, author or journal.** You may paste anonymized excerpts from past reports if that is easier.

**bs:S1.1. Your proudest review.** Which review are you proudest of, and what made it good? You might mention what you checked, what you caught, how you put it to the authors, and what came of it.

**bs:S1.2. A rejection.** Think of a paper you recommended rejecting. What was the decisive reason, the one whose repair would have changed your recommendation?

**bs:S1.3. Checks you skip under time pressure.** Which checks do you perform "on a good day" but skip when time is short? Some examples:
- re-deriving a proof;
- recomputing a statistic from the reported coefficients and standard errors;
- reading the appendix;
- checking that each measure matches its construct;
- checking a priority claim.

**bs:S1.4. Your home tradition.** What is your home tradition? Which of its commitments should a paper be challenged on, rather than allowed to take for granted, including when the paper is written from within that tradition? Please answer in your own words. If an entry in the workbench catalogue of material inferences (MI1–MI10) captures what you mean, name it, and say whether you endorse it, reject it, or think it must be argued for each time.

**What happens next.** In Round 2 I will draft:
- a candidate setting for each of the five dimensions;
- 10 to 16 candidate standards, each tied to the words of yours that suggested it;
- for each dimension, at most two further standards of my own, clearly marked as my suggestions.

You will accept, reject or rewrite each one and set the five weights. The order will follow `bs:EB.elicitation_order`.

**Decisions for the reviewer**
- Does `bs:EB` match your reading of the invitation? Correct it if not.
- If you have already read the manuscript, say so, so that your reactions to it are kept apart from your recalled standards.
- Optionally, share anonymized excerpts from past reports. I will use them to propose standards in Round 2.
