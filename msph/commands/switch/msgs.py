import colorful as cf

def active_target_set(target):
    msg = (
        f"{cf.green('SUCCESS')}: target {cf.magenta(target.name)} has been set to active.\n"
        "[auth]:"
    )
    if target.refresh_token:
        msg += cf.green("refresh_toked")
        if target.is_exp('refresh_token'):
            msg += cf.danger('(EXPIRED)')
        else:
            msg += f"(expires: {target.get_exp_time('refresh_token')})"
    else:
        msg += f"{cf.coral('user_code')}:{cf.cyan(target.user_code)} "
        if target.is_exp('user_code'):
            msg += cf.danger('(EXPIRED)')
        else:
            msg += f"(expires: {target.get_exp_time('user_code')})"
    return msg

def target_is_already_active(target):
    return f"Target {cf.magenta(target.name)} is already active."

def target_not_found(target_name):
    return (
        f"Target {cf.magenta(target_name)} is not registered with the WorkSpace.\n"
        f"Pass [-t] flag to create a new target or use the {cf.cyan('target')}."
    )

def target_already_exists(target):
    return f"{cf.yellow('WARNING')}: target '{target.name}' already exists in the WorkSpace. Ignoring [--target] flag."