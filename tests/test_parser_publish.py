import unittest
from .ParserTest import *
from pythontabcmd2.parsers.publish_parser import PublishParser


class PublishParserTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        commandname = 'publish'
        cls.parser_under_test, subparsers, mock_command = initialize_test_pieces(commandname)
        PublishParser.publish_parser(subparsers, mock_command)

    def test_publish_parser_with_name(self):
        input = ['publish', 'filenametopublish','--overwrite']
        result = self.parser_under_test.parse_args(input)
        assert result.name == 'filenametopublish'
        assert result.overwrite == True

    def test_publish_parser_missing_all_args(self):
        input = ['publish']
        with self.assertRaises(SystemExit):
            self.parser_under_test.parse_args(input)

