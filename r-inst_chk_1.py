import sympy as sp

s, g0, g1, h0, h1, u, m = sp.symbols('s g0 g1 h0 h1 u m', positive=True)
G = g0 + g1*u
H = h0 + h1*u
kstar = (s + G) / (H*(1 - m))                      # ms:S2.3

# Proposition 1
d_m = sp.diff(kstar, m)
assert sp.simplify(d_m - (s + G)/(H*(1 - m)**2)) == 0
print("P1: dk*/dm =", sp.simplify(d_m), "(positive for m<1)")

# Proposition 2
d_mu = sp.diff(kstar, m, u)
ms_claim = g1/(H*(1 - m)**2)                       # ms:Appendix
print("P2: true cross-partial =", sp.factor(sp.simplify(d_mu)))
print("P2: true minus manuscript formula =", sp.simplify(d_mu - ms_claim))
target = (g1*h0 - h1*(s + g0)) / (H**2 * (1 - m)**2)
assert sp.simplify(d_mu - target) == 0
print("Numerator g1*h0 - h1*(s+g0) < 0  <=>  h1/h0 > g1/(s+g0)  (= A3)")

# Numeric spot-check at a point where A3 holds
vals = {s: 1, g0: 1, g1: 0.5, h0: 1, h1: 2, u: 0.7, m: 0.3}
assert vals[h1]/vals[h0] > vals[g1]/(vals[s] + vals[g0])
print("true value:", float(d_mu.subs(vals)), " manuscript formula:", float(ms_claim.subs(vals)))
