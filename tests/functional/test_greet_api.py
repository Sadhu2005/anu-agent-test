"""Functional: greet behaves as a stable public API."""

import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from labapp import greet


class TestGreetFunctional(unittest.TestCase):
    def test_api_contract(self):
        out = greet("lab")
        self.assertTrue(out.startswith("Hello,"))
        self.assertIn("lab", out)
        self.assertTrue(out.endswith("!"))


if __name__ == "__main__":
    unittest.main()
