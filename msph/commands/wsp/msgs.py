import colorful as cf

def workspace_exists(app):
    return (
        f"WorkSpace at {cf.cyan(app.plugins.wsp.root_dir)} already exists.\n"
        f"Add {cf.cyan('--reset')} flag to reset WorkSpace.\n"
        f"{cf.yellow('WARNING')}: all data will be lost."
    )

def workspace_created(settings, wsp, target):
    return (
        f"{cf.green('SUCCESS')}: WorkSpace created at {cf.cyan(wsp.root_dir)}.\n"
        f"{cf.white('client_id')}: {cf.cyan(settings.client_id)}\n"
        f"{cf.white('active target')}: {cf.magenta(target.name)} [auth]:{cf.coral('user_code')}:{cf.cyan(target.user_code)} (expires at {target.get_exp_time('user_code')})"
    )

def invalid_client_id(settings):
    return (
        f"Could not get user_code for target '{settings.target_name}'.\n"
        f"Client id '{cf.cyan(settings.client_id)}'' may be invalid."
        f"Set '--verbose' flag for more detail."
    )