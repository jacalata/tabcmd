import unittest

from pythontabcmd2.parsers.refresh_extracts_parser import RefreshExtractsParser
from .ParserTest import *

class RefreshExtractsParserTest(unittest.TestCase):


    def test_refresh_extract_parser_unrecognized_arguments(self):
        input = ['refreshextracts', 'nameeeee']
        parser, subparsers, mock_command = initialize_test_pieces('refreshextracts')
        RefreshExtractsParser.refresh_extracts_parser(subparsers, mock_command)
        with self.assertRaises(SystemExit):
            args = parser.parse_args(input)


    def test_refresh_extract_parser_missing_all_args(self):
        input = ['refreshextracts']
        parser, subparsers, mock_command = initialize_test_pieces('refreshextracts')
        RefreshExtractsParser.refresh_extracts_parser(subparsers, mock_command)
        # not yet implemented
        # with self.assertRaises(SystemExit):
        #    args = parser.parse_args(input)
