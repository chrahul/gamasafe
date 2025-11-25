
"""
exit_rules.py
---------------------
Handles:
- End-of-week exit (Thu 3:20 PM)
- Combined premium < 15% exit
- Weekly loss limit exit
"""

from datetime import datetime

def should_exit_all(current_time: datetime, combined_premium: float, config: dict) -> bool:
    """
    Returns True if trade should be closed completely.
    """
    # TODO: implement logic
    return False


def should_reduce_size(weekly_pnl: float, config: dict) -> bool:
    """
    Returns True if lot size should be reduced after losses.
    """
    # TODO: implement logic
    return False
