import unittest
import get_data
import os
import sys


class TestGetData(unittest.TestCase):
    def test_get_data_invalid_colnum(self):
        with self.assertRaises(IndexError) as ex:
            get_data.read_stdin_col(5)
        self.assertTrue('Invalid column number' in str(ex.exception))
        

if __name__ == "__main__":
    unittest.main()




