"""Check harness (demonstration version). Extracts every ```python block from a probe's Part 1 output,
labels it with the nearest preceding CheckSpec id (pNN:chk:n), runs it in a fresh isolated interpreter
(python3 -I, empty environment, 120 s timeout, working directory a temporary folder), and writes the code,
stdout/stderr and run time to runs/NN_checks/. Usage: python3 harness.py runs/08_probe_derivation.md"""
import re, sys, os, subprocess, tempfile, datetime, json, hashlib
src = os.path.abspath(sys.argv[1]); text = open(src).read()
run = re.search(r"/(\d\d)_", "/" + os.path.basename(src)).group(1)
outdir = os.path.join(os.path.dirname(src), f"{run}_checks"); os.makedirs(outdir, exist_ok=True)
blocks = [(m.start(), m.group(1)) for m in re.finditer(r"```python\n(.*?)```", text, re.S)]
results = []
for i, (pos, code) in enumerate(blocks, 1):
    ids = re.findall(r"[a-z0-9-]+:chk:\d+", text[:pos]) or re.findall(r"[a-z0-9-]+:chk:\d+", code)
    cid = ids[-1] if ids else f"p{run}:chk:?{i}"
    # prefer an id named inside the block's first lines
    head = re.findall(r"[a-z0-9-]+:chk:\d+", code[:300])
    if head: cid = head[0]
    fn = os.path.join(outdir, cid.replace(":", "_") + ".py")
    if os.path.exists(fn): fn = fn.replace(".py", f"_b{i}.py")
    open(fn, "w").write(code)
    with tempfile.TemporaryDirectory() as td:
        t0 = datetime.datetime.now(datetime.timezone.utc)
        try:
            p = subprocess.run([sys.executable, "-I", fn], capture_output=True, text=True, timeout=120, cwd=td,
                               env={"PATH": "/usr/bin:/bin", "MPLBACKEND": "Agg"})
            out, err, rc = p.stdout, p.stderr, p.returncode
        except subprocess.TimeoutExpired:
            out, err, rc = "", "TIMEOUT after 120 s", -1
    ran = t0.strftime("%Y-%m-%dT%H:%M:%SZ")
    open(fn.replace(".py", ".out.txt"), "w").write(f"# {cid}  ran {ran}  exit {rc}\n## stdout\n{out}\n## stderr\n{err[-3000:]}\n")
    verdicts = [l for l in out.splitlines() if l.startswith("VERDICT")]
    results.append({"check": cid, "file": os.path.basename(fn), "ranAt": ran, "exit": rc,
                    "verdicts": verdicts, "codeSha256": hashlib.sha256(code.encode()).hexdigest()})
json.dump(results, open(os.path.join(outdir, "results.json"), "w"), indent=1)
for r in results: print(r["check"], r["exit"], r["verdicts"][:3])
