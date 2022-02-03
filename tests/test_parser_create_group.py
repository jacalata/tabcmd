import unittest
from .ParserTest import *
try:
    from unittest import mock
except ImportError:
    import mock
import argparse
from pythontabcmd2.parsers.create_group_parser import CreateGroupParser


class CreateGroupParserTest(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        commandname = 'creategroup'
        cls.parser_under_test, subparsers, mock_command = initialize_test_pieces(commandname)
        CreateGroupParser.create_group_parser(subparsers, mock_command)



    def test_create_group_parser_required_name(self):
        mock_args = ['creategroup', 'groupname']
        args = self.parser_under_test.parse_args(mock_args)
        assert args.groupname == 'groupname'

    def test_create_group_parser_missing_required_name(self):
        mock_args = ['creategroup']
        with self.assertRaises(SystemExit):
            args = self.parser_under_test.parse_args(mock_args)
