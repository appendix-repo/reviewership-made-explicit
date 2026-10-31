from scipy import stats

s, g0, g1, h0, h1 = 1.0, 1.0, 0.5, 1.0, 2.0      # A3: h1/h0 = 2 > g1/(s+g0) = 0.25
def kstar(m, u): return (s + g0 + g1*u) / ((h0 + h1*u) * (1 - m))
def Phi(m, u, dist): return dist.cdf(min(kstar(m, u), 1.0))
def cross(m, u, dist, e=1e-4):
    return (Phi(m+e, u+e, dist) - Phi(m+e, u-e, dist)
            - Phi(m-e, u+e, dist) + Phi(m-e, u-e, dist)) / (4*e*e)

dists = {"Uniform(0,1)": stats.uniform(), "Beta(2,5)": stats.beta(2, 5), "Beta(5,2)": stats.beta(5, 2)}
for name, dist in dists.items():
    for m, u in [(0.1, 5.0), (0.1, 3.0), (0.2, 2.0), (0.3, 3.0)]:
        print(f"{name:12s} m={m} u={u} k*={kstar(m, u):.3f} d2Phi/dmdu={cross(m, u, dist):+.4f}")
