import unittest
import math_lib

class TestMathLib(unittest.testCase):
    def test_list_mean_empty(self):
        r = math_lib.list_mean(None)
        self.assertEqual(r, None)

    