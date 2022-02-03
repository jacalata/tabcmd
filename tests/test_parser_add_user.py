import sys
import unittest

try:
    from unittest import mock
except ImportError:
    import mock
import argparse
from pythontabcmd2.parsers.add_users_parser import AddUserParser
from .ParserTest import *

class AddUsersParserTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        commandname = 'addusers'
        cls.parser_under_test, subparsers, mock_command = initialize_test_pieces(commandname)
        AddUserParser.add_user_parser(subparsers, mock_command)


    csv = ("testname", "testpassword", "test", "test", "test", "test")


    def test_add_user_parser_missing_group_name(self):
            with self.assertRaises(SystemExit):
                mock_args = ["addusers"]
                self.parser_under_test.parse_args(mock_args)


    # something is weird here
    def test_add_user_parser_group_name_present(self):
        with mock.patch('builtins.open', mock.mock_open(read_data='test')):
            mock_args = ["addusers", "groupname"]
            args = self.parser_under_test.parse_args(mock_args)
            print(args)
            assert args.groupname == 'groupname', args

    def test_add_user_parser_file_present(self):
        with mock.patch('builtins.open', mock.mock_open(read_data='test')):
            mock_args = ["addusers", "groupname", "--users", "test_csv.csv"]
            args = self.parser_under_test.parse_args(mock_args)
            assert args.groupname == 'groupname', args