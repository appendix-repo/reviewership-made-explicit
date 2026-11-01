"""Sample-size and minimum-detectable-effect calculations for the two-track critical test (appendix §8).
All inputs marked ASSUMPTION are to be replaced by pilot estimates before pre-registration."""
from scipy.stats import norm
import math
za = lambda a: norm.ppf(1 - a)
# Paired non-inferiority on blind ratings (7-point scale), AI-assisted minus human, same manuscript.
sd_diff = 1.2      # ASSUMPTION: SD of the within-manuscript difference in mean blind rating
margin = 0.3       # ASSUMPTION: non-inferiority margin, about 0.25 SD of the difference
alpha = 0.025      # one-sided
for power in (0.80, 0.90):
    n = ((za(alpha) + za(1 - power)) * sd_diff / margin) ** 2
    print(f"Non-inferiority, power {power:.2f}: n = {math.ceil(n)} paired manuscripts")
# Superiority on a pre-specified sub-task score (share of reference unentitled commitments located).
sd_sub = 0.25      # ASSUMPTION: SD of the within-manuscript difference in recall (0-1 scale)
for d in (0.08, 0.10):
    n = ((za(0.025) + za(0.20)) * sd_sub / d) ** 2
    print(f"Superiority on sub-task recall, difference {d:.2f}, power 0.80, two-sided alpha 0.05: n = {math.ceil(n)}")
# Holm correction across 3 pre-registered sub-task hypotheses: smallest alpha 0.05/3.
n = ((za(0.05 / 3 / 2) + za(0.20)) * sd_sub / 0.10) ** 2
print(f"  with Holm's smallest threshold (0.05/3, two-sided): n = {math.ceil(n)}")
# Fallback (internal) study: minimum detectable difference with n paired manuscripts.
for n in (30, 40):
    mdd = (za(0.025) + za(0.20)) * sd_diff / math.sqrt(n)
    print(f"Fallback n = {n}: minimum detectable mean rating difference = {mdd:.2f} points ({mdd/sd_diff:.2f} SD)")
# Human-likeness: can blind raters tell AI-assisted from human reviews? Test AUC > 0.5 (Hanley-McNeil variance).
def auc_se(A, n1, n2):
    q1, q2 = A / (2 - A), 2 * A * A / (1 + A)
    return math.sqrt((A * (1 - A) + (n1 - 1) * (q1 - A * A) + (n2 - 1) * (q2 - A * A)) / (n1 * n2))
for n in (126, 150):
    print(f"Human-likeness with {n}+{n} reviews: SE(AUC) at 0.60 = {auc_se(0.60, n, n):.3f}; detects AUC 0.60 vs 0.50: z = {(0.10)/auc_se(0.60, n, n):.2f}")
# Revealed trust: precision of the AI-track share.
for n in (200, 400):
    print(f"Track choice with {n} submissions: 95% CI half-width at share 0.5 = {1.96*math.sqrt(0.25/n):.3f}")
