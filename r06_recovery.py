"""R06. Seeded-defect recovery and unseeded yield (appendix Section 4.10; Sections 5.3 and 9.2).

The scoring itself was done by a separate model instance against the sealed key (runs/recovery_scoring.md,
runs/recovery_scoring_R12.md); it is a judgment and cannot be recomputed. What can be recomputed is every count the
appendix derives from the scorer's codes:
1. the recovery table of Section 4.10, row by row, from the scorer's summary table;
2. the 32 categories of substantive weakness, how many the draft raised (17), how many the workbench roles raised
   together (31), how many only the roles raised (15, i.e. 48%), and the one raised by the draft alone;
3. the final review's 28 categories against the draft's 17 (an 11-category gain), and the split of the five
   workbench-only categories it does not raise;
4. the demonstration rate (4 of 4; 5 of 5 with SD8) from the probes' statuses.
"""
from lib import APPENDIX, check, md_table, read

G = "Recovery"
RAISED = ("✓", "†")


def run():
    out = []
    app = open(APPENDIX, encoding="utf-8").read()
    rs = read("runs/recovery_scoring.md")
    r12 = read("runs/recovery_scoring_R12.md")

    _, arow = md_table(app, "| Output | SD1 |")
    _, srow = md_table(rs, "| Run | SD1 |")
    _, s12 = md_table(r12, "| Run | SD1 |")
    scorer = {r[0].split()[0]: r for r in srow + s12}
    for a in arow:
        run_id = "R" + a[0].replace("*", "").split()[0]
        s = scorer[run_id]
        loc = int(a[10].split()[0])
        out.append(check(G, f"{a[0].replace('*', '')}: SD codes, located, known-unseeded, new-substantive, mistaken", "4.10",
                         (a[1:10], loc, int(a[11]), int(a[12]), int(a[13])),
                         (s[1:10], int(s[10]), int(s[12]), int(s[13]), int(s[14]))))

    head, cats = md_table(rs, "| Category | R02 |")
    cols = head[1:]
    out.append(check(G, "Categories of substantive weakness identified by the scorers", "4.10", 32, len(cats)))
    draft = {c[0] for c in cats if c[1] in RAISED}
    roles = {c[0] for c in cats if any(x in RAISED for x in c[2:])}
    only_roles = roles - draft
    only_draft = draft - roles
    out.append(check(G, "Categories raised by the unassisted draft", "4.10", 17, len(draft)))
    out.append(check(G, "Categories raised by the workbench roles together", "4.10", 31, len(roles)))
    out.append(check(G, "Categories the roles raised and the draft did not (incremental recall)", "4.10", (15, 48),
                     (len(only_roles), round(100 * len(only_roles) / len(roles)))))
    out.append(check(G, "Category raised by the draft and by no role", "4.10", ["NS-q H2 omitted from summary"], sorted(only_draft)))

    _, c12 = md_table(r12, "| Category | R12 |")
    final = {c[0] for c in c12 if c[1] in RAISED}
    _, extra = md_table(r12, "| | KU raised |")
    ns_ab = [e for e in extra if e[0] == "R12"][0][3] == "yes"
    n_final = len(final) + (1 if ns_ab else 0)
    out.append(check(G, "Categories raised by the signed review (the 32, plus the new A3 category NS-ab)", "4.10", 28, n_final))
    out.append(check(G, "… all 17 of the draft's categories among them", "4.10", True, draft <= final))
    out.append(check(G, "… of the 15 workbench-only categories, raised in the signed review", "4.10", 10, len(only_roles & final)))
    out.append(check(G, "Gain of the signed review over the draft, in categories", "4.10", 11, n_final - len(draft)))
    out.append(check(G, "Workbench-only categories the signed review does not raise", "4.10",
                     sorted(["KU5 corner k* ≥ 1", "NS-o other post-outcome controls", "NS-p classification drift",
                             "NS-y behavioural rival", "NS-aa Nickell-type peer bias"]), sorted(only_roles - final)))

    _, st = md_table(rs, "| Probe | SD | In scope | Where | Status after Part 2 |")
    demo = {r[1].split()[0] for r in st if r[4].startswith("demonstrated")}
    out.append(check(G, "Demonstrable seeded defects demonstrated by the harness in at least one probe (SD1, SD2, SD3, SD6; and SD8)",
                     "4.10", ["SD1", "SD2", "SD3", "SD6", "SD8"], sorted(demo & {"SD1", "SD2", "SD3", "SD6", "SD8"})))
    return out


if __name__ == "__main__":
    for r in run():
        print(r.status, "|", r.claim, "|", r.expected, "|", r.observed, "|", r.detail)
