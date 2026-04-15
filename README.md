# CYRANO — Flow Cytometry Analysis Orchestrator

CLI and GUI tool for exploring, comparing, and analyzing flow cytometry (FCS) files.

## Installation

```bash
uv sync
```

## Usage

### CLI

```bash
# Show available commands
uv run cyrano

# Explore a single FCS file (events, channels, signal types, well)
uv run cyrano explore path/to/file.fcs

# Compare two FCS files side by side
uv run cyrano compare file1.fcs file2.fcs

# Analyze a 96-well plate (generates plate_heatmap.png in current directory)
uv run cyrano analyze path/to/dir_with_fcs/

# Launch the Streamlit GUI
uv run cyrano gui
```

### GUI (Streamlit)

The graphical interface provides three tabs:

- **Explore** — Upload a single FCS file to view its summary
- **Compare** — Upload two FCS files to compare them side by side
- **Analyze** — Upload FCS files from a 96-well plate to generate a heatmap