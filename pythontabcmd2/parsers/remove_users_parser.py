
from .parser_config import *


class RemoveUserParser:
    """
    Parser to removeusers command
    """
    @staticmethod
    def remove_user_parser(subparsers, command):
        """Method to parse remove user arguments passed by the user"""

        remove_users_parser =  subparsers.include(command)
        set_users_file_arg(remove_users_parser)
