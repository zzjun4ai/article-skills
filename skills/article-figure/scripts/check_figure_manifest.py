"""Validate required fields in an article-figure manifest without modifying it."""

import argparse
import json
import re
import sys
from pathlib import Path


REQUIRED_SCALARS = ("figure_id", "target", "backend", "claim")


def parse_simple_yaml(text: str) -> dict[str, str]:
    values: dict[str, str] = {}
    for line in text.splitlines():
        match = re.match(r"^([a-z_][a-z0-9_]*):\s*(.*)$", line)
        if match:
            values[match.group(1)] = match.group(2).strip().strip('"\'')
    return values


def validate(path: Path) -> tuple[dict, int]:
    try:
        values = parse_simple_yaml(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError) as exc:
        return {"file": str(path), "errors": [str(exc)]}, 2
    errors = [f"missing or empty field: {field}" for field in REQUIRED_SCALARS if not values.get(field)]
    if values.get("backend") and values["backend"] != "python-matplotlib":
        errors.append("backend must be python-matplotlib")
    return {"file": str(path), "errors": errors, "ready": not errors}, 2 if errors else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    report, code = validate(args.input)
    json.dump(report, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
