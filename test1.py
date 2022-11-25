import unittest

from subtraction import subtract

class TestSub(unittest.TestCase):
    def test_list_int(self):
        """
        Test case to subtract two numbers
        """
        a=20
        b=30
        result = subtract(a,b)
        self.assertEqual(result, -10)

if __name__ == '__main__':
    unittest.main()
