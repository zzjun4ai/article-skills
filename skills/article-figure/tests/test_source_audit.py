import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "audit_plot_source.py"


class SourceAuditTests(unittest.TestCase):
    def run_script(self, content, *args):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "figure.py"
            path.write_text(content, encoding="utf-8")
            return subprocess.run(
                [sys.executable, str(SCRIPT), str(path), *args],
                capture_output=True,
                text=True,
            )

    def test_complete_matplotlib_bundle_passes_strict(self):
        source = """import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.plot([1, 2], [3, 4])
fig.savefig('figure.pdf')
fig.savefig('figure.png')
plt.close(fig)
"""
        result = self.run_script(source, "--strict")
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertTrue(json.loads(result.stdout)["ready"])

    def test_missing_vector_export_fails(self):
        source = "import matplotlib.pyplot as plt\nfig, ax = plt.subplots()\nfig.savefig('figure.png')\n"
        result = self.run_script(source)
        self.assertEqual(result.returncode, 2)
        self.assertIn("editable PDF or SVG", " ".join(json.loads(result.stdout)["errors"]))


if __name__ == "__main__":
    unittest.main()

