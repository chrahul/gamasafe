
"""
tables.py
-------------------------
Table helper functions for GamaSafe dashboard.

TODO:
- Build real position tables
- Build option chain tables
"""

import streamlit as st
import pandas as pd

def show_positions_table(positions: list):
    """
    Renders a positions table in Streamlit.

    positions: list of dicts
    Example:
    [
        {"type": "CE", "strike": 24000, "qty": -50, "premium": 32},
        {"type": "PE", "strike": 23000, "qty": -50, "premium": 28}
    ]
    """
    if not positions:
        st.warning("No active positions.")
        return
    
    df = pd.DataFrame(positions)
    st.table(df)


def show_risk_table(data: dict):
    """
    Displays risk metrics like net delta, net gamma.
    """
    df = pd.DataFrame([data])
    st.table(df)
