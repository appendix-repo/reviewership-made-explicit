# p09:chk:5 -- is 'survives the in-house staffing control' informative about capability confounding? (P-ID)
# Model 3/Model 4 analogues: Phi on m (FE), and Phi on m + staffing (FE). Other ms:T2 regressors (u, m x u, Peer,
# controls) are omitted; by construction they are independent of the variables simulated here.
import numpy as np
import statsmodels.api as sm

rng = np.random.default_rng(2026102305)
N, T = 412, 11            # ms:§3.1: 412 hospitals, 2009-2019, balanced
REPS = 200
groups = np.repeat(np.arange(N), T)


def demean2(X):
    """Two-way (hospital, year) within transformation; exact for a balanced panel."""
    return X - X.mean(axis=1, keepdims=True) - X.mean(axis=0, keepdims=True) + X.mean()


def simulate(beta, c, d, a=1.5, b=0.2, rho=0.7):
    # C: unobserved, time-varying internal IT capability, the confounder named in ms:§3.3. ASSUMPTION: AR(1), rho=0.7
    C = np.empty((N, T))
    C[:, 0] = rng.normal(size=N)
    for t in range(1, T):
        C[:, t] = rho * C[:, t - 1] + np.sqrt(1 - rho ** 2) * rng.normal(size=N)
    yr = np.arange(T)[None, :]
    # C -> m (ms:§3.3). ASSUMPTION: capability raises modularity (d >= 0)
    m = rng.normal(0, 0.15, (N, 1)) + 0.03 * yr + d * C + rng.normal(0, 0.10, (N, T))
    # m -> Phi (ms:§3.3 equation) and C -> Phi (ms:§3.3). ASSUMPTION: capability raises outsourcing (c >= 0)
    phi = rng.normal(0, 0.10, (N, 1)) + 0.02 * yr + beta * m + c * C + rng.normal(0, 0.06, (N, T))
    # Phi -> staffing: ms:§3.2 "outsourcing a function transfers its staff to the vendor or eliminates the positions"
    # C -> staffing:   ms:§3.2 staffing "also tracks the scale of the hospital's internal IT capability"
    staff = rng.normal(0, 0.30, (N, 1)) - 0.01 * yr - a * phi + b * C + rng.normal(0, 0.10, (N, T))
    return demean2(phi).ravel(), demean2(m).ravel(), demean2(staff).ravel()


def fit(y, cols):
    r = sm.OLS(y, np.column_stack(cols)).fit(cov_type="cluster", cov_kwds={"groups": groups})
    return r.params[0], r.pvalues[0]


def run(beta, c, d):
    out = np.empty((REPS, 4))
    for i in range(REPS):
        y, m, s = simulate(beta, c, d)
        b3, p3 = fit(y, [m])        # Model 3 analogue
        b4, p4 = fit(y, [m, s])     # Model 4 analogue (adds in-house staffing)
        out[i] = (b3, p3, b4, p4)
    return out


A = run(beta=0.0, c=0.03, d=0.06)
B = run(beta=0.11, c=0.0, d=0.0)

for name, R, beta in (("A: beta=0, capability confounding", A, 0.0), ("B: beta=0.11, no confounding", B, 0.11)):
    print(f"Scenario {name}")
    print(f"  Model 3 analogue: mean b = {R[:, 0].mean():.4f} (MC SE {R[:, 0].std(ddof=1) / np.sqrt(REPS):.4f}); "
          f"share b>0 & p<.05 = {np.mean((R[:, 0] > 0) & (R[:, 1] < 0.05)):.2f}")
    print(f"  Model 4 analogue: mean b = {R[:, 2].mean():.4f} (MC SE {R[:, 2].std(ddof=1) / np.sqrt(REPS):.4f}); "
          f"share b>0 & p<.05 = {np.mean((R[:, 2] > 0) & (R[:, 3] < 0.05)):.2f}; true beta = {beta}")

survive_A = np.mean((A[:, 2] > 0) & (A[:, 3] < 0.05))
bias_B = B[:, 2].mean() - 0.11
mcse_B = B[:, 2].std(ddof=1) / np.sqrt(REPS)
biased_B = abs(bias_B) / 0.11 >= 0.05 and abs(bias_B) > 3 * mcse_B
print(f"A: share of replications in which the modularity effect 'survives' Model 4 with zero true effect = {survive_A:.2f}")
print(f"B: Model 4 bias = {bias_B:+.4f} ({bias_B / 0.11:+.1%} of true beta), MC SE {mcse_B:.4f}")

if survive_A >= 0.8:
    print(f"VERDICT: DEMONSTRATED - under the manuscript's own relations, a modularity coefficient with no causal content "
          f"survives the staffing control (positive, p<.05) in {survive_A:.0%} of replications; survival cannot rule out "
          f"capability confounding." + (f" The control also biases a true effect by {bias_B / 0.11:+.0%}." if biased_B else ""))
elif biased_B:
    print(f"VERDICT: DEMONSTRATED - the staffing control biases the modularity coefficient by {bias_B / 0.11:+.0%} even "
          f"without confounding; Model 4 is not a valid robustness test.")
else:
    print("VERDICT: INCONCLUSIVE - with these parameters the staffing control neither preserves a spurious effect nor "
          "biases a true one; the finding stands as argued only.")
