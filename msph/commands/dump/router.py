import argparse

from msph.frameworks.cli import Router

dump_router = Router(
    name='dump',
    description='Dispatches the subsequent commands',
)

#from .users.command import users
from .emails.command import email

#dump_router.registered_route(users)
dump_router.register_route(email)

