from pathlib import Path
from tempfile import TemporaryDirectory

import streamlit as st

from cyrano.services.analyze_plate import plot_plate_heatmap, scan_plate


def render_analyze() -> None:
    uploaded_files = st.file_uploader(
        "Upload FCS files (96-well plate)",
        type=["fcs"],
        accept_multiple_files=True,
        key="analyze",
    )

    if not uploaded_files:
        st.info("Upload FCS files from a 96-well plate to generate a heatmap.")
        return

    with TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir)
        for uploaded in uploaded_files:
            (tmp_path / uploaded.name).write_bytes(uploaded.read())

        well_counts = scan_plate(tmp_path)

    if not well_counts:
        st.warning("No FCS files with valid well identifiers found.")
        return

    fig = plot_plate_heatmap(well_counts)
    st.pyplot(fig)
