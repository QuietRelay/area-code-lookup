"""README guard tests. Run with: python -m unittest"""

import unittest
from pathlib import Path


class ReadmePathGuidanceTests(unittest.TestCase):
    """The Windows PATH snippet must edit the User PATH only, never copy $env:PATH into it."""

    def windows_block(self):
        readme = (Path(__file__).with_name("README.md")).read_text(encoding="utf-8")
        return readme, readme.split("**Windows (PowerShell or cmd):**")[1].split("```powershell")[1].split("```")[0]

    def test_windows_snippet_reads_only_the_user_path_and_checks_first(self):
        readme, block = self.windows_block()
        self.assertNotIn("$env:PATH", block)
        self.assertNotIn("$env:Path", block)
        self.assertIn("GetEnvironmentVariable('Path', 'User')", block)
        self.assertIn("-notcontains", block)
        self.assertEqual(block.count("SetEnvironmentVariable("), 1)
        self.assertIn("'User')", block)
        self.assertLess(block.index("-notcontains"), block.index("SetEnvironmentVariable("))
        self.assertIn("open a new terminal", readme.lower())
        self.assertIn("setx", readme)   # the truncation warning stays


if __name__ == "__main__":
    unittest.main()
