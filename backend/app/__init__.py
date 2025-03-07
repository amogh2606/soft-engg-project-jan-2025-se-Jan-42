from flask import Flask, jsonify
from flask_cors import CORS
from app.models import db
from app.security import security
from app.resources import api
from app.seed import seed_db, store_initial_embeddings
from werkzeug.exceptions import HTTPException
from sqlalchemy.exc import SQLAlchemyError


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    security.init_app(app)
    api.init_app(app)
    
    # Configure CORS 
    CORS(app, supports_credentials=True)

    with app.app_context():
        seed_db()
        # store_initial_embeddings()

    return app


app = create_app()


# json error handlers
@app.errorhandler(HTTPException)
def handle_http_errors(e):
    return jsonify(message=e.description), e.code

@app.errorhandler(SQLAlchemyError)
def handle_database_errors(e):
    db.session.rollback()
    return jsonify(message="Database error"), 500
