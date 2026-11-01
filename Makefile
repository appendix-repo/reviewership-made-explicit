.PHONY: setup replicate dry-run
setup:
	python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
replicate:
	.venv/bin/python replication/replicate_all.py
dry-run:
	.venv/bin/python reexecute/run_session.py --dry-run --out reexecute/out/dry-run
