from flask import Flask
from .models import db
from .resources import api


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    api.init_app(app)

    return app
