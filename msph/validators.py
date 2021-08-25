from msph.framework.cli.validator import BaseValidator
from msph.framework.cli.exceptions import ValidationError

class WorkSpaceRequired(BaseValidator):

    def validate(self, app):
        workspace = app.plugins['workspace']
        if not workspace.exists:
            raise ValidationError(
                'Workspace is not found. \n'
                f'Run ( {app.name} wsp init {{client_id}} )'
            )
        return True
        
class ClientIdRequired(WorkSpaceRequired):

    def validate(self, app):
        super().validate(app)
        if not getattr(app.settings, 'client_id', None):
            raise ValidationError(
                'Client_id is not registered in the WorkSpace. \n'
                f'Run ( {app.name} wsp init {{client_id}} )')
        return True

class DeviceCodeRequired(WorkSpaceRequired):
    
    def validate(self, app):
        super().validate(app)
        if not getattr(app.settings, 'device_code', None):
            raise ValidationError(
                'Device_code is not registered in the WorkSpace. \n'
                f'Run ( {app.name} auth devc )')
        return True

class RefreshTokenRequired(WorkSpaceRequired):

    def validate(self, app):
        super().validate(app)
        if not getattr(app.settings, 'refresh_token', None):
            raise ValidationError(
                'Refresh token is not registered in the WorkSpace'
            )
        return False
