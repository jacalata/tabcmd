import sys
import unittest

try:
    from unittest import mock
except ImportError:
    import mock
import argparse
from pythontabcmd2.parsers.delete_group_parser import DeleteGroupParser
from .ParserTest import *

class DeleteGroupParserTestT(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        commandname = 'deletegroup'
        cls.parser_under_test, subparsers, mock_command = initialize_test_pieces(commandname)
        DeleteGroupParser.delete_group_parser(subparsers, mock_command)


    def test_delete_group_parser_required_name(self):
        mock_args = ['deletegroup', 'groupname']

        args = self.parser_under_test.parse_args(mock_args)
        assert args.groupname == 'groupname'

    def test_delete_group_parser_required_name_missing(self):
        mock_args = ['deletegroup']
        with self.assertRaises(SystemExit):
            args = self.parser_under_test.parse_args(mock_args)
            args_from_command = vars(args)
            args_from_mock = vars(mock_args.return_value)
            self.assertEqual(args_from_command, args_from_mock)
