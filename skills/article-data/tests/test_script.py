import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "profile_table.py"


class ScriptTests(unittest.TestCase):
    def test_profile_reports_missing_and_numeric_columns(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "data.csv"
            path.write_text("id,value,note\na,1,ok\nb,,\n", encoding="utf-8")
            result = subprocess.run([sys.executable, str(SCRIPT), str(path)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        report = json.loads(result.stdout)
        self.assertEqual(report["rows"], 2)
        self.assertEqual(report["missing"]["value"], 1)
        self.assertTrue(report["numeric"]["value"])

    def test_headerless_file_fails(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "empty.csv"
            path.write_text("", encoding="utf-8")
            result = subprocess.run([sys.executable, str(SCRIPT), str(path)], capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)
