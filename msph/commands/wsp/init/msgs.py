def client_id_registered(client_id):
    return f"Workspace initialized with client_id: {client_id}"


def workspace_exists():
    return 'Work space already exists. Run (msph init --hard) to overwrite previous workspace.'