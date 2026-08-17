# Post-render visual review

Perform this loop after Matplotlib creates an actual preview at
the final physical size. A source-code inspection alone cannot detect layout defects.

1. Render a PNG preview without rescaling the canvas.
2. Run deterministic checks from `figure-qa.md` and inspect warnings from the selected
   script (missing glyphs, layout warnings, unsupported characters, font fallback).
3. Visually inspect the preview at 100% and at the intended manuscript size.
4. Check panel labels, alignment, whitespace, cropped text, tick-label overlap, legend
   occlusion, axis/scale-bar legibility, colours in grayscale, and semantic consistency
   of repeated encodings across panels.
5. Correct the plotting source, regenerate the vector master and preview, then repeat
   until every applicable check passes.

## Review record

Add the reviewer/date, preview filename, final-size check, grayscale/CVD check, and
any accepted limitation to `figure-manifest.yaml`. A reviewer should be able to tell
whether an issue was fixed in source or merely noticed after export.

## Common remedies

- Increase margins or simplify labels; never reduce body text below the final-size
  minimum merely to fit an overcrowded panel.
- Move or directly label a legend instead of allowing it to cover marks.
- Use figure-coordinate panel labels rather than independent per-axis placement.
- Replace colour-only distinctions with shapes, line styles, labels, or position.
- Correct font configuration in source and re-export; do not edit glyphs in a raster
  image.
