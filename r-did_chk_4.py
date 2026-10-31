from scipy import stats

b_mod, sd_m, sd_phi = 0.112, 0.24, 0.17
eff = b_mod*sd_m
print("1-SD modularity effect (pp):", round(100*eff, 2), "| in outcome SDs:", round(eff/sd_phi, 3))

b1_peer, b2_peer, se2 = 0.137, 0.042, 0.038
print("relative fall in peer coefficient M1 -> M2:", round((b1_peer - b2_peer)/b1_peer, 3))
z95, z90 = stats.norm.ppf(0.975), stats.norm.ppf(0.95)
print("M2 peer 95% CI:", (round(b2_peer - z95*se2, 4), round(b2_peer + z95*se2, 4)))
print("M2 peer 90% CI:", (round(b2_peer - z90*se2, 4), round(b2_peer + z90*se2, 4)))

def tost_p(b, se, delta):
    p_lower = stats.norm.sf((b + delta)/se)   # H0: beta <= -delta
    p_upper = stats.norm.cdf((b - delta)/se)  # H0: beta >= +delta
    return max(p_lower, p_upper)

for delta in [0.02, 0.05, 0.0685, 0.10, 0.137]:
    print(f"TOST p at bound +/-{delta}: {tost_p(b2_peer, se2, delta):.4f}")
delta_min = max(abs(b2_peer - z90*se2), abs(b2_peer + z90*se2))
print("smallest bound passable at alpha=0.05:", round(delta_min, 4),
      "| as share of M1 estimate:", round(delta_min/b1_peer, 3))
