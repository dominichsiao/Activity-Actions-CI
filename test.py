import unittest
import example


class TestCase(unittest.TestCase):

    def test_add_1(self):
        self.assertEqual(example.add(1, 4), 5)

    def test_subtract_1(self):
        self.assertEqual(example.subtract(3, 1), 2)


if __name__ == '__main__':
    unittest.main()
