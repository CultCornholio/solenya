import argparse

from msph.app import Command

from .phish.command import phish
from .refresh.command import refresh

auth = Command('auth', __name__)

@auth.assembly
def assemble_parser(subparsers, app):
    parser = subparsers.add_parser('auth',
        help="Manages authentication of targets registered with the WorkSpace.")
    subparsers = parser.add_subparsers(dest='auth_cmd')
    subparsers.required = True

    phish.assemble_parser(subparsers, app=app)
    refresh.assemble_parser(subparsers, app=app)

    return parser