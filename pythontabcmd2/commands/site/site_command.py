from ..commands import Commands


class SiteCommand(Commands):



    @staticmethod
    def find_site_id(server, site_name):
        """ Method to find the site id given site name"""
        all_sites, pagination_item = server.sites.get()
        all_site_names_ids = [(site.name, site.id) for site in all_sites]
        site_id = None
        for site in all_site_names_ids:
            if site[0] == site_name:
                site_id = site[1]
                break
        return site_id


    @staticmethod
    def get_site_mode(args):
        if args.site_admin_user_management:
            return 'ContentAndUsers'
        else:
            return 'ContentOnly'