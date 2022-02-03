import unittest

from pythontabcmd2.parsers.reencrypt_parser import ReencryptExtractsParser
from .ParserTest import *

class ReencryptExtractsParserTest(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        commandname = 'reencryptextracts'
        cls.parser_under_test, subparsers, mock_command = initialize_test_pieces(commandname)
        ReencryptExtractsParser.reencrypt_extracts_parser(subparsers, mock_command)

    def test_reencrypt_extract_parser_minimum_happy_args(self):
        input = ['reencryptextracts', 'sitenamevalue']
        output = self.parser_under_test.parse_args(input)
        assert output.sitename == 'sitenamevalue'

    def test_reencrypt_extract_parser_missing_site_name(self):
        input = ['reencryptextracts']
        with self.assertRaises(SystemExit):
            self.parser_under_test.parse_args(input)

    def test_reencrypt_extract_parser_unrecognized_arguments(self):
        input = ['reencryptextracts', 'sitename', 'randomextraarg']
        with self.assertRaises(SystemExit):
            self.parser_under_test.parse_args(input)

