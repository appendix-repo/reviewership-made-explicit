"""Re-execute the demonstration session of the technical appendix (Section 4) with fresh model calls.

This is a RE-EXECUTION kit, not a reproduction. The published runs (runs/) were single, unedited model runs made on
23 October 2026; model outputs are not deterministic, so a new session will not reproduce them word for word. What
this script does reproduce is the protocol: the order of the workbench loop (appendix Section 2.7), the instruction
sets each role received (instruction-sets/REVIEWERSHIP_INSTRUCTION_SETS.md, v0.1), the stand-in personas (Section S
of that file), the information each role may see, the sealed key, the check harness, and the hash-chained provenance
record. Reviewers can use it to see whether the qualitative results of Section 4 recur, and then score a new session
with the same deterministic tools the replication scripts use (see README.md, "Re-executing the session").

Prompts. The orchestrating session assembled each role's prompt by hand from the instruction set; those wrappers were
not saved verbatim. The prompts built here follow the instruction set and Section 4.0 of the appendix and are
written out (with their SHA-256) before any call, so that a re-execution is fully inspectable.

Information flow (Section 4.0), enforced by Agent.attach():
  - the elicitor never receives the manuscript, in any mode;
  - the editor stand-in receives the manuscript; the reviewer stand-in does not, until it drafts;
  - the panel synthesizer does not receive the manuscript;
  - only the two scorers (blind pilot scorer, recovery scorer) receive the sealed key.

Usage:
  python reexecute/run_session.py --dry-run                 # build and save every prompt; no API call
  python reexecute/run_session.py --out reexecute/out/s1    # full session (needs Anthropic credentials)
  python reexecute/run_session.py --only 01,02 --out ...    # a subset of runs (later runs read earlier outputs)
Options: --model (default claude-opus-5-5), --effort (default high), --pilot-models (three ids, low to high tier).
"""
import argparse
import datetime
import hashlib
import json
import os
import random
import re
import subprocess
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
ISET_PATH = os.path.join(ROOT, "instruction-sets", "REVIEWERSHIP_INSTRUCTION_SETS.md")
MS_PATH = os.path.join(ROOT, "case", "TEST_MANUSCRIPT.md")
KEY_PATH = os.path.join(ROOT, "case", "SEALED_DEFECT_KEY.md")
EDITOR_NOTE = ("I would value your reading of the transaction-cost model and the empirical design. "
               "The paper makes strong claims against the institutional account.")  # appendix Section 4.0, item 3
STANDIN_NOTE = ("After your reply, add a section headed exactly '### OUT-OF-ROLE NOTE' in which you step out of the "
                "persona and say, briefly, where you think your reply departs from what a human in this role would do.")
PILOT_STYLES = {  # appendix Section 7.5
    "S1": "Write in the voice of a senior, authoritative reviewer for a leading journal.",
    "S2": "Terse numbered findings, no rhetoric.",
}
SCORER_KINDS = {"pilot-scorer", "recovery-scorer"}


