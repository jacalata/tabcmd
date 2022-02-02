import tableauserverclient as TSC
from .. import log
from ... import Session
from .datasources_and_workbooks_command import DatasourcesAndWorkbooks


class RunSchedule(DatasourcesAndWorkbooks):
    """
    This command runs the specified schedule as it is on the server.
    """
    def __init__(self, args, schedule):
        super().__init__(args)
        self.schedule = schedule
        self.logging_level = args.logging_level
        self.logger = log('pythontabcmd2.runschedule_command',
                          self.logging_level)


    def run_command(self, args):
        session = Session()
        server_object = session.create_session(args)
        self.run_schedule(server_object)

    def run_schedule(self, server):
        pass
