import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "validate_references.py"


class ScriptTests(unittest.TestCase):
    def run_script(self, content):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "refs.csv"
            path.write_text(content, encoding="utf-8")
            return subprocess.run([sys.executable, str(SCRIPT), str(path)], capture_output=True, text=True)

    def test_valid_table(self):
        result = self.run_script("key,title,year,source_type,support_level,verification_status\na,Paper,2024,primary,direct,partial\n")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(json.loads(result.stdout)["rows"], 1)

    def test_duplicate_key_fails(self):
        result = self.run_script("key,title,year,source_type,support_level,verification_status\na,P1,2024,primary,direct,partial\na,P2,2024,review,contextual,partial\n")
        self.assertEqual(result.returncode, 2)

    def test_malformed_doi_fails(self):
        result = self.run_script("key,title,year,source_type,support_level,verification_status,doi\na,Paper,2024,primary,direct,verified,not-a-doi\n")
        self.assertEqual(result.returncode, 2)
