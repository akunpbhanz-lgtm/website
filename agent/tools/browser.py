import json
from urllib.parse import urlparse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
POLICY_PATH = ROOT / "policy/network-allowlist.json"
allow_domains = set(json.loads(POLICY_PATH.read_text())["domains"])


def browse(url: str) -> str:
    domain = urlparse(url).netloc
    if domain not in allow_domains:
        raise ValueError("Domain not allowed")
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        content = page.content()
        browser.close()
        return content
