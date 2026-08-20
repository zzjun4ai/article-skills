"""Find configured terminology variants in a text file."""

import argparse
import json
import re
import sys
from pathlib import Path


def check(text: str, terms: list[str]) -> dict:
    result = {}
    for item in terms:
        if "=" not in item:
            raise ValueError(f"term must use canonical=variant: {item!r}")
        canonical, variant = (part.strip() for part in item.split("=", 1))
        if not canonical or not variant:
            raise ValueError(f"term must have two non-empty values: {item!r}")
        result[canonical] = {"variant": variant, "count": len(re.findall(re.escape(variant), text, re.IGNORECASE))}
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--term", action="append", default=[], help="canonical=variant")
    args = parser.parse_args()
    try:
        text = args.input.read_text(encoding="utf-8")
        report = check(text, args.term)
    except (OSError, UnicodeError, ValueError) as exc:
        parser.error(str(exc))
    json.dump({"file": str(args.input), "terms": report}, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
