# 🔎 Local Research Agent (Async, Free, Ollama-Powered)

A **fully local, free, async research agent** that searches the web, scrapes sources, detects contradictions, scores factual confidence, and produces structured research reports — powered by **Ollama** and open-source tooling.

Designed for **deep technical and scientific research**, not shallow summaries.

---

## ✨ Features

- ✅ Local LLMs via Ollama (no cloud, no paid APIs)
- ⚡ Async web search & scraping (3–5× faster)
- 🧠 Query planning agent
- 📄 Multi-source research synthesis
- ⚠️ Contradiction detection agent
- 📊 Fact confidence scoring
- 🛡️ Robust JSON handling & self-healing
- 📁 Markdown + JSON outputs
- 🔌 Model-agnostic (Qwen, LLaMA, etc.)

---

## 🧠 Recommended Models

| Task | Model |
|---|---|
| Query planning | llama3.2:1b |
| Contradiction detection | llama3.2:1b |
| Final synthesis | qwen2.5:7b |

> ⚠️ Small models (1B) are **not suitable** for deep physics or math-heavy synthesis (e.g. Bell’s theorem). Use them only for planning or classification.

---

## 📁 Project Structure

```
research_agent/
├── agents/
│   ├── planner.py
│   ├── async_search.py
│   ├── async_scraper.py
│   ├── cleaner.py
│   ├── synthesizer.py
│   ├── contradiction.py
│   └── confidence.py
│
├── core/
│   ├── ollama_client.py
│   └── utils.py
│
├── outputs/
│   ├── report.md
│   └── facts.json
│
├── async_run.py
├── requirements.txt
└── README.md
```

---

## 🚀 Quick Start

### 1️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Install & run Ollama

```bash
ollama pull qwen2.5:7b
ollama pull llama3.2:1b
ollama serve
```

If Ollama runs on another machine:

```bash
export OLLAMA_HOST=http://<OLLAMA_IP>:11434
```

---

### 3️⃣ Run the research agent

```bash
MODEL=qwen2.5:7b python async_run.py
```

Example input:

```
Research topic: bell's theorem
```

Outputs:
- `outputs/report.md`
- `outputs/facts.json`

---

## 🧪 Example Output

### Fact (JSON)

```json
{
  "claim": "Bell's theorem shows that no local hidden variable theory can reproduce all predictions of quantum mechanics",
  "source": "https://...",
  "confidence": 0.91
}
```

---

## 🛡️ Reliability & Safety

This project is designed to **not crash** when LLMs misbehave:

- Invalid JSON → auto-repair
- Empty responses → fallback paths
- Token overflow → context caps
- Weak models → graceful degradation

---

## ⚠️ Known Limitations

- DuckDuckGo results may vary by region
- Heavy math / LaTeX content is summarized, not derived
- No Google scraping (by design)
- No formal peer-review verification

---

## 🔮 Planned Enhancements

- Citation graph (fact → multiple sources)
- Math-aware parsing (LaTeX blocks)
- SQLite research cache
- RAG memory (Chroma / FAISS)
- Streamlit “Research Copilot” UI
- CLI flags (`--deep`, `--fast`, `--physics`)

---

## 📜 Philosophy

> **Research should be transparent, local, auditable, and reproducible.**

This project favors:
- Open models
- Open web
- Explicit uncertainty
- Human-readable outputs

---

## 📄 License

MIT License
