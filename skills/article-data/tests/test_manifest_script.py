import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "validate_data_manifest.py"


class ManifestScriptTests(unittest.TestCase):
    def run_script(self, payload):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "manifest.json"
            path.write_text(json.dumps(payload), encoding="utf-8")
            return subprocess.run([sys.executable, str(SCRIPT), str(path)], capture_output=True, text=True)

    def test_complete_public_dataset_passes(self):
        payload = {"datasets": [{"id": "D1", "description": "source data", "supports": ["Fig. 1"], "access_route": "public-repository", "status": "complete", "identifier": "doi:10.1/example"}]}
        result = self.run_script(payload)
        self.assertEqual(result.returncode, 0)
        self.assertTrue(json.loads(result.stdout)["ready"])

    def test_completed_public_dataset_needs_location(self):
        payload = {"datasets": [{"id": "D1", "description": "source data", "supports": ["Fig. 1"], "access_route": "public-repository", "status": "complete"}]}
        result = self.run_script(payload)
        self.assertEqual(result.returncode, 2)

    def test_supports_must_be_a_list(self):
        payload = {"datasets": [{"id": "D1", "description": "source data", "supports": "Fig. 1", "access_route": "within-article", "status": "complete"}]}
        result = self.run_script(payload)
        self.assertEqual(result.returncode, 2)
