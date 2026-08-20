# Source routing

- `pdf-text` — extract selectable text and preserve page anchors; inspect layout for
  multi-column reading order.
- `scanned-pdf` — OCR page by page, retain page images, and mark low-confidence OCR.
- `publisher-html` — preserve heading hierarchy, figure captions, tables, and stable
  element or section anchors.
- `doi-arxiv` — resolve to an accessible canonical artifact before reading; record the
  version used.
- `markdown-or-pasted` — preserve headings and line anchors, but state that page and
  original figure placement may be unavailable.

Do not combine text from different versions without recording which sections came from
which artifact. If copyright or access constraints prevent full extraction, provide a
bounded analysis of accessible material rather than reconstructing unavailable text.
