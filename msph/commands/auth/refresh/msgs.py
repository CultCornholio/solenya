import colorful as cf

def checking_for_active_target(target):
    return f"Refreshing for active target: {cf.magenta(target.name)}, {cf.coral('user_code')}:{cf.cyan(target.user_code)}"

def checking_for_all_targets(targets):
    return f"Refreshing for {cf.magenta('all targets')}. Total targets: {cf.cyan(len(targets))}"

def no_refresh_token(target):
    return f"{cf.yellow('WARNING')}: target {cf.magenta(target.name)} does not have a valid {cf.green('refresh_token')}. {cf.white('Skipping...')}"

def could_not_get_access_token(target):
    return f"{cf.yellow('WARNING')}: could not get {cf.green('refresh_token')} for target {cf.magenta(target.name)}. {cf.white('Skipping...')}"

def access_token_success(target):
    return f"{cf.green('Access Token Refreshed')}: for target {target.name} (expires: {target.get_exp_time('access_token')})"