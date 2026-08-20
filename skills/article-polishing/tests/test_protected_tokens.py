import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "compare_protected_tokens.py"


class ProtectedTokenTests(unittest.TestCase):
    def run_script(self, original, revised):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            before, after = root / "before.txt", root / "after.txt"
            before.write_text(original, encoding="utf-8")
            after.write_text(revised, encoding="utf-8")
            return subprocess.run([sys.executable, str(SCRIPT), str(before), str(after)], capture_output=True, text=True)

    def test_rewording_with_same_tokens_passes(self):
        result = self.run_script("We observed 12 samples \\cite{x}.", "Across 12 samples, we observed this result \\cite{x}.")
        self.assertEqual(result.returncode, 0)
        self.assertTrue(json.loads(result.stdout)["pass"])

    def test_changed_number_fails(self):
        result = self.run_script("n = 12", "n = 14")
        self.assertEqual(result.returncode, 2)
        self.assertIn("numbers", json.loads(result.stdout)["changes"])
