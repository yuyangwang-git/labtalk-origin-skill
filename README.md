# LabTalk Origin Skill

OpenAI Codex skill for writing, debugging, reviewing, and explaining OriginLab Origin LabTalk scripts.

It is optimized for OpenAI Codex's skill format and includes compact references for LabTalk syntax, variables, ranges, datasets, X-Functions, workbooks, worksheets, graphing, importing/exporting, analysis workflows, automation, and command lookup.

## Install

Tell Codex:

```text
Install the OpenAI Codex skill located at labtalk-origin/ from https://github.com/yuyangwang-git/labtalk-origin-skill into my Codex skills directory.
```

The skill is in the repository subfolder:

```text
labtalk-origin/
```

Or manually copy that `labtalk-origin` folder into:

```text
~/.codex/skills/labtalk-origin
```

On Windows, this is typically:

```text
C:\Users\<you>\.codex\skills\labtalk-origin
```

Restart Codex or start a new conversation so the skill can be discovered, then ask Codex to use `$labtalk-origin`.

## Usage

Examples:

```text
Use $labtalk-origin to write a LabTalk script that imports a CSV file, creates a worksheet column, and plots the result.
```

```text
Use $labtalk-origin to explain how to call an Origin X-Function from LabTalk.
```

For command lookup, the skill includes:

```text
labtalk-origin/scripts/search_labtalk_reference.py
```

## Background

This skill was distilled from OriginLab's [LabTalk Scripting Guide](https://d2mvzyuse3lwjc.cloudfront.net/pdfs/Origin2026_Documentation/English/LabTalk_Scripting_Guide_E.pdf#zoom=100).
