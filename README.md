# Pandas CSV Parser Review
This project reviews `pandas.read_csv` row-width handling with a small synthetic example.
Reliable inputs matter for analyst workflows such as workforce summaries and Excel reporting at JPMorgan Chase; this project uses no JPMorgan data and makes no claim about its internal software.

## Problem

Before summarizing workforce or skills-training outcomes, how should an analyst distinguish a valid blank from a truncated CSV row? The brief describes mentorship and analyst work involving data and Excel; this review focuses on input quality, not on measuring those outcomes. It is an independent portfolio exercise, not a JPMorgan Chase project or endorsement.

## Data

[`data/synthetic_sample.csv`](data/synthetic_sample.csv) contains five fabricated rows for exercising the repository's CSV loader. The parser examples below are also fabricated inline; neither source contains employee or customer data. No dataset was downloaded. The reviewed open-source code is pandas 3.1.1: [`readers.py` documentation](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/parsers/readers.py#L1668-L1684) and its [parser tests](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/tests/io/parser/test_textreader.py#L157-L202).

## Approach

I read the `read_csv` parameter documentation and the parser tests, then ran two small examples on the installed pandas 3.1.1. The repository itself depends on pandas for CSV loading (`src/load_data.py`).

**Strength:** `on_bad_lines` has clear `error`, `warn`, and `skip` handling for rows with too many fields; the tests check raising, skipping, and warning behavior.

**Improvement ideas:**
- Offer an opt-in strict row-width check for rows with too few fields, preserving today's behavior by default.
- Document and test the difference between a short row (currently padded with a missing value) and a complete row with an intentionally empty field.

## Results

| Synthetic input | `on_bad_lines="error"` result on pandas 3.1.1 |
| --- | --- |
| `name,amount` / `A,10` / `B` | Returns 2 rows; `B.amount` is `NaN`; no exception. |
| `name,amount` / `A,10` / `B,20,extra` | Raises `ParserError`. |

The first case motivates the proposed enhancement, not a bug claim: the documented bad-line setting covers rows with too many fields. The existing project tests pass: `python -m pytest -q` reports 2 passed.

## Issue draft

[`ISSUE_DRAFT.md`](ISSUE_DRAFT.md) contains a reproducible feature request for opt-in rejection of short records. It has not been submitted to pandas.

## Limitations

- This review tests one behavior on pandas 3.1.1; it is not a comprehensive parser review or performance benchmark.
- A missing value may be intentional, so rejecting short rows should be opt-in and backward compatible.
- Public sources checked here do not establish that JPMorgan Chase uses pandas. The connection is analyst data quality and Excel-based workflows, not a claim about the company's software stack.
- The Ashley Wigfall-specific URL supplied in the brief returned HTTP 404 during this review; verify that story's direct source before citing it externally.

## How to run

```bash
python -m pip install -r requirements.txt
python -m src.analysis
python -m pytest -q
```

## Built with AI assistance

AI assistance helped organize and proofread this review. The pandas behavior described above was checked against the public source and tests and reproduced locally. Synthetic data is labeled as such.

## Email summary

I reviewed pandas' CSV row handling because reliable inputs are a practical part of analyst workflows relevant to JPMorgan Chase. On pandas 3.1.1, the documented `on_bad_lines="error"` catches rows with extra fields, while a short row is padded with `NaN`; I drafted an issue proposing an opt-in strict row-width check and clearer documentation. The examples and repository sample are synthetic, and I do not claim that JPMorgan Chase uses pandas or that this project is affiliated with the company.
