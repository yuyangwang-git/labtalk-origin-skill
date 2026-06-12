# Importing And Exporting

Use this reference for file IO workflows.

## Import ASCII Data

```labtalk
newbook;
string fpath$ = "Samples\Statistics\body.dat";
string fname$ = system.path.program$ + fpath$;
impasc;
```

- `impasc` imports ASCII files into the active workbook.
- Build file paths with string variables.
- Use explicit import options when headers, units, comments, or long names matter.

## Common Import X-Functions

| Name | Use |
|---|---|
| `impASC` | Import ASCII file(s) |
| `impCSV` | Import CSV files |
| `impExcel` | Import Excel files |
| `impImage` | Import images |

## Export Worksheets

```labtalk
expASC;
```

Use worksheet export X-Functions when creating data files from workbooks.

## Export Graphs

```labtalk
expGraph type:=png path:=system.path.user$ filename:="graph1";
```

- Use explicit `path` and `filename` values for reproducible automation.
- For exporting all graphs, combine graph enumeration with export commands.

## Export Matrices And Videos

- Use `expMatAsc` for non-image matrices.
- Use image/video export X-Functions when working with matrix images or graph animations.
