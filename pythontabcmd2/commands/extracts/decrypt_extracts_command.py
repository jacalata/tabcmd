import tableauserverclient as TSC
from .. import log
from ... import Session


class DecryptExtracts:
    def __init__(self, args, site_name):
        self.site_name = site_name
        self.args = args
        self.logging_level = args.logging_level
        self.logger = log('pythontabcmd2.decryptextracts_command',
                          self.logging_level)


    def run_command(self, args):
        session = Session()
        server_object = session.create_session(args)
        self.decrypt_extract(server_object)

    def decrypt_extract(self, server):
        pass
