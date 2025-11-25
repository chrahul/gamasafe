
"""
helpers.py
-----------------------
General-purpose utility functions used across the project.

TODO:
- Add logging utilities
- Add error handling helpers
"""

import pandas as pd
import numpy as np

def round_to_nearest(x: float, base: int = 50) -> float:
    """
    Rounds number to nearest base.
    Example:
    round_to_nearest(17834, 50) -> 17850
    """
    return base * round(x / base)


def format_rupees(value: float) -> str:
    """
    Formats numeric value into INR currency string.
    """
    return f"₹{value:,.2f}"


def safe_get(df: pd.DataFrame, col: str, default=None):
    """
    Safe column getter for DataFrame.
    """
    if col in df.columns:
        return df[col]
    return default


def log(message: str):
    """
    Simple console logger.
    TODO: replace with file-based logger
    """
    print(f"[GAMASAFE] {message}")
