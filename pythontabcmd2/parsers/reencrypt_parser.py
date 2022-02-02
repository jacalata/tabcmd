

class ReencryptExtractsParser:
    """
    Parser to reencrypt command
    """
    @staticmethod
    def reencrypt_extracts_parser(subparsers, command):
        """Method to parse reencrypt extracts arguments passed by the user"""

        reencrypt_extract_parser = subparsers.include(command)
        
