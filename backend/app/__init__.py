from flask import Flask
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy

from backend.app.database import db
from backend.app.resources import api



def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    jwt=JWTManager(app)
    api.init_app(app)
    with app.app_context():
        db.create_all()

    return app


app = create_app()
if __name__ == '__main__':
    app.run()
