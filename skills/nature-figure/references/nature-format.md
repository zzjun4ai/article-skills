# Nature-family formatting baseline

## Canvas and typography

- Decide final single-, intermediate-, or double-column display width before layout.
- Use one sans-serif font family throughout. Arial or Helvetica are the supplied
  baseline; use a target-journal template when it specifies a different family.
- At final display size, use 5–8 pt text as the working baseline. Test labels, ticks,
  annotation, and scale-bar text at that size rather than at a zoomed screen view.
- Keep panel lettering, axes, units, line weights, spacing, and decimal precision
  consistent across a figure and across related figures.

## File types and raster content

- Prefer editable Matplotlib vector masters for plots, schematics, labels, and
  chemical drawings: PDF, SVG, or EPS as accepted by the journal.
- Preserve live text and paths; embed or package fonts only as required by the target.
  Do not convert the entire plot to a bitmap merely to satisfy a font issue.
- For photographs, microscopy, and other continuous-tone panels, retain the original
  raster asset and export in RGB. The supplied guide gives **300 dpi or higher** as a
  baseline. Calculate pixels from final placed size; larger files do not recover lost
  detail from an undersampled original.
- Compose raster images with Matplotlib vector labels/scale bars. Keep native data and
  uncropped originals separately.

## Legend and statistics

Start the legend with a concise figure title, then explain what each panel shows,
symbols, colours, scale bars, n, error bars, tests, and replicate type so the figure
can be read independently. Keep methods detail in Methods/source data unless needed
to interpret the visual. The supplied guide recommends legends below 350 words; treat
this as a baseline, then check the target journal.

## Image integrity

Do not add/remove/move features. Retain original files. Apply intensity or colour
adjustments uniformly to the complete image and declare material adjustments. Clearly
separate images acquired in different experiments; show boundaries for splices and
preserve sufficient context for reviewer assessment.
