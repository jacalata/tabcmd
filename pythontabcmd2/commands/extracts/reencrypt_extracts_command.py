import tableauserverclient as TSC
from .. import log
from ... import Session


class ReencryptExtracts:
    def __init__(self, args, site_name):
        self.site_name = site_name
        self.args = args
        self.logging_level = args.logging_level
        self.logger = log('pythontabcmd2.reencryptextracts_command',
                          self.logging_level)

    def run_command(self, args):
        session = Session()
        server_object = session.create_session(args)
        self.reencrypt_extract(server_object)

    def reencrypt_extract(self, server):
        pass
