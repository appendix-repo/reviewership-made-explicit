from scipy import stats

cells = {  # ms:T2: (coef, SE, reported stars)
    "M1.Peer": (0.137, 0.031, "***"), "M2.Peer": (0.042, 0.038, ""),
    "M3.Peer": (0.039, 0.037, ""),    "M4.Peer": (0.036, 0.036, ""),
    "M2.Mod":  (0.112, 0.024, "***"), "M3.Mod":  (0.118, 0.025, "***"),
    "M4.Mod":  (0.097, 0.023, "***"), "M3.U":    (0.084, 0.051, "***"),
    "M4.U":    (0.079, 0.050, ""),    "M3.MxU":  (-0.061, 0.019, "**"),
    "M4.MxU":  (-0.058, 0.019, "**"), "M1.Spec": (-0.094, 0.027, "***"),
    "M2.Spec": (-0.091, 0.027, "***"), "M3.Spec": (-0.090, 0.026, "***"),
    "M4.Spec": (-0.088, 0.026, "***"), "M4.Staff": (-0.143, 0.029, "***"),
}
def stars(p): return "***" if p < 0.001 else "**" if p < 0.01 else "*" if p < 0.05 else ""
df = 412 - 1  # hospital clusters - 1
for k, (b, se, rep) in cells.items():
    z = b / se
    p_n = 2*stats.norm.sf(abs(z)); p_t = 2*stats.t.sf(abs(z), df)
    flag = "" if stars(p_n) == rep and stars(p_t) == rep else "   <-- MISMATCH"
    print(f"{k:9s} z={z:+.2f} p_norm={p_n:.4f} p_t={p_t:.4f} reported='{rep}' implied='{stars(p_t)}'{flag}")

tcrit = stats.t.ppf(0.975, df)
for k in ("M1.Peer", "M2.Peer"):
    b, se, _ = cells[k]
    print(k, "95% CI:", round(b - tcrit*se, 3), round(b + tcrit*se, 3))
print("M2 upper bound / M1 point estimate:", round((0.042 + tcrit*0.038)/0.137, 2))
print("Obs: 412x11 =", 412*11, "| 412x10 =", 412*10, "| reported 4712 | 4712/412 =", round(4712/412, 3))
print("1-SD modularity effect:", round(0.112*0.24, 4), "| in SDs of Phi:", round(0.112*0.24/0.17, 3))
print("Peer decline M1->M2:", round((0.137 - 0.042)/0.137, 3))
for uu in (-1, 0, 1, 2):  # M3 marginal effect of modularity; u standardized
    print(f"u={uu:+d}: dPhi/dm = {0.118 - 0.061*uu:+.3f}")
