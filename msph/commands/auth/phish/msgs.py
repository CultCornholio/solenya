from datetime import date, datetime
import colorful as cf

def ending_session(targets_authed_count, targets_expired_count):
    return (
        f"{cf.green('[Ending Session]')}({datetime.now()})\n"
        "[session summary]\n"
        f"\ttargets authed count: {cf.cyan(targets_authed_count)}\n"
        f"\ttargets expired count: {cf.cyan(targets_expired_count)}"
    )

def no_targets_need_phishing():
    return f"{cf.yellow('WARNING')}: No phishing targets remianing."

def target_authed(target):
    return f"{cf.green('Phishing SUCCESS')}: target {cf.magenta(target.name)} {cf.yellow('Pwn3d!')} ({datetime.now()})!"

def starting_check():
    return f"{cf.bold('Running checks...')}"

def checking_for_active_target(target):
    return f"Checking for active target: {cf.magenta(target.name)}, {cf.coral('user_code')}:{cf.cyan(target.user_code)}"

def checking_for_all_targets(targets):
    return f"Checking for {cf.magenta('all targets')}. Total targets: {cf.cyan(len(targets))}"

def starting_session():
    return f"{cf.green('[Starting Session]')}({datetime.now()})"

def has_refresh_token(target):
    return f"{cf.yellow('WARNING')}: target {cf.magenta(target.name)} has a valid {cf.coral('refresh_token')}. {cf.white('Skipping...')}"

def user_code_expired(target):
    return f"{cf.yellow('WARNING')}: target {cf.magenta(target.name)} has an expired {cf.coral('user_code')}. {cf.white('Skipping...')}"

