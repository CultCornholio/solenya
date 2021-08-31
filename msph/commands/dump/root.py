import argparse

from msph.app import Command

from .email.command import email


dump = Command('dump', __name__)

@dump.assembly
def assemble_parser(subparsers, app):
    parser = subparsers.add_parser('dump',
        help="Interacts with the Microsoft Graph API to gather data, exfiltrate data, and execute commands")
    subparsers = parser.add_subparsers(dest='dump_cmd')
    subparsers.required = True

    email.assemble_parser(subparsers, app=app)

    return parser