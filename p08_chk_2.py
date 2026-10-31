# CheckSpec p08:chk:2: Proposition 2, its Appendix proof, A3, and the §2.3 intuition
# Settles: p08:fnd:1, p08:fnd:2 (sign on k*), p08:fnd:3; also p08:inc:1, p08:inc:2
# Premises, from the manuscript only:
#   ms:§2.2  H(u) = h0 + h1 u;  G(u) = g0 + g1 u;  s, h0, h1, g0, g1 > 0;  u >= 0;  m in [0,1)
#   ms:§2.2  Assumption A3: h1/h0 > g1/(s + g0)
#   ms:§2.2  C_B = p - s + H(u) k (1-m);  C_M = p + G(u)
#   ms:§2.3  k* = (s + G(u)) / (H(u)(1-m));  Prop. 2 claims d2k*/dm du > 0
#   ms:App   "d2k*/dm du = G'(u)/(H(u)(1-m)^2) = g1/(H(u)(1-m)^2) > 0"
import sympy as sp
import numpy as np

s, g0, g1, h0, h1, k = sp.symbols('s g0 g1 h0 h1 k', positive=True)
u = sp.symbols('u', nonnegative=True)
m = sp.symbols('m', real=True)
w = sp.symbols('w', positive=True)            # w = 1 - m

G = g0 + g1*u
H = h0 + h1*u
kstar = (s + G) / (H*(1 - m))

# (1) Full cross-partial vs the Appendix expression
cross = sp.diff(kstar, m, u)
appendix_P2 = g1 / (H*(1 - m)**2)
Delta = g1*h0 - h1*(s + g0)
closed = Delta / (H**2 * (1 - m)**2)
ok_closed = (sp.simplify(cross - closed) == 0)
appendix_matches = (sp.simplify(cross - appendix_P2) == 0)
omitted = sp.simplify(cross - appendix_P2)
ok_omitted = (sp.simplify(omitted - (-(s + G)*h1 / (H**2 * (1 - m)**2))) == 0)
appendix_ok_only_if_h1_zero = (sp.simplify((cross - appendix_P2).subs(h1, 0)) == 0)
print("full cross-partial      =", sp.factor(sp.simplify(cross)))
print("closed form Delta/(H^2(1-m)^2), Delta = g1*h0 - h1*(s+g0); matches:", ok_closed)
print("Appendix expression matches full cross-partial:", appendix_matches)
print("term omitted by Appendix =", sp.factor(omitted), "| equals -(s+G)h1/(H^2(1-m)^2):", ok_omitted)
print("Appendix expression correct when h1 = 0 (excluded by ms:§2.2):", appendix_ok_only_if_h1_zero)

# (2) A3 is equivalent to Delta < 0: (h1/h0 - g1/(s+g0)) * h0 (s+g0) = -Delta
ok_A3_equiv = (sp.simplify((h1/h0 - g1/(s + g0))*h0*(s + g0) + Delta) == 0)
denom_pos = ((H**2 * w**2).is_positive is True)
print("A3 <=> Delta < 0:", ok_A3_equiv, "| denominator H^2(1-m)^2 > 0:", denom_pos)

# (3) dk*/du has the same sign (Prop. 2 <=> uncertainty widens outsourcing; inc:2)
ok_dkdu = (sp.simplify(sp.diff(kstar, u) - Delta / (H**2 * (1 - m))) == 0)
print("dk*/du = Delta/(H^2(1-m)):", ok_dkdu)

# (4) Worked example satisfying A3, with finite differences independent of sympy algebra
f_k = sp.lambdify((s, g0, g1, h0, h1, u, m), kstar, 'numpy')
f_c = sp.lambdify((s, g0, g1, h0, h1, u, m), closed, 'numpy')
f_a = sp.lambdify((s, g0, g1, h0, h1, u, m), appendix_P2, 'numpy')

def fd_cross(par, U, M, e=1e-4):
    return (f_k(*par, U + e, M + e) - f_k(*par, U - e, M + e)
            - f_k(*par, U + e, M - e) + f_k(*par, U - e, M - e)) / (4*e*e)

