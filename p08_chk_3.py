# CheckSpec p08:chk:3: from the threshold k* to the tested outcome Phi (ms:§2.4)
# Settles: p08:fnd:4; p08:S2 (H1 part)
# Premises, from the manuscript only:
#   ms:§2.4  "Let Phi denote the share of a hospital's IT functions, weighted by spending, that are outsourced"
#            "functions with k<k* are outsourced"  =>  Phi = F(k*), F the spending-weighted CDF of nominal k
#            (the manuscript states no assumption on F; we take F fixed in m and u, as §2.4 implicitly needs)
#   ms:§2.2/§2.3  H, G linear; s, h0, h1, g0, g1 > 0; u >= 0; m in [0,1); k* = (s+G)/(H(1-m)); A3
#   ms:§3.2  mean outsourcing share 0.31, SD 0.17
import sympy as sp
import numpy as np
from scipy import stats

s, g0, g1, h0, h1 = sp.symbols('s g0 g1 h0 h1', positive=True)
u = sp.symbols('u', nonnegative=True)
m = sp.symbols('m', real=True)
f, fp = sp.symbols('f fp', real=True)          # f = F'(k*) >= 0, fp = F''(k*)

G = g0 + g1*u
H = h0 + h1*u
kstar = (s + G) / (H*(1 - m))
k_m, k_u, k_mu = sp.diff(kstar, m), sp.diff(kstar, u), sp.diff(kstar, m, u)
Delta = g1*h0 - h1*(s + g0)

# chain rule for Phi = F(k*(m,u))
dPhi_dm = f*k_m
dPhi_du = f*k_u
d2Phi = fp*k_m*k_u + f*k_mu
ok_identity = (sp.simplify(d2Phi - Delta/(H**2*(1 - m)**2)*(f + kstar*fp)) == 0)
ok_dm = (sp.simplify(dPhi_dm - f*kstar/(1 - m)) == 0)
ok_du = (sp.simplify(dPhi_du - f*Delta/(H**2*(1 - m))) == 0)
print("d2Phi/dm du = Delta/(H^2(1-m)^2) * (f(k*) + k* f'(k*)):", ok_identity)
print("dPhi/dm = f(k*) k*/(1-m) >= 0 for any F:", ok_dm)
print("dPhi/du = f(k*) Delta/(H^2(1-m)) (<= 0 under A3, any F):", ok_du)

# Explicit distributions at one admissible point satisfying A3
par = dict(s=0.2, g0=0.2, g1=0.1, h0=1.0, h1=1.0)
a3 = par['h1']/par['h0'] > par['g1']/(par['s'] + par['g0'])

def kst(U, M):
    return (par['s'] + par['g0'] + par['g1']*U) / ((par['h0'] + par['h1']*U)*(1 - M))

def cross_fd(fun, U, M, e=1e-4):
    return (fun(U + e, M + e) - fun(U - e, M + e) - fun(U + e, M - e) + fun(U - e, M - e)) / (4*e*e)

U0, M0 = 1.0, 0.375
k0 = kst(U0, M0)                                # = 0.4, interior
Dl = par['g1']*par['h0'] - par['h1']*(par['s'] + par['g0'])
base = Dl / ((par['h0'] + par['h1']*U0)**2 * (1 - M0)**2)
c_k = cross_fd(kst, U0, M0)
print(f"A3 holds: {a3}; k* = {k0:.4f}; d2k*/dm du: finite-diff {c_k:+.5f}, closed {base:+.5f}")

dists = {"uniform(0,1)": stats.uniform(0, 1), "beta(2,2)": stats.beta(2, 2), "beta(1,5)": stats.beta(1, 5)}
sign = {}
agree = True
for name, d in dists.items():
    Phi = lambda U, M, d=d: d.cdf(np.minimum(kst(U, M), 1.0))
    c_fd = cross_fd(Phi, U0, M0)
    e = 1e-5
    kf_slope = ((k0 + e)*d.pdf(k0 + e) - (k0 - e)*d.pdf(k0 - e)) / (2*e)   # f + k f' at k*
    c_formula = base*kf_slope
    agree = agree and np.isclose(c_fd, c_formula, rtol=1e-3, atol=1e-6)
    sign[name] = np.sign(c_fd)
    print(f"  {name:13s} Phi={d.cdf(k0):.3f}  f+k f'={kf_slope:+.4f}  d2Phi/dm du: finite-diff {c_fd:+.5f}, formula {c_formula:+.5f}")

# Where in the beta(1,5) family does the sign on Phi flip? f + k f' = 5(1-k)^3(1-5k) < 0 iff k > 0.2
phi_flip = 1 - 0.8**5
print(f"beta(1,5): Phi-scale sign flips for hospitals with Phi > {phi_flip:.3f} "
      f"({(phi_flip - 0.31)/0.17:.2f} SD above the ms:§3.2 mean of 0.31)")

fnd4 = (ok_identity and a3 and agree and c_k < 0
        and sign["uniform(0,1)"] < 0 and sign["beta(2,2)"] < 0 and sign["beta(1,5)"] > 0)
print("VERDICT: p08:fnd:4",
      "DEMONSTRATED: under A3 the k*-scale interaction is negative, but the Phi-scale interaction has sign "
      "sign(Delta)*sign(f + k f'), positive for beta(1,5) at k* = 0.4; the step from Prop. 2 to H2 needs an assumption on F"
      if fnd4 else "NOT DEMONSTRATED")
print("VERDICT: p08:S2 (H1 part)",
      "CONFIRMED: dPhi/dm = f(k*) k*/(1-m) >= 0 for every spending-weighted F; H1 follows from Prop. 1 without further assumption"
      if ok_dm else "NOT CONFIRMED")
