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

from libnix.config.script.rename_script import RenameScript

LOG = logging.getLogger(__name__)


def init(subparsers: argparse._SubParsersAction):
    """
    Command line subparser for renaming an existing script.

    The following arguments can be interpreted by the subprocessor:

    :Old Name: Current name of the script.
    :New Name: New name for the script.  Must be unique from other scripts as well as tags.

    :param subparsers: Object that will contain the argument definitions.
    :type subparsers: ArgumentParser
    """
    LOG.debug("Initialize subparser for the script-rename command")

    subparser = subparsers.add_parser('rename',
                                      help='Rename a script.')

    subparser.add_argument(type=str,
                           help="Current name",
                           dest='name')

    subparser.add_argument(type=str,
                           help="New name",
                           dest='name_new')

    subparser.set_defaults(func=_process)


def _process(args):
    """Process a command line action for listing setup groups.

    :param args: Command line arguments
    :type args: Namespace
    """
    LOG.info("Begin action to create a new script")

    rename_script = RenameScript()

    rename_script.rename(args.name, args.name_new)
