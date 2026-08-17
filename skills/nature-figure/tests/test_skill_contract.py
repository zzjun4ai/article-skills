import unittest
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]


class SkillContractTests(unittest.TestCase):
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
