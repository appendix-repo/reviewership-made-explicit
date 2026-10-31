import numpy as np
import statsmodels.api as sm

rng = np.random.default_rng(1)
N, T = 412, 11
ids = np.repeat(np.arange(N), T)

def within(x):   # two-way demeaning, balanced panel ordered by hospital then year
    X = x.reshape(N, T)
    return (X - X.mean(1, keepdims=True) - X.mean(0, keepdims=True) + X.mean()).ravel()

def fe(y, *xs):
    X = np.column_stack([within(x) for x in xs])
    return sm.OLS(within(y), X).fit(cov_type="cluster", cov_kwds={"groups": ids})

def simulate(beta, conf, reps=200):
    out = []
    for _ in range(reps):
        a = rng.normal(size=N).repeat(T)
        tau = np.tile(np.linspace(0, 1, T), N)
        c = a + rng.normal(size=N*T)                       # time-varying capability
        m = 0.5*c + rng.normal(size=N*T)                   # capability raises modularity
        phi = beta*m + conf*c + a + tau + rng.normal(size=N*T)
        staff = -0.8*phi + 0.5*c + rng.normal(size=N*T)    # outsourcing cuts in-house staff (ms §3.2)
        r_without, r_with = fe(phi, m), fe(phi, m, staff)
        out.append((r_without.params[0], r_without.pvalues[0], r_with.params[0], r_with.pvalues[0]))
    o = np.array(out)
    print(f"true beta={beta}, confounding={conf}: b without staffing={o[:,0].mean():.3f} (share p<.05: {np.mean(o[:,1] < .05):.2f}); "
          f"b with staffing={o[:,2].mean():.3f} (share p<.05: {np.mean(o[:,3] < .05):.2f})")

simulate(beta=0.0, conf=0.3)   # A: confounding by capability, no true effect
simulate(beta=0.1, conf=0.0)   # B: true effect, no confounding
