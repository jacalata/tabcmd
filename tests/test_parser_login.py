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
        subparsers = create.Subparsers()
        parser = subparsers.get_root_parser()
        # argparse.ArgumentParser()
        # self.subparsers = self.parent.add_subparsers()
        # self.global_options = parent_parser.initialize_parser()
        # parent_parser.add_global_options(self.global_options)
        mock_command = commandname, LoginParserTest.mock_command_action, 'mock help text'

        cls.parser_under_test = parser
        LoginParser.login_parser(subparsers, mock_command)


    def test_login_parser_test_username_password(self):
        mock_args = ['login', '--username', 'me', '--password', 'pass']
        args = self.parser_under_test.parse_args(mock_args)
        assert args is not None


    def test_missing_server(self):
        mock_args = ['login', '--logging-level', 'info', '--no-prompt', '--password', 'testing123']


    def test_username(self):
        mock_args =['login', '--logging-level', 'info', '--password',
                        'testing123', '--no_prompt']

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
