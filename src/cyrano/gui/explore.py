from pathlib import Path
from tempfile import NamedTemporaryFile

import streamlit as st

from cyrano.services.summarize_fcs import extract_well, summarize_fcs


def render_explore() -> None:
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
