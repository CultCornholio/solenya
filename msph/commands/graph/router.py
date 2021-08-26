from msph.framework.cli import Router

from ...validators import AccessTokenRequired

graph = Router(
    'graph',
    description='Dispatches commands for graph API.',
    required=[AccessTokenRequired()]
)

from .dump.router import dump

graph.register_route(dump)