from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, List
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

# Initialize FastAPI app
app = FastAPI()

# Enable CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define request model
class StockRequest(BaseModel):
    stock_prices: Dict[str, List[float]]
    total_investment: float = 10000

# Placeholder stock analysis function
def analyze_stocks(stock_prices: Dict[str, List[float]], total_investment: float):
    results = {}
    for ticker, prices in stock_prices.items():
        if len(prices) != 7:
            raise HTTPException(status_code=400, detail=f"Invalid data for {ticker}. Expected 7 price values.")
        
        predicted_price = sum(prices[-3:]) / 3 * 1.01  # Simple moving average prediction
        decision = "BUY" if predicted_price > prices[-1] else "SELL"
        
        results[ticker] = {
            "Decision": decision,
            "Predicted Price": round(predicted_price, 2),
            "Current Price": prices[-1],
            "Allocation": f"${round(total_investment / len(stock_prices), 2)}"
        }
    return results

# Define API route
@app.post("/analyze")
def analyze(request: StockRequest):
    return analyze_stocks(request.stock_prices, request.total_investment)

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/")
def home():
    return {"message": "Stock Analysis API. Send a POST request to /analyze with stock price data."}

# Run with Uvicorn (for development only)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
