# Matplotlib vector workflow

## Script layout

Keep one figure per script or expose a clear `main()` entry point. Separate paths,
data loading, data transformation, style, plotting functions, export, and cleanup.
Do not hide calculations in plotting calls.

```python
from pathlib import Path
import matplotlib as mpl
import matplotlib.pyplot as plt

OUT = Path("output")
FIGSIZE = (3.5, 2.6)  # inches: final physical size, not a screen default

mpl.rcParams.update({
    "font.family": "Arial",
    "font.size": 7,
    "axes.labelsize": 7,
    "xtick.labelsize": 6,
    "ytick.labelsize": 6,
    "legend.fontsize": 6,
    "pdf.fonttype": 42,  # retain editable TrueType text in PDF
    "ps.fonttype": 42,
    "svg.fonttype": "none",  # preserve text elements in SVG
    "savefig.facecolor": "white",
    "savefig.transparent": False,
})

def save_figure(fig: plt.Figure, stem: Path, dpi: int = 300) -> None:
    stem.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(stem.with_suffix(".pdf"), format="pdf", bbox_inches="tight", pad_inches=0.01)
    fig.savefig(stem.with_suffix(".svg"), format="svg", bbox_inches="tight", pad_inches=0.01)
    fig.savefig(stem.with_name(f"{stem.name}_preview.png"), format="png", dpi=dpi,
                bbox_inches="tight", pad_inches=0.01)

def main() -> None:
    fig, ax = plt.subplots(figsize=FIGSIZE, layout="constrained")
    # Load explicitly named derived data, then draw semantic marks on ax.
    ax.set(xlabel="Measured quantity (unit)", ylabel="Outcome (unit)")
    save_figure(fig, OUT / "fig_1")
    plt.close(fig)

if __name__ == "__main__":
    main()
```

`bbox_inches="tight"` is not a substitute for layout review. Inspect the preview;
use explicit margins or `layout="constrained"` when labels need more space.

## Vector and raster rules

- Keep lines, markers, text, axes, legends, annotations, and schematic elements as
  vector artists. Do not call `rasterized=True` globally.
- For a large scatter cloud, contour field, or heatmap that makes a PDF impractically
  heavy, rasterise that **single** artist only (`artist.set_rasterized(True)`) and
  record it in the manifest. Preserve text and axes as vectors.
- For microscopy or photographs, retain the original raster file, use `imshow` at the
  intended physical size, and add vector scale bars/labels on top. Effective raster
  resolution is determined by placed size, not the `savefig` DPI alone.
- Prefer PDF when a journal production system is expected; use SVG when downstream
  editing or web-compatible vector inspection is required. Confirm the target journal
  accepts the chosen format before delivery.

## Style and layout invariants

- Use `GridSpec` or named axes for asymmetric multi-panel layouts. Do not rely on
  magic subplot indices that obscure panel intent.
- Define a small semantic palette as named constants. Reuse a condition's colour,
  marker, and label everywhere it appears.
- Put panel labels in figure coordinates or a shared helper so they align across axes.
- Use `ax.set_*`, `ax.tick_params`, and artist handles. Avoid global `plt.*` calls
  once axes exist, except `plt.close(fig)`.
- Put scale, units, and reference lines in source code; never add them in an external
  editor after export.

## Failure checks

Before delivery, confirm the script exits without warnings, PDF/SVG files exist and
are non-empty, the preview matches the vector layout, and text remains selectable in
the vector master. If a chosen font is unavailable, use an installed sans-serif
fallback consistently and record it; do not silently mix unrelated fallback fonts.
