from pathlib import Path

import pandas as pd
from fcsparser import parse


def load_fcs_file(file_path: str | Path) -> pd.DataFrame:
    if not Path(file_path).exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    _, data = parse(str(file_path), reformat_meta=True)
    return data
