from pythontabcmd2.parsers import parent_parser, create

def mock_command_action():
    print('a mockery!')

def initialize_test_pieces(commandname):
    manager = create.Subparsers()
    parser = manager.get_root_parser()
    mock_command = commandname, mock_command_action, 'mock help text'
    return parser, manager, mock_command

"""
 base test cases for each parser:
 has_required_arguments
 (maybe) missing required arguments
 has optional arguments
 bad mix of optional arguments
 has unknown arguments
 """

