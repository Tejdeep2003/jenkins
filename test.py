#!/usr/bin/python3

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
    
    def test_list_int1(self):
        """
        Test case to subtract two numbers
        """
        a=50
        b=30
        result = subtract(a,b)
        self.assertEqual(result, 20)

    def test_list_int3(self):
        """
        Test case to subtract two numbers
        """
        a=553
        b=53
        result = subtract(a,b)
        self.assertEqual(result, 500)

    def test_list_int4(self):
        """
        Test case to subtract two numbers
        """
        a=30
        b=30
        result = subtract(a,b)
        self.assertEqual(result, 10)

    def test_list_int5(self):
        """
        Test case to subtract two numbers
        """
        a=60
        b=30
        result = subtract(a,b)
        self.assertEqual(result, 20)


if __name__ == '__main__':
    unittest.main()
