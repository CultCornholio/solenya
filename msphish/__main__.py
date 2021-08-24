import sys
#sys.tracebacklimit = 0

from . import create_tool

def main(argv):
    tool = create_tool()
    tool.propagate(argv)

sys.exit(main(sys.argv[1:]))