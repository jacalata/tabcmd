from weakref import ref
from .parent_parser import *
class RefreshExtractsParser:
    """
    Parser to refreshextracts command
    """
    @staticmethod
    def refresh_extracts_parser(subparsers, command):
        """Method to parse refresh extracts arguments passed by the user"""
        refresh_extract_parser = subparsers.include(command)

        set_datasource_arg(refresh_extract_parser)
        set_incremental_option(refresh_extract_parser)
        set_sync_option(refresh_extract_parser)
        set_calculations_options(refresh_extract_parser)
        set_project_N_arg(refresh_extract_parser)
        set_url_arg(refresh_extract_parser)
        set_workbook_arg(refresh_extract_parser)
