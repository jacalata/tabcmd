from .parser_config import *

class CreateSiteParser:
    """
    Parser for createsite command
    """
    @staticmethod
    def create_site_parser(subparsers, command):
        """Method to parse create site arguments passed by the user"""
        create_site_parser = subparsers.include(command)

        create_site_parser.add_argument('--site-name', default=None,
                                        help='name of site')
        create_site_parser.add_argument('--url', '-r', default=None,
                                        help='used in URLs to specify site')


        set_site_args(create_site_parser)