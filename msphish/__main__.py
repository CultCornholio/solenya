import sys
#sys.tracebacklimit = 0

from . import cli

def main(argv):
    cli.dispatch(argv = argv)

sys.exit(main(sys.argv[1:]))