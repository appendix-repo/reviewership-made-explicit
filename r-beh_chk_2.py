from scipy import stats

rows = {  # (coef, se, reported stars), ms:T2
 "M1 peer": (0.137, 0.031, "***"), "M2 peer": (0.042, 0.038, ""),
 "M3 peer": (0.039, 0.037, ""),    "M4 peer": (0.036, 0.036, ""),
 "M2 mod":  (0.112, 0.024, "***"), "M3 mod":  (0.118, 0.025, "***"), "M4 mod": (0.097, 0.023, "***"),
 "M3 unc":  (0.084, 0.051, "***"), "M4 unc":  (0.079, 0.050, ""),
 "M3 mxu":  (-0.061, 0.019, "**"), "M4 mxu":  (-0.058, 0.019, "**"),
 "M1 spec": (-0.094, 0.027, "***"), "M2 spec": (-0.091, 0.027, "***"),
 "M3 spec": (-0.090, 0.026, "***"), "M4 spec": (-0.088, 0.026, "***"),
 "M4 staff": (-0.143, 0.029, "***"),
}
df = 412 - 1
def stars(p): return "***" if p < 0.001 else "**" if p < 0.01 else "*" if p < 0.05 else ""
for k, (b, se, rep) in rows.items():
    t = b/se; p = 2*stats.t.sf(abs(t), df)
    print(f"{k:9s} t={t:6.2f} p={p:.4f} implied={stars(p):3s} reported={rep:3s}",
          "OK" if stars(p) == rep else "MISMATCH")
print("Balanced N 412 x 11 =", 412*11, "| reported 4712 | 4712/412 =", round(4712/412, 3))
print("Effect 0.112*0.24 =", 0.112*0.24, "| in SD of Phi:", round(0.112*0.24/0.17, 3))
print("Peer fall M1->M2:", round((0.137 - 0.042)/0.137, 3), "(claim: > 2/3 =", round(2/3, 3), ")")
c = stats.t.ppf(0.975, df)
lo, hi = 0.042 - c*0.038, 0.042 + c*0.038
print("M2 peer 95% CI:", (round(lo, 3), round(hi, 3)), "| upper / M1 coef:", round(hi/0.137, 3))
print("Implied u effect at mean m (M3):", round(0.084 - 0.061*0.46, 3))
print("Max within-hospital shift from m (M2, m 0->1):", 0.112)
