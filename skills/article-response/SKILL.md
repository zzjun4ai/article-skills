---
name: article-response
description: >-
  Draft, audit, or revise evidence-based point-by-point responses to reviewers
  and editors. Use for reviewer comments, decision letters, rebuttal or response
  letters, major or minor revision, comment triage, revision-location mapping,
  and requests such as 回复审稿人、逐点回复、审稿意见回复、修回信 or 写rebuttal. Do
  not claim experiments, analyses, manuscript changes, or locations that are unverified.
---

# Article Response

Turn reviewer or editor feedback into a precise, respectful response document.

## Route the request

Identify `draft`, `audit`, `revise`, `triage-only`, `cover-letter`, `revision-package`,
or `appeal-like` mode. Also record the decision type and whether the supplied materials include the decision letter,
original manuscript, revised manuscript, figures/supplements, and author notes. Route
appeal-like cases separately; do not draft an appeal by default. For ordinary revision
work, extract `Major Revision`, `Minor Revision`, or equivalent from the decision letter;
if it remains unknown and changes strategy, ask before drafting prose.

## Shortest successful workflow

1. Extract editor instructions first, then reviewer comments. Split compound comments
   into atomic items and assign stable IDs such as `E1`, `R1.1`, and `R2.3` while
   preserving the original wording.
2. Classify each item as accepted, partial, clarified, disputed, or
   `AUTHOR_INPUT_NEEDED`; identify the evidence and manuscript action required.
   Preserve reviewer separation: an internal master may reconcile overlap, but a
   reviewer-facing response must not reveal another reviewer's wording or identifiers.
3. Draft each response in the order: direct answer, evidence/rationale, exact change,
   and revision location. Read [references/tone-and-evidence.md](references/tone-and-evidence.md)
   for disagreement and limitation language.
4. Distinguish completed revisions from proposed work, unavailable experiments, and
   placeholders. Do not convert a plan into past tense.
5. Map every claimed change to the revised manuscript or label the location as pending.
6. Read [references/package-consistency.md](references/package-consistency.md) and
   compare every quoted revision and claimed location against the latest manuscript.
   Any manuscript edit invalidates the previous quote/location check.
7. Run the response-matrix checker and return a readiness state with unresolved author
   inputs. Use [references/difficult-cases.md](references/difficult-cases.md) when
   reviewers conflict or a requested experiment is infeasible.

## Output contract

Return a strategy summary, point-by-point letter, and response matrix containing item
ID, preserved comment, classification, response, evidence, action, location, and
readiness. For audits, report unsupported claims and missing manuscript mappings before
rewriting the letter.

## Failure behavior

Do not claim an experiment, analysis, citation, line number, panel, supplement, or
revision was completed unless supplied evidence confirms it. Use
`AUTHOR_INPUT_NEEDED` and a precise placeholder instead.

## Non-goals

Do not hide adverse results, attack reviewers, invent editor instructions, or change
the manuscript beyond the requested response scope.

## Supporting resources

- Read [references/response-matrix.md](references/response-matrix.md) when
  converting a decision letter into a tracked response table.
- Read [references/tone-and-evidence.md](references/tone-and-evidence.md) for
  evidence-calibrated agreement, clarification, and disagreement.
- Read [references/difficult-cases.md](references/difficult-cases.md) for impossible
  experiments, conflicting reviewers, or appeal-like requests.
- Read [references/package-consistency.md](references/package-consistency.md) whenever
  the response and manuscript are edited together or a package is about to ship.
- Run `python {baseDir}/scripts/check_response_matrix.py INPUT.csv` before
  delivering a response matrix.
