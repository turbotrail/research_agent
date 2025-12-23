import yaml
import os
from dotenv import load_dotenv

load_dotenv()

def load_config(path="config/config.yaml"):
    with open(path, "r") as f:
        raw = yaml.safe_load(f)

    # Resolve ${ENV_VAR}
    def resolve(value):
        if isinstance(value, str) and value.startswith("${"):
            return os.getenv(value[2:-1])
        return value

    def walk(obj):
        if isinstance(obj, dict):
            return {k: walk(resolve(v)) for k, v in obj.items()}
        if isinstance(obj, list):
            return [walk(v) for v in obj]
        return resolve(obj)

    return walk(raw)

CONFIG = load_config()