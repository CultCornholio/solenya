from msph.app import Command, current_app
from msph.exceptions import CliAppError
from msph.settings import Settings

from ...validators import ActiveTargetRequired
from ... import settings
from ...models import Target, WspTarget
from . import msgs

switch = Command('switch', __name__,
    validators=[])

@switch.assembly
def assemble_parser(subparsers):
    parser = subparsers.add_parser('switch',
        help="Switches active target.")
    parser.add_argument('-t', '--target',
        help=("Automatically execute 'sol target {target_name}' "
            "command before running the 'switch' command."),
        dest="create_target",
        action="store_true")
    parser.add_argument('target_name',
        help="The name of the target to switch to.",
        type=str)
    return parser
    
@switch.func
def main():
    active_target = Target.select().join(WspTarget)\
        .where(WspTarget.active == True).first()
    target = Target.select().where(Target.name == settings.target_name).first()
    if settings.create_target:
        if target:
            current_app.display(msgs.target_already_exists(target))
        else:
            current_app.run_command(
                'msph.target', 
                settings=Settings(target_names = [settings.target_name]))
            target = Target.select().where(Target.name == settings.target_name).first()
    if not target:
        raise CliAppError(msgs.target_not_found(settings.target_name))
    if active_target.id == target.id:
        raise CliAppError(msgs.target_is_already_active(target))
    wsp_target_to_deactive = active_target.wsp_target.first()
    wsp_target_to_activate = target.wsp_target.first()
    wsp_target_to_deactive.active = False
    wsp_target_to_activate.active = True
    wsp_target_to_deactive.save()
    wsp_target_to_activate.save()
    current_app.display(msgs.active_target_set(target))