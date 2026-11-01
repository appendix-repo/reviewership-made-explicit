"""R04. The signed review, its dispositions, the provenance trace and the editor view (appendix Sections 4.8, 4.9).

1. The trace: 42 events, the hash chain verified, 21 actual and 21 reconstructed times, every event valid against
   ProvenanceEvent in the schema, and the correction recorded at ev:35.
2. The dispositions: 117 decisions (74 accept, 35 modify, 8 reject) and the table by source.
3. The machine-origin share at the four thresholds of Section 4.9, recomputed with tools/machine_origin.py; at the
   defined threshold the output is byte-identical to runs/14_machine_origin.json.
4. The editor view regenerated with tools/editor_view.py from the trace as it stood at signature (ev:1 to ev:39):
   byte-identical to runs/14_editor_view.md; and where the accepted and modified findings land.
"""
import collections
import hashlib
import json
import os
import re
import tempfile

import jsonschema

from lib import AGENT_OUTPUTS, ROOT, check, dispositions, p, provenance, read, run_tool

G = "Provenance and signed review"


def chain_ok(ev):
    prev = "0" * 64
    for e in ev:
        body = {k: v for k, v in e.items() if k != "hash"}
        h = hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()
        if e["prevHash"] != prev or h != e["hash"]:
            return False, e["@id"]
        prev = e["hash"]
    return True, None


