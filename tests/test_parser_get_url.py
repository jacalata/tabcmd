import unittest

try:
    from unittest import mock
except ImportError:
    import mock
import argparse
from pythontabcmd2.parsers.get_url_parser import GetUrlParser
from .ParserTest import *

class GetUrlParserTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        commandname = 'get'
        cls.parser_under_test, subparsers, mock_command = initialize_test_pieces(commandname)
        GetUrlParser.get_url_parser(subparsers, mock_command)

    def test_get_url_parser_file(self):
        input = ['get', 'url-value', '--filename', 'filename-value']
        result = self.parser_under_test.parse_args(input)
        assert result is not None

    def test_get_url_parser_missing_all_args(self):
        mock_args = ['get']
        with self.assertRaises(SystemExit):
            self.parser_under_test.parse_args(mock_args)

    def test_get_url_parser_no_file(self):
        mock_args = ['get', 'url-value']
        args = self.parser_under_test.parse_args(mock_args)
        assert args is not None
        assert args.url == 'url-value'