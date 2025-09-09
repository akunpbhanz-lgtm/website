import json
import shlex
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ALLOW_PATH = ROOT / "policy/allowlist.json"
DENY_PATH = ROOT / "policy/denylist.json"

allowlist = json.loads(ALLOW_PATH.read_text())["commands"]
denylist = json.loads(DENY_PATH.read_text())["patterns"]


def run_shell(command: str) -> str:
    parts = shlex.split(command)
    if not parts:
        raise ValueError("Empty command")
    if parts[0] not in allowlist:
        raise ValueError("Command not allowed")
    for pattern in denylist:
        if pattern in command:
            raise ValueError("Command denied")
    completed = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
    return completed.stdout.strip()
