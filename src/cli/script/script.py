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

from cli.script import script_create
from cli.script import script_list
from cli.script import script_rename
from cli.script import script_run
from cli.script import script_show
from cli.script import script_update
from cli.script import script_delete

LOG = logging.getLogger(__name__)


def script(prog: str, args: typing.List[str]):
    """
    Command line argument parser for the Nixconfig program.

    .. argparse::
        :module: src.cli.script.script
        :func: script
        :prog: NixConfig

    """
    _parser = argparse.ArgumentParser(
        prog="{} script".format(prog),
        description='Script command')

    _subparser = _parser.add_subparsers(title='Script')

    script_create.init(_subparser)
    script_delete.init(_subparser)
    script_list.init(_subparser)
    script_rename.init(_subparser)
    script_run.init(_subparser)
    script_show.init(_subparser)
    script_update.init(_subparser)

    if len(args) == 0:
        _parser.print_help()
        raise NixError("Missing script command")
    else:
        _args = _parser.parse_args(args)
        _args.func(_args)

if __name__ == '__main__':
    pass
