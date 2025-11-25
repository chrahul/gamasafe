
"""
risk_limits.py
--------------------
Implements portfolio-level risk limits such as:
- Max weekly loss
- Max drawdown per trade
- Position sizing rules

TODO:
- Wire this to actual P&L log
- Enforce no-trade condition once limit is hit
"""

def check_weekly_risk(weekly_realized_pnl: float, config: dict) -> bool:
    """
    Returns True if weekly loss limit is breached.

    Parameters:
    - weekly_realized_pnl: cumulative realized P&L for the week
    - config: config dict with 'risk' -> 'max_weekly_loss'

    Example:
    - max_weekly_loss = -25000
    - weekly_realized_pnl = -26000 -> returns True (limit breached)
    """
    max_weekly_loss = config.get("risk", {}).get("max_weekly_loss", 25000)
    # Loss is negative, so we compare if PnL < -max_weekly_loss
    if weekly_realized_pnl <= -abs(max_weekly_loss):
        return True
    return False


def check_position_risk(position_mtm: float, entry_premium: float, max_loss_factor: float = 2.0) -> bool:
    """
    Simple risk check per position.

    Returns True if current loss exceeds (max_loss_factor * entry_premium).

    Example:
    - entry_premium = 40
    - max_loss_factor = 2.0  -> allowed move to 80
    - if current loss > 40 (i.e. premium > 80), flag risk
    """
    # TODO: refine with actual MTM
    # Placeholder: no risk by default
    return False
