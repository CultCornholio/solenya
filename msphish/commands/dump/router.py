import argparse

from msphish.framework.cli import Router

dump_router = Router(
    name='dump dispatch command',
    description='the root command of {app.name}',
    dest='dump'
)

#from .users.command import users
from .emails.command import email

#dump_router.registered_route(users)
dump_router.register_route(email)

