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

from cli.script_tag import script_tag_add
from cli.script_tag import script_tag_list
from cli.script_tag import script_tag_remove

LOG = logging.getLogger(__name__)


def script_tag(prog: str, args: typing.List[str]):
    _parser = argparse.ArgumentParser(
        prog="{} script-tag".format(prog),
        description='Script-Tag command')

    _subparser = _parser.add_subparsers(title='Script-Tag')

    script_tag_add.init(_subparser)
    script_tag_remove.init(_subparser)
    script_tag_list.init(_subparser)

    if len(args) == 0:
        _parser.print_help()
        raise NixError("Missing script-tag command")
    else:
        _args = _parser.parse_args(args)

        _args.func(_args)

if __name__ == '__main__':
    pass
