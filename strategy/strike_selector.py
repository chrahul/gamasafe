"""
strike_selector.py
--------------------
Responsible for selecting strikes based on delta range (12–15),
option chain, IV conditions and your SOP rules.

TODO:
- Implement real delta filtering logic
- Include IV / OI filters
"""

import pandas as pd

def select_short_strikes(option_chain: pd.DataFrame, config: dict) -> dict:
    """
    Returns dict:
    {
        "short_call": strike,
        "short_put": strike
    }
    """
    # TODO: filter rows by delta between target_delta_low & high
    return {
        "short_call": None,
        "short_put": None
    }


def select_hedge_strikes(option_chain: pd.DataFrame, short_legs: dict, config: dict) -> dict:
    """
    Selects hedge strikes approx 400–600 points away
    or with premium <= 15
    """
    # TODO: implement hedge logic
    return {
        "hedge_call": None,
        "hedge_put": None
    }

