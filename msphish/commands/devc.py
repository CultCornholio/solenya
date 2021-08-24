import argparse

from .. import msgs
from ..clients import ms_online as client
from ..settings import Settings
from .. import utils
from .. import cli

def devc(settings):
    r = client.get_device_code(settings.client_id)
    stdout = utils.write_to_file if settings.output_path else cli.display
    if settings.raw_output:
        output = utils.format_json_string(r.json())
    else:
        output = r.json()['device_code']
        if not settings.output_path:
            output = msgs.create_device_code_msg(output)
    stdout(output)
    
def main(args):
    parser = argparse.ArgumentParser(
        prog="msphish devc",
        description="Get the device code for a client id.")
    parser.add_argument(
        "client_id",
        help='the id of the client.',
        type=str)
    parser.add_argument('-o', '--outfile',
        help=('The name of the file to which the device code will be written to. '
            'Output to console otherwise.'),
        type=str,
        dest='output_path'
    )
    parser.add_argument('-r', '--raw',
        help="get raw output from the api",
        action='store_true',
        dest='raw_output')
    parsed_args = parser.parse_args(args)
    settings = Settings().register_from_namespace(parsed_args)
    devc(settings)