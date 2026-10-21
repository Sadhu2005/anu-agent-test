import unittest
from todo import TodoList

class TestTodo(unittest.TestCase):
    def test_add_and_list(self):
        t = TodoList()
        t.add('a')
        self.assertEqual(t.list(), ['a'])

if __name__ == '__main__':
    unittest.main()
