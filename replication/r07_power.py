"""R07. Sample size for the critical test (appendix Sections 8.4 and 8.6), from tools/power_critical_test.py."""
import re

from lib import check, run_tool

G = "Critical-test power"


def run():
    s = run_tool(["tools/power_critical_test.py"])
    g = lambda pat: re.search(pat, s).groups()
    out = [
        check(G, "H2 non-inferiority, power 0.80: paired manuscripts", "8.4", "126", g(r"power 0\.80: n = (\d+)")[0]),
        check(G, "H2 non-inferiority, power 0.90: paired manuscripts", "8.4", "169", g(r"power 0\.90: n = (\d+)")[0]),
        check(G, "H3 sub-task superiority with Holm's smallest threshold", "8.4", "66", g(r"Holm's smallest threshold.*n = (\d+)")[0]),
        check(G, "H4: SE(AUC) at 0.60 with 150 reviews per source, and z", "8.4", ("0.033", "3.07"),
              g(r"150\+150 reviews: SE\(AUC\) at 0\.60 = ([\d.]+); detects AUC 0\.60 vs 0\.50: z = ([\d.]+)")),
        check(G, "Fallback, 30 pairs: minimum detectable difference (points, SD)", "8.6", ("0.61", "0.51"),
              g(r"Fallback n = 30: .* = ([\d.]+) points \(([\d.]+) SD\)")),
        check(G, "Fallback, 40 pairs: minimum detectable difference (points, SD)", "8.6", ("0.53", "0.44"),
              g(r"Fallback n = 40: .* = ([\d.]+) points \(([\d.]+) SD\)")),
    ]
    return out


if __name__ == "__main__":
    for r in run():
        print(r.status, "|", r.claim, "|", r.expected, "|", r.observed, "|", r.detail)
