from flask import Flask, jsonify
from werkzeug.exceptions import HTTPException
from app.models import db
from app.resources import api


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    api.init_app(app)

    return app


app = create_app()

@app.errorhandler(HTTPException)
def handle_exceptions(e):
    return jsonify(message=e.description), e.code

