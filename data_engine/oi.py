
"""
oi.py
----------------
Handles Open Interest logic, OI summaries, TMJ/TMG detection.

TODO:
- Compute OI change
- Identify strongest CE/PE levels
- Implement TMJ/TMG logic
"""

import pandas as pd

def get_oi_summary(option_chain: pd.DataFrame) -> dict:
    """
    Returns summary of OI structure including:
    - Highest CE OI
    - Highest PE OI
    - PCR
    """
    summary = {
        "highest_ce_oi": None,
        "highest_pe_oi": None,
        "pcr": None
    }
    # TODO: implement actual OI processing
    return summary
