from msph.framework.cli import Router

auth = Router(
    name = "auth",
    description = "Dispatches auth commands."
)


from .phish.command import phish
from .refresh.command import refresh
from .devc.command import devc

auth.register_route(phish)
auth.register_route(refresh)
auth.register_route(devc)


