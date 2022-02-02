from .parent_parser import *



class PublishSamplesParser():
    """
    Parser to the command publishsamples
    """
    @staticmethod
    def publish_samples_parser(subparsers, command):
        """Method to parse publish samples arguments passed by the user"""
        publish_samples_parser = subparsers.include(command)
        set_project_N_arg(publish_samples_parser)
        set_parent_project_arg(publish_samples_parser)