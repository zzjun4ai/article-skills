# Article Skills

This repository contains portable, production-oriented agent skills for scientific
workflows. The current published skill is `article-figure`, an evidence-led
workflow that profiles tabular data, recommends defensible charts, creates a
traceable data-to-figure contract, and checks Nature-family figure delivery.

## Design principles

- Keep the cross-agent `SKILL.md` contract canonical.
- Put trigger conditions in the frontmatter `description`.
- Keep the main instructions concise; load detailed references only when needed.
- Encode fragile or repetitive work in tested scripts.
- Match prescriptiveness to risk and state scope boundaries.
- Run the same checks locally and in CI.

## License

MIT License

## TODO

- [ ] Complete the `nature-figure` to `article-figure` migration: align the
  `SKILL.md` frontmatter name, `Makefile` test path, and README links.
- [ ] Implement and publish the remaining skill directories:
  `article-citation`, `article-data`, `article-polishing`, `article-reader`,
  `article-response`, `article-review`, and `article-writing`.
- [ ] Add a contract test suite for each published skill and keep `make check`
  green locally and in CI.
- [ ] Add a concise README entry and usage example for every published skill.
