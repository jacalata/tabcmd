from pythontabcmd2.parsers import parent_parser, create

def mock_command_action():
    print('a mockery!')

def initialize_test_pieces(commandname):
    parser = parent_parser.initialize_parser()
    subparsers = create.Subparsers(parser)
    mock_command = commandname, mock_command_action, 'mock help text'
    return parser, subparsers, mock_command

"""
 base test cases for each parser:
 has_required_arguments
 (maybe) missing required arguments
 has optional arguments
 bad mix of optional arguments
 has unknown arguments
 """

class GlobalOptionsTest():


    def test_missing_server(self):
        args = LogoutParser.logout_parser()
        assert args == argparse.Namespace(
                                          username="helloworld",
                                          site="",
                                          logging_level="info",
                                          password="testing123",
                                          no_prompt=True, token=None,
                                          token_name=None,
                                          cookie=True,
                                          no_cookie=False,
                                          prompt=False)


    def test_username(self):
        args = LogoutParser.logout_parser()
        assert args == argparse.Namespace(
            site="",
            logging_level="info",
            password="testing123",
            no_prompt=True, token=None,
            token_name=None,
            cookie=True,
            no_cookie=False,
            prompt=False)
