import unittest
import data_viz
import os


class TestDataViz(unittest.TestCase):
    def test_data_viz_boxplot_exist(self):
        output_name = 'boxplot_test.png'
        check_bf = os.path.exists(output_name)
        data_viz.boxplot(1, output_name)
        check_af = os.path.exists(output_name)
        self.assertFalse(check_bf)
        self.assertTrue(check_af)



if __name__ == "__main__":
    unittest.main()