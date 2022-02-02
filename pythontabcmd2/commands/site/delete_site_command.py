from .site_command import SiteCommand
import tableauserverclient as TSC
from .. import log
from ... import Session


class DeleteSiteCommand(SiteCommand):
    """
    Command to delete a site
    """
    def __init__(self, args):
        super().__init__(args)
        self.logger = log('pythontabcmd2.delete_site_command',
                          self.logging_level)


    def run_command(self, args):
        session = Session()
        server_object = session.create_session(args)
        self.delete_site(server_object, args.sitename)

    def delete_site(self, server, site_name):
        """Method to delete a site using tableauserverclient methods"""
        self.delete_site_helper(server, site_name)

    def delete_site_helper(self, server, site_name):
        """ Helper method to catch server errors thrown
        by tableauserverclient"""
        site_id = SiteCommand.find_site_id(server, self.args.site_name)
        try:
            server.sites.delete(site_id)
            self.logger.info('Successfully deleted the site')
        except TSC.ServerResponseError as e:
            print(e)
