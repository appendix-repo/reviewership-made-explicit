# tools/

> **PLACEHOLDER.** The original files for this folder were not available when this repository was assembled. They will be added; nothing here has been regenerated or rerun.

Expected contents:

| File | What it does | Where the appendix relies on it |
|---|---|---|
| `harness.py` | Extracts each check from a role's output and runs it in an isolated interpreter (empty environment, no network, 120-second limit) | §2.4, §4.0, §9.3 |
| `prov.py` | File-based provenance layer: hash-chained `ProvenanceEvent`s, actual and reconstructed times | §2.5, §4.9, §9.3 |
| `perspective_distance.py` | Perspective distance by dimension, with opposed material inferences | §1.4, §4.5, §5.3 |
| `machine_origin.py` | Machine-origin share of a signed review (5-gram overlap; definition in §5.3) | §4.9, §5.3 |
| `editor_view.py` | Builds the editor view from the trace, the dispositions and the machine-origin analysis | §4.9 |
| `style_metrics.py` | Length, hedging, nominalization and Flesch Reading Ease | §7.9 |
| `power_critical_test.py` | Sample-size calculations for the critical test | §8.4 |

The appendix records no hashes for these files. The outputs of `editor_view.py` and the harness are in `runs/`.
