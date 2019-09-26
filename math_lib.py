
def list_mean(L):
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
    return None
