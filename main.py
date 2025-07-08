
from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI()

@app.get("/")
def root():
    return {"message": "MOEX Price API is running"}

@app.get("/price")
async def get_price(ticker: str):
    url = f"https://iss.moex.com/iss/engines/stock/markets/shares/securities/{ticker}.json"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code != 200:
            raise HTTPException(status_code=404, detail="Ticker not found")
        data = response.json()
        try:
            price = data["marketdata"]["data"][0][12]  # LAST
            return {"ticker": ticker.upper(), "price": price}
        except (IndexError, TypeError):
            raise HTTPException(status_code=404, detail="Price not found")
