from .commands.auth.login_command import *
from .commands.project.create_project_command import *
from .commands.project.delete_project_command import *
from .commands.project.publish_samples_command import *
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
from .commands.datasources_and_workbooks.runschedule_command import *
from .commands.datasources_and_workbooks.get_url_command import *
from .commands.extracts.create_extracts_command import *
from .commands.extracts.decrypt_extracts_command import *
from .commands.extracts.delete_extracts_command import *
from .commands.extracts.encrypt_extracts_command import *
from .commands.extracts.reencrypt_extracts_command import *
from .commands.extracts.refresh_extracts_command import *


class CommandsMap:

    # command-name: (commandname-exactly-as-typed, command method, command help text)
    def login():
        return "login", LoginCommand, "Sign in to the server"

    def get():
        return "get", GetUrl, "Get a file from the server"

    def create_project():
        return "createproject", CreateProjectCommand, "Create a project"

    def delete_project():
        return "deleteproject", DeleteProjectCommand, "Delete a project"

    def create_group():
        return "creategroup", CreateGroupCommand, "Create a local group"

    def delete_group():
        return "deletegroup", DeleteGroupCommand, "Delete a group"

    def create_site_users():
        return "createsiteusers", CreateSiteUsersCommand, "Create users on a site"

    def remove_users():
        return "removeusers", RemoveUserCommand, "Remove users from a group"

    def export():
        return "export", ExportCommand, "Export the data or image of a view from the server"

    def logout():
        return "logout", LogoutCommand, "Sign out from the server"

    def add_users():
        return "addusers", AddUserCommand, "Add users to a group"

    def create_site_users():
        return "createsiteusers", CreateSiteUsersCommand, "Create users on the current site"

    def create_site():
        return "createsite", CreateSiteCommand, "Create a site"

    def delete_site():
        return "deletesite", DeleteSiteCommand, "Delete a site"

    def delete_site_users():
        return "deletesiteusers", DeleteSiteUsersCommand, "Delete site users"

    def edit_sites():
        return "editsite", EditSiteCommand, "Edit a site"

    def list_sites():
        return "listsites", ListSiteCommand, "List sites for user"

    def delete():
        return "delete", DeleteCommand, "Delete a workbook or data source from the server"

    def publish():
        return "publish", PublishCommand, "Publish a workbook, data source, or extract to the server"

    def create_extracts():
        return "createextracts", CreateExtracts, "Create extracts for a published workbook or data source"

    def decrypt_extracts():
        return "decryptextracts", DecryptExtracts, "Decrypt extracts on a site"

    def delete_extracts():
        return "deleteextracts", DeleteExtracts, "Delete extracts for a published workbook or data source"

    def encrypt_extracts():
        return "encryptextracts", EncryptExtracts, "Encrypt extracts on a site"

    def reencrypt_extracts():
        return "reencryptextracts", ReencryptExtracts, "Reencrypt extracts on a site"

    def refresh_extracts():
        return "refreshextracts", RefreshExtracts, "Refresh the extracts of a workbook or datasource on the server"

    def publish_samples():
        return "publishsamples", PublishSamplesCommand, "publish samples to the server"

        # def help():
        # "help", HelpCommand, "Help for tabcmd commands"