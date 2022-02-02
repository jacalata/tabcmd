from .parser_config import *

class CreateExtractsParser:
    """
    Parser for parser.xtracts command
    """
    @staticmethod
    def create_extracts_parser(subparsers, command):

        create_extract_parser = subparsers.include(command)
        create_extract_parser.add_argument('--datasource', '-d',
                                           help='name of datasource')
        create_extract_parser.add_argument('--embedded-datasources',
                                           help='A space-separated list'
                                                'of embedded data source '
                                                'names within the target'
                                                ' workbook. ')
        create_extract_parser.add_argument('--encrypt',
                                           help='parser.encrypted extract')
        create_extract_parser.add_argument('--include-all',
                                           help='Include all embedded data '
                                                'sources within target'
                                                ' workbook. Only available '
                                                'when creating extracts '
                                                'for workbook.')
        create_extract_parser.add_argument('--project',
                                           help='The name of the project'
                                                ' that contains the target '
                                                'resource')
        create_extract_parser.add_argument('--url',
                                           help='The canonical name for the '
                                                'resource as it appears'
                                                ' in the URL')
        create_extract_parser.add_argument('--workbook', '-w',
                                           help='The name of the target '
                                                'workbook for extract '
                                                'creation.')

