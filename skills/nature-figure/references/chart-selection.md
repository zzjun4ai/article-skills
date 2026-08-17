# Evidence-led chart selection

Choose a chart to make the claim inspectable. Start from the experimental unit,
variable types, sample size, and intended comparison; do not start from a familiar
chart type.

| Evidence question | Preferred display | Avoid unless justified |
| --- | --- | --- |
| What is the distribution of one continuous measurement? | Histogram/density plus a dot, box, or violin summary | A mean-only bar |
| Do groups differ on a continuous outcome? | Individual points, with a box/violin summary when useful | Mean-only bars that hide observations |
| Are two continuous variables related? | Scatter plot, fitted model/interval, and appropriate summary | A line plot if x is not ordered/continuous |
| Does an outcome change over time or dose? | Line/point plot with uncertainty and actual sampling positions | Bars that hide the trajectory |
| How do categories rank or contribute? | Sorted horizontal bars or labelled dot plot | Pie charts, especially with many categories |
| How does a matrix vary? | Labelled heatmap with an appropriate colour scale | 3D surfaces or rainbow colour maps |
| What is the relationship among several variables? | Correlation heatmap, pairwise plots, or a reduced representation with method details | A dense all-in-one chart |

## Interventions before plotting

- **Small groups:** if group sizes are small enough for points to be legible, show all
  observations. A summary may be overlaid but must not replace them.
- **Unordered categories:** do not connect category means with a line because it
  implies continuity. Use points, intervals, or bars only when a baseline at zero is
  meaningful.
- **Truncated axes:** truncation is sometimes valid for interval estimates or subtle
  changes, but it must be obvious, numerically justified, and not exaggerate a small
  difference. For bar lengths that encode magnitude, start at zero.
- **Dual y-axes:** use separate aligned panels or a principled transformation; dual
  axes can manufacture an apparent association.
- **Many groups or encodings:** split panels or facet the display when more than about
  a dozen categories are needed. Do not solve overcrowding by shrinking text.
- **Statistics:** choose the test from the design and assumptions, not from the chart.
  Do not infer significance from overlap/non-overlap of error bars alone.

When overriding the requested chart, explain the concern, recommend a concrete
alternative, and invite the user's decision. This is scientific review, not an
automatic refusal.
