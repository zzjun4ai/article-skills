import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "check_figure_manifest.py"


class ManifestScriptTests(unittest.TestCase):
    def run_script(self, content):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "manifest.yaml"
            path.write_text(content, encoding="utf-8")
            return subprocess.run([sys.executable, str(SCRIPT), str(path)], capture_output=True, text=True)

    def test_complete_core_fields_pass(self):
        result = self.run_script('figure_id: "Fig_1"\ntarget: "journal"\nbackend: "python-matplotlib"\nclaim: "A exceeds B"\n')
        self.assertEqual(result.returncode, 0)
        self.assertTrue(json.loads(result.stdout)["ready"])

    def test_empty_claim_fails(self):
        result = self.run_script('figure_id: "Fig_1"\ntarget: "journal"\nbackend: "python-matplotlib"\nclaim: ""\n')
        self.assertEqual(result.returncode, 2)
