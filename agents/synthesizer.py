from core.ollama_client import llm_call
from core.utils import safe_json_load

def synthesize(topic, sources):
    joined = "\n\n".join(
        f"Source ({s['url']}):\n{s['content']}"
        for s in sources[:6]  # HARD CAP (important)
    )

    prompt = f"""
You are a research system.

Return ONLY valid JSON.
No markdown.
No explanations.

JSON schema:
{{
  "report": "string",
  "facts": [
    {{
      "claim": "string",
      "source": "string"
    }}
  ]
}}

Topic: {topic}

Sources:
{joined}
"""

    response = llm_call(prompt, agent="synthesizer")

    # --- HARDENING ---
    response = response.strip()
    response = response.replace("```json", "").replace("```", "")

    try:
        data = safe_json_load(response)
        return data["report"], data.get("facts", [])
    except Exception:
        # Fallback: treat everything as report text
        return response, []