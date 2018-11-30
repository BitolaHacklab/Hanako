"""Defines the parser and CLI for Hanako Server.
"""
import sys
from argparse import ArgumentParser
from hanako.meta import version
from hanako.server.api import api

def get_parser():
    parser = ArgumentParser(prog='hanako', description='Real-time multiplayer server')

    parser.add_argument('-v', '--version', action='store_true', help='Print version and exit')

    return parser


def run_server():
    parser = get_parser()
    args = parser.parse_args()

    if args.version:
        print(version)
        sys.exit(0)

    print("Welcome to Hanako server")
    api.run()

if __name__ == '__main__':
    run_server()