import matplotlib
import matplotlib.pyplot as plt
import math_lib


def boxplot(L, out_file_name):
    plt.boxplot(L)
    plt.xlabel('Box')
    plt.ylabel('Distribution')
    plt.title('mean: ' + str(math_lib.list_mean(L)) + ' ' +
              'stdev: ' + str(math_lib.list_stdev(L)))
    plt.savefig(out_file_name, dpi = 300)
    pass

def histogram(L, out_file_name):
    pass

def combo(L, out_file_name):
    pass