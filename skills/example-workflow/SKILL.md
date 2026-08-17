---
name: example-workflow
description: Normalizes line-oriented text files and produces a deterministic JSON summary. Use when testing this repository template, learning how scripts and references support a SKILL.md workflow, or verifying a newly cloned skill repository end to end.
---

# Normalize Text Records

Turn a UTF-8 text file into stable, reviewable output. Treat each non-empty line as one record.

## Workflow

1. Inspect the input without modifying it.
2. Run `python3 {baseDir}/scripts/normalize.py INPUT --output OUTPUT`.
3. Review the emitted counts and sample records.
4. Report the input path, output path, record count, and duplicate count.

Use `--dry-run` when the user wants a preview. Never overwrite the input file.

## Output contract

Produce JSON containing `source`, `record_count`, `duplicate_count`, and `records`. Normalize surrounding whitespace, discard blank lines, preserve first-seen order, and remove exact duplicates.

Read [references/behavior.md](references/behavior.md) when changing normalization rules or tests.

## Failure handling

- Stop with a clear error if the input does not exist or is not UTF-8.
- Create parent directories for the requested output.
- Do not silently switch output paths.
