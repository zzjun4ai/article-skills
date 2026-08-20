# Reader output contract

## Overview

Return citation metadata, research question, approach, main findings, limitations, and
source anchors for each major point.

## Focused reading

Return the question, relevant source blocks, answer, evidence chain, limitations, and
what remains not assessable.

## Full-paper reader

Preserve section order. For bilingual output, pair source and translation in bounded
blocks and maintain a terminology ledger. Place each figure or table and its caption
near the relevant discussion. Add a source map with page/section anchors and extraction
confidence, plus translation notes for missing or ambiguous material.

Use `source_map.json` with a top-level `blocks` list. Each block must contain:

```json
{
  "id": "B1",
  "type": "section|figure|table|equation|note",
  "source_anchor": "page, section, figure, table, or supplement location",
  "confidence": "high|medium|low",
  "output_anchor": "matching-paper-md-heading-anchor"
}
```

Keep block IDs unique. Add optional crop paths, panel coverage, equation identifiers,
or terminology entries without replacing the five required traceability fields.

Do not reproduce long copyrighted passages when a sourced explanation is sufficient.
