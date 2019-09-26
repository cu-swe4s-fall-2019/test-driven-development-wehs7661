import unittest
import data_viz
import get_data
import os


class TestDataViz(unittest.TestCase):
    global L
    L = get_data.read_stdin_col(1)

    def test_data_viz_boxplot_exist(self):
        """This funtion test if the plot is saved properly.
        """
        output_name = 'boxplot_test.png'
        check_bf = os.path.exists(output_name)
        data_viz.boxplot(L, output_name)
        check_af = os.path.exists(output_name)
        self.assertFalse(check_bf)
        self.assertTrue(check_af)

    def test_data_viz_hist_exist(self):
        """This funtion test if the plot is saved properly.
        """
        output_name = 'hist_test.png'
        check_bf = os.path.exists(output_name)
        data_viz.histogram(L, output_name)
        check_af = os.path.exists(output_name)
        self.assertFalse(check_bf)
        self.assertTrue(check_af)

    def test_data_viz_combo_exist(self):
        """This funtion test if the plot is saved properly.
        """
        output_name = 'combo_test.png'
        check_bf = os.path.exists(output_name)
        data_viz.combo(L, output_name)
        check_af = os.path.exists(output_name)
        self.assertFalse(check_bf)
        self.assertTrue(check_af)


if __name__ == "__main__":
    unittest.main()
