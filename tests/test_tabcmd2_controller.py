
from ast import parse
import unittest
from pythontabcmd2 import commands
import pythontabcmd2
from pythontabcmd2.commands.auth.login_command import LoginCommand
from pythontabcmd2.commands.auth.session import Session
from pythontabcmd2.commands.datasources_and_workbooks.get_url_command import GetUrl
from pythontabcmd2.commands.datasources_and_workbooks.publish_command import PublishCommand
from pythontabcmd2.commands.group.create_group_command import CreateGroupCommand
from pythontabcmd2.commands.project.create_project_command import CreateProjectCommand
from pythontabcmd2.commands.site.edit_site_command import EditSiteCommand
from pythontabcmd2.commands.site.list_sites_command import ListSiteCommand
from pythontabcmd2.commands.user.add_users_command import AddUserCommand
from pythontabcmd2.context import Context
from unittest import mock

from pythontabcmd2.parsers.create_group_parser import CreateGroupParser

class CommandsTests(unittest.TestCase):


    parser = Context.initialize_parsers() # this adds all parsers and global options

    @mock.patch.object(AddUserCommand, 'run_command', autospec=True)
    @mock.patch.object(Session, 'create_session', autospec=True)
    def test_addusers(self, mock_session, mock_function):
        test_input = ['addusers', 'groupname']
        mock_session.create_session = mock.MagicMock(name='parser.session-mock')
        mock_function.run = mock.MagicMock(name='parser-tests.run-mock-command')
        parsed_args = Context.parse_inputs(self.parser, test_input)
        assert parsed_args.func == AddUserCommand
        assert parsed_args.groupname == test_input[1]


    @mock.patch.object(CreateProjectCommand, 'run_command', autospec=True)
    @mock.patch.object(Session, 'create_session', autospec=True)
    def test_create_project(self, mock_session, mock_function):
        test_input = ['createproject', '-n', 'project-name-to-give']
        mock_session.create_session = mock.MagicMock(name='parser.session-mock')
        parsed_args = Context.parse_inputs(self.parser, test_input)
        assert parsed_args.func == CreateProjectCommand
        assert parsed_args.projectname == test_input[2], parsed_args


    @mock.patch.object(CreateGroupCommand, 'run_command', autospec=True)
    @mock.patch.object(Session, 'create_session', autospec=True)
    def test_create_group(self, mock_session, mock_function):
        mock_session.create_session = mock.MagicMock(name='parser.session-mock')
        test_input = ['creategroup', 'groupname']
        parsed_args = Context.parse_inputs(self.parser, test_input)
        assert parsed_args.func == CreateGroupCommand
        assert parsed_args.groupname == test_input[1]


    @mock.patch.object(LoginCommand, 'run_command', autospec=True)
    @mock.patch.object(Session, 'create_session', autospec=True)
    def test_login(self, mock_session, mock_function):
        test_input = ['login']
        mock_session.create_session = mock.MagicMock(name='parser.session-mock')
        mock_function.run = mock.MagicMock(name='parser-tests.run-mock-command')
        parsed_args = Context.parse_inputs(self.parser, test_input)
        assert parsed_args.func == LoginCommand, parsed_args


    @mock.patch.object(EditSiteCommand, 'run_command', autospec=True)
    @mock.patch.object(Session, 'create_session', autospec=True)
    def test_editsite(self, mock_session, mock_function):
        mock_session.create_session = mock.MagicMock(name='parser.session-mock')
        test_input = ['editsite', 'site-name']
        parsed_args = Context.parse_inputs(self.parser, test_input)
        assert parsed_args.func == EditSiteCommand

    @mock.patch.object(PublishCommand, 'run_command', autospec=True)
    @mock.patch.object(Session, 'create_session', autospec=True)
    def test_publish(self, mock_session, mock_function):
        mock_session.create_session = mock.MagicMock(name='parser.session-mock')
        test_input = ['publish', 'filename', '-r', 'project-name']
        parsed_args = Context.parse_inputs(self.parser, test_input)
        assert parsed_args.func == PublishCommand
        assert parsed_args.name == test_input[1], parsed_args
        assert parsed_args.projectname == test_input[3], parsed_args


    @mock.patch.object(ListSiteCommand, 'run_command', autospec=True)
    @mock.patch.object(Session, 'create_session', autospec=True)
    def test_listsites(self, mock_session, mock_function):
        mock_session.create_session = mock.MagicMock(name='parser.session-mock')
        test_input = ['listsites']
        print(test_input)
        parsed_args = Context.parse_inputs(self.parser, test_input)
        assert parsed_args.func == ListSiteCommand


    @mock.patch.object(GetUrl, 'run_command', autospec=True)
    @mock.patch.object(Session, 'create_session', autospec=True)
    def test_geturl(self, mock_session, mock_function):
        mock_session.create_session = mock.MagicMock(name='parser.session-mock')
        test_input = ['get', 'url-to-get']
        parsed_args = Context.parse_inputs(self.parser, test_input)
        assert parsed_args.func == GetUrl

    @mock.patch.object(LoginCommand, 'run_command', autospec=True)
    @mock.patch.object(Session, 'create_session', autospec=True)
    def test_login(self, mock_session, mock_function):
        mock_session.create_session = mock.MagicMock(name='parser.session-mock')
        test_input = ['login', '--server', 'http://server']
        parsed_args = Context.parse_inputs(self.parser, test_input)
        assert parsed_args.func == LoginCommand

    @mock.patch.object(Session, 'create_session', autospec=True)
    def test_help(self, mock_session):
        mock_session.create_session = mock.MagicMock(name='parser.session-mock')
        test_input = ['--help']
        with self.assertRaises(SystemExit):
            parsed_args = Context.parse_inputs(self.parser, test_input)
