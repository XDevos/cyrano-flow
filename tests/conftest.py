from pathlib import Path

import numpy as np
import pytest
from fcswrite import write_fcs


@pytest.fixture
def sample_fcs_path(tmp_path: Path) -> Path:
    file_path = tmp_path / "P10 L_Experiment_4L_A4.fcs"
    channel_names = ["FSC-A", "FSC-H", "SSC-A", "SSC-H", "BL1-H"]
    data = np.array(
        [
            [100.0, 200.0, 50.0, 150.0, 10.0],
            [110.0, 210.0, 55.0, 155.0, 11.0],
            [120.0, 220.0, 60.0, 160.0, 12.0],
            [130.0, 230.0, 65.0, 165.0, 13.0],
            [140.0, 240.0, 70.0, 170.0, 14.0],
        ]
    )
    write_fcs(file_path, channel_names.copy(), data, compat_chn_names=False)
    return file_path
