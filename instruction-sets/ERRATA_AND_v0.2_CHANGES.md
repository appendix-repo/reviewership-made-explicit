# Instruction sets v0.1: errata, and changes planned for v0.2

`REVIEWERSHIP_INSTRUCTION_SETS.md` is kept exactly as the agents in the worked transcripts (appendix Section 4) received it, so that every run can be reproduced from it. Corrections and the changes the runs motivated are recorded here instead.

## Errata (wording only; no role's instructions change)

1. **Capability count.** The opening paragraph calls the gateway "capability 4". The proposal and the appendix count three reviewer-facing capabilities, served by the gateway; read "The gateway and the provenance layer are infrastructure, not agents".
2. **Table references.** "Appendix A, Table 1 to 4" refers to the Project Lakatos outline. The tables are reproduced in Annex D of the appendix and in `lakatos/LAKATOS_TABLES_1-4.md`.

## Changes planned for v0.2, from what the runs exposed (appendix Section 4.12)

1. **Editor brief in two parts.** Mode E records the editor's *needs and audience* (passed to Mode S) separately from the editor's *concerns about this manuscript* (withheld until the reviewer has drafted, then used by Mode C to check whether the draft answers the editor). In Run 01, the concerns carried findings into the elicitation.
2. **Common preamble, rule 3, scoped by role.** A simulated reviewer writes checks only where its configured TEC.2 setting says its tradition would (re-derive, re-run, re-simulate); formal checking beyond that is the probes' work. In Runs 03–06, a lens configured to spot-check re-derived the model because rule 3 told every role to.
3. **Panel composition from the scoreboard.** The default panel includes, for each material inference the manuscript's central claim relies on, at least one lens that endorses it. In Runs 03–06, all four lenses rejected MI7, so the panel could not show that fault line.
4. **Schema validation at every hand-off.** Every structured object an agent returns is validated against the schema; on failure, the agent is asked once to correct it, and any remaining coercion by the orchestrator is logged as an `annotate` event.
5. **Premises of simulation checks as reviewer decisions.** A P-ID check states its data-generating process as a numbered premise list, and the probe's disposition names which premises a "demonstrated" verdict depends on. Two checks of nearly the same claim reached different statuses in Runs 09 and 10 because their premises differed.
6. **A ranked digest.** Every role ends with its findings ranked by severity and status, deduplicated against the other roles' outputs by the panel synthesis, so that the reviewer reads a short list before the full outputs.
7. **Panel synthesis reports opposed inferences.** Alongside each pairwise perspective distance, the synthesizer receives and reports the material inferences on which the two perspectives take opposite stances, and the instruction "close perspectives" is defined (below the panel's median distance, as appendix Section 5.3 states). In Run 07, the sharpest split fell between the closest pair, on a single inference that the distance averages away.
8. **Check ids in a fixed first line.** Every check begins with a line `# check: <id>`. In Run 07, the panel synthesizer found a harness output labeled with the wrong id, taken from a comment in the code.
9. **One id per defect across roles.** The panel synthesis deduplicates across every role, probes included, and assigns each defect one id that the reviewer's dispositions use. In Run 12, one defect carried up to seven ids with different severities and statuses.
10. **One severity convention.** Every role uses the scoped label ("fatal to the adjudication claim, not to H1"), which Mode C then checks for consistency, instead of Mode C asking for one unscoped label per concern.
11. **A fuller disposition vocabulary.** Besides accept, reject and modify (for findings), the reviewer can *choose* between named options (fatal or damaging; credit or discount) and *note* a process decision that lands in no review text. Decision lists in all roles use one numbering.
12. **Contribution measured by decisions.** The editor view leads with the decision composition from the dispositions and reports the machine-origin share as a measure of wording only. In Run 14, the share was 1.9% for a review built on 109 accept or modify decisions.

## Tools (changes made or planned after the runs)

1. `tools/perspective_distance.py` now prints the opposed inferences for each pair (made after Run 07; no distance changes). 
2. `tools/harness.py` is kept as run. Planned for v0.2: take the id only from the fixed first line (change 8 above), refuse a block without one, and log a check whose output is empty as not run (two checks in Run 05 only defined functions).
3. `tools/editor_view.py`: the stand-in actor kind is matched as `stand-in`, the spelling the schema uses; pilot and scoring events are excluded from the view; a table of where accepted and modified findings land, and a warning that the machine-origin share measures wording, were added. A first rendering without these was replaced by the editor view now in `runs/14_editor_view.md`, whose hash is in provenance event `ev:41`.
