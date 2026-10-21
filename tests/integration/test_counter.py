import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from labapp.counter import Counter


class TestCounterIntegration(unittest.TestCase):
    def test_inc_chain(self):
        c = Counter()
        self.assertEqual(c.inc(), 1)
        self.assertEqual(c.inc(2), 3)
        c.reset()
        self.assertEqual(c.value, 0)


if __name__ == "__main__":
    unittest.main()
