"""R02. The 37 executable checks (appendix Sections 4.4 to 4.6 and 4.10; Section 9.3).

1. Re-run every check file in runs/NN_checks/ in the same sandbox the harness used, and compare its stdout and exit
   code with the recorded .out.txt. Many checks are simulations; they fix their own random seeds, so their output
   is reproduced exactly.
2. Re-run the harness itself (tools/harness.py, unchanged) on the transcripts in a scratch copy: it must extract the
   same code blocks, under the same file names and check ids, and produce the same outputs. For the three probes the
   harness is given Part 1 only, which r01 shows is exactly what existed when the harness ran. This also reproduces
   the harness's labeling fault reported in Section 4.5 (`r-tce_chk_1_b2` carries the id `r-tce:chk:1` but is the
   code of `r-tce:chk:2`).
3. The codeSha256 recorded in each results.json matches the check file.
4. The key harness outputs quoted in the appendix appear verbatim in the re-run output.
"""
import glob
import json
import os
import shutil
import subprocess
import sys
import tempfile

from lib import ROOT, RUNS, check, probe_part1_bytes, read, recorded_output, sandbox_python, sha256_bytes

G = "Executable checks"

# Lines the appendix quotes from harness output, with the section that quotes them.
QUOTED = [
    ("08_checks/p08_chk_2.out.txt", "Appendix expression matches full cross-partial: False", "4.6"),
    ("08_checks/p08_chk_2.out.txt", "-h1*(g0 + g1*u + s)/((h0 + h1*u)**2*(m - 1)**2)", "4.6"),
    ("08_checks/p08_chk_2.out.txt", "A3 <=> Delta < 0: True", "4.6"),
    ("08_checks/p08_chk_2.out.txt", "74343", "4.6"),
    ("09_checks/p09_chk_5.out.txt", "mean b = 0.1458", "4.6 (quoted rounded as 0.146)"),
    ("09_checks/p09_chk_5.out.txt", "100%", "4.6"),
    ("09_checks/p09_chk_7.out.txt", "0.107", "4.6"),
    ("09_checks/p09_chk_4.out.txt", "2.69", "4.6"),
    ("09_checks/p09_chk_4.out.txt", "0.158", "4.6"),
    ("09_checks/p09_chk_4.out.txt", "0.693", "4.6"),
    ("09_checks/p09_chk_9.out.txt", "-0.063", "4.6"),
    ("07_checks/pnl_chk_1.out.txt", "Pearson r = -0.423 (p = 0.40); Spearman rho = -0.648 (p = 0.16); n = 6 pairs", "4.5"),
]

TRANSCRIPTS = ["03_simulated_reviewer_TCE.md", "04_simulated_reviewer_INST.md", "05_simulated_reviewer_BEH.md",
               "06_simulated_reviewer_DID.md", "07_panel_synthesis.md", "08_probe_derivation.md",
               "09_probe_identification_numerical.md", "10_probe_inferential_audit.md"]


