# p09:chk:1 -- observation count against the stated panel design (P-NUM)
# ms:§3.1: "a balanced panel of 412 U.S. general acute-care hospitals observed annually from 2009 to 2019"
# ms:§3.1: "yielding 4,712 hospital-year observations"; ms:T2: Observations 4,712 in Models 1-4
# ms:§3.2: Peer outsourcing is measured "in year t-1"; it enters all four models (ms:T2)
hospitals = 412
first_year, last_year = 2009, 2019
years = last_year - first_year + 1
reported_n = 4712
balanced_n = hospitals * years
lagged_n = hospitals * (years - 1)   # Peer(t-1) cannot be formed for 2009 from in-window data
print(f"years in window (inclusive): {years}")
print(f"balanced panel N = {hospitals} x {years} = {balanced_n}")
print(f"N with Peer(t-1) from in-window data = {hospitals} x {years - 1} = {lagged_n}")
print(f"reported N = {reported_n}; reported N / {hospitals} = {reported_n / hospitals:.3f} years per hospital")
print(f"reported - balanced = {reported_n - balanced_n}")
if reported_n in (balanced_n, lagged_n):
    print("VERDICT: REFUTED-BY-CHECK - the reported N matches the stated design.")
elif reported_n % hospitals != 0:
    print(f"VERDICT: DEMONSTRATED - 4,712 is not a multiple of 412, so it cannot be a balanced 412-hospital panel; "
          f"expected {balanced_n} (all years) or at most {lagged_n} for models with Peer(t-1).")
else:
    print("VERDICT: INCONCLUSIVE - N is a multiple of 412 but matches neither expected count.")
