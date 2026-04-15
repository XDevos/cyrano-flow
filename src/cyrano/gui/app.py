import streamlit as st

from cyrano.gui.analyze import render_analyze
from cyrano.gui.compare import render_compare
from cyrano.gui.explore import render_explore

st.set_page_config(page_title="Cyrano", page_icon="👃", layout="centered")
st.title("CYRANO — Flow Cytometry Analysis Orchestrator")

tab_explore, tab_compare, tab_analyze = st.tabs(["Explore", "Compare", "Analyze"])

with tab_explore:
    render_explore()

with tab_compare:
    render_compare()

with tab_analyze:
    render_analyze()
