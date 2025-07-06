# ---- scenario_loader.py ----
import yaml


def load_scenario(path: str) -> dict:
    with open(path, 'r') as f:
        return yaml.safe_load(f)