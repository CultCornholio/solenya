def create_auth_pending():
    return ('Authorization pending...')

def create_auth_success():
    return ('Authorization Successful!, tokens saved to WorkSpace! Access token expires in 1 hour. '
        'Refresh token expires in 90 days. Run (msph auth refresh) to refresh access token.')

def create_auth_expired():
    return ('Device code expired, go back phishin')