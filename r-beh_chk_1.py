import numpy as np
import sympy as sp

s, g0, g1, h0, h1, u = sp.symbols('s g0 g1 h0 h1 u', positive=True)
m = sp.symbols('m', real=True)
G = g0 + g1*u
H = h0 + h1*u
kstar = (s + G) / (H*(1 - m))            # ms:§2.3

k_m  = sp.diff(kstar, m)
k_u  = sp.diff(kstar, u)
k_mu = sp.diff(kstar, m, u)

# (a) Prop 1: Appendix expression for dk*/dm
print("(a) Prop1 expression matches:", sp.simplify(k_m - (s + G)/(H*(1 - m)**2)) == 0)

# (b) Prop 2: Appendix expression g1/(H(1-m)^2)
print("(b) Appendix Prop2 expression matches:", sp.simplify(k_mu - g1/(H*(1 - m)**2)) == 0)
num_mu = sp.simplify(k_mu * H**2 * (1 - m)**2)
num_u  = sp.simplify(k_u  * H**2 * (1 - m))
target = g1*h0 - h1*(s + g0)
print("    numerator of k_mu:", sp.expand(num_mu))
print("    k_mu numerator == g1*h0 - h1*(s+g0):", sp.simplify(num_mu - target) == 0)
print("    k_u  numerator == g1*h0 - h1*(s+g0):", sp.simplify(num_u - target) == 0)
# A3: h1/h0 > g1/(s+g0)  <=>  h1*(s+g0) > g1*h0  <=>  target < 0 (all parameters positive)

# (b') numerical spot-check on random parameter draws satisfying A3
rng = np.random.default_rng(20261023)
N = 200000
S, G0, G1, H0, H1 = (rng.uniform(0.01, 5, N) for _ in range(5))
U = rng.uniform(0, 10, N); M = rng.uniform(0, 0.99, N)
a3 = H1/H0 > G1/(S + G0)
f_kmu = sp.lambdify((s, g0, g1, h0, h1, u, m), k_mu, 'numpy')
f_ku  = sp.lambdify((s, g0, g1, h0, h1, u, m), k_u, 'numpy')
v_mu = f_kmu(S, G0, G1, H0, H1, U, M); v_u = f_ku(S, G0, G1, H0, H1, U, M)
print("(b') A3 draws:", int(a3.sum()),
      "| share k_mu<0:", float((v_mu[a3] < 0).mean()),
      "| share k_u<0:", float((v_u[a3] < 0).mean()))
print("     non-A3 draws: share k_mu>0:", float((v_mu[~a3] > 0).mean()))

# (c) Phi scale: Phi = F(k*), F = spending-weighted CDF of nominal k
x = sp.Symbol('x')
F = sp.Function('F')
Phi_mu = sp.diff(F(kstar), m, u)
decomp = (sp.diff(F(x), x, 2).subs(x, kstar) * k_m * k_u
          + sp.diff(F(x), x).subs(x, kstar) * k_mu)
print("(c) Phi_mu == F''(k*) k_m k_u + F'(k*) k_mu:", sp.simplify((Phi_mu - decomp).doit()) == 0)
# Uniform F on [0,1], interior k*: Phi = k*, so Phi_mu = k_mu (negative under A3)
