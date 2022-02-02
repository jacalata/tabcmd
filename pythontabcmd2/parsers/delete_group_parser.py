
from .parser_config import *

class DeleteGroupParser:
    """
    Parser for the command deletegroup
    """
    @staticmethod
    def delete_group_parser(subparsers, command):
        """Method to parse delete group arguments passed by the user"""

        delete_group_parser = subparsers.include(command)
        delete_group_parser.add_argument('groupname', help='name of group to delete')
