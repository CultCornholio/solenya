def create_devc_message(user_code, device_code):
    return ('User code and device code obtained\n\n'
        f'user_code: {user_code}\n\n'
        f'device_code: {device_code}\n')

def create_instructions_msg():
    return ('Phish/Vish a user to enter the device code in the following endpoint\n\n'
        f'1.) The user code lasts 15 minutes, get busy phishing...\n'
        f'2.) Guide a user to enter the code and accept the permissions of the application\n'
        f'3.) https://login.microsoftonline.com/common/oauth2/deviceauth\n'
    )