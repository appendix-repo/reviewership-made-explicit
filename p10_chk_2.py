# p10:chk:2 — arithmetic recomputation of reported statistics in ms:TEST (§3.1, §3.2, Table 2, §4). Not run by the probe.
import numpy as np
from scipy import stats

R = 0.0005                    # half-unit rounding for 3-decimal entries in Table 2
G = 412                       # clusters (hospitals): Table 2 'Hospitals'
ORDER = {"": 0, "*": 1, "**": 2, "***": 3}
def stars_of(p): return "***" if p < 0.001 else "**" if p < 0.01 else "*" if p < 0.05 else ""
def p_of(t): return 2*stats.t.sf(abs(t), df=G - 1)

# (a) N — §3.1: balanced panel, 412 hospitals, annual 2009-2019, 4,712 hospital-years
years = 2019 - 2009 + 1
print(f"(a) 412 x {years} = {412*years}; reported 4712; 4712/412 = {4712/412:.3f}; "
      f"if 2009 is lost to Peer(t-1): {412*(years-1)}")
print("VERDICT: (a) N", "CONSISTENT" if 412*years == 4712 else "INCONSISTENT",
      "with a balanced 412-hospital annual 2009-2019 panel")

# (b) stars vs coef/SE — Table 2; legend '*** p<0.001; ** p<0.01; * p<0.05'
cells = [("M1 Peer", 0.137, 0.031, "***"), ("M2 Peer", 0.042, 0.038, ""), ("M3 Peer", 0.039, 0.037, ""),
         ("M4 Peer", 0.036, 0.036, ""), ("M2 Modularity", 0.112, 0.024, "***"), ("M3 Modularity", 0.118, 0.025, "***"),
         ("M4 Modularity", 0.097, 0.023, "***"), ("M3 Uncertainty", 0.084, 0.051, "***"), ("M4 Uncertainty", 0.079, 0.050, ""),
         ("M3 Mod x Unc", -0.061, 0.019, "**"), ("M4 Mod x Unc", -0.058, 0.019, "**"), ("M1 Specificity", -0.094, 0.027, "***"),
         ("M2 Specificity", -0.091, 0.027, "***"), ("M3 Specificity", -0.090, 0.026, "***"),
         ("M4 Specificity", -0.088, 0.026, "***"), ("M4 Staffing", -0.143, 0.029, "***")]
bad = []
for name, b, se, st in cells:
    tmin = max(abs(b) - R, 0)/(se + R); tmax = (abs(b) + R)/(se - R)
    lo, hi = ORDER[stars_of(p_of(tmin))], ORDER[stars_of(p_of(tmax))]
    ok = lo <= ORDER[st] <= hi
    print(f"(b) {name}: |t|={abs(b)/se:.2f}, p={p_of(b/se):.4f}, reported '{st}' -> {'ok' if ok else 'MISMATCH'}")
    if not ok:
        bad.append(name)
print("VERDICT: (b) stars", "CONSISTENT in all cells" if not bad else "INCONSISTENT in: " + ", ".join(bad))

# (c) magnitudes — §4 H1: 'one-standard-deviation increase in modularity (0.24) ... 2.7 percentage points ... about one-sixth of a SD'
b_m, sd_m, sd_phi = 0.112, 0.24, 0.17          # Table 2 M2; §3.2 SDs
eff = b_m*sd_m; frac = eff/sd_phi
c_ok = round(eff*100, 1) == 2.7 and 0.14 <= frac <= 0.19
print(f"(c) effect = {eff*100:.2f} pp; = {frac:.3f} SD of Phi (1/6 = 0.167); within R2 gain M1->M2 = {0.13-0.08:.2f}")
print("VERDICT: (c) H1 magnitudes", "CONSISTENT" if c_ok else "INCONSISTENT",
      f"with text; size is {frac:.2f} SD per SD of m (bears on 'strongly', p10:fnd:9)")

# (d) §4 H3: 'falls by more than two-thirds'
drop = (0.137 - 0.042)/0.137
drop_min = ((0.137 - R) - (0.042 + R))/(0.137 - R)
print(f"(d) fall = {drop:.3f} (min under rounding {drop_min:.3f})")
print("VERDICT: (d) 'more than two-thirds'", "CONSISTENT" if drop_min > 2/3 else "NOT ROBUST TO ROUNDING")

# (e) what the M2 peer estimate licenses (EPI.5; bears on 'rule out', p10:fnd:1)
b1, se1, b2, se2 = 0.137, 0.031, 0.042, 0.038
z = stats.norm.ppf(0.975)
ci = (b2 - z*se2, b2 + z*se2)
delta_min = abs(b2) + stats.norm.ppf(0.95)*se2   # smallest symmetric TOST bound giving equivalence at alpha = .05
print(f"(e) M2 peer 95% CI = [{ci[0]:.3f}, {ci[1]:.3f}]; TOST equivalence needs bounds >= ±{delta_min:.3f} "
      f"(= {delta_min/b1:.0%} of the M1 estimate)")
for rho in (0.0, 0.5, 0.8, 0.9):                 # covariance of M1 and M2 estimates is not reported
    sed = np.sqrt(se1**2 + se2**2 - 2*rho*se1*se2)
    zz = (b1 - b2)/sed
    print(f"(e) M1-M2 difference, assumed corr {rho}: z = {zz:.2f}, p = {2*stats.norm.sf(abs(zz)):.4f}")
print("VERDICT: (e) a null peer effect is", "NOT ESTABLISHED" if ci[1] > 0.5*b1 else "SUPPORTED",
      f"by M2: the 95% CI reaches {ci[1]:.3f}, i.e. {ci[1]/b1:.0%} of the M1 peer estimate")

# (f) implied auxiliary slope (omitted-variable / FWL identity; M1 and M2 share sample, FE and controls, Table 2):
#     b_spec(M1) = b_spec(M2) + b_m(M2) * pi,  pi = coefficient on specificity in the regression of m on M1's regressors
bs1, bs2 = -0.094, -0.091
pi = (bs1 - bs2)/b_m
pis = [((bs1 + d1) - (bs2 + d2))/(b_m + d3) for d1 in (-R, R) for d2 in (-R, R) for d3 in (-R, R)]
corr_bound = max(abs(min(pis)), abs(max(pis)))*0.5/sd_m   # specificity in [0,1] => SD <= 0.5 (raw SDs; within SDs unreported)
print(f"(f) implied pi = {pi:.4f} (rounding range {min(pis):.4f} to {max(pis):.4f}); "
      f"full-range change in specificity <-> {pi/sd_m:.2f} SD of m; |implied corr| <= {corr_bound:.3f} on raw-SD basis")
print("VERDICT: (f) INDICATIVE — conditional on controls and FE, modularity is nearly unrelated to measured specificity "
      f"(pi in [{min(pis):.3f}, {max(pis):.3f}]); if the rating measures effective specificity k(1-m), this does not fit the "
      "§2.2 mechanism (p10:fnd:5). Within-hospital SDs are unreported, so the bound is indicative only.")
