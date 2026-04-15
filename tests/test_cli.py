from click.testing import CliRunner

from cyrano.cli import main


def test_explore_with_valid_fcs_file(sample_fcs_path):
    runner = CliRunner()
    result = runner.invoke(main.main, ["explore", str(sample_fcs_path)])

    assert result.exit_code == 0


def test_explore_with_no_arguments():
    runner = CliRunner()
    result = runner.invoke(main.main, ["explore"])

    assert result.exit_code != 0


def test_compare_with_two_valid_fcs_files(sample_fcs_path):
    runner = CliRunner()
    result = runner.invoke(
        main.main, ["compare", str(sample_fcs_path), str(sample_fcs_path)]
    )

    assert result.exit_code == 0
    assert "File 1" in result.output
    assert "File 2" in result.output


def test_compare_with_no_arguments():
    runner = CliRunner()
    result = runner.invoke(main.main, ["compare"])

    assert result.exit_code != 0


def test_compare_with_one_argument(sample_fcs_path):
    runner = CliRunner()
    result = runner.invoke(main.main, ["compare", str(sample_fcs_path)])

    assert result.exit_code != 0


def test_main_with_no_command():
    runner = CliRunner()
    result = runner.invoke(main.main, [])

    assert result.exit_code == 0
    assert "explore" in result.output


def test_analyze_with_valid_directory(sample_plate_dir, tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    runner = CliRunner()
    result = runner.invoke(main.main, ["analyze", str(sample_plate_dir)])

    assert result.exit_code == 0
    assert "Heatmap saved" in result.output
    assert (tmp_path / "plate_heatmap.png").exists()


def test_analyze_with_no_arguments():
    runner = CliRunner()
    result = runner.invoke(main.main, ["analyze"])

    assert result.exit_code != 0
