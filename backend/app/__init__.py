from flask import Flask, jsonify
from app.models import db
from app.security import security
from app.resources import api
from werkzeug.exceptions import HTTPException
from sqlalchemy.exc import SQLAlchemyError


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    security.init_app(app)
    api.init_app(app)

    return app


app = create_app()


@app.errorhandler(HTTPException)
def handle_http_errors(e):
    return jsonify(message=e.description), e.code

@app.errorhandler(SQLAlchemyError)
def handle_database_errors(e):
    db.session.rollback()
    return jsonify(message="Database error"), 500
