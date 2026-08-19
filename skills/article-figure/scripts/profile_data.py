"""Create a deterministic, read-only profile of a CSV table for chart selection."""

from __future__ import annotations

import argparse
import csv
import json
import math
import statistics
import sys
from collections import Counter
from pathlib import Path
from typing import Any, Dict, List, Optional


def _number(value: str) -> Optional[float]:
    try:
        parsed = float(value)
    except ValueError:
        return None
    return parsed if math.isfinite(parsed) else None


def profile_csv(path: Path, groups: List[str], delimiter: str = ",") -> Dict[str, Any]:
    """Return a JSON-serializable, non-destructive profile for a non-empty CSV file."""
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle, delimiter=delimiter)
        if not reader.fieldnames:
            raise ValueError("CSV must contain a header row")
        fieldnames = reader.fieldnames
        unknown_groups = sorted(set(groups) - set(fieldnames))
        if unknown_groups:
            raise ValueError(f"group columns not found: {', '.join(unknown_groups)}")
        rows = list(reader)

    if not rows:
        raise ValueError("CSV contains no data rows")

    columns: Dict[str, Dict[str, Any]] = {}
    for name in fieldnames:
        values = [row.get(name, "").strip() for row in rows]
        present = [value for value in values if value]
        numeric_values = [_number(value) for value in present]
        is_numeric = bool(present) and all(value is not None for value in numeric_values)
        report: Dict[str, Any] = {
            "missing": len(values) - len(present),
            "unique": len(set(present)),
            "inferred_type": "numeric" if is_numeric else "categorical",
        }
        if is_numeric:
            numbers = [value for value in numeric_values if value is not None]
            report["summary"] = {
                "min": min(numbers),
                "max": max(numbers),
                "mean": statistics.fmean(numbers),
                "median": statistics.median(numbers),
            }
        else:
            report["most_common"] = Counter(present).most_common(5)
        columns[name] = report

    group_sizes: Dict[str, Dict[str, int]] = {}
    for name in groups:
        values = (row.get(name, "").strip() or "<missing>" for row in rows)
        group_sizes[name] = dict(sorted(Counter(values).items()))

    return {"input": str(path), "rows": len(rows), "columns": columns, "group_sizes": group_sizes}


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="Input CSV path; the file is never modified.")
    parser.add_argument("--group", action="append", default=[], help="Categorical grouping column; repeat as needed.")
    parser.add_argument("--delimiter", default=",", help="CSV delimiter (default: comma).")
    parser.add_argument("--output", type=Path, help="Write JSON report to this path instead of stdout.")
    args = parser.parse_args(argv)
    try:
        report = profile_csv(args.input, args.group, args.delimiter)
    except (OSError, ValueError, csv.Error) as error:
        parser.error(str(error))
    text = json.dumps(report, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
