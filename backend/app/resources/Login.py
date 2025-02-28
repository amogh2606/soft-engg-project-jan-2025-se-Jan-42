from flask import request, jsonify
from flask_restful import Resource
from flask_login import login_user, logout_user, login_required
from flask_jwt_extended import create_access_token, jwt_required
from flask_sqlalchemy.session import Session

from backend.app.models import User


from flask import request
from flask_restful import Resource
from flask_jwt_extended import create_access_token
from flask_login import login_user


class LoginResource(Resource):
    def post(self):
        data = request.json
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return {"error": "Email and password are required"}, 400

        user = User.query.filter_by(email=email).first()  # Correct way to fetch user by email

        if not user or not user.check_password(password):
            return {"error": "Invalid email or password"}, 401

        access_token = create_access_token(identity=user.id)
        return {"message": "Login successful", "access_token": access_token}, 200



class LogoutResource(Resource):
    @login_required
    def post(self):
        logout_user()
        return {"message": "Logged out successfully"}, 200


class ProtectedResource(Resource):
    @jwt_required()
    def get(self):
        return {"message": "Access granted to protected route!"}, 200
