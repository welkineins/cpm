#!/usr/bin/env python

import sys
import argparse
import argcomplete
import yaml

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
    return parsed_args.cmd_callback(options, parsed_args)

def initializeParser(args, commands):
    parser = argparse.ArgumentParser(prog=prog, description=description, epilog=epilog)
    parser.add_argument('--version', action='version', version=version)
    parser.add_argument('--debug', action='store_true', help='Enable debug mode')
    parser.add_argument('--verbose', '-v', action='count', help='Enable verbose output, upto -vvv')
    parser.set_defaults(cmd_callback=lambda o, a: parser.print_usage())
    
    if commands.__all__:
        sub_parsers = parser.add_subparsers(title='valid commands', metavar='command')

        for cmd_name in commands.__all__:
            cmd_class = getattr(globals()[cmd_name], cmd_name.capitalize() + "Command")
            sub_parser = sub_parsers.add_parser(cmd_class.name or cmd_name, aliases=cmd_class.aliases, help=cmd_class.description)
            cmd_class(sub_parser)

    argcomplete.autocomplete(parser)

    return parser

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))