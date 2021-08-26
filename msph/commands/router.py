from msph.framework.cli import Router

root_router = Router(
    name="root",
    description='Dispatches the subsequent commands.'
)

from .wsp.router import wsp
from .auth.router import auth
from .graph.router import graph

root_router.register_route(wsp)
root_router.register_route(auth)
root_router.register_route(graph)