def run():
    out = []
    files = sorted(glob.glob(os.path.join(RUNS, "*_checks", "*.py")))
    by_run = {}
    for f in files:
        by_run.setdefault(os.path.basename(os.path.dirname(f))[:2], []).append(f)
    sim = sum(len(by_run.get(k, [])) for k in ("03", "04", "05", "06"))
    prb = sum(len(by_run.get(k, [])) for k in ("08", "09", "10"))
    out.append(check(G, "Checks run in Section 4", "9.3", 37, len(files)))
    out.append(check(G, "… written by the simulated reviewers", "9.3", 18, sim))
    out.append(check(G, "… written by the probes", "9.3", 18, prb))
    out.append(check(G, "… written by the panel synthesis", "9.3", 1, len(by_run.get("07", []))))
    out.append(check(G, "Checks written by P-DER / P-ID and P-NUM / P-INF, P-MEAS and P-LIT", "4.6", (5, 9, 4),
                     tuple(len(by_run.get(k, [])) for k in ("08", "09", "10"))))

    # 1. Re-run each check
    diffs = []
    for f in files:
        rc, so, se = sandbox_python(f)
        header, rso, rse = recorded_output(f[:-3] + ".out.txt")
        rec_rc = int(header.rsplit("exit", 1)[1].strip())
        if so.rstrip("\n") != rso.rstrip("\n") or rc != rec_rc:
            diffs.append(os.path.relpath(f, ROOT))
    out.append(check(G, "Checks whose re-run stdout and exit code equal the recorded harness output", "4.4–4.6",
                     len(files), len(files) - len(diffs), "differ: " + ", ".join(diffs)))

    # 3. codeSha256 in results.json
    bad = []
    for rj in sorted(glob.glob(os.path.join(RUNS, "*_checks", "results.json"))):
        for r in json.load(open(rj)):
            fn = os.path.join(os.path.dirname(rj), r["file"])
            if sha256_bytes(open(fn, "rb").read()) != r["codeSha256"]:
                bad.append(r["file"])
    out.append(check(G, "Check files whose SHA-256 equals the codeSha256 the harness recorded", "4.6", 0, len(bad),
                     ", ".join(bad)))

    # 2. Re-run the harness on the transcripts
    with tempfile.TemporaryDirectory() as td:
        os.makedirs(os.path.join(td, "runs"))
        for t in TRANSCRIPTS:
            dst = os.path.join(td, "runs", t)
            rel = "runs/" + t
            if t[:2] in ("08", "09", "10"):
                open(dst, "wb").write(probe_part1_bytes(rel))
            else:
                shutil.copy(os.path.join(ROOT, rel), dst)
            subprocess.run([sys.executable, os.path.join(ROOT, "tools", "harness.py"), dst], capture_output=True,
                           text=True, check=True, timeout=1800)
        mism = []
        n = 0
        for d in sorted(glob.glob(os.path.join(td, "runs", "*_checks"))):
            got = sorted(os.path.basename(x) for x in glob.glob(os.path.join(d, "*.py")))
            want = sorted(os.path.basename(x) for x in glob.glob(os.path.join(RUNS, os.path.basename(d), "*.py")))
            if got != want:
                mism.append(f"{os.path.basename(d)}: names {got} vs {want}")
                continue
            for g in got:
                n += 1
                a = open(os.path.join(d, g), "rb").read()
                b = open(os.path.join(RUNS, os.path.basename(d), g), "rb").read()
                if a != b:
                    mism.append(g + " code")
                _, so1, se1 = recorded_output(os.path.join(d, g[:-3] + ".out.txt"))
                _, so2, se2 = recorded_output(os.path.join(RUNS, os.path.basename(d), g[:-3] + ".out.txt"))
                if (so1, se1) != (so2, se2):
                    mism.append(g + " output")
        out.append(check(G, "Harness re-run on the transcripts: check files extracted with the same names, code and output",
                         "4.0, 4.5", 37, n - len(mism), "; ".join(mism)))
        lab = open(os.path.join(td, "runs", "03_checks", "r-tce_chk_1_b2.out.txt")).readline().split()[1]
        out.append(check(G, "Harness labeling fault reproduced: r-tce_chk_1_b2 is labeled r-tce:chk:1", "4.5, 4.12 item 14",
                         "r-tce:chk:1", lab))

    # 4. Quoted outputs
    missing = [f"{f}: {s}" for f, s, _ in QUOTED if s not in read("runs/" + f)]
    out.append(check(G, "Harness output strings quoted in the appendix found in the outputs", "4.5, 4.6", len(QUOTED),
                     len(QUOTED) - len(missing), "; ".join(missing)))
    empty = [os.path.basename(f) for f in ("runs/05_checks/r-beh_chk_3.out.txt", "runs/05_checks/r-beh_chk_4.out.txt")
             if recorded_output(os.path.join(ROOT, f))[1].strip() == ""]
    out.append(check(G, "r-beh:chk:3 and r-beh:chk:4 print nothing (define functions only)", "4.5", 2, len(empty)))
    return out


if __name__ == "__main__":
    for r in run():
        print(r.status, "|", r.claim, "|", r.expected, "|", r.observed, "|", r.detail)
