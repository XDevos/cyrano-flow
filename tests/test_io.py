from cyrano.io import load_fcs_file


def test_load_fcs_file_success(sample_fcs_path):
    dataframe = load_fcs_file(sample_fcs_path)

    assert dataframe.shape == (5, 5)
    assert "FSC-A" in dataframe.columns
    assert "FSC-H" in dataframe.columns
    assert "BL1-H" in dataframe.columns
    assert "BL1-W" not in dataframe.columns


def test_load_fcs_file_nonexistent():
    try:
        load_fcs_file("nonexistent_file.fcs")
    except FileNotFoundError:
        pass
    else:
        assert False, "Expected FileNotFoundError was not raised"


def test_load_fcs_file_invalid_format(tmp_path):
    invalid_file = tmp_path / "invalid.fcs"
    invalid_file.write_text("This is not a valid FCS file.")

    try:
        load_fcs_file(invalid_file)
    except Exception:
        pass
    else:
        assert False, "Expected an exception for invalid FCS format was not raised"
