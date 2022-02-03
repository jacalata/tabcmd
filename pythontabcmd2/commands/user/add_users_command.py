from pythontabcmd2.commands.user.user_data import Userdata
from ..commands import Commands
import tableauserverclient as TSC
from .. import log
from ... import Session


class AddUserCommand():
    """
    Command to Adds users to a specified group
    """
    def __init__(self, args):
        self.args = args
        self.group = args.groupname
        self.logger = log('pythontabcmd2.add_user_command',
                          args.logging_level)

    def run_command(self, args):
        session = Session()
        server_object = session.create_session(args)
        self.add_users(server_object, args.users, args.groupname)

    def add_users(self, server_object, csv_lines, group_name):
        self.add_user_command(server_object, csv_lines, group_name)

    def add_user_command(self, server, csv_lines, group_name):
        """Method to add users to a group using Tableauserverclient methods"""
        command = Commands(self.args)
        user_obj_list = command.get_user(csv_lines)
        for user_obj in user_obj_list:
            username = user_obj.username
            user_id = Userdata.find_user_id(server, username)
            group = Userdata.find_group(server, group_name)
            try:
                server.groups.add_user(group, user_id)
                self.logger.info("Successfully added")
            except TSC.ServerResponseError as e:
                self.logger.error("Error: Server error occurred", e)
                # TODO Map Error code
