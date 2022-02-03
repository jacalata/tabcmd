from .parent_parser import *

class EncryptExtractsParser:
    """
    Parser for the command encryptextracts
    """
    @staticmethod
    def encrypt_extracts_parser(subparsers, command):
        """Method to parse encrypt extracts arguments passed by the user"""

        encrypt_extract_parser = subparsers.include(command)
        encrypt_extract_parser.add_argument('sitename', help='name of the site to upate')
