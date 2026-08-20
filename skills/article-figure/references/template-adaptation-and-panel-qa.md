# Template Adaptation and Panel QA

Use this reference when a request includes a preview image, an example figure, or an
existing plotting script. A rendered example proves only that one input rendered; it
does not prove that the underlying statistic, transform, or layout fits new data.

## Choose one reuse level

| Level | Use when | Reuse |
|---|---|---|
| `exact` | question, data shape, transform, uncertainty, and panel meaning match | paths, labels, output prefix |
| `structural` | scientific meaning and dimensionality match | explicit field mapping and guarded transforms |
| `style-only` | only the visual grammar is transferable | palette, spacing, typography, marks, legend style |
| `build-new` | the example answers another question | no inherited statistical logic |

Before adapting code, record `template field -> user field -> role -> units -> allowed
values`, category order, replicate unit, uncertainty definition, and exclusions. Reject
structural reuse when any of these are ambiguous. Guard logs, ratios, interpolation,
normalization, binning, density estimation, and stochastic summaries against invalid
inputs. Do not retain demo or simulated values in a production script.

## Learn from images without treating pixels as data

Use a reference PNG to inspect panel hierarchy, repeated encodings, crop strategy,
relative whitespace, legend placement, and final-size typography. Do not infer exact
measurements, sample sizes, uncertainty, or statistical tests from pixels. Large
canvases can hide unreadable or absurdly oversized labels when viewed as thumbnails;
physical-size review is mandatory.

For image plates, preserve raw channels, calibration, crop coordinates, scale bars,
global contrast operations, pseudocolour mapping, and the relation between each crop
and its parent image. A synthetic gallery image is a composition reference, not
evidence of an acceptable primary-image workflow.

## Audit panel by panel

Inspect every panel at target physical size, then inspect the assembled figure. Record:

| Panel | Unique claim | Data/replicate unit | Center and spread | Labels | Collision | Pass |
|---|---|---|---|---|---|---|

Cover each panel mentally. If the evidence chain remains complete, merge or remove the
panel. Compare repeated panels for identical terminology, uncertainty definitions,
axis semantics, category order, and colour mapping. Check the vector export for
selectable text and inspect the PNG only as a preview.

