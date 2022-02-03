from .parent_parser import *

class CreateSiteUsersParser:
    """
    Parser for the command CreateSiteUsers
    """
    @staticmethod
    def create_site_users_parser(subparsers, command):
        """Method to parse create user arguments passed """

        create_site_users_parser = subparsers.include(command)
        set_users_file_positional(create_site_users_parser)
        set_role_arg(create_site_users_parser)
        set_no_wait_option(create_site_users_parser)
        set_completeness_options(create_site_users_parser)
        set_silent_option(create_site_users_parser)


