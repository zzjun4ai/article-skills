# Article Skills

This repository contains portable, production-oriented agent skills for scientific
article workflows. Each skill keeps its behavior contract in `SKILL.md`, loads deeper
references only when needed, and uses deterministic scripts for checks that should not
depend on model judgment alone.

## Published skills

| Skill | Purpose |
|---|---|
| `article-figure` | Data-led chart selection, Matplotlib figures, image-guided style reproduction, vector export, and visual QA |
| `article-citation` | Claim-to-source mapping, citation verification states, insertion, and bibliography audits |
| `article-data` | Source-data packages, provenance, data availability, repository planning, and FAIR metadata |
| `article-polishing` | Meaning-preserving copyediting, restructuring, translation, and protected-token checks |
| `article-reader` | Source-grounded overview, focused reading, and full-paper bilingual readers |
| `article-response` | Point-by-point reviewer/editor responses with revision and evidence tracking |
| `article-review` | Bounded, evidence-grounded pre-submission and reviewer-style assessments |
| `article-writing` | Claim-evidence-led manuscript planning, section drafting, and integrity checks |

## Design principles

- Keep the cross-agent `SKILL.md` contract canonical.
- Put trigger conditions in the frontmatter `description`.
- Keep the main instructions concise; load detailed references only when needed.
- Encode fragile or repetitive work in tested scripts.
- Match prescriptiveness to risk and state scope boundaries.
- Run the same checks locally and in CI.

## License

MIT License

## Validate

Run all contract, link, and script tests from the repository root:

```sh
make check
```

## Reference

This repository is an independent adaptation. Its compact routing, progressive disclosure, artifact-level QA, and figure template/preview review were informed by the following open-source projects; their code and assets remain under their respective licences. In particular, third-party PNG examples are treated as design references and are not redistributed here.

- [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills)
- [google-deepmind/science-skills](https://github.com/google-deepmind/science-skills)
- [Trae1ounG/paper-plot-skills](https://github.com/Trae1ounG/paper-plot-skills)
- [Haojae/scipilot-figure-skill](https://github.com/Haojae/scipilot-figure-skill), [scipilot-cite-skill](https://github.com/Haojae/scipilot-cite-skill), and [scipilot-writing-skill](https://github.com/Haojae/scipilot-writing-skill) 
