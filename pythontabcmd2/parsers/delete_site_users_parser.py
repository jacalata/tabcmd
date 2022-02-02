
from .parser_config import *

class DeleteSiteUsersParser:
    """
    Parser for the command deletesiteusers
    """
    @staticmethod
    def delete_site_users_parser(subparsers, command):
        """Method to parse delete users passed by the user"""

        delete_site_users_parser = subparsers.include(command)
        set_users_file_arg(delete_site_users_parser)

