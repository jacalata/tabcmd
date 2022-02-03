import sys
import unittest

try:
    from unittest import mock
except ImportError:
    import mock
import argparse
from pythontabcmd2.parsers.delete_site_users_parser \
    import DeleteSiteUsersParser
from .ParserTest import *

class DeleteSiteUsersParserTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        commandname = 'deletesiteusers'
        cls.parser_under_test, subparsers, mock_command = initialize_test_pieces(commandname)
        DeleteSiteUsersParser.delete_site_users_parser(subparsers, mock_command)



    csv = ("testname", "testpassword", "test", "test", "test", "test")

    def test_delete_site_user_parser(self):
        with mock.patch('builtins.open', mock.mock_open(read_data='test')):
            input = ["deletesiteusers", "test_csv.csv"]
            args = self.parser_under_test.parse_args(input)

    def test_delete_site_user_parser_missing_arguments(self):
        with self.assertRaises(SystemExit):
            input = ["deletesiteusers"]

            args = self.parser_under_test.parse_args(input)

