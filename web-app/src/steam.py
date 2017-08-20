import re
from urllib.request import urlopen

from flask import Flask, redirect, json, g
from flask_openid import OpenID 
from redis import Redis
from urllib.parse import urlencode, quote_plus

_steam_id_re = re.compile('steamcommunity.com/openid/id/(.*?)$')

app = Flask(__name__)
app.secret_key = 'super secret key'
app.config.from_pyfile('settings.cfg')
oid = OpenID(app)
redis_server = Redis(host='redis_server', port='6379')

@app.route('/login')
@oid.loginhandler
def login():
    if redis_server.get('user_id') is not None:
        print(oid.get_next_url())
        return redirect(oid.get_next_url())

    return oid.try_login('http://steamcommunity.com/openid')

@oid.after_login
def create_or_login(resp):
    match = _steam_id_re.search(resp.identity_url)
    steam_id = match.group(1)
    
    steamdata = get_steam_userinfo(steam_id)

    redis_server.set(steam_id, steamdata)
    redis_server.set('user_id', steam_id)
    return redirect(oid.get_next_url())

@app.route("/")
def home():
    steam_id = redis_server.get('user_id')
    if steam_id is not None:
        steam_user_info = redis_server.get(steam_id.decode()).decode()
        return steam_user_info
    
    return "<a href='/login'>Login Steam</a>"


@app.before_request
def before_request():
    print('before_request')

def get_steam_userinfo(steam_id):
    options = {
        'key': app.config['STEAM_API_KEY'],
        'steamids': steam_id
    }
    url = 'http://api.steampowered.com/ISteamUser/' \
          'GetPlayerSummaries/v0001/?%s' % urlencode(options, quote_via=quote_plus)

    print('Getting steam user info url: ' + url)
    rv = json.load(urlopen(url))
    return rv['response']['players']['player'][0] or {}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

