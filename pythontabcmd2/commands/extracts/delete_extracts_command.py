import tableauserverclient as TSC
from .. import log
from ... import Session


class DeleteExtracts:
    def __init__(self, args):
        self.args = args
        self.logging_level = args.logging_level
        self.logger = log('pythontabcmd2.deleteextracts_command',
                          self.logging_level)

    def run_command(self, args):
        session = Session()
        server_object = session.create_session(args)
        self.delete_extract(server_object)

    def delete_extract(self, server):
        pass
