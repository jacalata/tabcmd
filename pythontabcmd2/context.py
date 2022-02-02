from .map_of_commands import CommandsMap

from .parsers import create
from .parsers import parent_parser
from .parsers.add_users_parser import AddUserParser
from .parsers.create_extracts_parser import CreateExtractsParser
from .parsers.create_group_parser import CreateGroupParser
from .parsers.create_project_parser import CreateProjectParser
from .parsers.create_site_parser import CreateSiteParser
from .parsers.create_site_users_parser import CreateSiteUsersParser
from .parsers.decrypt_extracts_parser import DecryptExtractsParser
from .parsers.delete_extracts_parser import DeleteExtractsParser
from .parsers.delete_group_parser import DeleteGroupParser
from .parsers.delete_parser import DeleteParser
from .parsers.delete_project_parser import DeleteProjectParser
from .parsers.delete_site_parser import DeleteSiteParser
from .parsers.delete_site_users_parser import DeleteSiteUsersParser
from .parsers.edit_site_parser import EditSiteParser
from .parsers.encrypt_extracts_parser import EncryptExtractsParser
from .parsers.export_parser import ExportParser
from .parsers.get_url_parser import GetUrlParser
from .parsers.list_sites_parser import ListSitesParser
from .parsers.login_parser import LoginParser
from .parsers.logout_parser import LogoutParser
from .parsers.publish_parser import PublishParser
from .parsers.publish_samples_parser import PublishSamplesParser
from .parsers.reencrypt_parser import ReencryptExtractsParser
from .parsers.refresh_extracts_parser import RefreshExtractsParser
from .parsers.remove_users_parser import RemoveUserParser

from .logger_config import get_logger

class Context:

    def logger():
        return get_logger(__name__, 'debug')

    def initialize_parsers():
        parent = parent_parser.initialize_parser()
        subparsers = create.Subparsers(parent)

        AddUserParser.add_user_parser(subparsers, CommandsMap.add_users())

        CreateExtractsParser.create_extracts_parser(subparsers, CommandsMap.create_extracts())
        DeleteExtractsParser.delete_extracts_parser(subparsers, CommandsMap.delete_extracts())

        CreateGroupParser.create_group_parser(subparsers, CommandsMap.create_group())
        CreateProjectParser.create_project_parser(subparsers, CommandsMap.create_project())
        CreateSiteParser.create_site_parser(subparsers, CommandsMap.create_site())
        CreateSiteUsersParser.create_site_users_parser(subparsers, CommandsMap.create_site_users())
        # parser.parser.user_parser(subparsers, CommandsMap.parser.users())

        DecryptExtractsParser.decrypt_extracts_parser(subparsers, CommandsMap.decrypt_extracts())
        DeleteGroupParser.delete_group_parser(subparsers, CommandsMap.delete_group())
        DeleteParser.delete_parser(subparsers, CommandsMap.delete())
        DeleteProjectParser.delete_project_parser(subparsers, CommandsMap.delete_project())
        DeleteSiteParser.delete_site_parser(subparsers, CommandsMap.delete_site())
        DeleteSiteUsersParser.delete_site_users_parser(subparsers, CommandsMap.delete_site_users())

        EditSiteParser.edit_site_parser(subparsers, CommandsMap.edit_sites())
        EncryptExtractsParser.encrypt_extracts_parser(subparsers, CommandsMap.encrypt_extracts())
        ExportParser.export_parser(subparsers, CommandsMap.export())

        GetUrlParser.get_url_parser(subparsers, CommandsMap.get())

        ListSitesParser.list_site_parser(subparsers, CommandsMap.list_sites())
        LoginParser.login_parser(subparsers, CommandsMap.login())
        LogoutParser.logout_parser(subparsers, CommandsMap.logout())

        PublishParser.publish_parser(subparsers, CommandsMap.publish())
        PublishSamplesParser.publish_samples_parser(subparsers, CommandsMap.publish_samples())

        ReencryptExtractsParser.reencrypt_extracts_parser(subparsers, CommandsMap.reencrypt_extracts())
        RefreshExtractsParser.refresh_extracts_parser(subparsers, CommandsMap.refresh_extracts())
        RemoveUserParser.remove_user_parser(subparsers, CommandsMap.remove_users())
        # parsers.runschedule_parser(subparsers, CommandsMap.run_schedule())

        return parent

    # allow passing in test inputs
    def parse_inputs(parser, input=None):
        namespace = parser.parse_args(input)
        print(namespace)
        # if a subcommand was identified, call the function assigned to it
        # https://stackoverflow.com/questions/49038616/argparse-subparsers-with-functions

        namespace.func(namespace).run_command(namespace)
        return namespace



