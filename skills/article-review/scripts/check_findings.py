"""Validate a JSON list of structured manuscript-review findings."""

import argparse
import json
import sys
from pathlib import Path


REQUIRED = ("id", "severity", "location", "evidence", "consequence", "request")
SEVERITIES = {"fatal", "major", "minor", "suggestion"}


def check(path: Path) -> tuple[dict, int]:
    try:
        findings = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        return {"findings": 0, "errors": [str(exc)]}, 2
    errors = []
    if not isinstance(findings, list):
        return {"findings": 0, "errors": ["top-level JSON value must be a list"]}, 2
    ids = []
    for index, finding in enumerate(findings, start=1):
        if not isinstance(finding, dict):
            errors.append(f"finding {index}: must be an object")
            continue
        for field in REQUIRED:
            if not str(finding.get(field, "")).strip():
                errors.append(f"finding {index}: missing {field}")
        severity = str(finding.get("severity", "")).lower()
        ids.append(str(finding.get("id", "")).strip())
        if severity and severity not in SEVERITIES:
            errors.append(f"finding {index}: invalid severity {severity!r}")
        confidence = str(finding.get("confidence", "")).lower()
        if confidence and confidence not in {"high", "medium", "low"}:
            errors.append(f"finding {index}: invalid confidence {confidence!r}")
    duplicates = sorted({item for item in ids if item and ids.count(item) > 1})
    if duplicates:
        errors.append("duplicate finding ids: " + ", ".join(duplicates))
    return {"findings": len(findings), "errors": errors}, 2 if errors else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    report, code = check(args.input)
    json.dump(report, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
