import unittest

try:
    from unittest import mock
except ImportError:
    import mock
import argparse
from pythontabcmd2.parsers.encrypt_extracts_parser \
    import EncryptExtractsParser
from .ParserTest import *

class EncryptExtractsParserTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        commandname = 'encryptextracts'
        cls.parser_under_test, subparsers, mock_command = initialize_test_pieces(commandname)
        EncryptExtractsParser.encrypt_extracts_parser(subparsers, mock_command)


    def test_encrypt_extract_parser_missing_site_name(self):
        mock_args = ['encryptextracts']
        with self.assertRaises(SystemExit):
            args = self.parser_under_test.parse_args(mock_args)


    def test_encrypt_extracts_parser_happy(self):
        input = ['encryptextracts', 'sitename']
        result = self.parser_under_test.parse_args(input)
        assert result is not None