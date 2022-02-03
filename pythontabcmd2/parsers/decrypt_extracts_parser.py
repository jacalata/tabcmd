from .parent_parser import *


class DecryptExtractsParser:
    """
    Parser for the command decryptextracts
    """
    @staticmethod
    def decrypt_extracts_parser(subparsers, command):
        """Method to parse decrypt extracts arguments passed by the user"""
       
        decrypt_extract_parser = subparsers.include(command)
        decrypt_extract_parser.add_argument('sitename', default=None, help='Name of site to delete')

