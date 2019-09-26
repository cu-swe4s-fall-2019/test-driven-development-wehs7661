import matplotlib
import matplotlib.pyplot as plt
import math_lib


def boxplot(L, out_file_name):
    plt.figure()
    plt.boxplot(L)
    plt.xlabel('Box')
    plt.ylabel('Distribution')
    plt.title('Mean: %6.2f, Standard deviation: %6.2f' % (math_lib.list_mean(L), math_lib.list_stdev(L)))
    plt.savefig(out_file_name, dpi = 300)
    plt.close('all')
    pass


def histogram(L, out_file_name):
    plt.figure()
    plt.hist(L, bins = 20)
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Mean: %6.2f, Standard deviation: %6.2f' % (math_lib.list_mean(L), math_lib.list_stdev(L)))
    plt.savefig(out_file_name, dpi = 300)
    plt.close('all')
    pass

def combo(L, out_file_name):
    fig, axs = plt.subplots(1, 2, figsize=(12, 6))
    axs[0].boxplot(L)
    axs[1].hist(L, bins=20)
    fig.suptitle('Mean: %6.2f, Standard deviation: %6.2f' % (math_lib.list_mean(L), math_lib.list_stdev(L)))
    fig.savefig(out_file_name, dpi = 300)
    plt.close('all')
    pass