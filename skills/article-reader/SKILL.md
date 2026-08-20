---
name: article-reader
description: >-
  Read, translate, and explain scientific papers and supplementary materials
  with source-grounded section, figure, table, method, and result tracing. Use
  for full-paper or focused reading from PDF, DOI, arXiv, HTML, Markdown, or
  pasted text; Chinese-English explanations; literature comparison; and
  requests such as 读论文、精读论文、全文翻译、文献阅读 or 帮我读这篇文章. Do not
  degrade a requested full reading into summary-only output or invent missing content.
---

# Article Reader

Create a source-grounded understanding of a scientific article.

## Route the request

- `overview` — concise structured summary with source anchors.
- `focused-reading` — answer a defined question by tracing relevant methods, results,
  figures, tables, and limitations.
- `full-paper-reader` — section-preserving reading or Chinese-English side-by-side
  translation with figure/table placement and a terminology ledger.

Detect the source format: selectable PDF, scanned PDF, publisher HTML, DOI/arXiv link,
Markdown, or pasted text. Read [references/source-routing.md](references/source-routing.md)
for extraction choices and state the detected route. A DOI that resolves to a PDF first
uses the DOI route, then the PDF route. State unavailable pages, supplements, equations,
or figures before analysis.

## Shortest successful workflow

1. Define the reading mode, question, audience level, language, and source boundary.
2. Build a source map before summarizing: sections, page/line anchors, figures, tables,
   supplements, references, and extraction confidence.
3. Separate reported methods, observations, author interpretations, limitations, and
   your own inference. Never merge them into one voice.
4. Trace important statements to page, section, figure, table, or supplement. Place
   figures/tables near the prose they support in full-paper outputs.
5. Maintain a terminology ledger for recurring technical terms and preserve hedging,
   uncertainty, and equation/identifier fidelity in translation. Read
   [references/equation-and-figure-grounding.md](references/equation-and-figure-grounding.md)
   when mathematical or figure-aware fidelity matters.
6. For a full-paper package, run `validate_reader_package.py` against `paper.md` and
   `source_map.json`; then run a coverage check against the requested mode.
7. List missing or low-confidence
   source blocks.

## Output contract

Return the mode-appropriate package defined in
[references/output-contract.md](references/output-contract.md). Every substantive claim
must have a source anchor, and interpretation must be visibly distinguished from source
content. A full-paper request must not silently collapse into a summary.

## Failure behavior

When extraction, OCR, pages, supplements, or figures are unavailable, create a bounded
draft and mark exact gaps and confidence. Do not invent missing numbers, equations,
methods, figure content, or conclusions.

## Non-goals

Do not rewrite the paper as an original study, present inference as quotation, or treat
a summary as a substitute for the source.

## Supporting resources

- Read [references/reading-record.md](references/reading-record.md) when a
  paper needs an auditable reading record.
- Read [references/source-routing.md](references/source-routing.md) before extracting
  non-Markdown sources.
- Read [references/output-contract.md](references/output-contract.md) for full-paper,
  bilingual, or figure-aware deliverables.
- Read [references/equation-and-figure-grounding.md](references/equation-and-figure-grounding.md)
  for equations, image-only formulae, crops, captions, and figure placement.
- Run `python {baseDir}/scripts/extract_sections.py PAPER.md` to create a
  lightweight section map.
- Run `python {baseDir}/scripts/validate_reader_package.py PAPER.md --source-map
  SOURCE_MAP.json --strict` before delivering a full-paper reader package.
