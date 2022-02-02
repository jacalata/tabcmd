from .parent_parser import *
class EditSiteParser:
    """
    Parser for the command editsite
    """
    @staticmethod
    def edit_site_parser(subparsers, command):
        """Method to parse edit site arguments passed by the user"""
        edit_site_parser = subparsers.include(command)
        set_site_args(edit_site_parser)
