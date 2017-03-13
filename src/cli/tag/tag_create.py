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

from libnix.config.tag.create_tag import CreateTag

LOG = logging.getLogger(__name__)


def init(subparsers: argparse._SubParsersAction):
    """
    Command line subparser for creatiing a new tag.

    The following arguments can be interpreted by the subprocessor:

    :Name: Name of the tag.  Must be unique from other tags as well as scripts.
    :Description: Brief description of what the tag is for.

    :param subparsers: Object that will contain the argument definitions.
    :type subparsers: ArgumentParser
    """
    LOG.debug("Initialize subparser for the tag-create command")

    subparser = subparsers.add_parser('create',
                                      help='Create a tag.')

    subparser.add_argument(type=str,
                           help="Name of new tag",
                           dest='tag')

    subparser.add_argument(type=str,
                           help="Description",
                           dest='desc')

    subparser.set_defaults(func=_process)


def _process(args):
    """Process a command line action for listing scripts.

    :param args: Command line arguments
    :type args: Namespace
    """
    LOG.info("Begin action to create a tag")

    _create_tag = CreateTag()

    _create_tag.create(args.tag, args.desc)
