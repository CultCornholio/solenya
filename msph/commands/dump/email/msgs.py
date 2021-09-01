from datetime import date, datetime
import colorful as cf


def target_dumped(target):
    return f"{cf.green('Emails Gathered!')}: target {cf.magenta(target.name)} {cf.yellow('Pwn3d!')} ({datetime.now()})!"

def target_failed(target):
    return f"{cf.red('Failed to fetch emails!')}: {cf.magenta(target.name)} verify the access token is still valid."

def starting_check():
    return f"{cf.bold('Running checks...')}"

def run_for_active_target(target):
    return f"Checking for active target: {cf.magenta(target.name)},{cf.coral('user_code')}:{cf.cyan(target.user_code)}"

def run_for_all_targets(targets):
    return f"Running for {cf.magenta('all targets')}. Total targets: {cf.cyan(len(targets))}"

def starting_session():
    return f"{cf.green('[Starting Session]')}({datetime.now()})"

def user_code_expired(target):
    return f"{cf.yellow('WARNING')}: target {cf.magenta(target.name)} has an invalid {cf.coral('acesss_token')}. {cf.white('Skipping...')}"

def no_targets_with_access_token():
    return 'no targets have valid access tokens.'

def file_saved(path, count):
    return f"Saved emails for {cf.cyan(count)} targets to {cf.cyan(path)}"