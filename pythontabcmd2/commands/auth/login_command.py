from .. import LoginParser
from .. import log
from ..commands import Commands
from .session import Session


class LoginCommand(Commands):
    """
    Logs in a Tableau Server user.
    """
    def __init__(self, args):
        super().__init__(args)
        self.args = args
        self.logger = log('pythontabcmd2.login_command', self.logging_level)

    def run_command(self, args):
        self.create_session_login_command(args)

    def create_session_login_command(self, args):
        """ Method to authenticate user and establish connection """
        self.logger.info("========Creating a new session========")
        session = Session()
        session.create_session(args)
