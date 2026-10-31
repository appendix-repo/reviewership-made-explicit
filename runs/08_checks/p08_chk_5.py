# CheckSpec p08:chk:5: the sign of the uncertainty effect implied by A3, against Table 2
# Settles: p08:fnd:5
# Premises, from the manuscript only:
#   ms:§2.2  H, G linear; s, h0, h1, g0, g1 > 0; u >= 0; m in [0,1); A3: h1/h0 > g1/(s+g0)
#   ms:§2.3  k* = (s+G)/(H(1-m));  ms:§2.4 Phi = F(k*)  =>  dPhi/du = f(k*) dk*/du  (see p08:chk:3)
#   ms:§3.3  Phi = b1 m + b2 u + b3 (m x u) + ...  (m entered uncentred; u a z-score)  =>  dPhi/du = b2 + b3 m
#   ms:T2    Model 3: b2 = 0.084 (0.051), b3 = -0.061 (0.019); Model 4: b2 = 0.079 (0.050), b3 = -0.058 (0.019)
#   ms:§3.2  modularity mean 0.46, SD 0.24 (m in [0,1] as a share)
#   cov(b2, b3) is not reported, so SEs of b2 + b3 m are bounded using |corr| <= 1
import sympy as sp
import numpy as np
from scipy import stats

s, g0, g1, h0, h1 = sp.symbols('s g0 g1 h0 h1', positive=True)
u = sp.symbols('u', nonnegative=True)
m = sp.symbols('m', real=True)
H = h0 + h1*u
G = g0 + g1*u
kstar = (s + G) / (H*(1 - m))
num = sp.simplify(sp.diff(kstar, u)*H**2*(1 - m))      # sign of dk*/du (H^2(1-m) > 0)
ok_num = (sp.simplify(num - (g1*h0 - h1*(s + g0))) == 0)
ok_A3 = (sp.simplify((h1/h0 - g1/(s + g0))*h0*(s + g0) + num) == 0)   # A3 <=> num < 0
print("sign(dk*/du) = sign(g1*h0 - h1*(s+g0)):", ok_num, "| A3 <=> dk*/du < 0:", ok_A3)

models = {"M3": (0.084, 0.051, -0.061, 0.019), "M4": (0.079, 0.050, -0.058, 0.019)}
report_at = (0.0, 0.22, 0.46, 0.70, 1.0)               # 0, mean - 1 SD, mean, mean + 1 SD, 1
pos_all, sig_any, zmax_all = True, False, 0.0
for name, (b2, se2, b3, se3) in models.items():
    print(f"{name}: dPhi/du = {b2:+.3f} {b3:+.3f} m; zero crossing at m = {-b2/b3:.2f}")
    for mv in np.linspace(0.0, 1.0, 101):
        me = b2 + b3*mv
        se_hi = se2 + mv*se3                            # corr(b2, b3) = +1 (m >= 0)
        se_lo = abs(se2 - mv*se3)                       # corr(b2, b3) = -1
        z_min = abs(me)/se_hi
        z_max = abs(me)/se_lo if se_lo > 0 else np.inf
        pos_all = pos_all and (me > 0)
        sig_any = sig_any or (2*stats.norm.sf(z_max) < 0.05)
        zmax_all = max(zmax_all, z_max)
        if any(np.isclose(mv, x) for x in report_at):
            print(f"   m={mv:.2f}: estimate {me:+.4f}; SE in [{se_lo:.4f}, {se_hi:.4f}]; "
                  f"|z| in [{z_min:.2f}, {z_max:.2f}]; p in [{2*stats.norm.sf(z_max):.3f}, {2*stats.norm.sf(z_min):.3f}]")

if ok_num and ok_A3 and pos_all and not sig_any:
    v = ("DEMONSTRATED (tension, not refutation): under A3 the model implies dPhi/du <= 0 at every m; "
         "Table 2 point estimates of dPhi/du are positive for all m in [0,1] (M3, M4); none is significant at 5% "
         f"under any cov(b2,b3) (max |z| = {zmax_all:.2f}); the manuscript neither states nor tests the implication")
elif ok_num and ok_A3 and pos_all and sig_any:
    v = ("DEMONSTRATED (possible significant contradiction): estimates positive on [0,1] and significant at 5% "
         "for some admissible cov(b2,b3); authors' vcov needed")
else:
    v = "NOT DEMONSTRATED"
print("VERDICT: p08:fnd:5", v)
