def target_exists(name):
    return f"WARNING: target '{name}' already exists. Skipping..."

def target_registered(target):
    return (
        f"SUCCESS: target '{target.name}' has been registered. "
        f"(user_code: {target.user_code}, expires: {target.get_exp_time('user_code')})"
    )

def target_reset(target):
    return (
        f"SUCCESS: target '{target.name}' has been reset. "
        f"(user_code: {target.user_code}, expires: {target.get_exp_time('user_code')})"
    )

def target_not_wsp(name):
    return f"WARNING: target '{name}' is not in WorkSpace. Skipping..."

def target_is_active(target):
    return f"WARNING: target '{target.name}' is active. Can not delete active target. Skipping..."

def target_has_refresh_token(target):
    return (
        f"WARNING: target '{target.name}' has a non expired refresh_token. "
        "Add [--hard] flag to overwrite block. Skipping..."
    )

def target_deleted(target):
    return f"SUCCESS: target '{target.name}' has been deleted."

def target_list(targets):
    msg = ""
    for target in targets:
        if target.active: sub_msg = "* "
        else: sub_msg = "  "
        sub_msg += f"{target.name} [auth]"
        if target.refresh_token:
            sub_msg += f"refresh_token" 
            if target.is_exp('refresh_token'):
                sub_msg += "(EXPIRED)"
            else:
                sub_msg += f"(expires: {target.get_exp_time('refresh_token')})"
        else:
            sub_msg += f"user_code:{target.user_code}"
            if target.is_exp('user_code'):
                sub_msg += "(EXPIRED)"
            else:
                sub_msg += f"(expires: {target.get_exp_time('user_code')})"
        msg += f"{sub_msg}\n"
    msg = msg[:-1]
    return msg

def target_made_active(target):
    return (
        f"[WARNING] WorkSpace did not find an active target, Setting target '{target.name}' as active."
    )
