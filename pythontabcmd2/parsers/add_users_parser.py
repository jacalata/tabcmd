from .parent_parser import *

class AddUserParser:
    """
    Parser for AddUser command
    """
    @staticmethod
    def add_user_parser(subparsers, command):
        """Method to parse add user arguments passed """

        add_user_parser = subparsers.include(command)
        add_user_parser.add_argument('groupname', help='name of group to add users to')
        set_users_file_arg(add_user_parser)
