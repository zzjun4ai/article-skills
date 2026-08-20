---
name: article-polishing
description: >-
  Polish, restructure, proofread, or translate scientific prose into clear,
  precise, publication-ready English while preserving evidence and meaning.
  Use for titles, abstracts, introductions, methods, results, discussions,
  conclusions, full manuscripts, Chinese-to-English academic drafts, and
  requests such as 论文润色、英文论文润色、语言润色、改写 or 学术英语. Do not add
  unsupported claims or silently change technical conclusions.
---

# Article Polishing

Improve manuscript language without weakening scientific precision.

## Route the request

- `copyedit` — correct grammar, concision, and consistency with minimal intervention.
- `substantive-edit` — repair paragraph logic and section flow while preserving claims.
- `translate-and-polish` — translate for scientific meaning, then polish in the target
  language.
- `language-audit` — diagnose issues and propose edits without rewriting everything.

Confirm the target section, output medium (`tex`, Word/plain, or Markdown), language
direction, journal/audience, paper type, and intervention level. State the detected
axes in one short line when they affect the edit. Preserve the user's formatting
medium; do not inject Markdown into Word text or damage LaTeX commands.

## Shortest successful workflow

1. Record protected content before editing: numbers, units, equations, citation keys,
   cross-references, named entities, qualifiers, and conclusion direction. Read
   [references/preservation-rules.md](references/preservation-rules.md).
2. Build or update a terminology ledger for recurring terms, abbreviations, notation,
   units, and named methods. Diagnose the highest-level problem first: section purpose, paragraph logic,
   claim-evidence-boundary, sentence structure, then word choice.
3. Revise only as deeply as requested. Keep good wording; do not rewrite merely to
   create visible changes.
4. Run terminology checks and compare protected tokens between original and revision.
   For a full manuscript or a repeatedly revised draft, also run the cross-document
   sweep in [references/whole-manuscript-consistency.md](references/whole-manuscript-consistency.md).
5. Read the revision as a skeptical reviewer for overclaim, causal inflation,
   terminology drift, and mechanical “AI-like” rhythm. Revise again when needed.
6. Return the polished text, material-change log, and unresolved author questions.

## Output contract

Return publication-ready prose in the requested medium, plus a concise change log.
For translation or deep editing, include a meaning-preservation note or back-check for
substantive shifts. Report machine checks actually run and any residual warnings.

## Failure behavior

Do not guess missing methods, results, citations, numerical values, or intended causal
claims. If protected content changes unexpectedly, stop and reconcile the diff before
delivery. Never claim “meaning unchanged” without checking.

## Non-goals

Do not peer-review, redesign the study, invent citations, or alter statistical
interpretation. Route manuscript drafting to `article-writing` and reviewer replies to
`article-response`.

## Supporting resources

- Read [references/polishing-checklist.md](references/polishing-checklist.md)
  when performing a substantive language edit.
- Read [references/preservation-rules.md](references/preservation-rules.md) before
  translating or deeply rewriting technical prose.
- Read [references/whole-manuscript-consistency.md](references/whole-manuscript-consistency.md)
  for terminology, unit, precision, claim, display, and cross-section drift.
- Run `python {baseDir}/scripts/check_terminology.py INPUT.txt --term
  canonical=variant` to identify terminology drift.
- Run `python {baseDir}/scripts/compare_protected_tokens.py ORIGINAL REVISED` before
  delivering a translation or substantive edit.
