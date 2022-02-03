import unittest

try:
    from unittest import mock
except ImportError:
    import mock
from pythontabcmd2.parsers.logout_parser import LogoutParser
from .ParserTest import *

class LogoutParserTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        commandname = 'logout'
        cls.parser_under_test, subparsers, mock_command = initialize_test_pieces(commandname)
        LogoutParser.logout_parser(subparsers, mock_command)


    def test_logout_many_args(self):
        input = ['logout', '--server', "https://localhost/", '--username', 'helloworld',
                '--logging-level', "info", '--password', "testing123"]

        args = self.parser_under_test.parse_args(input)
        assert args is not None

    def test_logout_no_args(self):
        args = self.parser_under_test.parse_args([])
        assert args is not None



