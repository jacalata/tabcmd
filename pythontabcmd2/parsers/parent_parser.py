import argparse

"""
parents project path
"""
def add_parent_project_path():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--parent-project-path',
                        default=None,
                        help='path of parent project')
    return parser

"""
Basics of options
- if not otherwise specified, the value passed in with the option will be saved as args.option-name
- all arguments in here are optional: names must be --option-name so users can tell it's optional
- options that just need to turn on or off a flag should be set with action=store_True/False
Method naming conventions
- I have named methods in here aaaa_arg if it returns a value we want, aaa_option if it's a flag
- all methods in here should return a parser for nice fluent chaining
"""

def initialize_parser():
    parser = argparse.ArgumentParser(add_help=False)
    return parser


"""
All these options can be used with any command.
Options are listed here in the same order as the 'global optios' list online at
https://help.tableau.com/current/server/en-us/tabcmd_cmd.htm#options7
"""
def add_global_options(parser):
    # -h/help is implemented by argparse
    parser.add_argument('--certificate', '-c',
        help='Use client certificate to sign in. Required when mutual SSL is enabled.')
    parser.add_argument('--server', '-s',
        help='The Tableau Server URL. e.g. https://online.tableau.com.')

    # TODO: should we make token-name and user-name mutually exclusive?
    parser.add_argument('--username', '-u',
        help='The user name of the user logging in. For Tableau Online, the user name is the users email address.')

    credential_group = parser.add_mutually_exclusive_group()
    credential_group.add_argument('--password', '-p', default=None,
        help='Password for the user specified for --username. If you do not provide a password you will be prompted for one.')
    credential_group.add_argument('--token', '-to', default=None,
        help='personal access token to sign into the server')

    parser.add_argument('--token-name', '-tn',
        help='name of the personal access token used to sign into the server')


    parser.add_argument('--password-file', # type = open file for write?
        help='Allows the password to be stored in the given .txt file rather than the command line for increased security.')
    parser.add_argument('--site', '-t', default='',
        help='Used in the URL to uniquely identify the site.')

    proxy_group = parser.add_mutually_exclusive_group()
    proxy_group.add_argument('--proxy', '-x',
        help='Host:Port. Uses the specified HTTP proxy.')
    proxy_group.add_argument('--no-proxy',
        help='When specified, an HTTP proxy will not be used.')

    parser.add_argument('--no-prompt', action='store_true',
        help='When specified, the command will not prompt for a password. If no valid password is provided the command will fail.')

    parser.add_argument('--no-certcheck', action='store_true',
        help='When specified, tabcmd (the client) does not validate the server\'s SSL certificate.')

    ### store_true means if this flag is seen, this value will be true
    cookie_group = parser.add_mutually_exclusive_group()
    cookie_group.add_argument('--no-cookie', action='store_true',
        help='Use the no- prefix to not save the session ID. By default, the session is saved.')
    cookie_group.add_argument('--cookie', action='store_true',
        help='When specified, the session ID is saved on login so subsequent commands will not need to log in.')
    # TODO: we can use a single variable to save this state
    # parser.add_argument('--cookie', dest='cookie', action='store_true')
    # parser.add_argument('--no-cookie', dest='cookie', action='store_false')
    # parser.set_defaults(cookie=True)

    parser.add_argument('--timeout', # cannot use '-t' because it means site
        help='Waits the specified number of seconds for the server to complete processing the command. \
            By default, the process will wait until the server responds.')

    parser.add_argument('--logging-level', '-l', choices=['debug', 'info', 'error'],
                        default='info',
                        help='desired logging level (set to info by default)')

    # TODO: not quite sure how to implement this one
    # Specifies the end of options on the command line. You can use -- to indicate to tabcmd \
    # that anything that follows -- should not be interpreted as an option setting and can \
    # instead be interpreted as a value for the command.
    # parser.add_argument('--')
    # Argparse alreaday interprets it as 'after this is positional only'

    parser.add_argument('-v', '--version', action='version', version='%(prog)s 2.pre-release')

    return parser



"""
This section is for arguments/sets of arguments that are used by more than one command, but not all of them

"""

