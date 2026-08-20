---
name: article-citation
description: >-
  Select, verify, and place citations in scientific manuscripts, with traceable
  claim-to-source mapping and consistent reference metadata. Use when adding
  references to a paragraph or manuscript, finding literature for a claim,
  checking citation support, building a reference list, or handling requests
  such as 补引用、找引用、加参考文献、文献支撑 or 学术写作引用. Do not invent
  sources or treat title-level relevance as evidence.
---

# Article Citation

Build a traceable claim-to-source evidence chain for a scientific article.

## Route the request

- `passage-support` — find and assess sources for supplied claims without editing a
  document.
- `manuscript-insertion` — add citation markers and a bibliography to a scoped copy of
  a manuscript while preserving all existing prose and formatting.
- `bibliography-audit` — verify metadata, support, ordering, and citation-list coverage
  for existing references.

Confirm the mode, target text, date range, source-type or venue constraints, preprint
policy, citation style, desired number of sources, and whether the user requires a
restricted journal family. State detected scope and date limits before searching. For
more than about ten claims, batch the work and preserve stable claim IDs across batches.

## Shortest successful workflow

1. Split the target text into atomic, citable claims; do not attach one citation to a
   paragraph containing several unrelated assertions.
2. Read [references/search-strategy.md](references/search-strategy.md). Decompose each
   claim into entity, relationship, outcome, context, and boundary; create precise,
   synonym, and broader fallback queries and identify the needed evidence type.
3. Search authoritative scholarly sources and inspect at least the abstract or full
   source page. A title or search snippet is not enough to establish support.
4. Record stable identifiers and assign both a metadata verification state and a claim
   support grade using [references/verification-and-support.md](references/verification-and-support.md).
   Keep `metadata-only`, contradictory, and context-mismatched candidates out of the
   accepted-support set even when their titles look relevant.
5. Reject sources whose identity or support cannot be established. Prefer fewer
   verified references to a padded list.
6. For manuscript insertion, work on a new output or reviewable diff, preserve the
   original text, and place markers only beside claims they support.
7. Run `validate_references.py`, check citation order and bibliography coverage, then
   report unresolved claims and partially verified metadata.

## Output contract

Return a citation matrix with claim ID, source ID, support grade, verification state,
and rationale. Add the formatted bibliography or edited manuscript copy when requested,
plus an explicit rejected/unresolved list. Never label an offline metadata check as
live verification.

## Failure behavior

Do not fabricate a citation, DOI, quotation, bibliographic field, verification log, or
support rationale. If search access or source text is unavailable, mark the item
`UNVERIFIED` and stop it from entering the final bibliography.

## Non-goals

Do not turn a focused citation task into a broad literature review, rewrite scientific
claims, or silently change reference-manager files.

## Supporting resources

- Read [references/citation-workflow.md](references/citation-workflow.md) when
  designing a claim-to-source table.
- Read [references/verification-and-support.md](references/verification-and-support.md)
  before accepting sources into the final bibliography.
- Read [references/search-strategy.md](references/search-strategy.md) when converting
  Chinese or English claims into searches, fallback queries, and support decisions.
- Run `python {baseDir}/scripts/validate_references.py INPUT.csv` to check a
  reference table without modifying it.
