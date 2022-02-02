from .parser_config import *

class AddUserParser:
    """
    Parser for AddUser command
    """
    @staticmethod
    def add_user_parser(subparsers, command):
        """Method to parse add user arguments passed """

        add_user_parser = subparsers.include(command)
        set_users_file_positional(add_user_parser)
