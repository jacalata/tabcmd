from .parent_parser import *

class CreateSiteParser:
    """
    Parser for createsite command
    """
    @staticmethod
    def create_site_parser(subparsers, command):
        """Method to parse create site arguments passed by the user"""
        create_site_parser = subparsers.include(command)

        create_site_parser.add_argument('sitename', help='name of site')
        set_content_url_arg(create_site_parser)
        set_site_args(create_site_parser)