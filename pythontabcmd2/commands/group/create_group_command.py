
from .group_command import GroupCommand
import tableauserverclient as TSC
from .. import log
from ... import Session


class CreateGroupCommand(GroupCommand):
    """
    This command is used to create a group
    """
    def __init__(self, args):
        super().__init__(args)
        self.logger = log('pythontabcmd2.create_group_command',
                          self.logging_level)

    def run_command(self, args):
        session = Session()
        server_object = session.create_session(args)
        self.create_group(server_object)

    def create_group(self, server):
        """Method to create group using Tableauserverclient methods"""
        try:
            new_group = TSC.GroupItem(self.name)
            server.groups.create(new_group)
            self.logger.info("Successfully created group")
        except TSC.ServerResponseError as e:
            self.logger.error("Group already exists")
