import re
import unittest
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]


class SkillContractTests(unittest.TestCase):
    def test_frontmatter_name_matches_directory(self) -> None:
        skill = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
        match = re.search(r"\A---\s*\nname:\s*([^\n]+)", skill)
        self.assertIsNotNone(match)
        self.assertEqual(match.group(1).strip(), SKILL_ROOT.name)

    def test_matplotlib_is_the_only_rendering_backend(self) -> None:
        skill = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("Python with Matplotlib", skill)
        self.assertIn("Do not switch to R, Plotly", skill)
        self.assertIn("matplotlib-vector-workflow.md", skill)

    def test_vector_workflow_preserves_editable_output(self) -> None:
        workflow = (SKILL_ROOT / "references" / "matplotlib-vector-workflow.md").read_text(encoding="utf-8")
        self.assertIn('"pdf.fonttype": 42', workflow)
        self.assertIn('"svg.fonttype": "none"', workflow)
        self.assertIn("fig.savefig", workflow)

    def test_contract_exposes_output_and_failure_semantics(self) -> None:
        skill = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("## Output contract", skill)
        self.assertIn("## Failure behavior", skill)
        self.assertIn("image-guided-reproduction.md", skill)

    def test_template_adaptation_and_static_preflight_are_routed(self) -> None:
        skill = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("template-adaptation-and-panel-qa.md", skill)
        self.assertIn("audit_plot_source.py", skill)


if __name__ == "__main__":
    unittest.main()
