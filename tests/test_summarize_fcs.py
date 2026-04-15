from cyrano.services.summarize_fcs import extract_well, summarize_fcs


def test_summarize_fcs_from_fcs_file(sample_fcs_path):
    info = summarize_fcs(sample_fcs_path)

    assert info.event_count == 5
    assert "FSC" in info.channels
    assert "SSC" in info.channels
    assert "BL1" in info.channels
    assert "A (Area)" in info.signal_types
    assert "H (Height)" in info.signal_types


def test_extract_well_from_filename():
    assert extract_well("PB-10 LB_Experiment_LB_A4.fcs") == "A4"
    assert extract_well("Experiment_H12.fcs") == "H12"
    assert extract_well("random_file.fcs") is None
    assert extract_well("no_well_here.csv") is None
