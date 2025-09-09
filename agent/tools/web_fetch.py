import json
import time
from urllib.parse import urlparse
from pathlib import Path
import requests

ROOT = Path(__file__).resolve().parents[2]
POLICY_PATH = ROOT / "policy/network-allowlist.json"
allow_domains = set(json.loads(POLICY_PATH.read_text())["domains"])


def fetch(url: str, retries: int = 3, timeout: int = 10) -> str:
    domain = urlparse(url).netloc
    if domain not in allow_domains:
        raise ValueError("Domain not allowed")
    for attempt in range(retries):
        try:
            resp = requests.get(url, timeout=timeout)
            resp.raise_for_status()
            return resp.text
        except Exception:
            if attempt == retries - 1:
                raise
            time.sleep(2 ** attempt)
