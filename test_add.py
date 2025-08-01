import unittest
from add import add

class TestAddFunction(unittest.TestCase):
    def test_add_integers(self):
        self.assertEqual(add(2, 3), "The sum of 2 and 3 is 5.")

    def test_add_negatives(self):
        self.assertEqual(add(-2, -4), "The sum of -2 and -4 is -6.")

    def test_add_zero(self):
        self.assertEqual(add(0, 0), "The sum of 0 and 0 is 0.")
    print("All tests passed!")

if __name__ == '__main__':
    unittest.main()
