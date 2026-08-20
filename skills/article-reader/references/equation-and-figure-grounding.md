# Equation and Figure Grounding

## Equations

Preserve equation order, identifiers, symbols, subscripts, superscripts, operators,
units, and surrounding definitions. Resolve custom LaTeX macros before rewriting an
expression. Distinguish inline from display mathematics and keep prose outside math
delimiters. If an equation is image-only or OCR is uncertain, embed or cite the crop,
record the page and bounding region, and mark the transcription confidence; do not
guess missing glyphs.

## Figures and tables

Place each figure or table near its first explanatory passage. Record source page,
caption, panel labels, crop boundaries, and extraction confidence. Keep the full
caption or a source-faithful caption reference. Do not crop away scale bars, legends,
axis labels, panel labels, or contextual insets. When the source cannot be legally or
technically reproduced, use an anchored description instead of inventing a replacement.

## Source-map minimum

Each important block should have a stable ID, block type, source anchor, confidence,
and output location. Equations should additionally record their identifier and whether
they were transcribed or embedded. Figures should record panel coverage and crop or
asset path. A missing source block remains explicit in `translation_notes.md`; it does
not justify switching a requested full reader into summary mode.

