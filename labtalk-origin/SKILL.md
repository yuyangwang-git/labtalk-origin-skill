---
name: labtalk-origin
description: Use when Codex needs to write, debug, review, or explain OriginLab Origin LabTalk scripts and Origin automation workflows, including LabTalk syntax, variables, ranges, datasets, string handling, X-Functions, workbook and worksheet operations, graphing, importing/exporting, analysis, batch processing, Excel/R/Python integration, and LabTalk function or command lookup.
---

# LabTalk Origin

Use this skill to produce practical Origin LabTalk code and explanations. Prefer concise scripts that use LabTalk idioms from the references rather than generic pseudocode.

## Workflow

1. Identify the task area and read only the needed reference files:
   - Core syntax, control flow, strings: `references/language-fundamentals.md`
   - Variables, datasets, ranges, substitution: `references/variables-ranges-datasets.md`
   - X-Function calls and argument patterns: `references/x-functions.md`
   - Workbooks, worksheets, columns: `references/workbooks-worksheets.md`
   - Plotting, layers, axes, graph objects: `references/graphing.md`
   - File import/export: `references/importing-exporting.md`
   - Statistics, fitting, signal/image analysis: `references/analysis.md`
   - Projects, batch, Excel, R, Python: `references/automation-python-r.md`
   - Function and X-Function lookup: `references/function-reference.md`
2. For command or X-Function lookup, run `scripts/search_labtalk_reference.py <term>` before loading large references.
3. Write LabTalk with explicit object/range references when possible. Include setup lines such as `newbook;`, `impasc;`, `range`, or `page.active$` when the script depends on active windows.
4. Preserve LabTalk syntax exactly: semicolons, `$` string variables, `%()` substitution, `arg:=value` X-Function arguments, and range notation.

## Output Style

- Return runnable LabTalk snippets in fenced `labtalk` code blocks when the user asks for code.
- Mention assumptions about active workbook, selected columns, graph layer, file paths, or OriginPro-only features.
- Prefer X-Functions for built-in operations such as import/export, statistics, fitting, and worksheet transforms.
- If an operation may create output sheets or reports, name the output explicitly, for example `rt:=<new name:=mynw>`.
