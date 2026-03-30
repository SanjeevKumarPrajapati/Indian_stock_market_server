from datetime import datetime
import pytz

def get_market_status() -> dict:
    """Check if NSE/BSE market is currently open"""
    ist = pytz.timezone("Asia/Kolkata")
    now = datetime.now(ist)
    hour, minute, weekday = now.hour, now.minute, now.weekday()

    is_weekday = weekday < 5  # Mon–Fri
    market_open = (hour > 9 or (hour == 9 and minute >= 15))
    market_close = (hour < 15 or (hour == 15 and minute <= 30))
    is_open = is_weekday and market_open and market_close

    return {
        "status": "🟢 OPEN" if is_open else "🔴 CLOSED",
        "current_IST": now.strftime("%I:%M %p"),
        "day": now.strftime("%A"),
        "market_hours": "9:15 AM – 3:30 PM IST (Mon–Fri)",
    }