---
name: article-figure
description: >-
  Create, revise, reproduce, or audit publication-ready scientific data figures with
  reproducible Python and Matplotlib code, editable PDF/SVG masters, source-data
  traceability, and post-render visual QA. Use for manuscript plots, chart selection,
  multi-panel figures, figure-code review, image-guided style reproduction, journal
  export, colour accessibility, 论文配图、科研绘图、复现这个图 or 投稿级图表. Do not
  use for R, Plotly, dashboards, or diagram/infographic work without quantitative data.
---

# Article Figure

Write Python code that creates a defensible scientific figure and its editable vector
master. The deliverable is not an image alone: it is a reproducible Matplotlib script,
derived/source data, a vector export, a final-size preview, and a review record.

## Route the request

Choose one mode before acting:

- `data-to-figure` — profile supplied data, select a chart from the claim and data
  shape, then render it.
- `revise-or-audit` — inspect existing code and rendered output, identify semantic,
  technical, and visual defects, then fix the source.
- `image-guided-reproduction` — reproduce the layout and visual grammar of a supplied
  figure using separately supplied real data. Read
  [references/image-guided-reproduction.md](references/image-guided-reproduction.md).

An image is evidence for proportions and styling, not for exact underlying values.

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

1. State the mode, figure claim, target journal or `Nature-family baseline`, final
   display width, expected panels, and delivery files. If the claim is unknown, ask
   what the figure must persuade the reader to believe; a chart type is not a claim.
2. For `data-to-figure`, read `references/data-contract.md`. For CSV data, run
   `python {baseDir}/scripts/profile_data.py INPUT.csv --group GROUP_COLUMN`; inspect
   types, missingness, group sizes, and numerical summaries before selecting a chart.
   For image-guided work, measure the reference image and obtain the actual data.
3. Read `references/chart-selection.md` and recommend the chart from the claim and
   data shape. Explain a misleading request and offer a concrete alternative before
   coding it.
4. If reusing a supplied image, script, or example, classify the reuse as `exact`,
   `structural`, `style-only`, or `build-new` with
   [references/template-adaptation-and-panel-qa.md](references/template-adaptation-and-panel-qa.md).
   Write an explicit source-field mapping before adapting statistical logic.
5. Complete `templates/figure-manifest.yaml` beside the source script. Set its backend
   to `python-matplotlib`; never overwrite raw input.
6. Read `references/matplotlib-vector-workflow.md`, then write one self-contained
   Python script that loads data, computes displayed values, creates the figure, and
   calls the prescribed vector export helper.
7. Read `references/nature-format.md` and `references/colour-accessibility.md` before
   styling. Render a final-size PNG preview from the same Matplotlib script.
8. Run `audit_plot_source.py`, then apply `references/figure-qa.md`,
   `references/visual-review.md`, and the panel audit in
   `references/template-adaptation-and-panel-qa.md`. Inspect each panel at final size,
   fix source code, re-export, and repeat until the vector master and preview pass.

## Output contract

Deliver the plotting script, derived/source data, completed figure manifest, editable
vector master, final-size PNG preview, and a short QA record. For audits, distinguish
observed failures, source-code fixes, and checks that could not run.

## Failure behavior

If required data, labels, units, statistics, runtime, or source images are missing,
stop the affected step and name the missing input. Never invent measurements from a
reference image or claim a render/export check that was not executed.

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
- `references/image-guided-reproduction.md` — measure and reproduce visual structure
  without treating pixels as source data.
- `references/template-adaptation-and-panel-qa.md` — choose a safe template-reuse
  level and audit every panel rather than approving a full-page thumbnail.
- Run `python {baseDir}/scripts/audit_plot_source.py FIGURE.py --strict` before
  rendering the delivery bundle; treat its static findings as preflight, not visual
  or statistical validation.

## Boundaries

- Do not claim BRISQ compliance without the original checklist or an applicable
  user-supplied reporting standard.
- Do not selectively alter microscopy, gels, blots, or other primary-image pixels.
  Retain originals and document crops, compositing, contrast adjustment, and
  pseudocolour.
- Do not manually repair a flattened PDF/SVG. Make visual corrections in the Python
  source, then regenerate all deliverables from that source.
