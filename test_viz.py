import unittest
import data_viz
import get_data
import os
import viz


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
        self.assertEqual(parser.col_num, '2')
        self.assertEqual(parser.output_name, 'boxplot.png')

if __name__ == '__main__':
    unittest.main()