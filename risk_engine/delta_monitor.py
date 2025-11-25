
"""
delta_monitor.py
--------------------
Calculates and monitors net delta exposure for the portfolio.

This helps you understand whether your book is:
- Delta neutral
- Call-heavy (short calls dominating)
- Put-heavy (short puts dominating)

TODO:
- Integrate with real option chain + position book
- Add thresholds for safe / warning / danger zones
"""

import pandas as pd

def calculate_net_delta(positions: pd.DataFrame, option_chain: pd.DataFrame) -> float:
    """
    Calculates net portfolio delta.

    Parameters:
    - positions: DataFrame with columns [symbol, strike, type, qty, side]
    - option_chain: DataFrame with Greek column 'delta'

    Returns:
    - net_delta: float
    """
    # TODO:
    # 1. Merge positions with option_chain on [strike, type]
    # 2. Multiply each position qty by its delta
    # 3. Sum to get net delta

    net_delta = 0.0
    return net_delta


def get_delta_status(net_delta: float, threshold: float = 50.0) -> str:
    """
    Returns a human-readable interpretation of net delta.

    Example outputs:
    - 'neutral'
    - 'call_side_risk'
    - 'put_side_risk'

    threshold: absolute delta above which we flag risk.
    """
    # TODO: tune threshold based on your comfort
    if abs(net_delta) < threshold:
        return "neutral"
    elif net_delta > 0:
        return "call_side_risk"
    else:
        return "put_side_risk"