def run():
    out = []
    ev = provenance()
    ok, where = chain_ok(ev)
    kinds = collections.Counter(e["timestampKind"] for e in ev)
    out.append(check(G, "Events in the trace", "4.9", 42, len(ev)))
    out.append(check(G, "Hash chain verifies (SHA-256 over canonical JSON, linked to predecessor)", "2.5, 4.9", True, ok,
                     f"breaks at {where}" if where else ""))
    out.append(check(G, "Events with actual / reconstructed times", "4.9", (21, 21), (kinds["actual"], kinds["reconstructed"])))
    schema = json.loads(read("schema/review-objects.v0.schema.json"))
    sub = {"$schema": schema.get("$schema"), "$defs": schema["$defs"], "$ref": "#/$defs/ProvenanceEvent"}
    v = jsonschema.Draft202012Validator(sub)
    invalid = [e["@id"] for e in ev if list(v.iter_errors(e))]
    out.append(check(G, "Events valid against ProvenanceEvent in the schema", "4.9, 9.3", 42, 42 - len(invalid),
                     ", ".join(invalid)))
    e35 = [e for e in ev if e["@id"] == "ev:35"][0]
    out.append(check(G, "ev:35 records a correction before publication (actor kind of ev:31)", "4.9", True,
                     e35["action"] == "annotate" and "ev:31" in e35["inputs"] and "stand-in" in e35["rationale"]))
    out.append(check(G, "Actor kind of ev:31 after the correction", "4.9", "stand-in",
                     [e for e in ev if e["@id"] == "ev:31"][0]["actor"]["kind"]))
    out.append(check(G, "Events of Runs 01–14 up to signature (the trace the editor view uses)", "4.9", 39,
                     [i for i, e in enumerate(ev, 1) if e["action"] == "sign"][0]))

    # Dispositions
    d = dispositions()
    c = collections.Counter(x["decision"] for x in d)
    out.append(check(G, "Decisions: total, accept, modify, reject", "4.8", (117, 74, 35, 8),
                     (len(d), c["accept"], c["modify"], c["reject"])))
    out.append(check(G, "Accept or modify decisions on workbench findings", "4.9", 109, c["accept"] + c["modify"]))

    def bucket(src):
        if src.startswith("Run 11"):
            return "Consistency check on the draft (Run 11)"
        if src.startswith("Run 07"):
            return "Panel synthesis (Run 07), its own items"
        if src.startswith("Runs "):
            return "Findings raised by several roles, decided together"
        if re.match(r"Run (08|09|10)", src):
            return "Probes (Runs 08–10), single-role items and decisions"
        if re.match(r"Run 0[3-6]", src):
            return "Simulated reviewers, single-role items"
        return "other: " + src
    tab = collections.OrderedDict()
    for x in d:
        b = tab.setdefault(bucket(x["source"]), collections.Counter())
        b["n"] += 1
        b[x["decision"]] += 1
    want = {"Consistency check on the draft (Run 11)": (24, 3, 1),
            "Panel synthesis (Run 07), its own items": (22, 6, 1),
            "Findings raised by several roles, decided together": (28, 12, 0),
            "Probes (Runs 08–10), single-role items and decisions": (38, 13, 3),
            "Simulated reviewers, single-role items": (5, 1, 3)}
    for k, (n, m, r) in want.items():
        got = tab.get(k, collections.Counter())
        out.append(check(G, f"Dispositions from: {k} (decisions, modified, rejected)", "4.8", (n, m, r),
                         (got["n"], got["modify"], got["reject"])))
    out.append(check(G, "Rejected findings land nowhere in the review", "4.8", 0,
                     sum(1 for x in d if x["decision"] == "reject" and x.get("landsIn"))))

    # Machine origin
    base = ["tools/machine_origin.py", "runs/12_reviewer_dispositions_final_review.md", "--draft", "runs/02_reviewer_draft.md",
            "--manuscript", "case/TEST_MANUSCRIPT.md", "--agents"] + AGENT_OUTPUTS
    want = {0.6: (1.9, 0.0, 14.2, 83.9), 0.4: (6.0, 0.4, 17.2, 76.4), 0.3: (9.4, 1.1, 22.1, 67.4), 0.2: (15.7, 1.1, 26.6, 56.6)}
    with tempfile.TemporaryDirectory() as td:
        for th, exp in want.items():
            js = os.path.join(td, f"mo_{th}.json")
            run_tool(base + ["--threshold", str(th), "--json", js])
            s = json.load(open(js))["summary"]
            got = tuple(round(100 * s[k], 1) for k in ("machine_origin_share", "mixed_share", "carried_from_draft_share", "new_share"))
            out.append(check(G, f"Composition at threshold {th}: machine, mixed, draft, new (% of sentences)", "4.9", exp, got))
            if th == 0.6:
                out.append(check(G, "Sentences scored", "4.9", 267, s["sentences_scored"]))
                same = open(js, "rb").read() == open(p("runs/14_machine_origin.json"), "rb").read()
                out.append(check(G, "Machine-origin analysis byte-identical to runs/14_machine_origin.json", "4.9", True, same))
                rows = json.load(open(js))["sentences"]
                ag = [r["sentence"].lstrip("- ").strip() for r in rows if r["origin"] == "agent"]
                out.append(check(G, "Sentences of machine origin at the defined threshold", "4.9", 5, len(ag)))
                out.append(check(G, "Longest machine-origin sentence", "4.9",
                                 "The rating's coefficient barely moves when m enters (−0.094 to −0.091).", max(ag, key=len)))

        # Editor view from the trace at signature
        evf = os.path.join(td, "events_at_signature.json")
        json.dump(ev[:39], open(evf, "w"), indent=1, ensure_ascii=False)
        outf = os.path.join(td, "14_editor_view.md")
        run_tool(["tools/editor_view.py", "--events", evf, "--final", "runs/12_reviewer_dispositions_final_review.md",
                  "--origin", "runs/14_machine_origin.json", "--out", outf])
        gen = open(outf, encoding="utf-8").read()
    out.append(check(G, "Editor view regenerated from ev:1–ev:39 is byte-identical to runs/14_editor_view.md", "4.9", True,
                     gen == read("runs/14_editor_view.md")))
    out.append(check(G, "Editor view reports the hash chain verified", "4.9", True, "Hash chain: verified" in gen))
    land = collections.Counter()
    proc = 0
    for x in d:
        if x["decision"] not in ("accept", "modify"):
            continue
        parts = [s.strip() for s in re.split(r";\s*", str(x.get("landsIn") or "")) if s.strip()]
        for s in parts:
            land[s] += 1
        if parts and all(s.lower().startswith("process only") for s in parts):
            proc += 1
    top = sorted(land.items(), key=lambda kv: -kv[1])[:2]
    out.append(check(G, "Parts of the signed review where most accepted/modified findings land", "4.9",
                     {"Major 2": 26, "Minor concerns": 26}, dict(top)))
    out.append(check(G, "Decisions that concern process only and land in no text", "4.9", 7, proc))
    return out


if __name__ == "__main__":
    for r in run():
        print(r.status, "|", r.claim, "|", r.expected, "|", r.observed, "|", r.detail)
