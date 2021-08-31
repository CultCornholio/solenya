from datetime import date, datetime
import colorful as cf


def target_dumped(target):
    return f"{cf.green('Emails Gathered!')}: target {cf.magenta(target.name)} {cf.yellow('Pwn3d!')} ({datetime.now()})!"

def target_failed(target):
    return f"{cf.red('Failed to fetch emails!')}: target verify the access token is still valid)!"

def starting_check():
    return f"{cf.bold('Running checks...')}"

def run_for_active_target(target):
    return f"Checking for active target: {cf.magenta(target.name)}, {cf.coral('user_code')}:{cf.cyan(target.user_code)}"

def run_for_all_targets(targets):
    return f"Running for {cf.magenta('all targets')}. Total targets: {cf.cyan(len(targets))}"

def starting_session():
    return f"{cf.green('[Starting Session]')}({datetime.now()})"

def has_refresh_token(target):
    return f"{cf.yellow('WARNING')}: target {cf.magenta(target.name)} has an active {cf.coral('refresh_token')}. {cf.white('Skipping...')}"

def user_code_expired(target):
    return f"{cf.yellow('WARNING')}: target {cf.magenta(target.name)} has an expired {cf.coral('user_code')}. {cf.white('Skipping...')}"