import json
from core.ollama_client import llm_call
from core.utils import safe_json_load


def score_facts(facts):
    """
    Score factual confidence using an LLM agent.

    Input:
    facts = [
        { "claim": "...", "source": "url" }
    ]

    Output:
    [
        {
          "claim": "...",
          "source": "...",
          "confidence": 0.0–1.0,
          "reasoning": "..."
        }
    ]
    """

    if not facts:
        return []

    prompt = f"""
You are a fact verification assistant.

For each factual claim below, assign a confidence score between 0.0 and 1.0.

Base your score on:
- Reliability of the source
- Specificity of the claim
- Certainty of language
- General scientific or factual plausibility

Return ONLY valid JSON in this exact format:

[
  {{
    "claim": "...",
    "source": "...",
    "confidence": 0.0,
    "reasoning": "short explanation"
  }}
]

Facts:
{json.dumps(facts, indent=2)}
"""

    response = llm_call(prompt, agent="confidence")

    response = response.strip().replace("```json", "").replace("```", "")

    try:
        return safe_json_load(response)
    except Exception:
        # Graceful fallback: mark confidence as unknown
        return [
            {
                **f,
                "confidence": None,
                "reasoning": "LLM confidence scoring failed"
            }
            for f in facts
        ]