"""Check completeness of a CSV point-by-point response matrix."""

import argparse
import csv
import json
import sys
from pathlib import Path


REQUIRED = ("comment_id", "comment", "status", "response", "location")
STATUSES = {"accepted", "partial", "clarified", "disputed", "author-input-needed"}
EVIDENCE_STATES = {"verified", "author-input-needed", "not-applicable"}


def check(path: Path) -> tuple[dict, int]:
    errors = []
    with path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        missing = [field for field in REQUIRED if field not in (reader.fieldnames or [])]
        if missing:
            return {"rows": 0, "errors": ["missing columns: " + ", ".join(missing)]}, 2
        rows = list(reader)
    ids = [row["comment_id"].strip() for row in rows]
    for line, row in enumerate(rows, start=2):
        for field in REQUIRED:
            if not row[field].strip() and not (field == "location" and row["status"].strip().lower() == "author-input-needed"):
                errors.append(f"line {line}: missing {field}")
        if row["status"].strip().lower() not in STATUSES:
            errors.append(f"line {line}: invalid status {row['status']!r}")
        evidence_status = row.get("evidence_status", "").strip().lower()
        if evidence_status and evidence_status not in EVIDENCE_STATES:
            errors.append(f"line {line}: invalid evidence_status {evidence_status!r}")
    duplicates = sorted({item for item in ids if item and ids.count(item) > 1})
    if duplicates:
        errors.append("duplicate comment_id: " + ", ".join(duplicates))
    unresolved = sum(row["status"].strip().lower() == "author-input-needed" for row in rows)
    return {"rows": len(rows), "unresolved": unresolved, "ready": not errors and unresolved == 0, "errors": errors}, 2 if errors else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    try:
        report, code = check(args.input)
    except (OSError, UnicodeError, csv.Error) as exc:
        parser.error(str(exc))
    json.dump(report, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
