#!/usr/bin/env python
import sys
import argparse
import argcomplete
import commands
from commands import *

prog = 'cpm'
description = 'CPM (Cat Package Manager) is yet another package manager for cross-platform projects.'
epilog = 'enjoy it ;-)'
version = '0.0.1'

def main(args):
    options = []
    parser = initializeParser(args, commands)
    parsed_args = parser.parse_args(args)
    return parsed_args.func(options, parsed_args)

def initializeParser(args, commands):
    parser = argparse.ArgumentParser(prog=prog, description=description, epilog=epilog)
    parser.add_argument('-v', '--version', action='version', version=version)
    
    if commands.__all__:
        sub_parsers = parser.add_subparsers()

        for cmd_name in commands.__all__:
            sub_parser = sub_parsers.add_parser(cmd_name)
            cmd_class = getattr(globals()[cmd_name], cmd_name.capitalize() + "Command")
            cmd_class(sub_parser)

    argcomplete.autocomplete(parser)

    return parser

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))