import numpy as np

rng = np.random.default_rng(42)

def twoway_demean(x):
    return x - x.mean(1, keepdims=True) - x.mean(0, keepdims=True) + x.mean()

def ols(y, *xs):
    X = np.column_stack([twoway_demean(x).ravel() for x in xs])
    return np.linalg.lstsq(X, twoway_demean(y).ravel(), rcond=None)[0]

# Scenario A: true modularity effect = 0; time-varying capability w confounds m and Phi;
# staffing is reduced one-for-one by outsourcing (the manuscript's own account, ms:S3.2).
N, T, R = 412, 11, 200
resA = []
for _ in range(R):
    alpha = rng.normal(0, 0.1, (N, 1))
    w = np.cumsum(rng.normal(0, 0.3, (N, T)), axis=1)          # time-varying capability
    m = 0.4 + 0.5*w + rng.normal(0, 0.5, (N, T))
    phi = alpha + 0.0*m + 0.3*w + rng.normal(0, 0.5, (N, T))   # beta_m = 0
    staff = -1.0*phi + 0.2*w + rng.normal(0, 0.2, (N, T))
    resA.append((ols(phi, m)[0], ols(phi, m, staff)[0]))
resA = np.array(resA)
print("Scenario A (true beta_m = 0)")
print("  beta_m without staffing: mean %.3f, sd %.3f" % (resA[:, 0].mean(), resA[:, 0].std()))
print("  beta_m with staffing   : mean %.3f, sd %.3f" % (resA[:, 1].mean(), resA[:, 1].std()))

# Scenario B: no direct peer effect on Phi. Modularity diffuses ONLY by imitation of
# peers' lagged outsourcing (leave-one-out same-state mean), and Phi depends on m.
S, T, R = 50, 11, 200
resB = []
for _ in range(R):
    state = np.concatenate([np.arange(S), rng.integers(0, S, 412 - S)])   # every state >= 1, most >= 2
    N = state.size
    a_s = rng.normal(0, 0.1, S)
    alpha = 0.3 + a_s[state] + rng.normal(0, 0.05, N)
    beta, kappa = 0.1, 0.1
    m = np.zeros((N, T + 1)); phi = np.zeros((N, T + 1)); peer = np.full((N, T + 1), np.nan)
    m[:, 0] = rng.uniform(0.1, 0.4, N)
    phi[:, 0] = alpha + beta*m[:, 0] + rng.normal(0, 0.03, N)
    for t in range(1, T + 1):
        tot = np.bincount(state, phi[:, t-1], minlength=S)
        cnt = np.bincount(state, minlength=S)
        loo = np.where(cnt[state] > 1, (tot[state] - phi[:, t-1]) / np.maximum(cnt[state] - 1, 1), np.nan)
        peer[:, t] = loo
        m[:, t] = m[:, t-1] + kappa*np.nan_to_num(loo, nan=phi[:, t-1]) + rng.normal(0, 0.02, N)
        phi[:, t] = alpha + beta*m[:, t] + rng.normal(0, 0.03, N)
    keep = ~np.isnan(peer[:, 1:]).any(axis=1)          # drop single-hospital states
    P, M_, F = peer[keep, 1:], m[keep, 1:], phi[keep, 1:]
    resB.append((ols(F, P)[0], ols(F, P, M_)[0], ols(F, P, M_)[1]))
resB = np.array(resB)
print("Scenario B (all diffusion of m is imitation; no direct peer effect on Phi)")
print("  peer coef without m: mean %.3f, sd %.3f" % (resB[:, 0].mean(), resB[:, 0].std()))
print("  peer coef with m   : mean %.3f, sd %.3f" % (resB[:, 1].mean(), resB[:, 1].std()))
print("  m coef with peer   : mean %.3f (true beta = 0.1)" % resB[:, 2].mean())
