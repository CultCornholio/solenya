from msph.frameworks.cli import Router

root_router = Router(
    name="root",
    description='Dispatches the subsequent commands.'
)

from .init.command import init
from .devc.command import devc
#from .dump.router import dump_router

root_router.register_route(init)
root_router.register_route(devc)
#root_router.register_route()

