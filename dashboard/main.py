
"""
main.py
-------------------------
Entry point for the GamaSafe 1.0 dashboard.
This Streamlit app acts as your trading control panel.

TODO:
- Connect to data_engine
- Connect to strategy modules
- Connect to risk modules
"""

import streamlit as st
from datetime import datetime

from utils.config_loader import load_config
from dashboard.charts import *
from dashboard.tables import *
from dashboard.alerts import *

st.set_page_config(
    page_title="GamaSafe 1.0",
    layout="wide"
)

# Load config
config = load_config()

# --- SIDEBAR ---
st.sidebar.title("GamaSafe 1.0")
st.sidebar.subheader("Options Selling Control Dashboard")

st.sidebar.write("**Strategy Settings**")
st.sidebar.write(f"Entry Window: {config['entry']['entry_time_start']} - {config['entry']['entry_time_end']}")
st.sidebar.write(f"Delta Range: {config['strikes']['target_delta_low']} - {config['strikes']['target_delta_high']}")
st.sidebar.write(f"Max Weekly Loss: ₹{config['risk']['max_weekly_loss']}")

st.sidebar.markdown("---")
st.sidebar.write("**Mode**")
mode = st.sidebar.radio("Choose Mode:", ["Live", "Simulation"], index=1)

st.sidebar.markdown("---")
st.sidebar.wri
