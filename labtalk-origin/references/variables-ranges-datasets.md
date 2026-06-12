# Variables, Ranges, And Datasets

Use this reference when a task depends on LabTalk variable scope, worksheet ranges, loose datasets, object properties, or substitution notation.

## Data Types

| Type | Purpose |
|---|---|
| double | Default numeric value |
| int | Integer value, stored as double internally |
| const | Constant value |
| dataset | Numeric array |
| string | Character sequence, variable name ends with `$` |
| StringArray | Array of strings |
| range | Reference to workbook, worksheet, matrix, graph, or loose dataset data |
| tree | Hierarchical nodes and leaves |
| Graphic Object | Labels, arrows, lines, and user-created graphic elements |

## Scope Patterns

| Scope | Pattern | Persistence |
|---|---|---|
| Project variable | `aa = 1;` | Saved with the OPJ while project is open |
| Session variable | declare in Script Window or command context | While Origin session runs |
| Local variable | declare inside OGS/routine | While script runs |
| Local as session | `@glob=1;` then declare | Session scope; can be saved via project events |

## Dataset Patterns

```labtalk
dataset aa = {1:0.2:10};
int nSize = aa.GetSize();
type "aa has $(nSize) values";

bb = {10:2:100}; // project-level loose dataset
create %(strWks$) -wdn 10 aa bb;
```

## Range Notation

```labtalk
range cc = [Book1]Sheet2!Col(3);
range ll = [Graph1]Layer1!2;
range mm = [MBook1]MSheet1!2;
range xx = [??]!tmpdata_a;
```

General forms:

```text
range r = [BookName]SheetNameOrIndex!ColumnNameOrIndex[RowBegin:RowEnd]
range r = [MatrixBookName]MatrixSheetNameOrIndex!MatrixObjectNameOrIndex[CellBegin:CellEnd]
range r = [GraphName]LayerNameOrIndex!DataPlotIndex[RowBegin:RowEnd]
```

- Use `[??]` for loose datasets.
- Worksheets, matrix sheets, and graph layers can usually be referenced by name or index.
- Range variables can be passed directly to X-Function arguments.

## Substitution

- Use `$(numericExpression)` to convert numeric results to strings.
- Use `%()` for string substitution and worksheet/column addressing.
- For file paths and object names, assign to string variables first to avoid quoting mistakes.

```labtalk
winName$ = "Book1";
type "Active window is %H";
type "Rows: $(wks.nrows)";
```

## Variable Name Conflicts

`@ppv` controls conflicts between project variables, session variables, and local variables:

| Variable | Meaning |
|---|---|
| `@ppv=0` | Default; session/local variables may reuse project variable names |
| `@ppv=1` | Session variable cannot share an existing project variable name |
| `@ppv=2` | Local variable cannot share an existing project variable name |
| `@ppv=3` | Applies both `@ppv=1` and `@ppv=2` |
