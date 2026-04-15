from cyrano.services.summarize_fcs import summarize_fcs


def test_summarize_fcs_from_fcs_file(sample_fcs_path):
    info = summarize_fcs(sample_fcs_path)

    assert info.event_count == 5
    assert "FSC" in info.channels
    assert "SSC" in info.channels
    assert "BL1" in info.channels
    assert "A (Area)" in info.signal_types
    assert "H (Height)" in info.signal_types
