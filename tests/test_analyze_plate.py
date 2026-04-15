import matplotlib.figure

from cyrano.services.analyze_plate import plot_plate_heatmap, scan_plate


def test_scan_plate(sample_plate_dir):
    well_counts = scan_plate(sample_plate_dir)

    assert len(well_counts) == 4
    assert set(well_counts.keys()) == {"A1", "A2", "B1", "B2"}
    assert all(count > 0 for count in well_counts.values())


def test_plot_plate_heatmap(sample_plate_dir):
    well_counts = scan_plate(sample_plate_dir)
    fig = plot_plate_heatmap(well_counts)

    assert isinstance(fig, matplotlib.figure.Figure)
