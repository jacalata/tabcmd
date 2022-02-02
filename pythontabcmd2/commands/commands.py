from .command_strategy_interface import CommandStrategyInterface
from . import get_logger
logger = get_logger('pythontabcmd2.commands', 'info')


class Commands(CommandStrategyInterface):

    # these should really only be checked for in Session?
    """
        def __init__(self, args):
            self.username = args.username
            self.password = args.password
            self.server = args.server
            self.site = args.site
            self.token_name = args.token_name
            self.personal_token = args.token
            self.logging_level = args.logging_level
    """

