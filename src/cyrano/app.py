from pathlib import Path
from tempfile import NamedTemporaryFile

import streamlit as st

from cyrano.services.summarize_fcs import summarize_fcs

st.set_page_config(page_title="Cyrano", page_icon="👃", layout="centered")
st.title("CYRANO — Flow Cytometry Analysis Orchestrator")

uploaded = st.file_uploader("Upload an FCS file", type=["fcs"])

if uploaded is not None:
    with NamedTemporaryFile(suffix=".fcs", delete=False) as tmp:
        tmp.write(uploaded.read())
        tmp_path = Path(tmp.name)

    info = summarize_fcs(tmp_path)

    st.table(
        {
            "Property": ["Number of events", "Channels", "Signal types"],
            "Value": [
                str(info.event_count),
                ", ".join(info.channels),
                ", ".join(info.signal_types),
            ],
        }
    )

    tmp_path.unlink()
