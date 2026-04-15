import subprocess
import sys
from pathlib import Path

import click

from cyrano.services.summarize_fcs import extract_well, summarize_fcs


@click.group(invoke_without_command=True)
@click.pass_context
def main(ctx: click.Context) -> None:
    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())


@main.command()
@click.argument("fcs_file", type=click.Path(exists=True, path_type=Path))
def explore(fcs_file: Path) -> None:
    well = extract_well(fcs_file.name)
    if well:
        click.echo(f"Well: {well}")
    info = summarize_fcs(fcs_file)
    click.echo(f"Number of events: {info.event_count}")
    click.echo(f"Channels: {', '.join(info.channels)}")
    click.echo(f"Signal types: {', '.join(info.signal_types)}")


@main.command()
def gui() -> None:
    app_path = Path(__file__).parent / "app.py"
    subprocess.run(
        [sys.executable, "-m", "streamlit", "run", str(app_path)], check=True
    )
