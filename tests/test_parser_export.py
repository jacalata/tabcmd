import unittest
from .ParserTest import *
try:
    from unittest import mock
except ImportError:
    import mock
import argparse
from pythontabcmd2.parsers.export_parser import ExportParser


class ExportParserTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        commandname = 'export'
        cls.parser_under_test, subparsers, mock_command = initialize_test_pieces(commandname)
        ExportParser.export_parser(subparsers, mock_command)


    def test_export_parser_file_type_pdf(self):
        mock_args = ['export', '--pdf']
        args = self.parser_under_test.parse_args(mock_args)
        assert args.pdf is True
        
    def test_export_parser_file_type_fullpdf(self):
        mock_args = ['export', '--fullpdf']
        args = self.parser_under_test.parse_args(mock_args)
        assert args.fullpdf is True


    def test_export_parser_missing_all_args(self):
        mock_args = ['export']
        with self.assertRaises(SystemExit):
            self.parser_under_test.parse_args(mock_args)