par = (1.0, 1.0, 1.0, 1.0, 2.0)               # s, g0, g1, h0, h1
print("example A3 holds (h1/h0 = 2 > g1/(s+g0) = 0.5):", par[4]/par[3] > par[2]/(par[0] + par[1]))
ex_ok = True
for U0 in (0.0, 0.5, 1.0, 2.0, 5.0):
    for M0 in (0.0, 0.25, 0.5, 0.75):
        fdv, cv, av = fd_cross(par, U0, M0), f_c(*par, U0, M0), f_a(*par, U0, M0)
        ex_ok = ex_ok and np.isclose(fdv, cv, rtol=1e-4) and fdv < 0
        print(f"  u={U0:.2f} m={M0:.2f}  finite-diff={fdv:+.5f}  closed={cv:+.5f}  Appendix={av:+.5f}")

# (5) Random admissible draws: sign of the cross-partial with and without A3
rng = np.random.default_rng(208)
n = 100000
Sx, G0x, G1x, H0x, H1x = rng.uniform(0.2, 3.0, size=(5, n))
Ux = rng.uniform(0.0, 5.0, n)
Mx = rng.uniform(0.0, 0.9, n)
cx = f_c(Sx, G0x, G1x, H0x, H1x, Ux, Mx)
a3 = H1x/H0x > G1x/(Sx + G0x)
n_a3, n_a3_pos = int(a3.sum()), int((cx[a3] > 0).sum())
n_not, n_not_pos = int((~a3).sum()), int((cx[~a3] > 0).sum())
idx = np.arange(5000)
fdx = fd_cross((Sx[idx], G0x[idx], G1x[idx], H0x[idx], H1x[idx]), Ux[idx], Mx[idx])
fd_ok = bool(np.allclose(fdx, cx[idx], rtol=1e-3, atol=1e-3))   # atol covers round-off where Delta is near 0
print(f"draws with A3: {n_a3}, of which cross-partial > 0: {n_a3_pos}")
print(f"draws without A3: {n_not}, of which cross-partial > 0: {n_not_pos}")
print("finite differences agree with closed form on 5000 draws:", fd_ok)

# (6) §2.3 intuition: per-function cost saving vs threshold
saving = (G) - (-s + H*k*(1 - m))             # C_M - C_B, p cancels
ok_saving = (sp.simplify(sp.diff(saving, m, u) - h1*k) == 0)
ok_prop = (sp.simplify(sp.diff(kstar, m) - kstar/(1 - m)) == 0)
print("d2(C_M - C_B)/dm du = h1*k > 0:", ok_saving, "| dk*/dm = k*/(1-m):", ok_prop)

fnd1 = (ok_closed and not appendix_matches and ok_omitted and ok_A3_equiv and denom_pos
        and n_a3_pos == 0 and ex_ok and fd_ok)
print("VERDICT: p08:fnd:1",
      "DEMONSTRATED: Appendix omits -(s+G)h1/(H^2(1-m)^2); true cross-partial = (g1*h0 - h1*(s+g0))/(H^2(1-m)^2); "
      "A3 <=> numerator < 0, so Prop. 2 is false at every admissible (m,u) under A3" if fnd1 else "NOT DEMONSTRATED")
print("VERDICT: p08:inc:2",
      "DEMONSTRATED: Prop. 2 holds iff A3 fails iff dk*/du > 0 (uncertainty favours the market)"
      if (ok_dkdu and n_not_pos == n_not and n_a3_pos == 0) else "NOT DEMONSTRATED")
print("VERDICT: p08:fnd:2",
      "DEMONSTRATED (k* scale): the correctly derived model under A3 predicts a NEGATIVE m x u interaction "
      "(same sign as ms:T2.M3, -0.061) and dk*/du < 0" if (fnd1 and ok_dkdu) else "NOT DEMONSTRATED")
print("VERDICT: p08:fnd:3",
      "DEMONSTRATED: modularity's per-function cost saving rises with u (h1*k > 0), but its threshold effect is "
      "k*/(1-m), which falls with u under A3" if (ok_saving and ok_prop and fnd1) else "NOT DEMONSTRATED")
