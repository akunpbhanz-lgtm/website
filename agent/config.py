import json
from pathlib import Path

CONFIG_PATH = Path(__file__).resolve().parent / "config.json"
DEFAULT_CONFIG = {"mode": "auto"}


def load_config() -> dict:
    if CONFIG_PATH.exists():
        return json.loads(CONFIG_PATH.read_text())
    return DEFAULT_CONFIG.copy()


def save_config(cfg: dict) -> None:
    CONFIG_PATH.write_text(json.dumps(cfg))


def set_mode(mode: str) -> None:
    cfg = load_config()
    cfg["mode"] = mode
    save_config(cfg)
