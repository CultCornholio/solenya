import argparse

from msph.app import Command

from .wsp.command import wsp_cmd
from .target.command import target
from .switch.command import switch
from .auth.root import auth
from .dump.root import dump
from .export.command import export

msph = Command('sol', __name__)

@msph.assembly
def assemble_parser(app):
    parser = argparse.ArgumentParser(
        prog=msph.name,
        description="Microsoft365 Device Code Phishing CLI tool."
    )
    subparsers = parser.add_subparsers(dest="root_cmd")
    subparsers.required = True

    wsp_cmd.assemble_parser(subparsers, app = app)
    target.assemble_parser(subparsers, app = app)
    switch.assemble_parser(subparsers, app = app)
    auth.assemble_parser(subparsers, app = app)
    dump.assemble_parser(subparsers, app= app)
    export.assemble_parser(subparsers, app = app)

    return parser