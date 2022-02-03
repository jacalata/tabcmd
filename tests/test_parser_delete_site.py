import sys
import unittest

try:
    from unittest import mock
except ImportError:
    import mock
import argparse
from pythontabcmd2.parsers.delete_site_parser import DeleteSiteParser
from .ParserTest import *

class DeleteSiteParserTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        commandname = 'deletesite'
        cls.parser_under_test, subparsers, mock_command = initialize_test_pieces(commandname)
        DeleteSiteParser.delete_site_parser(subparsers, mock_command)


    def test_delete_site(self):
        mock_args = ['deletesite', 'sitenamevalue']
        args = self.parser_under_test.parse_args(mock_args)
        assert args.sitename == 'sitenamevalue'

    # why doesn't this throw a systemexit?
    def test_delete_site_required_name_none(self):
        mock_args = ['deletesite']
        with self.assertRaises(SystemExit):
            args = self.parser_under_test.parse_args(mock_args)
