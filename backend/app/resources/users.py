from flask import request, jsonify
from flask_restful import Resource
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required

from backend.app.database import db
from backend.app.models import User, Role


class UserResource(Resource):
    @jwt_required()
    def get(self, user_id=None):
        if user_id:
            user = User.query.get(user_id)
            if not user:
                return {'message': 'User not found'}, 404
            return jsonify({
                'id': user.id,
                'email': user.email,
                'active': user.active,
                'roles': [role.name for role in user.roles]
            })
        users = User.query.all()
        return jsonify([{
            'id': user.id,
            'email': user.email,
            'active': user.active,
            'roles': [role.name for role in user.roles]
        } for user in users])

    def post(self):
        data = request.get_json()
        if not data.get('email') or not data.get('password'):
            return {'message': 'Email and password are required'}, 400
        user_role = Role.query.filter_by(name='user').first()
        if not user_role:
            user_role = Role(name='user', description='Primary user')
            db.session.add(user_role)
            db.session.commit()
        hashed_password = (data['password'])
        user = User(
            email=data['email'],
            password=hashed_password,
            fs_uniquifier=data['email'] ,
            roles=[user_role]# Example usage
        )
        db.session.add(user)
        db.session.commit()
        return {'message': 'User created successfully', 'id': user.id}, 201

    @jwt_required()
    def put(self, user_id):
        user = User.query.get(user_id)
        if not user:
            return {'message': 'User not found'}, 404
        data = request.get_json()
        if 'email' in data:
            user.email = data['email']
        if 'password' in data:
            user.password = generate_password_hash(data['password'])
        if 'active' in data:
            user.active = data['active']
        db.session.commit()
        return {'message': 'User updated successfully'}

    @jwt_required()
    def delete(self, user_id):
        user = User.query.get(user_id)
        if not user:
            return {'message': 'User not found'}, 404
        db.session.delete(user)
        db.session.commit()
        return {'message': 'User deleted successfully'}

#working
class LoginResource(Resource):
    def post(self):
        data = request.get_json()
        user = User.query.filter_by(email=data.get('email')).first()

        if user and (user.password == data.get('password')):  # Ensure proper password handling

            roles = [role.name for role in user.roles]  # Convert to list
            first_role = roles[0] if roles else "guest"  # Use the first role, fallback to "guest"

            access_token = create_access_token(identity=first_role)  # Store only first role in token

            return {'access_token': access_token, 'roles': roles}

        return {'message': 'Invalid credentials'}, 401

#working
class AdminUserCreation(Resource):
    def post(self):
        data = request.get_json()
        admin_role = Role.query.filter_by(name='admin').first()
        if not admin_role:
            admin_role = Role(name='admin',description='Primary Admin')
            db.session.add(admin_role)
            db.session.commit()
        user = User(
            email=data['email'],
            password=(data['password']),
            fs_uniquifier=data['email'],
            roles=[admin_role]
        )
        db.session.add(user)
        db.session.commit()
        return {'message': 'Admin user created successfully', 'id': user.id}, 201

#working
class InstructorUserCreation(Resource):
    def post(self):
        data = request.get_json()
        instructor_role = Role.query.filter_by(name='instructor').first()
        if not instructor_role:
            instructor_role = Role(name='instructor',description='Instructor of Course')
            db.session.add(instructor_role)
            db.session.commit()
        user = User(
            email=data['email'],
            password=(data['password']),
            fs_uniquifier=data['email'],
            roles=[instructor_role]
        )
        db.session.add(user)
        db.session.commit()
        return {'message': 'Instructor user created successfully', 'id': user.id}, 201
