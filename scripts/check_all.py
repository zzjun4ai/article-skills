"""Validate every published skill and run its tests."""

import os
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def validate_contract(skill_root: Path) -> list[str]:
    skill_file = skill_root / "SKILL.md"
    errors: list[str] = []
    if not skill_file.is_file():
        return [f"{skill_root.name}: missing SKILL.md"]
    text = skill_file.read_text(encoding="utf-8")
    frontmatter = re.match(r"\A---\s*\n(.*?)\n---", text, re.DOTALL)
    if not frontmatter:
        errors.append(f"{skill_root.name}: invalid frontmatter block")
        return errors
    keys = re.findall(r"^([a-zA-Z0-9_-]+):", frontmatter.group(1), re.MULTILINE)
    unexpected = sorted(set(keys) - {"name", "description"})
    if unexpected:
        errors.append(f"{skill_root.name}: unexpected frontmatter keys: {', '.join(unexpected)}")
    if "description" not in keys:
        errors.append(f"{skill_root.name}: missing description")
    name = re.search(r"\A---\s*\nname:\s*([^\n]+)", text)
    if not name or name.group(1).strip() != skill_root.name:
        errors.append(f"{skill_root.name}: frontmatter name does not match directory")
    if len(text.splitlines()) > 500:
        errors.append(f"{skill_root.name}: SKILL.md exceeds 500 lines")
    if re.search(r"\bTODO\b|\bTBD\b", text, re.IGNORECASE):
        errors.append(f"{skill_root.name}: unfinished TODO/TBD marker")
    for target in LINK.findall(text):
        if "://" in target or target.startswith("#"):
            continue
        target_path = (skill_root / target.split("#", 1)[0]).resolve()
        if not target_path.exists():
            errors.append(f"{skill_root.name}: broken local link {target}")
    return errors


def main() -> int:
    failures: list[str] = []
    skill_roots = sorted(path for path in SKILLS.iterdir() if path.is_dir())
    for skill_root in skill_roots:
        failures.extend(validate_contract(skill_root))
        tests = skill_root / "tests"
        if tests.is_dir():
            env = os.environ.copy()
            env["PYTHONDONTWRITEBYTECODE"] = "1"
            result = subprocess.run(
                [sys.executable, "-m", "unittest", "discover", "-s", str(tests), "-p", "test*.py", "-v"],
                cwd=ROOT,
                env=env,
            )
            if result.returncode:
                failures.append(f"{skill_root.name}: tests failed")
    if failures:
        for failure in failures:
            print(f"FAIL: {failure}", file=sys.stderr)
        return 1
    print(f"PASS: {len(skill_roots)} skills validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
