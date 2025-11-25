
"""
gamma_monitor.py
--------------------
Monitors gamma risk on the portfolio.

Gamma risk becomes dangerous when:
- Spot is near short strikes
- Gamma is high
- Time to expiry is low

TODO:
- Use actual gamma from option_chain
- Define robust thresholds based on backtests
"""

import pandas as pd

def calculate_net_gamma(positions: pd.DataFrame, option_chain: pd.DataFrame) -> float:
    """
    Calculates net portfolio gamma.

    Parameters:
    - positions: DataFrame with columns [symbol, strike, type, qty, side]
    - option_chain: DataFrame with Greek column 'gamma'

    Returns:
    - net_gamma: float
    """
    # TODO:
    # 1. Merge positions with option_chain on [strike, type]
    # 2. Multiply each position qty by its gamma
    # 3. Sum to get net gamma

    net_gamma = 0.0
    return net_gamma


def get_gamma_status(net_gamma: float, spot: float, short_call_strike: float = None,
                     short_put_strike: float = None) -> str:
    """
    Returns a gamma risk label, combining distance from short strikes & gamma.

    Possible outputs:
    - 'safe'
    - 'watch'
    - 'danger'

    TODO:
    - Implement actual distance + gamma logic
    """
    # Placeholder: always safe for now
    return "safe"
