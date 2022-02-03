from pythontabcmd2.parsers import parent_parser as parent_parser
import argparse

"""
set up the arguments needed for each command given a commandmap value:
command[0] = command-name
command[1] = command method
command[2] = command help text
"""

class Subparsers():

    def __init__(self):
        self.global_options = argparse.ArgumentParser(add_help=False)
        parent_parser.add_global_options(self.global_options)
        self.root = argparse.ArgumentParser(parents=[self.global_options])
        # https://stackoverflow.com/questions/7498595/python-argparse-add-argument-to-multiple-subparsers
        # self.global_options = argparse.ArgumentParser(add_help=False)
        self.subparsers = self.root.add_subparsers()

    def get_root_parser(self):
        return self.root

    def include(self, command):
        additional_parser = self.subparsers.add_parser(command[0],
            help=command[2], parents=[self.global_options])
        additional_parser.set_defaults(func=command[1])
        return additional_parser
