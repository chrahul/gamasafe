
"""
charts.py
-------------------------
Chart helper functions for GamaSafe dashboard.

TODO:
- Add OI bar charts
- Add IV trend
- Add delta/gamma charts
"""

import streamlit as st
import matplotlib.pyplot as plt

def plot_placeholder_chart():
    """
    Temporary placeholder chart for early development.
    """
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3], [2, 3, 2])
    ax.set_title("Placeholder Chart")
    st.pyplot(fig)
