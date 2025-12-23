import requests
from core.config import CONFIG

def ollama_call(prompt, model, temperature):
    url = CONFIG["llm"]["ollama"]["base_url"] + "/v1/chat/completions"

    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": temperature
    }

    r = requests.post(
        url,
        json=payload,
        timeout=CONFIG["limits"]["request_timeout"]
    )
    r.raise_for_status()
    return r.json()["choices"][0]["message"]["content"]

def openai_call(prompt, model, temperature):
    url = CONFIG["llm"]["openai"]["base_url"] + "/chat/completions"

    headers = {
        "Authorization": f"Bearer {CONFIG['llm']['openai']['api_key']}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": temperature
    }

    r = requests.post(
        url,
        headers=headers,
        json=payload,
        timeout=CONFIG["limits"]["request_timeout"]
    )
    r.raise_for_status()
    return r.json()["choices"][0]["message"]["content"]

def llm_call(prompt, agent="default"):
    provider = CONFIG["llm"]["provider"]
    agent_cfg = CONFIG["agents"].get(agent, {})

    model = agent_cfg.get(
        "model",
        CONFIG["llm"][provider]["default_model"]
    )
    temperature = agent_cfg.get("temperature", 0.2)

    if provider == "ollama":
        return ollama_call(prompt, model, temperature)

    if provider == "openai":
        return openai_call(prompt, model, temperature)

    raise ValueError(f"Unknown LLM provider: {provider}")