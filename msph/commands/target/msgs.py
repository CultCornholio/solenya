import colorful as cf

def target_exists(name):
    return f"{cf.yellow('WARNING')}: target {cf.cyan(name)} already exists. {cf.white('Skipping...')}"

def target_registered(target):
    return (
        f"{cf.green('SUCCESS')}: target {cf.magenta(target.name)} has been registered. "
        f"({cf.coral('user_code')}:{cf.cyan(target.user_code)}, expires: {target.get_exp_time('user_code')})"
    )

def target_reset(target):
    return (
        f"{cf.green('SUCCESS')}: target {cf.magenta(target.name)} has been reset. "
        f"({cf.coral('user_code')}:{cf.cyan(target.user_code)}, expires: {target.get_exp_time('user_code')})"
    )

def could_not_get_user_code(settings):
    return (
        f"Could not get user_code for specified targets.\n"
        f"Client id '{cf.cyan(settings.client_id)}' may be invalid."
        "Set '--verbose' flag for more detail."
    )

def target_not_wsp(name):
    return f"{cf.yellow('WARNING')}: target {cf.magenta(name)} is not in WorkSpace. {cf.white('Skipping...')}"

def target_is_active(target):
    return f"{cf.yellow('WARNING')}: target {cf.magenta(target.name)} is active. Can not delete active target. {cf.white('Skipping...')}"

def target_has_refresh_token(target):
    return (
        f"{cf.yellow('WARNING')}: target {cf.magenta(target.name)} has a non expired refresh_token. "
        f"Add [--hard] flag to overwrite block. {cf.white('Skipping...')}"
    )

def target_deleted(target):
    return f"{cf.green('SUCCESS')}: target {cf.magenta(target.name)} has been deleted."

def target_list(targets):
    msg = ""
    for target in targets:
        if target.active: sub_msg = cf.orange("* ")
        else: sub_msg = "  "
        sub_msg += f"{cf.magenta(target.name)} [auth]:"
        if target.refresh_token:
            sub_msg += cf.green('refresh_token') 
            if target.is_exp('refresh_token'):
                sub_msg += cf.red("(EXPIRED)")
            else:
                sub_msg += f"(expires: {target.get_exp_time('refresh_token')})"
        else:
            sub_msg += f"{cf.coral('user_code')}:{cf.cyan(target.user_code)}"
            if target.is_exp('user_code'):
                sub_msg += cf.red("(EXPIRED)")
            else:
                sub_msg += f"(expires: {target.get_exp_time('user_code')})"
        msg += f"{sub_msg}\n"
    msg = msg[:-1]
    return msg

def target_made_active(target):
    return (
        f"{cf.yellow('WARNING')} WorkSpace did not find an active target, Setting target {cf.magenta(target.name)} as active."
    )
