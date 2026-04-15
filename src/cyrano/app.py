from pathlib import Path
from tempfile import NamedTemporaryFile

import streamlit as st

from cyrano.services.summarize_fcs import extract_well, summarize_fcs

st.set_page_config(page_title="Cyrano", page_icon="👃", layout="centered")
st.title("👃 CYRANO — Flow Cytometry Analysis Orchestrator")

tab_explore, tab_compare, tab_analyze = st.tabs(["Explore", "Compare", "Analyze"])

with tab_explore:
    uploaded = st.file_uploader("Upload an FCS file", type=["fcs"], key="explore")

    if uploaded is not None:
        with NamedTemporaryFile(suffix=".fcs", delete=False) as tmp:
            tmp.write(uploaded.read())
            tmp_path = Path(tmp.name)

        well = extract_well(uploaded.name)
        info = summarize_fcs(tmp_path)
        tmp_path.unlink()

        st.table(
            {
                "Property": ["Well", "Number of events", "Channels", "Signal types"],
                "Value": [
                    str(well),
                    str(info.event_count),
                    ", ".join(info.channels),
                    ", ".join(info.signal_types),
                ],
            }
        )

with tab_compare:
    col1, col2 = st.columns(2)
    with col1:
        st.file_uploader("Upload FCS file 1", type=["fcs"], key="compare_1")
    with col2:
        st.file_uploader("Upload FCS file 2", type=["fcs"], key="compare_2")
    st.info("Comparison coming soon")

with tab_analyze:
    st.info("Batch analysis coming soon")