# add/parser.remove-user
# parser.users command has a bunch of deprecated options. Just ditch them?
# --admin-type, --[no-]publisher, --[no-]complete (which was ssuuuuubtly different from add-users)

def set_users_file_arg(parser):
    parser.add_argument('--users', type=argparse.FileType('r'),
        help='Remove the users in the given .csv file from the specified group.')
    return parser

def set_users_file_positional(parser):
    parser.add_argument('filename.csv', type=argparse.FileType('r'),
        help='CSV file containing a list of user details.')
    return parser

def set_no_wait_option(parser):
    parser.add_argument('--no-wait', action='store_true', # we wait UNLESS they add this option
        help='Do not wait for asynchronous jobs to complete.')
    return parser

def set_role_arg(parser):
    parser.add_argument('-role',
        choices=['ServerAdministrator', 'SiteAdministratorCreator', 'SiteAdministratorExplorer',
                'SiteAdministrator', 'Creator', 'ExplorerCanPublish', 'Publisher', 'Explorer',
                'Interactor', 'Viewer', 'Unlicensed'],
        help='Specifies a site role for all users in the .csv file.')
    return parser

def set_silent_option(parser):
    parser.add_argument('--silent-progress',
        help='Do not display progress messages for the command.')
    return parser

def set_completeness_options(parser):
    completeness_group = parser.add_mutually_exclusive_group()
    completeness_group.add_argument('--complete', dest='require_all_valid', action='store_true',
        help='Requires that all rows be valid for any change to succeed. If not specified --complete is used.')
    completeness_group.add_argument('--no-complete', dest='require_all_valid', action='store_false',
            help='Requires that all rows be valid for any change to succeed. If not specified --complete is used.')
    completeness_group.set_defaults(require_all_valid=True)
    return parser



# used in parser.delete extract
# docs don't say it, but --embedded-datasources and --include-all could be mutually exclusive
def set_embedded_datasources_option(parser):
    parser.add_argument('--embedded-datasources',
        help='A space-separated list of embedded data source names within the target workbook.')
    parser.add_argument('--include-all',
        help='Include all embedded data sources within target workbook.')
    return parser

# used in parser.extract. listed in delete-extract but makes no sense there
def set_encryption_option(parser):
    parser.add_argument('--encrypt', dest='encrypt_extract', action='store_false',
        help='parser.encrypted extract.')
    return parser



#### item arguments: datasource, workbook, project, url ...
### distinct from all the positional 'name' arguments for e.g deleteproject


# for some reason in parser.project, publish-samples it uses -n for destination project name
# for publish it uses -r for destination project name
# but parser.site uses -r for site-content-url
def set_project_R_arg(parser):
    parser.add_argument('--project', '-r',
        help='The name of the destination project.')
    return parser

def set_project_N_arg(parser):
    parser.add_argument('--project', '-n',
        help='The name of the project.')
    return parser

# the help message for 'datasource' needs to be slightly different for each command
def set_datasource_arg(parser):
    parser.add_argument('--datasource', '-d',
        help='The name of the target data source.')
    return parser

def set_url_arg(parser):
    parser.add_argument('--url',
        help='The canonical name for the resource as it appears in the URL')
    return parser

def set_workbook_arg(parser):
    parser.add_argument('--workbook', '-w',
        help='The name of the target workbook.')
    return parser

# help text is slightly different depending on command in use
def set_description_arg(parser):
    parser.add_argument('--description', '-d',
        help='Specifies a description for the item.')
    return parser




# parser.site/update-site - lots of these options are never used elsewhere

def set_content_url_arg(parser):
    parser.add_argument('--url', '-r',
        help='Used in URLs to specify the site. Different from the site name.')
    return parser
# BUT this seems to be a mismatch between them? site id is listed in edit-site
def set_site_id_arg(parser):
    parser.add_argument('--site-id', help='Used in the URL to uniquely identify the site.')
    return parser

# only in edit-site
def set_site_status_arg(parser):
    parser.add_argument('--status', choices=['ACTIVE', 'SUSPENDED'],
        help='Set to ACTIVE to activate a site, or to SUSPENDED to suspend a site.')
    return parser

