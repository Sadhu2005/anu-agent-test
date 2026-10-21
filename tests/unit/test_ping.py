import unittest

from labapp.ping import ping


class TestPing(unittest.TestCase):
    def test_ping_returns_pong(self):
        self.assertEqual(ping(), "pong")


if __name__ == '__main__':
    unittest.main()
