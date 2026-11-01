"""Append a ProvenanceEvent to runs/provenance_events.json (hash-chained, SHA-256 over canonical JSON).
Usage: python3 prov.py ACTION ACTOR_KIND ACTOR_NAME [--model M] [--iset V] [--route R] [--in a,b] [--out c,d]
       [--responds ev:n] [--why TEXT] [--file PATH_TO_HASH] [--time ISO --kind reconstructed]"""
import json, sys, hashlib, argparse, datetime, os
F = os.path.join(os.path.dirname(__file__), "..", "runs", "provenance_events.json")
ap = argparse.ArgumentParser()
ap.add_argument("action"); ap.add_argument("kind"); ap.add_argument("name")
for a in ["--model", "--iset", "--route", "--in", "--out", "--responds", "--why", "--file", "--time"]: ap.add_argument(a)
ap.add_argument("--tkind", default="actual")
a = ap.parse_args()
ev = json.load(open(F)) if os.path.exists(F) else []
prev = ev[-1]["hash"] if ev else "0" * 64
actor = {"kind": a.kind, "name": a.name}
if a.model: actor["model"] = a.model
if a.iset: actor["instructionSetVersion"] = a.iset
if a.route: actor["gatewayRoute"] = a.route
e = {"@id": f"ev:{len(ev)+1}", "@type": "ProvenanceEvent",
     "timestamp": a.time or datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
     "timestampKind": a.tkind, "actor": actor, "action": a.action,
     "inputs": a.__dict__["in"].split(",") if a.__dict__["in"] else [], "outputs": a.out.split(",") if a.out else []}
if a.responds: e["respondsTo"] = a.responds
if a.why: e["rationale"] = a.why
if a.file: e["contentHash"] = hashlib.sha256(open(a.file, "rb").read()).hexdigest()
e["prevHash"] = prev
e["hash"] = hashlib.sha256(json.dumps(e, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()
ev.append(e); json.dump(ev, open(F, "w"), indent=1, ensure_ascii=False)
print(e["@id"], e["timestamp"], e["action"], e["hash"][:12])
