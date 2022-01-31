# Tabcmd2

[![Tableau Supported](https://img.shields.io/badge/Support%20Level-Tableau%20Supported-53bd92.svg)](https://www.tableau.com/support-levels-it-and-developer-tools)

A Python based app that replicates the functionality of the existing [Tabcmd command line utility](https://help.tableau.com/current/server/en-us/tabcmd.htm).

**Important Note:** Tabcmd2 is a work in progress ("beta") which may be useful for test and development purposes, but is not yet recommended for production environments.

* [Why Tabcmd2\?](#whytabcmd2)
* [Demo](#demo)
* [Get started](#get-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Run](#run)
  * [Available Commands](#available-commands)
* [Contributions](#contributions)

## Why Tabcmd2?

* Add support for MacOS
* Authenticate using Personal Access Tokens (existing Tabcmd does not support Personal Access Token login)
* Use public endpoints available in Python based [Tableau Server Client](https://github.com/tableau/server-client-python/)
* Easier future development to add more functionality 

## Demo/Samples

_coming soon_

## Get started

This section describes how to install and configure Tabcmd2.

### Prerequisites

To work with Tabcmd2, you need the following:

* Python 3.7+ installed

### Installation

To install Tabcmd2, follow these steps:

1. Clone the repo
2. Run `pip install .`

## Run

To run Tabcmd2, follow these steps:

1. To run a command:
    * `tabcmd2 [command_name] [--flags]`
    * Examples:
        * `tabcmd2 login --username [username] --password [password] --server
         [server_name] --site [site_name]`
        * `tabcmd2 createproject --name [project_name]`

## Packaging
pip install pyinstaller
pyinstaller tabcmd.py --clean --noconfirm


## Contributions

Code contributions and improvements by the community are welcomed!

See the LICENSE file for current open-source licensing and use information.

Before we can accept pull requests from contributors, we require a signed [Contributor License Agreement (CLA)](http://tableau.github.io/contributing.html).
