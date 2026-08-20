# Image-guided figure reproduction

Use this mode when the user supplies a paper figure or screenshot as a visual target.
The image may define composition and styling; it does not establish exact data values.

## Measure before coding

Record the image width, height, aspect ratio, panel grid, relative panel widths,
plot-area margins, legend placement, font class, line and marker hierarchy, palette,
spines, ticks, grids, annotations, and special elements such as insets or broken axes.

Match the reference to an existing chart archetype where possible. Reuse the
archetype's structure, then replace every displayed value with user-supplied data.
If only the image exists, produce a style scaffold and label data arrays as required
inputs; do not digitize or guess values unless the user explicitly requests a separate
digitization workflow.

## Iteration contract

1. Render at the target aspect ratio and final physical size.
2. Compare geometry before colour: panel proportions, axes, limits, and whitespace.
3. Compare typography and encodings next.
4. Run the normal final-size visual review and grayscale/CVD checks.
5. Correct the Matplotlib source and re-render; never paint over the preview.

Preserve scientific integrity when the reference itself uses misleading encodings.
Explain the issue and offer a defensible adaptation instead of copying it blindly.
