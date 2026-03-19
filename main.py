from fastapi import FastAPI, Depends
from data_collector import collect_data
from ai_analyzer import analyze_data
from auth import verify_api_key
from rate_limiter import check_rate_limit
from fastapi import Request, HTTPException

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Trade Opportunities API running"}

@app.get("/analyze/{sector}")
async def analyze_sector(
    sector: str,
    request: Request,
    api_key: str = Depends(verify_api_key)
):
    client_ip = request.client.host

    if not check_rate_limit(client_ip):
        raise HTTPException(status_code=429, detail="Too many requests")

    data = await collect_data(sector)
    report = await analyze_data(sector, data)

    return {"report": report}