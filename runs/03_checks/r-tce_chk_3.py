import numpy as np
from scipy import stats

table = {  # row: (coef, se, reported stars)
 "M1 Peer": (0.137, 0.031, "***"), "M2 Peer": (0.042, 0.038, ""), "M3 Peer": (0.039, 0.037, ""), "M4 Peer": (0.036, 0.036, ""),
 "M2 Modularity": (0.112, 0.024, "***"), "M3 Modularity": (0.118, 0.025, "***"), "M4 Modularity": (0.097, 0.023, "***"),
 "M3 Uncertainty": (0.084, 0.051, "***"), "M4 Uncertainty": (0.079, 0.050, ""),
 "M3 MxU": (-0.061, 0.019, "**"), "M4 MxU": (-0.058, 0.019, "**"),
 "M1 Specificity": (-0.094, 0.027, "***"), "M2 Specificity": (-0.091, 0.027, "***"),
 "M3 Specificity": (-0.090, 0.026, "***"), "M4 Specificity": (-0.088, 0.026, "***"),
 "M4 Staffing": (-0.143, 0.029, "***"),
}
df = 412 - 1   # hospital clusters - 1
def stars(p): return "***" if p < 0.001 else "**" if p < 0.01 else "*" if p < 0.05 else ""
for k, (b, se, rep) in table.items():
    t = b / se
    p = 2 * stats.t.sf(abs(t), df)
    print(f"{k:16s} t={t:6.2f} p={p:.4f} implied='{stars(p)}' reported='{rep}' {'OK' if stars(p) == rep else 'MISMATCH'}")

print("N, balanced 2009-2019 (11 waves):", 412*11, "| reported 4712 | implied waves:", round(4712/412, 3))
print("N if 2009 is lost to the t-1 peer lag:", 412*10)
print("1-SD effect of m (Model 2):", 0.112*0.24, "| in SDs of Phi:", 0.112*0.24/0.17)
print("Peer decline M1->M2:", (0.137-0.042)/0.137, "| > 2/3:", (0.137-0.042)/0.137 > 2/3)
b, se = 0.042, 0.038
z = stats.norm.ppf(0.975)
print("M2 Peer 95% CI:", (b - z*se, b + z*se))
for sesoi in (0.05, 0.137/2, 0.137):
    p_tost = max(stats.norm.sf((b + sesoi)/se), stats.norm.cdf((b - sesoi)/se))
    print(f"TOST vs +/-{sesoi:.4f}: p = {p_tost:.4f} (equivalence at 5% iff p < 0.05)")
print("Naive z for change 0.137 -> 0.042 (ignores covariance):", (0.137-0.042)/np.sqrt(0.031**2 + 0.038**2))
