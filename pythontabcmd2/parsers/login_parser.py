
class LoginParser:
    """ Parses login arguments passed by the user"""
    @staticmethod
    def login_parser(subparsers, command):
        login_parser = subparsers.include(command)
        # asking for arguments we need is done in Session as we try to log in
