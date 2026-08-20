"""Compare protected scientific tokens between original and revised text."""

import argparse
import collections
import json
import re
import sys
from pathlib import Path


PATTERNS = {
    "numbers": r"(?<![A-Za-z])[-+]?\d+(?:\.\d+)?(?:e[-+]?\d+)?%?",
    "citations": r"\\cite[a-zA-Z]*\{[^}]+\}",
    "cross_references": r"\\(?:ref|eqref|autoref)\{[^}]+\}",
    "labels": r"\\label\{[^}]+\}",
}


def extract(text: str) -> dict[str, collections.Counter]:
    return {name: collections.Counter(re.findall(pattern, text, re.IGNORECASE)) for name, pattern in PATTERNS.items()}


def compare(original: str, revised: str) -> dict:
    before, after = extract(original), extract(revised)
    changes = {}
    for name in PATTERNS:
        removed = list((before[name] - after[name]).elements())
        added = list((after[name] - before[name]).elements())
        if removed or added:
            changes[name] = {"removed": removed, "added": added}
    return {"pass": not changes, "changes": changes}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("original", type=Path)
    parser.add_argument("revised", type=Path)
    args = parser.parse_args()
    try:
        report = compare(args.original.read_text(encoding="utf-8"), args.revised.read_text(encoding="utf-8"))
    except (OSError, UnicodeError) as exc:
        parser.error(str(exc))
    json.dump(report, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")
    return 0 if report["pass"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
