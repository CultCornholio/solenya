from playhouse.shortcuts import model_to_dict
from datetime import datetime
import os

from msph.app import Command, current_app

from ... import settings, wsp
from ...models import WspTarget, Target
from ...validators import ActiveTargetRequired
from ... import utils
from . import msgs

export = Command('export', __name__, validators=[ActiveTargetRequired()])

@export.assembly
def assembly(subparsers):
    parser = subparsers.add_parser(export.name,
        help="Exports data from the WorkSpace.")
    parser.add_argument('-a', '--all',
        help="Designates all targets.",
        action="store_true",
        dest="all_targets")
    parser.add_argument('-o', '--output',
        help="Specify the path to save the output to.",
        dest="outpath")
    parser.add_argument('-f', '--format',
        help="The format of the export file.",
        choices=['csv', 'json'],
        default='csv',
        dest='outfile_format')
    return parser

@export.func
def main():
    if settings.all_targets:
        targets = [target for target in Target.select()]
        current_app.display(msgs.exporting_active_target(targets[0]))
    else:
        targets = [target for target in Target.select()\
            .join(WspTarget)\
                .where(WspTarget.active == True)]
        current_app.display(msgs.exporting_all_targets(targets))
    if settings.outpath:
        file_path = settings.outpath
    else:
        file_path = os.path.join(
            wsp.root_dir, 
            f"targets.{datetime.now().strftime('%Y%m%dT%H%M%S')}.{settings.outfile_format}"
        )
    if settings.outfile_format == 'csv':
        target_rows = [model_to_dict(target).values() for target in targets]
        target_headers = next(model_to_dict(target).keys() for target in targets)
        utils.save_to_csv(target_rows, target_headers, file_path)
    if settings.outfile_format == 'json':
        target_dicts = [model_to_dict(target) for target in targets]
        for target in target_dicts:
            for k, v in target.items():
                if isinstance(v, datetime):
                    target[k] = v.isoformat(sep=' ')
        utils.save_json(target_dicts, file_path)
    current_app.display(msgs.saved_targets_to_file(file_path))

    
    

