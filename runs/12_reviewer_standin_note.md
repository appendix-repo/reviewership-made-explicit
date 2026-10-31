# Run 12: stand-in reviewer's note to the orchestrator (out of role)

This note is not part of the review. It covers the four questions run12.md asks.

**Process.** I read only the permitted files. I listed the check folders with a single `ls` and read some check outputs and scripts there (`10_checks/p10_chk_1.out.txt` and `.py`). I located ids with search tools. I ran no code and did not use the web. The disposition counts are 74 accept, 35 modify and 8 reject, across 117 entries.

## 1. Where a human reviewer would probably have decided differently

- **Severity of Major 2.** The draft rated it damaging. I moved it to "fatal to the adjudication claim as worded". The reasons I gave are the editor brief's headline ranking and the demonstrated non-discrimination. But the move also tracks three simulated lenses and two probes that point the same way, and the panel itself warns that its simulators are correlated. A human anchored on their draft, or close to R-TCE, might well have kept "damaging" and simply made the call explicit, as bs:CI4 suggested.
- **Corroboration (pnl:dis:3).** I held the draft's line by applying the std:2 scope rule verbatim: a sign repaired after the result is a rescue. A human might not remember their own rule word for word, and could be moved by R-BEH's point that the sign follows from A3, which was stated in advance.
- **The rise in p10:fnd:10's severity.** I declined it after reading the check script and seeing that its grid kept k* at 0.34 or above. A human would probably either have accepted the raised severity or skipped the point altogether.
- **Coverage.** A human with an hour or two would read Section 6 of the panel synthesis and the probes' ranked lists, take the top findings, and leave the rest. Several small additions I kept would probably have been dropped:
  - the u domain;
  - m = 1;
  - pooled SDs;
  - the omitted-variable inference on the specificity coefficient;
  - the function-level separation in pnl:dis:15.
- **Machine checks.** Some humans would be reluctant to tell the authors that machine checks were run, or would instead cite simulation numbers that I left out.
- **Literature.** A human with library access could have verified Loh & Venkatraman (1992) and Ang & Cummings (1997) in minutes. I could not, so both stay "to verify". I also added Loh & Venkatraman from my own recall. That recall is not independent of the simulators' recall, since we are the same model family.

## 2. What I could not have done in a human's time

- I read the consistency check, the panel synthesis (about 640 lines), three probes (up to about 1,000 lines each), the findings blocks of four simulated reviews, and one check script. I then reconciled ids and severities across all of them. That is several hours of reading for a human.
- I wrote 117 dispositions, each with a one-line reason and a landing place.
- I checked my own reasoning against the scripts, for example the parameter grid behind p10's Beta(2,5) result.

## 3. Accepted findings I could not have assessed without the harness

- **p10:fnd:2 (p10:chk:4).** Without the simulation, I could argue that the pattern arises under imitative diffusion of interfaces, but not demonstrate it. The finding's status rests on the simulation and on my accepting its added premise.
- **p09:fnd:11.** That persistent state shocks can produce a peer coefficient of Table 2's size is a magnitude claim. The review states it only qualitatively.
- **p09:fnd:5 / p10:fnd:6.** That the staffing control can raise or lower the coefficient follows from logic. That this happens under the manuscript's own relations comes from the simulation.
- **p09:fnd:8.** That modest feedback alone could match the estimate is a simulation result. I put the premise to the authors as a question.
- **p08:fnd:5.** "Not significant under any covariance" (max |z| = 1.65) is a bound I would not have computed by hand.
- **p09:fnd:10.** The rejection rates under hospital and state clustering are simulation results, though the direction is standard.

The P2 derivation, N, the stars, the interval and equivalence bounds, and the Φ-scale sign condition I had done, or could do, by hand. For those, the harness confirmed my results rather than enabling them.

## 4. What made the decisions harder than they needed to be

- **No cross-walk of ids.** One defect carries up to seven ids across the panel, the four simulated reviews and three probes, with different severities and statuses. p10's "cross-type" findings duplicate p08 and p09. The panel's agreement table helps, but it does not cover the probes.
- **Severity disagreement explained only in a script.** p08 keeps the Φ-scale reversal fixable (fnd:4), while p10 raises the same point to damaging (fnd:10). The reason is that p10's grid kept k* high, and that was visible only in the script, not in either output's text.
- **Overlapping decision lists.** Part 1 and Part 2 decision lists overlap and are renumbered, with pointers such as "still open from Part 1". p10 uses decision ids (`p10:dec:n`); p08, p09, the panel and Mode C use unnumbered lists. Mode C's numbered Decisions repeat its own CS, CU and CI items.
- **Vocabulary that fits findings, not choices.** Accept, reject and modify suit findings. They fit poorly for:
  - choices between options, such as fatal versus damaging, or credit versus discount;
  - process items, such as "run the checks" or "alignment".

  The rule that an accepted item must land in the review has no slot for process decisions. I used "Process only (no review text)".
- **Conflicting severity conventions.** Probes and the panel use scoped labels ("fatal to the adjudication claim, not to H1"), while Mode C asks for one label per concern. The two had to be reconciled by hand.
- **Status labels that bundle conditions.** Labels such as "demonstrated, conditional on p10:dec:6" or "demonstrated with a caveat" push the reviewer to judge the premise of a simulation. That is fair, but it is hidden work.
- **Size.** Token limits forced chunked reads of the longer outputs, and two passes over some files.
