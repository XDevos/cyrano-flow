from pathlib import Path

import click

from cyrano.services.summarize_fcs import extract_well, summarize_fcs


@click.command()
@click.argument("fcs_file_1", type=click.Path(exists=True, path_type=Path))
@click.argument("fcs_file_2", type=click.Path(exists=True, path_type=Path))
def compare(fcs_file_1: Path, fcs_file_2: Path) -> None:
    well_1 = extract_well(fcs_file_1.name) or "—"
    well_2 = extract_well(fcs_file_2.name) or "—"
    info_1 = summarize_fcs(fcs_file_1)
    info_2 = summarize_fcs(fcs_file_2)

    label_w = max(
        len("Property"),
        len("Well"),
        len("Events"),
        len("Channels"),
        len("Signal types"),
    )
    col_w = max(
        len("File 1"),
        len("File 2"),
        len(well_1),
        len(well_2),
        len(str(info_1.event_count)),
        len(str(info_2.event_count)),
        len(", ".join(info_1.channels)),
        len(", ".join(info_2.channels)),
        len(", ".join(info_1.signal_types)),
        len(", ".join(info_2.signal_types)),
    )

    def row(label: str, v1: str, v2: str) -> str:
        return f"{label:<{label_w}}  {v1:<{col_w}}  {v2}"

    click.echo(row("Property", "File 1", "File 2"))
    click.echo(row("-" * label_w, "-" * col_w, "-" * col_w))
    click.echo(row("Well", well_1, well_2))
    click.echo(row("Events", str(info_1.event_count), str(info_2.event_count)))
    click.echo(row("Channels", ", ".join(info_1.channels), ", ".join(info_2.channels)))
    click.echo(
        row(
            "Signal types",
            ", ".join(info_1.signal_types),
            ", ".join(info_2.signal_types),
        )
    )
