from .parent_parser import *

class CreateGroupParser:
    """
    Parser for creategroup command
    """
    @staticmethod
    def create_group_parser(subparsers, command):
        """Method to parse create group arguments passed by the user"""
        create_group_parser = subparsers.include(command)
        create_group_parser.add_argument('groupname', help='name of group')
