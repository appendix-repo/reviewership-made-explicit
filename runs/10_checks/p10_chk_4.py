# p10:chk:4 — does the §2.4 discriminating prediction discriminate? (ms:TEST §2.4 last ¶; §4 H3; §3.2 Peer; Table 2 M1-M2)
# Not run by the probe.
import numpy as np
import pandas as pd
import statsmodels.api as sm

rng = np.random.default_rng(4)
S, n, T = 50, 8, 12   # ~8 sample hospitals per state (412/50, inferred from §3.1); 12 waves so Peer(t-1) exists for 11 years

def fe_ols(df, y, xs):
    d = df[[y] + xs + ['i', 't']].copy()
    for v in [y] + xs:                            # hospital + year FE (§3.3), balanced panel
        d[v] = d[v] - d.groupby('i')[v].transform('mean') - d.groupby('t')[v].transform('mean') + d[v].mean()
    r = sm.OLS(d[y], d[xs]).fit(cov_type='cluster', cov_kwds={'groups': d['i'].values})   # clustered by hospital (§3.3)
    return r.params, r.tvalues

def simulate(kind, beta=0.11, kappa=0.8):
    N = S*n; st = np.repeat(np.arange(S), n)
    a = rng.normal(0.31, 0.1, N)
    m = np.clip(rng.normal(0.2, 0.05, N), 0, 1)
    L = rng.integers(2, 9, S)                     # staggered state timing (cf. §4 Robustness, requirements 2011-2016)
    is_leader = (np.arange(N) % n) < 2            # DGP I: two early adopters per state
    recs, phi_prev = [], None
    for t in range(T):
        if t > 0:
            if kind == 'T':
                # §4 H3 reading: standards diffuse by state; no imitation anywhere
                m = m + 0.02 + 0.15*(t == L[st]) + rng.normal(0, 0.02, N)
            else:
                # §1 institutional mechanism (imitate peers under uncertainty) applied to adopting standard interfaces
                peer_m = (np.bincount(st, weights=m, minlength=S)[st] - m)/(n - 1)
                jump = 0.5*(t == L[st])*is_leader
                m = m + 0.02 + kappa*np.clip(peer_m - m, 0, None) + jump + rng.normal(0, 0.02, N)
            m = np.clip(m, 0, 1)
        phi = a + beta*m + rng.normal(0, 0.02, N)  # §2.2-2.4: Phi responds to m; NO direct peer term in either DGP
        if phi_prev is not None:
            peer = (np.bincount(st, weights=phi_prev, minlength=S)[st] - phi_prev)/(n - 1)   # §3.2: other same-state hospitals, t-1
            recs.append(pd.DataFrame(dict(i=np.arange(N), t=t, phi=phi, m=m, peer=peer)))
        phi_prev = phi
    return pd.concat(recs, ignore_index=True)

summary = {}
for kind in ('T', 'I'):
    res = []
    for _ in range(20):
        df = simulate(kind)
        b1, t1 = fe_ols(df, 'phi', ['peer'])          # Table 2 M1 analogue
        b2, t2 = fe_ols(df, 'phi', ['peer', 'm'])     # Table 2 M2 analogue
        res.append((b1['peer'], t1['peer'], b2['peer'], t2['peer'], b2['m']))
    res = np.array(res)
    sig1, sig2 = np.mean(np.abs(res[:, 1]) > 1.96), np.mean(np.abs(res[:, 3]) > 1.96)
    summary[kind] = (sig1, sig2)
    label = 'standards diffuse by state, no imitation' if kind == 'T' else 'standards diffuse by imitation'
    print(f"DGP {kind} ({label}): M1 peer mean {res[:, 0].mean():.3f}, significant in {sig1:.0%}; "
          f"M2 peer mean {res[:, 2].mean():.3f}, significant in {sig2:.0%}; M2 b_m mean {res[:, 4].mean():.3f}")
pattern = {k: (v[0] > 0.5 and v[1] <= 0.2) for k, v in summary.items()}
if pattern['T'] and pattern['I']:
    print("VERDICT: the M1-M2 pattern (peer significant without m, not with m) arises BOTH without imitation and under "
          "imitative diffusion of standards; the §2.4 prediction does NOT discriminate economizing from mimicry routed through modularity.")
elif pattern['T']:
    print("VERDICT: pattern arises without imitation but NOT under imitative diffusion in this DGP; demonstration for p10:fnd:2 FAILS here "
          "(the finding then rests on argument alone).")
else:
    print(f"VERDICT: INCONCLUSIVE — the simulated DGPs did not reproduce the manuscript's M1-M2 pattern ({pattern}); adjust the DGP before concluding.")
