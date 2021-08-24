import argparse

from msphish.framework.cli import Router

root_router = Router(
    dest='{app.name}',
    name='dispatch command',
    description='the root command of {app.name}'
)

from .init.command import init
#from .devc.command import devc
from .dump.router import dump_router

root_router.register_route(init)
#router.register_route(devc)
#root_router.register_route()

