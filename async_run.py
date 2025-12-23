import asyncio
from agents.planner import plan_queries
from agents.async_search import search_queries
from agents.async_scraper import scrape_all
from agents.cleaner import clean_text
from agents.synthesizer import synthesize
from agents.contradiction import detect_contradictions
from agents.confidence import score_facts

TOPIC = input("Research topic: ")

async def main():
    queries = plan_queries(TOPIC)
    results = await search_queries(queries)

    urls = list({r["href"] for r in results})
    scraped = await scrape_all(urls)

    sources = []
    for url, text in scraped:
        cleaned = clean_text(text or "")
        if len(cleaned) > 300:
            sources.append({"url": url, "content": cleaned})

    report, facts = synthesize(TOPIC, sources)

    contradictions = detect_contradictions(facts)
    scored = score_facts(facts)

    with open("outputs/report.md", "w") as f:
        f.write(report)

    with open("outputs/facts.json", "w") as f:
        import json
        json.dump(scored, f, indent=2)

    print("Done. Async research completed.")

asyncio.run(main())