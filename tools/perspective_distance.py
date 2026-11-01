"""Perspective distance (appendix §5.3, draft v0.1).
Usage: python3 perspective_distance.py FILE.json [FILE2.json ...]  (each file: one ReviewingPerspective or a list)
Per parameter: Jaccard distance for sets; normalized rank difference for ordinal scales; 0/1 for other categories;
mean |r1-r2|/2 over options for model-class or strategy ratings (preferred 2, admissible 1, suspect 0; accepted 1, suspect 0).
Material inferences MI1..MI10 scored endorsed +1, neutral 0, rejected -1; distance = mean |a-b|/2; counted as parameter INF.2.
Free-text parameters (INF.1, PRA.1, PRA.5) are not compared. Dimension distance = mean over parameters both perspectives set.
Overall distance = sum_d wbar_d * dist_d / sum_d wbar_d, with wbar_d the mean of the two perspectives' weights.
Each pair is also reported with its opposed inferences (endorsed by one perspective, rejected by the other), because
an average over parameters can hide the single inference on which a disagreement turns (appendix Section 4.5)."""
import json, sys, itertools
ORD = {"ONT.2": ["same level required", "cross-level with explicit bridging", "indifferent"],
       "ONT.4": ["strict", "moderate", "loose"], "EPI.4": ["high", "medium", "low"],
       "INF.3": ["proof", "sketch", "verbal"], "INF.4": ["low", "medium", "high"],
       "INF.7": ["required", "preferred", "not required"], "TEC.1": ["required", "preferred", "not expected"],
       "TEC.3": ["very high", "high", "moderate", "low"], "TEC.4": ["always", "sometimes", "never"],
       "PRA.3": ["always", "sometimes", "never"], "PRA.4": ["high", "medium", "low"]}
FREE = {"INF.1", "PRA.1", "PRA.5", "PRA.6"}
RATE = {"preferred": 2, "admissible": 1, "suspect": 0, "accepted": 2}
def norm(x): return x.strip().lower() if isinstance(x, str) else x
def pdist(code, a, b):
    if code in FREE: return None
    if isinstance(a, list) or isinstance(b, list):
        A = {norm(x) for x in (a if isinstance(a, list) else [a])}; B = {norm(x) for x in (b if isinstance(b, list) else [b])}
        return 1 - len(A & B) / len(A | B) if A | B else 0.0
    if isinstance(a, dict) and isinstance(b, dict):
        keys = set(a) | set(b)
        return sum(abs(RATE.get(norm(a.get(k, "admissible")), 1) - RATE.get(norm(b.get(k, "admissible")), 1)) / 2 for k in keys) / len(keys)
    a, b = norm(a), norm(b)
    if code in ORD and a in ORD[code] and b in ORD[code]:
        return abs(ORD[code].index(a) - ORD[code].index(b)) / (len(ORD[code]) - 1)
    return 0.0 if a == b else 1.0
def mivec(p):
    mi = p.get("materialInferences", {}); e, r = set(mi.get("endorsed", [])), set(mi.get("rejected", []))
    return [1 if f"MI{i}" in e else -1 if f"MI{i}" in r else 0 for i in range(1, 11)]
def distance(p, q):
    out, num, den = {}, 0.0, 0.0
    for d in ["ONT", "EPI", "INF", "TEC", "PRA"]:
        pa, qa = p["dimensions"][d]["parameters"], q["dimensions"][d]["parameters"]
        ds = [x for x in (pdist(c, pa[c], qa[c]) for c in set(pa) & set(qa)) if x is not None]
        if d == "INF": ds.append(sum(abs(x - y) for x, y in zip(mivec(p), mivec(q))) / 20)
        dd = sum(ds) / len(ds) if ds else 0.0
        w = (p["dimensions"][d]["weight"] + q["dimensions"][d]["weight"]) / 2
        out[d] = round(dd, 3); num += w * dd; den += w
    out["overall"] = round(num / den, 3)
    out["opposed"] = [f"MI{i}" for i, (x, y) in enumerate(zip(mivec(p), mivec(q)), 1) if x * y < 0]
    return out
if __name__ == "__main__":
    ps = []
    for f in sys.argv[1:]:
        x = json.load(open(f)); ps += x if isinstance(x, list) else [x]
    print("| Pair | ONT | EPI | INF | TEC | PRA | Overall | Opposed inferences |\n|---|---|---|---|---|---|---|---|")
    for p, q in itertools.combinations(ps, 2):
        r = distance(p, q); print(f"| {p['@id']} – {q['@id']} | " + " | ".join(f"{r[k]:.2f}" for k in ["ONT", "EPI", "INF", "TEC", "PRA", "overall"]) + f" | {', '.join(r['opposed']) or 'none'} |")
