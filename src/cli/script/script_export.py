# NixConfig
# Copyright (c) 2017  Mark Biciunas.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import argparse
import logging

from libnix.config.script.export_script import ExportScript

LOG = logging.getLogger(__name__)


def init(subparsers: argparse._SubParsersAction):
    """
    Command line subparser for deleting an existing script.

    The following arguments can be interpreted by the subprocessor:

    :Name: Name of the script.
    :Description: Description of the script.
    :Tags: One or more tags to attach to the script.

    """
    LOG.debug("Initialize subparser for the export command")

    subparser = subparsers.add_parser('export',
                                      help='Export a script.')

    subparser.add_argument(type=str,
                           help="Name of script to export",
                           dest='name')

    subparser.add_argument(type=str,
                           help="Name of exported file",
                           dest='path')

    subparser.set_defaults(func=_process)


def _process(args):
    """Process a command line action for listing setup groups.

    :param args: Command line arguments
    :type args: Namespace
    """
    LOG.info("Begin action to export a script")

    export_script = ExportScript(args.name, args.path)

    export_script.export()
