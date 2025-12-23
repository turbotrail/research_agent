from core.ollama_client import ollama
import itertools

def detect_contradictions(facts):
    contradictions = []

    for a, b in itertools.combinations(facts, 2):
        prompt = f"""
Do the following two statements contradict each other?

Statement A:
{a['claim']}

Statement B:
{b['claim']}

Answer ONLY as JSON:
{{"contradiction": true/false, "reason": "..."}}
"""
        resp = ollama(prompt, temperature=0)
        if '"contradiction": true' in resp:
            contradictions.append({
                "a": a,
                "b": b,
                "analysis": resp
            })

    return contradictions