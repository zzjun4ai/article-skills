import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "validate_reader_package.py"


class ReaderPackageTests(unittest.TestCase):
    def run_package(self, paper, source_map, *args):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            paper_path = root / "paper.md"
            map_path = root / "source_map.json"
            paper_path.write_text(paper, encoding="utf-8")
            map_path.write_text(json.dumps(source_map), encoding="utf-8")
            return subprocess.run(
                [sys.executable, str(SCRIPT), str(paper_path), "--source-map", str(map_path), *args],
                capture_output=True,
                text=True,
            )

    def test_grounded_package_passes_strict(self):
        source_map = {"blocks": [{
            "id": "B1", "type": "section", "source_anchor": "p.1",
            "confidence": "high", "output_anchor": "introduction",
        }]}
        result = self.run_package("# Introduction\nGrounded text.\n", source_map, "--strict")
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertTrue(json.loads(result.stdout)["ready"])

    def test_unknown_anchor_and_unbalanced_math_fail(self):
        source_map = {"blocks": [{
            "id": "B1", "type": "equation", "source_anchor": "p.2",
            "confidence": "medium", "output_anchor": "missing",
        }]}
        result = self.run_package("# Results\n$$x = 1\n", source_map)
        self.assertEqual(result.returncode, 2)
        report = json.loads(result.stdout)
        self.assertGreaterEqual(len(report["errors"]), 2)


if __name__ == "__main__":
    unittest.main()

