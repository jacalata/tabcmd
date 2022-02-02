from pythontabcmd2.parsers import parent_parser as parent_parser


"""
set up the arguments needed for each command given a commandmap value:
command[0] = command-name
command[1] = command method
command[2] = command help text
"""

class Subparsers():

    def __init__(self, main_parser=None):
        if main_parser is None:
            main_parser = parent_parser.initialize_parser() # tests don't usually need a ref to this
        self.parent = main_parser

        self.subparsers = self.parent.add_subparsers()

        self.global_options = parent_parser.initialize_parser()
        parent_parser.add_global_options(self.global_options)

    def include(self, command):
        additional_parser = self.subparsers.add_parser(command[0], help=command[2], parents=[self.global_options])
        additional_parser.set_defaults(func=command[1])
        return additional_parser
