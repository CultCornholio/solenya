import peewee as pw
from playhouse.hybrid import hybrid_property
from datetime import date, datetime, timedelta

from .exceptions import CliAppError

from . import wsp

class BaseModel(pw.Model):
    class Meta:
        database = wsp.db

class Wsp(BaseModel):
    client_id = pw.CharField(100)

class Target(BaseModel):

    device_code_exp = timedelta(minutes=15)
    user_code_exp = timedelta(minutes=15)
    access_token_exp = timedelta(hours=1)
    refresh_token_exp = timedelta(days=90)
        
    name = pw.CharField(100)
    device_code = pw.TextField(null=True)
    user_code = pw.TextField(null=True)
    access_token = pw.TextField(null=True)
    refresh_token = pw.TextField(null=True)
    device_code_ts = pw.DateTimeField(null=True)
    user_code_ts = pw.DateTimeField(null=True)
    access_token_ts = pw.DateTimeField(null=True)
    refresh_token_ts = pw.DateTimeField(null=True)

    def is_exp(self, ts_str):
        return datetime.now() > self.get_exp_time(ts_str)

    def get_exp_time(self, ts_str):
        ts = getattr(self, f"{ts_str}_ts")
        if not ts:
            return datetime.min
        return getattr(self, f"{ts_str}_ts") + getattr(Target, f"{ts_str}_exp")

    @hybrid_property
    def active(self):
        return self.wsp_target.first().active

class WspTarget(BaseModel):
    wsp = pw.ForeignKeyField(Wsp, backref='wsp_target')
    target = pw.ForeignKeyField(Target, backref="wsp_target")
    active = pw.BooleanField(default = False)
    timestamp = pw.DateTimeField(default=datetime.now)
