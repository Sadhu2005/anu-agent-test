import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from labapp import greet


class TestGreet(unittest.TestCase):
    def test_default(self):
        self.assertEqual(greet(), "hello, world")

    def test_name(self):
        self.assertEqual(greet("anu"), "hello, anu")


if __name__ == "__main__":
    unittest.main()
