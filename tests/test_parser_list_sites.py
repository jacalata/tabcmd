import unittest

try:
    from unittest import mock
except ImportError:
    import mock
import argparse
from pythontabcmd2.parsers.list_sites_parser import ListSitesParser
from .ParserTest import *

class ListSitesParserTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        commandname = 'listsites'
        cls.parser_under_test, subparsers, mock_command = initialize_test_pieces(commandname)
        ListSitesParser.list_site_parser(subparsers, mock_command)

    @mock.patch('argparse.ArgumentParser.parse_args',
                return_value=argparse.Namespace())
    def test_list_site_parser_user_quota_integer_missing(self, mock_args):
        args = self.parser_under_test.parse_args(mock_args)
        args_from_command = vars(args)
        args_from_mock = vars(mock_args.return_value)
        assert args_from_command == args_from_mock

    @mock.patch('argparse.ArgumentParser.parse_args',
                return_value=argparse.Namespace(username="hello",
                                                password="hellotest",
                                                site="helloworld"))
    def test_list_site_parser_user_quota_integer(self, mock_args):
        args = self.parser_under_test.parse_args(mock_args)
        args_from_command = vars(args)
        args_from_mock = vars(mock_args.return_value)
        assert args_from_command == args_from_mock
