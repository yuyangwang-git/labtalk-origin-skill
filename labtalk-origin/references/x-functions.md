# X-Functions

Use this reference for calling Origin X-Functions from LabTalk.

## Call Syntax

```labtalk
xfname arg1:=value arg2:=value;
```

- X-Function arguments use `name:=value`.
- Input ranges commonly use column indexes, range variables, or grouped ranges.
- Outputs can often be assigned to `<new>`, `<none>`, or `<new name:=...>`.
- Many analysis, import/export, graphing, and worksheet operations are exposed as X-Functions.

## Output Patterns

```labtalk
colstats irng:=1:4 sem:=<new> n:=<none>;
mwtest irng:=(col(c), col(d)) tail:=two rt:=<new name:=mynw>;
getresults tr:=mynw;
```

- Use `<none>` to suppress outputs you do not need.
- Use named report trees or sheets when later script lines read results.
- Activate output pages with `page.active$="name";` when needed.

## Range Arguments

```labtalk
range rr = 1:4;
colstats irng:=rr;

range rin = 1;
minterp2 method:=bicubic cols:=nx rows:=ny;
```

## Common Workflow

1. Prepare data and active workbook/worksheet.
2. Define input ranges explicitly.
3. Call the X-Function with named arguments.
4. Store reports/results in named output objects.
5. Read results with `getresults` or continue processing the output worksheet.

```labtalk
newbook;
fname$ = system.path.program$ + "Samples\Statistics\body.dat";
impasc;

mwtest irng:=(col(c), col(d)) tail:=two rt:=<new name:=mynw>;
page.active$="mynw";
getresults tr:=mynw;

if (mynw.Stats.Stats.C3 <= 0.05) {
    type "At 0.05 level, height of boys and girls are different.";
}
```

## Lookup

Run `scripts/search_labtalk_reference.py <term>` to find brief descriptions of X-Functions and functions in `references/command-index.json`.
