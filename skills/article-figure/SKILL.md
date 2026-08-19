---
name: data-to-nature-figure
description: >-
  Guide agents to write reproducible Python and Matplotlib code for publication-ready,
  editable vector figures. Use for Nature-style manuscript plots, data-to-figure
  workflows, Matplotlib PDF/SVG/EPS export, multi-panel scientific figures, chart
  selection, figure-code review, source-data packages, colour accessibility, and
  post-render visual QA. Do not use for R, Plotly, web dashboards, or Illustrator-first work.
---

# Data to Nature Figure

Write Python code that creates a defensible scientific figure and its editable vector
master. The deliverable is not an image alone: it is a reproducible Matplotlib script,
derived/source data, a vector export, a final-size preview, and a review record.

## Non-negotiable execution contract

- Use **Python with Matplotlib** for all plotting, preview rendering, vector export,
  and visual corrections. `pandas`, NumPy, and SciPy may prepare/analyse data, but
  Matplotlib must own the final figure canvas and export.
- Do not switch to R, Plotly, browser graphics, PowerPoint, or manual vector editing
  as a workaround. If Matplotlib or a required package is unavailable, report the
  blocker and provide the Matplotlib code; do not generate a substitute figure.
- Preserve raw data and primary images. Write derived data to a new file and record
  every filtering, transformation, normalization, and aggregation decision.
- Export data plots as editable `PDF` and/or `SVG`. Rasterise only a specific dense
  layer or continuous-tone image when necessary, never the entire figure.

## Shortest successful workflow

1. State the figure claim, target journal or `Nature-family baseline`, final display
   width, expected panels, and delivery files. If the claim is unknown, ask what the
   figure must persuade the reader to believe; a requested chart type is not a claim.
2. Read `references/data-contract.md`. For CSV data, run
   `python {baseDir}/scripts/profile_data.py INPUT.csv --group GROUP_COLUMN`; inspect
   types, missingness, group sizes, and numerical summaries before selecting a chart.
3. Read `references/chart-selection.md` and recommend the chart from the claim and
   data shape. Explain a misleading request and offer a concrete alternative before
   coding it.
4. Complete `templates/figure-manifest.yaml` beside the source script. Set its backend
   to `python-matplotlib`; never overwrite raw input.
5. Read `references/matplotlib-vector-workflow.md`, then write one self-contained
   Python script that loads data, computes displayed values, creates the figure, and
   calls the prescribed vector export helper.
6. Read `references/nature-format.md` and `references/colour-accessibility.md` before
   styling. Render a final-size PNG preview from the same Matplotlib script.
7. Apply `references/figure-qa.md` and `references/visual-review.md`. Fix source code,
   re-export, and re-review until the vector master and preview pass.

## Code requirements

The generated script must:

- set figure dimensions in inches from the intended final physical size, not rescale
  a generic canvas after export;
- centralize rcParams, semantic colours, font sizes, and output paths near the top;
- use an explicit `fig, ax = plt.subplots(...)` (or named GridSpec layout), never
  stateful implicit plotting for a multi-panel manuscript figure;
- define units, n, uncertainty, statistics, and the plotted data transformation in
  code and carry the same facts into the figure legend/source-data package;
- call `fig.savefig` for vector output with deterministic filenames and finish with
  `plt.close(fig)`; and
- emit a PNG preview only for QA. A PNG is not the vector master.

## Nature-style defaults

Design at final display size with one sans-serif family, 5–8 pt labels as the baseline,
white plot backgrounds, restrained lines, direct labels where clearer than a legend,
and one semantic palette. Show individual observations where they are interpretable;
do not let mean-only bars conceal a small sample. Every uncertainty display must be
defined in the legend together with exact n and statistical method.

Use colour with redundant encodings such as shape, line style, position, or labels.
Do not use rainbow/`jet`, red-versus-green-only distinctions, dual y-axes that imply
an association, 3D charts, or lines joining unordered categories.

## On-demand references

- `references/data-contract.md` — raw-to-derived provenance and source-data package.
- `references/chart-selection.md` — evidence-led chart choice and interventions.
- `references/matplotlib-vector-workflow.md` — Matplotlib code structure, rcParams,
  editable vector export, raster-image placement, and failure checks.
- `references/nature-format.md` — Nature-family formatting and image-integrity baseline.
- `references/colour-accessibility.md` — perceptual colour and CVD/grayscale checks.
- `references/figure-qa.md` — deterministic preflight and delivery bundle.
- `references/visual-review.md` — final-size preview and source-code remediation loop.
- `references/evidence-notes.md` — scope of supplied evidence.

## Boundaries

- Do not claim BRISQ compliance without the original checklist or an applicable
  user-supplied reporting standard.
- Do not selectively alter microscopy, gels, blots, or other primary-image pixels.
  Retain originals and document crops, compositing, contrast adjustment, and
  pseudocolour.
- Do not manually repair a flattened PDF/SVG. Make visual corrections in the Python
  source, then regenerate all deliverables from that source.