# these ones are shared in parser.site and edit-site
def set_site_args(parser):
    parser.add_argument('--user-quota',
        help='Maximum number of users that can be added to the site.')

    site_help = 'Allows or denies site administrators the ability to add users to or remove users from the site.'
    site_group = parser.add_mutually_exclusive_group()
    site_group.add_argument('--site-mode', dest='site_admin_user_management', action='store_true', help=site_help)
    site_group.add_argument('--no-site-mode', dest='site_admin_user_management', action='store_false', help=site_help)

    parser.add_argument('--storage-quota',
        help='In MB, the amount of workbooks, extracts, and data sources that can be stored on the site.')

    parser.add_argument('--extract-encryption-mode', choices=['enforced','enabled','disabled'],
        help='The extract encryption mode for the site can be enforced, enabled or disabled. ')

    parser.add_argument('--run-now-enabled',
        help='Allow or deny users from running extract refreshes, flows, or schedules manually. \
            true to allow users to run tasks manually or false to prevent users from running tasks manually.')
    return parser



# export --- mmmaaaannnyyyy options
# publish


# refresh-extracts
def set_incremental_option(parser):
    parser.add_argument('--incremental',
        help='Runs the incremental refresh operation.')
    return parser
# should incremental/sync be mutually exclusive?
def set_sync_option(parser):
    parser.add_argument('--synchronous',
        help='Adds the full refresh operation to the queue used by the Backgrounder process, to be run as soon as a Backgrounder process is available.')
    return parser

def set_calculations_options(parser):
    calc_group = parser.add_mutually_exclusive_group()
    calc_group.add_argument('--addcalculations', action='store_true',
        help='Use to precalculate data operations in the extract data source.')
    calc_group.add_argument('--removecalculations', action= 'store_true',
        help='Use to remove precalculated data in the extract data source.')
    return parser


### TODO these are not used in any Online operations, on the backburner



# edit-domain: none of these are used in other commands
def set_domain_arguments(parser):
    parser.add_argument('--id',
        help='The ID of domain to change. To get a list of domain IDs, use use listdomains.')
    parser.add_argument('--name',
        help='The new name for the domain.')
    parser.add_argument('--nickname',
        help='The new nickname for the domain.')
    return parser

# reset-openid-sub
def set_target_users_arg(parser):
    target_users_group = parser.add_mutually_exclusive_group()
    target_users_group.add_argument('--target-username',
        help='Clears sub value for the specified individual user.')
    target_users_group.add_argument('--all',
        help='Clears sub values for all users.')
    return parser

# set setting
# choices: allow_scheduling, embedded_credentials, remember_passwords_forever
# use !setting-name to disable them
# hmmmm

# sync-group
def set_update_group_args(parser):
    parser.add_argument('--grant-license-mode', choices=['on-login', 'on-sync'],
        help='Specifies whether a role should be granted on sign in. ')
    parser.add_argument('--overwritesiterole', action='store_true',
        help='Allows a user’s site role to be overwritten with a less privileged one when using --role.')
    return parser

def set_upgrade_stop_option(parser):
    parser.add_argument('--stop', action='store_true',
        help='When specified, stops the in progress Upgrade Thumbnails job.')
    return parser

# validate-idp-metadata
# TODO not sure how these space-separated lists will work
def set_validate_idp_options(parser):
    parser.add_argument('--digest-algorithms', # <ALGORITHMS>
        help='A space-separated list of digest algorithms. Legal values are sha1and sha256. \
            If not specified, server uses values from server configuration setting, wgserver.saml.blocklisted_digest_algorithms.')
    parser.add_argument('--min-allowed-elliptic-curve-size', # <SIZE>
        help='If not specified, server uses values from server configuration setting, wgserver.saml.min_allowed.elliptic_curve_size.')
    parser.add_argument('--min-allowed-rsa-key-size', # <SIZE>
        help='If not specified, server uses values from server configuration setting, wgserver.saml.min_allowed.rsa_key_size.')
    parser.add_argument('--site-names', # <SITENAMES>
        help='A space-separated list of site names on which to perform certificate validation. If not specified, then all sites are inspected.')


