# Skill authoring guide

## Source of truth

Treat each `skills/<name>/SKILL.md` as the canonical behavior contract. Keep platform-specific metadata as a thin adapter and never duplicate the workflow there.

## Required structure

```text
skills/<skill-name>/
├── SKILL.md
├── scripts/                # optional deterministic utilities
├── references/             # optional on-demand knowledge
└── assets/                 # optional output resources
```

Use lowercase kebab-case names of at most 64 characters. The directory name and frontmatter `name` must match.

## SKILL.md rules

- Put only `name` and `description` in YAML frontmatter for broad compatibility.
- Make `description` say both what the skill does and when it should trigger.
- Write instructions in imperative form.
- Keep `SKILL.md` under 500 lines.
- Put the shortest successful workflow first.
- Explain decision criteria, invariants, output contracts, and failure behavior.
- Match strictness to risk: fragile tasks need checkpoints; flexible tasks need heuristics.
- Add explicit non-goals when a nearby workflow would produce a wrong or unsafe result.

## Progressive disclosure

Link every supporting reference directly from `SKILL.md` and say when to read it. Avoid reference chains. Store executable procedures in `scripts/`, detailed knowledge in `references/`, and files copied into outputs in `assets/`. Delete unused directories.

Use `{baseDir}` in instructions when referring to the current skill directory. Never hardcode a contributor's absolute path.

## Scripts and tests

Prefer standard-library scripts when practical. Give scripts a CLI, useful errors, deterministic output, and non-destructive defaults. Test scripts by executing them on representative data, not merely importing them.

Every behavior-changing contribution must add or update a test. Include at least one realistic success case and one meaningful failure or boundary case.

## Review checklist

- Does the description trigger on substantive user language without being overly broad?
- Does the skill add non-obvious procedural value?
- Can an agent find every required resource directly from `SKILL.md`?
- Are output and failure semantics observable and testable?
- Are destructive actions gated or replaced with reviewable output?
- Does `make check` pass?
