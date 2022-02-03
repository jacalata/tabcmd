import unittest
from pythontabcmd2.parsers import create


class RunScheduleParserTest(unittest.TestCase):

    def mock_command_action():
        print('a mocking test')

    def test_runschedule_parser_optional_arguments(self):
        mock_command = 'runschedule', RunScheduleParserTest.mock_command_action, 'mock help text'
        input = []
        subparsers = create.Subparsers()
        parser = subparsers.get_root_parser()

        # parser.runschedule_parser(mock_command)
        args = parser.parse_args(input)



