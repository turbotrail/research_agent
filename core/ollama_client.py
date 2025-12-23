import requests
import os

OLLAMA_URL = "http://192.168.0.242:11434/api/generate"
MODEL = os.getenv("MODEL", "gemma3:4b")

def ollama(prompt, temperature=0.2):
    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": temperature
        }
    }
    r = requests.post(OLLAMA_URL, json=payload, timeout=120)
    r.raise_for_status()
    return r.json()["response"]