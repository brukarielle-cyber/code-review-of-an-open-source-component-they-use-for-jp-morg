"""The analysis. Start here: load the data, answer the question in the README, save one chart."""
from src.load_data import load_data


def summarize(df):
    """A first look: rows, columns, and missing values. Replace with your analysis."""
    return {"rows": len(df), "columns": list(df.columns), "missing": int(df.isna().sum().sum())}


def main() -> None:
    df = load_data()
    print(summarize(df))


if __name__ == "__main__":
    main()
