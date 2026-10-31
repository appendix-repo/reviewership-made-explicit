# CheckSpec p08:chk:1: threshold derivation, Proposition 1, model domain
# Settles: p08:S1, p08:S2 (Prop. 1 part), p08:fnd:8
# Premises, from the manuscript only:
#   ms:§2.2  C_B = p - s + H(u) k (1-m);  C_M = p + G(u)
#   ms:§2.2  H(u) = h0 + h1 u;  G(u) = g0 + g1 u;  s, h0, h1, g0, g1 > 0;  u >= 0;  m in [0,1)
#   ms:§2.3  buy iff C_B < C_M iff k < k* = (s + G(u)) / (H(u)(1-m))
#   ms:App   dk*/dm = (s + G(u)) / (H(u)(1-m)^2) > 0
#   ms:§3.2  u is "standardized to mean zero and unit variance" (negative values occur)
import sympy as sp
import numpy as np

p, s, g0, g1, h0, h1, k = sp.symbols('p s g0 g1 h0 h1 k', positive=True)
u = sp.symbols('u', nonnegative=True)
m = sp.symbols('m', real=True)
w = sp.symbols('w', positive=True)            # w = 1 - m > 0 on m in [0,1)

G = g0 + g1*u
H = h0 + h1*u
CB = p - s + H*k*(1 - m)
CM = p + G
kstar = (s + G) / (H*(1 - m))

# (a) Threshold: C_M - C_B = H(1-m)(k* - k), and H(1-m) > 0 on the domain
identity = sp.simplify((CM - CB) - H*(1 - m)*(kstar - k))
ok_threshold = (identity == 0)
factor_positive = (sp.simplify(H*w).is_positive is True)
print("C_M - C_B - H(1-m)(k*-k) simplifies to:", identity)
print("H(u)(1-m) > 0 on domain:", factor_positive)

# (b) Proposition 1: the Appendix expression and its sign
dk_dm = sp.diff(kstar, m)
appendix_P1 = (s + G) / (H*(1 - m)**2)
ok_P1_expr = (sp.simplify(dk_dm - appendix_P1) == 0)
ok_P1_sign = (sp.simplify(appendix_P1.subs(m, 1 - w)).is_positive is True)
print("dk*/dm =", sp.simplify(dk_dm), "| matches Appendix:", ok_P1_expr, "| positive on domain:", ok_P1_sign)

# numeric cross-check on random admissible draws
rng = np.random.default_rng(8)
f_k = sp.lambdify((s, g0, g1, h0, h1, u, m), kstar, 'numpy')
f_d = sp.lambdify((s, g0, g1, h0, h1, u, m), appendix_P1, 'numpy')
n = 20000
S, G0, G1, H0, H1 = (rng.uniform(0.05, 3.0, n) for _ in range(5))
U = rng.uniform(0.0, 5.0, n)
M = rng.uniform(0.0, 0.95, n)
eps = 1e-6
fd = (f_k(S, G0, G1, H0, H1, U, M + eps) - f_k(S, G0, G1, H0, H1, U, M - eps)) / (2*eps)
an = f_d(S, G0, G1, H0, H1, U, M)
num_ok = bool(np.allclose(fd, an, rtol=1e-4, atol=1e-8) and (an > 0).all())
print("numeric: finite differences match Appendix dk*/dm and all > 0:", num_ok)

# (c) Domain: the measured u is a z-score (ms:§3.2), but the model needs H(u) > 0
z = sp.symbols('z', real=True)
root = sp.solve(sp.Eq(h0 + h1*z, 0), z)[0]           # H = 0 at z = -h0/h1
example = {h0: 1, h1: sp.Rational(1, 2)}
H_at = (h0 + h1*(-3)).subs(example)                    # a hospital 3 SD below mean uncertainty
flip = bool(H_at < 0)
print("H(z) = 0 at z =", root, "| example h0=1, h1=1/2, z=-3: H =", H_at,
      "-> C_M - C_B = H(1-m)(k*-k) means buy iff k > k* (rule reverses):", flip)
print("k* at m = 1:", kstar.subs(m, 1))

print("VERDICT: p08:S1 threshold derivation", "CONFIRMED" if (ok_threshold and factor_positive) else "NOT CONFIRMED")
print("VERDICT: p08:S2 Proposition 1 (expression and sign)",
      "CONFIRMED" if (ok_P1_expr and (ok_P1_sign or num_ok) and num_ok) else "NOT CONFIRMED")
print("VERDICT: p08:fnd:8",
      "DEMONSTRATED: with u measured as a z-score, H(u) <= 0 is possible (u <= -h0/h1) and the buy rule reverses; k* undefined at m = 1"
      if flip else "NOT DEMONSTRATED")
