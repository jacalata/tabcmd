import getpass
import sys
from .. import Constants
import tableauserverclient as TSC
from .. import log
import json
import os


class Session:
    """
    Session class handles all authentication related work
    """
    def __init__(self):
        self.username = None
        self.password = None
        self.auth_token = None
        self.token_name = None
        self.token = None
        self.site = None
        self.site_id = None
        self.server = None
        self.last_login_using = None
        self.logging_level = "info"
        self.logger = log('pythontabcmd2.session', self.logging_level)
        self._read_from_json()

    def _get_file_path(self):
        home_path = os.path.expanduser("~")
        file_path = os.path.join(home_path, 'tableau_auth.json')
        return file_path

    def _read_from_json(self):
        if not self._check_json():
            return
        file_path = self._get_file_path()
        with open(str(file_path), 'r') as input:
            data = json.load(input)
            for auth in data['tableau_auth']:
                self.auth_token = auth['token']
                self.server = auth['server']
                self.site = auth['site_name']
                self.site_id = auth['site_id']
                self.username = auth['username']
                self.token_name = auth['personal_access_token_name']
                self.token = auth['personal_access_token']
                self.last_login_using = auth['last_login_using']


    def _check_json(self):
        home_path = os.path.expanduser("~")
        file_path = os.path.join(home_path, 'tableau_auth.json')
        return os.path.exists(file_path)

    def _update_session(self, args):
        if args.username:
            self.username = args.username
        if args.site is not None:
            self.site = args.site
        if args.password:
            self.password = args.password
        if args.server:
            self.server = args.server
        if args.logging_level:
            self.logging_level = args.logging_level
        if args.token_name:
            self.token_name = args.token_name
        if args.token:
            self.token = args.token

    def check_for_missing_arguments(self):
        if self.server is None:
            self.logger.error("Please pass server")
            sys.exit()
        if self.site is None:
            self.site = ''

    def save_token_to_json_file(self):
        data = {}
        data['tableau_auth'] = []
        data['tableau_auth'].append({
            'token': self.auth_token,
            'server': self.server,
            'username': self.username,
            'site_name': self.site,
            'site_id': self.site_id,
            'personal_access_token_name': self.token_name,
            'personal_access_token': self.token,
            'last_login_using': self.last_login_using
        })
        file_path = self._get_file_path()
        with open(str(file_path), 'w') as f:
            json.dump(data, f)

    def no_cookie_save_session_creation_with_username(self, args):
        try:
            if self.password is None: #check the --no-prompt value?
                self.password = getpass.getpass("Password:")
            self.check_for_missing_arguments()
            self.logger.info("server: {}".format(self.server))
            tableau_auth = TSC.TableauAuth(self.username,
                                           self.password, self.site)
            tableau_server = self._create_server_connection(args)
            signed_in_object = tableau_server.auth.sign_in(tableau_auth)
            self.auth_token = tableau_server.auth_token
            self.site_id = tableau_server.site_id
            self.last_login_using = "username"
            self.logger.info("=========Succeeded========")
            return tableau_server
        except TSC.ServerResponseError as e:
            if e.code == Constants.login_error:
                self.logger.error("Please check the provided credentials and try again", e)

    def _reuse_session(self, args):
        tableau_server = self._create_server_connection(args)
        tableau_server._auth_token = self.auth_token
        tableau_server._site_id = self.site_id
        return tableau_server

    def _no_cookie_save_session_creation_with_token(self, args):
        self.logger.info("server: {}".format(
            self.server))
        try:
            if self.token is None: # check no-prompt
                self.token = getpass.getpass("Token:")
            self.check_for_missing_arguments()
            tableau_auth = \
                TSC.PersonalAccessTokenAuth(self.token_name,
                                            self.token, self.site)
            tableau_server = self._create_server_connection(args)
            signed_in_object = \
                tableau_server.auth.sign_in_with_personal_access_token(
                    tableau_auth)
            self.auth_token = tableau_server.auth_token
            self.site_id = tableau_server.site_id
            self.last_login_using = "token"
            self.logger.info("=========Succeeded========")
            return tableau_server
        except TSC.ServerResponseError as e:
            if e.code == Constants.login_error:
                self.logger.error("Please Login again and check login "
                                  "credentials")

    def _create_server_connection(self, args):
        # relevant args: proxy, cert, cert-check, timeout
        ts = TSC.Server(self.server)
        ts.version = '3.16' # not sure what the ideal behavior here is
        if args.no_certcheck:
            ts.add_http_options({'verify': False})

        return ts

    def create_session(self, args):
        signed_in_object = None
        if args.username or args.password:
            signed_in_object = self._create_new_session_using_username(args)
            return self._open_session(args, signed_in_object)
        elif args.token or args.token_name:
            signed_in_object = self._create_new_session_using_token(args)
            return self._open_session(args, signed_in_object)
        else:
            if not self._check_json():
                # no credentials given and saved credentials are not present
                self.logger.info("Please enter server and credential information to log in.")
                sys.exit()

        if args.site or args.server:
            last_login_username_present, last_login_token_name_present, \
                username, token_name = \
                self._check_last_login_username_token_name()
            if last_login_username_present:
                signed_in_object = self._create_new_session_using_username(args)
                return self._open_session(args, signed_in_object)
            elif last_login_token_name_present:
                signed_in_object = self._create_new_session_using_token(args)
                return self._open_session(args, signed_in_object)

        # not sure we can be in a good state when we reach here
        return self._open_session(args, signed_in_object)

    def _open_session(self, args, signed_in_object):
        if args.no_cookie:
            self._remove_json()
        else:
            self.save_token_to_json_file()
        return signed_in_object

    def _remove_json(self):
        file_path = self._get_file_path()
        if os.path.exists(file_path):
            os.remove(file_path)

    def _check_last_login_username_token_name(self):
        last_login_username_present = False
        last_login_token_name_present = False
        username = False
        token_name = False
        file_path = self._get_file_path()
        with open(str(file_path), 'r') as input:
            data = json.load(input)
            for auth in data['tableau_auth']:
                if auth['last_login_using'] == "username":
                    last_login_username_present = True
                if auth['last_login_using'] == "token":
                    last_login_token_name_present = True
            return last_login_username_present, \
                last_login_token_name_present, \
                username, token_name

    def _create_new_session_using_username(self, args):
        self._update_session(args)
        signed_in_object = self.no_cookie_save_session_creation_with_username(args)
        return signed_in_object

    def _create_new_session_using_token(self, args):
        self._update_session(args)
        signed_in_object = self._no_cookie_save_session_creation_with_token(args)
        return signed_in_object
