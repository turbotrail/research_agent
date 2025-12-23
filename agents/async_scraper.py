import aiohttp
import trafilatura
import asyncio

async def fetch(session, url):
    try:
        async with session.get(url, timeout=15) as resp:
            html = await resp.text()
            text = trafilatura.extract(html)
            return url, text
    except Exception:
        return url, ""

async def scrape_all(urls, concurrency=5):
    connector = aiohttp.TCPConnector(limit=concurrency)
    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = [fetch(session, u) for u in urls]
        return await asyncio.gather(*tasks)