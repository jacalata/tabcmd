
from .parent_parser import *

class DeleteSiteParser:
    """
    Parser for the command deletesite
    """
    @staticmethod
    def delete_site_parser(subparsers, command):
        """Method to parse delete site arguments passed by the user"""

        delete_site_parser = subparsers.include(command)
        delete_site_parser.add_argument('sitename', help='Name of site to delete')
