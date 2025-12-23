from core.ollama_client import llm_call
import json
import re
from core.utils import safe_json_load

def plan_queries(topic):
    prompt = f"""
You are a planning module.

Return ONLY a valid JSON array of strings.
No explanations.
No markdown.
No backslashes.
No trailing commas.

Example:
["query one", "query two"]

Topic:
{topic}
"""

    response = llm_call(prompt, agent="planner")
    response = response.strip()
    response = response.replace("```json", "").replace("```", "")
    try:
        return safe_json_load(response)
    except Exception:
        # fallback: line-based parsing
        return [l.strip("-• ") for l in response.splitlines() if len(l.strip()) > 10]