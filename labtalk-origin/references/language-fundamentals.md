# Language Fundamentals

Use this reference for LabTalk syntax, execution, statements, variables, strings, and control flow.

## Quick Start

```labtalk
type "Hello World";
type -b "Hello World"; // pop-up message box
```

- LabTalk commands are case-insensitive.
- The Script Window executes one line when pressing Enter. Multi-line scripts commonly end statements with `;`.
- A trailing `=` prints quick output interactively:

```labtalk
wks.ncols=;
wks.col1.name$=;
A = A*PI;
A=;
```

## Statements And Operators

- Assignment uses `=` and can target variables, object properties, columns, and ranges.
- Numeric expressions support normal arithmetic and many built-in functions.
- String variables conventionally end in `$`; the `$` is mandatory when assigning or reading a string variable value.
- Use literal string delimiters `<[< ... >]>` when strings contain quotes, semicolons, or special punctuation.

```labtalk
double dd = 4.5678;
int vv = 10;
const em = 0.5772157;

string greeting$ = "Hello";
greeting2$ = "World";

string s1$ = <[<a"b'";"c">]>;
patternT text:=<[<"Sample A" "Sample B" "Sample C">]>;
```

## Control Flow

```labtalk
if (condition) {
    type "true branch";
} else {
    type "false branch";
}

for(ii = 1; ii <= 10; ii++) {
    type "$(ii)";
}

loop(ii, 1, wks.ncols) {
    type wks.col$(ii).name$;
}
```

- `break` exits loops and can also be used with progress UI patterns.
- `continue` skips to the next loop iteration.
- `switch` is useful when more than two branches are needed.

## Strings

```labtalk
string str$ = Johann Sebastian Bach;
str.Find('Sebastian')=;

/* Assign to string register %A */
%A = "Hello World";
```

- Prefer string variables over string registers for new scripts.
- `%A` to `%Z` are global string registers and can be convenient for short transient values.
- Use string methods where possible for parsing and transformation.

## Running And Debugging

- Use the Script Window for quick tests and Code Builder or OGS files for reusable scripts.
- Use sections such as `[Main]` in OGS routines.
- For UI-triggered scripts, Origin can attach LabTalk to buttons, custom menus, graph labels, and project events.
- Use `type`, `type -b`, and quick-output `=` statements for lightweight debugging.
