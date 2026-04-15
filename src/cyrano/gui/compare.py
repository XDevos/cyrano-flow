from pathlib import Path
from tempfile import NamedTemporaryFile

import streamlit as st

from cyrano.services.summarize_fcs import extract_well, summarize_fcs


def render_compare() -> None:
    col1, col2 = st.columns(2)
    with col1:
        uploaded_1 = st.file_uploader(
            "Upload FCS file 1", type=["fcs"], key="compare_1"
        )
    with col2:
        uploaded_2 = st.file_uploader(
            "Upload FCS file 2", type=["fcs"], key="compare_2"
        )

    if uploaded_1 is not None and uploaded_2 is not None:
        summaries = []
        for uploaded in (uploaded_1, uploaded_2):
            with NamedTemporaryFile(suffix=".fcs", delete=False) as tmp:
                tmp.write(uploaded.read())
                tmp_path = Path(tmp.name)
            well = extract_well(uploaded.name)
            info = summarize_fcs(tmp_path)
            tmp_path.unlink()
            summaries.append((well, info))

        (well_1, info_1), (well_2, info_2) = summaries

        st.table(
            {
                "Property": ["Well", "Number of events", "Channels", "Signal types"],
                "File 1": [
                    str(well_1),
                    str(info_1.event_count),
                    ", ".join(info_1.channels),
                    ", ".join(info_1.signal_types),
                ],
                "File 2": [
                    str(well_2),
                    str(info_2.event_count),
                    ", ".join(info_2.channels),
                    ", ".join(info_2.signal_types),
                ],
            }
        )
    else:
        st.info("Upload two FCS files to compare them")
