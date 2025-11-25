
"""
datetime_tools.py
-----------------------
Utility functions for handling date and time operations,
including entry windows, expiry detection, and formatting.

TODO:
- Add timezone support if needed
"""

from datetime import datetime, time

def is_within_time_window(now: datetime,
                          start: str,
                          end: str) -> bool:
    """
    Checks if current time is between start and end.

    Parameters:
    - now: datetime object (current time)
    - start, end: "HH:MM" string format

    Example:
    is_within_time_window(now, "10:45", "11:15")
    """
    try:
        start_time = time.fromisoformat(start)
        end_time = time.fromisoformat(end)
        return start_time <= now.time() <= end_time
    except Exception as e:
        print(f"[ERROR] time window check: {e}")
        return False


def get_today_date_str() -> str:
    """
    Returns today's date in YYYY-MM-DD format.
    """
    return datetime.today().strftime("%Y-%m-%d")


def get_next_expiry() -> str:
    """
    Returns next Thursday date as 'YYYY-MM-DD'.

    NOTE: Placeholder logic for now.
    TODO: Replace with accurate expiry calendar including holidays.
    """
    # TODO: implement correct expiry logic
    return "2025-01-01"
