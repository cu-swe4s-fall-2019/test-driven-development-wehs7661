import sys


def read_stdin_col(col_num):
   dataset = []
   for l in sys.stdin:
       col = l.splitlines()[0].split()
       try:
           data = col[col_num - 1]
       except IndexError:
           raise IndexError('Invalid column number')
       except TypeError:
           raise TypeError('Wrong data type of input')
       dataset.append(data)
   return dataset