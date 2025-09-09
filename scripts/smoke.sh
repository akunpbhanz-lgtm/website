#!/bin/bash
set -e
python -m agent.main --help >/dev/null
PYTHONPATH=. pytest -q
