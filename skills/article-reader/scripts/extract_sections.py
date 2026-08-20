"""Extract Markdown headings and their section text as JSON."""

import argparse
import json
import re
import sys
from pathlib import Path


HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.MULTILINE)


def extract(text: str) -> list[dict]:
    matches = list(HEADING.finditer(text))
    sections = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        start_line = text.count("\n", 0, match.start()) + 1
        end_line = text.count("\n", 0, end)
        if end == len(text) and not text.endswith("\n"):
            end_line += 1
        end_line = max(start_line, end_line)
        heading = match.group(2).strip()
        anchor = re.sub(r"[^a-z0-9]+", "-", heading.lower()).strip("-") or f"section-{index + 1}"
        sections.append({
            "level": len(match.group(1)),
            "heading": heading,
            "anchor": anchor,
            "start_line": start_line,
            "end_line": end_line,
            "text": text[match.end():end].strip(),
        })
    return sections


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    try:
        sections = extract(args.input.read_text(encoding="utf-8"))
    except (OSError, UnicodeError) as exc:
        parser.error(str(exc))
    json.dump({"file": str(args.input), "sections": sections}, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
