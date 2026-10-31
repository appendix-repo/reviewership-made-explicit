"""Check every file listed in MANIFEST.txt against its recorded size and SHA-256 prefix.
Usage: python verify.py   (run from the repository root)"""
import hashlib, os, sys
ok = bad = missing = 0
for line in open("MANIFEST.txt", encoding="utf-8"):
    if line.startswith("#") or not line.strip():
        continue
    path, size, prefix = line.rstrip("\n").split("\t")
    if not os.path.exists(path):
        missing += 1
        print("MISSING ", path)
        continue
    data = open(path, "rb").read()
    good = hashlib.sha256(data).hexdigest().startswith(prefix) and (size == "-" or len(data) == int(size))
    ok += good
    bad += not good
    if not good:
        print("MISMATCH", path)
print(f"{ok} verified, {bad} mismatched, {missing} missing (see the PLACEHOLDER.md files and runs/MISSING_FILES.md)")
sys.exit(1 if bad else 0)
