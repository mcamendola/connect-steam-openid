import re
from .models import User

def get_steam_id_from_identity_url(identity_url):
    steam_id_re = re.compile('steamcommunity.com/openid/id/(.*?)$')
    match = steam_id_re.search(identity_url)
    return match.group(1)

def convert_steam_data_to_user(steam_data):
    player = steam_data['response']['players'][0]
    return User(player['steamid'], player['personaname'])