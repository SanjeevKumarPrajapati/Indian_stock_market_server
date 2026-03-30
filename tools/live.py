import yfinance as yf

def get_stock_quote(symbol: str) -> dict:
    """Get live stock price for an Indian stock (e.g. RELIANCE.NS)"""
    ticker = yf.Ticker(symbol)
    info = ticker.info
    return {
        "symbol": symbol,
        "name": info.get("longName", "N/A"),
        "price": info.get("currentPrice", "N/A"),
        "change": info.get("regularMarketChange", "N/A"),
        "change_percent": round(info.get("regularMarketChangePercent", 0), 2),
        "day_high": info.get("dayHigh", "N/A"),
        "day_low": info.get("dayLow", "N/A"),
        "volume": info.get("volume", "N/A"),
        "market_cap": info.get("marketCap", "N/A"),
    }