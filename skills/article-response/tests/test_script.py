import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "check_response_matrix.py"


class ScriptTests(unittest.TestCase):
    def run_script(self, content):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "response.csv"
            path.write_text(content, encoding="utf-8")
            return subprocess.run([sys.executable, str(SCRIPT), str(path)], capture_output=True, text=True)

    def test_complete_response_passes(self):
        result = self.run_script("comment_id,comment,status,response,location\nR1,Explain,accepted,Added detail,Methods\n")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(json.loads(result.stdout)["rows"], 1)

    def test_missing_location_fails(self):
        result = self.run_script("comment_id,comment,status,response,location\nR1,Explain,accepted,Added detail,\n")
        self.assertEqual(result.returncode, 2)

    def test_author_input_needed_is_valid_but_not_ready(self):
        result = self.run_script("comment_id,comment,status,response,location\nR1,Add control,author-input-needed,Provide control result,\n")
        self.assertEqual(result.returncode, 0)
        report = json.loads(result.stdout)
        self.assertFalse(report["ready"])
        self.assertEqual(report["unresolved"], 1)
