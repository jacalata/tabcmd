import sys
import unittest

try:
    from unittest import mock
except ImportError:
    import mock
import argparse
from pythontabcmd2.parsers.delete_project_parser import DeleteProjectParser
from .ParserTest import *

class DeleteProjectParserTest(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        commandname = 'deleteproject'
        cls.parser_under_test, subparsers, mock_command = initialize_test_pieces(commandname)
        DeleteProjectParser.delete_project_parser(subparsers, mock_command)


    def test_delete_project(self):
        mock_args = ['deleteproject', 'projectnameinput', '--site', 'sitenameinput']
        args = self.parser_under_test.parse_args(mock_args)
        assert args is not None
        assert args.site =='sitenameinput', args

    def test_delete_project_add_parent_path(self):
        mock_args = ['deleteproject', 'required-name', '--parent-project-path', 'test']

        args = self.parser_under_test.parse_args(mock_args)
        assert args is not None
        assert args.parent_project_path == "test", args
        assert args.projectname == 'required-name', args


    def test_delete_project_required_name_none(self):
        mock_args = ['deleteproject']
        with self.assertRaises(SystemExit):
            args = self.parser_under_test.parse_args(mock_args)


