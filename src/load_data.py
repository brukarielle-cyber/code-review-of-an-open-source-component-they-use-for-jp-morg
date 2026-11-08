"""Loads the project's data: the public dataset below, or the labeled synthetic sample."""
from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
# The public dataset from the brief. Replace it if you choose another public source, and say so in the README.
DATA_URL = None
SAMPLE = DATA_DIR / "synthetic_sample.csv"


def load_data(use_sample: bool = False) -> pd.DataFrame:
    """Returns the dataset as a DataFrame. Falls back to the synthetic sample when offline."""
    if not use_sample and DATA_URL and DATA_URL.endswith(".csv"):
        try:
            return pd.read_csv(DATA_URL)
        except Exception:  # noqa: BLE001 - offline or moved: use the sample and say so
            print("Could not download the dataset; using the synthetic sample.")
    return pd.read_csv(SAMPLE)
