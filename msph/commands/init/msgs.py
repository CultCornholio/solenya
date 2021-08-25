def create_client_id_registered_msg(client_id):
    return f"Workspace initialized with client_id: {client_id}"


def create_workspace_exists_msg():
    return 'Work space already exists. Run (msph init --hard) to overwrite previous workspace.'