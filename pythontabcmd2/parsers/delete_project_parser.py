
from .parent_parser import *

class DeleteProjectParser:
    """
    Parser for the command deleteproject
    """
    @staticmethod
    def delete_project_parser(subparsers, command):
        """Method to parse delete project arguments passed by the user"""

        delete_project_parser = subparsers.include(command)
        delete_project_parser.add_argument('projectname', help='name of project to delete')
        set_parent_project_arg(delete_project_parser)
