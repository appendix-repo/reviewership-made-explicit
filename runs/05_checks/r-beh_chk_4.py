import statsmodels.formula.api as smf

def aspiration_test(panel):
    """panel: Phi, m, u, peer_lag, spec, margin, margin_lag1, state_margin_lag1, controls, hospital, year, state.
    Aspiration form follows Greve 2003 (to verify); weights are illustrative."""
    p = panel.sort_values(["hospital", "year"]).copy()
    p["aspiration"] = 0.5*p.groupby("hospital")["margin"].shift(2) + 0.5*p["state_margin_lag1"]
    p = p.dropna(subset=["aspiration", "margin_lag1"])
    p["below"] = (p["margin_lag1"] < p["aspiration"]).astype(int)
    f = "Phi ~ m*below + u + m:u + peer_lag + spec + C(hospital) + C(year)"  # add ms:§3.2 controls by name
    return smf.ols(f, data=p).fit(cov_type="cluster", cov_kwds={"groups": p["state"]})
# Behavioral rival predicts coef on m:below > 0 and m alone near 0; TCE (cmt:24) predicts m:below about 0.
