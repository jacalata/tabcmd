import tableauserverclient as TSC
from .. import log
from ..project.project_command import ProjectCommand
from ... import Session
from .datasources_and_workbooks_command import DatasourcesAndWorkbooks


class PublishCommand(DatasourcesAndWorkbooks):
    """
    This command publishes the specified workbook (.twb(x)), data source
    (.tds(x)), or extract (.hyper) to Tableau Server.
    """
    def __init__(self, args):
        self.file_name = args.name
        # ?? self.file_path = source
        self.project_path = args.parent_project_path
        # self.source = self.get_source_type(source)
        self.logging_level = args.logging_level
        self.logger = log('pythontabcmd2.publish',
                          self.logging_level)

    def run_command(self, args):
        session = Session()
        server_object = session.create_session(args)
        self.publish(server_object)

    def publish(self, server):
        if self.args.project is not None:
            project_id = \
                ProjectCommand.find_project_id(server, self.args.project)
        else:
            project_id = ''
        if self.source == "twbx" or self.source == "twb":
            new_workbook = TSC.WorkbookItem(project_id,
                                            name=self.args.name,
                                            show_tabs=self.args.tabbed)  # TODO

            if self.args.overwrite:
                publish_mode = TSC.Server.PublishMode.Overwrite
            else:
                publish_mode = TSC.Server.PublishMode.CreateNew
            new_workbook = server.workbooks.publish(new_workbook,
                                                    self.file_name,
                                                    publish_mode)
            self.logger.info("Workbook {} published".format(
                new_workbook.name))

        elif self.source == "tds" or self.source == "tdsx" or \
                self.source == "hyper":
            new_datasource = TSC.DatasourceItem(project_id,
                                                name=self.args.name)
            if self.args.overwrite:
                publish_mode = TSC.Server.PublishMode.Overwrite
            else:
                publish_mode = TSC.Server.PublishMode.CreateNew
            new_datasource = server.datasources.publish(new_datasource,
                                                        self.file_path,
                                                        publish_mode)
            self.logger.info("DataSource {} published".format(
                new_datasource.name))

    def get_source_type(self, source):
        source_list = source.split('.')
        twbx = 'twbx'
        twb = 'twb'
        tdsx = 'tdsx'
        tds = 'tds'
        hyper = 'hyper'
        if twbx in source_list:
            return twbx
        elif twb in source_list:
            return twb
        elif tdsx in source_list:
            return tdsx
        elif tds in source_list:
            return tds
        elif hyper in source_list:
            return hyper
