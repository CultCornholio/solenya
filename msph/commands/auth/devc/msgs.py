def create_devc_message(user_code, device_code):
    return (
        f'user_code: {user_code}\n\n'
        f'device_code: {device_code}\n')

def create_instructions_msg():
    return ('\nInstructions:\n'
        f'1.) The user code lasts 15 minutes, get busy phishing...\n'
        f'2.) Start monitor mode to add check for an access code\n'
        f'3.) Guide a user to enter the code and accept the permissions of the application\n'
        f'4.) https://login.microsoftonline.com/common/oauth2/deviceauth\n'
    )