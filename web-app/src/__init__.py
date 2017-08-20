import os

from flask import Flask
from flask_openid import OpenID

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config.from_pyfile('settings.cfg')

oid = OpenID(app, os.path.join(basedir, 'tmp'))

from src import views
