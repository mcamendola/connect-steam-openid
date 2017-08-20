import json
from src import app
from urllib.request import urlopen
from urllib.parse import urlencode, quote_plus

def get_user_steam_data(steam_id):
    parameters = {
        'key': app.config['STEAM_API_KEY'],
        'steamids': steam_id
    }
    encoded_parameters = urlencode(parameters, quote_via=quote_plus)
    url = '{}/ISteamUser/GetPlayerSummaries/{}/?{}'.format(app.config['STEAM_WEB_API_URL'], app.config['STEAM_WEB_API_VERSION'], encoded_parameters)
    
    return json.load(urlopen(url))
    