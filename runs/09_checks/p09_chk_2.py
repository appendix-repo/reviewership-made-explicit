# p09:chk:2 -- stars against coefficient/SE for every cell of Table 2 (P-NUM)
from scipy import stats

# ms:T2 as printed: (row, model, coefficient, SE, number of stars)
cells = [
    ("Peer outsourcing (t-1)", "M1", 0.137, 0.031, 3),
    ("Peer outsourcing (t-1)", "M2", 0.042, 0.038, 0),
    ("Peer outsourcing (t-1)", "M3", 0.039, 0.037, 0),
    ("Peer outsourcing (t-1)", "M4", 0.036, 0.036, 0),
    ("Modularity", "M2", 0.112, 0.024, 3),
    ("Modularity", "M3", 0.118, 0.025, 3),
    ("Modularity", "M4", 0.097, 0.023, 3),
    ("Environmental uncertainty", "M3", 0.084, 0.051, 3),
    ("Environmental uncertainty", "M4", 0.079, 0.050, 0),
    ("Modularity x uncertainty", "M3", -0.061, 0.019, 2),
    ("Modularity x uncertainty", "M4", -0.058, 0.019, 2),
    ("Asset specificity", "M1", -0.094, 0.027, 3),
    ("Asset specificity", "M2", -0.091, 0.027, 3),
    ("Asset specificity", "M3", -0.090, 0.026, 3),
    ("Asset specificity", "M4", -0.088, 0.026, 3),
    ("In-house IT staffing (log)", "M4", -0.143, 0.029, 3),
]
DF = 412 - 1      # ms:T2: 412 hospital clusters; t(G-1) reference
HALF = 0.0005     # printed values are rounded to three decimals


def stars(p):
    return 3 if p < 0.001 else 2 if p < 0.01 else 1 if p < 0.05 else 0


def p_two(t, dist):
    return 2 * (stats.norm.sf(t) if dist == "normal" else stats.t.sf(t, DF))


mismatches = []
print(f"{'row':28s} {'mod':3s} {'coef':>7s} {'se':>6s} {'|t|':>6s} {'p(t411)':>9s} {'printed':>7s} {'attainable':>11s}")
for row, mod, b, se, st in cells:
    t = abs(b) / se
    p = p_two(t, "t")
    t_lo = (abs(b) - HALF) / (se + HALF)
    t_hi = (abs(b) + HALF) / (se - HALF)
    ok = set()
    for dist in ("normal", "t"):
        s_lo, s_hi = stars(p_two(t_lo, dist)), stars(p_two(t_hi, dist))
        ok |= set(range(min(s_lo, s_hi), max(s_lo, s_hi) + 1))
    flag = ""
    if st not in ok:
        mismatches.append(f"{row} {mod}: {b} ({se}) printed {'*' * st}, |t|={t:.2f}, p={p:.4f}")
        flag = "  <-- MISMATCH"
    print(f"{row:28s} {mod:3s} {b:7.3f} {se:6.3f} {t:6.2f} {p:9.5f} {st:7d} {str(sorted(ok)):>11s}{flag}")

print(f"cells checked: {len(cells)}; mismatches: {len(mismatches)}")
if mismatches:
    print("VERDICT: DEMONSTRATED - stars inconsistent with coefficient/SE (robust to rounding) in: " + "; ".join(mismatches))
else:
    print("VERDICT: REFUTED-BY-CHECK - all printed stars are attainable from the printed coefficients and SEs.")
