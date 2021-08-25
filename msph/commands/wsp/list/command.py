from msph.framework.cli import  Command, display

from . import msgs
from .... import workspace
from ....validators import WorkSpaceRequired

list_ = Command(
    'list',
    description='Lists data from the workspace.',
    required=[WorkSpaceRequired()]
)

@list_.cli()
def cli(cmd):
    group = cmd.parser.add_mutually_exclusive_group(required = True)
    group.add_argument('-a', '--all',
        help=f"Returns all data avaliable in the {workspace.settings_file.path} file.",
        action='store_true')
    group.add_argument('-k', '--keys',
        help=f"Returns all keys avaliable in the {workspace.settings_file.path} file.",
        action='store_true')
    group.add_argument('file_key',
        help=f"Specifies which value to return from the {workspace.settings_file.path} file.",
        nargs='?',
        choices = workspace.settings_file.read().keys())
    return cmd

@list_.target()
def target(settings):
    settings_file_content = workspace.settings_file.read()
    if settings.keys:
        display(msgs.create_list_keys_msg(settings_file_content.keys()))
    if settings.all:
        display(msgs.create_list_all_msg(settings_file_content))
    if settings.file_key:
        display(msgs.create_list_file_key_msg(
            settings.file_key, 
            settings_file_content[settings.file_key]
        ))
    
        