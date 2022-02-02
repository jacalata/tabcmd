from .parser_config import *


class DecryptExtractsParser:
    """
    Parser for the command decryptextracts
    """
    @staticmethod
    def decrypt_extracts_parser(subparsers, command):
        """Method to parse decrypt extracts arguments passed by the user"""
       
        decrypt_extract_parser = subparsers.include(command)

