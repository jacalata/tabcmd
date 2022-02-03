
import unittest

try:
    from unittest import mock
except ImportError:
    import mock
import argparse
from pythontabcmd2.parsers.delete_parser import DeleteParser
from .ParserTest import *

class DeleteParserTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        commandname = 'delete'
        cls.parser_under_test, subparsers, mock_command = initialize_test_pieces(commandname)
        DeleteParser.delete_parser(subparsers, mock_command)


    def test_delete_parser(self):
        mock_args = ['delete', '-r', 'project-name-input', '--datasource', 'datasource-input']
        args = self.parser_under_test.parse_args(mock_args)
        assert args is not None
        assert args.projectname == 'project-name-input', args
        assert args.datasource == 'datasource-input', args

    # todo: we should make this fail?
    def test_delete_parser_datasource_and_workbook_present(self):
        mock_args = ['delete', '-r', 'project-name-input',
            '--datasource', 'datasource-input', '--workbook', 'workbook-name']
        args = self.parser_under_test.parse_args(mock_args)
        assert args.datasource == 'datasource-input', args
        assert args.workbook == 'workbook-name', args

    # todo we should make this fail
    def test_delete_parser_missing_args(self):
        args = self.parser_under_test.parse_args(['delete'])
        assert args is not None
        assert args.datasource is None
        assert args.workbook is None

