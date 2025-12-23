import json
import re

def safe_json_load(text):
    """
    Attempts to extract and parse JSON from LLM output safely.
    """
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass

    # Try to extract JSON array manually
    match = re.search(r"\[.*\]", text, re.DOTALL)
    if not match:
        raise ValueError("No JSON array found in LLM output")

    cleaned = match.group(0)

    # Remove invalid escape sequences
    cleaned = cleaned.replace("\\", "")

    try:
        return json.loads(cleaned)
    except json.JSONDecodeError as e:
        raise ValueError(f"Failed to parse JSON after cleanup:\n{cleaned}") from e