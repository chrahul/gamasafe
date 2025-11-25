
"""
alerts.py
-------------------------
Handles Streamlit alert visuals.

TODO:
- Add color-coded risk alerts
- Add adjustment alerts
"""

import streamlit as st

def show_suggestion_alerts(suggestions: list):
    """
    Shows GamaSafe model suggestions in a bullet list.
    """
    if not suggestions:
        st.info("No suggestions at the moment.")
        return
    
    st.success("### Recommendations:")
    for suggestion in suggestions:
        st.write(f"- {suggestion}")


def show_risk_alert(level: str):
    """
    Shows color-coded alert message based on risk level.

    level options:
    - 'safe'
    - 'watch'
    - 'danger'
    """
    if level == "safe":
        st.success("Portfolio is SAFE.")
    elif level == "watch":
        st.warning("Market in WATCH zone – adjust carefully.")
    elif level == "danger":
        st.error("DANGER zone! Immediate action required.")
