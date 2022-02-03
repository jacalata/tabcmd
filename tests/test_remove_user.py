import unittest
from .ParserTest import *
from pythontabcmd2.parsers.remove_users_parser import RemoveUserParser

class RemoveUsersParserTest(unittest.TestCase):

    def test_remove_users_parser(self):

        parser, subparsers, mock_command = initialize_test_pieces('removeusers')
        input = ["removeusers", "group-name"]
        RemoveUserParser.remove_user_parser(subparsers, mock_command)

        args = parser.parse_args(input)
        assert args is not None
        assert args.groupname == "group-name"


    def test_remove_users_parser_no_file(self):
        input = ["removeusers", "group-name", "--users"]
        parser, subparsers, mock_command = initialize_test_pieces('removeusers')
        RemoveUserParser.remove_user_parser(subparsers, mock_command)

        with self.assertRaises(SystemExit):
            parser.parse_args(input)


    # this should be an error but it isn't
    def test_remove_users_parser_missing_group_name(self):
        parser, subparsers, mock_command = initialize_test_pieces('removeusers')
        input = ["removeusers"]
        RemoveUserParser.remove_user_parser(subparsers, mock_command)
        with self.assertRaises(SystemExit):
            parser.parse_args(input)


