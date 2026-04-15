import subprocess
import sys
from pathlib import Path

import click

from cyrano.cli.analyze import analyze
from cyrano.cli.compare import compare
from cyrano.cli.explore import explore


@click.group(invoke_without_command=True)
@click.pass_context
def main(ctx: click.Context) -> None:
    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())


main.add_command(analyze)
main.add_command(explore)
main.add_command(compare)


@main.command()
def gui() -> None:
    """Launch graphical interface (Streamlit)"""
    app_path = Path(__file__).resolve().parent.parent / "gui" / "app.py"
    subprocess.run(
        [sys.executable, "-m", "streamlit", "run", str(app_path)], check=True
    )
