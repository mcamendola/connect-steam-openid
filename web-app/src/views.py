import json
from flask import render_template, flash, redirect, session, url_for, request, g
from src import app, oid, helpers
from src.services import steam_api_service

@app.route('/')
def index():
    return render_template('index.html', user=g.user)

@app.route('/login')
@oid.loginhandler
def login():
    if g.user is not None:
        return redirect(url_for('/'))
    return oid.try_login(app.config['STEAM_OPEN_ID_URL'], ask_for=['email'])

@oid.after_login
def after_login(resp):
    session['email'] = resp.email

    user_steam_id = helpers.get_steam_id_from_identity_url(resp.identity_url)
    user_steam_data = steam_api_service.get_user_steam_data(user_steam_id)
    user = helpers.convert_steam_data_to_user(user_steam_data)
    
    session['LOGGED_USER'] = json.dumps(user_steam_data)
    
    return redirect(oid.get_next_url())

@app.before_request
def before_request():
    g.user = None
    if 'LOGGED_USER' in session:
        g.user = helpers.convert_steam_data_to_user(json.loads(session['LOGGED_USER']))