import unittest
import get_data
import viz

class TestViz(unittest.TestCase):
    def test_viz_column_exceptions(self):
        with self.assertRaises(IndexError) as ex:
            get_data.read_stdin_col(5)
        self.assertTrue('Invalid column number' in str(ex.exception))
        with self.assertRaises(TypeError) as ex:
            get_data.read_stdin_col('X')
        self.assertTrue('Wrong data type of input' in str(ex.exception))


class ParserTest(unittest.TestCase):
    def setUp(self):
        """This function set up the parser for the unit test of argparse
        """
        self.parser = viz.initialize()

    def test_viz_parser(self):
        """This function test if the parser works properly 
        """
        parsed = self.parser.parse_args(['-t', 'boxplot', '-c', '2', '-n', 'boxplot.png'])
        self.assertEqual(parsed.type, 'boxplot')
        self.assertEqual(parsed.col_num, '2')
        self.assertEqual(parsed.output_name, 'boxplot.png')

if __name__ == '__main__':
    unittest.main()