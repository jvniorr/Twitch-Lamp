import requests
import config


token_parameters = {'client_id': config.client_id, 'client_secret': config.client_secret,
                    "grant_type": 'client_credentials'}
token_data = requests.post(
    url='https://id.twitch.tv/oauth2/token', params=token_parameters)
data = token_data.json()


headers = {
    'Client-ID': config.client_id,
    'Authorization': 'Bearer ' + data['access_token']
}


def request_json(nickname):
    base_url = f'https://api.twitch.tv/helix/streams?user_login={nickname}'
    request = requests.get(url=base_url, headers=headers).json()
    return request
