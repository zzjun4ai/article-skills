import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "check_findings.py"


class ScriptTests(unittest.TestCase):
    def run_script(self, content):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "findings.json"
            path.write_text(content, encoding="utf-8")
            return subprocess.run([sys.executable, str(SCRIPT), str(path)], capture_output=True, text=True)

    def test_complete_finding_passes(self):
        result = self.run_script('[{"id":"F1","severity":"major","location":"Fig. 1","evidence":"label unclear","consequence":"result cannot be interpreted","request":"clarify"}]')
        self.assertEqual(result.returncode, 0)
        self.assertEqual(json.loads(result.stdout)["findings"], 1)

    def test_missing_request_fails(self):
        result = self.run_script('[{"id":"F1","severity":"major","location":"Fig. 1","evidence":"label unclear","consequence":"result cannot be interpreted"}]')
        self.assertEqual(result.returncode, 2)

    def test_duplicate_ids_fail(self):
        result = self.run_script('[{"id":"F1","severity":"minor","location":"p1","evidence":"x","consequence":"y","request":"z"},{"id":"F1","severity":"minor","location":"p2","evidence":"x","consequence":"y","request":"z"}]')
        self.assertEqual(result.returncode, 2)
