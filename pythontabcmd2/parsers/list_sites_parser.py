from .parent_parser import *
class ListSitesParser:
    """
    Parser to list sites
    """
    @staticmethod
    def list_site_parser(subparsers, command):
        """Method to parse list sites arguments passed by the user"""


        list_sites_parsers = subparsers.include(command)
        set_view_site_encryption(list_sites_parsers)
