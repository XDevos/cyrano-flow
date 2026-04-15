from pathlib import Path

import matplotlib.figure
import matplotlib.pyplot as plt

from cyrano.services.summarize_fcs import extract_well, summarize_fcs

ROWS = list("ABCDEFGH")
COLS = list(range(1, 13))


def scan_plate(directory: Path) -> dict[str, int]:
    """Scan a directory for FCS files and return {well_id: event_count}."""
    well_counts: dict[str, int] = {}
    for fcs_file in sorted(directory.glob("*.fcs")):
        well = extract_well(fcs_file.name)
        if well is not None:
            info = summarize_fcs(fcs_file)
            well_counts[well] = info.event_count
    return well_counts


def plot_plate_heatmap(well_counts: dict[str, int]) -> matplotlib.figure.Figure:
    """Build a 96-well plate heatmap with round wells colored by event count."""
    fig, ax = plt.subplots(figsize=(10, 6))

    xs, ys, values = [], [], []
    for well, count in well_counts.items():
        row_letter = well[0].upper()
        col_number = int(well[1:])
        if row_letter in ROWS and 1 <= col_number <= 12:
            xs.append(col_number - 1)
            ys.append(ROWS.index(row_letter))
            values.append(count)

    # Background: empty wells as light grey circles
    for r in range(len(ROWS)):
        for c in range(len(COLS)):
            ax.scatter(
                c,
                r,
                s=500,
                color="#e0e0e0",
                edgecolors="#cccccc",
                linewidths=0.5,
                zorder=1,
            )

    # Filled wells
    if values:
        sc = ax.scatter(
            xs,
            ys,
            s=500,
            c=values,
            cmap="YlOrRd",
            edgecolors="#888888",
            linewidths=0.5,
            zorder=2,
        )
        cbar = fig.colorbar(sc, ax=ax, shrink=0.8, pad=0.02)
        cbar.set_label("Event count")

    ax.set_xticks(range(len(COLS)))
    ax.set_xticklabels(COLS)
    ax.set_yticks(range(len(ROWS)))
    ax.set_yticklabels(ROWS)
    ax.invert_yaxis()
    ax.set_xlim(-0.7, 11.7)
    ax.set_ylim(7.7, -0.7)
    ax.set_aspect("equal")
    ax.set_title("96-Well Plate — Event Count")
    fig.tight_layout()

    return fig
