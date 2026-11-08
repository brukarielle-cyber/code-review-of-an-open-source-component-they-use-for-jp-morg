from src.analysis import summarize
from src.load_data import load_data


def test_sample_loads():
    df = load_data(use_sample=True)
    assert len(df) > 0


def test_summary_counts_rows():
    df = load_data(use_sample=True)
    assert summarize(df)["rows"] == len(df)
