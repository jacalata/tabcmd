import logging

from pythontabcmd2.parsers.global_options import Arguments
from .map_of_commands import CommandsMap
from .commands.auth.login_command import *
from .commands.project.create_project_command import *
from .commands.project.delete_project_command import *
from .commands.group.delete_group_command import *
from .commands.group.create_group_command import *
from .commands.user.remove_users_command import *
from .commands.auth.logout_command import *
from .commands.user.add_users_command import *
from .commands.site.create_site_command import *
from .commands.user.create_site_users import *
from .commands.site.delete_site_command import *
from .commands.site.delete_site_users_command import *
from .commands.site.edit_site_command import *
from .commands.site.list_sites_command import *
from .commands.datasources_and_workbooks.delete_command import *
from .commands.datasources_and_workbooks.export_command import *
from .commands.datasources_and_workbooks.publish_command import *
from .commands.datasources_and_workbooks.get_url_command import *
from .parsers.parent_parser import ParentParser

from .logger_config import get_logger

class Context:

    def logger():
        return get_logger(__name__, 'debug')

    def initialize_parsers():
        parser = ParentParser.initialize_parser()

        subparsers = parser.add_subparsers(help='tabcmd commands', dest='command')
        AddUserParser.add_user_parser(subparsers)
        CreateProjectParser.create_project_parser(subparsers)
        CreateGroupParser.with_create_group_command(subparsers)

        ParentParser.add_global_options(parser)
        return parser

    # allow passing in test inputs
    def parse_inputs(parser, input=None):
        if input is not None:
            print('testing:', input)
        args = parser.parse_args(input)
        return args

    def execute_command(command_name, args):
        Context.logger().debug("execute_command:", command_name, sys.modules[__name__])
        command_object = getattr(sys.modules[__name__],
                                        CommandsMap.commands_hash_map.
                                        get(command_name))
        command_strategy = command_object.parse()
        command_strategy.run_command()



