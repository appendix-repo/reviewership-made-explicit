"""Machine-origin share of a signed review (draft definition, appendix Section 5.3).

A sentence of the signed review is of machine origin if at least THRESHOLD of its word 5-grams occur in some
agent output of the session, after removing 5-grams that occur in the manuscript (quotations) or in the
reviewer's own unassisted draft (which precedes every agent output on the manuscript).

Usage: python3 machine_origin.py REVIEW_FILE --draft DRAFT --manuscript MS --agents A1 A2 ... [--threshold 0.6] [--json OUT]
REVIEW_FILE may contain the markers <!-- SIGNED REVIEW START --> and <!-- SIGNED REVIEW END -->; only the text
between them is scored.
"""
import argparse, json, re

ap = argparse.ArgumentParser()
ap.add_argument("review"); ap.add_argument("--draft", required=True); ap.add_argument("--manuscript", required=True)
ap.add_argument("--agents", nargs="+", required=True); ap.add_argument("--threshold", type=float, default=0.6)
ap.add_argument("--json")
a = ap.parse_args()

def words(t):
    return re.findall(r"[a-z0-9]+(?:['.][a-z0-9]+)*", t.lower())

def grams(t, n=5):
    w = words(t)
    return {tuple(w[i:i + n]) for i in range(len(w) - n + 1)}

def sentences(t):
    t = re.sub(r"```.*?```", " ", t, flags=re.S)          # code blocks are not review prose
    t = re.sub(r"^\s*#+\s*", "", t, flags=re.M)            # headings
    parts = re.split(r"(?<=[.!?])\s+|\n\s*[-*]\s+|\n{2,}", t)
    return [p.strip() for p in parts if len(words(p)) >= 5]

rev = open(a.review).read()
if "<!-- SIGNED REVIEW START -->" in rev:
    rev = rev.split("<!-- SIGNED REVIEW START -->", 1)[1].split("<!-- SIGNED REVIEW END -->", 1)[0]
ms_g = grams(open(a.manuscript).read())
draft_g = grams(open(a.draft).read())
agent_g = {}
for f in a.agents:
    agent_g[f] = grams(open(f).read())
all_agent = set().union(*agent_g.values())

rows = []
for s in sentences(rev):
    g = grams(s) - ms_g
    if not g:
        rows.append({"sentence": s, "n5": 0, "draft": 0.0, "agent": 0.0, "origin": "manuscript quotation or too short"}); continue
    d = len(g & draft_g) / len(g)
    rest = g - draft_g
    ag = len(rest & all_agent) / len(g)
    src = sorted(((len(rest & G) / len(g), f) for f, G in agent_g.items()), reverse=True)[0] if rest else (0.0, None)
    origin = "draft" if d >= a.threshold else ("agent" if ag >= a.threshold else ("mixed" if d + ag >= a.threshold else "new"))
    rows.append({"sentence": s, "n5": len(g), "draft": round(d, 2), "agent": round(ag, 2),
                 "closest_agent_output": src[1] if origin in ("agent", "mixed") else None, "origin": origin})

scored = [r for r in rows if r["n5"] > 0]
share = lambda k: round(sum(r["origin"] == k for r in scored) / len(scored), 3) if scored else 0.0
summary = {"sentences_scored": len(scored), "threshold": a.threshold,
           "machine_origin_share": share("agent"), "mixed_share": share("mixed"),
           "carried_from_draft_share": share("draft"), "new_share": share("new")}
print(json.dumps(summary, indent=1))
for r in rows:
    if r["origin"] in ("agent", "mixed"):
        print(f'- [{r["origin"]}, agent overlap {r["agent"]}, {r["closest_agent_output"]}] {r["sentence"][:160]}')
if a.json:
    json.dump({"summary": summary, "sentences": rows}, open(a.json, "w"), indent=1, ensure_ascii=False)
