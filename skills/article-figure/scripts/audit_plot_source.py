"""Run a dependency-free static preflight on a Matplotlib figure script."""

import argparse
import ast
import json
import re
import sys
from pathlib import Path


def audit(text: str) -> dict:
    errors: list[str] = []
    warnings: list[str] = []
    try:
        ast.parse(text)
    except SyntaxError as exc:
        errors.append(f"syntax error at line {exc.lineno}: {exc.msg}")

    if not re.search(r"\b(?:import\s+matplotlib|from\s+matplotlib\b)", text):
        errors.append("Matplotlib import not found")
    if "savefig" not in text:
        errors.append("savefig call not found")

    suffixes = {match.lower() for match in re.findall(r"['\"]([^'\"]+\.(?:pdf|svg|png|tiff?|jpg))['\"]", text, re.I)}
    vector = sorted(path for path in suffixes if path.endswith((".pdf", ".svg")))
    previews = sorted(path for path in suffixes if path.endswith(".png"))
    if not vector:
        errors.append("editable PDF or SVG export not found")
    if not previews:
        warnings.append("final-size PNG preview export not found")
    if not re.search(r"\bplt\.close\s*\(", text):
        warnings.append("plt.close(...) not found")
    if not re.search(r"\b(?:plt\.subplots|fig\.add_gridspec|GridSpec)\b", text):
        warnings.append("explicit subplots or GridSpec layout not found")
    if re.search(r"\b(?:np\.random|numpy\.random|random\.|sample\s*\()", text):
        warnings.append("random, demo, or sampling logic requires an explicit production-data guard")
    if re.search(r"\b(?:jet|rainbow|nipy_spectral)\b", text, re.I):
        warnings.append("unsafe rainbow-style colormap token found")

    return {
        "errors": errors,
        "warnings": warnings,
        "vector_exports": vector,
        "preview_exports": previews,
        "ready": not errors,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("--strict", action="store_true", help="treat warnings as failures")
    args = parser.parse_args()
    try:
        report = audit(args.source.read_text(encoding="utf-8"))
    except (OSError, UnicodeError) as exc:
        report = {"errors": [str(exc)], "warnings": [], "ready": False}
    report["file"] = str(args.source)
    report["ready"] = report["ready"] and not (args.strict and report["warnings"])
    json.dump(report, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")
    return 0 if report["ready"] else 2


if __name__ == "__main__":
    raise SystemExit(main())

