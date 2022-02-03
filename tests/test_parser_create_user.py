
import unittest

try:
    from unittest import mock
except ImportError:
    import mock
from pythontabcmd2.parsers.create_users_parser import CreateUserParser
from .ParserTest import *

class CreateUserParserTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        commandname = 'createusers'
        cls.parser_under_test, subparsers, mock_command = initialize_test_pieces(commandname)
        CreateUserParser.create_user_parser(subparsers, mock_command)


    def test_create_user_missing_all_args(self):
        with self.assertRaises(SystemExit):
            args = self.parser_under_test.parse_args(['createusers'])


    def test_create_user_parser_role(self):
        with mock.patch('builtins.open', mock.mock_open(read_data='test')):
            mock_args = ["createusers", "test_csv.csv"]
            args = self.parser_under_test.parse_args(mock_args)

