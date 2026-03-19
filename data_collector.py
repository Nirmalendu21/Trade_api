from duckduckgo_search import DDGS

async def collect_data(sector: str):
    query = f"India {sector} sector news"

    results = []

    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=5):
            results.append(r["body"])

    return results