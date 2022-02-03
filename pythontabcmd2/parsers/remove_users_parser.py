
from .parent_parser import *


class RemoveUserParser:
    """
    Parser to removeusers command
    """
    @staticmethod
    def remove_user_parser(subparsers, command):
        """Method to parse remove user arguments passed by the user"""

        remove_users_parser =  subparsers.include(command)
        remove_users_parser.add_argument('groupname', help='name of group')
        set_users_file_arg(remove_users_parser)
