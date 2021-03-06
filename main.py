import unittest
from stack import Stack

class TestStackMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())



    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_stack_push_returns_true(self):
        s = Stack()
        self.assertEqual(s.push(), True)

    def test_stack_remove(self):
        s = Stack()
        self.assertEqual(s.remove(), True)

    def test_reflection(self):
        s = Stack()
        self.assertEqual(s.reflect('test'), 'test')

    def test_count_ones3(self):
        s = Stack()
        self.assertEqual(s.count_ones([0,1,1,1,0]), 3)

    def test_count_ones2(self):
        s = Stack()
        self.assertEqual(s.count_ones([0,1,1,0,0]), 2)

    def test_count_ones0(self):
        s = Stack()
        self.assertEqual(s.count_ones([0,0,0,0,0,0]), 0)

if __name__ == '__main__':
    unittest.main()


