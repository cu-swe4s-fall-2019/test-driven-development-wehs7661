import unittest
import get_data
import os
import sys


class TestGetData(unittest.TestCase):
   def test_get_data_invalid_colnum(self):
       with self.assertRaises(IndexError) as ex:
           get_data.read_stdin_col(5)
       self.assertTrue('Invalid column number' in str(ex.exception))
   def test_get_data_wrong_type(self):
       with self.assertRaises(TypeError) as ex:
           get_data.read_stdin_col('X')
       self.assertTrue('Wrong data type of input' in str(ex.exception))
       
if __name__ == "__main__":
   unittest.main()