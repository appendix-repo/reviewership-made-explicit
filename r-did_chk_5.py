import numpy as np
from scipy import stats

# Parameters chosen to satisfy A3: h1/h0 = 0.5 > g1/(s+g0) = 0.2
s, g0, g1, h0, h1 = 0.2, 0.3, 0.1, 1.0, 0.5
assert h1/h0 > g1/(s + g0)

def kstar(m, u):
    return (s + g0 + g1*u) / ((h0 + h1*u) * (1 - m))

def Phi(m, u, dist):
    # spending-weighted share of functions with k < k*, k distributed on [0,1]
    return dist.cdf(np.minimum(kstar(m, u), 1.0))

def cross(f, m, u, e=1e-4):
    return (f(m+e, u+e) - f(m+e, u-e) - f(m-e, u+e) + f(m-e, u-e)) / (4*e*e)

dists = {"uniform": stats.uniform(0, 1), "beta(2,2)": stats.beta(2, 2),
         "beta(5,2)": stats.beta(5, 2), "beta(1,3)": stats.beta(1, 3), "beta(2,5)": stats.beta(2, 5)}

for M, U in [(0.3, 0.0), (0.2, 0.5), (0.1, 1.0)]:
    ks = kstar(M, U)
    print(f"\nm={M}, u={U}: k*={ks:.3f} (interior: {ks < 1}), k*_mu={cross(kstar, M, U):+.4f}")
    for name, dist in dists.items():
        val = cross(lambda a, b: Phi(a, b, dist), M, U)
        print(f"  {name:10s} Phi_mu = {val:+.5f}")
