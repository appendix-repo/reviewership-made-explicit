import pandas as pd

def decompose(panel: pd.DataFrame, beta1: float = 0.112) -> dict:
    """panel columns: hospital, year, Phi, m (ms:§3.2 definitions)."""
    g = panel.groupby("year")[["Phi", "m"]].mean()
    dPhi = g.loc[2019, "Phi"] - g.loc[2009, "Phi"]
    dm = g.loc[2019, "m"] - g.loc[2009, "m"]
    return {"dPhi": dPhi, "dm": dm, "beta1_dm": beta1*dm, "share_explained": beta1*dm/dPhi}
# Manuscript-only bound: beta1*dm <= 0.112, since m lies in [0,1).
