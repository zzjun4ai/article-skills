import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "check_manuscript_refs.py"


class ScriptTests(unittest.TestCase):
    def test_common_references_are_counted(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "manuscript.md"
            path.write_text("See Figure 1, Table 2, and references [1, 3].", encoding="utf-8")
            result = subprocess.run([sys.executable, str(SCRIPT), str(path)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        references = json.loads(result.stdout)["references"]
        self.assertEqual(references["figures"], 1)
        self.assertEqual(references["tables"], 1)
        self.assertEqual(references["numbered_citations"], 1)

    def test_empty_document_is_valid_but_reports_zero(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "empty.md"
            path.write_text("", encoding="utf-8")
            result = subprocess.run([sys.executable, str(SCRIPT), str(path)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        self.assertEqual(sum(json.loads(result.stdout)["references"].values()), 0)

    def test_unresolved_placeholder_is_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "draft.md"
            path.write_text("AUTHOR_INPUT_NEEDED: sample size", encoding="utf-8")
            result = subprocess.run([sys.executable, str(SCRIPT), str(path)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        self.assertEqual(json.loads(result.stdout)["unresolved_placeholders"], 1)
