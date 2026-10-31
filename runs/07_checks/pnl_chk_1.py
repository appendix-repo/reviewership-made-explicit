import pandas as pd
from scipy import stats

SCORE = {"s": 1.0, "q": 0.5, "f": 0.0}
rows = [f"pnl:ctb:{i}" for i in range(1, 9)]
V = pd.DataFrame({
    "R-TCE":  ["q", "q", "q", "f", "f", "q", "f", "q"],
    "R-INST": ["q", "q", "q", "f", "f", "s", "q", "q"],
    "R-BEH":  ["q", "q", "f", "f", "q", "q", "f", "q"],
    "R-DID":  ["q", "q", "f", "f", "f", "q", "q", "f"],
}, index=rows)
S = V.apply(lambda col: col.map(SCORE))

table = pd.DataFrame({
    "score": S.mean(axis=1),
    "robust": (S >= 0.5).all(axis=1),
    "fails_for_all": (S == 0.0).all(axis=1),
    "survivors": S.apply(lambda r: ",".join(r.index[r.values >= 0.5]), axis=1),
})
print(table.to_string())

dist = {("R-TCE", "R-INST"): 0.68, ("R-TCE", "R-BEH"): 0.45, ("R-TCE", "R-DID"): 0.36,
        ("R-INST", "R-BEH"): 0.42, ("R-INST", "R-DID"): 0.65, ("R-BEH", "R-DID"): 0.43}

def divergence(scores):
    out = [{"pair": f"{a}/{b}", "distance": d,
            "same_verdict": int((scores[a] == scores[b]).sum()),
            "mean_abs_diff": float((scores[a] - scores[b]).abs().mean())}
           for (a, b), d in dist.items()]
    return pd.DataFrame(out).sort_values("distance")

S_alt = S.copy()
S_alt.loc["pnl:ctb:3", ["R-BEH", "R-DID"]] = 0.5   # score pnl:ctb:3 by the remnants R-BEH and R-DID state
for label, scores in [("as stated", S), ("sensitivity: pnl:ctb:3 scored by stated remnants", S_alt)]:
    P = divergence(scores)
    r, p = stats.pearsonr(P["distance"], P["mean_abs_diff"])
    rho, p_s = stats.spearmanr(P["distance"], P["mean_abs_diff"])
    print(f"\n[{label}]\n{P.to_string(index=False)}")
    print(f"Pearson r = {r:+.3f} (p = {p:.2f}); Spearman rho = {rho:+.3f} (p = {p_s:.2f}); n = {len(P)} pairs")

# Lens-dependent: stands (>= 0.5) for two or more reviewers but not all, with every survivor pair within the threshold
for thr in (0.40, 0.45):
    flagged = []
    for c in rows:
        surv = [k for k in S.columns if S.loc[c, k] >= 0.5]
        if 2 <= len(surv) < S.shape[1]:
            pairs = [dist.get((a, b), dist.get((b, a))) for i, a in enumerate(surv) for b in surv[i + 1:]]
            if all(d <= thr for d in pairs):
                flagged.append(c)
    print(f"threshold {thr}: lens-dependent ->", flagged or "none")
