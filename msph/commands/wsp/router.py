from msph.framework.cli import Router

wsp = Router(
    'wsp',
    description='Dispatches wsp commands.'
)

from .init.command import init
from .list.command import list_

wsp.register_route(init)
wsp.register_route(list_)