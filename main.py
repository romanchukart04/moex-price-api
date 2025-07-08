from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/price/{ticker}")
def get_price(ticker: str):
    url = f"https://iss.moex.com/iss/engines/stock/markets/shares/securities/{ticker}.json"
    response = requests.get(url)
    data = response.json()

    try:
        price = data["marketdata"]["data"][0][12]
        return {"ticker": ticker, "price": price}
    except:
        return {"error": "Failed to fetch price or ticker not found"}
