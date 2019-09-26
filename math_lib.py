import math


def list_mean(L):
    """This function returns the mean of a given list
    """
    if L is None:
        return None
    if len(L) == 0:
        return None
    try:
        mean = sum(L)/len(L)
    except TypeError:
        raise TypeError('Unsupported value in the list')

    return mean


def list_stdev(L):
    """This function returns the standard deviation of
    a given list. Note that the standard deviation returned
    here is the sample standard deviation, which is the
    same as the formula used in statistics.stdev.
    """
    if L is None:
        return None
    if len(L) == 0:
        return None
    try:
        m = sum(L)/len(L)
    except TypeError:
        raise TypeError('Unsupported value in the list')
    std = math.sqrt(sum([(m - x) ** 2 for x in L]) / (len(L) - 1))
    return std
