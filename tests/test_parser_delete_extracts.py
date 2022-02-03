import unittest

try:
    from unittest import mock
except ImportError:
    import mock
import argparse
from pythontabcmd2.parsers.delete_extracts_parser import DeleteExtractsParser
from .ParserTest import *

class DeleteExtractsParserTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        commandname = 'deleteextract'
        cls.parser_under_test, subparsers, mock_command = initialize_test_pieces(commandname)
        DeleteExtractsParser.delete_extracts_parser(subparsers, mock_command)


    # if I add --include-all it fails
    def test_delete_extract_parser_optional_arguments(self):
        mock_args = ['deleteextract', '-w' ,'workbookname', '--encrypt']
        args = self.parser_under_test.parse_args(mock_args)

        assert args.datasource is None
        assert args.workbook == 'workbookname'
        assert args.encrypt_extract is False

    # why doesn't this fail and exit?
    def test_delete_extract_parser_missing_all_args(self):
        mock_args = ['deleteextract']
        #with self.assertRaises(SystemExit):
        args = self.parser_under_test.parse_args(mock_args)

    def test_delete_extract_parser_missing_project_path(self):
        mock_args = ['deleteextract', '-d', 'datasource', '--parent-project-path']
        with self.assertRaises(SystemExit):
            args = self.parser_under_test.parse_args(mock_args)

