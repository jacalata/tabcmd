from .parent_parser import *

class GetUrlParser:
    """Parser for the command geturl"""
    @staticmethod
    def get_url_parser(subparsers ,command):
        """Method to parse get url arguments passed by the user"""
        get_url_parser = subparsers.include(command)
        get_url_parser.add_argument('--filename', '-f',
                                    help='name of the file')

