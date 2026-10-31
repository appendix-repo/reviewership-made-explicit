# Reviewership Made Explicit: repository

This repository accompanies the Stage 1 proposal "Reviewership Made Explicit" and its technical appendix, submitted to the *Organization Science* special issue on AI-enabled frontiers in organizational science. The appendix refers to the files here by path. Section numbers below are the appendix's.

## Contents and status

| Folder | Contents | Status |
|---|---|---|
| `REVIEWERSHIP_ANNEX_C_TRANSCRIPTS.md` | Annex C of the appendix: the transcripts of `runs/` combined in run order, with the harness output of every check. Also submitted as a supplementary file | Present. Headings are moved down three levels so they nest under the file headings; the text of each file is otherwise as in `runs/` |
| `runs/` | Every transcript of Runs 01–12 and 14, the check scripts the roles wrote, the harness output of every check, and the recovery scoring | 103 of the 124 files in the Annex C manifest are present, each matching its recorded size and SHA-256 hash. The other 21 are listed in `runs/MISSING_FILES.md`, `runs/13_pilot/PLACEHOLDER.md` and `runs/configs/PLACEHOLDER.md` |
| `case/` | The test manuscript, the sealed defect key and their hashes (§4.1; Annex B) | Present. Both files match the hashes recorded in §4.1 |
| `schema/` | The draft v0.1 JSON Schema and JSON-LD context (§5; Annex A) | Present, as reproduced in Annex A. The appendix records no hashes for these files |
| `lakatos/` | Project Lakatos Tables 1–4 (§3; Annex D) | Present, as reproduced in Annex D. No recorded hash |
| `governance/` | Consent instruments, draft v0.1 (§6.5; Annex E) | Present, as reproduced in Annex E. No recorded hash |
| `instruction-sets/` | The instruction sets (v0.1) and the v0.2 errata (§2, §4.0, §4.12) | Placeholder: see `instruction-sets/PLACEHOLDER.md` |
| `tools/` | The harness, provenance layer, distance, machine-origin, editor-view, style and power tools | Placeholder: see `tools/PLACEHOLDER.md` |

Nothing in this repository has been rerun or regenerated. The present files are copies of the run outputs and case files of 23 October 2026. The missing ones will be added as they are, and `verify.py` will confirm them against the manifest.

## Verifying the files

```
python verify.py
```

The script checks every file in `MANIFEST.txt` against its recorded size and SHA-256 prefix. The manifest is the table in Annex C of the appendix, plus the full hashes of the two case files from §4.1. It reports each file as verified, mismatched or missing.

## Notes

- In these runs, Claude instances stood in for the handling editor and the reviewer (appendix §4.0). Every stand-in's out-of-role notes are in `runs/`, next to the turns they comment on.
- One harness output carries the wrong check id in its header: `runs/03_checks/r-tce_chk_1_b2.out.txt` is the output of `r-tce:chk:2` (appendix §4.5 and §4.12, item 14). The file is kept as the harness produced it.
- `case/HASHES.txt` gives the full SHA-256 hashes of the two case files, computed from the files in this repository.