def read(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


def sha(s):
    return hashlib.sha256(s.encode() if isinstance(s, str) else s).hexdigest()


# ---------------------------------------------------------------- instruction-set sections

ISET = read(ISET_PATH)


def section(heading):
    """Text from a heading line to the next heading of the same or higher level."""
    level = len(heading) - len(heading.lstrip("#"))
    i = ISET.index(heading)
    rest = ISET[i + len(heading):]
    m = re.search(r"^#{1,%d} " % level, rest, re.M)
    return (heading + rest[: m.start()] if m else heading + rest).strip().rstrip("-").strip()


SHARED = "\n\n".join(section(h) for h in ("## Common preamble (all roles)",
                                          "## The perspective specification (shared by all roles)",
                                          "## The scoreboard (shared output format)"))
ROLE = {"elicitor": section("## Role 1. The Best-Self Elicitor (capability 1)"),
        "simulated": section("## Role 2. The Simulated Reviewer (capability 2)"),
        "panel": section("## Role 3. The Panel Synthesizer (capability 2)"),
        "probe": section("## Role 4. The Adversarial Probe (capability 3)")}
PERSONA = {"editor": section("### S1. Handling editor (stand-in)"), "reviewer": section("### S2. Focal reviewer (stand-in)")}


def invitation():
    ms = read(MS_PATH)
    title = ms.splitlines()[0].lstrip("# ").strip()
    abstract = ms.split("## Abstract", 1)[1].split("\n## ", 1)[0].strip()
    return f"**Invitation to review**\n\nTitle: {title}\n\nAbstract: {abstract}\n\nEditor's note: {EDITOR_NOTE}"


# ---------------------------------------------------------------- provenance (same hashing as tools/prov.py)

class Trace:
    def __init__(self, path):
        self.path, self.ev = path, []

    def add(self, action, kind, name, inputs=(), outputs=(), why=None, content=None, model=None):
        actor = {"kind": kind, "name": name}
        if model:
            actor["model"] = model
            actor["instructionSetVersion"] = "Reviewership v0.1"
        e = {"@id": f"ev:{len(self.ev) + 1}", "@type": "ProvenanceEvent",
             "timestamp": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
             "timestampKind": "actual", "actor": actor, "action": action, "inputs": list(inputs), "outputs": list(outputs)}
        if why:
            e["rationale"] = why
        if content is not None:
            e["contentHash"] = sha(content)
        e["prevHash"] = self.ev[-1]["hash"] if self.ev else "0" * 64
        e["hash"] = sha(json.dumps(e, sort_keys=True, separators=(",", ":"), ensure_ascii=False))
        self.ev.append(e)
        json.dump(self.ev, open(self.path, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
        return e["@id"]


# ---------------------------------------------------------------- agents

class Agent:
    """One separate model instance: its own system prompt and its own conversation."""
    ACCESS = {  # which kinds of input each role may receive
        "elicitor": {"invitation", "relay", "specification", "draft"},
        "editor-standin": {"manuscript", "relay"},
        "reviewer-standin": {"invitation", "relay", "manuscript", "specification", "draft", "workbench"},
        "simulated": {"manuscript"},
        "panel": {"simulated-review", "check-output", "draft", "distances"},
        "probe": {"manuscript", "check-output"},
        "pilot": {"manuscript"},
        "pilot-scorer": {"manuscript", "key", "blind-review"},
        "recovery-scorer": {"manuscript", "key", "output"},
    }

    def __init__(self, sess, kind, name, system):
        self.sess, self.kind, self.name, self.system, self.messages = sess, kind, name, system, []
        self.model = sess.model
        self._pending = []
        slug = re.sub(r"[^a-z0-9]+", "_", name.lower()).strip("_")
        self.log = os.path.join(sess.out, "prompts", slug)
        os.makedirs(self.log, exist_ok=True)
        open(os.path.join(self.log, "system.md"), "w", encoding="utf-8").write(system)

    def attach(self, kind, label, text):
        if kind not in self.ACCESS[self.kind]:
            raise PermissionError(f"{self.name} ({self.kind}) may not receive {kind} ({label})")
        if kind == "key" and self.kind not in SCORER_KINDS:
            raise PermissionError("the sealed key goes only to the scorers")
        self._pending.append(f"<file name=\"{label}\">\n{text}\n</file>")

    def send(self, text):
        content = "\n\n".join(self._pending + [text])
        self._pending = []
        self.messages.append({"role": "user", "content": content})
        n = len(self.messages)
        open(os.path.join(self.log, f"turn_{n:02d}_user.md"), "w", encoding="utf-8").write(content)
        reply = self.sess.call(self)
        self.messages.append({"role": "assistant", "content": reply})
        open(os.path.join(self.log, f"turn_{n:02d}_assistant.md"), "w", encoding="utf-8").write(reply)
        return reply


def split_note(text):
    if "### OUT-OF-ROLE NOTE" in text:
        a, b = text.split("### OUT-OF-ROLE NOTE", 1)
        return a.rstrip() + "\n", "### OUT-OF-ROLE NOTE" + b
    return text, ""


class Session:
    def __init__(self, a):
        self.out, self.model, self.effort, self.dry = a.out, a.model, a.effort, a.dry_run
        os.makedirs(os.path.join(self.out, "runs", "01_dialogue"), exist_ok=True)
        self.trace = Trace(os.path.join(self.out, "runs", "provenance_events.json"))
        self.client = None
        if not self.dry:
            import anthropic  # imported here so that --dry-run needs no SDK
            self.client = anthropic.Anthropic()
        self.calls = []

    def call(self, agent):
        if self.dry:
            return f"[DRY RUN: no model call was made for {agent.name}, turn {len(agent.messages)}]"
        with self.client.messages.stream(
            model=agent.model, max_tokens=64000, system=agent.system, messages=agent.messages,
            thinking={"type": "adaptive"}, output_config={"effort": self.effort},
        ) as stream:
            msg = stream.get_final_message()
        self.calls.append({"agent": agent.name, "requested_model": agent.model, "served_model": msg.model,
                           "stop_reason": msg.stop_reason, "usage": msg.usage.model_dump() if msg.usage else None})
        json.dump(self.calls, open(os.path.join(self.out, "calls.json"), "w"), indent=1)
        if msg.stop_reason == "refusal":
            # Appendix Section 4.12, item 11: a refused role is recorded, never silently dropped.
            self.trace.add("annotate", "orchestrator", "re-execution session", why=f"{agent.name}: request refused by the "
                           f"model provider's safeguard ({getattr(msg, 'stop_details', None)})")
            raise RuntimeError(f"{agent.name}: refused; see provenance_events.json")
        if msg.stop_reason == "max_tokens":
            raise RuntimeError(f"{agent.name}: output hit max_tokens")
        return "".join(b.text for b in msg.content if b.type == "text")

    def save(self, rel, text):
        p = os.path.join(self.out, "runs", rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        open(p, "w", encoding="utf-8").write(text)
        return p

    def harness(self, path):
        if self.dry:
            return ""
        subprocess.run([sys.executable, os.path.join(ROOT, "tools", "harness.py"), path], check=True, timeout=3600)
        d = os.path.join(os.path.dirname(path), os.path.basename(path)[:2] + "_checks")
        outs = sorted(f for f in os.listdir(d) if f.endswith(".out.txt")) if os.path.isdir(d) else []
        return "\n\n".join(f"<file name=\"{os.path.basename(d)}/{f}\">\n{read(os.path.join(d, f))}\n</file>" for f in outs)


def system_for(role, extra=""):
    return f"{SHARED}\n\n---\n\n{ROLE[role]}" + (f"\n\n---\n\n{extra}" if extra else "")


def standin_system(persona):
    return (PERSONA[persona] + "\n\nYou are a stand-in for a human participant in a demonstration of a reviewing "
            "workbench. Stay in persona in your replies. " + STANDIN_NOTE)


# ---------------------------------------------------------------- the runs

def run01(s, st):
    """Run 01: Best-Self elicitation, Modes E and S (appendix Section 4.2)."""
    inv = invitation()
    el = Agent(s, "elicitor", "Best-Self Elicitor", system_for("elicitor"))
    ed = Agent(s, "editor-standin", "Editor stand-in", standin_system("editor"))
    rv = Agent(s, "reviewer-standin", "Reviewer stand-in (elicitation)", standin_system("reviewer"))
    el.attach("invitation", "invitation.md", inv)
    t = {}
    t[1] = el.send("Mode E. Write your questions to the handling editor, in one message, with a draft editor brief.")
    ed.attach("manuscript", "TEST_MANUSCRIPT.md", read(MS_PATH))
    t[2] = ed.send("The Best-Self Elicitor writes to you:\n\n" + t[1])
    ans2, note2 = split_note(t[2])
    t[3] = el.send("The editor's answers:\n\n" + ans2 + "\n\nWrite the editor brief and Mode S, Round 1, to the reviewer.")
    rv.attach("invitation", "invitation.md", inv)
    for k, prompt in [(4, "Round 1"), (6, "Round 2"), (8, "Round 3")]:
        t[k] = rv.send("The Best-Self Elicitor writes to you:\n\n" + t[k - 1])
        ans, _ = split_note(t[k])
        if k < 8:
            t[k + 1] = el.send(f"The reviewer's reply to {prompt}:\n\n{ans}\n\nContinue with the next round.")
    ans8, _ = split_note(t[8])
    t[9] = el.send("The reviewer's reply to Round 3:\n\n" + ans8 + "\n\nOutput the standards specification "
                   "(StandardsSpecification), including the reviewer's perspective as a ReviewingPerspective JSON object.")
    names = {1: "turn_01_elicitor_E0", 2: "turn_02_editor", 3: "turn_03_elicitor_EB_S1", 4: "turn_04_reviewer_S1",
             5: "turn_05_elicitor_S2", 6: "turn_06_reviewer_S2", 7: "turn_07_elicitor_S3", 8: "turn_08_reviewer_S3",
             9: "turn_09_elicitor_SPEC"}
    for k, n in names.items():
        body, note = split_note(t[k]) if k in (2, 4, 6, 8) else (t[k], "")
        s.save(f"01_dialogue/{n}.md", body)
        if note:
            s.save(f"01_dialogue/{n}_standin_note.md", note)
        kind = "stand-in" if k in (2, 4, 6, 8) else "agent"
        s.trace.add("specify" if k == 9 else "elicit", kind, ["Editor stand-in", "Reviewer stand-in"][k > 2] if kind == "stand-in"
                    else "Best-Self Elicitor", content=body, model=s.model, why=f"Run 01, turn {k}")
    st["spec"] = t[9]


def run02(s, st):
    """Run 02: the reviewer's unassisted draft (Section 4.3)."""
    rv = Agent(s, "reviewer-standin", "Reviewer stand-in (draft)", standin_system("reviewer"))
    rv.attach("manuscript", "TEST_MANUSCRIPT.md", read(MS_PATH))
    rv.attach("specification", "standards_specification.md", st["spec"])
    body, note = split_note(rv.send("Draft your review now, as this reviewer would in one sitting of about an hour."))
    s.save("02_reviewer_draft.md", body)
    if note:
        s.save("02_reviewer_draft_standin_note.md", note)
    s.trace.add("draft", "stand-in", "Reviewer stand-in", content=body, why="Run 02: unassisted draft")
    st["draft"] = body


LENSES = [("03", "TCE", "persp:R-TCE"), ("04", "INST", "persp:R-INST"), ("05", "BEH", "persp:R-BEH"), ("06", "DID", "persp:R-DID")]


def run03_06(s, st):
    """Runs 03 to 06: four simulated reviewers, then the harness on their checks (Section 4.4)."""
    ps = {p["@id"]: p for p in json.load(open(os.path.join(ROOT, "runs", "configs", "simulated_perspectives.json")))}
    st["sims"] = {}
    for run, tag, pid in LENSES:
        p = ps[pid]
        cfg = (f"## Your configuration\n\n[perspective]\n```json\n{json.dumps(p, indent=1, ensure_ascii=False)}\n```\n\n"
               f"[lens]: {p['label']}\n\n[corpus]: {'; '.join(p['corpus'])}\n\n[relation]: {p['relationToFocal']}")
        a = Agent(s, "simulated", f"Simulated Reviewer {tag}", system_for("simulated", cfg))
        a.attach("manuscript", "TEST_MANUSCRIPT.md", read(MS_PATH))
        text = a.send("Write your simulated review.")
        path = s.save(f"{run}_simulated_reviewer_{tag}.md", text)
        s.trace.add("simulate", "agent", f"Simulated Reviewer ({p['label']})", inputs=["ms:TEST", pid], content=text, model=s.model)
        st["sims"][tag] = (text, s.harness(path))
    s.trace.add("check", "harness", "check harness", why="Checks written by the simulated reviewers, run for the record")


def run07(s, st):
    """Run 07: the panel synthesis (Section 4.5)."""
    d = subprocess.run([sys.executable, os.path.join(ROOT, "tools", "perspective_distance.py"),
                        os.path.join(ROOT, "runs", "configs", "focal_perspective_normalized.json"),
                        os.path.join(ROOT, "runs", "configs", "simulated_perspectives.json")],
                       capture_output=True, text=True, check=True).stdout
    a = Agent(s, "panel", "Panel Synthesizer", system_for("panel"))
    for tag, (text, outs) in st["sims"].items():
        a.attach("simulated-review", f"simulated_review_{tag}.md", text)
        if outs:
            a.attach("check-output", f"checks_{tag}.md", outs)
    a.attach("draft", "reviewer_draft.md", st["draft"])
    a.attach("distances", "perspective_distances.md", d)
    text = a.send("Synthesize the panel. Any statistic you compute must be bound to a check, as for every role.")
    path = s.save("07_panel_synthesis.md", text)
    s.harness(path)
    s.trace.add("synthesize", "agent", "Panel Synthesizer", content=text, model=s.model)
    st["panel"] = text


PROBES = [("08", "probe_derivation", "P-DER (with P-NUM on arithmetic in §2 and §4 that bears on the model)"),
          ("09", "probe_identification_numerical", "P-ID; P-NUM on every reported statistic in §3 and §4"),
          ("10", "probe_inferential_audit", "P-INF, P-MEAS, P-LIT (no literature search is available)")]


def run08_10(s, st):
    """Runs 08 to 10: adversarial probes, Part 1, harness, Part 2 (Section 4.6)."""
    st["probes"] = {}
    for run, name, types in PROBES:
        a = Agent(s, "probe", f"Adversarial Probe {run}", system_for("probe", f"[probe types]: {types}"))
        a.attach("manuscript", "TEST_MANUSCRIPT.md", read(MS_PATH))
        p1 = a.send("Write Part 1: reconstruction, scoreboard, findings and checks. Label each check with its id "
                    f"(p{run}:chk:n) in a comment on its first line. Do not run the checks.")
        path = s.save(f"{run}_{name}.md", "# Part 1\n\n" + p1 + "\n\n")
        s.trace.add("probe", "agent", f"Adversarial Probe ({types.split(';')[0]}), Part 1", content=read(path), model=s.model)
        outs = s.harness(path)
        s.trace.add("check", "harness", "check harness", why=f"Run {run} checks executed")
        a.attach("check-output", f"{run}_checks.md", outs or "[no harness output]")
        p2 = a.send("The harness has run your checks; the outputs are attached. Write Part 2: dispose of every bound "
                    "finding as demonstrated, refuted-by-check or inconclusive, revise severities, and end with a ranked "
                    "list and the decisions for the reviewer.")
        full = read(path) + "---\n\n# Part 2: disposition after the harness\n\n" + p2
        s.save(f"{run}_{name}.md", full)
        s.trace.add("probe", "agent", f"Adversarial Probe {run}, Part 2", content=full, model=s.model)
        st["probes"][run] = (full, outs)


def run11(s, st):
    """Run 11: the consistency check, Mode C (Section 4.7). The elicitor still has no manuscript."""
    a = Agent(s, "elicitor", "Best-Self Elicitor (Mode C)", system_for("elicitor"))
    a.attach("specification", "standards_specification.md", st["spec"])
    a.attach("draft", "reviewer_draft.md", "\n".join(f"dr:L{i} {l}" for i, l in enumerate(st["draft"].splitlines(), 1)))
    text = a.send("Mode C. Check the reviewer's draft (lines numbered dr:Ln) against the specification. Mark "
                  "needs_manuscript: true wherever a judgment would need the manuscript.")
    s.save("11_consistency_check.md", text)
    s.trace.add("consistency-check", "agent", "Best-Self Elicitor (Mode C)", content=text, model=s.model)
    st["mode_c"] = text


def run12(s, st):
    """Run 12: dispositions and the signed review (Section 4.8)."""
    rv = Agent(s, "reviewer-standin", "Reviewer stand-in (dispositions)", standin_system("reviewer"))
    rv.attach("manuscript", "TEST_MANUSCRIPT.md", read(MS_PATH))
    rv.attach("specification", "standards_specification.md", st["spec"])
    rv.attach("draft", "your_draft.md", st["draft"])
    rv.attach("workbench", "11_consistency_check.md", st["mode_c"])
    rv.attach("workbench", "07_panel_synthesis.md", st["panel"])
    for run, (text, outs) in st["probes"].items():
        rv.attach("workbench", f"probe_{run}.md", text)
    for tag, (text, outs) in st["sims"].items():
        rv.attach("workbench", f"simulated_review_{tag}.md", text)
    out = rv.send(
        "Decide on every finding rated fatal or damaging, every probe finding the harness demonstrated, refuted or left "
        "inconclusive, every item in the panel's 'What the focal reviewer faces', every question the consistency check "
        "puts to you, and every probe's decisions for the reviewer; decide other findings in groups. Write no code. "
        "Output one file: first a fenced ```json block {\"Dispositions\": [{\"finding\", \"source\", \"decision\" "
        "(accept | reject | modify), \"reason\" (one line), \"landsIn\" (the part of the signed review, or null)}]}; then "
        "the revised, signed review between the lines <!-- SIGNED REVIEW START --> and <!-- SIGNED REVIEW END -->; then "
        "'# Attestation'.")
    body, note = split_note(out)
    s.save("12_reviewer_dispositions_final_review.md", body)
    if note:
        s.save("12_reviewer_standin_note.md", note)
    s.trace.add("sign", "stand-in", "Reviewer stand-in", content=body, why="Run 12: dispositions and signed review")


def run13(s, st, pilot_models):
    """Run 13: the base-model pilot (Section 7.9): three tiers x two styles, blind labels, blind scorer."""
    cells = [(m, sty) for m in pilot_models for sty in ("S1", "S2")]
    labels = list("ABCDEF")
    random.SystemRandom().shuffle(labels)
    umap = {}
    for (m, sty), lab in zip(cells, labels):
        a = Agent(s, "pilot", f"Pilot {m} {sty}", "Write a referee report on the academic manuscript. " + PILOT_STYLES[sty])
        a.model = m
        a.attach("manuscript", "TEST_MANUSCRIPT.md", read(MS_PATH))
        s.save(f"13_pilot/blind/review_{lab}.md", a.send("Write the referee report."))
        umap[lab] = f"{m}_{sty}"
    um = json.dumps(dict(sorted(umap.items())), indent=1)
    s.save("13_pilot/UNBLINDING_MAP.json", um)
    s.trace.add("simulate", "agent", "Base-model pilot", why=f"Outputs blind-labelled; mapping sha256 {sha(um)} before scoring")
    sc = Agent(s, "pilot-scorer", "Blind pilot scorer", "You score referee reports against a sealed defect key. You are "
               "not told which model or style produced any report.")
    sc.attach("manuscript", "TEST_MANUSCRIPT.md", read(MS_PATH))
    sc.attach("key", "SEALED_DEFECT_KEY.md", read(KEY_PATH))
    for lab in "ABCDEF":
        sc.attach("blind-review", f"review_{lab}.md", read(os.path.join(s.out, "runs", "13_pilot", "blind", f"review_{lab}.md")))
    text = sc.send("Score each report on each seeded defect (L located, T touched, M missed) by the key's recovery rule; "
                   "count known-unseeded weaknesses, new substantive categories and mistaken findings; give a summary "
                   "table '| Report | SD1 | ... | SD9 | Located | Touched | New-substantive | Mistaken | Recommendation |' "
                   "and list the calls you were unsure of.")
    s.save("13_pilot/scoring.md", text)
    s.trace.add("score", "agent", "Blind pilot scorer", content=text)


def recovery(s, st):
    """Section 4.10: recovery scoring of every output that makes findings, with the sealed key."""
    sc = Agent(s, "recovery-scorer", "Recovery scorer", "You score review outputs against a sealed defect key.")
    sc.attach("manuscript", "TEST_MANUSCRIPT.md", read(MS_PATH))
    sc.attach("key", "SEALED_DEFECT_KEY.md", read(KEY_PATH))
    for rel in ["02_reviewer_draft.md"] + [f"{r}_simulated_reviewer_{t}.md" for r, t, _ in LENSES] + \
               [f"{r}_{n}.md" for r, n, _ in PROBES]:
        sc.attach("output", rel, read(os.path.join(s.out, "runs", rel)))
    text = sc.send("Score each output on SD1–SD9 (L, T, M; mark † where a finding appears only as a referral to another "
                   "probe type), count known-unseeded weaknesses and new substantive categories, give a category-by-output "
                   "table with ✓ where an output raises a category, and list the calls you were unsure of.")
    s.save("recovery_scoring.md", text)
    s.trace.add("score", "agent", "Recovery scorer", content=text)


def run14(s, st):
    """Run 14: machine-origin share and editor view, with the deterministic tools (Section 4.9)."""
    if s.dry:
        return
    r = os.path.join(s.out, "runs")
    agents = [os.path.join(r, f) for f in [f"{x}_simulated_reviewer_{t}.md" for x, t, _ in LENSES] +
              ["07_panel_synthesis.md"] + [f"{x}_{n}.md" for x, n, _ in PROBES] + ["11_consistency_check.md"]]
    subprocess.run([sys.executable, os.path.join(ROOT, "tools", "machine_origin.py"),
                    os.path.join(r, "12_reviewer_dispositions_final_review.md"), "--draft", os.path.join(r, "02_reviewer_draft.md"),
                    "--manuscript", MS_PATH, "--agents", *agents, "--json", os.path.join(r, "14_machine_origin.json")], check=True)
    subprocess.run([sys.executable, os.path.join(ROOT, "tools", "editor_view.py"), "--events", os.path.join(r, "provenance_events.json"),
                    "--final", os.path.join(r, "12_reviewer_dispositions_final_review.md"),
                    "--origin", os.path.join(r, "14_machine_origin.json"), "--out", os.path.join(r, "14_editor_view.md")], check=True)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", default=os.path.join(ROOT, "reexecute", "out",
                                                  datetime.datetime.now().strftime("%Y%m%d_%H%M%S")))
    ap.add_argument("--model", default="claude-opus-5-5")
    ap.add_argument("--effort", default="high", choices=["low", "medium", "high", "xhigh", "max"])
    ap.add_argument("--pilot-models", default="claude-haiku-5-5,claude-sonnet-5-5,claude-opus-5-5")
    ap.add_argument("--only", default="", help="comma-separated runs, e.g. 01,02,03-06,07,08-10,11,12,13,rec,14")
    ap.add_argument("--dry-run", action="store_true", help="build and save every prompt without calling the API")
    a = ap.parse_args()
    if os.path.abspath(a.out).startswith(os.path.join(ROOT, "runs")):
        sys.exit("refusing to write into runs/: the published runs are read-only")
    s = Session(a)
    s.trace.add("ingest", "orchestrator", "re-execution session", outputs=["ms:TEST"], content=read(MS_PATH))
    s.trace.add("seal", "orchestrator", "re-execution session", inputs=["ms:TEST"], outputs=["key:SEALED"],
                content=read(KEY_PATH), why="Sealed key registered by hash; withheld from every role but the scorers")
    st = {"spec": "[specification]", "draft": "[draft]", "sims": {}, "probes": {}, "panel": "", "mode_c": ""}
    steps = [("01", run01), ("02", run02), ("03-06", run03_06), ("07", run07), ("08-10", run08_10), ("11", run11),
             ("12", run12), ("13", lambda s_, st_: run13(s_, st_, a.pilot_models.split(","))), ("rec", recovery), ("14", run14)]
    only = set(filter(None, a.only.split(",")))
    for k, f in steps:
        if not only or k in only:
            print(f"[run {k}]", flush=True)
            f(s, st)
    open(os.path.join(a.out, "PROMPT_HASHES.txt"), "w").write(
        "\n".join(f"{sha(read(os.path.join(dp, f)))}  {os.path.relpath(os.path.join(dp, f), a.out)}"
                  for dp, _, fs in sorted(os.walk(os.path.join(a.out, "prompts"))) for f in sorted(fs)) + "\n")
    print("done:", a.out)


if __name__ == "__main__":
    main()
