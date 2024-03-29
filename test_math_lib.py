import unittest
import math_lib
import random
import statistics


class TestMathLib(unittest.TestCase):
    def test_list_mean_empty(self):
        """This function tests if the input list is empty
        """
        r = math_lib.list_mean(None)
        self.assertEqual(r, None)

    def test_list_mean_const(self):
        """This function tests if list_mean gives correct
        result given a list of constants.
        """
        r = math_lib.list_mean([1, 1, 1, 1])
        self.assertEqual(r, 1)

    def test_list_mean_rand(self):
        """This function tests if list_mean gives correct
        result given a list of random numbers.
        """
        L = []
        for j in range(100):
            for i in range(10):
                L.append(random.random())
            r = math_lib.list_mean(L)
            e = statistics.mean(L)
            self.assertAlmostEqual(r, e)

    def test_list_mean_exceptions(self):
        """This function tests if an exception is handled properly
        """
        with self.assertRaises(TypeError) as ex:
            math_lib.list_mean([1, 1, 1, 'x'])
        self.assertTrue('Unsupported value in the list' in str(ex.exception))

    def test_list_stdev_empty(self):
        """This function tests if the input list is empty
        """
        r = math_lib.list_stdev(None)
        self.assertEqual(r, None)

    def test_list_stdev_const(self):
        """This function tests if list_stdev gives correct
        result given a list of constants.
        """
        r = math_lib.list_stdev([1, 1, 1, 1])
        self.assertEqual(r, 0)

    def test_list_stdev_rand(self):
        """This function tests if list_stdev gives correct
        result given a list of random numbers.
        """
        L = []
        for j in range(100):
            for i in range(10):
                L.append(random.random())
            r = math_lib.list_stdev(L)
            e = statistics.stdev(L)
            self.assertAlmostEqual(r, e)

    def test_list_stdev_exceptions(self):
        """This function tests if an exception is handled properly
        """
        with self.assertRaises(TypeError) as ex:
            math_lib.list_stdev([1, 1, 1, 'x'])
        self.assertTrue('Unsupported value in the list' in str(ex.exception))


if __name__ == "__main__":
    unittest.main()
