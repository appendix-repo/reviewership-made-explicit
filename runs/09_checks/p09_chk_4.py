# p09:chk:4 -- H1 magnitude, the 'two-thirds' fall, and where the modularity effect crosses zero (P-NUM)
from scipy import stats

b_m2, sd_m, sd_phi = 0.112, 0.24, 0.17      # ms:T2.M2 modularity; ms:§3.2 SDs (pooled)
eff = b_m2 * sd_m
ratio = eff / sd_phi
drop = (0.137 - 0.042) / 0.137              # ms:T2 peer, Model 1 -> Model 2
print(f"one-SD effect = {b_m2} x {sd_m} = {eff:.4f} ({eff * 100:.2f} pp); reported 2.7 pp")
print(f"as share of SD(Phi): {ratio:.3f}; one-sixth = {1 / 6:.3f}")
print(f"fall in peer coefficient: {drop:.3f}; two-thirds = {2 / 3:.3f}")
ok = (round(eff * 100, 1) == 2.7) and (abs(ratio - 1 / 6) <= 0.02) and (drop > 2 / 3)

# informational: marginal effect of m = beta1 + beta3*u, u standardized (ms:§3.2)
for label, b1, b3 in (("Model 3", 0.118, -0.061), ("Model 4", 0.097, -0.058)):
    u0 = -b1 / b3
    print(f"{label}: marginal effect of m is zero at u = {u0:.2f} SD; "
          f"share of hospital-years above it if u ~ N(0,1) [ASSUMPTION]: {stats.norm.sf(u0):.3f}")
print("note: SDs are pooled (ms:§3.2); within-hospital SDs, which govern the FE estimand, are not reported.")
if ok:
    print("VERDICT: REFUTED-BY-CHECK - the reported magnitudes (2.7 pp, about one-sixth SD, fall > two-thirds) are arithmetically correct.")
else:
    print("VERDICT: DEMONSTRATED - at least one reported magnitude does not follow from Table 2 and the ms:§3.2 moments.")
