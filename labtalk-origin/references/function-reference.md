# Function And X-Function Reference

Use this reference as the entry point for function lookup. For exact matches and fuzzy search, run:

```powershell
python scripts/search_labtalk_reference.py <term>
```

The generated index lives in `references/command-index.json` and is derived from the cleaned LabTalk tables.

## High-Value Lookups

| Name | Brief Description |
|---|---|
| `impASC` | Import ASCII file(s) |
| `impCSV` | Import CSV file(s) |
| `expASC` | Export worksheet data as ASCII file |
| `expGraph` | Export graph(s) to graphics file(s) |
| `plotxy` | Plot worksheet data as XY graph |
| `colstats` | Columnwise statistics |
| `rowstats` | Row statistics |
| `mwtest/kstest2` | Nonparametric two-sample tests |
| `kaplanmeier` | Kaplan-Meier survival estimator |
| `minterp2` | Matrix interpolation/extrapolation |

## Lookup Workflow

1. Search for the function or concept.
2. Open the relevant topic reference for usage patterns.
3. Write a small runnable LabTalk snippet.
4. Include assumptions about active workbooks, selected columns, and OriginPro-only tools.
