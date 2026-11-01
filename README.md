# Reviewership Made Explicit: replication repository

This repository accompanies the Stage 1 proposal *Reviewership Made Explicit* (Organization Science Special Issue: AI-Enabled Frontiers in Organizational Science) and its technical appendix, `docs/REVIEWERSHIP_TECHNICAL_APPENDIX.md`. It holds every file the appendix refers to (`instruction-sets/`, `schema/`, `case/`, `runs/`, `tools/`, `governance/`, `lakatos/`) exactly as the appendix describes them, together with code that recomputes every quantitative result in the appendix from those files.

*It is anonymized for review. Author names, affiliations and the hosting institution are withheld; "[institution]" in the documents stands for the latter.*

## Quick start

```bash
python3 -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
python replication/replicate_all.py          # about two minutes
```

The script prints a summary and writes `replication/REPLICATION_REPORT.md` (one row per result: the appendix's value, the recomputed value, the script, PASS / FAIL / NOTE) and `replication/results.json`. It exits non-zero if anything fails. The same command runs on every push in `.github/workflows/replicate.yml`.

Expected outcome with the pinned versions: **173 results, 164 PASS, 0 FAIL, 9 NOTE**. The NOTEs are explained under [Known discrepancies](#known-discrepancies).

## What can be replicated, and what cannot

The demonstration in Section 4 of the appendix consists of **model runs** (Claude agent instances playing the four roles and the two human stand-ins, each run once) and **deterministic computations** on their outputs (the check harness, the distance tool, the provenance chain, the machine-origin share, the editor view, the stylistic profile, the power calculations).

| | Status in this repository |
|---|---|
| Every deterministic result in the appendix | **Recomputed** by `replication/` from the files in the repository, and compared with the value the appendix prints |
| The 37 executable checks the roles wrote | **Re-run** in the harness's sandbox; all 37 reproduce their recorded output byte for byte (simulations fix their own seeds). The harness itself is also re-run on the transcripts and re-extracts the same 37 checks |
| That the record was fixed when the appendix says it was | **Verified** by hash: the Annex C manifest, the case hashes recorded before any run, every content hash in the provenance trace (including each probe's Part 1, hashed before the harness ran), and the pilot's unblinding map |
| The model outputs themselves (transcripts in `runs/`) | **Not reproducible** word for word: they were single, unedited runs of a non-deterministic model. They are published as produced and hash-verified. `reexecute/` re-runs the whole protocol with fresh model calls (see below) |
| The scorers' codes (located, touched, missed; categories of unseeded weakness) | Judgments by a model instance against the sealed key; **not recomputable**. Every count the appendix derives from those codes is recomputed (`r06_recovery.py`) |
| The citation verdicts of Section 4.11 | Judgments made against the published record; the table is reproduced in the appendix and its counts are recomputed (`r08_counts.py`) |

## Where each result is reproduced

Section numbers refer to `docs/REVIEWERSHIP_TECHNICAL_APPENDIX.md`.

| Appendix | Result | Script | Underlying tool or data |
|---|---|---|---|
| §1.4 | Table of perspective distances (10 pairs × 5 dimensions, overall, opposed inferences) | `r03_perspectives_panel.py` | `tools/perspective_distance.py`; `runs/configs/*.json` |
| §1.4, §4.5 | Reversing MI6 moves the R-TCE – R-DID distance 0.114 → 0.097 (INF), 0.365 → 0.361 (overall) | `r03_perspectives_panel.py` | same |
| §4.1 | SHA-256 of the manuscript (`a8ab4709…52d0`) and the sealed key (`970e0574…809d`), recorded at `ev:1`, `ev:2` before any role ran | `r01_integrity.py` | `case/HASHES.txt`; `runs/provenance_events.json` |
| §4.2 | Turn word counts; 16 standards, 7 tensions; the focal perspective's weights and material inferences | `r08_counts.py`, `r03_perspectives_panel.py` | `runs/01_dialogue/`; `runs/configs/focal_perspective_normalized.json` |
| §4.3, §4.8 | Draft 1,567 words; signed review 3,758 (body 3,334); Flesch 48.6 vs 47.1; hedges 7.2 vs 6.4 per 1,000 | `r05_style_pilot.py` | `tools/style_metrics.py` |
| §4.4 | The four lenses' material inferences; word counts of the simulated reviews | `r03_perspectives_panel.py`, `r08_counts.py` | `runs/configs/simulated_perspectives.json` |
| §4.4–4.6, §9.3 | 37 checks (18 by the simulated reviewers, 18 by the probes, 1 by the panel), each re-run; outputs quoted in the text (e.g. "Appendix expression matches full cross-partial: False"; 74,343 draws; 0.146; 0.107; −0.063) | `r02_checks.py` | `runs/*_checks/`; `tools/harness.py` |
| §4.5, §4.12 item 14 | The harness's labeling fault (`r-tce_chk_1_b2` labeled `r-tce:chk:1`), reproduced by re-running the harness; the two checks that print nothing | `r02_checks.py` | `tools/harness.py` |
| §4.5 | Survival scores and classifications of the eight contributions; no contribution lens-dependent; Pearson r = −0.42 (p = 0.40), Spearman ρ = −0.65 (p = 0.16), n = 6; closest pair R-TCE / R-DID at 0.36; 33 agreement ids; 18 disagreement entries | `r03_perspectives_panel.py`, `r08_counts.py` | the survival table; `runs/07_checks/pnl_chk_1.*` |
| §4.6 | Probe findings (8, 12, 21) and checks (5, 9, 4); Part 1 of each probe fixed before the harness ran | `r08_counts.py`, `r01_integrity.py`, `r02_checks.py` | `runs/08_…` to `10_…` |
| §4.7 | Mode C: 7 silent skips, 4 undeclared standards, 6 consistency items; 35,792 bytes | `r08_counts.py` | `runs/11_consistency_check.md` |
| §4.8 | 117 decisions (74 accept, 35 modify, 8 reject) and the table by source | `r04_provenance_review.py` | Dispositions block of `runs/12_…` |
| §4.9 | 42 events, hash chain verified, 21 actual / 21 reconstructed, all valid against `ProvenanceEvent`; correction at `ev:35` | `r04_provenance_review.py` | `runs/provenance_events.json`; `schema/` |
| §4.9 | Machine-origin share at thresholds 0.6 / 0.4 / 0.3 / 0.2 (1.9% … 15.7%), 267 sentences, 5 machine-origin sentences; output byte-identical to `runs/14_machine_origin.json` | `r04_provenance_review.py` | `tools/machine_origin.py` |
| §4.9 | Editor view regenerated from the trace at signature (`ev:1`–`ev:39`), byte-identical to `runs/14_editor_view.md`; Major 2 and the minor concerns receive 26 findings each; 7 process-only decisions | `r04_provenance_review.py` | `tools/editor_view.py` |
| §4.10 | Recovery table (every row); 32 categories; draft 17, roles 31, roles-only 15 (48%); signed review 28 (+11); demonstration rate 4 of 4 (5 of 5 with SD8) | `r06_recovery.py` | `runs/recovery_scoring.md`, `runs/recovery_scoring_R12.md` |
| §4.11 | 54 works checked, 3 partly supported, 6 checked against an online record | `r08_counts.py` | the table in §4.11 |
| §7.9 | Pilot table: unblinding, words, hedges, nominalizations, Flesch, located / touched / missed / new / mistaken; terse style shortens reviews by 42–47%; unblinding-map hash logged at `ev:9` before scoring | `r05_style_pilot.py`, `r01_integrity.py` | `runs/13_pilot/`; `tools/style_metrics.py` |
| §8.4, §8.6 | Sample sizes 126 / 169 / 66; SE(AUC) 0.033, z ≈ 3.1; fallback MDD 0.61 (0.51 SD) and 0.53 (0.44 SD) | `r07_power.py` | `tools/power_critical_test.py` |
| Annex C | All 124 files in the manifest match their byte counts and SHA-256 prefixes | `r01_integrity.py` | |

**The proposal's main body** makes four claims about the demonstration (§3), each of which points to the appendix: that elicited standards are "sharper and more checkable than a reviewer's first statement of them" (appendix §4.2, §4.7; the transcripts in `runs/01_dialogue/` and `runs/11_consistency_check.md`), that simulated disagreements "track real theoretical fault lines" (§4.5; the counts are recomputed above), that probes locate genuine soft points "demonstrated by executed checks" (§4.6, §4.10; `r02_checks.py`, `r06_recovery.py`), and that "the current instruction sets and worked transcripts are in the accompanying repository" (`instruction-sets/`, `runs/`). The appendix (§4.0) states plainly what these runs can and cannot show: both human roles were played by model stand-ins, so the claims about human reviewers are tested in the critical test (§8), not here.

## The sealed defect key

`case/SEALED_DEFECT_KEY.md` lists the nine defects seeded in the synthetic test manuscript. It was hashed together with the manuscript before any role ran (`case/HASHES.txt`; provenance events `ev:1`, `ev:2`), and in the runs only the two scorers saw it. It is published because the appendix reproduces it (Annex B). If you want to read the manuscript or the transcripts blind, do not open the key first; `r01_integrity.py` checks that its hash is unchanged. The re-execution kit enforces the same rule: only the scorer roles can be given the key.

## Re-executing the session with fresh model calls

`reexecute/run_session.py` runs the protocol of Section 4 again, in the order of the workbench loop: the Best-Self elicitation with the editor and reviewer stand-ins (Run 01), the unassisted draft (02), the four simulated reviewers (03–06), the panel synthesis (07), the three probes with the harness between Part 1 and Part 2 (08–10), the consistency check (11), the dispositions and signed review (12), the base-model pilot with blind labels and a blind scorer (13), recovery scoring, and the machine-origin share and editor view (14). Each role is a separate model instance whose system prompt is assembled from `instruction-sets/REVIEWERSHIP_INSTRUCTION_SETS.md` (v0.1). The script enforces the information flow of §4.0 (the elicitor and the panel never receive the manuscript; only the scorers receive the key), writes every prompt and its SHA-256 before the call, logs a hash-chained provenance trace, and records any refusal as a provenance event rather than dropping the role (§4.12, item 11). It never writes into `runs/`.

```bash
python reexecute/run_session.py --dry-run --out reexecute/out/dry     # inspect every prompt; no API call
pip install -r requirements-reexecute.txt                              # then, with Anthropic credentials:
python reexecute/run_session.py --out reexecute/out/session1 [--model claude-opus-5-5] [--effort high]
```

Two cautions. The original runs used "Claude, as served on 23 October 2026"; the trace does not record a version string, so a re-execution uses whatever model you name, and its outputs will differ from the published ones. And the orchestrating session wrote each role's wrapper by hand from the instruction set; those wrappers were not saved verbatim, so the prompts here are a faithful reconstruction, not the originals. A re-execution therefore tests whether the qualitative results recur (for example, whether the probes' checks demonstrate SD1, SD2, SD3 and SD6), not whether the transcripts reproduce. The deterministic tools in `tools/` can be pointed at a new session's files in the same way the replication scripts use them.

## Repository layout

```
docs/                 Technical appendix (31 Oct 2026) and Annex C, the full transcripts in run order
case/                 Synthetic test manuscript, sealed defect key, their SHA-256 hashes
instruction-sets/     Instruction sets v0.1 for the four roles and the stand-in personas; errata and v0.2 changes
schema/               JSON Schema (draft 2020-12) and JSON-LD context, draft v0.1
runs/                 Runs 01–14 as produced: transcripts, check code and harness output, configs, provenance trace
tools/                The tools used in the runs, unchanged: harness, provenance, distance, machine origin,
                      editor view, style metrics, power calculations
governance/           Consent instruments (Annex E)
lakatos/              Project Lakatos Tables 1 to 4 (Annex D)
replication/          Scripts that recompute every result and the report they write
reexecute/            Kit to re-run the session with fresh model calls
```

The files in `runs/`, `case/` and `tools/` are kept byte-identical to what the appendix describes, faults included (the harness's labeling fault, §4.5; the check files that print nothing). Changing any of them would break the hashes in Annex C and in the provenance trace.

## Known discrepancies

`replicate_all.py` reports these as NOTE rather than FAIL.

1. **Word counts in §4.1, §4.2 and §4.4.** They were taken when the runs were made, and the appendix does not say how words were counted. A whitespace count reproduces six of the fourteen exactly and the others to within 1%, with one exception: **turn 04 of Run 01**, which the 31 October appendix gives as 2,322 words. The file has 1,751 whitespace-separated words, which is the figure the 23 October version of the appendix gave. No common counting convention yields 2,322.
2. **"The terse condition shortened reviews by 42 to 47 percent"** (§7.9). The three reductions are 42.4%, 42.5% and 47.5%; the upper bound rounds to 48 under the usual convention.
3. **"0.146"** (§4.6) is the rounded form of the harness output `mean b = 0.1458`.

One transcript (`runs/08_probe_derivation.md`, Part 2) mentions the absolute path of the folder in which the runs were made. It identifies no person, and it is left as written because the file is hash-verified.

## Environment

Verified on Python 3.13 with the versions in `requirements.txt`. The check scripts use only `numpy`, `scipy`, `sympy`, `statsmodels` and `pandas`, as the instruction set requires. The harness runs each check with `python -I` in an empty environment and a temporary working directory, with a 120-second limit. `tools/harness.py` does not itself block network access (none of the 37 checks uses the network); run it inside a sandbox without network if you add checks of your own.

## License

Code under the MIT License; text and data under CC BY 4.0. See `LICENSE`.
