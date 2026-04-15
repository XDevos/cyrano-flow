from click.testing import CliRunner

from cyrano.cli import main


def test_main_with_valid_fcs_file(sample_fcs_path):
    runner = CliRunner()
    result = runner.invoke(main, [str(sample_fcs_path)])

    assert result.exit_code == 0


def test_main_with_no_arguments():
    runner = CliRunner()
    result = runner.invoke(main, [])

    assert result.exit_code != 0


def test_main_with_too_many_arguments(sample_fcs_path):
    runner = CliRunner()
    result = runner.invoke(main, [str(sample_fcs_path), "extra_arg"])

    assert result.exit_code != 0
