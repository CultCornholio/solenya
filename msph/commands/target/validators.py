from msph.app import Validator, current_app

from ... import settings

class CliValidator(Validator):

    def validate(self):
        if settings.delete_target:
            if not settings.target_names:
                current_app.active_command.parser.error('Must specify {target_names} with [-d] flag.')
        if settings.reset_target:
            if not settings.target_names and not settings.all_targets:
                current_app.active_command.parser.error('Must specify either {target_names} or [-a] flag with [-r] flag.')
            if settings.target_names and settings.all_targets:
                current_app.active_command.parser.error('Can no specify {target_names} with [-a] flag.')
        if settings.all_targets and not settings.reset_target:
            current_app.active_command.parser.error("[-a] flag can only be set with [-r] flag.")
        if settings.reset_hard:
            if not settings.delete_target and not settings.reset_target:
                current_app.active_command.parser.error("[--hard] flag can only be set with [-d, -r] flags.")
        if settings.delete_target or not settings.target_name:
            if settings.verbose:
                current_app.active_command.parser.error("[-v] flag can only be set when creating or reseting targets.")
        return True
        