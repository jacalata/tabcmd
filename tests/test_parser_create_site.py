import unittest

try:
    from unittest import mock
except ImportError:
    import mock
import argparse
from .ParserTest import *

from pythontabcmd2.parsers.create_site_parser import CreateSiteParser


class CreateSiteParserTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        commandname = 'createsite'
        cls.parser_under_test, subparsers, mock_command = initialize_test_pieces(commandname)
        CreateSiteParser.create_site_parser(subparsers, mock_command)

    def test_create_site_parser_missing_both_site_modes(self):
        mock_args = ['createsite', 'sitename']
        args = self.parser_under_test.parse_args(mock_args)
        assert args.site_admin_user_management == False, args


    def test_create_site_parser_missing_all_args(self):
        mock_args = ['createsite']
        with self.assertRaises(SystemExit):
            args = self.parser_under_test.parse_args(mock_args)

    def test_create_site_parser_user_quota_integer(self):
        mock_args = ['createsite', 'testsite', '--user-quota', '12']
        args = self.parser_under_test.parse_args(mock_args)
        assert args.user_quota == '12', args
