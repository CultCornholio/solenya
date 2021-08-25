from msph.frameworks.cli.validator import BaseValidator
from msph.frameworks.cli.exceptions import ValidationError

class WorkSpaceRequired(BaseValidator):

    def validate(self, app):
        workspace = app.plugins['workspace']
        if not workspace.exists:
            raise ValidationError(
                'Workspace is not found. \n'
                f'Run ( {app.name} init {{client_id}} )'
            )
        return True
        
class ClientIdRequired(BaseValidator):

    def validate(self, app):
        if not getattr(app.settings, 'client_id', None):
            raise ValidationError(
                'Client_id is not registered in the WorkSpace. \n'
                f'Run ( {app.name} init {{client_id}} )')
        return True
