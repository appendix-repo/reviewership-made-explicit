# p09:chk:7 -- reverse timing: does within-hospital FE exclude same-year feedback from outsourcing to modularity? (P-ID)
import numpy as np
import statsmodels.api as sm

rng = np.random.default_rng(2026102307)
N, S, REPS = 412, 50, 200                # ms:§3.1: 412 hospitals. ASSUMPTION: 50 states
years = np.arange(2009, 2020)            # ms:§3.1
T = years.size
state = np.arange(N) % S


def demean2(X):
    return X - X.mean(axis=1, keepdims=True) - X.mean(axis=0, keepdims=True) + X.mean()


def simulate(beta, pi):
    adopt = np.full(S, 9999)
    adopters = rng.permutation(S)[:40]                    # ASSUMPTION: 40 of 50 states adopt
    adopt[adopters] = rng.integers(2011, 2017, size=40)   # ms:§4: 2011-2016
    Z = (years[None, :] >= adopt[state][:, None]).astype(float)
    eps = np.empty((N, T))
    eps[:, 0] = rng.normal(0, 0.06, N)
    for t in range(1, T):                                 # ASSUMPTION: serially correlated outsourcing shocks
        eps[:, t] = 0.5 * eps[:, t - 1] + np.sqrt(0.75) * rng.normal(0, 0.06, N)
    yr = (years - 2009)[None, :]
    base_m = rng.normal(0, 0.15, (N, 1)) + 0.03 * yr + 0.2 * Z + rng.normal(0, 0.10, (N, T))
    a = rng.normal(0, 0.10, (N, 1))
    # Simultaneous system: Phi = a + .02*yr + beta*m + eps (ms:§3.3 eq.);  m = base_m + pi*Phi (feedback, inferred from ms:§1)
    phi = (a + 0.02 * yr + beta * base_m + eps) / (1 - beta * pi)
    m = base_m + pi * phi
    return phi, m, Z


def ols(y, x, groups):
    r = sm.OLS(y, x[:, None]).fit(cov_type="cluster", cov_kwds={"groups": groups})
    return r.params[0], r.pvalues[0], r.tvalues[0]


def iv(y, m, z, groups):
    b = (z @ y) / (z @ m)
    u = y - b * m
    scores = np.bincount(groups, weights=z * u)
    se = np.sqrt(np.sum(scores ** 2)) / abs(z @ m)
    return b, se


def run(beta, pi):
    out = np.empty((REPS, 7))
    gh_all = np.repeat(np.arange(N), T)
    gs_all = np.repeat(state, T)
    gh_lag = np.repeat(np.arange(N), T - 1)
    for i in range(REPS):
        phi, m, Z = simulate(beta, pi)
        y, x, z = demean2(phi).ravel(), demean2(m).ravel(), demean2(Z).ravel()
        b_ols, p_ols, _ = ols(y, x, gh_all)                                     # Model 2 analogue
        b_lag, p_lag, _ = ols(demean2(phi[:, 1:]).ravel(), demean2(m[:, :-1]).ravel(), gh_lag)   # m at t-1
        _, _, t_fs = ols(x, z, gs_all)                                          # first stage, clustered by state
        b_iv, se_iv = iv(y, x, z, gs_all)
        out[i] = (b_ols, p_ols, b_lag, p_lag, b_iv, se_iv, t_fs)
    return out


A = run(beta=0.0, pi=0.5)
B = run(beta=0.11, pi=0.0)
for name, R, beta in (("A: beta=0, feedback pi=0.5", A, 0.0), ("B: beta=0.11, no feedback", B, 0.11)):
    print(f"Scenario {name} (true beta = {beta})")
    print(f"  FE OLS on m_t:      mean b = {R[:, 0].mean():.4f}; share b>0 & p<.05 = {np.mean((R[:, 0] > 0) & (R[:, 1] < 0.05)):.2f}")
    print(f"  FE OLS on m_(t-1):  mean b = {R[:, 2].mean():.4f}; share b>0 & p<.05 = {np.mean((R[:, 2] > 0) & (R[:, 3] < 0.05)):.2f}")
    print(f"  FE 2SLS (state requirement as instrument): mean b = {R[:, 4].mean():.4f}; mean SE = {R[:, 5].mean():.4f}; "
          f"mean first-stage t = {R[:, 6].mean():.1f}")

spurious = np.mean((A[:, 0] > 0) & (A[:, 1] < 0.05))
lag_spurious = np.mean((A[:, 2] > 0) & (A[:, 3] < 0.05))
if spurious >= 0.8:
    print(f"VERDICT: DEMONSTRATED - with no effect of modularity and same-year feedback from outsourcing to reported "
          f"modularity, the within-hospital FE estimate is positive and significant in {spurious:.0%} of replications "
          f"(mean {A[:, 0].mean():.3f}); lagging m still gives {lag_spurious:.0%}; 2SLS on state requirements gives mean "
          f"{A[:, 4].mean():.3f} (a valid repair only if requirements satisfy exclusion, which ms does not argue).")
else:
    print(f"VERDICT: INCONCLUSIVE - feedback produced a significant positive FE estimate in only {spurious:.0%} of replications.")
