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
import sys

from cli.script import script
from cli.script_tag import script_tag
from cli.tag import tag

LOG = logging.getLogger(__name__)


def make_parser(sys_argv):
    """
    Command line argument parser for the Nixconfig program.

    """
    LOG.debug("Call parser")

    parser = argparse.ArgumentParser(
        description='Configure Nix',
        usage='''nixconfig {script,script-tag,tag} [<args>]

Commands:
    script              create, delete, update... scripts
    script-tag          add, remove, list... tags from scripts
    tag                 create, delete, list... tags
        ''')

    parser.add_argument('command', nargs="?", default="", help='Subcommand to run')

    args = parser.parse_args(sys_argv[1:2])

    _prog = sys.argv[0].rsplit("/", 1)[-1]

    if args.command == "script":
        script.script(_prog, sys_argv[2:])
    elif args.command == "script-tag":
        script_tag.script_tag(_prog, sys_argv[2:])
    elif args.command == "tag":
        tag.tag(_prog, sys_argv[2:])
    else:
        print('Unrecognized command')
        parser.print_help()
        exit(1)

if __name__ == '__main__':
    pass
