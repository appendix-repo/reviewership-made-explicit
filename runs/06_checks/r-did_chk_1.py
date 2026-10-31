import sympy as sp
import numpy as np

m, u = sp.symbols('m u', real=True)
s, h0, g0, g1, d = sp.symbols('s h0 g0 g1 delta', positive=True)
h1 = sp.symbols('h1', positive=True)

H = h0 + h1*u
G = g0 + g1*u
kstar = (s + G) / (H*(1 - m))

k_m  = sp.simplify(sp.diff(kstar, m))
k_u  = sp.simplify(sp.diff(kstar, u))
k_mu = sp.simplify(sp.diff(kstar, m, u))

# Prop. 1: compare with the appendix expression
app_k_m = (s + G) / (H*(1 - m)**2)
print("Prop1 matches appendix:", sp.simplify(k_m - app_k_m) == 0)

# Prop. 2: appendix expression versus the full derivative
app_k_mu = g1 / (H*(1 - m)**2)
print("Prop2 appendix expression equals full derivative:", sp.simplify(k_mu - app_k_mu) == 0)

num_mu = sp.expand(sp.simplify(k_mu * H**2 * (1 - m)**2))
num_u  = sp.expand(sp.simplify(k_u  * H**2 * (1 - m)))
print("numerator of k_mu:", num_mu)
print("numerator of k_u :", num_u)
target = sp.expand(g1*h0 - h1*(s + g0))
print("k_mu numerator == g1*h0 - h1*(s+g0):", sp.simplify(num_mu - target) == 0)
print("k_u  numerator == g1*h0 - h1*(s+g0):", sp.simplify(num_u - target) == 0)

# Impose A3 as h1 = h0*g1*(1+delta)/(s+g0), delta > 0
A3 = {h1: h0*g1*(1 + d)/(s + g0)}
num_A3 = sp.simplify(target.subs(A3))
print("numerator under A3:", num_A3, "| is_negative:", num_A3.is_negative)

# Numeric sweep over A3-satisfying parameters, m in [0, 0.99), u in [0, 5]
rng = np.random.default_rng(0)
f_kmu = sp.lambdify((m, u, s, h0, h1, g0, g1), k_mu, 'numpy')
signs = []
for _ in range(20000):
    S, H0, G0, G1 = rng.uniform(0.01, 3, 4)
    H1 = H0*G1/(S + G0)*(1 + rng.uniform(0.001, 5))
    M, U = rng.uniform(0, 0.99), rng.uniform(0, 5)
    signs.append(np.sign(f_kmu(M, U, S, H0, H1, G0, G1)))
signs = np.array(signs)
print("share of A3 draws with k_mu < 0:", np.mean(signs < 0))
print("share of A3 draws with k_mu > 0:", np.mean(signs > 0))
