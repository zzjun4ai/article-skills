"""Validate a small CSV reference table and print a JSON report."""

import argparse
import csv
import json
import re
import sys
from pathlib import Path


REQUIRED = ("key", "title", "year", "source_type", "support_level", "verification_status")
SOURCE_TYPES = {"primary", "review", "method", "dataset", "software"}
SUPPORT_LEVELS = {"direct", "contextual", "insufficient"}
VERIFICATION_STATES = {"verified", "partial", "unverified"}
DOI_PATTERN = re.compile(r"^10\.\d{4,9}/\S+$", re.IGNORECASE)


def validate(path: Path) -> tuple[dict, int]:
    errors: list[str] = []
    warnings: list[str] = []
    rows = []
    try:
        with path.open(newline="", encoding="utf-8-sig") as handle:
            reader = csv.DictReader(handle)
            fields = reader.fieldnames or []
            missing_columns = [field for field in REQUIRED if field not in fields]
            if missing_columns:
                errors.append("missing columns: " + ", ".join(missing_columns))
            for line, row in enumerate(reader, start=2):
                rows.append(row)
                for field in REQUIRED:
                    if not row.get(field, "").strip():
                        errors.append(f"line {line}: missing {field}")
                year = row.get("year", "").strip()
                if year and (not year.isdigit() or not 1800 <= int(year) <= 2100):
                    errors.append(f"line {line}: invalid year {year!r}")
                source_type = row.get("source_type", "").strip().lower()
                if source_type and source_type not in SOURCE_TYPES:
                    errors.append(f"line {line}: unknown source_type {source_type!r}")
                support = row.get("support_level", "").strip().lower()
                if support and support not in SUPPORT_LEVELS:
                    errors.append(f"line {line}: unknown support_level {support!r}")
                verification = row.get("verification_status", "").strip().lower()
                if verification and verification not in VERIFICATION_STATES:
                    errors.append(f"line {line}: unknown verification_status {verification!r}")
                doi = row.get("doi", "").strip()
                doi = re.sub(r"^(?:https?://doi\.org/|doi:\s*)", "", doi, flags=re.IGNORECASE)
                if doi and not DOI_PATTERN.match(doi):
                    errors.append(f"line {line}: malformed DOI {row.get('doi')!r}")
                if verification == "verified" and not doi and not row.get("url", "").strip():
                    warnings.append(f"line {line}: verified row has no DOI or URL")
    except (OSError, UnicodeError, csv.Error) as exc:
        errors.append(str(exc))
    keys = [row.get("key", "").strip() for row in rows]
    duplicates = sorted({key for key in keys if key and keys.count(key) > 1})
    if duplicates:
        errors.append("duplicate keys: " + ", ".join(duplicates))
    if not rows and not errors:
        warnings.append("reference table is empty")
    report = {"file": str(path), "rows": len(rows), "errors": errors, "warnings": warnings}
    return report, 2 if errors else 0


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
