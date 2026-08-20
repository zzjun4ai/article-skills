"""Profile a CSV table using only the Python standard library."""

import argparse
import csv
import json
import sys
from pathlib import Path


def profile(path: Path) -> dict:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames:
            raise ValueError("CSV has no header row")
        rows = list(reader)
    columns = reader.fieldnames
    missing = {column: sum(not row.get(column, "").strip() for row in rows) for column in columns}
    numeric = {}
    for column in columns:
        values = [row.get(column, "").strip() for row in rows if row.get(column, "").strip()]
        numeric[column] = bool(values) and all(_is_number(value) for value in values)
    return {"file": str(path), "rows": len(rows), "columns": columns, "missing": missing, "numeric": numeric}


def _is_number(value: str) -> bool:
    try:
        float(value)
    except ValueError:
        return False
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    try:
        report = profile(args.input)
    except (OSError, UnicodeError, csv.Error, ValueError) as exc:
        parser.error(str(exc))
    json.dump(report, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
