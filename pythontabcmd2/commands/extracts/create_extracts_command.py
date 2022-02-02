import tableauserverclient as TSC
from .. import log
from ... import Session


class CreateExtracts:
    def __init__(self, args):
        self.args = args
        self.logging_level = args.logging_level
        self.logger = log('pythontabcmd2.createextracts_command',
                          self.logging_level)

    def run_command(self, args):
        session = Session()
        server_object = session.create_session(args)
        self.create_extract(server_object)

    def create_extract(self, server):
        pass
