import unittest

try:
    from unittest import mock
except ImportError:
    import mock
from pythontabcmd2.parsers.list_sites_parser import ListSitesParser
from .ParserTest import *

class ListSitesParserTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        commandname = 'listsites'
        cls.parser_under_test, subparsers, mock_command = initialize_test_pieces(commandname)
        ListSitesParser.list_site_parser(subparsers, mock_command)

    def test_list_site_parser(self):
        mock_args = ['listsites']
        args = self.parser_under_test.parse_args(mock_args)
        assert args is not None

    def test_list_site_parser_with_encryption(self):
        mock_args = ['listsites', '--get-extract-encryption-mode' ]
        args = self.parser_under_test.parse_args(mock_args)
        assert args.get_extract_encryption_mode == True, args