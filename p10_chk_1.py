# p10:chk:1 — re-derive Prop. 1 and Prop. 2 of ms:TEST from its own §2.2-2.3 (Part A);
#              sign of the m x u interaction on the Phi scale of §2.4 (Part B). Not run by the probe.
import numpy as np
import sympy as sp
from scipy import stats

# §2.2: s > 0; h0, h1, g0, g1 > 0; u >= 0; m in [0,1)
s, h0, h1, g0, g1 = sp.symbols('s h0 h1 g0 g1', positive=True)
u = sp.symbols('u', nonnegative=True)
m = sp.symbols('m', nonnegative=True)
H = h0 + h1*u                    # §2.2 H(u) = h0 + h1 u
G = g0 + g1*u                    # §2.2 G(u) = g0 + g1 u
kstar = (s + G) / (H*(1 - m))    # §2.3 k*(m,u) = (s + G(u)) / (H(u)(1 - m)), from C_B < C_M

# ---------- Part A1: Prop. 1 ----------
d_m = sp.diff(kstar, m)
appendix_d_m = (s + G) / (H*(1 - m)**2)            # Appendix, Proof of Prop. 1
p1_match = sp.simplify(d_m - appendix_d_m) == 0

# ---------- Part A2: Prop. 2 ----------
d_mu = sp.simplify(sp.diff(kstar, m, u))
appendix_d_mu = g1 / (H*(1 - m)**2)                # Appendix, Proof of Prop. 2
p2_appendix_match = sp.simplify(d_mu - appendix_d_mu) == 0
numer_claim = g1*h0 - h1*(s + g0)                  # probe's claimed sign-bearing numerator
numer_ok = sp.simplify(d_mu*H**2*(1 - m)**2 - numer_claim) == 0
e = sp.symbols('e', positive=True)                 # A3 slack: h1/h0 = (1+e) g1/(s+g0), e > 0
numer_A3 = sp.simplify(numer_claim.subs(h1, g1*h0*(1 + e)/(s + g0)))
print("Prop 1: Appendix derivative equals re-derivation:", p1_match)
print("Prop 2: re-derived cross-partial:", sp.factor(d_mu))
print("Prop 2: Appendix expression equals re-derivation:", p2_appendix_match)
print("Prop 2: numerator equals g1*h0 - h1*(s+g0):", numer_ok, "| under A3 it is", numer_A3,
      "| symbolically negative:", numer_A3.is_negative)

# Numerical sweep over parameters satisfying A3 (and, for contrast, violating it)
args = (s, h0, h1, g0, g1, u, m)
f_dm = sp.lambdify(args, d_m, 'numpy')
f_dmu = sp.lambdify(args, d_mu, 'numpy')
rng = np.random.default_rng(1)
n = 200_000
S_ = rng.uniform(0.01, 2, n); H0 = rng.uniform(0.01, 2, n)
G0 = rng.uniform(0.01, 2, n); G1 = rng.uniform(0.01, 2, n)
U = rng.uniform(0, 5, n); M = rng.uniform(0, 0.99, n)
ratio = G1/(S_ + G0)
H1 = H0*ratio*rng.uniform(1.0001, 5, n)            # enforces A3: h1/h0 > g1/(s+g0)
H1r = H0*ratio*rng.uniform(0.01, 0.9999, n)        # A3 violated
share_dm_pos = np.mean(f_dm(S_, H0, H1, G0, G1, U, M) > 0)
share_dmu_neg = np.mean(f_dmu(S_, H0, H1, G0, G1, U, M) < 0)
share_dmu_pos_noA3 = np.mean(f_dmu(S_, H0, H1r, G0, G1, U, M) > 0)
print(f"Sweep: dk*/dm > 0 in {share_dm_pos:.4f} of A3 draws; d2k*/dmdu < 0 in {share_dmu_neg:.4f} of A3 draws;"
      f" d2k*/dmdu > 0 in {share_dmu_pos_noA3:.4f} of draws violating A3")

p1_ok = p1_match and share_dm_pos == 1.0
print("VERDICT: Prop. 1 —", "UPHELD (Appendix derivative correct; positive on the whole domain)" if p1_ok
      else "NOT UPHELD (see lines above)")
if (not p2_appendix_match) and numer_ok and share_dmu_neg == 1.0:
    print("VERDICT: Prop. 2 — REFUTED under the manuscript's own A3: the Appendix omits H'(u)=h1; "
          "the cross-partial has the sign of g1*h0 - h1*(s+g0), which A3 makes negative for all u>=0, m in [0,1).")
elif p2_appendix_match:
    print("VERDICT: Prop. 2 — Appendix expression matches the re-derivation; probe finding p10:fnd:3 not supported.")
else:
    print("VERDICT: Prop. 2 — INCONCLUSIVE (Appendix mismatch but sign under A3 not uniformly negative; inspect output).")

# ---------- Part B: H2 on the Phi scale (§2.4) ----------
# Phi(m,u) = F(k*(m,u)), F = CDF of spending-weighted specificity on [0,1]. Beta shapes are illustrative only:
# the manuscript does not state F, which is the point of p10:fnd:10.
par = dict(s=0.2, g0=0.3, g1=0.1, h0=1.0, h1=0.5)   # A3: 0.5 > 0.1/0.5 = 0.2
assert par['h1']/par['h0'] > par['g1']/(par['s'] + par['g0'])
def kst(mm, uu, p=par):
    return (p['s'] + p['g0'] + p['g1']*uu) / ((p['h0'] + p['h1']*uu)*(1 - mm))
def Phi(mm, uu, a, b):
    return stats.beta.cdf(np.minimum(kst(mm, uu), 1.0), a, b)
def mixed(f, mm, uu, h=1e-4):
    return (f(mm+h, uu+h) - f(mm+h, uu-h) - f(mm-h, uu+h) + f(mm-h, uu-h)) / (4*h*h)
rows = []
for (a, b) in [(1, 1), (2, 5), (5, 2), (2, 2), (0.5, 0.5)]:
    for mm in np.linspace(0.05, 0.5, 10):
        for uu in np.linspace(0.01, 3.0, 10):
            if kst(mm, uu) >= 1 - 1e-3:
                continue                                   # corner: all functions outsourced
            kmu = float(f_dmu(par['s'], par['h0'], par['h1'], par['g0'], par['g1'], uu, mm))
            phimu = mixed(lambda x, y: Phi(x, y, a, b), mm, uu)
            rows.append((a, b, np.sign(kmu), np.sign(phimu)))
rows = np.array(rows)
for (a, b) in sorted(set(map(tuple, rows[:, :2]))):
    sel = (rows[:, 0] == a) & (rows[:, 1] == b)
    print(f"Part B Beta({a},{b}): sign disagreement in {np.mean(rows[sel, 2] != rows[sel, 3]):.2f} of {sel.sum()} interior points")
dis = np.mean(rows[:, 2] != rows[:, 3])
print("VERDICT: H2 scale —", (f"sign of the Phi-scale interaction differs from sign of d2k*/dmdu at {dis:.0%} of interior points; "
      "Prop. 2 alone does not fix the sign on the tested scale") if dis > 0 else
      "sign of the Phi-scale interaction matched sign of d2k*/dmdu at every interior point tried; p10:fnd:10 not supported for these densities")
