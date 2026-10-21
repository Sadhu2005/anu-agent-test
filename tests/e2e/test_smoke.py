"""Lightweight e2e: import package and exercise public surface."""

import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from labapp import greet, __version__
from labapp.counter import Counter


class TestE2ESmoke(unittest.TestCase):
    def test_package_smoke(self):
        self.assertTrue(__version__)
        self.assertEqual(greet("e2e"), "hello, e2e")
        self.assertEqual(Counter(1).inc(), 2)


if __name__ == "__main__":
    unittest.main()
