import argparse
from uuid import UUID


def client_id(value):
    try:
        uuid_obj = UUID(value, version=4)
    except ValueError:
        raise argparse.ArgumentTypeError(
            "client id must be a valid UUID 4.")
    else:
        return value