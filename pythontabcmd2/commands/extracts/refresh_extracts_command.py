import tableauserverclient as TSC
from .. import log
from ... import Session


class RefreshExtracts:
    def __init__(self, args):
        self.args = args
        self.logging_level = args.logging_level
        self.logger = log('pythontabcmd2.refreshextract_command',
                          self.logging_level)


    def run_command(self, args):
        session = Session()
        server_object = session.create_session(args)
        self.refresh_extracts(server_object)

    def refresh_extracts(self, server):
        pass
