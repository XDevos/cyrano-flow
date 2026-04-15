from click.testing import CliRunner

from cyrano.cli import main


def test_explore_with_valid_fcs_file(sample_fcs_path):
    runner = CliRunner()
    result = runner.invoke(main, ["explore", str(sample_fcs_path)])

    assert result.exit_code == 0


def test_explore_with_no_arguments():
    runner = CliRunner()
    result = runner.invoke(main, ["explore"])

    assert result.exit_code != 0


def test_main_with_no_command():
    runner = CliRunner()
    result = runner.invoke(main, [])

    assert result.exit_code == 0
    assert "explore" in result.output
    assert "gui" in result.output
