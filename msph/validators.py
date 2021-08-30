from msph.app import Validator

from .exceptions import ValidationError
from . import wsp
from .models import Wsp, WspTarget

class WorkSpaceRequired(Validator):

    def validate(self):
        super().validate()
        if not wsp.exists:
            raise ValidationError('WorkSpace is required.')

class ClientIdRequired(WorkSpaceRequired):
    
    def validate(self):
        super().validate()
        if not Wsp.select().first():
            raise ValidationError('Client id is required.')

class ActiveTargetRequired(ClientIdRequired):

    def validate(self):
        super().validate()
        if not WspTarget.select().where(WspTarget.active == True).first():
            raise ValidationError('No active target found in WorkSpace.')
        