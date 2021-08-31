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
    base_url = f'streams?user_login={nickname}'
    url_follows_list = 'https://api.twitch.tv/helix/' + base_url
    request_test = requests.get(url=url_follows_list, headers=headers).json()
    return request_test
