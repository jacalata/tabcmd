
from .parent_parser import *


class DeleteParser:
    """Parser for the command delete"""
    @staticmethod
    def delete_parser(subparsers, command):
        """Method to parse delete data source arguments passed by the user"""

        delete_parser = subparsers.include(command)
        set_project_R_arg(delete_parser)
        # todo: should be required to have EITHER ds OR wb
        set_datasource_arg(delete_parser)
        set_workbook_arg(delete_parser)
        set_embedded_datasources_option(delete_parser)
        set_parent_project_arg(delete_parser)
        # no-wait?

