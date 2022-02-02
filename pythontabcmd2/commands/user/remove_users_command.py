from ..commands import Commands
import tableauserverclient as TSC
from .. import log
from ... import Session
from .user_data import *


class RemoveUserCommand():
    """
     Command to remove users from the specified group
    """
    def __init__(self, args, csv_lines, group_name):
        super().__init__(csv_lines, args)
        self.args = args
        self.group = group_name
        self.logger = log('pythontabcmd2.remove_users_command',
                          self.logging_level)


    def run_command(self, args):
        session = Session()
        server_object = session.create_session(args)
        self.remove_users(server_object, args.users, args.groupname)

    def remove_users(self, server_object, csv_lines, group_name):
        self.remove_user_command(server_object, csv_lines, group_name)

    def remove_user_command(self, server, csv_lines, group_name):
        """Method to remove users using Tableauserverclient methods"""
        command = Commands(self.args)
        user_obj_list = command.get_user(csv_lines)
        for user_obj in user_obj_list:
            username = user_obj.username
            user_id = find_user_id(server, username)
            group = find_group(server, group_name)
            try:
                server.groups.remove_user(group, user_id)
                self.logger.info("Successfully removed")
            except TSC.ServerResponseError as e:
                self.logger.error("Error: Server error occurred", e)
                # TODO Map Error code
