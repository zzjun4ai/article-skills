# Agent Skill Repository Template

A small, production-oriented template for building portable Agent Skills. It combines a standards-first `SKILL.md` layout, progressive disclosure, executable validation, and a working reference skill.

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

See `AGENTS.md` for authoring rules and `skills/example-workflow` for a complete, runnable example.

## License

MIT License
