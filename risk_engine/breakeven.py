
"""
breakeven.py
--------------------
Computes breakeven levels for short strangle structures.

Typical formula (simple):
- BE_low  = spot - net_credit
- BE_high = spot + net_credit

Or based on short strikes:
- BE_low  = short_put_strike - net_credit
- BE_high = short_call_strike + net_credit

TODO:
- Support more complex structures (iron condor, ratio spreads)
"""

from typing import Tuple

def compute_strangle_breakevens(short_put_strike: float,
                                short_call_strike: float,
                                net_credit: float) -> Tuple[float, float]:
    """
    Returns (BE_low, BE_high) for a short strangle.

    Parameters:
    - short_put_strike
    - short_call_strike
    - net_credit: total premium received per unit

    Returns:
    - (BE_low, BE_high)
    """
    be_low = short_put_strike - net_credit
    be_high = short_call_strike + net_credit
    return be_low, be_high
