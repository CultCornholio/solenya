def create_auth_pending():
    return ('Authorization pending...')

def create_auth_success(access_token, refresh_token, id_token):
    return ('Authorization Successful!, tokens saved to WorkSpace!')

def create_auth_expired():
    return ('Device code expired, go back phishin')