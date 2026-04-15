import re
from dataclasses import dataclass
from pathlib import Path


from cyrano.io import load_fcs_file

SIGNAL_TYPES = {
    "A": "A (Area)",
    "H": "H (Height)",
    "W": "W (Width)",
}

_WELL_PATTERN = re.compile(r"_([A-H](?:1[0-2]|[1-9]))\.fcs$", re.IGNORECASE)


@dataclass(frozen=True)
class FCSInfo:
    event_count: int
    channels: list[str]
    signal_types: list[str]


def _extract_channels_and_types(
    columns: list[str],
) -> tuple[list[str], list[str]]:
    seen_channels: list[str] = []
    seen_suffixes: list[str] = []
    for col in columns:
        parts = col.rsplit("-", 1)
        if len(parts) == 2 and len(parts[1]) == 1:
            base, suffix = parts
            if base not in seen_channels:
                seen_channels.append(base)
            if suffix in SIGNAL_TYPES and SIGNAL_TYPES[suffix] not in seen_suffixes:
                seen_suffixes.append(SIGNAL_TYPES[suffix])
        else:
            if col not in seen_channels:
                seen_channels.append(col)
    return seen_channels, seen_suffixes


def extract_well(filename: str) -> str | None:
    """Extract the well identifier (e.g. 'A4') from an FCS filename.

    Expects the well to appear as the last segment before .fcs,
    separated by an underscore: '..._A4.fcs' -> 'A4'.
    Returns None if the filename doesn't match this convention.
    """
    match = _WELL_PATTERN.search(filename)
    return match.group(1).upper() if match else None


def summarize_fcs(source: Path) -> FCSInfo:
    """Summarize the content of an FCS file (events, channels, signal types)."""
    dataframe = load_fcs_file(source)
    columns = [str(c) for c in dataframe.columns]
    channels, signal_types = _extract_channels_and_types(columns)
    return FCSInfo(
        event_count=len(dataframe),
        channels=channels,
        signal_types=signal_types,
    )
