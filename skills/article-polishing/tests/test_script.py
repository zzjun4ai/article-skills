import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "check_terminology.py"


class ScriptTests(unittest.TestCase):
    def test_variant_is_counted(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "text.txt"
            path.write_text("Colour is useful. colour improves contrast.", encoding="utf-8")
            result = subprocess.run([sys.executable, str(SCRIPT), str(path), "--term", "color=colour"], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        self.assertEqual(json.loads(result.stdout)["terms"]["color"]["count"], 2)

    def test_malformed_term_fails(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "text.txt"
            path.write_text("text", encoding="utf-8")
            result = subprocess.run([sys.executable, str(SCRIPT), str(path), "--term", "colour"], capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)
