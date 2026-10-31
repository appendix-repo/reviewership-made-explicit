import numpy as np
import pandas as pd
from scipy import stats

cells = [
    ("M1", "Peer", 0.137, 0.031, "***"), ("M2", "Peer", 0.042, 0.038, ""),
    ("M3", "Peer", 0.039, 0.037, ""),    ("M4", "Peer", 0.036, 0.036, ""),
    ("M2", "Modularity", 0.112, 0.024, "***"), ("M3", "Modularity", 0.118, 0.025, "***"),
    ("M4", "Modularity", 0.097, 0.023, "***"),
    ("M3", "Uncertainty", 0.084, 0.051, "***"), ("M4", "Uncertainty", 0.079, 0.050, ""),
    ("M3", "Mod x Unc", -0.061, 0.019, "**"),   ("M4", "Mod x Unc", -0.058, 0.019, "**"),
    ("M1", "Specificity", -0.094, 0.027, "***"), ("M2", "Specificity", -0.091, 0.027, "***"),
    ("M3", "Specificity", -0.090, 0.026, "***"), ("M4", "Specificity", -0.088, 0.026, "***"),
    ("M4", "Staffing", -0.143, 0.029, "***"),
]
df_t = 412 - 1  # clusters - 1

def stars(p):
    return "***" if p < 0.001 else "**" if p < 0.01 else "*" if p < 0.05 else ""

rows = []
for mdl, var, b, se, rep in cells:
    # rounding interval: reported to 3 decimals
    t_lo = (abs(b) - 0.0005) / (se + 0.0005)
    t_hi = (abs(b) + 0.0005) / (se - 0.0005)
    t = abs(b) / se
    p_z  = 2*stats.norm.sf(t)
    p_t  = 2*stats.t.sf(t, df_t)
    p_lo = 2*stats.t.sf(t_hi, df_t)   # most significant admissible
    p_hi = 2*stats.t.sf(t_lo, df_t)   # least significant admissible
    rows.append(dict(model=mdl, var=var, b=b, se=se, t=round(t, 3), p_t=p_t, p_z=p_z,
                     reported=rep, implied=stars(p_t),
                     implied_range=(stars(p_hi), stars(p_lo)),
                     consistent=(rep in {stars(p_hi), stars(p_lo), stars(p_t)})))
out = pd.DataFrame(rows)
pd.set_option("display.width", 200)
print(out.to_string(index=False))
print("\nInconsistent cells:\n", out.loc[~out.consistent, ["model", "var", "b", "se", "t", "p_t", "reported", "implied"]])
