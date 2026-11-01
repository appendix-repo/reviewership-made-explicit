"""R01. Integrity of the record (appendix Section 4.1, Section 4.9, Annex C).

1. Every file listed in Annex C has the byte count and SHA-256 prefix the appendix prints.
2. The test manuscript and the sealed defect key hash to the values in case/HASHES.txt, which are also the
   contentHash of provenance events ev:1 and ev:2 (recorded before any role ran).
3. Every contentHash in the provenance trace matches a file in the repository. For the three probes, the hash
   recorded when Part 1 was written matches the file's Part 1 exactly, so Part 1 was fixed before the harness ran
   and Part 2 was appended afterwards.
4. The blind pilot's unblinding map hashes to the value logged before scoring (ev:9) and matched at unblinding (ev:25).
"""
import glob
import os
import re

from lib import (ROOT, APPENDIX, PROBE_PART1, check, note, p, probe_part1_bytes, provenance, read, sha256_bytes,
                 sha256_file)

G = "Integrity"


def run():
    out = []
    # 1. Annex C manifest, parsed from the appendix itself
    text = open(APPENDIX, encoding="utf-8").read()
    annex = text.split("## Annex C.", 1)[1].split("## Annex D.", 1)[0]
    rows = re.findall(r"^\| `([^`]+)` \| ([\d,]+) \| `([0-9a-f]{16})…` \|$", annex, re.M)
    bad = []
    for f, size, prefix in rows:
        if not os.path.exists(p(f)):
            bad.append(f"{f}: missing")
            continue
        if os.path.getsize(p(f)) != int(size.replace(",", "")) or sha256_file(f)[:16] != prefix:
            bad.append(f"{f}: size or hash differs")
    n_rows = sum(1 for l in annex.splitlines() if l.startswith("| `"))
    out.append(check(G, "Annex C manifest rows parsed (every file row of the table)", "Annex C", n_rows, len(rows)))
    out.append(check(G, "Annex C files whose size and SHA-256 prefix match", "Annex C", len(rows), len(rows) - len(bad),
                     "; ".join(bad)))

    # 2. Case hashes
    hashes = dict(reversed(l.split()) for l in read("case/HASHES.txt").splitlines() if l.strip())
    for name, short, sect in [("TEST_MANUSCRIPT.md", "a8ab4709…52d0", "4.1"), ("SEALED_DEFECT_KEY.md", "970e0574…809d", "4.1")]:
        h = sha256_file("case/" + name)
        out.append(check(G, f"SHA-256 of case/{name} equals case/HASHES.txt", "4.1", hashes[name], h))
        out.append(check(G, f"Hash of case/{name} as printed in the appendix ({short})", "4.1",
                         short, f"{h[:8]}…{h[-4:]}"))
    ev = {e["@id"]: e for e in provenance()}
    out.append(check(G, "ev:1 registers the manuscript by its hash", "4.1", hashes["TEST_MANUSCRIPT.md"], ev["ev:1"]["contentHash"]))
    out.append(check(G, "ev:2 seals the defect key by its hash", "4.1", hashes["SEALED_DEFECT_KEY.md"], ev["ev:2"]["contentHash"]))
    out.append(check(G, "The key was sealed before any role ran (ev:2 precedes ev:3)", "4.0, 4.1", True,
                     ev["ev:2"]["timestamp"] < ev["ev:3"]["timestamp"]))

    # 3. Every contentHash in the trace
    by_hash = {}
    for f in glob.glob(os.path.join(ROOT, "**", "*"), recursive=True):
        if os.path.isfile(f) and "/.git/" not in f:
            by_hash.setdefault(sha256_file(os.path.relpath(f, ROOT)), os.path.relpath(f, ROOT))
    for rel, (eid, _) in PROBE_PART1.items():
        by_hash.setdefault(sha256_bytes(probe_part1_bytes(rel)), rel + " (Part 1)")
    with_hash = [e for e in ev.values() if "contentHash" in e]
    unmatched = [e["@id"] for e in with_hash if e["contentHash"] not in by_hash]
    out.append(check(G, "Provenance events whose contentHash matches a file (or a probe's Part 1) in the repository",
                     "4.9", len(with_hash), len(with_hash) - len(unmatched), "unmatched: " + ", ".join(unmatched)))
    for rel, (eid, _) in PROBE_PART1.items():
        out.append(check(G, f"{eid}: hash of Part 1 of {os.path.basename(rel)} as written before the harness ran",
                         "4.6, 4.9", ev[eid]["contentHash"], sha256_bytes(probe_part1_bytes(rel))))

    # 4. Unblinding map
    um = sha256_file("runs/13_pilot/UNBLINDING_MAP.json")
    out.append(check(G, "Unblinding map hash logged at ev:9 (prefix b5ad0406)", "7.9", "b5ad0406", um[:8]))
    out.append(check(G, "Unblinding map matched at ev:25", "7.9", ev["ev:25"]["contentHash"], um))
    out.append(check(G, "Unblinding map hashed before scoring began (ev:9 not after ev:10)", "7.9", True,
                     ev["ev:9"]["timestamp"] <= ev["ev:10"]["timestamp"]))
    return out


if __name__ == "__main__":
    for r in run():
        print(r.status, "|", r.claim, "|", r.expected, "|", r.observed, "|", r.detail)
