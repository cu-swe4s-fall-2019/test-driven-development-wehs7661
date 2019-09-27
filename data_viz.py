import matplotlib
import matplotlib.pyplot as plt
import math_lib


def boxplot(L, out_file_name):
    """Generates a boxplot with given data and save
    it with the file name specified by the user
    """
    plt.figure()
    plt.boxplot(L)
    plt.xlabel('Box')
    plt.ylabel('Distribution')
    plt.title('Mean: %6.2f, Standard deviation: %6.2f' %
              (math_lib.list_mean(L), math_lib.list_stdev(L)))
    plt.savefig(out_file_name, dpi=300)
    plt.show()
    pass


def histogram(L, out_file_name):
    """Generates a histogram with given data and save
    it with the file name specified by the user
    """
    plt.figure()
    plt.hist(L, bins=20)
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Mean: %6.2f, Standard deviation: %6.2f' %
              (math_lib.list_mean(L), math_lib.list_stdev(L)))
    plt.savefig(out_file_name, dpi=300)
    plt.show()
    pass


def combo(L, out_file_name):
    """Generates a subplot containing a boxplot and a
    histogram with given data and save it with the
    file name specified by the user
    """
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.boxplot(L)
    plt.xlabel('Value')
    plt.ylabel('Distribution')

    plt.subplot(1, 2, 2)
    plt.hist(L, bins=20)
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    fig.suptitle('Mean: %6.2f, Standard deviation: %6.2f' %
                 (math_lib.list_mean(L), math_lib.list_stdev(L)))
    fig.savefig(out_file_name, dpi=300)
    plt.show()
    pass
