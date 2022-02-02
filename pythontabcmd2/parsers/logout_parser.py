class LogoutParser:
    """ Parses logout arguments passed by the user"""
    @staticmethod
    def logout_parser(subparsers, command):
        logout_parser = subparsers.include(command)

