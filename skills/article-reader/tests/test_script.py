import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "extract_sections.py"


class ScriptTests(unittest.TestCase):
    def test_sections_are_extracted_in_order(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "paper.md"
            path.write_text("# Intro\nclaim\n## Methods\nprotocol\n", encoding="utf-8")
            result = subprocess.run([sys.executable, str(SCRIPT), str(path)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        sections = json.loads(result.stdout)["sections"]
        self.assertEqual([section["heading"] for section in sections], ["Intro", "Methods"])
        self.assertEqual(sections[0]["anchor"], "intro")
        self.assertEqual(sections[0]["start_line"], 1)
        self.assertEqual(sections[0]["end_line"], 2)

    def test_document_without_headings_returns_empty_map(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "plain.md"
            path.write_text("plain text", encoding="utf-8")
            result = subprocess.run([sys.executable, str(SCRIPT), str(path)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        self.assertEqual(json.loads(result.stdout)["sections"], [])
