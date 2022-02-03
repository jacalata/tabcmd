import unittest

try:
    from unittest import mock
except ImportError:
    import mock
import argparse
from pythontabcmd2.parsers.decrypt_extracts_parser \
    import DecryptExtractsParser
from .ParserTest import *

class DecryptExtractsParserTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        commandname = 'decryptextracts'
        cls.parser_under_test, subparsers, mock_command = initialize_test_pieces(commandname)
        DecryptExtractsParser.decrypt_extracts_parser(subparsers, mock_command)


    def test_decrypt_extract_parser_happy(self):
        input = ['decryptextracts', 'sitename']
        args = self.parser_under_test.parse_args(input)


    def test_decrypt_extract_parser_missing_all_args(self):
        mock_args = ['decryptextracts']
        with self.assertRaises(SystemExit):
            args = self.parser_under_test.parse_args(mock_args)


 