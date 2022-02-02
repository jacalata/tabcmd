
from .parent_parser import *


class CreateProjectParser():
    """
    Parser for createproject command
    """
    @staticmethod
    def create_project_parser(subparsers, command):
        """Method to parse create project arguments passed by the user"""

        create_project_parser = subparsers.include(command)
        set_project_N_arg(create_project_parser)
        set_description_arg(create_project_parser)
        set_parent_project_arg(create_project_parser)

        create_project_parser.add_argument('--content-permission',
                                           default=None,
                                           help='content permission ')
