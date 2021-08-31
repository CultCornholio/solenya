import argparse
from functools import wraps
import sys

def subparser_default(func):
    def layer(subparser):
        def wrapper(*args, **kwargs):
            return func(subparser, *args, **kwargs)
        return wrapper
    return layer

@subparser_default
def foo(subparser):
    subparser.error('err')

@subparser_default
def bar(subparser):
    subparser.error('err')

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

foo_parser = subparsers.add_parser('foo')
foo_parser.set_defaults(func = foo(foo_parser))

bar_parser = subparsers.add_parser('bar')
bar_parser.set_defaults(func = bar(bar_parser))


args = parser.parse_args(sys.argv[1:])
args.func()