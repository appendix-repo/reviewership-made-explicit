# p09:chk:3 -- does Table 2 license 'no longer predicts' / 'rule out'? (P-NUM)
from scipy import stats

b1, se1 = 0.137, 0.031   # ms:T2, Peer, Model 1
b2, se2 = 0.042, 0.038   # ms:T2, Peer, Model 2
DF = 411                 # 412 hospital clusters (ms:T2)
t975, t95 = stats.t.ppf(0.975, DF), stats.t.ppf(0.95, DF)

lo, hi = b2 - t975 * se2, b2 + t975 * se2
print(f"Model 2 peer: 95% CI = [{lo:.4f}, {hi:.4f}]; upper bound = {hi / b1:.2f} x Model 1 estimate")

delta_min = abs(b2) + t95 * se2
print(f"smallest symmetric margin at which TOST declares equivalence (alpha=.05): {delta_min:.4f} "
      f"= {delta_min / b1:.2f} x Model 1 estimate")

margin = 0.5 * b1
p_upper = stats.t.cdf((b2 - margin) / se2, DF)   # H0: beta >= +margin
p_lower = stats.t.sf((b2 + margin) / se2, DF)    # H0: beta <= -margin
p_tost = max(p_upper, p_lower)
print(f"TOST, margin = 0.5 x Model 1 estimate = {margin:.4f}: p = {p_tost:.3f}")

print(f"change M1 - M2 = {b1 - b2:.3f}; the covariance of the two estimates is not reported, so the test is bounded:")
for rho in (0.0, 0.5, 0.8, 0.9):
    sd = (se1 ** 2 + se2 ** 2 - 2 * rho * se1 * se2) ** 0.5
    z = (b1 - b2) / sd
    print(f"  assumed rho={rho:.1f}: se={sd:.4f}, z={z:.2f}, p={2 * stats.norm.sf(abs(z)):.4f}")

if p_tost >= 0.05 and hi > margin:
    print(f"VERDICT: DEMONSTRATED - the Model 2 peer estimate is not shown equivalent to zero (TOST p={p_tost:.3f} at margin "
          f"{margin:.3f}); its 95% CI reaches {hi:.3f}. Non-significance does not license 'rule out'.")
else:
    print("VERDICT: REFUTED-BY-CHECK - the Model 2 peer estimate is statistically equivalent to zero at the stated margin.")
