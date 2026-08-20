"""Count common figure, table, and numbered citation references in Markdown."""

import argparse
import json
import re
import sys
from pathlib import Path


PATTERNS = {
    "figures": r"\b(?:Figure|Fig\.)\s*[A-Za-z]?\d+",
    "tables": r"\bTable\s*[A-Za-z]?\d+",
    "numbered_citations": r"\[\d+(?:\s*[-,]\s*\d+)*\]",
    "latex_citations": r"\\cite[a-zA-Z]*\{[^}]+\}",
}
PLACEHOLDER_PATTERN = re.compile(r"AUTHOR_INPUT_NEEDED|\[TODO(?::[^\]]*)?\]|\{\{[^}]+\}\}", re.IGNORECASE)


def check(text: str) -> dict:
    references = {name: len(re.findall(pattern, text, flags=re.IGNORECASE)) for name, pattern in PATTERNS.items()}
    return {"references": references, "unresolved_placeholders": len(PLACEHOLDER_PATTERN.findall(text))}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    try:
        report = check(args.input.read_text(encoding="utf-8"))
    except (OSError, UnicodeError) as exc:
        parser.error(str(exc))
    json.dump({"file": str(args.input), **report}, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
