from .parent_parser import *
class DeleteExtractsParser:
    """
    Parser for the command delete extracts
    """
    @staticmethod
    def delete_extracts_parser(subparsers, command):

          delete_extract_parser = subparsers.include(command)
          set_datasource_arg(delete_extract_parser)
          set_embedded_datasources_option(delete_extract_parser)
          set_encryption_option(delete_extract_parser)
          set_project_N_arg(delete_extract_parser)
          set_url_arg(delete_extract_parser)
          set_workbook_arg(delete_extract_parser)

