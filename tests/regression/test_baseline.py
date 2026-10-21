"""Regression: prior baseline greetings must stay stable."""

import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from labapp import greet


class TestRegressionBaseline(unittest.TestCase):
    def test_world_still_works(self):
        self.assertEqual(greet(), "Hello, world!")


if __name__ == "__main__":
    unittest.main()
