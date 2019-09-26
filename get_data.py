import sys


def read_stdin_col(col_num):
    dataset = []
    for l in sys.stdin:
        col = l.splitlines()[0].split()
        try:
            data = col[col_num - 1]
        except IndexError:
            raise IndexError('Invalid column number')
        dataset.append(data)
    return dataset



