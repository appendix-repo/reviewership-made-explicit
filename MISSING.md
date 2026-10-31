# Still needed before posting (delete this file once done)

Mihnea, these are the files the appendix names that neither the appendix nor the Annex C transcripts reproduce, so they have to come from the original runs of 23 October. Each has a placeholder at its path (a `PLACEHOLDER.md` in the folder, or an entry in `runs/MISSING_FILES.md`) that says what it is and where the appendix relies on it. Please add the files exactly as produced; nothing should be rerun or regenerated.

## Instruction sets

- [ ] `instruction-sets/REVIEWERSHIP_INSTRUCTION_SETS.md` (v0.1). The most important file here: proposal §3 says the instruction sets are in this repository, and appendix §2 gives them only in substance. Please also confirm that the stand-in personas are in its Section S, as §4.0 says; if they are elsewhere, §4.0 has to change.
- [ ] `instruction-sets/ERRATA_AND_v0.2_CHANGES.md` (§4.12)

## Code

- [ ] `tools/harness.py`
- [ ] `tools/prov.py`
- [ ] `tools/perspective_distance.py`
- [ ] `tools/machine_origin.py`
- [ ] `tools/editor_view.py`
- [ ] `tools/style_metrics.py`
- [ ] `tools/power_critical_test.py`

## Run records

These are listed in the Annex C manifest, so `MANIFEST.txt` already holds their sizes and hashes, and `python verify.py` will confirm each one once it is in place.

- [ ] `runs/13_pilot/`: the six blind reports (`blind/review_A.md` to `review_F.md`), `scoring.md`, `UNBLINDING_MAP.json` and `style_metrics.txt` (§7.9)
- [ ] `runs/configs/focal_perspective_normalized.json`. The unnormalized perspective is in `runs/01_dialogue/turn_09_elicitor_SPEC.md`, so this could be rebuilt if the original is lost, but only the original will match the manifest hash.
- [ ] `runs/configs/simulated_perspectives.json`. This can't be rebuilt: the transcripts of Runs 03–06 give each lens's weights, material inferences and standards, but not its settings on the 29 parameters, and the §1.4 distance table depends on them.
- [ ] `runs/provenance_events.json` (§4.9)
- [ ] `runs/14_machine_origin.json` (§4.9)
- [ ] `runs/03_checks/results.json` to `runs/10_checks/results.json` (eight files). Every harness output they summarize is already present as a `.out.txt` file.

## Please check

- [ ] **Files taken from the appendix.** Three files here were copied from its annexes, and the appendix records no hashes for them: `schema/review-objects.v0.schema.json` and `schema/context.v0.jsonld` (Annex A), `lakatos/LAKATOS_TABLES_1-4.md` (Annex D) and `governance/CONSENT_INSTRUMENTS.md` (Annex E). If you have the originals, use yours. If yours differ from the appendix, the appendix has to change to match. The `runs/` and `case/` files need no check: each matches the hash the appendix records for it.
- [ ] **`case/HASHES.txt`.** This was regenerated from the two case files, so its hashes match §4.1, but its layout may differ from your original. Use yours if you have it.
- [ ] **The Lakatos tables.** This repository is public, while the appendix goes only to the review team. Keeping `lakatos/` here publishes the tables. If we would rather not, delete the folder, and the appendix's three references to it (front matter, §3, References) change to point to Annex D alone.
- [ ] **Paths.** Folder and file names have to match the appendix exactly (for example `case/`, not `cases/`). After the last file is added, download a fresh copy and run `python verify.py`. It should report 126 verified, 0 mismatched, 0 missing.
- [ ] **Hashes for the new files.** The appendix records no hashes for the instruction sets or the tools. Add them to `MANIFEST.txt` and to the Annex C manifest when they go in, so that a reader can confirm these are the versions used on 23 October.
- [ ] **Placeholders.** Delete each `PLACEHOLDER.md`, and `runs/MISSING_FILES.md`, once its files are in.
- [ ] **Licence.** None has been added yet.
