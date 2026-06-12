# Analysis And Applications

Use this reference for statistics, fitting, interpolation, signal processing, peaks, baseline, and image analysis.

## Descriptive Statistics

```labtalk
newbook;
fname$ = system.path.program$ + "Samples\Statistics\nitrogen_raw.txt";
impasc;

colstats irng:=1:4 sem:=<new> n:=<none>;
```

Common descriptive-statistics X-Functions:

| Name | Brief Description |
|---|---|
| `colstats` | Columnwise statistics |
| `rowstats` | Row statistics |
| `stats` | Treat selected columns as a dataset |
| `freqcounts` | Frequency counts |
| `corrcoef` | Correlation coefficient |

## Nonparametric Tests

| Name | Brief Description |
|---|---|
| `signrank1` | Test whether a population median equals a specified value |
| `signrank2/sign2` | Test paired medians |
| `mwtest/kstest2` | Test whether two samples have identical distribution |
| `kwanova/mediantest` | Test medians across indexed groups |
| `friedman` | Compare three or more paired groups |

```labtalk
mwtest irng:=(col(c), col(d)) tail:=two rt:=<new name:=mynw>;
page.active$="mynw";
getresults tr:=mynw;
```

## Survival Analysis

| Name | Brief Description |
|---|---|
| `kaplanmeier` | Kaplan-Meier estimator |
| `phm_cox` | Cox proportional hazards model |
| `weibullfit` | Weibull fit |

## Interpolation And Matrix Analysis

```labtalk
newbook mat:=1;
filepath$ = "Samples\Matrix Conversion and Gridding\Direct.dat";
string fname$ = system.path.program$ + filepath$;
impasc;

range rin = 1;
int nx, ny;
nx = rin.ncols * 10;
ny = rin.nrows * 10;
minterp2 method:=bicubic cols:=nx rows:=ny;
```

## General Advice

- Prefer X-Functions for built-in analysis.
- Name output report trees/sheets when subsequent code reads results.
- Mark OriginPro-only features if a table or function name says Pro Only.
