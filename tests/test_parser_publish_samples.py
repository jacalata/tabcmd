import unittest
from .ParserTest import *
from pythontabcmd2.parsers.publish_samples_parser import PublishSamplesParser


class PublishSamplesParserTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        commandname = 'publishsamples'
        cls.parser_under_test, subparsers, mock_command = initialize_test_pieces(commandname)
        PublishSamplesParser.publish_samples_parser(subparsers, mock_command)

    def test_publish_parser_with_name(self):
        input = ['publishsamples', '-n', 'project-name-value']
        result = self.parser_under_test.parse_args(input)
        assert result.projectname == 'project-name-value'

    def test_publish_parser_projectname_without_flag(self):
        input = ['publishsamples', 'project-name']
        with self.assertRaises(SystemExit):
            self.parser_under_test.parse_args(input)


    def test_publish_samples_parser_optional_args(self):
        input = ['publishsamples', '-n', 'projectname', '--parent-project-path', 'parent-goes-here']
        result = self.parser_under_test.parse_args(input)
        assert result.projectname == 'projectname'
        assert result.parent_project_path == 'parent-goes-here'
