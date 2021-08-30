def workspace_exists(app):
    return (
        f"WorkSpace at '{app.plugins.wsp.root_dir}' already exists.\n"
        f"Run '{app.name} wsp --reset' flag to reset WorkSpace.\n"
        "WARNING: all data will be lost."
    )

def workspace_created(settings, wsp, target):
    return (
        f"WorkSpace created at {wsp.root_dir}.\n"
        f"client_id: {settings.client_id}\n"
        f"active target: {target.name} [auth]user_code:{target.user_code}(expires at {target.get_exp_time('user_code')})"
    )

def invalid_client_id(settings):
    return (
        f"Could not get user_code for target '{settings.target_name}'.\n"
        f"Client id '{settings.client_id}'' may be invalid."
        f"Set '--verbose' flag for more detail."
    )