import numpy as np
from scipy import stats

def kstar(m, u, s, g0, g1, h0, h1):
    return (s + g0 + g1*u) / ((h0 + h1*u) * (1 - m))

def kmu(m, u, s, g0, g1, h0, h1):        # closed form from r-tce:chk:1
    H = h0 + h1*u
    return (g1*h0 - h1*(s + g0)) / (H**2 * (1 - m)**2)

def Phi(m, u, F, p):
    return F.cdf(np.clip(kstar(m, u, **p), 0.0, 1.0))

def cross(m, u, F, p, e=1e-3):
    f = lambda a, b: Phi(a, b, F, p)
    return (f(m+e, u+e) - f(m+e, u-e) - f(m-e, u+e) + f(m-e, u-e)) / (4*e*e)

params = {"A3 holds":    dict(s=0.2, g0=0.2, g1=0.05, h0=1.0, h1=0.5),
          "A3 violated": dict(s=0.2, g0=0.2, g1=0.30, h0=1.0, h1=0.05)}
dists = {"uniform": stats.beta(1, 1), "Beta(2,5)": stats.beta(2, 5), "Beta(5,2)": stats.beta(5, 2)}
grid = [(mm, uu) for mm in (0.1, 0.3, 0.5) for uu in (0.2, 0.5, 1.0)]
for pn, p in params.items():
    ksign = ["+" if kmu(mm, uu, **p) > 0 else "-" for mm, uu in grid]
    for dn, F in dists.items():
        psign = ["sat" if kstar(mm, uu, **p) >= 1 else ("+" if cross(mm, uu, F, p) > 0 else "-") for mm, uu in grid]
        diff = sum(a != b for a, b in zip(ksign, psign) if b != "sat")
        print(f"{pn:12s} {dn:10s} k*_mu: {ksign}  Phi_mu: {psign}  sign differences: {diff}")
