from pathlib import Path

import click

from cyrano.services.analyze_plate import plot_plate_heatmap, scan_plate


@click.command()
@click.argument(
    "fcs_dir", type=click.Path(exists=True, file_okay=False, path_type=Path)
)
def analyze(fcs_dir: Path) -> None:
    """Analyze a directory of FCS files and generate a 96-well plate heatmap."""
    well_counts = scan_plate(fcs_dir)
    if not well_counts:
        click.echo("No FCS files with valid well identifiers found.")
        return

    fig = plot_plate_heatmap(well_counts)
    output = Path("plate_heatmap.png")
    fig.savefig(output, dpi=150)
    click.echo(f"Heatmap saved to {output}")
