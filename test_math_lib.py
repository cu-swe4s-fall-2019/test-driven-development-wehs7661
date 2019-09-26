import unittest
import math_lib
import random
import statistics

class TestMathLib(unittest.TestCase):
    def test_list_mean_empty(self):
        r = math_lib.list_mean(None)
        self.assertEqual(r, None)

    def test_list_mean_const(self):
        r = math_lib.list_mean([1,1,1,1])
        self.assertEqual(r, 1)

    def test_list_mean_rand(self):
        L = []
        for j in range(100):
            for i in range(10):
                L.append(random.random())
            r = math_lib.list_mean(L)
            e = statistics.mean(L)
            self.assertAlmostEqual(r, e)

    def test_list_mean_exceptions(self):
        with self.assertRaises(TypeError) as ex:
            math_lib.list_mean([1, 1, 1, 'x'])
        self.assertTrue('Unsupported value in the list' in str(ex.exception))

    def test_list_stdev_empty(self):
        r = math_lib.list_stdev(None)
        self.assertEqual(r, None)

    

if __name__ == "__main__":
    unittest.main()