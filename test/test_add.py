import unittest
import xmlrunner
from add import add  # make sure your function is in add.py

class TestAdd(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(add(2, 3), "The sum of 2 and 3 is 5.")

    def test_negative_numbers(self):
        self.assertEqual(add(-1, -2), "The sum of -1 and -2 is -3.")

    def test_zero(self):
        self.assertEqual(add(0, 0), "The sum of 0 and 0 is 0.")

if __name__ == '__main__':
    with open('test-reports/results.xml', 'wb') as output:
        unittest.main(
            testRunner=xmlrunner.XMLTestRunner(output=output),
            verbosity=2,
            exit=False
        )
