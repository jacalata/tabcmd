import argparse

from pythontabcmd2.parsers.add_users_parser import AddUserParser
from pythontabcmd2.parsers.create_project_parser import CreateProjectParser
from pythontabcmd2.parsers.create_group_parser import CreateGroupParser
class ParentParser:

    """
    parents project path
    """
    def add_parent_project_path():
        parser = argparse.ArgumentParser(add_help=False)
        parser.add_argument('--parent-project-path',
                            default=None,
                            help='path of parent project')
        return parser


    @staticmethod
    def initialize_parser():
        parser = argparse.ArgumentParser(add_help=False)
        return parser

    def add_global_option():
        parser = ParentParser.initialize_parser()
        ParentParser.add_global_options(parser)

    """Parser that will be used by all commands. Contains
    authentication and logging level setting"""
    @staticmethod
    def add_global_options(parser):
        parser.add_argument('--server', '-s',
                            help='server of account holder')
        parser.add_argument('--username', '-u',
                            help='username of account holder')
        parser.add_argument('--site', '-t', default='',
                            help='Used in the URL to uniquely identify the '
                                 'site.')
        parser.add_argument('--password', '-p',
                            help='password of account holder')
        prompt_group = parser.add_mutually_exclusive_group()
        prompt_group.add_argument('--no-prompt', action='store_true',
                                  help='no prompt for password')
        prompt_group.add_argument('--prompt', action='store_true',
                                  help='prompt for password')
        parser.add_argument('--logging-level', '-l',
                            choices=['debug', 'info', 'error'],
                            default='info',
                            help='desired logging level '
                                 '(set to error by default)')
        parser.add_argument('--token', '-to', default=None,
                            help='personal access token to '
                                 'sign into the '
                                 'server')
        parser.add_argument('--token-name', '-tn',
                            help='name of the personal access '
                                 'token used to sign into the server')
        group = parser.add_mutually_exclusive_group()
        group.add_argument('--no-cookie', action='store_true',
                           help='do not save session id')
        group.add_argument('--cookie', action='store_true',
                           help='save session id')
        return parser

