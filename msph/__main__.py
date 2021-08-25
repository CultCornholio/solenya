import sys
#sys.tracebacklimit = 0

from . import create_app

def main(argv):
    app = create_app()
    app.propagate(argv)

sys.exit(main(sys.argv[1:]))