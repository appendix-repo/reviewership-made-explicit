# p09:chk:6 -- does the Model 1 -> Model 2 peer pattern discriminate economizing from mimicry? (P-ID)
import numpy as np
import statsmodels.api as sm

rng = np.random.default_rng(2026102306)
S = 50                                   # ASSUMPTION: 50 states (the number is not reported)
NPOP = 40                                # ASSUMPTION: hospitals per state in the field (sample + non-sample)
n_s = np.full(S, 412 // S)
n_s[: 412 % S] += 1                      # 412 sample hospitals (ms:§3.1): 12 states with 9, 38 with 8
BURN = list(range(2004, 2009))           # unobserved burn-in years
OBS = list(range(2009, 2020))            # ms:§3.1 observation window
REPS = 100

state = np.repeat(np.arange(S), NPOP)
in_sample = np.concatenate([np.arange(NPOP) < n_s[s] for s in range(S)])
NP = S * NPOP
samp = np.where(in_sample)[0]
samp_state = state[samp]
NS = samp.size
assert NS == 412


def field_mean(x):
    """True field prevalence: mean over all hospitals in the state (sample and non-sample)."""
    return np.bincount(state, weights=x, minlength=S) / NPOP


def demean2(X):
    return X - X.mean(axis=1, keepdims=True) - X.mean(axis=0, keepdims=True) + X.mean()


def simulate(beta, lam, kappa, theta, sig_zeta=0.01):
    adopt = np.full(S, 9999)
    adopters = rng.permutation(S)[:40]                    # ASSUMPTION: 40 of 50 states adopt a requirement
    adopt[adopters] = rng.integers(2011, 2017, size=40)   # ms:§4: requirements adopted 2011-2016
    a = rng.normal(0, 0.10, NP)                           # hospital effects in Phi
    am = rng.normal(0, 0.15, NP)                          # hospital effects in m
    w = np.zeros(S)
    e = rng.normal(0, 0.12, NP)
    phi_prev = a.copy()
    F_prev = field_mean(phi_prev)
    PHI, M, PEER = [], [], []
    for yr in BURN + OBS:
        w = w + rng.normal(0, 0.10, S)
        R = (yr >= adopt).astype(float) + w               # state standards diffusion (ms:§4 'common diffusion of standards')
        e = 0.5 * e + np.sqrt(0.75) * rng.normal(0, 0.12, NP)
        # kappa > 0: field prevalence of outsourcing prompts own adoption of certified interfaces (mimicry via m)
        m = am + 0.03 * (yr - 2009) + lam * R[state] + kappa * F_prev[state] + e
        zeta = rng.normal(0, sig_zeta, S)                 # state-year outsourcing shock (serially independent here)
        # beta: H1 (ms:§3.3 eq.); theta > 0: direct imitation of the field (H3, ms:§2.4)
        phi = (a + 0.02 * (yr - 2009) + beta * m + theta * F_prev[state] + zeta[state]
               + rng.normal(0, 0.06, NP))
        # observed Peer: mean of the OTHER SAMPLE hospitals in the same state in t-1 (ms:§3.2)
        ps = phi_prev[samp]
        ssum = np.bincount(samp_state, weights=ps, minlength=S)
        peer = (ssum[samp_state] - ps) / (n_s[samp_state] - 1)
        if yr in OBS:
            PHI.append(phi[samp]); M.append(m[samp]); PEER.append(peer)
        F_prev = field_mean(phi)
        phi_prev = phi
    # 2009 is dropped: Peer(t-1) would need 2008 data outside the window (see p09:fnd:1)
    PHI, M, PEER = (np.column_stack(z)[:, 1:] for z in (PHI, M, PEER))
    return PHI, M, PEER


def run(beta, lam, kappa, theta):
    out = np.empty((REPS, 7))
    for i in range(REPS):
        PHI, M, PEER = simulate(beta, lam, kappa, theta)
        g = np.repeat(np.arange(NS), PHI.shape[1])
        y, m, p = (demean2(Z).ravel() for Z in (PHI, M, PEER))
        r1 = sm.OLS(y, p[:, None]).fit(cov_type="cluster", cov_kwds={"groups": g})                 # Model 1 analogue
        r2 = sm.OLS(y, np.column_stack([p, m])).fit(cov_type="cluster", cov_kwds={"groups": g})   # Model 2 analogue
        b1, p1 = r1.params[0], r1.pvalues[0]
        b2, p2 = r2.params[0], r2.pvalues[0]
        bm, pm = r2.params[1], r2.pvalues[1]
        pattern = (b1 > 0) and (p1 < 0.05) and (p2 >= 0.05) and (b2 <= b1 / 3) and (bm > 0) and (pm < 0.05)
        out[i] = (b1, p1, b2, p2, bm, pm, float(pattern))
    return out


scenarios = [
    ("i", "economizing only (no mimicry)", dict(beta=0.11, lam=0.25, kappa=0.0, theta=0.0), "none"),
    ("ii", "mimicry through modularity, kappa=1", dict(beta=0.11, lam=0.25, kappa=1.0, theta=0.0), "indirect 0.11"),
    ("ii", "mimicry through modularity, kappa=2", dict(beta=0.11, lam=0.25, kappa=2.0, theta=0.0), "indirect 0.22"),
    ("iii", "direct mimicry, theta=0.10", dict(beta=0.11, lam=0.25, kappa=0.0, theta=0.10), "direct 0.10"),
    ("iii", "direct mimicry, theta=0.20", dict(beta=0.11, lam=0.25, kappa=0.0, theta=0.20), "direct 0.20"),
    ("iii", "direct mimicry, theta=0.30", dict(beta=0.11, lam=0.25, kappa=0.0, theta=0.30), "direct 0.30"),
]
rates = {"i": [], "ii": [], "iii": []}
print("Table 2 for reference: M1 peer 0.137 (0.031)***; M2 peer 0.042 (0.038); M2 modularity 0.112 (0.024)***")
for fam, label, par, true_mim in scenarios:
    R = run(**par)
    rate = R[:, 6].mean()
    rates[fam].append((label, rate))
    print(f"[{fam}] {label} (true mimetic effect of field prevalence: {true_mim})")
    print(f"    M1 peer mean {R[:, 0].mean():.3f}, share p<.05 {np.mean(R[:, 1] < 0.05):.2f} | "
          f"M2 peer mean {R[:, 2].mean():.3f}, share p<.05 {np.mean(R[:, 3] < 0.05):.2f} | "
          f"M2 modularity mean {R[:, 4].mean():.3f}, share p<.05 {np.mean(R[:, 5] < 0.05):.2f} | "
          f"pattern reproduced in {rate:.2f} of replications")

rate_i = rates["i"][0][1]
best_ii = max(rates["ii"], key=lambda x: x[1])
best_iii = max(rates["iii"], key=lambda x: x[1])
if rate_i < 0.5:
    print(f"VERDICT: INCONCLUSIVE - the economizing-only DGP reproduces the Table 2 pattern in only {rate_i:.2f} of "
          f"replications with these parameters, so the comparison is not informative (p09:fnd:6, p09:fnd:7).")
else:
    overall = best_ii[1] >= 0.5 or best_iii[1] >= 0.5
    print(("VERDICT: DEMONSTRATED - " if overall else "VERDICT: INCONCLUSIVE - ")
          + f"economizing-only reproduces the pattern in {rate_i:.2f} of replications; best mimicry DGPs: "
          f"'{best_ii[0]}' {best_ii[1]:.2f}, '{best_iii[0]}' {best_iii[1]:.2f}. "
          + ("The Model 1 -> Model 2 pattern does not discriminate economizing from mimicry." if overall else ""))
    print(("VERDICT: DEMONSTRATED - p09:fnd:6: " if best_ii[1] >= 0.5 else "VERDICT: INCONCLUSIVE - p09:fnd:6: ")
          + f"mimicry operating through modularity reproduces the pattern in {best_ii[1]:.2f} of replications ({best_ii[0]}).")
    print(("VERDICT: DEMONSTRATED - p09:fnd:7: " if best_iii[1] >= 0.5 else "VERDICT: INCONCLUSIVE - p09:fnd:7: ")
          + f"direct mimicry seen through the sample-based Peer reproduces the pattern in {best_iii[1]:.2f} of "
          f"replications ({best_iii[0]}).")
