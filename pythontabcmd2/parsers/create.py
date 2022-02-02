import pythontabcmd2.parsers.parser_config as parser_config


"""
set up the arguments needed for each command given a commandmap value:
command[0] = command-name
command[1] = command method
command[2] = command help text
"""

class Subparsers():

    def __init__(self, parent_parser=None):
        if parent_parser is None:
            parent_parser = parser_config.initialize_parser() # tests don't usually need a ref to this
        self.parent = parent_parser

        self.subparsers = self.parent.add_subparsers()

        self.global_options = parser_config.initialize_parser()
        parser_config.add_global_options(self.global_options)

    def include(self, command):
        additional_parser = self.subparsers.add_parser(command[0], help=command[2], parents=[self.global_options])
        additional_parser.set_defaults(func=command[1])
        return additional_parser


##### individual commands defined: these are not being used currently


    def add_user_parser(self, command):
        add_user_parser = self.subparsers.add_parser(command[0], help=command[2]) #, parents=[self.global_options])
        parser_config.set_users_file_positional(add_user_parser)
        # is there a difference to doing this instead of setting it in the line above?
        add_user_parser.set_defaults(func=command[1])

    def create_group_parser(self, command):
        create_group_parser = self.subparsers.add_parser(command[0], help=command[2], parents=[self.global_options])
        create_group_parser.add_argument('groupname', help='name of group')
        create_group_parser.set_defaults(func=command[1])

    def create_project_parser(self, command):
        add_project_parser = self.subparsers.add_parser(command[0], help=command[2], parents=[self.global_options])
        add_project_parser.add_argument('projectname', help='name of project')
        parser_config.set_description_arg(add_project_parser)
        parser_config.set_parent_project_arg(add_project_parser)
        add_project_parser.add_argument('--content-permission',  default=None,  help='content permission ')
        add_project_parser.set_defaults(func=command[1])


    def create_site_parser(self, command):
        create_site_parser = self.subparsers.add_parser(command[0], help=command[2], parents=[self.global_options])
        create_site_parser.add_argument('sitename', help='name of site')
        parser_config.set_site_args(create_site_parser)
        parser_config.set_content_url_arg(create_site_parser)
        create_site_parser.set_defaults(func=command[1])


    def create_site_user_parser(self, command):
        add_site_users_parser = self.subparsers.add_parser(command[0], help=command[2], parents=[self.global_options])
        parser_config.set_role_arg(add_site_users_parser)
        parser_config.set_users_file_arg(add_site_users_parser)
        parser_config.set_no_wait_option(add_site_users_parser)
        parser_config.set_completeness_options(add_site_users_parser)
        parser_config.set_silent_option(add_site_users_parser)
        add_site_users_parser.set_defaults(func=command[1])


    def create_user_parser(self, command):
        add_users_parser = self.subparsers.add_parser(command[0], help=command[2], parents=[self.global_options])
        parser_config.set_users_file_arg(add_users_parser)
        add_users_parser.set_defaults(func=command[1])


    def decrypt_extracts_parser(self, command):
        decrypt_extract_parser = self.subparsers.add_parser(command[0], help=command[2], parents=[self.global_options])
        parser_config.set_workbook_arg(decrypt_extract_parser)
        parser_config.set_datasource_arg(decrypt_extract_parser)
        parser_config.set_project_R_arg(decrypt_extract_parser)
        parser_config.set_parent_project_arg(decrypt_extract_parser)
        parser_config.set_embedded_datasources_option(decrypt_extract_parser)
        # missing some here
        decrypt_extract_parser.set_defaults(func=command[1])

    def delete_parser(self, command):
        delete_parser = self.subparsers.add_parser(command[0], help=command[2], parents=[self.global_options])
        parser_config.set_project_R_arg(delete_parser)
        parser_config.set_datasource_arg(delete_parser)
        parser_config.set_workbook_arg(delete_parser)
        parser_config.set_embedded_datasources_option(delete_parser)
        parser_config.set_parent_project_arg(delete_parser)
        # no-wait?
        delete_parser.set_defaults(func=command[1])

    def delete_group_parser(self, command):
        delete_group_parser = self.subparsers.add_parser(command[0], help=command[2], parents=[self.global_options])
        delete_group_parser.add_argument('groupname', help='name of group to delete')
        delete_group_parser.set_defaults(func=command[1])

    def delete_project_parser(self, command):
        delete_project_parser = self.subparsers.add_parser(command[0], help=command[2], parents=[self.global_options])
        delete_project_parser.add_argument('projectname', help='name of project to delete')
        parser_config.set_parent_project_arg(delete_project_parser)
        delete_project_parser.set_defaults(func=command[1])

    def delete_site_parser(self, command):
        delete_site_parser = self.subparsers.add_parser(command[0], help=command[2], parents=[self.global_options])
        delete_site_parser.add_argument('sitename', default=None, help='Name of site to delete')
        delete_site_parser.set_defaults(func=command[1])

    def delete_site_users_parser(self, command):
        delete_site_users_parser = self.subparsers.add_parser(command[0], help=command[2], parents=[self.global_options])
        parser_config.set_users_file_arg(delete_site_users_parser)
        delete_site_users_parser.set_defaults(func=command[1])

    def edit_site_parser(self, command):
        edit_site_parser = self.subparsers.add_parser(command[0], help=command[2], parents=[self.global_options])
        parser_config.set_site_args(edit_site_parser)
        parser_config.set_site_id_arg(edit_site_parser)
        parser_config.set_site_status_arg(edit_site_parser)
        edit_site_parser.set_defaults(func=command[1])

    def encrypt_extracts_parser(self, command):
        encrypt_extract_parser = self.subparsers.add_parser(command[0], help=command[2], parents=[self.global_options])
        # missing stuff here?
        encrypt_extract_parser.set_defaults(func=command[1])

    def get_url_parser(self, command):
        get_url_parser = self.subparsers.add_parser(command[0], help=command[2], parents=[self.global_options])
        get_url_parser.add_argument('url', help='name of the file on Tableau Server to download')
        get_url_parser.set_defaults(func=command[1])

    def list_site_parser(self, command):
        list_site_parser = self.subparsers.add_parser(command[0], help=command[2], parents=[self.global_options])
        parser_config.set_encryption_option(list_site_parser)
        list_site_parser.set_defaults(func=command[1])

    def login_parser(self, command):
        login_parser = self.subparsers.add_parser(command[0], help=command[2], parents=[self.global_options])
        login_parser.set_defaults(func=command[1])

    def logout_parser(self, command):
        logout_parser = self.subparsers.add_parser(command[0], help=command[2], parents=[self.global_options])
        logout_parser.set_defaults(func=command[1])

    def publish_samples_parser(self, command):
        publish_samples_parser = self.subparsers.add_parser(command[0], help=command[2], parents=[self.global_options])
        parser_config.set_project_N_arg(publish_samples_parser)
        parser_config.set_parent_project_arg(publish_samples_parser)
        publish_samples_parser.set_defaults(func=command[1])

    def reencrypt_extracts_parser(self, command):
        reencrypt_extract_parser = self.subparsers.add_parser(command[0], help=command[2], parents=[self.global_options])
        reencrypt_extract_parser.set_defaults(func=command[1])

    def refresh_extracts_parser(self, command):
        refresh_extract_parser = self.subparsers.add_parser(command[0], help=command[2], parents=[self.global_options])
        parser_config.set_datasource_arg(refresh_extract_parser)
        parser_config.set_workbook_arg(refresh_extract_parser)
        parser_config.set_incremental_option(refresh_extract_parser)
        parser_config.set_sync_option(refresh_extract_parser)
        parser_config.set_calculations_options(refresh_extract_parser)
        parser_config.set_project_N_arg(refresh_extract_parser)
        parser_config.set_parent_project_arg(refresh_extract_parser)
        parser_config.set_url_arg(refresh_extract_parser)
        refresh_extract_parser.set_defaults(func=command[1])

    def remove_user_parser(self, command):
        remove_users_parser = self.subparsers.add_parser(command[0], help=command[2], parents=[self.global_options])
        remove_users_parser.add_argument('groupname', help='name of group')
        parser_config.set_users_file_arg(remove_users_parser)
        remove_users_parser.set_defaults(func=command[1])

    def runschedule_parser(self, command):
        runschedule_parser = self.subparsers.add_parser(command[0], help=command[2], parents=[self.global_options])
        runschedule_parser.add_argument('schedulename', help='name of schedule')
        runschedule_parser.set_defaults(func=command[1])
