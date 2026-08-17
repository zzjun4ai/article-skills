#!/usr/bin/env python3
"""Normalize line-oriented UTF-8 records into deterministic JSON."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def normalize(source: Path) -> dict[str, object]:
    seen: set[str] = set()
    records: list[str] = []
    duplicates = 0
    for raw in source.read_text(encoding="utf-8").splitlines():
        record = raw.strip()
        if not record:
            continue
        if record in seen:
            duplicates += 1
            continue
        seen.add(record)
        records.append(record)
    return {
        "source": str(source),
        "record_count": len(records),
        "duplicate_count": duplicates,
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    result = normalize(args.input)
    rendered = json.dumps(result, indent=2, ensure_ascii=False) + "\n"
    if args.dry_run:
        print(rendered, end="")
        return 0

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(rendered, encoding="utf-8")
    print(f"wrote {args.output} ({result['record_count']} records)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
