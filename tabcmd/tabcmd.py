from tabcmd.execution.tabcmd_controller import TabcmdController
import sys


def main():

    if sys.version_info < (3, 7):
        raise ImportError("Tabcmd requires Python 3.7 but you are on " +
                          sys.version_info + " - please update your python version.")

    tabcmd_controller = TabcmdController()
    tabcmd_controller.initialize_parsers()
    tabcmd_controller.parse_inputs()


if __name__ == "__main__":
    main()
