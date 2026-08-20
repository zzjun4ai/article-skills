import re
import unittest
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]


class SkillContractTests(unittest.TestCase):
    def test_frontmatter_name_matches_directory(self):
        text = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
        match = re.search(r"\A---\s*\nname:\s*([^\n]+)", text)
        self.assertIsNotNone(match)
        self.assertEqual(match.group(1).strip(), SKILL_ROOT.name)

    def test_contract_states_workflow_output_and_failure_behavior(self):
        text = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
        for heading in ("## Shortest successful workflow", "## Output contract", "## Failure behavior"):
            self.assertIn(heading, text)

    def test_description_has_trigger_and_boundary(self):
        text = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
        description = re.search(r"description: >-\n((?:  .+\n)+)---", text).group(1)
        description = " ".join(description.split())
        self.assertIn("Use ", description)
        self.assertIn("not ", description.lower())

    def test_full_reader_has_equation_and_package_qa(self):
        text = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("equation-and-figure-grounding.md", text)
        self.assertIn("validate_reader_package.py", text)
        output = (SKILL_ROOT / "references" / "output-contract.md").read_text(encoding="utf-8")
        self.assertIn("top-level `blocks` list", output)
        self.assertIn('"output_anchor"', output)


if __name__ == "__main__":
    unittest.main()
