from .parent_parser import *
class EditSiteParser:
    """
    Parser for the command editsite
    """
    @staticmethod
    def edit_site_parser(subparsers, command):
        """Method to parse edit site arguments passed by the user"""
        edit_site_parser = subparsers.include(command)
        edit_site_parser.add_argument('sitename', help='name of the site to edit')
        
        set_site_args(edit_site_parser)
        set_site_id_arg(edit_site_parser)
        set_site_status_arg(edit_site_parser)

