from agents.planner import plan_queries
from agents.search import web_search
from agents.scraper import scrape_url
from agents.cleaner import clean_text
from agents.synthesizer import synthesize
from rich import print

TOPIC = input("Enter research topic: ")

print("[bold cyan]Planning queries...[/bold cyan]")
queries = plan_queries(TOPIC)

sources = []

for q in queries:
    print(f"[yellow]Searching:[/yellow] {q}")
    results = web_search(q)

    for r in results[:2]:
        url = r["href"]
        text = scrape_url(url)
        text = clean_text(text)

        if len(text) > 300:
            sources.append({
                "url": url,
                "content": text
            })

print("[bold green]Synthesizing research...[/bold green]")
report = synthesize(TOPIC, sources)

with open("outputs/report.md", "w") as f:
    f.write(report)

print("[bold green]Done! Saved to outputs/report.md[/bold green]")