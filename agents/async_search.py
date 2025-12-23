from ddgs import DDGS

async def search_queries(queries, max_results=5):
    results = []
    with DDGS() as ddgs:
        for q in queries:
            results.extend(ddgs.text(q, max_results=max_results))
    return results