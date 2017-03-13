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
import typing

from libnix.exception.nix_error import NixError

from cli.tag import tag_create
from cli.tag import tag_list
from cli.tag import tag_rename
from cli.tag import tag_show
from cli.tag import tag_delete

LOG = logging.getLogger(__name__)


def tag(prog: str, args: typing.List[str]):
    _parser = argparse.ArgumentParser(
        prog="{} tag".format(prog),
        description='Tag command')

    _subparser = _parser.add_subparsers(title='Script')

    tag_create.init(_subparser)
    tag_delete.init(_subparser)
    tag_list.init(_subparser)
    tag_rename.init(_subparser)
    tag_show.init(_subparser)

    if len(args) == 0:
        _parser.print_help()
        raise NixError("Missing tag command")
    else:
        _args = _parser.parse_args(args)

        _args.func(_args)

if __name__ == '__main__':
    pass