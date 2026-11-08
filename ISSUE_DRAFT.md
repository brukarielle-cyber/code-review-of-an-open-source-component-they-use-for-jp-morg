# Feature request: add opt-in strict row-width validation to `read_csv`

## Summary

Please consider an opt-in `read_csv` mode that rejects records with fewer fields than the header. Today, `on_bad_lines="error"` rejects rows with too many fields, but a short row is padded with a missing value. That can make a truncated record look like an intentional blank in downstream summaries.

## Reproduction

```python
from io import StringIO

import pandas as pd

csv = "name,amount\nA,10\nB\n"
print(pd.read_csv(StringIO(csv), on_bad_lines="error"))
```

On pandas 3.1.1, this returns two rows and sets `B.amount` to `NaN`; it does not raise. For comparison, replacing the last row with `B,20,extra` raises `ParserError` with the same `on_bad_lines` setting.

## Expected behavior

An opt-in strict mode should reject the short record and identify its row, while accepting a complete record with an explicitly empty field, such as `B,`. Existing defaults should remain unchanged because short rows can be intentional.

## Scope

Please document the behavior and add tests for short rows, explicit empty fields, and the supported parser engines. This request is for an optional validation feature, not a claim that current behavior violates the documented contract. The synthetic example above contains no real data.