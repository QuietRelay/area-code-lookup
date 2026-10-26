"""README guard tests. Run with: python -m unittest"""

import unittest
from pathlib import Path


class ReadmePathGuidanceTests(unittest.TestCase):
    """The Windows PATH snippet must edit the User PATH only, never copy $env:PATH into it."""

    def windows_block(self):
        readme = (Path(__file__).with_name("README.md")).read_text(encoding="utf-8")
        return readme, readme.split("**Windows (PowerShell or cmd):**")[1].split("```powershell")[1].split("```")[0]

    def test_windows_snippet_edits_the_raw_user_value_and_checks_first(self):
        readme, block = self.windows_block()
        for bad in ("$env:PATH", "$env:Path", "GetEnvironmentVariable", "SetEnvironmentVariable", "QUIETRELAY_PATH_REFRESH"):
            self.assertNotIn(bad, block, bad)
        for good in ("CurrentUser.OpenSubKey($sub, $true)", "$sub = 'Environment'", "DoNotExpandEnvironmentNames",
                     "GetValueKind('Path')", "-notcontains", "$key.SetValue('Path', $new, $kind)",
                     "} finally {", "if ($key) { $key.Close() }"):
            self.assertIn(good, block, good)
        self.assertEqual(block.count("SetValue("), 1)
        self.assertLess(block.index("-notcontains"), block.index("SetValue("))
        self.assertLess(block.index("SetValue("), block.index("} finally {"))
        lower = readme.lower()
        self.assertIn("open a new terminal", lower)
        self.assertIn("sign out", lower)
        self.assertIn("setx", readme)   # the truncation warning stays


if __name__ == "__main__":
    unittest.main()
