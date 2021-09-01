import colorful as cf

def exporting_active_target(target):
    return f"Export active target: {cf.magenta(target.name)}."

def exporting_all_targets(targets):
    return f"Export {cf.magenta('all targets')}. Total targets: {cf.cyan(len(targets))}"

def saved_targets_to_file(path):
    return f"Saved target/targets to {cf.cyan(path)}"