from .parser_config import *

class EncryptExtractsParser:
    """
    Parser for the command encryptextracts
    """
    @staticmethod
    def encrypt_extracts_parser(subparsers, command):
        """Method to parse encrypt extracts arguments passed by the user"""
        encrypt_extract_parser = subparsers.include(command)