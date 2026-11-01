"""Shared helpers for the replication scripts.

Every script in this folder exposes run() -> list[Result]. Each Result ties one number or claim in the technical
appendix (docs/REVIEWERSHIP_TECHNICAL_APPENDIX.md) to what the script recomputes from the files in this repository.

Status values:
  PASS  the recomputed value equals the value the appendix reports;
  FAIL  it does not;
  NOTE  the appendix's value is reproduced only approximately, or depends on a counting convention the files do not
        fix; the script says how close it is and why.
"""
import dataclasses
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
RUNS = os.path.join(ROOT, "runs")
TOOLS = os.path.join(ROOT, "tools")
APPENDIX = os.path.join(ROOT, "docs", "REVIEWERSHIP_TECHNICAL_APPENDIX.md")
if TOOLS not in sys.path:
    sys.path.insert(0, TOOLS)

# The four simulated reviews, the panel synthesis, the three probes and the consistency check: the agent outputs
# of the session against which the machine-origin share is computed (appendix Sections 4.9 and 5.3).
AGENT_OUTPUTS = [
    "runs/03_simulated_reviewer_TCE.md", "runs/04_simulated_reviewer_INST.md",
    "runs/05_simulated_reviewer_BEH.md", "runs/06_simulated_reviewer_DID.md",
    "runs/07_panel_synthesis.md", "runs/08_probe_derivation.md",
    "runs/09_probe_identification_numerical.md", "runs/10_probe_inferential_audit.md",
    "runs/11_consistency_check.md",
]


@dataclasses.dataclass
class Result:
    group: str
    claim: str
    section: str
    expected: object
    observed: object
    status: str
    detail: str = ""


def check(group, claim, section, expected, observed, detail=""):
    return Result(group, claim, section, expected, observed, "PASS" if expected == observed else "FAIL", detail)


def note(group, claim, section, expected, observed, detail):
    return Result(group, claim, section, expected, observed, "NOTE", detail)


def p(rel):
    return os.path.join(ROOT, rel)


def read(rel, mode="r"):
    with open(p(rel), mode, **({} if "b" in mode else {"encoding": "utf-8"})) as f:
        return f.read()


def sha256_file(rel):
    with open(p(rel), "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


def sandbox_python(script_path, timeout=300):
    """Run a Python file as the demonstration harness did (tools/harness.py): `python -I`, an empty environment
    apart from PATH and MPLBACKEND, a fresh temporary working directory, a time limit."""
    with tempfile.TemporaryDirectory() as td:
        try:
            r = subprocess.run([sys.executable, "-I", os.path.abspath(script_path)], capture_output=True, text=True,
                               timeout=timeout, cwd=td, env={"PATH": "/usr/bin:/bin", "MPLBACKEND": "Agg"})
            return r.returncode, r.stdout, r.stderr
        except subprocess.TimeoutExpired:
            return -1, "", "TIMEOUT"


def recorded_output(out_txt):
    """Split a harness .out.txt into (header, stdout, stderr)."""
    t = open(out_txt, encoding="utf-8").read()
    m = re.match(r"(# .*?)\n## stdout\n(.*)\n## stderr\n(.*)\Z", t, re.S)
    return m.group(1), m.group(2), m.group(3)


def run_tool(args, timeout=600):
    r = subprocess.run([sys.executable] + args, capture_output=True, text=True, timeout=timeout, cwd=ROOT)
    if r.returncode != 0:
        raise RuntimeError(f"{' '.join(args)} failed:\n{r.stderr[-2000:]}")
    return r.stdout


def provenance():
    return json.loads(read("runs/provenance_events.json"))


def signed_review():
    t = read("runs/12_reviewer_dispositions_final_review.md")
    return t.split("<!-- SIGNED REVIEW START -->", 1)[1].split("<!-- SIGNED REVIEW END -->", 1)[0]


def dispositions():
    t = read("runs/12_reviewer_dispositions_final_review.md")
    for blk in re.findall(r"```json\s*(.*?)```", t, flags=re.S):
        try:
            j = json.loads(blk)
        except json.JSONDecodeError:
            continue
        if isinstance(j, dict) and "Dispositions" in j:
            return j["Dispositions"]
    raise RuntimeError("no Dispositions block")


def md_table(text, header_startswith):
    """Return the rows (lists of stripped cells) of the first Markdown table whose header row starts with the given
    text."""
    lines = text.splitlines()
    for i, l in enumerate(lines):
        if l.startswith(header_startswith):
            head = [c.strip() for c in l.strip().strip("|").split("|")]
            rows = []
            for l2 in lines[i + 2:]:
                if not l2.startswith("|"):
                    break
                rows.append([c.strip() for c in l2.strip().strip("|").split("|")])
            return head, rows
    raise RuntimeError(f"table not found: {header_startswith}")


# Offsets at which Part 1 of each probe ends. Part 1 is what the harness was given; Part 2 was appended after the
# harness had run. The offsets are not assumptions: replication/r01_integrity.py shows that the SHA-256 of exactly
# these prefixes equals the contentHash the provenance trace recorded for Part 1 (ev:16, ev:26, ev:20).
PROBE_PART1 = {
    "runs/08_probe_derivation.md": ("ev:16", "\n---\n\n# Part 2: disposition after the harness"),
    "runs/09_probe_identification_numerical.md": ("ev:26", "\n---\n\n## Part 2: disposition after the harness"),
    "runs/10_probe_inferential_audit.md": ("ev:20", "\n---\n\n# Part 2: disposition after the harness"),
}


def probe_part1_bytes(rel):
    b = read(rel, "rb")
    marker = PROBE_PART1[rel][1].encode()
    return b[: b.index(marker) + 1]  # Part 1 ends with the blank line before the "---" rule
