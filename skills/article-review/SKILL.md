---
name: article-review
description: >-
  Produce a structured reviewer-style assessment of scientific manuscripts,
  covering novelty, significance, evidence, methods, analysis, reporting,
  readability, and major validity risks. Use for pre-submission review, mock
  peer review, reviewer reports, manuscript critique, 投稿前自审、模拟审稿、预审
  or 帮我审一下论文. Use article-response instead for author rebuttals; do not
  present the assessment as an editorial decision or invent unsupported defects.
---

# Article Review

Produce a constructive, evidence-grounded assessment of a scientific article.

## Establish the review boundary

Confirm whether the input is a full manuscript or a bounded excerpt and list available
methods, data, figures, tables, supplements, and reporting statements. A partial input
receives a bounded review; missing material is “not assessable,” not a defect.

This skill is the referee perspective. Route author rebuttal drafting to
`article-response` and language-only editing to `article-polishing`.

## Shortest successful workflow

1. Extract a shared fact base: research question, central claims, study design,
   visible evidence, claimed significance, audience, and stated limitations.
2. Evaluate claim-evidence alignment, originality, significance, methods and controls,
   analysis and uncertainty, reporting/reproducibility, figures/tables, and readability.
   Read [references/review-checklist.md](references/review-checklist.md).
3. Record strengths as well as concerns. For every finding, provide a stable ID,
   severity, applicability state, claim pointer, exact evidence location, consequence,
   and a resolution test. Read
   [references/concern-calibration.md](references/concern-calibration.md).
4. Separate `fatal`, `major`, `minor`, and `suggestion`; do not inflate stylistic
   preferences into validity failures. `Not assessable` is a boundary, not a defect.
5. Run a role-boundary and groundedness check, then synthesize the highest-leverage
   revisions and what remains not assessable.

## Output contract

Return the review setup and boundary, overall assessment, prioritized findings,
strengths, limitations, actionable requests, and a concise synthesis. Each concern must
be tied to observable manuscript evidence. Use multiple reviewer voices only when the
user requests them; never invent reviewer identities.

## Failure behavior

State unavailable materials and lower confidence accordingly. Do not assert data,
statistical, reporting, ethical, or novelty defects without an observable basis. Do not
present the review as an editor's decision.

## Non-goals

Do not rewrite the manuscript wholesale, fabricate prior-art distinctions, or make
publication decisions on behalf of a journal.

## Supporting resources

- Read [references/review-checklist.md](references/review-checklist.md) when
  conducting a structured review.
- Read [references/role-boundaries.md](references/role-boundaries.md) before producing
  simulated multi-reviewer or recommendation language.
- Read [references/report-structure.md](references/report-structure.md) for a complete
  or bounded review package.
- Read [references/concern-calibration.md](references/concern-calibration.md) to decide
  applicability, severity, confidence, and what would close each concern.
- Run `python {baseDir}/scripts/check_findings.py INPUT.json` to validate a
  machine-readable findings list.
