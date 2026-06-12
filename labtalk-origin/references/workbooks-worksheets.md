# Workbooks, Worksheets, And Columns

Use this reference for creating books, selecting sheets, manipulating columns, and transforming worksheet data.

## Workbook Basics

```labtalk
newbook;
newbook name:=MyBook;
page.active$ = "Book1";
```

- `page` refers to the active window/page.
- `wks` refers to the active worksheet.
- Use explicit workbook/sheet/range notation when a script should not depend on the active window.

## Worksheet And Column Operations

```labtalk
wks.ncols = 3;
wks.addcol();
wks.col2.name$ = "Result";
wks.col$(wks.ncols).lname$ = "Mean";

col(B) = 2 * col(A);
```

## Column Metadata

```labtalk
wks.col$(ii).lname$ = "Long Name";
wks.col$(ii).unit$ = "ms";
wks.col$(ii).comment$ = "Processed value";
```

## Transforming Worksheets

```labtalk
wunstackcol irng1:=(1, 3:7) irng2:=2 label:="Comments";
wstackcol;
wtranspose type:=all ow:=<new>;
```

## Row/Column Ranges

```labtalk
range rr1 = 1:2;
delete rr1;

range data = [Book1]Sheet1!Col(2)[1:100];
```

## Practical Pattern

```labtalk
newbook;
string fname$ = system.path.program$ + "Samples\Statistics\nitrogen_raw.txt";
impasc;

// Perform statistics on columns 1 to 4.
colstats irng:=1:4 sem:=<new> n:=<none>;
```
