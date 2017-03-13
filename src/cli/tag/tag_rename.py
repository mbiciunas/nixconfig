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

from libnix.config.tag.rename_tag import RenameTag

LOG = logging.getLogger(__name__)


def init(subparsers: argparse._SubParsersAction):
    """
    Command line subparser for renaming an existing tag.
    The following arguments can be interpreted by the subprocessor:

    :Old Name: Current name of the tag.
    :New Name: New name for the tag.  Must be unique from other tags as well as scripts.

    :param subparsers: Object that will contain the argument definitions.
    :type subparsers: ArgumentParser
    """
    LOG.debug("Initialize subparser for the tag-rename command")

    subparser = subparsers.add_parser('rename',
                                      help='Rename a tag.')

    subparser.add_argument(type=str,
                           help="Current tag name",
                           dest='tag')

    subparser.add_argument(type=str,
                           help="New tag name",
                           dest='tag_new')

    subparser.set_defaults(func=_process)


def _process(args):
    """Process a command line action for renaming tags.

    :param args: Command line arguments
    :type args: Namespace
    """
    LOG.info("Begin action to rename a tag")

    _rename_tag = RenameTag()

    _rename_tag.rename(args.tag, args.tag_new)
