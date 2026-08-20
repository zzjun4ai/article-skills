"""Validate a JSON article-data manifest and print a readiness report."""

import argparse
import json
import sys
from pathlib import Path


ROUTES = {
    "public-repository", "controlled-access", "within-article", "reused-public",
    "third-party-restricted", "justified-request", "not-applicable",
}
REQUIRED = ("id", "description", "supports", "access_route", "status")
STATUSES = {"complete", "planned", "pending", "not-applicable"}


def validate(path: Path) -> tuple[dict, int]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        return {"datasets": 0, "errors": [str(exc)], "ready": False}, 2
    datasets = payload.get("datasets") if isinstance(payload, dict) else None
    if not isinstance(datasets, list):
        return {"datasets": 0, "errors": ["top-level datasets must be a list"], "ready": False}, 2
    errors: list[str] = []
    ids: list[str] = []
    for index, item in enumerate(datasets, start=1):
        if not isinstance(item, dict):
            errors.append(f"dataset {index}: must be an object")
            continue
        for field in REQUIRED:
            if not item.get(field):
                errors.append(f"dataset {index}: missing {field}")
        dataset_id = str(item.get("id", "")).strip()
        ids.append(dataset_id)
        route = str(item.get("access_route", "")).strip()
        status = str(item.get("status", "")).strip()
        if "supports" in item and not isinstance(item["supports"], list):
            errors.append(f"dataset {index}: supports must be a list")
        if route and route not in ROUTES:
            errors.append(f"dataset {index}: invalid access_route {route!r}")
        if status and status not in STATUSES:
            errors.append(f"dataset {index}: invalid status {status!r}")
        if route in {"public-repository", "reused-public"} and status == "complete":
            if not item.get("location") and not item.get("identifier"):
                errors.append(f"dataset {index}: completed public route needs location or identifier")
    duplicates = sorted({item for item in ids if item and ids.count(item) > 1})
    if duplicates:
        errors.append("duplicate dataset ids: " + ", ".join(duplicates))
    return {"datasets": len(datasets), "errors": errors, "ready": not errors}, 2 if errors else 0


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
