from fastmcp import FastMCP
from tools.live import get_stock_quote
from tools.history import get_stock_history
from tools.search import search_stock
from tools.market import get_market_status
import json

mcp = FastMCP("indian-stock-market")


@mcp.tool()
def stock_live(symbol: str) -> str:
    """
    Get live stock price for an Indian stock.
    Use .NS for NSE (e.g. RELIANCE.NS) and .BO for BSE (e.g. RELIANCE.BO)
    """
    result = get_stock_quote(symbol)
    return json.dumps(result, indent=2)


@mcp.tool()
def stock_history(symbol: str, period: str = "1mo") -> str:
    """
    Get historical price data for an Indian stock.
    Period options: 1mo, 3mo, 6mo, 1y
    """
    result = get_stock_history(symbol, period)
    return json.dumps(result, indent=2)


@mcp.tool()
def search_indian_stock(query: str) -> str:
    """
    Search for Indian stocks by company name.
    Example: 'Reliance', 'Infosys', 'HDFC Bank'
    """
    result = search_stock(query)
    return json.dumps(result, indent=2)


@mcp.tool()
def market_status() -> str:
    """
    Check if NSE/BSE market is currently open or closed.
    """
    result = get_market_status()
    return json.dumps(result, indent=2)


if __name__ == "__main__":
    mcp.run()