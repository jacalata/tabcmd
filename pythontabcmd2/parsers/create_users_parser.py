from .parent_parser import *

class CreateUserParser:
    """
    Parser for the command CreateUser
    """
    @staticmethod
    def create_user_parser(subparsers, command):
        """Method to parse create user arguments passed """

        create_users_parser = subparsers.include(command)
        set_users_file_positional(create_users_parser)