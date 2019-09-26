import sys


def read_stdin_col(col_num):
    """This function returns an array corresponding to values from
    stdin at the column number position

    Parameters
    ----------
    col_num : int
        column number

    Returns
    -------
    dataset : list
        An list of values, which is a part of data from stdin

    """

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
