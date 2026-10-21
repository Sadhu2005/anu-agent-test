"""E2E smoke for labapp package."""

import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from labapp import greet


class TestE2ESmoke(unittest.TestCase):
    def test_package_smoke(self):
        self.assertEqual(greet("e2e"), "Hello, e2e!")


if __name__ == "__main__":
    unittest.main()
