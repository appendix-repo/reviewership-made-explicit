# p09:chk:9 -- state-level regressor, hospital clustering, and persistent state shocks (P-ID)
import numpy as np
import statsmodels.api as sm

rng = np.random.default_rng(2026102309)
S = 50                                   # ASSUMPTION: 50 states
n_s = np.full(S, 412 // S)
n_s[: 412 % S] += 1                      # 412 sample hospitals (ms:§3.1)
st = np.repeat(np.arange(S), n_s)
NS = st.size
BURN = list(range(2004, 2009))
OBS = list(range(2009, 2020))            # ms:§3.1


def demean2(X):
    return X - X.mean(axis=1, keepdims=True) - X.mean(axis=0, keepdims=True) + X.mean()


def simulate(rho_z, sig_z=0.03):
    a = rng.normal(0, 0.10, NS)
    z = rng.normal(0, sig_z, S)
    phi_prev = a + z[st] + rng.normal(0, 0.06, NS)
    PHI, PEER = [], []
    for yr in BURN + OBS:
        z = rho_z * z + np.sqrt(1 - rho_z ** 2) * rng.normal(0, sig_z, S)   # state-year shock (not absorbed by year FE)
        phi = a + 0.02 * (yr - 2009) + z[st] + rng.normal(0, 0.06, NS)      # NO imitation, NO modularity
        ssum = np.bincount(st, weights=phi_prev, minlength=S)
        peer = (ssum[st] - phi_prev) / (n_s[st] - 1)                         # ms:§3.2 Peer, t-1
        if yr in OBS:
            PHI.append(phi); PEER.append(peer)
        phi_prev = phi
    return np.column_stack(PHI)[:, 1:], np.column_stack(PEER)[:, 1:]       # drop 2009 (lag; see p09:fnd:1)


def run(rho_z, reps):
    out = np.empty((reps, 3))
    for i in range(reps):
        PHI, PEER = simulate(rho_z)
        T = PHI.shape[1]
        y, p = demean2(PHI).ravel(), demean2(PEER).ravel()
        rh = sm.OLS(y, p[:, None]).fit(cov_type="cluster", cov_kwds={"groups": np.repeat(np.arange(NS), T)})
        rs = sm.OLS(y, p[:, None]).fit(cov_type="cluster", cov_kwds={"groups": np.repeat(st, T)})
        out[i] = (rh.params[0], rh.pvalues[0], rs.pvalues[0])
    return out


Ra = run(rho_z=0.0, reps=300)
rej_h, rej_s = np.mean(Ra[:, 1] < 0.05), np.mean(Ra[:, 2] < 0.05)
print(f"(a) iid state-year shocks, true peer effect 0: mean b = {Ra[:, 0].mean():.4f}; "
      f"5% rejection rate: hospital-clustered {rej_h:.3f}, state-clustered {rej_s:.3f}")
Rb = run(rho_z=0.7, reps=100)
rej_b = np.mean((Rb[:, 0] > 0) & (Rb[:, 2] < 0.05))
print(f"(b) persistent state shocks (rho=0.7), true peer effect 0: mean b = {Rb[:, 0].mean():.4f}; "
      f"share b>0 & p<.05 (state-clustered) = {rej_b:.2f}; hospital-clustered = {np.mean((Rb[:, 0] > 0) & (Rb[:, 1] < 0.05)):.2f}")
print("reference: ms:T2.M1 peer = 0.137 (0.031)")

if rej_h >= 0.08 and rej_h - rej_s >= 0.03:
    print(f"VERDICT: DEMONSTRATED - p09:fnd:10: hospital-clustered SEs reject a true null for Peer at {rej_h:.1%} "
          f"(nominal 5%; state-clustered {rej_s:.1%}).")
else:
    print(f"VERDICT: INCONCLUSIVE - p09:fnd:10: hospital-clustered rejection {rej_h:.1%} vs state-clustered {rej_s:.1%}.")
if Rb[:, 0].mean() > 0 and rej_b >= 0.5:
    print(f"VERDICT: DEMONSTRATED - p09:fnd:11: with persistent state shocks and no imitation, lagged Peer predicts "
          f"own outsourcing (mean b = {Rb[:, 0].mean():.3f}; significant in {rej_b:.0%} with state clustering).")
else:
    print(f"VERDICT: INCONCLUSIVE - p09:fnd:11: persistent state shocks did not produce a reliable spurious peer coefficient.")
