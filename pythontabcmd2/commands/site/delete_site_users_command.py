from pythontabcmd2.commands.user import user_data
from ..commands import Commands
import tableauserverclient as TSC
from .. import log
from ... import Session
from .site_command import SiteCommand


class DeleteSiteUsersCommand(SiteCommand):
    """
    Command to Remove users from from the site that user is logged in to.
    The users to be removed are specified in a file that contains
    a simple list of one user name per line.
    """
    def __init__(self, args):
        super().__init__(args)
        self.logger = log('pythontabcmd2.delete_site_users_command',
                          self.logging_level)


    def run_command(self, args):
        session = Session()
        server_object = session.create_session(self.args)
        self.delete_users(server_object, args.users)

    def delete_users(self, server_object, csv_lines):
        self.delete_user_command(server_object, csv_lines)

    def delete_user_command(self, server, csv_lines):
        """Method to delete users using Tableauserverclient methods"""
        number_of_users_deleted = 0
        command = Commands(self.args)
        user_obj_list = command.get_user(csv_lines)
        self.logger.info("======== 0% complete ========")
        for user_obj in user_obj_list:
            username = user_obj.username
            user_id = user_data.find_user_id(server, username)
            try:
                server.users.remove(user_id)
                self.logger.info("Successfully deleted user from site: {}".
                                 format(username))
                number_of_users_deleted += 1
            except TSC.ServerResponseError as e:
                self.logger.error(" Server error occurred", e)
                # TODO Map Error code
            except ValueError:
                self.logger.error(" Could not delete user: User {} not "
                                  "found".format(username))
        self.logger.info("======== 100% complete ========")
        self.logger.info("======== Number of users deleted from site: {} "
                         "=========".
                         format(number_of_users_deleted))
