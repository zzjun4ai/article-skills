# Scientific Skills

This repository contains portable, production-oriented agent skills for scientific
workflows. The current published skill is `data-to-nature-figure`, an evidence-led
workflow that profiles tabular data, recommends defensible charts, creates a
traceable data-to-figure contract, and checks Nature-family figure delivery.

## Repository layout

```text
skills/                 Published, self-contained skills
templates/skill/        Source used by the skill generator
.github/workflows/      CI equivalent of `make check`
```

Each skill must keep its required entrypoint at `skills/<name>/SKILL.md`. Optional `scripts/`, `references/`, and `assets/` directories belong inside that same skill.

## Design principles

- Keep the cross-agent `SKILL.md` contract canonical.
- Put trigger conditions in the frontmatter `description`.
- Keep the main instructions concise; load detailed references only when needed.
- Encode fragile or repetitive work in tested scripts.
- Match prescriptiveness to risk and state scope boundaries.
- Run the same checks locally and in CI.

## Validate

Run the skill checks from the repository root:

```sh
make check
```

See `AGENTS.md` for authoring rules and
[`skills/data-to-nature-figure/SKILL.md`](skills/data-to-nature-figure/SKILL.md)
for the complete workflow.

## License

MIT License
