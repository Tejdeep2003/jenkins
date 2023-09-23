#! /usr/bin/python3
# Test case for adding 2 numbers

import unittest

from Prog1 import summation

class Testsum(unittest.TestCase):
    def test_list_init(self):
        """
        Test case to add 2 numbers
        """
        data = [32, 35]
        result = summation(data)
        self.assertEqual(result, 67)

if __name__=='__main__':
    unittest.main()
