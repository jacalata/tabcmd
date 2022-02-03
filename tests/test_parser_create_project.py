import unittest
from .ParserTest import *
from pythontabcmd2.parsers.create_project_parser import CreateProjectParser

class ProjectParserTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        commandname = 'createproject'
        cls.parser_under_test, subparsers, mock_command = initialize_test_pieces(commandname)
        CreateProjectParser.create_project_parser(subparsers, mock_command)


    def test_parser_project_parser_optional_arguments(self):
        input = ['createproject', '-n', 'testproject','--parent-project-path', 'abcdef',
                  '--description', 'desc']
        args = self.parser_under_test.parse_args(input)
        assert args.parent_project_path == "abcdef"
        assert args.description == 'desc'


    def test_parser_project_parser_required_arguments_name(self):
        input = ['createproject', '--project', 'mock-name']
        args = self.parser_under_test.parse_args(input)
        assert args is not None
        print(args)
        assert args.projectname == 'mock-name'
        print (args)


    def test_parser_project_parser_required_arguments_name_missing(self):
        input = ['createproject', '-n']
        with self.assertRaises(SystemExit):
            args = self.parser_under_test.parse_args(input)

    def test_parser_project_parser_random_extra(self):
        input = ['createproject', 'boo', '--random']
        with self.assertRaises(SystemExit):
             args = self.parser_under_test.parse_args(input)