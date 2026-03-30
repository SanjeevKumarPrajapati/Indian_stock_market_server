import yfinance as yf

def get_stock_history(symbol: str, period: str) -> list:
    """Get historical price data. Period: 1mo, 3mo, 6mo, 1y"""
    ticker = yf.Ticker(symbol)
    hist = ticker.history(period=period)
    result = []
    for date, row in hist.tail(10).iterrows():
        result.append({
            "date": str(date.date()),
            "open": round(row["Open"], 2),
            "high": round(row["High"], 2),
            "low": round(row["Low"], 2),
            "close": round(row["Close"], 2),
            "volume": int(row["Volume"]),
        })
    return result