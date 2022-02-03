from .project_command import *
import tableauserverclient as TSC
from .. import log
from ... import Session


class PublishSamplesCommand(ProjectCommand):
    """
    Command to Publish Tableau Sample workbooks to the specified project.
    Any existing samples will be overwritten.
    """

    def __init__(self, args):
        super().__init__(args)
        self.args = args
        self.logger = log('pythontabcmd2.publish_samples_command',
                          args.logging_level)


    def run_command(self, args):
        session = Session()
        server_object = session.create_session(args)
        self.publish_samples(server_object)

    def publish_samples(self, server):
        """Method to publish samples using tableauserverclient methods"""
        if self.parent_path_name is not None:
            project_path = ProjectCommand. \
                find_project_id(server, self.parent_path_name)
        else:
            project_path = None
