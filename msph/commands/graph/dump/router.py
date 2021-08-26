from msph.framework.cli import Router

dump = Router(
    'dump',
    description='Dispatches commands for dump.'
)

from .emails.command import emails

dump.register_route(emails)