"""R08. Counts read off the transcripts (appendix Sections 4.1, 4.2, 4.4, 4.5, 4.7, 4.11, 4.12).

These are tallies of ids, words and table rows in the files, not computations. Word counts in Sections 4.1, 4.2 and
4.4 were made when the runs were written, and the appendix does not state the tokenizer. This script counts
whitespace-separated tokens, which reproduces most of the reported counts exactly; where it does not, the result is
a NOTE with the size of the difference.
"""
import json
import re

from lib import APPENDIX, check, note, read

G = "Counts"

WORDS = [  # file, reported, section
    ("case/TEST_MANUSCRIPT.md", 2744, "4.1"),
    ("runs/01_dialogue/turn_01_elicitor_E0.md", 863, "4.2"),
    ("runs/01_dialogue/turn_02_editor.md", 816, "4.2"),
    ("runs/01_dialogue/turn_03_elicitor_EB_S1.md", 1751, "4.2"),
    ("runs/01_dialogue/turn_04_reviewer_S1.md", 2322, "4.2"),
    ("runs/01_dialogue/turn_05_elicitor_S2.md", 3978, "4.2"),
    ("runs/01_dialogue/turn_06_reviewer_S2.md", 2246, "4.2"),
    ("runs/01_dialogue/turn_07_elicitor_S3.md", 4886, "4.2"),
    ("runs/01_dialogue/turn_08_reviewer_S3.md", 2399, "4.2"),
    ("runs/01_dialogue/turn_09_elicitor_SPEC.md", 9509, "4.2"),
    ("runs/03_simulated_reviewer_TCE.md", 8266, "4.4"),
    ("runs/04_simulated_reviewer_INST.md", 8939, "4.4"),
    ("runs/05_simulated_reviewer_BEH.md", 8855, "4.4"),
    ("runs/06_simulated_reviewer_DID.md", 9585, "4.4"),
]


def ids(text, pat):
    return sorted(set(re.findall(pat, text)), key=lambda s: [int(x) if x.isdigit() else x for x in re.split(r"(\d+)", s)])


def run():
    out = []
    for f, rep, sec in WORDS:
        n = len(read(f).split())
        diff = n - rep
        if diff == 0:
            out.append(check(G, f"Words in {f}", sec, rep, n))
        else:
            extra = ""
            if f.endswith("turn_04_reviewer_S1.md"):
                extra = (" The 23 October version of the appendix gave 1,751, which equals the whitespace count of this"
                         " file; the 31 October version gives 2322, which this script cannot reproduce by any common"
                         " word-count convention. Worth checking before submission.")
            out.append(note(G, f"Words in {f}", sec, rep, n,
                            f"whitespace count differs by {diff:+d} ({100 * diff / rep:+.1f}%).{extra}"))

    out.append(check(G, "Bytes of runs/11_consistency_check.md", "4.7", 35792, len(read("runs/11_consistency_check.md", "rb"))))

    spec = read("runs/01_dialogue/turn_09_elicitor_SPEC.md")
    out.append(check(G, "Standards in the specification (std:1 to std:16)", "4.2", 16, len(ids(spec, r"std:\d+"))))
    out.append(check(G, "Tensions in the specification (bs:T1 to bs:T7)", "4.2", 7, len(ids(spec, r"bs:T\d+"))))
    foc = json.loads(read("runs/configs/focal_perspective_normalized.json"))
    out.append(check(G, "The normalized focal perspective sets all five dimensions", "4.0, 5.1", ["EPI", "INF", "ONT", "PRA", "TEC"],
                     sorted(foc["dimensions"])))

    mc = read("runs/11_consistency_check.md")
    out.append(check(G, "Mode C: silent skips, undeclared standards, internal-consistency items", "4.7", (7, 4, 6),
                     (len(ids(mc, r"bs:CS\d+")), len(ids(mc, r"bs:CU\d+")), len(ids(mc, r"bs:CI\d+")))))

    pnl = read("runs/07_panel_synthesis.md")
    out.append(check(G, "Panel: agreement ids (27 findings and 6 agreed strengths, repairs and probes)", "4.5", 33,
                     len(ids(pnl, r"pnl:agr:\d+"))))
    out.append(check(G, "Panel: entries in the disagreement map", "4.5", 18, len(ids(pnl, r"pnl:dis:\d+"))))
    out.append(check(G, "Panel: contributions aligned", "4.5", 8, len(ids(pnl, r"pnl:ctb:\d+"))))

    p08 = read("runs/08_probe_derivation.md")
    p09 = read("runs/09_probe_identification_numerical.md")
    p10 = read("runs/10_probe_inferential_audit.md")
    out.append(check(G, "Probe findings: Run 08, Run 09 (with the new p09:fnd:12), Run 10", "4.6", (8, 12, 21),
                     (len(ids(p08, r"p08:fnd:\d+")), len(ids(p09, r"p09:fnd:\d+")), len(ids(p10, r"p10:fnd:\d+")))))

    app = open(APPENDIX, encoding="utf-8").read()
    sec = app.split("### 4.11", 1)[1].split("### 4.12", 1)[0]
    rows = [l for l in sec.splitlines() if l.startswith("| ") and not l.startswith("| Work as verified")]
    verdicts = [l.rstrip(" |").rsplit("|", 1)[1].strip() for l in rows]
    partly = sum(v.startswith("**Partly") for v in verdicts)
    out.append(check(G, "Works checked in the citation table; partly supported", "4.11", (54, 3), (len(rows), partly)))
    out.append(check(G, "Works marked † (checked against an online record)", "4.11", 6, sum("†" in l.split("|")[1] for l in rows)))

    s412 = app.split("### 4.12", 1)[1].split("\n---", 1)[0]
    out.append(check(G, "Numbered items in Section 4.12", "4.12", 16, len(re.findall(r"^\d+\. \*\*", s412, re.M))))
    return out


if __name__ == "__main__":
    for r in run():
        print(r.status, "|", r.claim, "|", r.expected, "|", r.observed, "|", r.detail)
