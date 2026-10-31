import sympy as sp
import numpy as np

m, u, s, g0, g1, h0, h1 = sp.symbols('m u s g0 g1 h0 h1', positive=True)
G = g0 + g1*u
H = h0 + h1*u
kstar = (s + G) / (H * (1 - m))          # ms:TEST §2.3

# Proposition 1
k_m = sp.diff(kstar, m)
ms_k_m = (s + G) / (H * (1 - m)**2)       # ms:TEST Appendix
print("P1 equals manuscript expression:", sp.simplify(k_m - ms_k_m) == 0)

# Proposition 2
k_mu = sp.diff(kstar, m, u)
ms_k_mu = g1 / (H * (1 - m)**2)           # ms:TEST Appendix
print("P2 equals manuscript expression:", sp.simplify(k_mu - ms_k_mu) == 0)
scaled = sp.simplify(k_mu * H**2 * (1 - m)**2)
print("k*_mu * H^2 (1-m)^2 =", sp.expand(scaled))
print("Scaled numerator equals g1*h0 - h1*(s+g0):", sp.simplify(scaled - (g1*h0 - h1*(s + g0))) == 0)
print("Identity k*_mu == k*_u/(1-m):", sp.simplify(k_mu - sp.diff(kstar, u)/(1 - m)) == 0)
# A3: h1/h0 > g1/(s+g0)  <=>  g1*h0 - h1*(s+g0) < 0  <=>  k*_mu < 0

vals = {s: 1.0, g0: 1.0, g1: 0.5, h0: 1.0, h1: 1.0, m: 0.5, u: 1.0}
print("A3 holds at illustration point:", vals[h1]/vals[h0] > vals[g1]/(vals[s] + vals[g0]))
print("true k*_mu:", float(k_mu.subs(vals)), " manuscript k*_mu:", float(ms_k_mu.subs(vals)))

rng = np.random.default_rng(0)
f = sp.lambdify((m, u, s, g0, g1, h0, h1), k_mu, 'numpy')
D = rng.uniform(0.01, 3, size=(100000, 7))
D[:, 0] = rng.uniform(0, 0.99, 100000)    # m in [0,1)
a3 = D[:, 6]/D[:, 5] > D[:, 4]/(D[:, 2] + D[:, 3])
v = f(*D.T)
print("A3 draws:", int(a3.sum()), " share with k*_mu < 0:", float(np.mean(v[a3] < 0)))
print("non-A3 draws: share with k*_mu > 0:", float(np.mean(v[~a3] > 0)))
