from datetime import date, datetime

def ending_session(targets_authed_count, targets_expired_count):
    return (
        f"[Ending Session]({datetime.now()})\n"
        "[session summary]\n"
        f"\ttargets authed count: {targets_authed_count}\n"
        f"\ttargets expired count: {targets_expired_count}"
    )

def targets_with_tokens_count(targets, targets_no_rt):
    return (
        f"({len(targets) - len(targets_no_rt)}) targets removed due to non expired refresh token. "
        "Use 'msph auth refresh' to get a new access token.\n"
        f"\ttargets remaining: {len(targets_no_rt)}"
    )

def no_targets_need_phishing():
    return "WARNING: No phishing targets remianing."

def target_authed(target):
    return f"SUCCESS: target '{target.name}' has been successfully authenticated ({datetime.now()})!"

def user_code_expired(target):
    return f"WARNING: user code for target '{target.name}' has expired. Run 'msph target -r '{target.name}' to create a new one."

def starting_check():
    return "Starting check..."

def checking_for_active_target(target):
    return f"Checking for active target: '{target.name}', user_code: {target.user_code}"

def checking_for_all_targets(targets):
    return f"Checking for all targets. Count: {len(targets)}"

def starting_session():
    return f"[Starting Session]({datetime.now()})"