
"""
config_loader.py
-----------------------
Loads YAML configuration for GamaSafe 1.0 and makes it accessible
to all modules.

TODO:
- Add caching
- Validate data types
"""

import yaml

def load_config(path: str = "strategy/config.yaml") -> dict:
    """
    Loads YAML config file and returns as a dictionary.

    Parameters:
    - path: path to config.yaml

    Returns:
    - config: dict with all strategy & risk params
    """
    try:
        with open(path, "r") as f:
            config = yaml.safe_load(f)
        return config
    except Exception as e:
        print(f"[ERROR] Failed to load config: {e}")
        return {}
