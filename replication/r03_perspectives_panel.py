"""R03. Perspective distances and the panel's survival table (appendix Sections 1.4, 4.4, 4.5, 5.3).

1. The table of distances in Section 1.4, recomputed with tools/perspective_distance.py from the elicited focal
   perspective and the four configured lenses.
2. The sensitivity reported in Section 4.5: reversing R-DID's stance on MI6 moves the INF distance between R-TCE and
   R-DID from 0.114 to 0.097 and the overall distance from 0.365 to 0.361, and removes the only opposed inference.
3. The survival scores and classifications of Section 4.5, recomputed from the verdict table printed there, and
   compared with the panel's own check (pnl:chk:1).
4. The correlation of verdict divergence with distance (Pearson r = −0.42, Spearman ρ = −0.65, n = 6 pairs).
"""
import copy
import json

import numpy as np
from scipy import stats

from lib import APPENDIX, check, md_table, read
import perspective_distance as pd

G = "Perspectives and panel"


def perspectives():
    ps = [json.loads(read("runs/configs/focal_perspective_normalized.json"))]
    ps += json.loads(read("runs/configs/simulated_perspectives.json"))
    return {x["@id"].split(":", 1)[1]: x for x in ps}


def run():
    out = []
    P = perspectives()
    app = open(APPENDIX, encoding="utf-8").read()
    _, rows = md_table(app, "| Pair | ONT | EPI | INF | TEC | PRA | Overall | Opposed inferences |")
    for r in rows:
        a, b = [x.strip() for x in r[0].split("–")]
        d = pd.distance(P[a], P[b])
        got = [f"{d[k]:.2f}" for k in ("ONT", "EPI", "INF", "TEC", "PRA", "overall")] + [", ".join(d["opposed"]) or "none"]
        out.append(check(G, f"Distance {a} – {b} (ONT, EPI, INF, TEC, PRA, overall, opposed)", "1.4", r[1:], got))

    t, dd = P["R-TCE"], P["R-DID"]
    base = pd.distance(t, dd)
    flipped = copy.deepcopy(dd)
    mi = flipped["materialInferences"]
    mi["rejected"].remove("MI6")
    mi.setdefault("endorsed", []).append("MI6")
    fl = pd.distance(t, flipped)
    out.append(check(G, "R-TCE – R-DID INF distance, as configured → MI6 reversed", "4.5", (0.114, 0.097), (base["INF"], fl["INF"])))
    out.append(check(G, "R-TCE – R-DID overall distance, as configured → MI6 reversed", "4.5", (0.365, 0.361),
                     (base["overall"], fl["overall"])))
    out.append(check(G, "Reversing one stance moves the inferential distance by less than 0.02", "1.4", True,
                     abs(base["INF"] - fl["INF"]) < 0.02))
    f = pd.distance(P["FOCAL"], P["R-DID"])
    out.append(check(G, "FOCAL – R-DID: close on INF, far on EPI", "1.4", (0.25, 0.79), (round(f["INF"], 2), round(f["EPI"], 2))))
    near = min(("R-TCE", "R-INST", "R-BEH", "R-DID"), key=lambda k: pd.distance(P["FOCAL"], P[k])["overall"])
    far = max(("R-TCE", "R-INST", "R-BEH", "R-DID"), key=lambda k: pd.distance(P["FOCAL"], P[k])["overall"])
    out.append(check(G, "Nearest and farthest lens from the elicited focal perspective", "1.4, 4.4", ("R-TCE", "R-INST"), (near, far)))

    # Material-inference stances of the lenses (Section 4.4)
    want = {"R-TCE": ({"MI1", "MI6", "MI8", "MI9"}, {"MI3", "MI7", "MI10"}),
            "R-INST": ({"MI3", "MI4", "MI10"}, {"MI2", "MI7", "MI9"}),
            "R-BEH": ({"MI4", "MI5"}, {"MI2", "MI7", "MI9"}),
            "R-DID": (set(), {"MI6", "MI7"}),
            "FOCAL": ({"MI1", "MI6"}, {"MI7"})}
    for k, (e, r) in want.items():
        m = P[k].get("materialInferences", {})
        out.append(check(G, f"{k}: endorsed and rejected material inferences", "4.2, 4.4", (sorted(e), sorted(r)),
                         (sorted(m.get("endorsed", [])), sorted(m.get("rejected", [])))))
    w = {d: P["FOCAL"]["dimensions"][d]["weight"] for d in ("ONT", "EPI", "INF", "TEC", "PRA")}
    out.append(check(G, "Focal reviewer's weights", "4.2", {"ONT": 0.6, "EPI": 0.9, "INF": 0.9, "TEC": 0.7, "PRA": 0.4}, w))

    # Survival table (Section 4.5)
    head, rows = md_table(app, "| Contribution (as aligned by the panel) |")
    val = {"survives": 1.0, "**survives**": 1.0, "qualified": 0.5, "fails": 0.0}
    lenses = ["R-TCE", "R-INST", "R-BEH", "R-DID"]
    verdicts = {}
    pnl = read("runs/07_checks/pnl_chk_1.out.txt")
    for r in rows:
        cid = r[0].split("`")[1]
        v = [val[x] for x in r[1:5]]
        verdicts[cid] = v
        score = sum(v) / 4
        robust = all(x > 0 for x in v)
        cls = "robust" if robust else ("fails for every lens" if all(x == 0 for x in v) else "neither")
        out.append(check(G, f"{cid}: survival score and classification", "4.5, 5.3", (float(r[5]), r[6]), (score, cls)))
        line = [l for l in pnl.splitlines() if l.startswith(cid)][0].split()
        out.append(check(G, f"{cid}: score agrees with the panel's own check pnl:chk:1", "4.5", float(line[1]), score))
    # Lens-dependent (Section 5.3): stands (survives or qualified) for two or more reviewers but not all, and every
    # pair of those reviewers is closer than the panel's median pairwise distance.
    pair_d = {(a, b): pd.distance(P[a], P[b])["overall"] for i, a in enumerate(lenses) for b in lenses[i + 1:]}
    med = float(np.median(list(pair_d.values())))
    dep = []
    for cid, v in verdicts.items():
        surv = [lenses[i] for i, x in enumerate(v) if x >= 0.5]
        if 2 <= len(surv) < 4 and all(pair_d.get((a, b), pair_d.get((b, a))) < med
                                       for i, a in enumerate(surv) for b in surv[i + 1:]):
            dep.append(cid)
    out.append(check(G, "Contributions classified lens-dependent (panel median distance as the cut-off)", "4.5, 5.3",
                     [], dep, f"median pairwise distance {med:.3f}"))

    # Divergence against distance (Section 4.5): mean absolute verdict difference over the eight contributions
    xs, ys = [], []
    for i, a in enumerate(lenses):
        for b in lenses[i + 1:]:
            xs.append(round(pd.distance(P[a], P[b])["overall"], 2))
            ys.append(np.mean([abs(v[lenses.index(a)] - v[lenses.index(b)]) for v in verdicts.values()]))
    r_, pr = stats.pearsonr(xs, ys)
    rho, ps_ = stats.spearmanr(xs, ys)
    out.append(check(G, "Verdict divergence against distance: Pearson r (p)", "4.5", (-0.42, 0.40), (round(r_, 2), round(pr, 2))))
    out.append(check(G, "Verdict divergence against distance: Spearman ρ (p)", "4.5", (-0.65, 0.16), (round(rho, 2), round(ps_, 2))))
    closest = min(zip(xs, [f"{a}/{b}" for i, a in enumerate(lenses) for b in lenses[i + 1:]]))
    out.append(check(G, "Closest pair of lenses", "4.5", (0.36, "R-TCE/R-DID"), closest))
    return out


if __name__ == "__main__":
    for r in run():
        print(r.status, "|", r.claim, "|", r.expected, "|", r.observed, "|", r.detail)
