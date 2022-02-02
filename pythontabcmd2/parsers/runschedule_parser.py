import sys

class RunScheduleParser:
    """
    Parser to runschedule command
    """
    @staticmethod
    def runschedule_parser(subparsers, command):
        """Method to parse run-schedule arguments passed by the user"""
        runschedule_parser = subparsers.include(command)
        runschedule_parser.add_argument('schedulename',
            help='Name of the schedule to run')
