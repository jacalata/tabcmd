import sys
import unittest

try:
    from unittest import mock
except ImportError:
    import mock
import argparse
from pythontabcmd2.parsers.create_site_users_parser \
    import CreateSiteUsersParser
from .ParserTest import *

class CreateSiteUsersParserTest(unittest.TestCase):
    csv = ("testname", "testpassword", "test", "test", "test", "test")
    @classmethod
    def setUpClass(cls):
        commandname = 'createsiteusers'
        cls.parser_under_test, subparsers, mock_command = initialize_test_pieces(commandname)
        CreateSiteUsersParser.create_site_users_parser(subparsers, mock_command)


    def test_create_site_users_parser_role(self):
        with mock.patch('builtins.open', mock.mock_open(read_data='test')):
            mock_args = ["createsiteusers", "test_csv.csv", "-r", "Unlicensed"]
            args = self.parser_under_test.parse_args(mock_args)
            assert args.role == 'Unlicensed'

    def test_create_site_users_parser_missing_arguments(self):
        with mock.patch('builtins.open', mock.mock_open(read_data='test')):
            with self.assertRaises(SystemExit):
                mock_args = ["createsiteusers"]
                args = self.parser_under_test.parse_args(mock_args)
