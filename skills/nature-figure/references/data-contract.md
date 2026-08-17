# Data and provenance contract

## Immutable layers

Maintain four separately identifiable layers:

1. `raw`: received instrument, clinical, image, or database output. Do not edit it.
2. `tidy`: one observation per row, with stable sample/subject/experiment IDs, units,
   conditions, time, batch, and measurement fields.
3. `derived`: explicitly generated values such as normalization, filtering, summary,
   model output, or image quantification. Keep a script and parameter record.
4. `display`: plotting-only order, labels, colours, and annotations. Never make a
   display-only transformation the sole record of an analysis decision.

The figure manifest must name every input file, script/environment version, and
source-data output. Record data ownership/access restrictions rather than embedding
identifiable or controlled-access material in figure source data.

## Analysis record

Before plotting, record:

- outcome and units; predictor/group definitions; planned comparison;
- inclusion, exclusion, QC threshold, missing-data, outlier, and duplicate handling;
- normalization or baseline definition; transformations; aggregation formula;
- biological and technical replicate definitions, experimental unit, and exact n;
- statistical method, assumptions/diagnostics, multiple-testing policy, and software.

If an analysis choice was exploratory, label it as such. The plotted error bar must
name its meaning (`s.d.`, `s.e.m.`, CI, bootstrap interval, etc.); it must not be
called simply “error”.

## Biospecimen-aware record

For human, animal, tissue, or other biospecimen-based figures, report the fields
material to interpretation when available: source/population and eligibility,
anatomical site and diagnosis/phenotype, collection method and timing, ischemia or
pre-analytical intervals when relevant, fixation/preservation, processing, storage,
freeze-thaw or shipping history, assay platform/version, batch controls, and
de-identification/ethics constraints.

## Source-data package

Use a tidy CSV/TSV/XLSX table that reproduces each plotted mark or summary. Include a
README with column definitions, units, panel mapping, calculation links, and a note
for data that cannot be shared. Keep source data distinct from the rendered image.
