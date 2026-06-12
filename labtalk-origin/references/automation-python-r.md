# Automation, Projects, Excel, R, And Python

Use this reference for project-level automation and integration workflows.

## Project Automation

- Use project and page objects to manage active windows, metadata, and object loops.
- Use OGS routines and project events for reusable automation.
- Use analysis templates when the workflow should be repeatable across files or batches.

```labtalk
doc -n; // new project
```

## Batch Processing

- Import files in a loop.
- Apply worksheet transformations or analysis templates.
- Save or export outputs with explicit names.

## Excel

LabTalk can open, save, connect, and run Excel workflows from Origin.

Task areas:

- Open Excel workbook
- Save Excel workbook
- Update Origin when Excel changes
- Connect Excel workbook
- Run Excel macro
- Invoke Visual Basic function

## R And Python

- Use Origin's integration features when LabTalk needs to call R or Python.
- Keep file paths and data exchange ranges explicit.
- Use LabTalk for orchestration and the external language for specialized analysis.

## User Interaction

```labtalk
type -b "Processing complete.";
```

Use dialogs or point-picking workflows only when the script is intentionally interactive.
