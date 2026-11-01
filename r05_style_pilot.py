"""R05. Stylistic profiles and the base-model pilot (appendix Sections 4.3, 4.8, 7.9).

1. tools/style_metrics.py on the six blind pilot reports reproduces runs/13_pilot/style_metrics.txt and the
   Words / Hedges / Nominalizations / Flesch columns of the pilot table, joined to tier and style through the
   unblinding map.
2. The shortening under the terse style (Section 7.9, item 3).
3. The blind scorer's codes in runs/13_pilot/scoring.md give the Located / Touched / Missed / New substantive /
   Mistaken columns of the pilot table.
4. The draft and the signed review: words, hedges per 1,000 words and Flesch reading ease (Sections 4.3 and 4.8).
"""
import json

from lib import APPENDIX, check, md_table, note, read, run_tool, signed_review
from style_metrics import profile

G = "Style and pilot"


def run():
    out = []
    got = run_tool(["tools/style_metrics.py"] + [f"runs/13_pilot/blind/review_{x}.md" for x in "ABCDEF"])
    out.append(check(G, "style_metrics.py output equals runs/13_pilot/style_metrics.txt", "7.9", read("runs/13_pilot/style_metrics.txt"), got))

    umap = json.loads(read("runs/13_pilot/UNBLINDING_MAP.json"))
    tiers = {"haiku": "Haiku", "sonnet": "Sonnet", "opus": "Opus"}
    styles = {"S1": "S1 reviewerly", "S2": "S2 terse"}
    app = open(APPENDIX, encoding="utf-8").read()
    head, rows = md_table(app, "| Tier | Style | Report |")
    _, sc = md_table(read("runs/13_pilot/scoring.md"), "| Report | SD1 |")
    sc = {r[0]: r for r in sc}
    prof = {}
    for r in rows:
        tier, style, rep = r[0], r[1], r[2]
        t, s = umap[rep].split("_")
        out.append(check(G, f"Report {rep} unblinds to {tier}, {style}", "7.9", (tier, style), (tiers[t], styles[s])))
        pr = profile(read(f"runs/13_pilot/blind/review_{rep}.md"))
        prof[(t, s)] = pr["words"]
        out.append(check(G, f"Report {rep}: words, hedges/1,000, nominalizations/100, Flesch", "7.9",
                         (int(r[9].replace(",", "")), float(r[10]), float(r[11]), float(r[12])),
                         (pr["words"], pr["hedges_per_1000"], pr["nominalizations_per_100"], pr["flesch"])))
        codes = sc[rep][1:10]
        touched = [f"SD{i}" for i, c in enumerate(codes, 1) if c == "T"]
        exp_t = r[4].split(" ")[0]
        out.append(check(G, f"Report {rep}: located, touched, missed, new substantive, mistaken (blind scorer)", "7.9",
                         (int(r[3]), int(exp_t), int(r[5].split(" ")[0]), int(r[7]), int(r[8])),
                         (codes.count("L"), len(touched), codes.count("M"), int(sc[rep][12]), int(sc[rep][13]))))
    cuts = sorted(round(100 * (1 - prof[(t, "S2")] / prof[(t, "S1")]), 1) for t in tiers)
    out.append(note(G, "Terse style shortened reviews by '42 to 47 percent'", "7.9 item 3", "42 to 47", cuts,
                    "Haiku 42.4%, Opus 42.5%, Sonnet 47.5%. The upper end rounds to 47 or 48 depending on convention."))
    out.append(check(G, "Terse reports stay between 2,000 and 2,800 words", "7.9 item 3", True,
                     all(2000 <= prof[(t, "S2")] <= 2850 for t in tiers),
                     "S2 lengths: " + ", ".join(str(prof[(t, 'S2')]) for t in tiers)))

    dr = profile(read("runs/02_reviewer_draft.md"))
    sg = profile(signed_review())
    body = profile(signed_review().split("**Checks run**", 1)[0])
    out.append(check(G, "Unassisted draft: words (with headings and the checks list)", "4.3", 1567, dr["words"]))
    out.append(check(G, "Signed review: words, by the same measure", "4.8", 3758, sg["words"]))
    out.append(check(G, "Signed review: words in the body (before the checks list and the note to the editor)", "4.8", 3334, body["words"]))
    out.append(check(G, "Flesch reading ease, signed review against draft", "4.8", (48.6, 47.1), (sg["flesch"], dr["flesch"])))
    out.append(check(G, "Hedges per 1,000 words, signed review against draft", "4.8", (7.2, 6.4), (sg["hedges_per_1000"], dr["hedges_per_1000"])))
    return out


if __name__ == "__main__":
    for r in run():
        print(r.status, "|", r.claim, "|", r.expected, "|", r.observed, "|", r.detail)
