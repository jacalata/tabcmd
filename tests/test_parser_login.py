import unittest
from pythontabcmd2.parsers import parent_parser, create
try:
    from unittest import mock
except ImportError:
    import mock
import argparse
from pythontabcmd2.parsers.login_parser import LoginParser


class LoginParserTest(unittest.TestCase):

    def mock_command_action():
        print('a mockery!')

    @classmethod
    def setUpClass(cls):
        commandname = 'login'

        parser = parent_parser.initialize_parser()
        subparsers = create.Subparsers(parser)
        mock_command = commandname, LoginParserTest.mock_command_action, 'mock help text'

        cls.parser_under_test = parser
        LoginParser.login_parser(subparsers, mock_command)


    @mock.patch('argparse.ArgumentParser.parse_args',
                return_value=argparse.Namespace(
                    server="https://localhost/",
                    username="helloworld",
                    site="",
                    logging_level="info",
                    password="testing123",
                    no_prompt=True, token=None,
                    token_name=None,
                    cookie=True,
                    no_cookie=False,
                    prompt=False
                ))
    def test_login_parser_test_username_password(self, mock_args):
        args = self.parser_under_test.parse_args(mock_args)
        assert args is not None

    """ no required args yet
    @mock.patch('argparse.ArgumentParser.parse_args',
                return_value=argparse.Namespace(
                    server="https://localhost/",
                    username=None,
                    site="",
                    logging_level="info",
                    password=None,
                    no_prompt=True, token=None,
                    token_name="test",
                    cookie=True,
                    no_cookie=False,
                    prompt=False))
    def test_login_parser_token_name(self, mock_args):
        with self.assertRaises(SystemExit):
            args = self.parser_under_test.parse_args(mock_args)

    @mock.patch('argparse.ArgumentParser.parse_args',
                return_value=argparse.Namespace(
                    server="https://localhost/",
                    username="test",
                    site="",
                    logging_level="info",
                    password=None,
                    no_prompt=True, token=None,
                    token_name=None,
                    cookie=True,
                    no_cookie=False,
                    prompt=False))
    def test_login_parser_username_pass(self, mock_args):
        with self.assertRaises(SystemExit):
            args = self.parser_under_test.parse_args(mock_args)
"""
