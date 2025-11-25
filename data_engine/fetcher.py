
"""
fetcher.py
----------------
Responsible for fetching live or test option chain, spot price,
and other required market data.

TODO:
- Integrate KiteConnect API
- Add retry logic
- Add error handling & caching
"""

import pandas as pd
import requests

def get_spot(symbol: str) -> float:
    """
    Returns current spot price for the given symbol.
    Placeholder implementation.
    """
    # TODO: Replace with KiteConnect or broker API
    return 0.0


def get_option_chain(symbol: str, expiry: str) -> pd.DataFrame:
    """
    Returns option chain for symbol & expiry.
    Placeholder returns empty DataFrame.
    """
    # TODO: Replace with real API data
    return pd.DataFrame()


def get_test_chain(filepath: str) -> pd.DataFrame:
    """
    Loads option chain from CSV for simulation/testing.
    """
    return pd.read_csv(filepath)
