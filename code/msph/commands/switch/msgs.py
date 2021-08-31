def active_target_set(target):
    msg = (
        f"Target '{target.name}' has been set to active.\n"
        "\t[auth]: "
    )
    if target.refresh_token:
        msg += "refresh_toked "
        if target.is_exp('refresh_token'):
            msg += '(EXPIRED)'
        else:
            msg += f"(expires: {target.get_exp_time('refresh_token')})"
    else:
        msg += f"user_code:{target.user_code} "
        if target.is_exp('user_code'):
            msg += '(EXPIRED)'
        else:
            msg += f"(expires: {target.get_exp_time('user_code')})"
    return msg

def target_is_already_active(target):
    return f"Target '{target.name}' is already active."

def target_not_found(target_name):
    return (
        f"Target '{target_name}' is not registered with the WorkSpace.\n"
        f"Pass [-t] flag to create a new target or run 'msph target {target_name}'."
    )

def target_already_exists(target):
    return f"\nTarget '{target.name}' already exists in the WorkSpace. Ignoring [--target] flag."