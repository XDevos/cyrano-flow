from pathlib import Path

import click

from cyrano.services.summarize_fcs import extract_well, summarize_fcs


@click.command()
@click.argument("fcs_file", type=click.Path(exists=True, path_type=Path))
def explore(fcs_file: Path) -> None:
    well = extract_well(fcs_file.name)
    if well:
        click.echo(f"Well: {well}")
    info = summarize_fcs(fcs_file)
    click.echo(f"Number of events: {info.event_count}")
    click.echo(f"Channels: {', '.join(info.channels)}")
    click.echo(f"Signal types: {', '.join(info.signal_types)}")
