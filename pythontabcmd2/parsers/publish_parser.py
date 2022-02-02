

class PublishParser():
    """Parser to the command publish"""
    @staticmethod
    def publish_parser(subparsers, command):
    
        publish_parser = subparsers.include(command)
        publish_parser.add_argument('name',
                                    help='Name of the workbook or '
                                         'data source on the server')
        publish_parser.add_argument('--overwrite', '-o', action='store_true',
                                    help='Overwrites the workbook, '
                                         'data source, or data extract '
                                         'if it already exists on '
                                         'the server.')
        # make overwrite and append flags mutually exclusive
        publish_parser.add_argument('--project', '-r', default=None,
                                    help='Publishes the workbook, '
                                         'data source, or data extract'
                                         ' into the specified project')
        publish_parser.add_argument('--db-username',
                                    help='Use this option to publish a '
                                         'database user name with the '
                                         'workbook,'
                                         ' data source, or data extract.')
        publish_parser.add_argument('--db-password',
                                    help=' publish a database password '
                                         'with the workbook, data source, '
                                         'or extract')
        publish_parser.add_argument('--tabbed', action='store_true',
                                    help='When a workbook with tabbed '
                                         'views is published, each sheet'
                                         ' becomes a tab that viewers can '
                                         'use to navigate through '
                                         'the workbook')


