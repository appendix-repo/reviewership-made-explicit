# p09:chk:8 -- TWFE event study under staggered adoption with heterogeneous dynamic effects (P-ID)
import numpy as np
import statsmodels.api as sm

rng = np.random.default_rng(2026102308)
N, S, REPS = 412, 50, 100                 # ms:§3.1: 412 hospitals. ASSUMPTION: 50 states
years = np.arange(2009, 2020)             # ms:§3.1
T = years.size
state = np.arange(N) % S
NEVER = 9999
groups = np.repeat(state, T)              # cluster by state (the level of treatment)


def demean2(X):
    return X - X.mean(axis=1, keepdims=True) - X.mean(axis=0, keepdims=True) + X.mean()


def draw_adoption():
    adopt = np.full(S, NEVER)
    adopters = rng.permutation(S)[:40]                 # ASSUMPTION: 40 adopting states, 10 never-treated
    adopt[adopters] = 2011 + (np.arange(40) % 6)       # ms:§4: cohorts 2011-2016, each non-empty
    return adopt[state]


def true_effect(adopt_h):
    rel = years[None, :] - adopt_h[:, None]
    treated = (adopt_h < NEVER)[:, None] & (rel >= 0)
    slope = 0.003 * (2017 - adopt_h)[:, None]          # ASSUMPTION: earlier cohorts gain more per year
    return np.where(treated, slope * (rel + 1), 0.0), rel


def dummies(rel, never, spec):
    ever = ~never[:, None]
    cols, labels = [], []
    if spec == "saturated":                            # every relative period except -1
        for k in range(-7, 9):
            if k != -1:
                cols.append(((rel == k) & ever).astype(float)); labels.append(str(k))
    else:                                              # binned endpoints: <=-5, -4..-2, 0..4, >=5
        cols.append(((rel <= -5) & ever).astype(float)); labels.append("<=-5")
        for k in (-4, -3, -2, 0, 1, 2, 3, 4):
            cols.append(((rel == k) & ever).astype(float)); labels.append(str(k))
        cols.append(((rel >= 5) & ever).astype(float)); labels.append(">=5")
    return cols, labels


def truth(eff, rel, never, labels):
    ever = ~never[:, None]
    out = []
    for lab in labels:
        if lab == "<=-5":
            mask = (rel <= -5) & ever
        elif lab == ">=5":
            mask = (rel >= 5) & ever
        else:
            mask = (rel == int(lab)) & ever
        out.append(eff[mask].mean() if mask.any() else np.nan)
    return np.array(out)


flags = []
for spec in ("saturated", "binned"):
    est, pv, tru = [], [], []
    for _ in range(REPS):
        adopt_h = draw_adoption()
        never = adopt_h == NEVER
        eff, rel = true_effect(adopt_h)
        y = rng.normal(0, 0.10, (N, 1)) + 0.02 * (years - 2009)[None, :] + eff + rng.normal(0, 0.06, (N, T))
        cols, labels = dummies(rel, never, spec)
        X = np.column_stack([demean2(c).ravel() for c in cols])
        r = sm.OLS(demean2(y).ravel(), X).fit(cov_type="cluster", cov_kwds={"groups": groups})
        est.append(r.params); pv.append(r.pvalues); tru.append(truth(eff, rel, never, labels))
    est, pv, tru = np.array(est), np.array(pv), np.array(tru)
    mean, mcse, t_mean = est.mean(0), est.std(0, ddof=1) / np.sqrt(REPS), np.nanmean(tru, 0)
    print(f"Specification: {spec}")
    print(f"  {'rel':>5s} {'TWFE mean':>10s} {'MC SE':>7s} {'truth':>7s} {'bias':>8s} {'rej5%':>6s}")
    for j, lab in enumerate(labels):
        bias = mean[j] - t_mean[j]
        rej = np.mean(pv[:, j] < 0.05)
        is_lead = lab.startswith("-") or lab.startswith("<=")
        if is_lead:
            bad = abs(mean[j]) > max(3 * mcse[j], 0.005) or rej > 0.10
        else:
            bad = abs(bias) > max(3 * mcse[j], 0.10 * abs(t_mean[j]))
        if bad:
            flags.append(f"{spec} rel {lab}: mean {mean[j]:.4f} vs truth {t_mean[j]:.4f}")
        print(f"  {lab:>5s} {mean[j]:10.4f} {mcse[j]:7.4f} {t_mean[j]:7.4f} {bias:8.4f} {rej:6.2f}{'  <--' if bad else ''}")

if flags:
    print("VERDICT: DEMONSTRATED - part (a) of p09:fnd:9: with zero pre-trends and cohort-heterogeneous dynamic effects, "
          "TWFE event-study coefficients do not recover the true effects (or show non-zero leads): " + "; ".join(flags))
else:
    print("VERDICT: REFUTED-BY-CHECK - part (a) of p09:fnd:9: under these DGPs, TWFE leads are null and lags recover the "
          "true weighted effects in both specifications; parts (b)-(c) (estimand, exclusion, reporting) remain argued.")
