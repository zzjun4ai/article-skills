"""Validate a Markdown reader and optional JSON source map without modifying them."""

import argparse
import json
import re
import sys
from pathlib import Path


HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.MULTILINE)
REQUIRED_BLOCK_FIELDS = ("id", "type", "source_anchor", "confidence", "output_anchor")
CONFIDENCE = {"high", "medium", "low"}


def anchors(text: str) -> set[str]:
    result = set()
    for index, match in enumerate(HEADING.finditer(text), start=1):
        value = re.sub(r"[^a-z0-9]+", "-", match.group(2).lower()).strip("-")
        result.add(value or f"section-{index}")
    return result


def validate(paper: str, source_map: object | None) -> dict:
    errors: list[str] = []
    warnings: list[str] = []
    paper_anchors = anchors(paper)
    if not paper_anchors:
        warnings.append("paper has no Markdown headings")
    if paper.count("$$") % 2:
        errors.append("unbalanced $$ display-math delimiters")
    if paper.count("\\[") != paper.count("\\]"):
        errors.append("unbalanced \\[ and \\] display-math delimiters")
    if re.search(r"SOURCE_GAP|LOW_CONFIDENCE|AUTHOR_INPUT_NEEDED", paper, re.I):
        warnings.append("reader contains unresolved source or confidence markers")

    block_count = 0
    if source_map is not None:
        blocks = source_map.get("blocks") if isinstance(source_map, dict) else None
        if not isinstance(blocks, list):
            errors.append("source map must contain a top-level blocks list")
        else:
            block_count = len(blocks)
            ids: list[str] = []
            for index, block in enumerate(blocks, start=1):
                if not isinstance(block, dict):
                    errors.append(f"block {index}: must be an object")
                    continue
                for field in REQUIRED_BLOCK_FIELDS:
                    if not str(block.get(field, "")).strip():
                        errors.append(f"block {index}: missing {field}")
                block_id = str(block.get("id", "")).strip()
                ids.append(block_id)
                confidence = str(block.get("confidence", "")).strip().lower()
                if confidence and confidence not in CONFIDENCE:
                    errors.append(f"block {index}: invalid confidence {confidence!r}")
                output_anchor = str(block.get("output_anchor", "")).strip().lstrip("#")
                if output_anchor and output_anchor not in paper_anchors:
                    errors.append(f"block {index}: unknown output_anchor {output_anchor!r}")
            duplicates = sorted({item for item in ids if item and ids.count(item) > 1})
            if duplicates:
                errors.append("duplicate block ids: " + ", ".join(duplicates))

    return {
        "headings": len(paper_anchors),
        "blocks": block_count,
        "errors": errors,
        "warnings": warnings,
        "ready": not errors,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paper", type=Path)
    parser.add_argument("--source-map", type=Path)
    parser.add_argument("--strict", action="store_true", help="treat warnings as failures")
    args = parser.parse_args()
    try:
        paper = args.paper.read_text(encoding="utf-8")
        source_map = json.loads(args.source_map.read_text(encoding="utf-8")) if args.source_map else None
        report = validate(paper, source_map)
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        report = {"headings": 0, "blocks": 0, "errors": [str(exc)], "warnings": [], "ready": False}
    report["paper"] = str(args.paper)
    report["ready"] = report["ready"] and not (args.strict and report["warnings"])
    json.dump(report, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")
    return 0 if report["ready"] else 2


if __name__ == "__main__":
    raise SystemExit(main())

