import yfinance as yf

def search_stock(query: str) -> list:
    """Search Indian stocks by company name"""
    ticker = yf.Search(query)
    results = ticker.quotes
    indian = [
        {
            "symbol": r.get("symbol"),
            "name": r.get("longname") or r.get("shortname"),
            "exchange": r.get("exchange"),
            "type": r.get("quoteType"),
        }
        for r in results
        if r.get("exchange") in ("NSI", "BSE")
    ]
    return indian[:5]