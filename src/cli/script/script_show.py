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

from libnix.config.script.show_script import ShowScript

LOG = logging.getLogger(__name__)


def init(subparsers: argparse._SubParsersAction):
    """
    Command line subparser for showing the contents of a script.

    The following arguments can be interpreted by the subprocessor:

    :Name: Name of the script to show details for.

    :param subparsers: Object that will contain the argument definitions.
    :type subparsers: ArgumentParser
    """
    LOG.debug("Initialize subparser for the show command")

    subparser = subparsers.add_parser('show',
                                      help='Show the contents of a script.')

    subparser.add_argument(type=str,
                           help="Name of script",
                           dest='name')

    subparser.set_defaults(func=_process)


def _process(args):
    """Process a command line action for listing setup groups.

    :param args: Command line arguments
    :type args: Namespace
    """
    LOG.info("Begin action to show a script")

    _show_script = ShowScript()

    _show_script.show(args.name)
