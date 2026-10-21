import unittest

from labapp import greet


class TestGreet(unittest.TestCase):
    def test_greet_default(self):
        self.assertEqual(greet(), "Hello, world!")

    def test_greet_name(self):
        self.assertEqual(greet("Ada"), "Hello, Ada!")


if __name__ == '__main__':
    unittest.main()
