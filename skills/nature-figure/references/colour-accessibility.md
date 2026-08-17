# Colour and accessibility policy

This policy applies the supplied Crameri et al. (2020) guidance: colour must encode
data without introducing perceptual boundaries, false emphasis, or access barriers.

## Match palette to data meaning

| Data meaning | Use | Avoid |
| --- | --- | --- |
| Ordered magnitude | perceptually ordered sequential map, e.g. `cividis`, `viridis`, `magma` | rainbow/`jet`, unordered categorical hues |
| Signed deviation around a meaningful midpoint | balanced diverging map with the midpoint fixed and labelled | diverging map when zero/reference is arbitrary |
| Cyclic quantity | cyclic map with matched endpoints | sequential map that fabricates an edge |
| Nominal groups | small, distinguishable categorical palette plus shapes/direct labels | more hues than readers can reliably distinguish |

Do not use rainbow/`jet` for quantitative data. Its uneven lightness can create false
edges and unequal emphasis. Avoid red-versus-green contrasts, especially at similar
lightness. For “increase/decrease”, combine hue with sign, arrows, position, labels,
or line style; do not rely on red/green alone.

## Required QA

1. Check that quantitative maps have monotonic perceived lightness and label their
   scale, range, and midpoint.
2. View the complete figure in grayscale. Distinct groups and numerical order must
   remain interpretable through luminance, marks, direct labels, or structure.
3. Check common red-green colour-vision deficiency simulations or use a palette
   designed for that purpose. Cividis is a useful sequential default; no palette
   replaces semantic redundancy.
4. Ensure adjacent symbols differ in more than hue when comparison is necessary.
5. Verify that alert/accent colours are used sparingly and consistently; never make
   saturation stand in for statistical significance.

The goal is perceptual accuracy, not a prescribed brand palette. If a journal or
collaborator requires colours that fail the checks, add non-colour encodings and note
the limitation in the figure-review record.
