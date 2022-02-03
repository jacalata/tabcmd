
import unittest
from pythontabcmd2.parsers import create, parent_parser
from pythontabcmd2.parsers import create_extracts_parser
from pythontabcmd2.parsers.create_extracts_parser import CreateExtractsParser

class ExtractsParserTest(unittest.TestCase):


    def mock_command_action():
        print('a mockery!')

    """ This test fails
    def test_parser_extract_parser_missing_all_args(self):
        parser = parser_setup.initialize_parser()

        with self.assertRaises(SystemExit):
            parser.ExtractsParser.parser.Extracts_parser(parser)
            args = parser.parse_args(['parser.Extracts'])
    """

    def test_parser_extract_parser_missing_project_path(self):

        mock_command = 'createextracts', ExtractsParserTest.mock_command_action, 'mock help text'
        parser = parent_parser.initialize_parser()
        subparsers = create.Subparsers(parser)
        create_extracts_parser.CreateExtractsParser().create_extracts_parser(subparsers, mock_command)

        no_project_path = ['createextracts', '-d', 'dsname', '-p', '123']
        args = parser.parse_args(no_project_path)
        assert args.datasource == 'dsname'

    def test_parser_extract_parser_optional_arguments(self):

        input = ['createextracts', '-d', 'testproject', '--embedded-datasources', 'desc',
            # unrecognized '-u', '1234',
            '--project', 'test123',
            # unrecognized'--parent-project-path', 'abcdef',
            '-w', 'workbooktest']

        mock_command = 'createextracts', ExtractsParserTest.mock_command_action, 'mock help text'
        parser = parent_parser.initialize_parser()
        subparsers = create.Subparsers(parser)
        create_extracts_parser.CreateExtractsParser().create_extracts_parser(subparsers, mock_command)

        args = parser.parse_args(input)
        assert args is not None
        assert args.workbook == 'workbooktest'
        assert args.project == 'test123'


    def test_parser_extract_parser_missing_workbook(self):
        input = ['createextracts', '--datasource', 'testproject', '--embedded_datasources', 'desc',
            '-u', '1234', '-p', 'test123', '-w', '--include_all', 'True']

        mock_command = 'createextracts', ExtractsParserTest.mock_command_action, 'mock help text'
        parser = parent_parser.initialize_parser()
        subparsers = create.Subparsers(parser)
        create_extracts_parser.CreateExtractsParser().create_extracts_parser(subparsers, mock_command)

        with self.assertRaises(SystemExit):
            args = parser.parse_args(input)


    def test_parser_extract_parser_missing_datasource(self):
        input = ['createextracts', '--datasource', '--embedded_datasources', 'desc',
            '-u', '1234', '-p', 'test123', '-w', 'testproject', '--include_all', 'True']

        mock_command = 'createextracts', ExtractsParserTest.mock_command_action, 'mock help text'
        parser = parent_parser.initialize_parser()
        subparsers = create.Subparsers(parser)
        create_extracts_parser.CreateExtractsParser().create_extracts_parser(subparsers, mock_command)

        with self.assertRaises(SystemExit):
            args = parser.parse_args(input)


    def test_parser_extract_parser_missing_embedded(self):
        input = ['createextracts', '--datasource', '123', '--embedded_datasources', '-u', '1234', '-p', 'test123',
            '-w', 'testproject', '--include_all', 'True']

        mock_command = 'createextracts', ExtractsParserTest.mock_command_action, 'mock help text'
        parser = parent_parser.initialize_parser()
        subparsers = create.Subparsers(parser)
        create_extracts_parser.CreateExtractsParser().create_extracts_parser(subparsers, mock_command)

        with self.assertRaises(SystemExit):
            args = parser.parse_args(input)
