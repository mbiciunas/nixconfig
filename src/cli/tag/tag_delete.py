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

from libnix.config.tag.delete_tag import DeleteTag

LOG = logging.getLogger(__name__)


def init(subparsers: argparse._SubParsersAction):
    """
    Command line subparser for deleting an existing tag.

    The following arguments can be interpreted by the subprocessor:

    :Name: Name of the tag to delete.

    :param subparsers: Object that will contain the argument definitions.
    :type subparsers: ArgumentParser
    """
    LOG.debug("Initialize subparser for the tag-delete command")

    subparser = subparsers.add_parser('delete',
                                      help='Delete a tag.')

    subparser.add_argument(type=str,
                           help="Name of tag",
                           dest='tag')

    subparser.set_defaults(func=_process)


def _process(args):
    """Process a command line action for deleting tags.

    :param args: Command line arguments
    :type args: Namespace
    """
    LOG.info("Begin action to delete tag")

    _delete_tag = DeleteTag()

    _delete_tag.delete(args.tag)
