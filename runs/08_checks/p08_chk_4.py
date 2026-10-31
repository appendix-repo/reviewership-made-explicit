# CheckSpec p08:chk:4: numerical consistency of ms:§3.1, ms:Table 2 and the §4 arithmetic
# Settles: p08:fnd:6, p08:fnd:7, p08:S3
# Premises, from the manuscript only:
#   ms:Table 2 coefficients, clustered SEs, stars; note "*** p < 0.001; ** p < 0.01; * p < 0.05"
#   ms:§3.1 "balanced panel of 412 ... observed annually from 2009 to 2019 ... 4,712 hospital-year observations"
#   ms:§3.2 modularity SD 0.24; outsourcing share SD 0.17
#   ms:§4  "one-standard-deviation increase in modularity (0.24) ... 2.7 percentage points ... about one-sixth of a standard deviation"
#   ms:§4  "the peer coefficient falls by more than two-thirds"
import numpy as np
from scipy import stats

rows = [
    ("T2.M1.peer", 0.137, 0.031, "***"), ("T2.M2.peer", 0.042, 0.038, ""),
    ("T2.M3.peer", 0.039, 0.037, ""), ("T2.M4.peer", 0.036, 0.036, ""),
    ("T2.M2.modularity", 0.112, 0.024, "***"), ("T2.M3.modularity", 0.118, 0.025, "***"),
    ("T2.M4.modularity", 0.097, 0.023, "***"),
    ("T2.M3.uncertainty", 0.084, 0.051, "***"), ("T2.M4.uncertainty", 0.079, 0.050, ""),
    ("T2.M3.interaction", -0.061, 0.019, "**"), ("T2.M4.interaction", -0.058, 0.019, "**"),
    ("T2.M1.specificity", -0.094, 0.027, "***"), ("T2.M2.specificity", -0.091, 0.027, "***"),
    ("T2.M3.specificity", -0.090, 0.026, "***"), ("T2.M4.specificity", -0.088, 0.026, "***"),
    ("T2.M4.staffing", -0.143, 0.029, "***"),
]
N_CLUSTERS = 412                 # ms:§3.1; Table 2 "Hospitals 412"
DF = N_CLUSTERS - 1              # usual reference df for cluster-robust t
HALF = 0.0005                    # values reported to 3 decimals
RANK = {"": 0, "*": 1, "**": 2, "***": 3}

def stars(p):
    return "***" if p < 0.001 else "**" if p < 0.01 else "*" if p < 0.05 else ""

def p_two(z, ref):
    return 2*stats.norm.sf(z) if ref == "normal" else 2*stats.t.sf(z, DF)

inconsistent = []
for name, b, se, rep in rows:
    z = abs(b)/se
    z_lo = (abs(b) - HALF)/(se + HALF)   # smallest |t| compatible with rounding
    z_hi = (abs(b) + HALF)/(se - HALF)   # largest |t| compatible with rounding
    ok_any = False
    for ref in ("t", "normal"):
        lo, hi = RANK[stars(p_two(z_lo, ref))], RANK[stars(p_two(z_hi, ref))]
        if lo <= RANK[rep] <= hi:
            ok_any = True
    pc = p_two(z, "t")
    print(f"{name:20s} b={b:+.3f} se={se:.3f} |t|={z:5.2f} p(t,{DF})={pc:.4g} implied='{stars(pc)}' "
          f"reported='{rep}' {'ok' if ok_any else 'INCONSISTENT'}")
    if not ok_any:
        inconsistent.append(name)

# §4 H1 arithmetic
eff = 0.112*0.24
frac_sd = eff/0.17
ok_27 = (round(100*eff, 1) == 2.7)
ok_sixth = abs(frac_sd - 1/6)/(1/6) < 0.10
print(f"1 SD effect = {eff:.5f} ({100*eff:.2f} pp); share of outcome SD = {frac_sd:.3f} (1/6 = {1/6:.3f})")

# §4 H3 arithmetic, including the least favourable rounding
drop = (0.137 - 0.042)/0.137
drop_min = (0.1365 - 0.0425)/0.1365
ok_twothirds = drop > 2/3 and drop_min > 2/3
print(f"peer coefficient drop = {drop:.3f} (least favourable rounding {drop_min:.3f}); 2/3 = {2/3:.3f}")

# INFO only (referred to P-INF; not a P-NUM finding): 95% CI of the Model 2 peer coefficient
tc = stats.t.ppf(0.975, DF)
lo, hi = 0.042 - tc*0.038, 0.042 + tc*0.038
print(f"INFO: Model 2 peer 95% CI = [{lo:.3f}, {hi:.3f}]; upper bound = {hi/0.137:.0%} of the Model 1 estimate")

# §3.1 sample size
years = 2019 - 2009 + 1
n_bal, n_bal_lag, N_rep = 412*years, 412*(years - 1), 4712
ok_N = N_rep in (n_bal, n_bal_lag)
print(f"412 x {years} = {n_bal}; with t-1 lag dropping 2009: {n_bal_lag}; reported {N_rep}; "
      f"4712/412 = {N_rep/412:.3f}; remainder {N_rep % 412}")

others = [x for x in inconsistent if x != "T2.M3.uncertainty"]
print("VERDICT: p08:fnd:6",
      ("DEMONSTRATED: stars inconsistent with coefficient/SE for " + ", ".join(inconsistent))
      if "T2.M3.uncertainty" in inconsistent else "REFUTED-BY-CHECK: T2.M3.uncertainty stars consistent")
print("VERDICT: p08:fnd:7",
      "DEMONSTRATED: N = 4,712 is incompatible with a balanced panel of 412 hospitals over 2009-2019 (4,532; 4,120 with lag)"
      if not ok_N else "REFUTED-BY-CHECK")
print("VERDICT: p08:S3",
      ("CONFIRMED: 2.7 pp, ~1/6 SD, >2/3 drop correct; all other stars consistent" if (ok_27 and ok_sixth and ok_twothirds and not others)
       else f"NOT CONFIRMED: ok_27={ok_27} ok_sixth={ok_sixth} ok_twothirds={ok_twothirds} other_inconsistent={others}"))
