import numpy as np

rng = np.random.default_rng(7)
years = np.arange(2009, 2020)
S, per = 40, 10
cohorts = np.array([2011]*5 + [2012]*5 + [2013]*5 + [2014]*5 + [2015]*6 + [2016]*6 + [0]*8)  # 0 = never
assert cohorts.size == S
g = np.repeat(cohorts, per)
N, T = g.size, years.size

def twoway_demean(x):
    return x - x.mean(1, keepdims=True) - x.mean(0, keepdims=True) + x.mean()

R, est, att = 200, [], []
for _ in range(R):
    t = np.broadcast_to(years, (N, T))
    D = ((g[:, None] > 0) & (t >= g[:, None])).astype(float)
    slope = np.where(g > 0, 0.01*(2017 - g), 0.0)[:, None]     # earlier cohorts gain faster
    tau = D * slope * (t - g[:, None] + 1)
    y = rng.normal(0, 0.1, (N, 1)) + 0.01*(t - 2009) + tau + rng.normal(0, 0.05, (N, T))
    yd, Dd = twoway_demean(y).ravel(), twoway_demean(D).ravel()
    est.append((Dd @ yd) / (Dd @ Dd))
    att.append(tau[D == 1].mean())
print("true ATT over treated cells: %.4f" % np.mean(att))
print("static TWFE estimate       : %.4f (sd %.4f)" % (np.mean(est), np.std(est)))
print("TWFE / ATT                 : %.2f" % (np.mean(est)/np.mean(att)))
