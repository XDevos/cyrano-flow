from pathlib import Path

import click

from cyrano.services.summarize_fcs import summarize_fcs


def explore_fcs_file(fcs_file: Path) -> None:
    info = summarize_fcs(fcs_file)
    print(f"Number of events: {info.event_count}")
    print(f"Scatter channels: {', '.join(info.channels)}")
    print(f"Signal types: {', '.join(info.signal_types)}")


@click.command()
@click.argument("fcs_file", type=click.Path(exists=True, path_type=Path))
def main(fcs_file: Path) -> None:
    explore_fcs_file(fcs_file)
