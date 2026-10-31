# p10:chk:3 — does surviving the in-house-staffing control exclude capability confounding? (ms:TEST §3.3 ¶2; §3.2; Table 2 M4)
# Not run by the probe. Signs and sizes of the capability paths are not given in ms:TEST; several are tried.
import numpy as np
import pandas as pd
import statsmodels.api as sm

rng = np.random.default_rng(3)
N, T = 412, 11                                   # §3.1: 412 hospitals, 2009-2019

def fe_ols(df, y, xs):
    d = df[[y] + xs + ['i', 't']].copy()
    for v in [y] + xs:                           # two-way within transformation, balanced panel (hospital + year FE, §3.3)
        d[v] = d[v] - d.groupby('i')[v].transform('mean') - d.groupby('t')[v].transform('mean') + d[v].mean()
    r = sm.OLS(d[y], d[xs]).fit(cov_type='cluster', cov_kwds={'groups': d['i'].values})   # clustered by hospital (§3.3)
    return r.params, r.tvalues

def one_draw(c_m, c_phi, c_s=1.0, d=0.5, beta_m=0.0):
    i = np.repeat(np.arange(N), T); t = np.tile(np.arange(T), N)
    C = np.cumsum(rng.normal(0, 0.1, (N, T)), axis=1).ravel()   # §3.3: unobserved, time-varying internal IT capability
    m = 0.46 + c_m*C + np.repeat(rng.normal(0, 0.1, N), T) + rng.normal(0, 0.05, N*T)    # capability -> modularity (§3.3)
    phi = (0.31 + beta_m*m + c_phi*C + np.repeat(rng.normal(0, 0.1, N), T)
           + 0.01*t + rng.normal(0, 0.05, N*T))                  # capability -> outsourcing (§3.3); true beta_m = 0
    S = c_s*C - d*phi + rng.normal(0, 0.05, N*T)                 # §3.2: staffing tracks capability; outsourcing removes positions
    df = pd.DataFrame(dict(i=i, t=t, phi=phi, m=m, S=S))
    b2, t2 = fe_ols(df, 'phi', ['m'])                            # Model-2-like (controls omitted)
    b4, t4 = fe_ols(df, 'phi', ['m', 'S'])                       # Model-4-like (adds staffing)
    return b2['m'], t2['m'], b4['m'], t4['m']

refuted = []
for c_m, c_phi in [(0.5, 0.5), (0.5, -0.5), (1.0, 0.3)]:
    out = np.array([one_draw(c_m, c_phi) for _ in range(40)])
    rej2, rej4 = np.mean(np.abs(out[:, 1]) > 1.96), np.mean(np.abs(out[:, 3]) > 1.96)
    print(f"C->m {c_m:+}, C->Phi {c_phi:+}: Model-2-like mean b_m = {out[:, 0].mean():.3f} (reject 0 in {rej2:.0%}); "
          f"Model-4-like mean b_m = {out[:, 2].mean():.3f} (reject 0 in {rej4:.0%}); true b_m = 0")
    if rej4 > 0.5:
        refuted.append((c_m, c_phi))
print("VERDICT:", ("§3.3 ¶2 claim REFUTED for DGP(s) " + str(refuted) + ": with true beta_m = 0 and capability confounding, "
      "beta_m 'survives' the staffing control, so survival cannot exclude capability differences") if refuted else
      "in these DGPs the staffing control removed the capability bias; p10:fnd:6 NOT DEMONSTRATED by simulation "
      "(the claim is still not entailed; see p10:inc:3)")
